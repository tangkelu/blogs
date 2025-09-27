#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PCB博客生成器 - 多模型多语言版本."""

import argparse
import json
import math
import os
import random
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional

from openai import OpenAI

# 目录配置
DATE_DIR = datetime.now().strftime("%m-%d")
BLOGS_BASE_DIR = Path("blogs")
OUTPUT_DIR = BLOGS_BASE_DIR / DATE_DIR
IMG_DIR = OUTPUT_DIR / "img"
CATEGORY_BASE_DIR = Path("prompts/blogs_prompt_v1")
USAGE_TRACKER_PATH = CATEGORY_BASE_DIR / "usage_tracker.json"

# API配置
GEMINI_API_KEY_3 = "AIzaSyDPvLeyUSDml1yWnxJVqghCuJntv-jsC_Y"
GEMINI_API_KEY_2 = "AIzaSyDNPpthbPLNonQmC8ybz6FEIuzqhHszBv8"
GEMINI_API_KEY = "AIzaSyALnAc5TlHvjInfh1e3qpQarYAD1ePXz-U"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/openai/" 
API_KEY = "sk-VdEV4UZmLtWT2Uu51Zz3zgQbLqq2X7yvoqwzAXel1Myk3b02"
API_URL = "https://www.chataiapi.com/v1"
MODELS = [
    # "deepseek-v3",
    "gemini-2.5-pro",
    # "gpt-4o",
    # "claude-sonnet-4-20250514",
]


def slugify(text: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "-", text)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-").lower()


