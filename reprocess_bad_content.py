#!/usr/bin/env python3
"""
重新爬取内容不匹配的文件。
使用改进的搜索策略和内容验证。
"""

import re
import json
import time
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

class ReprocessCrawler:
    def __init__(self):
        self.session = self._setup_session()
        self.reprocessed = 0
        
    def _setup_session(self):
        s = requests.Session()
        retry = Retry(total=1, backoff_factor=0.3, status_forcelist=[429, 500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retry)
        s.mount("http://", adapter)
        s.mount("https://", adapter)
        s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        return s
    
    def check_content_relevance(self, content: str, keyword: str) -> float:
        """检查内容与关键词的相关性 (0-1)"""
        content_lower = content.lower()
        keyword_lower = keyword.lower()
        
        keyword_words = [w for w in keyword_lower.split() if len(w) > 2]
        if not keyword_words:
            return 0.5
        
        match_count = sum(1 for w in keyword_words if w in content_lower)
        return match_count / len(keyword_words)
    
    def search_and_fetch(self, domain: str, keyword: str, max_attempts=3) -> dict:
        """搜索和爬取相关内容"""
        
        # 多个搜索策略
        search_strategies = [
            f"https://www.{domain}/blog/?s={quote(keyword)}",
            f"https://{domain}/blog/?s={quote(keyword)}",
            f"https://www.{domain}/?s={quote(keyword)}",
            f"https://{domain}/?s={quote(keyword)}",
        ]
        
        best_result = None
        best_relevance = 0
        
        for search_url in search_strategies:
            try:
                logger.debug(f"    Searching: {search_url}")
                r = self.session.get(search_url, timeout=8)
                
                if r.status_code != 200:
                    continue
                
                soup = BeautifulSoup(r.content, 'html.parser')
                
                # 查找所有链接并评分
                links_with_scores = []
                
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    link_text = link.get_text().lower()
                    
                    # 跳过外部链接、锚点等
                    if not href or href.startswith('#') or href.startswith('javascript'):
                        continue
                    
                    # 处理相对 URL
                    if href.startswith('/'):
                        if domain in href:
                            continue
                        href = f"https://www.{domain}{href}"
                    elif not href.startswith('http'):
                        continue
                    
                    # 评分：链接文本中包含关键词
                    text_score = 0
                    for word in keyword.lower().split():
                        if len(word) > 2 and word in link_text:
                            text_score += 1
                    
                    # 评分：链接 URL 中有博客或文章路径
                    url_score = 0
                    if any(p in href.lower() for p in ['/blog/', '/article/', '/post/', '/news/', '/insights/']):
                        url_score = 10
                    
                    total_score = text_score * 5 + url_score
                    
                    if total_score > 0 or url_score > 0:
                        links_with_scores.append((href, total_score, link_text))
                
                # 按分数排序
                links_with_scores.sort(key=lambda x: x[1], reverse=True)
                
                # 尝试爬取前 3 个最相关的链接
                for href, score, text in links_with_scores[:5]:
                    try:
                        logger.debug(f"      Fetching: {text[:40]}... (score: {score})")
                        r2 = self.session.get(href, timeout=8)
                        
                        if r2.status_code != 200:
                            continue
                        
                        soup2 = BeautifulSoup(r2.content, 'html.parser')
                        
                        # 提取标题
                        title = ""
                        h1 = soup2.find('h1')
                        if h1:
                            title = h1.get_text().strip()[:150]
                        if not title:
                            title_tag = soup2.find('title')
                            if title_tag:
                                title = title_tag.get_text().strip()[:150]
                        
                        # 提取描述
                        desc = ""
                        meta = soup2.find('meta', attrs={'name': 'description'})
                        if meta:
                            desc = meta.get('content', '')[:300]
                        
                        # 清理
                        for el in soup2.find_all(['script', 'style', 'nav', 'footer', 'form']):
                            el.decompose()
                        
                        # 提取内容
                        content = ""
                        main = soup2.find('article') or soup2.find('main') or soup2.find('body')
                        if main:
                            paragraphs = []
                            for elem in main.find_all(['p', 'h2', 'h3', 'li']):
                                text = elem.get_text().strip()
                                if text and len(text) > 20:
                                    text = re.sub(r'\s+', ' ', text)
                                    paragraphs.append(text)
                            content = '\n\n'.join(paragraphs[:60])
                        
                        if not content or len(content) < 200:
                            continue
                        
                        # 检查相关性
                        relevance = self.check_content_relevance(content, keyword)
                        logger.debug(f"      Relevance: {relevance:.1%}, Length: {len(content)} chars")
                        
                        if relevance > best_relevance:
                            best_relevance = relevance
                            best_result = {
                                'url': href,
                                'title': title or "Article",
                                'description': desc,
                                'content': content,
                                'relevance': relevance
                            }
                        
                        if relevance > 0.5:  # 如果相关性足够高，停止搜索
                            break
                    
                    except Exception as e:
                        logger.debug(f"      Error: {e}")
                        continue
                    
                    time.sleep(0.2)
                
                # 如果找到结果，返回
                if best_result and best_result['relevance'] > 0.3:
                    logger.info(f"    ✓ Found: {best_result['title'][:50]}... (relevance: {best_result['relevance']:.1%})")
                    return best_result
                
            except Exception as e:
                logger.debug(f"    Search error: {e}")
                continue
            
            time.sleep(0.5)
        
        return None
    
    def reprocess_bad_files(self, validation_report: str = "/data/top_keywords_blog/validation_report.json"):
        """重新处理不匹配的文件"""
        
        try:
            with open(validation_report, 'r', encoding='utf-8') as f:
                report = json.load(f)
        except:
            logger.error("Cannot load validation report")
            return
        
        mismatched_files = report['problems']['mismatched']
        logger.info(f"Found {len(mismatched_files)} mismatched files\n")
        
        updated_count = 0
        
        for i, item in enumerate(mismatched_files[:50], 1):  # 限制处理 50 个
            file_path = Path(item['file'])
            keyword = item['keyword']
            domain = file_path.parent.name
            
            logger.info(f"[{i}/{min(50, len(mismatched_files))}] {file_path.name}")
            
            # 搜索和爬取新内容
            result = self.search_and_fetch(domain, keyword)
            
            if result and result['relevance'] > 0.3:
                # 保存新内容
                md = f"""---
title: "{result['title'].replace('"', "'")}"
description: "{result['description'].replace('"', "'")}"
category: technology
date: "{datetime.now().strftime('%Y-%m-%d')}"
featured: false
tags: ["{keyword}"]
source: "{result['url']}"
---

{result['content']}

---

**原文链接:** [{result['url']}]({result['url']})

**相关性:** {result['relevance']:.1%}

**更新时间:** {datetime.now().isoformat()}
"""
                
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(md)
                    updated_count += 1
                    logger.info(f"  ✓ Updated")
                except Exception as e:
                    logger.error(f"  ✗ Save error: {e}")
            else:
                logger.info(f"  ✗ No relevant content found")
            
            time.sleep(0.5)
        
        logger.info(f"\n{'='*60}")
        logger.info(f"✓ 更新文件: {updated_count} 个")
        logger.info(f"{'='*60}")


if __name__ == "__main__":
    crawler = ReprocessCrawler()
    crawler.reprocess_bad_files()
