#!/usr/bin/env python3
"""
继续爬取剩余的 Excel 文件关键词对应的博客。
"""

import os
import time
import re
from pathlib import Path
from datetime import datetime
from urllib.parse import quote
import logging
import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ContinueCrawler:
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
        return re.sub(r'-organic.*', '', filename).replace('_', '.')
    
    def search_and_fetch(self, domain: str, keyword: str):
        """搜索和爬取博客"""
        search_urls = [
            f"https://{domain}/blog/?s={quote(keyword)}",
            f"https://www.{domain}/blog/?s={quote(keyword)}",
        ]
        
        for search_url in search_urls:
            try:
                r = self.session.get(search_url, timeout=8)
                if r.status_code == 200:
                    soup = BeautifulSoup(r.content, 'html.parser')
                    for link in soup.find_all('a', href=True):
                        href = link['href']
                        if any(x in href.lower() for x in ['/blog/', '/article/', '/post/', '/news/']):
                            if not href.startswith('http'):
                                href = f"https://{domain}{href}" if href.startswith('/') else f"https://www.{domain}{href}"
                            
                            # 爬取页面
                            try:
                                r2 = self.session.get(href, timeout=8)
                                if r2.status_code == 200:
                                    soup2 = BeautifulSoup(r2.content, 'html.parser')
                                    
                                    # 提取信息
                                    title = ""
                                    h1 = soup2.find('h1')
                                    if h1:
                                        title = h1.get_text().strip()[:100]
                                    if not title:
                                        title_tag = soup2.find('title')
                                        if title_tag:
                                            title = title_tag.get_text().strip()[:100]
                                    
                                    desc = ""
                                    meta = soup2.find('meta', attrs={'name': 'description'})
                                    if meta:
                                        desc = meta.get('content', '')[:200]
                                    
                                    # 清理
                                    for el in soup2.find_all(['script', 'style', 'nav', 'footer']):
                                        el.decompose()
                                    
                                    # 内容
                                    content = ""
                                    main = soup2.find('article') or soup2.find('main') or soup2.find('body')
                                    if main:
                                        paragraphs = main.find_all(['p', 'h2', 'h3', 'li'])
                                        content_lines = []
                                        for p in paragraphs[:25]:
                                            text = p.get_text().strip()
                                            if text and len(text) > 20:
                                                content_lines.append(text)
                                        content = '\n\n'.join(content_lines)
                                    
                                    if content and len(content) > 100:
                                        # 保存
                                        self.save_file(domain, keyword, {
                                            'url': href,
                                            'title': title or "Blog",
                                            'description': desc,
                                            'content': content
                                        })
                                        return True
                            except:
                                pass
            except:
                pass
        
        return False
    
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
title: "{blog_data['title']}"
description: "{blog_data['description'].replace('"', "'")}"
category: technology
date: "{datetime.now().strftime('%Y-%m-%d')}"
featured: false
tags: ["{keyword}"]
source: "{blog_data['url']}"
---

{blog_data['content']}

---

**来源:** {blog_data['url']}
"""
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md)
            
            self.saved += 1
            return True
        except:
            return False
    
    def run(self, excel_dir="/code/blogs/top_blog_keywords"):
        """主流程"""
        excel_files = sorted(Path(excel_dir).glob("*.xlsx"))
        
        # 继续从第 6 个文件开始
        for i, excel_file in enumerate(excel_files[5:20], 6):
            try:
                logger.info(f"\n[{i}/{min(20, len(excel_files))}] {excel_file.name}")
                
                domain = self.get_domain(excel_file.name)
                df = pd.read_excel(excel_file)
                
                first_col = df.columns[0]
                keywords = df[first_col].dropna().unique().tolist()[:30]
                
                for j, keyword in enumerate(keywords, 1):
                    keyword = str(keyword).strip()
                    if not keyword:
                        continue
                    
                    if self.search_and_fetch(domain, keyword):
                        logger.info(f"  [{j}/{len(keywords)}] ✓ {keyword}")
                    
                    time.sleep(0.2)
                
                time.sleep(1)
            except Exception as e:
                logger.error(f"Error: {e}")
        
        logger.info(f"\n{'='*50}")
        logger.info(f"保存文件: {self.saved}")
        logger.info(f"{'='*50}")


if __name__ == "__main__":
    crawler = ContinueCrawler()
    crawler.run()
