#!/usr/bin/env python3
"""
批量爬取所有 Excel 关键词对应的博客，仅保存内容，提高效率。
"""

import os
import json
import time
import re
from pathlib import Path
from datetime import datetime
from urllib.parse import quote
import logging
import pandas as pd
import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Optional
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SimpleBlogCrawler:
    def __init__(self, output_dir="/data/top_keywords_blog"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.session = self._setup_session()
        self.saved_count = 0
        
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
    
    def search_blog(self, domain: str, keyword: str, timeout=8) -> Optional[str]:
        """搜索博客链接"""
        search_urls = [
            f"https://{domain}/blog/?s={quote(keyword)}",
            f"https://www.{domain}/blog/?s={quote(keyword)}",
        ]
        
        for url in search_urls:
            try:
                r = self.session.get(url, timeout=timeout)
                if r.status_code == 200:
                    soup = BeautifulSoup(r.content, 'html.parser')
                    for link in soup.find_all('a', href=True):
                        href = link['href']
                        if any(x in href.lower() for x in ['/blog/', '/article/', '/post/', '/news/']):
                            if not href.startswith('http'):
                                href = f"https://{domain}{href}" if href.startswith('/') else f"https://www.{domain}{href}"
                            return href
            except:
                pass
        
        return None
    
    def fetch_blog(self, url: str, timeout=8) -> Optional[Dict]:
        """爬取博客内容"""
        try:
            r = self.session.get(url, timeout=timeout)
            if r.status_code != 200:
                return None
            
            soup = BeautifulSoup(r.content, 'html.parser')
            
            # 提取标题
            title = ""
            h1 = soup.find('h1')
            if h1:
                title = h1.get_text().strip()[:100]
            if not title:
                title_tag = soup.find('title')
                if title_tag:
                    title = title_tag.get_text().strip()[:100]
            
            # 提取描述
            desc = ""
            meta = soup.find('meta', attrs={'name': 'description'})
            if meta:
                desc = meta.get('content', '')[:200]
            
            # 清理无用元素
            for el in soup.find_all(['script', 'style', 'nav', 'footer']):
                el.decompose()
            
            # 提取内容
            content = ""
            main = soup.find('article') or soup.find('main') or soup.find('body')
            if main:
                paragraphs = main.find_all(['p', 'h2', 'h3', 'li'])
                content_lines = []
                for p in paragraphs[:25]:
                    text = p.get_text().strip()
                    if text and len(text) > 20:
                        content_lines.append(text)
                content = '\n\n'.join(content_lines)
            
            if not content or len(content) < 100:
                return None
            
            return {
                'url': url,
                'title': title or "Blog Post",
                'description': desc,
                'content': content
            }
        except:
            return None
    
    def save_file(self, domain: str, keyword: str, blog_data: Dict) -> bool:
        """保存 markdown 文件"""
        try:
            domain_dir = self.output_dir / domain
            domain_dir.mkdir(parents=True, exist_ok=True)
            
            # 生成文件名
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
            
            # 生成 markdown
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
            
            self.saved_count += 1
            return True
        except Exception as e:
            logger.error(f"Save error: {e}")
            return False
    
    def process_excel(self, excel_path: Path) -> int:
        """处理单个 Excel 文件"""
        try:
            domain = self.get_domain(excel_path.name)
            df = pd.read_excel(excel_path)
            
            first_col = df.columns[0]
            keywords = df[first_col].dropna().unique().tolist()[:30]  # 限制 30 个
            
            logger.info(f"Domain: {domain}, Keywords: {len(keywords)}")
            
            count = 0
            for i, keyword in enumerate(keywords):
                keyword = str(keyword).strip()
                if not keyword:
                    continue
                
                logger.info(f"  [{i+1}/{len(keywords)}] Keyword: {keyword}")
                
                # 搜索
                blog_url = self.search_blog(domain, keyword)
                if blog_url:
                    # 爬取
                    blog_data = self.fetch_blog(blog_url)
                    if blog_data:
                        # 保存
                        if self.save_file(domain, keyword, blog_data):
                            count += 1
                            logger.info(f"    ✓ Saved: {keyword}")
                
                time.sleep(0.3)
            
            return count
        except Exception as e:
            logger.error(f"Excel processing error: {e}")
            return 0
    
    def run(self, excel_dir="/code/blogs/top_blog_keywords"):
        """主流程"""
        excel_files = sorted(Path(excel_dir).glob("*.xlsx"))
        logger.info(f"Found {len(excel_files)} Excel files")
        
        for i, excel_file in enumerate(excel_files[:15], 1):  # 处理前 15 个文件
            logger.info(f"\n[{i}/{min(15, len(excel_files))}] Processing {excel_file.name}")
            self.process_excel(excel_file)
            time.sleep(1)
        
        logger.info(f"\n{'='*50}")
        logger.info(f"✓ 保存文件数: {self.saved_count}")
        logger.info(f"✓ 输出目录: {self.output_dir}")
        logger.info(f"{'='*50}")


if __name__ == "__main__":
    crawler = SimpleBlogCrawler()
    crawler.run()
