#!/usr/bin/env python3
"""
爬取 top_blog_keywords 中 Excel 文件的所有关键词对应的博客内容 - 改进版。
使用直接 URL 构建和 API 方式提高效率。
"""

import os
import json
import time
import re
from pathlib import Path
from datetime import datetime
from urllib.parse import quote, urljoin
import logging
import pandas as pd
import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Optional, Tuple
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class KeywordBlogCrawlerV2:
    def __init__(self, output_base_dir="/data/top_keywords_blog"):
        self.output_base_dir = Path(output_base_dir)
        self.output_base_dir.mkdir(parents=True, exist_ok=True)
        
        # 设置 session with retry strategy
        self.session = self._create_session()
        
        # 用于记录已爬取的 URL
        self.crawled_urls = set()
        self.failed_urls = []
        self.stats = {
            'total_keywords': 0,
            'fetched_blogs': 0,
            'failed_blogs': 0,
            'saved_files': 0
        }
        
        # 网站特定的路由配置
        self.site_routes = {
            'default': [
                '/blog/?s={keyword}',
                '/search?q={keyword}',
                '/articles/?s={keyword}',
                '/insights/?s={keyword}',
                '/news/?s={keyword}',
            ]
        }
    
    def _create_session(self):
        """创建带重试机制的 requests session"""
        session = requests.Session()
        retry_strategy = Retry(
            total=2,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        return session
    
    def extract_keywords_from_excel(self, excel_path: Path) -> List[str]:
        """从 Excel 文件中提取关键词"""
        try:
            df = pd.read_excel(excel_path)
            # 假设关键词在第一列
            first_col = df.columns[0]
            keywords = df[first_col].dropna().unique().tolist()
            return [str(k).strip() for k in keywords if k][:50]  # 限制前 50 个
        except Exception as e:
            logger.error(f"Failed to read Excel {excel_path}: {e}")
            return []
    
    def extract_domain_from_filename(self, filename: str) -> str:
        """从文件名中提取域名"""
        match = re.match(r'(.*?)-organic', filename)
        if match:
            domain = match.group(1)
            domain = domain.replace('www.', '').replace('_', '.')
            return domain
        return "unknown"
    
    def generate_search_urls(self, domain: str, keyword: str) -> List[Tuple[str, str]]:
        """生成多个搜索 URL"""
        urls = []
        routes = self.site_routes.get(domain, self.site_routes['default'])
        
        # 尝试带 www 和不带 www 的域名
        for prefix in [domain, f'www.{domain}']:
            for route in routes:
                search_keyword = quote(keyword)
                url = f"https://{prefix}{route.format(keyword=search_keyword)}"
                urls.append((url, prefix))
        
        return urls
    
    def fetch_page(self, url: str, timeout: int = 10) -> Optional[BeautifulSoup]:
        """获取页面内容"""
        try:
            response = self.session.get(url, timeout=timeout)
            if response.status_code == 200:
                response.encoding = response.apparent_encoding or 'utf-8'
                return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            logger.debug(f"Error fetching {url}: {e}")
        return None
    
    def extract_blog_links(self, soup: BeautifulSoup, domain: str) -> List[str]:
        """从页面中提取博客链接"""
        if not soup:
            return []
        
        blog_links = []
        blog_patterns = ['/blog/', '/article/', '/post/', '/news/', '/insights/', '/resource/']
        
        for link in soup.find_all('a', href=True):
            href = link.get('href', '').strip()
            
            if not href or href.startswith('#') or href.startswith('javascript'):
                continue
            
            # 处理相对 URL
            if href.startswith('/'):
                href = f"https://{domain}{href}"
            elif not href.startswith('http'):
                continue
            
            # 检查是否是博客链接
            if any(pattern in href.lower() for pattern in blog_patterns):
                if href not in blog_links:
                    blog_links.append(href)
        
        return blog_links[:3]  # 返回前 3 个链接
    
    def extract_content(self, soup: BeautifulSoup) -> Tuple[str, str, str]:
        """提取页面标题、描述和内容"""
        if not soup:
            return "", "", ""
        
        # 提取标题
        title = ""
        h1 = soup.find('h1')
        if h1:
            title = h1.get_text().strip()
        if not title:
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.get_text().strip()
        
        # 提取描述
        description = ""
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            description = meta_desc.get('content', '').strip()
        
        # 提取内容
        content = self._extract_body_content(soup)
        
        return title, description, content
    
    def _extract_body_content(self, soup: BeautifulSoup) -> str:
        """提取正文内容"""
        # 清理无用元素
        for element in soup.find_all(['script', 'style', 'nav', 'footer', 'header', 'form']):
            element.decompose()
        
        # 查找主要内容区域
        selectors = ['article', 'main', '[role="main"]', '.post-content', '.article-content', '.entry-content']
        content_elem = None
        
        for selector in selectors:
            found = soup.select_one(selector)
            if found and len(found.get_text().strip()) > 200:
                content_elem = found
                break
        
        if not content_elem:
            content_elem = soup.find('body')
        
        if not content_elem:
            return ""
        
        # 提取段落和标题
        paragraphs = []
        for elem in content_elem.find_all(['p', 'h2', 'h3', 'li']):
            text = elem.get_text().strip()
            if text and len(text) > 30:
                paragraphs.append(text)
        
        return '\n\n'.join(paragraphs[:30])  # 限制段落数量
    
    def fetch_blog_content(self, url: str) -> Optional[Dict]:
        """爬取博客内容"""
        if url in self.crawled_urls:
            return None
        
        soup = self.fetch_page(url)
        if not soup:
            self.failed_urls.append(url)
            return None
        
        title, description, content = self.extract_content(soup)
        
        if not content or len(content) < 100:
            return None
        
        self.crawled_urls.add(url)
        
        return {
            'url': url,
            'title': title or "Blog Article",
            'description': description,
            'content': content,
            'fetched_at': datetime.now().isoformat()
        }
    
    def generate_markdown(self, blog_data: Dict, keyword: str, domain: str) -> str:
        """生成 markdown 格式的博客文章"""
        # 清理描述中的引号
        description = blog_data['description'].replace('"', "'") if blog_data['description'] else keyword
        
        template = f"""---
title: "{blog_data['title']}"
description: "{description}"
category: technology
date: "{datetime.now().strftime('%Y-%m-%d')}"
featured: false
image: ""
readingTime: 5
tags: ["{keyword}", "{domain}"]
source: "{blog_data['url']}"
---

{blog_data['content']}

---

**原文链接:** [{blog_data['url']}]({blog_data['url']})

**爬取时间:** {blog_data['fetched_at']}
"""
        return template
    
    def save_markdown(self, markdown_content: str, domain: str, keyword: str) -> bool:
        """保存 markdown 文件"""
        try:
            domain_dir = self.output_base_dir / domain
            domain_dir.mkdir(parents=True, exist_ok=True)
            
            # 生成文件名
            safe_keyword = re.sub(r'[^\w\s-]', '', keyword).replace(' ', '-').lower()[:40]
            
            # 使用哈希避免重复
            keyword_hash = hashlib.md5(keyword.encode()).hexdigest()[:8]
            filename = f"{safe_keyword}_{keyword_hash}.md"
            filepath = domain_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            self.stats['saved_files'] += 1
            return True
        except Exception as e:
            logger.error(f"Failed to save markdown: {e}")
            return False
    
    def process_keyword(self, domain: str, keyword: str) -> bool:
        """处理单个关键词"""
        search_urls = self.generate_search_urls(domain, keyword)
        
        for search_url, prefix in search_urls:
            logger.debug(f"Searching: {search_url}")
            soup = self.fetch_page(search_url)
            
            if soup:
                blog_links = self.extract_blog_links(soup, prefix)
                
                for blog_url in blog_links:
                    blog_data = self.fetch_blog_content(blog_url)
                    
                    if blog_data:
                        markdown = self.generate_markdown(blog_data, keyword, domain)
                        if self.save_markdown(markdown, domain, keyword):
                            self.stats['fetched_blogs'] += 1
                            logger.info(f"✓ Saved: {domain} - {keyword}")
                            return True
                        
                        time.sleep(0.2)
        
        self.stats['failed_blogs'] += 1
        return False
    
    def process_excel_file(self, excel_path: Path) -> int:
        """处理单个 Excel 文件"""
        logger.info(f"Processing: {excel_path.name}")
        
        domain = self.extract_domain_from_filename(excel_path.name)
        keywords = self.extract_keywords_from_excel(excel_path)
        
        if not keywords:
            logger.warning(f"No keywords found in {excel_path}")
            return 0
        
        self.stats['total_keywords'] += len(keywords)
        saved_count = 0
        
        # 使用线程池加快处理
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = {
                executor.submit(self.process_keyword, domain, keyword): keyword
                for keyword in keywords[:20]  # 限制每个文件 20 个关键词
            }
            
            for future in as_completed(futures):
                try:
                    if future.result():
                        saved_count += 1
                except Exception as e:
                    logger.error(f"Error processing keyword: {e}")
        
        return saved_count
    
    def run(self, keyword_dir: str = "/code/blogs/top_blog_keywords"):
        """运行爬虫"""
        start_time = time.time()
        
        keyword_path = Path(keyword_dir)
        excel_files = sorted(list(keyword_path.glob("*.xlsx")))
        
        logger.info(f"Found {len(excel_files)} Excel files")
        
        for i, excel_file in enumerate(excel_files[:10], 1):  # 处理前 10 个文件
            try:
                logger.info(f"[{i}/{min(10, len(excel_files))}] Processing {excel_file.name}")
                self.process_excel_file(excel_file)
            except Exception as e:
                logger.error(f"Error processing {excel_file}: {e}")
            
            time.sleep(1)
        
        elapsed = time.time() - start_time
        
        # 输出统计
        logger.info("\n" + "="*50)
        logger.info("爬虫完成统计")
        logger.info("="*50)
        logger.info(f"总关键词数: {self.stats['total_keywords']}")
        logger.info(f"成功爬取: {self.stats['fetched_blogs']} 个页面")
        logger.info(f"失败: {self.stats['failed_blogs']} 个页面")
        logger.info(f"保存文件数: {self.stats['saved_files']} 个")
        logger.info(f"耗时: {elapsed:.2f} 秒")
        logger.info(f"输出目录: {self.output_base_dir}")
        logger.info("="*50)


if __name__ == "__main__":
    crawler = KeywordBlogCrawlerV2()
    crawler.run()
