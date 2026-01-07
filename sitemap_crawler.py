#!/usr/bin/env python3
"""
基于 Sitemap 的爬虫 - 直接从网站地图获取所有文章，然后按关键词匹配
"""

import os
import re
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin
import logging
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SitemapCrawler:
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
            f"https://www.{domain}/sitemap_index.xml",
            f"https://{domain}/sitemap_index.xml",
        ]
        
        all_urls = []
        
        for sitemap_url in sitemap_urls:
            try:
                logger.debug(f"  Fetching sitemap: {sitemap_url}")
                r = self.session.get(sitemap_url, timeout=10)
                
                if r.status_code == 200:
                    # 解析 XML
                    try:
                        root = ET.fromstring(r.content)
                        ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
                        
                        # 检查是否是索引文件
                        sitemaps = root.findall('.//sm:sitemap/sm:loc', ns)
                        if sitemaps:
                            # 这是索引，递归获取子 sitemap
                            for sitemap_elem in sitemaps:
                                sub_url = sitemap_elem.text
                                logger.debug(f"    Found sub-sitemap: {sub_url}")
                                all_urls.extend(self.fetch_sitemap_urls(sub_url))
                        else:
                            # 直接获取 URL
                            urls = root.findall('.//sm:url/sm:loc', ns)
                            for url_elem in urls:
                                all_urls.append(url_elem.text)
                    
                    except Exception as e:
                        logger.debug(f"    XML parse error: {e}")
                        continue
                    
                    logger.info(f"  ✓ Found {len(all_urls)} URLs in sitemap")
                    return all_urls
            
            except Exception as e:
                logger.debug(f"    Error: {e}")
                continue
        
        logger.info(f"  ✗ No sitemap found")
        return []
    
    def fetch_sitemap_urls(self, sitemap_url: str) -> list:
        """从单个 sitemap URL 获取所有 URL"""
        try:
            r = self.session.get(sitemap_url, timeout=10)
            if r.status_code == 200:
                root = ET.fromstring(r.content)
                ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
                urls = root.findall('.//sm:url/sm:loc', ns)
                return [url_elem.text for url_elem in urls]
        except:
            pass
        return []
    
    def filter_articles(self, urls: list, keywords: list) -> dict:
        """根据关键词和 URL 模式过滤文章"""
        articles_by_keyword = {}
        
        for keyword in keywords:
            matched = []
            keyword_lower = keyword.lower()
            
            for url in urls:
                url_lower = url.lower()
                
                # 检查 URL 中是否包含博客路径
                if not any(p in url_lower for p in ['/blog/', '/article/', '/post/', '/news/', '/insights/']):
                    continue
                
                # 检查 URL 中是否包含关键词的任何部分
                keyword_words = [w for w in keyword_lower.split() if len(w) > 2]
                match_count = sum(1 for w in keyword_words if w in url_lower)
                
                if match_count > 0:
                    matched.append(url)
            
            if matched:
                articles_by_keyword[keyword] = matched[:3]  # 每个关键词最多 3 个 URL
        
        return articles_by_keyword
    
    def fetch_article(self, url: str, keyword: str) -> dict:
        """爬取文章内容"""
        try:
            r = self.session.get(url, timeout=10)
            if r.status_code != 200:
                return None
            
            soup = BeautifulSoup(r.content, 'html.parser')
            
            # 提取标题
            title = ""
            h1 = soup.find('h1')
            if h1:
                title = h1.get_text().strip()[:150]
            if not title:
                title_tag = soup.find('title')
                if title_tag:
                    title = title_tag.get_text().strip()[:150]
            
            # 提取描述
            desc = ""
            meta = soup.find('meta', attrs={'name': 'description'})
            if meta:
                desc = meta.get('content', '')[:300]
            
            # 清理
            for el in soup.find_all(['script', 'style', 'nav', 'footer', 'form']):
                el.decompose()
            
            # 提取内容
            content = ""
            main = soup.find('article') or soup.find('main') or soup.find('body')
            if main:
                paragraphs = []
                for elem in main.find_all(['p', 'h2', 'h3', 'li']):
                    text = elem.get_text().strip()
                    if text and len(text) > 20:
                        text = re.sub(r'\s+', ' ', text)
                        paragraphs.append(text)
                content = '\n\n'.join(paragraphs[:60])
            
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
        """爬取单个域的所有关键词"""
        logger.info(f"\nCrawling: {domain}")
        
        # 获取 sitemap
        urls = self.fetch_sitemap(domain)
        if not urls:
            logger.warning(f"  No sitemap found for {domain}")
            return 0
        
        # 过滤相关文章
        articles = self.filter_articles(urls, keywords)
        logger.info(f"  Found {len(articles)} matching keywords")
        
        saved = 0
        for keyword, article_urls in articles.items():
            for article_url in article_urls:
                article = self.fetch_article(article_url, keyword)
                
                if article:
                    if self.save_file(domain, keyword, article):
                        logger.info(f"    ✓ {keyword}: {article['title'][:50]}")
                        saved += 1
                
                time.sleep(0.3)
        
        return saved
    
    def run(self, domains: list, keywords_file: str):
        """主流程"""
        # 读取所有关键词
        all_keywords = set()
        
        logger.info(f"Processing {len(domains)} domains\n")
        
        for domain in domains:
            try:
                self.crawl_domain(domain, list(all_keywords) if all_keywords else [])
            except Exception as e:
                logger.error(f"Error processing {domain}: {e}")
            
            time.sleep(1)
        
        logger.info(f"\n{'='*60}")
        logger.info(f"✓ 保存文件: {self.saved}")
        logger.info(f"{'='*60}")


if __name__ == "__main__":
    import os
    import pandas as pd
    
    # 获取所有域名和关键词
    top_keywords_dir = Path("/code/blogs/top_blog_keywords")
    excel_files = sorted(top_keywords_dir.glob("*.xlsx"))
    
    domains_and_keywords = {}
    
    for excel_file in excel_files[:10]:
        domain = re.sub(r'-organic.*', '', excel_file.name).replace('_', '.')
        df = pd.read_excel(excel_file)
        first_col = df.columns[0]
        keywords = df[first_col].dropna().unique().tolist()[:30]
        domains_and_keywords[domain] = keywords
    
    # 创建爬虫并运行
    crawler = SitemapCrawler()
    
    for domain, keywords in domains_and_keywords.items():
        crawler.crawl_domain(domain, keywords)
        time.sleep(1)
