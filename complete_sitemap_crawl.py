#!/usr/bin/env python3
"""
完整的 Sitemap 爬虫 - 处理所有 32 个网站
"""

import os
import re
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
import logging
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

class CompleteSitemapCrawler:
    def __init__(self, output_dir="/data/top_keywords_blog"):
        self.output_dir = Path(output_dir)
        self.session = self._setup_session()
        self.saved = 0
        
    def _setup_session(self):
        s = requests.Session()
        retry = Retry(total=1, backoff_factor=0.3, status_forcelist=[429, 500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retry)
        s.mount("http://", adapter)
        s.mount("https://", adapter)
        s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        return s
    
    def fetch_sitemap(self, domain: str) -> list:
        """获取网站地图中的所有 URL"""
        sitemap_urls = [
            f"https://www.{domain}/sitemap.xml",
            f"https://{domain}/sitemap.xml",
        ]
        
        all_urls = []
        
        for sitemap_url in sitemap_urls:
            try:
                r = self.session.get(sitemap_url, timeout=10)
                if r.status_code == 200:
                    root = ET.fromstring(r.content)
                    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
                    
                    # 尝试获取子 sitemap
                    sitemaps = root.findall('.//sm:sitemap/sm:loc', ns)
                    if sitemaps:
                        for sitemap_elem in sitemaps:
                            try:
                                sub_url = sitemap_elem.text
                                r2 = self.session.get(sub_url, timeout=10)
                                if r2.status_code == 200:
                                    root2 = ET.fromstring(r2.content)
                                    urls = root2.findall('.//sm:url/sm:loc', ns)
                                    all_urls.extend([u.text for u in urls])
                            except:
                                pass
                    else:
                        urls = root.findall('.//sm:url/sm:loc', ns)
                        all_urls.extend([u.text for u in urls])
                    
                    if all_urls:
                        logger.info(f"  ✓ Found {len(all_urls)} URLs")
                        return all_urls
            except Exception as e:
                logger.debug(f"  Error: {e}")
                continue
        
        logger.warning(f"  ✗ No sitemap found")
        return []
    
    def filter_articles(self, urls: list, keywords: list) -> dict:
        """根据关键词过滤文章"""
        articles = {}
        
        for keyword in keywords:
            matched = []
            keyword_lower = keyword.lower()
            
            for url in urls:
                url_lower = url.lower()
                
                # 检查是否是文章 URL
                if not any(p in url_lower for p in ['/blog/', '/article/', '/post/', '/news/', '/insights/', '/resource/']):
                    continue
                
                # 检查是否匹配关键词
                keyword_words = [w for w in keyword_lower.split() if len(w) > 2]
                if any(w in url_lower for w in keyword_words):
                    matched.append(url)
            
            if matched:
                articles[keyword] = matched[:2]  # 每个关键词最多 2 个 URL
        
        return articles
    
    def fetch_article(self, url: str) -> dict:
        """爬取文章"""
        try:
            r = self.session.get(url, timeout=10)
            if r.status_code != 200:
                return None
            
            soup = BeautifulSoup(r.content, 'html.parser')
            
            # 标题
            title = ""
            h1 = soup.find('h1')
            if h1:
                title = h1.get_text().strip()[:150]
            if not title:
                title_tag = soup.find('title')
                if title_tag:
                    title = title_tag.get_text().strip()[:150]
            
            # 描述
            desc = ""
            meta = soup.find('meta', attrs={'name': 'description'})
            if meta:
                desc = meta.get('content', '')[:300]
            
            # 清理
            for el in soup.find_all(['script', 'style', 'nav', 'footer', 'form']):
                el.decompose()
            
            # 内容
            content = ""
            main = soup.find('article') or soup.find('main') or soup.find('body')
            if main:
                paragraphs = []
                for elem in main.find_all(['p', 'h2', 'h3', 'li']):
                    text = elem.get_text().strip()
                    if text and len(text) > 20:
                        text = re.sub(r'\s+', ' ', text)
                        paragraphs.append(text)
                content = '\n\n'.join(paragraphs[:80])
            
            if not content or len(content) < 200:
                return None
            
            return {
                'url': url,
                'title': title or "Article",
                'description': desc,
                'content': content
            }
        
        except Exception as e:
            logger.debug(f"  Fetch error: {e}")
            return None
    
    def save_file(self, domain: str, keyword: str, article: dict) -> bool:
        """保存文件"""
        try:
            domain_dir = self.output_dir / domain
            domain_dir.mkdir(parents=True, exist_ok=True)
            
            safe_name = re.sub(r'[^\w\s-]', '', keyword)[:40].replace(' ', '-').lower()
            filename = f"{safe_name}.md"
            filepath = domain_dir / filename
            
            # 避免覆盖
            counter = 1
            base = filepath
            while filepath.exists():
                name, ext = os.path.splitext(base)
                filepath = Path(f"{name}_{counter}{ext}")
                counter += 1
            
            md = f"""---
title: "{article['title'].replace('"', "'")}"
description: "{article['description'].replace('"', "'")}"
category: technology
date: "{datetime.now().strftime('%Y-%m-%d')}"
featured: false
tags: ["{keyword}"]
source: "{article['url']}"
---

{article['content']}

---

**原文链接:** [{article['url']}]({article['url']})

**爬取方法:** Sitemap 爬虫

**爬取时间:** {datetime.now().isoformat()}
"""
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md)
            
            self.saved += 1
            return True
        
        except Exception as e:
            logger.error(f"Save error: {e}")
            return False
    
    def crawl_domain(self, domain: str, keywords: list) -> int:
        """爬取单个域"""
        logger.info(f"\n爬取: {domain}")
        
        # 获取 sitemap
        urls = self.fetch_sitemap(domain)
        if not urls:
            return 0
        
        # 过滤
        articles = self.filter_articles(urls, keywords)
        logger.info(f"  匹配关键词: {len(articles)} 个")
        
        saved = 0
        for keyword, article_urls in articles.items():
            for article_url in article_urls:
                article = self.fetch_article(article_url)
                
                if article:
                    if self.save_file(domain, keyword, article):
                        logger.info(f"    ✓ {keyword}")
                        saved += 1
                
                time.sleep(0.2)
        
        return saved
    
    def run(self, excel_dir="/code/blogs/top_blog_keywords"):
        """主流程"""
        excel_files = sorted(Path(excel_dir).glob("*.xlsx"))
        
        logger.info(f"处理 {len(excel_files)} 个 Excel 文件\n")
        
        total_saved = 0
        
        for i, excel_file in enumerate(excel_files, 1):
            try:
                domain = re.sub(r'-organic.*', '', excel_file.name).replace('_', '.')
                
                df = pd.read_excel(excel_file)
                first_col = df.columns[0]
                keywords = df[first_col].dropna().unique().tolist()[:25]
                
                saved = self.crawl_domain(domain, keywords)
                total_saved += saved
                
                time.sleep(1)
            
            except Exception as e:
                logger.error(f"Error: {e}")
        
        logger.info(f"\n{'='*60}")
        logger.info(f"✓ 总计保存: {total_saved} 个文件")
        logger.info(f"✓ 总数据量: {self.output_dir.stat().st_size / 1024 / 1024:.1f} MB")
        logger.info(f"{'='*60}")


if __name__ == "__main__":
    crawler = CompleteSitemapCrawler()
    crawler.run()
