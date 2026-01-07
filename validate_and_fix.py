#!/usr/bin/env python3
"""
验证爬取的内容，检查标题和内容是否匹配关键词。
"""

import re
import json
from pathlib import Path
from collections import defaultdict

def validate_markdown_files(base_dir="/data/top_keywords_blog"):
    """验证 markdown 文件内容"""
    base_path = Path(base_dir)
    
    issues = {
        'mismatched': [],  # 标题和内容不匹配关键词
        'too_short': [],   # 内容太短
        'no_content': [],  # 没有实际内容
        'valid': []        # 有效的文件
    }
    
    for md_file in base_path.glob('**/*.md'):
        # 跳过 README 和 INDEX
        if md_file.name in ['README.md', 'INDEX.md']:
            continue
        
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取文件名中的关键词
            keyword = md_file.stem.replace('_', ' ').lower()
            keyword_words = [w for w in keyword.split() if len(w) > 2]
            
            # 提取标题
            title_match = re.search(r'^title:\s*"([^"]*)"', content, re.MULTILINE)
            title = title_match.group(1).lower() if title_match else ""
            
            # 提取主要内容
            body_start = content.find('\n---\n', 4)
            if body_start > 0:
                body = content[body_start+5:].lower()
            else:
                body = content.lower()
            
            # 移除 URL 和 markdown 符号
            body = re.sub(r'https?://[^\s]+', '', body)
            body = re.sub(r'[#*`\[\]()]+', ' ', body)
            
            # 统计内容长度
            body_length = len(body.split())
            
            # 检查匹配度
            matched_keywords = sum(1 for w in keyword_words if w in title or w in body)
            match_ratio = matched_keywords / len(keyword_words) if keyword_words else 0
            
            # 分类
            if body_length < 100:
                issues['too_short'].append({
                    'file': str(md_file),
                    'keyword': keyword,
                    'length': body_length,
                    'title': title
                })
            elif match_ratio < 0.3 and len(keyword_words) > 0:
                issues['mismatched'].append({
                    'file': str(md_file),
                    'keyword': keyword,
                    'title': title,
                    'match_ratio': match_ratio
                })
            elif body_length < 50:
                issues['no_content'].append({
                    'file': str(md_file),
                    'keyword': keyword
                })
            else:
                issues['valid'].append({
                    'file': str(md_file),
                    'keyword': keyword,
                    'length': body_length,
                    'title': title
                })
        
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
    
    return issues

def print_report(issues):
    """打印验证报告"""
    print("\n" + "="*70)
    print("爬取内容验证报告")
    print("="*70)
    
    total = sum(len(v) for v in issues.values())
    
    print(f"\n📊 总体统计")
    print("-" * 70)
    print(f"  有效文件:        {len(issues['valid'])} 个")
    print(f"  内容太短:        {len(issues['too_short'])} 个")
    print(f"  标题内容不匹配:   {len(issues['mismatched'])} 个")
    print(f"  无实际内容:      {len(issues['no_content'])} 个")
    print(f"  总计:           {total} 个")
    
    # 显示问题文件
    if issues['mismatched']:
        print(f"\n⚠️  标题内容不匹配的文件 ({len(issues['mismatched'])} 个)")
        print("-" * 70)
        for item in issues['mismatched'][:10]:
            print(f"  {Path(item['file']).name}")
            print(f"    关键词: {item['keyword']}")
            print(f"    标题:   {item['title'][:60]}...")
            print(f"    匹配度: {item['match_ratio']:.1%}")
    
    if issues['too_short']:
        print(f"\n⚠️  内容太短的文件 ({len(issues['too_short'])} 个)")
        print("-" * 70)
        for item in issues['too_short'][:10]:
            print(f"  {Path(item['file']).name}")
            print(f"    关键词: {item['keyword']}")
            print(f"    字数:   {item['length']} 个单词")
    
    if issues['no_content']:
        print(f"\n⚠️  无实际内容的文件 ({len(issues['no_content'])} 个)")
        print("-" * 70)
        for item in issues['no_content'][:10]:
            print(f"  {Path(item['file']).name}")
            print(f"    关键词: {item['keyword']}")
    
    # 有效文件统计
    print(f"\n✅ 有效文件示例 ({len(issues['valid'])} 个)")
    print("-" * 70)
    for item in issues['valid'][:5]:
        print(f"  {Path(item['file']).name}")
        print(f"    关键词: {item['keyword']}")
        print(f"    字数:   {item['length']} 个单词")
    
    print("\n" + "="*70 + "\n")
    
    # 保存详细报告
    report = {
        'summary': {
            'valid': len(issues['valid']),
            'too_short': len(issues['too_short']),
            'mismatched': len(issues['mismatched']),
            'no_content': len(issues['no_content']),
            'total': total
        },
        'problems': {
            'mismatched': [
                {
                    'file': i['file'],
                    'keyword': i['keyword'],
                    'match_ratio': i['match_ratio']
                }
                for i in issues['mismatched']
            ],
            'too_short': [
                {
                    'file': i['file'],
                    'keyword': i['keyword'],
                    'word_count': i['length']
                }
                for i in issues['too_short']
            ]
        }
    }
    
    report_file = Path('/data/top_keywords_blog/validation_report.json')
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"✓ 详细报告已保存到: {report_file}")

if __name__ == "__main__":
    print("正在验证爬取的内容...")
    issues = validate_markdown_files()
    print_report(issues)
