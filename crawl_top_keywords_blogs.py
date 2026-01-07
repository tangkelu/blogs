#!/usr/bin/env python3
"""
爬取 top_blog_keywords 中 Excel 文件的所有关键词对应的博客内容。
将内容保存为 markdown 格式到 /data/top_keywords_blog 目录。
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
from typing import Dict, List, Optional
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class KeywordBlogCrawler:
    def __init__(self, output_base_dir="/data/top_keywords_blog"):
        self.output_base_dir = Path(output_base_dir)
        self.output_base_dir.mkdir(parents=True, exist_ok=True)
        
        # 设置 session with retry strategy
        self.session = self._create_session()
        
        # 用于记录已爬取的 URL
        self.crawled_urls = set()
        self.failed_urls = []
        
    def _create_session(self):
        """创建带重试机制的 requests session"""
        session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        return session
    
    def extract_keywords_from_excel(self, excel_path: Path) -> List[str]:
        """从 Excel 文件中提取关键词"""
        try:
            df = pd.read_excel(excel_path)
            # 假设关键词在 'Keyword' 或 'keyword' 列
            for col in df.columns:
                if 'keyword' in col.lower():
                    keywords = df[col].dropna().unique().tolist()
                    return [str(k).strip() for k in keywords if k]
            
            # 如果没找到 keyword 列，返回第一列的数据
            first_col = df.columns[0]
            keywords = df[first_col].dropna().unique().tolist()
            return [str(k).strip() for k in keywords if k]
        except Exception as e:
            logger.error(f"Failed to read Excel {excel_path}: {e}")
            return []
    
    def extract_domain_from_filename(self, filename: str) -> str:
        """从文件名中提取域名"""
        # 格式: domain-organic.Positions-us-*.xlsx
        match = re.match(r'(.*?)-organic', filename)
        if match:
            domain = match.group(1)
            # 处理特殊情况
            domain = domain.replace('www.', '')
            return domain
        return "unknown"
    
    def search_blog_on_site(self, domain: str, keyword: str) -> Optional[str]:
        """在网站上搜索关键词相关的博客"""
        # 构建搜索 URL
        urls_to_try = [
            f"https://{domain}/search?q={quote(keyword)}",
            f"https://www.{domain}/search?q={quote(keyword)}",
            f"https://{domain}/blog/?s={quote(keyword)}",
            f"https://www.{domain}/blog/?s={quote(keyword)}",
        ]
        
        for url in urls_to_try:
            try:
                logger.info(f"Trying to fetch from: {url}")
                response = self.session.get(url, timeout=10)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    # 查找博客文章链接
                    blog_url = self._extract_blog_url(soup, domain)
                    if blog_url:
                        return blog_url
                
                time.sleep(0.5)  # 礼貌延迟
            except Exception as e:
                logger.debug(f"Error fetching {url}: {e}")
                continue
        
        return None
    
    def _extract_blog_url(self, soup: BeautifulSoup, domain: str) -> Optional[str]:
        """从搜索结果页面中提取博客 URL"""
        # 查找常见的链接模式
        for link in soup.find_all('a', href=True):
            href = link.get('href', '')
            
            # 确保是当前域名的链接
            if domain not in href and not href.startswith('/'):
                continue
            
            # 查找可能是博客文章的链接
            if any(pattern in href.lower() for pattern in ['/blog/', '/article/', '/post/', '/news/', '/insights/']):
                if href.startswith('/'):
                    return f"https://{domain}{href}" if domain not in domain else f"https://www.{domain}{href}"
                return href
        
        return None
    
    def fetch_blog_content(self, url: str) -> Optional[Dict]:
        """爬取博客内容"""
        if url in self.crawled_urls:
            return None
        
        try:
            logger.info(f"Fetching blog from: {url}")
            response = self.session.get(url, timeout=15)
            response.encoding = 'utf-8'
            
            if response.status_code != 200:
                logger.warning(f"Failed to fetch {url}, status code: {response.status_code}")
                self.failed_urls.append(url)
                return None
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 提取标题
            title = self._extract_title(soup)
            
            # 提取描述
            description = self._extract_description(soup)
            
            # 提取主要内容
            content = self._extract_content(soup)
            
            if not content:
                logger.warning(f"No content found for {url}")
                return None
            
            self.crawled_urls.add(url)
            
            return {
                'url': url,
                'title': title,
                'description': description,
                'content': content,
                'fetched_at': datetime.now().isoformat()
            }
        
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            self.failed_urls.append(url)
            return None
    
    def _extract_title(self, soup: BeautifulSoup) -> str:
        """提取页面标题"""
        # 尝试多种标题获取方式
        title = soup.find('h1')
        if title:
            return title.get_text().strip()
        
        title_tag = soup.find('title')
        if title_tag:
            return title_tag.get_text().strip()
        
        return "Untitled"
    
    def _extract_description(self, soup: BeautifulSoup) -> str:
        """提取描述"""
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            return meta_desc.get('content', '').strip()
        
        meta_og_desc = soup.find('meta', attrs={'property': 'og:description'})
        if meta_og_desc:
            return meta_og_desc.get('content', '').strip()
        
        return ""
    
    def _extract_content(self, soup: BeautifulSoup) -> str:
        """提取主要文章内容"""
        # 移除不需要的元素
        for element in soup.find_all(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()
        
        # 尝试多种内容选择器
        selectors = [
            'article',
            'main',
            '[role="main"]',
            '.post-content',
            '.article-content',
            '.entry-content',
            '.content'
        ]
        
        content_elem = None
        for selector in selectors:
            content_elem = soup.select_one(selector)
            if content_elem:
                break
        
        if not content_elem:
            # 回退到 body
            content_elem = soup.find('body')
        
        if not content_elem:
            return ""
        
        # 提取文本
        paragraphs = content_elem.find_all(['p', 'h2', 'h3', 'h4', 'ul', 'ol'])
        content_lines = []
        
        for para in paragraphs:
            text = para.get_text().strip()
            if text and len(text) > 20:  # 过滤过短的文本
                content_lines.append(text)
        
        return '\n\n'.join(content_lines)
    
    def generate_markdown(self, blog_data: Dict, keyword: str, domain: str) -> str:
        """生成 markdown 格式的博客文章"""
        template = f"""---
