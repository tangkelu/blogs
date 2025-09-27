#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量博客生成脚本
遍历所有19个类别，为每个类别生成一篇博客
"""

import os
import json
import random
import time
import re
import math
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from openai import OpenAI
from slugify import slugify

# 配置
PROMPTS_DIR = Path("prompts/blogs_prompt_v1")
OUTPUT_BASE_DIR = Path("blogs")
GEMINI_API_KEY = "AIzaSyALnAc5TlHvjInfh1e3qpQarYAD1ePXz-U"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
DELAY_BETWEEN_REQUESTS = 5  # 秒

def get_all_categories() -> List[Path]:
    """获取所有类别目录"""
    categories = []
    for item in PROMPTS_DIR.iterdir():
        if item.is_dir() and item.name.startswith(('01-', '02-', '03-', '04-', '05-', 
                                                   '06-', '07-', '08-', '09-', '10-',
                                                   '11-', '12-', '13-', '14-', '15-',
                                                   '16-', '17-', '18-', '19-')):
            categories.append(item)
    return sorted(categories)

def load_keywords(keywords_file: Path) -> Dict:
    """加载关键词文件"""
    try:
        with open(keywords_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ 加载关键词文件失败: {keywords_file} - {e}")
        return {}

def save_keywords(keywords_file: Path, data: Dict):
    """保存关键词文件"""
    try:
        with open(keywords_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"❌ 保存关键词文件失败: {keywords_file} - {e}")

def select_keywords(keywords_data: Dict) -> Tuple[Optional[Dict], List[str]]:
    """
    选择1个主关键词和5个LSI关键词
    返回: (主关键词字典, LSI关键词列表)
    """
    # 收集所有未使用的关键词
    all_unused_keywords = []
    
    for subsection in keywords_data.get("subsections", []):
        for keyword_obj in subsection.get("keywords", []):
            if not keyword_obj.get("used", False):
                keyword_obj["subsection"] = subsection["name"]
                all_unused_keywords.append(keyword_obj)
    
    if not all_unused_keywords:
        print("❌ 没有找到未使用的关键词")
        return None, []
    
    # 随机选择主关键词
    main_keyword = random.choice(all_unused_keywords)
    
    # 从同一子类别中选择LSI关键词
    same_subsection_keywords = [
        kw for kw in all_unused_keywords 
        if kw["subsection"] == main_keyword["subsection"] and kw != main_keyword
    ]
    
    # 如果同一子类别的关键词不够，从其他子类别补充
    if len(same_subsection_keywords) < 5:
        other_keywords = [
            kw for kw in all_unused_keywords 
            if kw["subsection"] != main_keyword["subsection"]
        ]
        same_subsection_keywords.extend(other_keywords)
    
    # 选择5个LSI关键词
    lsi_count = min(5, len(same_subsection_keywords))
    lsi_keywords = random.sample(same_subsection_keywords, lsi_count) if lsi_count > 0 else []
    lsi_keyword_names = [kw["keyword"] for kw in lsi_keywords]
    
    return main_keyword, lsi_keyword_names

def get_least_used_template(templates_dir: Path, keywords_data: Dict) -> Optional[Path]:
    """根据使用次数选择最少使用的模板文件"""
    template_files = list(templates_dir.glob("*.md"))
    if not template_files:
        return None
    
    # 获取模板使用统计
    template_stats = keywords_data.get("template_usage_stats", {})
    
    # 如果没有统计数据，初始化统计数据
    if not template_stats:
        template_stats = {}
        for template_file in template_files:
            template_stats[template_file.name] = {
                "usage_count": 0,
                "last_used": None,
                "created_blogs": []
            }
        keywords_data["template_usage_stats"] = template_stats
    
    # 找到使用次数最少的模板
    min_usage_count = float('inf')
    least_used_templates = []
    
    for template_file in template_files:
        template_name = template_file.name
        usage_count = template_stats.get(template_name, {}).get("usage_count", 0)
        
        if usage_count < min_usage_count:
            min_usage_count = usage_count
            least_used_templates = [template_file]
        elif usage_count == min_usage_count:
            least_used_templates.append(template_file)
    
    # 如果有多个使用次数相同的模板，随机选择一个
    return random.choice(least_used_templates) if least_used_templates else None

def get_random_template(templates_dir: Path) -> Optional[Path]:
    """随机选择一个模板文件（保留原函数名以兼容现有代码）"""
    template_files = list(templates_dir.glob("*.md"))
    if not template_files:
        return None
    return random.choice(template_files)

def fill_template_variables(template_content: str, keyword: str, lsi_keywords: List[str]) -> str:
    """填充模板变量"""
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    # 构建tags数组
    tags = [keyword] + lsi_keywords
    tags_str = json.dumps(tags, ensure_ascii=False)
    
    # 替换变量
    filled_template = template_content.replace("{{keyword}}", keyword)
    filled_template = filled_template.replace("{{lsi}}", ", ".join(lsi_keywords))
    filled_template = filled_template.replace("{{date}}", date_str)
    filled_template = filled_template.replace("{{tags}}", tags_str)
    
    return filled_template

def generate_blog_with_gemini(prompt: str, max_retries: int = 3) -> Optional[str]:
    """使用Gemini生成博客内容"""
    for attempt in range(max_retries):
        try:
            print(f"🤖 使用 Gemini-2.5-Pro 生成博客... (尝试 {attempt + 1}/{max_retries})")
            
            client = OpenAI(
                api_key=GEMINI_API_KEY,
                base_url=GEMINI_API_URL,
            )
            
            response = client.chat.completions.create(
                model="gemini-2.5-pro",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=16000
            )
            
            result = response.choices[0].message.content.strip()
            print(f"✅ Gemini 生成成功，字符数: {len(result)}")
            return result
                
        except Exception as e:
            print(f"❌ Gemini API 调用失败 (尝试 {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 30
                print(f"⏳ 等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
            else:
                print("❌ Gemini: 所有重试都失败了")
                return None
    
    return None

def post_process_content(content: str) -> str:
    """后处理生成的内容"""
    # 移除可能的markdown代码块标记
    content = re.sub(r'^```[\w]*\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'\n```$', '', content, flags=re.MULTILINE)
    
    # 确保内容以换行符结尾
    if not content.endswith('\n'):
        content += '\n'
    
    return content

def detect_language(content: str) -> str:
    """检测内容语言"""
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', content))
    total_chars = len(content)
    
    if total_chars > 0 and chinese_chars / total_chars > 0.3:
        return "中文"
    return "英文"

def build_front_matter(content: str, keyword: str, template_name: str, lsi_keywords: List[str]) -> str:
    """构建前置元数据"""
    content = content.strip()
    
    # 如果内容已经有前置元数据，直接返回
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
    
    # 智能截断description，确保在合适位置结束
    if len(description) > 180:
        truncate_pos = 180
        # 向前查找合适的截断点
        for i in range(min(180, len(description)) - 1, max(120, 0), -1):
            if description[i] in '。，、；！？':
                truncate_pos = i + 1
                break
            elif description[i] == ' ' and i > 150:
                truncate_pos = i
                break
        # 如果没找到合适的截断点，就在180字符处截断
        if truncate_pos >= len(description):
            truncate_pos = 180
        description = description[:truncate_pos].strip()
    
    safe_description = description.replace('"', "'")

    reading_time = max(3, math.ceil(len(content.split()) / 200))
    date_str = datetime.now().strftime('%Y-%m-%d')

    # 构建tags：主关键词 + LSI关键词
    tags = [keyword] + lsi_keywords
    tags_str = ', '.join('"{}"'.format(tag) for tag in tags)

    front_matter_lines = [
        "---",
        f'title: "{safe_title}"',
        f'description: "{safe_description}"',
        f'category: "pcb"',
        f'date: "{date_str}"',
        f'featured: false',
        f'image: ""',
        f'readingTime: {reading_time}',
        f'tags: [{tags_str}]',
        "---",
        ""
    ]

    return '\n'.join(front_matter_lines) + content

def generate_filename(keyword: str, template_name: str) -> str:
    """生成文件名"""
    # 移除PCB和版本号
    keyword_clean = re.sub(r'\s*PCB\s*', ' ', keyword, flags=re.IGNORECASE).strip()
    template_clean = re.sub(r'-v\d+$', '', template_name)
    template_clean = re.sub(r'-pcb', '', template_clean, flags=re.IGNORECASE)
    
    # 生成slug
    keyword_slug = slugify(keyword_clean)
    template_slug = slugify(template_clean)
    
    return f"{keyword_slug}-{template_slug}.md"

def save_blog_to_file(content: str, filename: str) -> Path:
    """保存博客到文件"""
    # 创建日期目录
    today = datetime.now().strftime('%m%d')
    output_dir = OUTPUT_BASE_DIR / today / "cn"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 保存文件
    file_path = output_dir / filename
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return file_path

def update_template_usage(keywords_data: Dict, template_name: str, blog_filename: str):
    """更新模板使用统计"""
    template_stats = keywords_data.get("template_usage_stats", {})
    
    if template_name not in template_stats:
        template_stats[template_name] = {
            "usage_count": 0,
            "last_used": None,
            "created_blogs": []
        }
    
    # 更新使用统计
    template_stats[template_name]["usage_count"] += 1
    template_stats[template_name]["last_used"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    template_stats[template_name]["created_blogs"].append({
        "filename": blog_filename,
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    
    # 确保 template_usage_stats 存在于 keywords_data 中
    keywords_data["template_usage_stats"] = template_stats

def update_keyword_usage(keywords_data: Dict, main_keyword: str, lsi_keywords: List[str], template_name: str):
    """更新关键词使用状态（包括主关键词和LSI关键词）"""
    all_keywords = [main_keyword] + lsi_keywords
    updated_count = 0
    
    for keyword in all_keywords:
        for subsection in keywords_data.get("subsections", []):
            for keyword_obj in subsection.get("keywords", []):
                if keyword_obj["keyword"] == keyword:
                    keyword_obj["used"] = True
                    keyword_obj["template"] = template_name
                    keyword_obj["usage_date"] = datetime.now().strftime('%Y-%m-%d')
                    keyword_obj["notes"] = "Generated by batch script"
                    updated_count += 1
                    break
    
    return updated_count > 0

def process_category(category_dir: Path) -> bool:
    """处理单个类别，生成一篇博客"""
    category_name = category_dir.name
    print(f"\n🎯 处理类别: {category_name}")
    
    # 加载关键词
    keywords_file = category_dir / "keywords.json"
    if not keywords_file.exists():
        print(f"❌ 关键词文件不存在: {keywords_file}")
        return False
    
    keywords_data = load_keywords(keywords_file)
    if not keywords_data:
        return False
    
    # 选择关键词
    main_keyword, lsi_keywords = select_keywords(keywords_data)
    if not main_keyword:
        print(f"❌ 无法选择关键词")
        return False
    
    print(f"🔑 主关键词: {main_keyword['keyword']}")
    print(f"🔗 LSI关键词: {', '.join(lsi_keywords)}")
    
    # 选择模板（使用最少使用的模板）
    templates_dir = category_dir / "templates"
    template_file = get_least_used_template(templates_dir, keywords_data)
    if not template_file:
        print(f"❌ 没有找到模板文件")
        return False
    
    print(f"📝 使用模板: {template_file.name}")
    
    # 加载并填充模板
    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except Exception as e:
        print(f"❌ 读取模板失败: {e}")
        return False
    
    filled_prompt = fill_template_variables(template_content, main_keyword["keyword"], lsi_keywords)
    
    # 生成博客
    print(f"🤖 使用 Gemini-2.5-Pro 生成博客...")
    blog_content = generate_blog_with_gemini(filled_prompt)
    
    if not blog_content:
        print(f"❌ 博客生成失败")
        return False
    
    print(f"✅ 博客生成成功，字符数: {len(blog_content)}")
    
    # 后处理内容
    blog_content = post_process_content(blog_content)
    language = detect_language(blog_content)
    blog_content = build_front_matter(blog_content, main_keyword["keyword"], template_file.stem, lsi_keywords)
    
    # 生成文件名并保存
    filename = generate_filename(main_keyword["keyword"], template_file.stem)
    file_path = save_blog_to_file(blog_content, filename)
    
    print(f"✅ 博客已保存到: {file_path}")
    
    # 更新模板使用统计
    update_template_usage(keywords_data, template_file.name, filename)
    
    # 更新关键词状态
    if update_keyword_usage(keywords_data, main_keyword["keyword"], lsi_keywords, template_file.name):
        save_keywords(keywords_file, keywords_data)
        print(f"✅ 关键词状态已更新（主关键词 + {len(lsi_keywords)} 个LSI关键词）")
        print(f"✅ 模板使用统计已更新: {template_file.name}")
    
    return True

def main():
    """主函数"""
    print("=" * 80)
    print("批量PCB博客生成脚本")
    print("=" * 80)
    print(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"输出目录: {OUTPUT_BASE_DIR}")
    print("=" * 80)
    
    # 获取所有类别
    categories = get_all_categories()
    print(f"📁 找到 {len(categories)} 个类别")
    
    success_count = 0
    failed_categories = []
    
    for i, category_dir in enumerate(categories, 1):
        print(f"\n[{i}/{len(categories)}] 处理类别: {category_dir.name}")
        
        try:
            if process_category(category_dir):
                success_count += 1
                print(f"✅ 类别 {category_dir.name} 处理成功")
            else:
                failed_categories.append(category_dir.name)
                print(f"❌ 类别 {category_dir.name} 处理失败")
        except Exception as e:
            failed_categories.append(category_dir.name)
            print(f"❌ 类别 {category_dir.name} 处理异常: {e}")
        
        # 延迟5秒（除了最后一个）
        if i < len(categories):
            print(f"⏳ 等待 {DELAY_BETWEEN_REQUESTS} 秒...")
            time.sleep(DELAY_BETWEEN_REQUESTS)
    
    # 总结
    print("\n" + "=" * 80)
    print("🎉 批量生成完成！")
    print("=" * 80)
    print(f"✅ 成功生成: {success_count} 篇博客")
    print(f"❌ 失败数量: {len(failed_categories)} 个类别")
    
    if failed_categories:
        print(f"❌ 失败的类别: {', '.join(failed_categories)}")
    
    print(f"完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

if __name__ == "__main__":
    main()