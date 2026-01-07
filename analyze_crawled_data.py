#!/usr/bin/env python3
"""
分析和统计爬取的博客数据。
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import yaml

def analyze_markdown_files(base_dir="/data/top_keywords_blog"):
    """分析 markdown 文件"""
    base_path = Path(base_dir)
    
    stats = {
        'total_files': 0,
        'total_size': 0,
        'sites': defaultdict(lambda: {'count': 0, 'size': 0}),
        'avg_file_size': 0,
        'content_length': defaultdict(int),
    }
    
    markdown_files = list(base_path.glob('**/*.md'))
    stats['total_files'] = len(markdown_files)
    
    for md_file in markdown_files:
        # 跳过索引和 README
        if md_file.name in ['INDEX.md', 'README.md']:
            continue
        
        # 获取网站名
        site = md_file.parent.name
        
        # 统计文件大小
        size = md_file.stat().st_size
        stats['total_size'] += size
        stats['sites'][site]['size'] += size
        stats['sites'][site]['count'] += 1
        
        # 读取内容统计
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # 提取 frontmatter
                match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
                if match:
                    fm_text = match.group(1)
                    try:
                        fm = yaml.safe_load(fm_text)
                        if fm and 'title' in fm:
                            title = fm['title']
                        else:
                            title = md_file.stem
                    except:
                        title = md_file.stem
                else:
                    title = md_file.stem
                
                # 计算内容长度
                body_start = content.find('\n---\n', 4) + 5
                if body_start > 4:
                    body = content[body_start:]
                else:
                    body = content
                
                content_len = len(body)
                stats['content_length'][site] += content_len
        except:
            pass
    
    # 计算平均文件大小
    if stats['total_files'] > 2:  # 减去 INDEX 和 README
        stats['avg_file_size'] = stats['total_size'] // (stats['total_files'] - 2)
    
    return stats

def print_report(stats):
    """打印报告"""
    print("\n" + "="*60)
    print("爬虫数据分析报告")
    print("="*60)
    
    print(f"\n📊 全局统计")
    print("-" * 60)
    print(f"  总文件数:          {stats['total_files']} 个")
    print(f"  总数据量:          {stats['total_size'] / 1024:.2f} KB")
    print(f"  平均文件大小:      {stats['avg_file_size'] / 1024:.2f} KB")
    
    print(f"\n🌐 按网站分类统计")
    print("-" * 60)
    
    # 排序网站列表
    sorted_sites = sorted(
        stats['sites'].items(),
        key=lambda x: x[1]['count'],
        reverse=True
    )
    
    for site, site_stats in sorted_sites:
        count = site_stats['count']
        size = site_stats['size'] / 1024
        avg_size = size / count if count > 0 else 0
        content = stats['content_length'].get(site, 0) / 1024
        
        print(f"\n  {site}")
        print(f"    文件数:       {count}")
        print(f"    总大小:       {size:.2f} KB")
        print(f"    平均文件:     {avg_size:.2f} KB")
        print(f"    内容量:       {content:.2f} KB")
    
    print(f"\n{'='*60}\n")

if __name__ == "__main__":
    print("正在分析爬取的数据...")
    stats = analyze_markdown_files()
    print_report(stats)
    
    # 保存统计信息为 JSON
    import json
    stats_dict = {
        'total_files': stats['total_files'],
        'total_size_kb': stats['total_size'] / 1024,
        'avg_file_size_kb': stats['avg_file_size'] / 1024,
        'sites': {}
    }
    
    for site, site_stats in stats['sites'].items():
        stats_dict['sites'][site] = {
            'file_count': site_stats['count'],
            'size_kb': site_stats['size'] / 1024,
            'content_kb': stats['content_length'].get(site, 0) / 1024
        }
    
    # 保存到文件
    output_file = Path('/data/top_keywords_blog/stats.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(stats_dict, f, indent=2, ensure_ascii=False)
    
    print(f"✓ 统计信息已保存到: {output_file}")
