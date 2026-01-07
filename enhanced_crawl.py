#!/usr/bin/env python3
"""
增强版爬虫 - 支持更完整的内容提取，包括图片、表格等
"""

import os
import time
import re
from pathlib import Path
from datetime import datetime
from urllib.parse import quote, urljoin
import logging
import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EnhancedBlogCrawler:
    def __init__(self, output_dir="/data/top_keywords_blog"):
        self.output_dir = Path(output_dir)
        self.session = self._setup_session()
        self.saved = 0
        
    def _setup_session(self):
        """设置 session"""
        s = requests.Session()
        retry = Retry(total=1, backoff_factor=0.3, status_forcelist=[429, 500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retry)
        s.mount("http://", adapter)
        s.mount("https://", adapter)
        s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        return s
    
    def get_domain(self, filename: str) -> str:
        """从文件名提取域名"""
        return re.sub(r'-organic.*', '', filename).replace('_', '.')
    
    def search_blog(self, domain: str, keyword: str, timeout=8):
        """搜索博客链接"""
        search_urls = [
            f"https://{domain}/blog/?s={quote(keyword)}",
            f"https://www.{domain}/blog/?s={quote(keyword)}",
            f"https://www.{domain}/search?q={quote(keyword)}",
        ]
        
        for url in search_urls:
            try:
                r = self.session.get(url, timeout=timeout)
                if r.status_code == 200:
                    soup = BeautifulSoup(r.content, 'html.parser')
                    
                    # 寻找包含关键词的链接
                    links_found = []
                    for link in soup.find_all('a', href=True):
                        href = link['href']
                        text = link.get_text().lower()
                        
                        # 优先选择标题中包含关键词的链接
                        if keyword.lower() in text or any(k in text for k in keyword.lower().split()):
                            if any(x in href.lower() for x in ['/blog/', '/article/', '/post/', '/news/']):
                                if not href.startswith('http'):
                                    href = f"https://{domain}{href}" if href.startswith('/') else f"https://www.{domain}{href}"
                                links_found.append((href, text, 1))  # 优先级 1
                    
                    # 备选：其他博客链接
                    if not links_found:
                        for link in soup.find_all('a', href=True):
                            href = link['href']
                            if any(x in href.lower() for x in ['/blog/', '/article/', '/post/', '/news/']):
                                if not href.startswith('http'):
                                    href = f"https://{domain}{href}" if href.startswith('/') else f"https://www.{domain}{href}"
                                links_found.append((href, link.get_text(), 0))  # 优先级 0
                    
                    # 排序返回优先级高的
                    links_found.sort(key=lambda x: x[2], reverse=True)
                    return [link[0] for link in links_found[:5]]
            except:
                pass
        
        return []
    
    def fetch_blog(self, url: str, keyword: str, timeout=10):
        """爬取博客内容（增强版）"""
        try:
            r = self.session.get(url, timeout=timeout)
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
            
            # 清理无用元素
            for el in soup.find_all(['script', 'style', 'nav', 'footer', 'form', 'button']):
                el.decompose()
            
            # 提取内容（增强版）
            content = ""
            main = soup.find('article') or soup.find('main') or soup.find('body')
            if main:
                paragraphs = []
                
                # 提取所有文本块
                for elem in main.find_all(['p', 'h2', 'h3', 'h4', 'li', 'pre', 'blockquote']):
                    text = elem.get_text().strip()
                    if text and len(text) > 15:
                        # 清理过多空白
                        text = re.sub(r'\s+', ' ', text)
                        paragraphs.append(text)
                
                # 提取表格
                for table in main.find_all('table'):
                    table_text = self._extract_table(table)
                    if table_text:
                        paragraphs.append(table_text)
                
                content = '\n\n'.join(paragraphs[:50])  # 增加到 50 个段落
            
            # 检查内容相关性
            if content:
                content_lower = content.lower()
                keyword_lower = keyword.lower()
                
                # 如果内容中不包含任何关键词词汇，降低匹配度
                keyword_words = [w for w in keyword_lower.split() if len(w) > 2]
                match_count = sum(1 for w in keyword_words if w in content_lower)
                
                # 如果关键词匹配度太低，返回 None
                if len(keyword_words) > 0 and match_count == 0:
                    logger.debug(f"  Content relevance check failed for keyword: {keyword}")
                    return None
            
            if not content or len(content) < 200:  # 增加最小字数要求
                return None
            
            return {
                'url': url,
                'title': title or "Blog Post",
                'description': desc,
                'content': content,
                'keyword': keyword
            }
        except Exception as e:
            logger.debug(f"Fetch error: {e}")
            return None
    
    def _extract_table(self, table) -> str:
        """提取表格内容"""
        try:
            rows = []
            for tr in table.find_all('tr'):
                cols = []
                for td in tr.find_all(['td', 'th']):
                    text = td.get_text().strip()
                    cols.append(text)
                if cols:
                    rows.append(' | '.join(cols))
            return '\n'.join(rows)
        except:
            return ""
    
    def save_file(self, domain: str, keyword: str, blog_data: dict) -> bool:
        """保存文件"""
        try:
            domain_dir = self.output_dir / domain
            domain_dir.mkdir(parents=True, exist_ok=True)
            
            safe_name = re.sub(r'[^\w\s-]', '', keyword)[:40].replace(' ', '-').lower()
            filename = f"{safe_name}.md"
            filepath = domain_dir / filename
            
            counter = 1
            base = filepath
            while filepath.exists():
                name, ext = os.path.splitext(base)
                filepath = Path(f"{name}_{counter}{ext}")
                counter += 1
            
            md = f"""---
title: "{blog_data['title'].replace('"', "'")}"
description: "{blog_data['description'].replace('"', "'")}"
category: technology
date: "{datetime.now().strftime('%Y-%m-%d')}"
featured: false
tags: ["{keyword}"]
source: "{blog_data['url']}"
---

{blog_data['content']}

---

**原文链接:** [{blog_data['url']}]({blog_data['url']})

**关键词:** {keyword}

**爬取时间:** {datetime.now().isoformat()}
"""
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md)
            
            self.saved += 1
            return True
        except Exception as e:
            logger.error(f"Save error: {e}")
            return False
    
    def process_keyword(self, domain: str, keyword: str) -> bool:
        """处理单个关键词"""
        logger.info(f"  Processing: {keyword}")
        
        # 搜索
        search_urls = self.search_blog(domain, keyword)
        if not search_urls:
            logger.debug(f"    No search results found")
            return False
        
        # 尝试多个搜索结果
        for i, blog_url in enumerate(search_urls):
            blog_data = self.fetch_blog(blog_url, keyword)
            
            if blog_data:
                if self.save_file(domain, keyword, blog_data):
                    logger.info(f"    ✓ Saved from: {blog_url[:80]}")
                    return True
            
            time.sleep(0.2)
        
        logger.debug(f"    No suitable content found")
        return False
    
    def run(self, excel_dir="/code/blogs/top_blog_keywords", start_file=0, max_files=10):
        """主流程"""
        excel_files = sorted(Path(excel_dir).glob("*.xlsx"))
        
        logger.info(f"Found {len(excel_files)} Excel files\n")
        
        for i, excel_file in enumerate(excel_files[start_file:start_file+max_files], start_file+1):
            try:
                logger.info(f"[{i}] {excel_file.name}")
                
                domain = self.get_domain(excel_file.name)
                df = pd.read_excel(excel_file)
                
                first_col = df.columns[0]
                keywords = df[first_col].dropna().unique().tolist()[:30]
                
                for keyword in keywords:
                    keyword = str(keyword).strip()
                    if not keyword:
                        continue
                    
                    self.process_keyword(domain, keyword)
                    time.sleep(0.3)
                
                time.sleep(1)
            except Exception as e:
                logger.error(f"File error: {e}")
        
        logger.info(f"\n{'='*50}")
        logger.info(f"✓ 新增保存文件: {self.saved}")
        logger.info(f"✓ 输出目录: {self.output_dir}")
        logger.info(f"{'='*50}")


if __name__ == "__main__":
    crawler = EnhancedBlogCrawler()
    # 从第 6 个文件开始继续爬取
    crawler.run(start_file=5, max_files=15)