def load_usage_tracker() -> Dict[str, Dict[str, object]]:
    if USAGE_TRACKER_PATH.exists():
        try:
            return json.loads(USAGE_TRACKER_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:  # pragma: no cover - defensive guard
            print(f"⚠️ 无法解析使用记录 {USAGE_TRACKER_PATH}: {exc}")
    return {}


def save_usage_tracker(data: Dict[str, Dict[str, object]]) -> None:
    USAGE_TRACKER_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def category_matches(filters: Optional[Iterable[str]], category_id: str, folder_name: str, title: str) -> bool:
    if not filters:
        return True
    lower_folder = folder_name.lower()
    lower_title = title.lower()
    for item in filters:
        token = item.lower()
        if token == category_id.lower():
            return True
        if token in lower_folder or token in lower_title:
            return True
    return False


def load_categories(filters: Optional[List[str]] = None) -> List[Dict[str, object]]:
    categories: List[Dict[str, object]] = []
    for path in sorted(CATEGORY_BASE_DIR.iterdir()):
        if not path.is_dir():
            continue
        if not re.match(r"^\d{2}-", path.name):
            continue

        keywords_path = path / "keywords.json"
        if not keywords_path.exists():
            print(f"⚠️ 缺少关键词配置: {keywords_path}")
            continue

        with keywords_path.open(encoding="utf-8") as fp:
            payload = json.load(fp)

        category_id = f"{int(payload['section_number']):02d}"
        category_title = payload['section_title']

        if not category_matches(filters, category_id, path.name, category_title):
            continue

        templates_dir = path / "templates"
        templates = sorted(templates_dir.glob("*.md")) if templates_dir.exists() else []
        if not templates:
            print(f"⚠️ 类别 {path.name} 缺少模板文件，请在 {templates_dir} 下添加模板。")

        categories.append(
            {
                "id": category_id,
                "dir": path,
                "title": category_title,
                "subsections": payload.get("subsections", []),
                "templates": templates,
            }
        )

    return categories


def build_prompt(category_title: str, subsection: str, keyword: str, related_keywords: List[str], template_content: str) -> str:
    related_section = ", ".join(related_keywords)
    header = (
        "## Blogging Task Context\n"
        f"- Primary keyword: {keyword}\n"
        f"- Category: {category_title}\n"
        f"- Subtopic: {subsection}\n"
        f"- Related keywords: {related_section}\n\n"
    )
    return f"{header}{template_content.strip()}\n"


def build_generation_queue(
    categories: List[Dict[str, object]],
    usage_tracker: Dict[str, Dict[str, object]],
    limit: Optional[int] = None,
) -> List[Dict[str, object]]:
    combinations: List[Dict[str, object]] = []
    template_cache: Dict[Path, str] = {}

    for category in categories:
        category_dir: Path = category["dir"]
        category_title: str = category["title"]
        category_id: str = category["id"]

        for template_path in category["templates"]:
            template_rel = template_path.relative_to(CATEGORY_BASE_DIR).as_posix()
            template_slug = slugify(template_path.stem) or "template"
            if template_path not in template_cache:
                template_cache[template_path] = template_path.read_text(encoding="utf-8")
            template_content = template_cache[template_path]

            for subsection in category["subsections"]:
                subsection_name = subsection.get("name", "")
                keywords = subsection.get("keywords", [])
                for keyword in keywords:
                    usage_key = f"{category_dir.name}::{template_rel}::{keyword}"
                    usage_info = usage_tracker.get(usage_key, {})
                    combinations.append(
                        {
                            "category": category,
                            "template_path": template_path,
                            "template_rel": template_rel,
                            "template_slug": template_slug,
                            "template_content": template_content,
                            "subsection_name": subsection_name,
                            "subsection_keywords": keywords,
                            "keyword": keyword,
                            "usage_key": usage_key,
                            "usage_count": usage_info.get("count", 0),
                            "last_used": usage_info.get("last_used"),
                        }
                    )

    combinations.sort(
        key=lambda item: (
            item["usage_count"],
            item["last_used"] or "",
            item["category"]["id"],
            item["template_slug"],
            item["keyword"],
        )
    )

    grouped: Dict[int, List[Dict[str, object]]] = {}
    for combo in combinations:
        grouped.setdefault(combo["usage_count"], []).append(combo)

    ordered: List[Dict[str, object]] = []
    for usage in sorted(grouped.keys()):
        group = grouped[usage]
        random.shuffle(group)
        ordered.extend(group)

    if limit is not None:
        limit = max(limit, 0)
        ordered = ordered[:limit]

    combinations = ordered

    for combo in combinations:
        combo["prompt_content"] = build_prompt(
            combo["category"]["title"],
            combo["subsection_name"],
            combo["keyword"],
            combo["subsection_keywords"],
            combo["template_content"],
        )
        keyword_slug = slugify(combo["keyword"]) or "keyword"
        combo["output_filename"] = f"{keyword_slug}-{combo['template_slug']}.md"
        combo["prompt_label"] = f"{combo['category']['dir'].name}:{combo['keyword']}[{combo['template_slug']}]"

    return combinations


def mark_usage(
    usage_tracker: Dict[str, Dict[str, object]],
    usage_key: str,
    output_filename: str,
) -> None:
    record = usage_tracker.setdefault(usage_key, {})
    record["count"] = int(record.get("count", 0)) + 1
    record["last_used"] = datetime.now().isoformat(timespec="seconds")
    history: List[Dict[str, str]] = record.setdefault("history", [])
    history.append(
        {
            "timestamp": record["last_used"],
            "output": output_filename,
        }
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate PCB blogs from structured prompts.")
    parser.add_argument(
        "--limit",
        type=int,
        default=1,
        help="Number of keyword/template combinations to process in this run.",
    )
    parser.add_argument(
        "--categories",
        nargs="*",
        help="Filter categories by编号或名称片段，例如 01 datacenter。",
    )
    parser.add_argument(
        "--date-dir",
        help="Override output date folder (default: today's MM-DD).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview selected combinations without calling any API.",
    )
    return parser.parse_args()


def _ensure_style_color(match, color="#1B2838"):
    prefix, styles = match.groups()
    parts = [part.strip() for part in styles.split(';') if part.strip()]
    has_color = any(part.lower().startswith('color:') for part in parts)
    if not has_color:
        parts.append(f'color: {color}')
    style_str = '; '.join(parts)
    if style_str and not style_str.endswith(';'):
        style_str += ';'
    return f"{prefix}{style_str}\""


def post_process_content(content: str) -> str:
    if not content:
        return content

    content = content.replace('\r\n', '\n')

    lines = content.split('\n')
    header_idx = next((i for i, line in enumerate(lines) if line.strip().startswith('#')), None)
    if header_idx is not None and header_idx > 0:
        content = '\n'.join(lines[header_idx:])

    content = re.sub(r'^(#+)\s*H\d:\s*', r'\1 ', content, flags=re.MULTILINE)

    for pattern in [r'(<div[^>]*style=")(.*?)"', r'(<table[^>]*style=")(.*?)"', r'(<th[^>]*style=")(.*?)"', r'(<td[^>]*style=")(.*?)"']:
        content = re.sub(pattern, _ensure_style_color, content)

    content = re.sub(r'<img[^>]*?>', '', content)
    content = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', content)

    content = re.sub(r'\((?:Get|Explore|Request|Contact)[^()\n]{0,80}\)', '', content)

    content = re.sub(r'\n{3,}', '\n\n', content)
    return content.strip()


def detect_language(content: str) -> str:
    if re.search(r'[\u4e00-\u9fff]', content):
        return 'zh'
    return 'en'


def insert_quote_button(content: str, language: str, keyword: str) -> str:
    button_templates = {
        'en': (
            'https://hilpcb.com/en/quote',
            f'Get {keyword} Quote'
        ),
        'zh': (
            'https://hilpcb.com/cn/quote',
            f'获取{keyword}报价'
        ),
    }
    url, text = button_templates.get(language, button_templates['en'])
    button_html = (
        f"<center><a href=\"{url}\" style=\"display:inline-block;background:#4CAF50;color:#fff;"
        "padding:10px 20px;font-size:16px;border-radius:5px;text-decoration:none;margin:20px 20px;\">"
        f"{text}</a></center>"
    )

    h2_matches = list(re.finditer(r'^##\s+.*$', content, flags=re.MULTILINE))
    if len(h2_matches) < 2:
        return content + '\n\n' + button_html

    second_h2 = h2_matches[1]
    insert_pos = second_h2.end()
    return content[:insert_pos] + '\n\n' + button_html + '\n' + content[insert_pos:]


def build_front_matter(content: str, keyword: str, language: str) -> str:
    stripped = content.lstrip()
    if stripped.startswith('---'):
        return content

    title_match = re.search(r'^#\s+(.*)', content, flags=re.MULTILINE)
    title = title_match.group(1).strip() if title_match else keyword
    safe_title = title.replace('"', "'")

    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', content) if p.strip()]
    description = paragraphs[1] if paragraphs and paragraphs[0].startswith('#') and len(paragraphs) > 1 else paragraphs[0] if paragraphs else f"Insights on {keyword}."
    description = re.sub(r'<[^>]+>', '', description)
    description = re.sub(r'\s+', ' ', description).strip()
    description = description[:200]
    safe_description = description.replace('"', "'")

    reading_time = max(3, math.ceil(len(content.split()) / 200))
    date_str = datetime.now().strftime('%Y-%m-%d')

    tags = [keyword]
    tags_str = ', '.join('"{}"'.format(tag) for tag in tags)
    front_matter_lines = [
        '---',
        f'title: "{safe_title}"',
        f'description: "{safe_description}"',
        'category: pcb',
        f'date: "{date_str}"',
        'featured: false',
        'image: ""',
        f'readingTime: {reading_time}',
        f'tags: [{tags_str}]',
        '---',
        '',
    ]

    return '\n'.join(front_matter_lines) + content


def generate_blog_with_openai(model, prompt, language=None):
    """
    使用OpenAI兼容API生成博客文章
    
    Args:
        model (str): 模型名称
        prompt (str): 提示词
        language (str): 语言标识 (zh/en) - 此参数将被忽略，始终输出英文
    
    Returns:
        str: 生成的博客内容，失败时返回None
    """
    max_retries = 3
    for attempt in range(max_retries):
        try:
            print(f"Generating English blog post using {model}... (Attempt {attempt + 1}/{max_retries})")
            
            # 根据模型选择API配置
            if model == "gemini-2.5-pro":
                # 使用Gemini API配置
                client = OpenAI(
                    api_key=GEMINI_API_KEY,
                    base_url=GEMINI_API_URL,
                )
            else:
                # 使用默认API配置
                client = OpenAI(
                    api_key=API_KEY,
                    base_url=API_URL,
                )
            
            # 生成内容
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=16000
            )
            
            result = response.choices[0].message.content.strip()
            print(f"✓ {model} (English) generation successful, character count: {len(result)}")
            return result
            
        except Exception as e:
            print(f"✗ {model} API call failed (Attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 30  # 递增等待时间
                print(f"等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
            else:
                print(f"✗ {model}: All retries failed.")
                return None
    
    return None

def save_blog_to_file(content, filename):
    """
    将博客内容保存到文件

    Args:
        content (str): 博客内容
        filename (str): 文件名
    """
    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        filepath = OUTPUT_DIR / filename

        with filepath.open('w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ 博客已保存到: {filepath}")
        return str(filepath)
    except Exception as e:
        print(f"✗ 保存文件失败: {e}")
        return None

    

def main():
    """主函数 - 根据结构化配置生成PCB博客。"""

    args = parse_args()

    global DATE_DIR, OUTPUT_DIR, IMG_DIR
    if args.date_dir:
        sanitized = args.date_dir.strip().replace('\\', '-').replace('/', '-')
        if sanitized:
            DATE_DIR = sanitized
    OUTPUT_DIR = BLOGS_BASE_DIR / DATE_DIR
    IMG_DIR = OUTPUT_DIR / 'img'

    categories = load_categories(args.categories)
    if not categories:
        print('错误: 未找到符合条件的提示词分类，请检查目录结构或过滤条件。')
        return

    usage_tracker = load_usage_tracker()
    queue = build_generation_queue(categories, usage_tracker, args.limit)

    if not queue:
        print('⚠️ 没有可用的关键词/模板组合可生成，请确认模板与关键词配置。')
        return

    print('=' * 80)
    print('PCB博客生成器 - 多模型多语言版本')
    print('=' * 80)
    print(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f'输出目录: {OUTPUT_DIR}')
    print(f'目标分类: {len(categories)} 个；本次任务: {len(queue)} 个关键词组合')
    print(f"模型列表: {', '.join(MODELS)}")
    print('=' * 80)

    for combo in queue:
        print(f" - {combo['prompt_label']}")

    if args.dry_run:
        print('\n🔍 Dry run 模式：仅预览待处理组合，不调用API。')
        return

    results = []
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    usage_modified = False

    for model_index, model in enumerate(MODELS):
        print(f'\n🚀 开始处理模型: {model}')
        print('-' * 60)

        for combo in queue:
            keyword_slug = slugify(combo['keyword']) or 'keyword'
            template_slug = combo['template_slug']
            filename = combo['output_filename']
            filepath = OUTPUT_DIR / filename
            prompt_label = combo['prompt_label']

            if filepath.exists():
                print(f'\n⏭️ Skipping ({prompt_label}) - file already exists: {filename}')
                results.append({
                    'model': model,
                    'category': combo['category']['dir'].name,
                    'keyword': combo['keyword'],
                    'template': combo['template_rel'],
                    'success': True,
                    'char_count': 0,
                    'image_count': 0,
                    'filename': filename,
                    'skipped': True,
                    'usage_key': combo['usage_key'],
                })
                continue

            print(f'\n📝 Generating blog ({prompt_label})...')
            content = generate_blog_with_openai(model, combo['prompt_content'])

            result_entry = {
                'model': model,
                'category': combo['category']['dir'].name,
                'keyword': combo['keyword'],
                'template': combo['template_rel'],
                'success': content is not None,
                'char_count': len(content) if content else 0,
                'image_count': 0,
                'filename': None,
                'skipped': False,
                'usage_key': combo['usage_key'],
            }

            if content:
                content = post_process_content(content)
                content = re.sub(
                    r'!\[.*?\]\(placeholder\)(?: <!-- AI生成建议：.*? -->)?',
                    '',
                    content,
                )
                language = detect_language(content)
                content = insert_quote_button(content, language, combo['keyword'])
                content = build_front_matter(content, combo['keyword'], language)
                result_entry['image_count'] = 0

                save_blog_to_file(content, filename)
                result_entry['filename'] = filename

                if not combo.get('_usage_marked'):
                    mark_usage(usage_tracker, combo['usage_key'], filename)
                    usage_modified = True
                    combo['_usage_marked'] = True

            results.append(result_entry)

            if model == 'gemini-2.5-pro':
                print('⏳ Waiting 1 minute for gemini-2.5-pro to avoid rate limit...')
                time.sleep(60)

        print(f'✅ 模型 {model} 处理完成')

        if model_index != len(MODELS) - 1:
            print('⏳ 等待3秒后处理下一个模型...')
            time.sleep(3)

    if usage_modified:
        save_usage_tracker(usage_tracker)
        print(f'💾 已更新使用记录: {USAGE_TRACKER_PATH}')

    print('\n' + '=' * 80)
    print('🎉 所有博客生成完成！')
    print('=' * 80)

    report_lines = ['# PCB博客生成报告\n']
    report_lines.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report_lines.append(f'输出目录: {OUTPUT_DIR}\n')
    report_lines.append(f"模型: {', '.join(MODELS)}\n")
    report_lines.append(f'任务数: {len(queue)} 个关键词组合\n')

    report_lines.append('## 任务详情\n')
    report_lines.append('| Category | Keyword | Template | Model | Status | Characters | Images | Output |\n')
    report_lines.append('|---|---|---|---|---|---|---|---|\n')

    for result in results:
        status = 'Skipped' if result.get('skipped') else ('Success' if result['success'] else 'Failed')
        report_lines.append(
            '| {category} | {keyword} | {template} | {model} | {status} | {chars} | {images} | {output} |'.format(
                category=result['category'],
                keyword=result['keyword'],
                template=result['template'],
                model=result['model'],
                status=status,
                chars=result.get('char_count', 0),
                images=result.get('image_count', 0),
                output=result.get('filename', '-'),
            )
        )

    total_attempts = len(results)
    success_count = sum(1 for r in results if r['success'] and not r.get('skipped'))
    skip_count = sum(1 for r in results if r.get('skipped'))
    failure_count = total_attempts - success_count - skip_count
    success_rate = (success_count / total_attempts * 100) if total_attempts else 0

    report_lines.append('\n## 总结\n')
    report_lines.append(f'- 成功: {success_count}')
    report_lines.append(f'- 失败: {failure_count}')
    report_lines.append(f'- 跳过: {skip_count}')
    report_lines.append(f'- 成功率: {success_rate:.1f}%\n')

    report_filename = f'generation_report_{timestamp}.md'
    report_path = save_blog_to_file('\n'.join(report_lines), report_filename)

    if report_path:
        print(f'✅ 对比报告已保存: {report_filename}')
    else:
        print('❌ 保存对比报告失败')

    print('\n📈 最终统计:')
    print(f'   成功: {success_count}')
    print(f'   失败: {failure_count}')
    print(f'   跳过: {skip_count}')
    print(f'   成功率: {success_rate:.1f}%')

    successful_results = [r for r in results if r['success'] and not r.get('skipped')]
    if successful_results:
        print('\n✅ 成功生成的文件:')
        for result in successful_results:
            print(
                f"   - {result['filename']} (Keyword: {result['keyword']}, Template: {result['template']}, Model: {result['model']}, Chars: {result['char_count']})"
            )

    failed_results = [r for r in results if not r['success'] and not r.get('skipped')]
    if failed_results:
        print('\n❌ 失败的任务:')
        for result in failed_results:
            print(
                f"   - {result['keyword']} (Template: {result['template']}, Model: {result['model']})"
            )

    print('\n🎯 建议: 查看生成的博客与报告文件，按需发布并跟踪使用记录。')

if __name__ == "__main__":
    main()