title: "{blog_data['title']}"
description: "{blog_data['description']}"
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
    
    def save_markdown(self, markdown_content: str, domain: str, keyword: str):
        """保存 markdown 文件"""
        # 创建目录
        domain_dir = self.output_base_dir / domain
        domain_dir.mkdir(parents=True, exist_ok=True)
        
        # 生成文件名
        safe_keyword = re.sub(r'[^\w\s-]', '', keyword).replace(' ', '-').lower()[:50]
        filename = f"{safe_keyword}.md"
        filepath = domain_dir / filename
        
        # 避免覆盖现有文件
        counter = 1
        base_filepath = filepath
        while filepath.exists():
            name, ext = os.path.splitext(base_filepath)
            filepath = Path(f"{name}_{counter}{ext}")
            counter += 1
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            logger.info(f"Saved: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"Failed to save {filepath}: {e}")
            return None
    
    def process_excel_file(self, excel_path: Path):
        """处理单个 Excel 文件"""
        logger.info(f"Processing: {excel_path}")
        
        domain = self.extract_domain_from_filename(excel_path.name)
        keywords = self.extract_keywords_from_excel(excel_path)
        
        logger.info(f"Domain: {domain}, Keywords count: {len(keywords)}")
        
        if not keywords:
            logger.warning(f"No keywords found in {excel_path}")
            return
        
        # 处理前 10 个关键词（可根据需要调整）
        for i, keyword in enumerate(keywords[:10]):
            logger.info(f"Processing keyword {i+1}/{len(keywords[:10])}: {keyword}")
            
            # 搜索博客
            blog_url = self.search_blog_on_site(domain, keyword)
            
            if blog_url:
                # 爬取博客内容
                blog_data = self.fetch_blog_content(blog_url)
                
                if blog_data:
                    # 生成 markdown
                    markdown = self.generate_markdown(blog_data, keyword, domain)
                    
                    # 保存文件
                    self.save_markdown(markdown, domain, keyword)
            
            # 礼貌延迟
            time.sleep(1)
    
    def run(self, keyword_dir: str = "/code/blogs/top_blog_keywords"):
        """运行爬虫"""
        keyword_path = Path(keyword_dir)
        excel_files = list(keyword_path.glob("*.xlsx"))
        
        logger.info(f"Found {len(excel_files)} Excel files")
        
        for excel_file in excel_files[:5]:  # 先处理前 5 个文件以测试
            try:
                self.process_excel_file(excel_file)
            except Exception as e:
                logger.error(f"Error processing {excel_file}: {e}")
            
            time.sleep(2)  # 文件间延迟
        
        # 输出统计
        logger.info(f"\n=== 爬虫完成统计 ===")
        logger.info(f"成功爬取: {len(self.crawled_urls)} 个页面")
        logger.info(f"失败: {len(self.failed_urls)} 个页面")
        logger.info(f"输出目录: {self.output_base_dir}")


if __name__ == "__main__":
    crawler = KeywordBlogCrawler()
    crawler.run()
