#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PCB博客生成测试脚本 - 单关键词测试版本."""

import json
import math
import random
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from openai import OpenAI

# 配置
KEYWORDS_PATH = Path("prompts/blogs_prompt_v1/01-DataCenter-ServerPCB/keywords.json")
TEMPLATE_PATH = Path("prompts/blogs_prompt_v1/01-DataCenter-ServerPCB/templates/datacenter-server-pcb-v1.md")
OUTPUT_DIR = Path("blogs/test")

# API配置
GEMINI_API_KEY = "AIzaSyALnAc5TlHvjInfh1e3qpQarYAD1ePXz-U"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"


def slugify(text: str) -> str:
    """将文本转换为URL友好的slug格式"""
    slug = re.sub(r"[^A-Za-z0-9]+", "-", text)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-").lower()


def load_keywords() -> Dict:
    """加载关键词配置文件"""
    try:
        with KEYWORDS_PATH.open(encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ 无法加载关键词文件: {e}")
        return {}


def save_keywords(data: Dict) -> None:
    """保存关键词配置文件"""
    try:
        with KEYWORDS_PATH.open('w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 关键词状态已更新: {KEYWORDS_PATH}")
    except Exception as e:
        print(f"❌ 保存关键词文件失败: {e}")


def load_template() -> str:
    """加载模板文件"""
    try:
        return TEMPLATE_PATH.read_text(encoding="utf-8")
    except Exception as e:
        print(f"❌ 无法加载模板文件: {e}")
        return ""


def select_unused_keyword(keywords_data: Dict) -> Optional[Dict]:
    """选择一个未使用的关键词"""
    unused_keywords = []
    
    for subsection in keywords_data.get("subsections", []):
        subsection_name = subsection.get("name", "")
        keywords = subsection.get("keywords", [])
        
        for keyword_obj in keywords:
            if isinstance(keyword_obj, dict) and not keyword_obj.get("used", False):
                unused_keywords.append({
                    "keyword": keyword_obj.get("keyword", ""),
                    "subsection": subsection_name,
                    "subsection_keywords": keywords,
                    "keyword_obj": keyword_obj
                })
    
    if not unused_keywords:
        print("⚠️ 没有找到未使用的关键词")
        return None
    
    # 随机选择一个未使用的关键词
    selected = random.choice(unused_keywords)
    print(f"🎯 选择的主关键词: {selected['keyword']} (来自: {selected['subsection']})")
    return selected


def get_lsi_keywords(selected_keyword: Dict, count: int = 4) -> List[str]:
    """从同一子类中获取LSI关键词"""
    main_keyword = selected_keyword["keyword"]
    subsection_keywords = selected_keyword["subsection_keywords"]
    
    # 获取同一子类中的其他关键词
    other_keywords = []
    for keyword_obj in subsection_keywords:
        if isinstance(keyword_obj, dict):
            keyword = keyword_obj.get("keyword", "")
            if keyword != main_keyword and keyword:
                other_keywords.append(keyword)
    
    # 随机选择指定数量的LSI关键词
    if len(other_keywords) <= count:
        lsi_keywords = other_keywords
    else:
        lsi_keywords = random.sample(other_keywords, count)
    
    print(f"🔗 选择的LSI关键词: {', '.join(lsi_keywords)}")
    return lsi_keywords


def fill_template_variables(template_content: str, keyword: str, lsi_keywords: List[str]) -> str:
    """填充模板变量"""
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # 创建标签列表
    tags = [keyword] + lsi_keywords
    tags_str = ', '.join(f'"{tag}"' for tag in tags)
    
    # 替换模板变量
    filled_template = template_content.replace("{{keyword}}", keyword)
    filled_template = filled_template.replace("{{lsi}}", ", ".join(lsi_keywords))
    filled_template = filled_template.replace("{{date}}", current_date)
    filled_template = filled_template.replace("{{tags}}", f"[{tags_str}]")
    
    print(f"📝 模板变量已填充:")
    print(f"   - keyword: {keyword}")
    print(f"   - lsi: {', '.join(lsi_keywords)}")
    print(f"   - date: {current_date}")
    print(f"   - tags: [{tags_str}]")
    
    return filled_template


def generate_blog_with_gemini(prompt: str) -> Optional[str]:
    """使用Gemini生成博客文章"""
    max_retries = 3
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
            print(f"❌ Gemini API 调用失败 (尝试 {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 30
                print(f"⏳ 等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
            else:
                print("❌ Gemini: 所有重试都失败了")
                return None
    
    return None


def post_process_content(content: str) -> str:
    """后处理博客内容"""
    if not content:
        return content

    # 标准化换行符
    content = content.replace('\r\n', '\n')

    # 移除开头的非标题内容
    lines = content.split('\n')
    header_idx = next((i for i, line in enumerate(lines) if line.strip().startswith('#')), None)
    if header_idx is not None and header_idx > 0:
        content = '\n'.join(lines[header_idx:])

    # 清理标题格式
    content = re.sub(r'^(#+)\s*H\d:\s*', r'\1 ', content, flags=re.MULTILINE)

    # 确保样式有颜色
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

    for pattern in [r'(<div[^>]*style=")(.*?)"', r'(<table[^>]*style=")(.*?)"', r'(<th[^>]*style=")(.*?)"', r'(<td[^>]*style=")(.*?)"']:
        content = re.sub(pattern, _ensure_style_color, content)

    # 移除图片
    content = re.sub(r'<img[^>]*?>', '', content)
    content = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', content)

    # 移除推广文本
    content = re.sub(r'\((?:Get|Explore|Request|Contact)[^()\n]{0,80}\)', '', content)

    # 清理多余换行
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content.strip()


def detect_language(content: str) -> str:
    """检测内容语言"""
    if re.search(r'[\u4e00-\u9fff]', content):
        return 'zh'
    return 'en'


def insert_quote_button(content: str, language: str, keyword: str) -> str:
    """插入报价按钮"""
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


def build_front_matter(content, keyword, template_name, lsi_keywords=None):
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
        # 在180字符附近找到最后一个句号、逗号或空格
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
    tags = [keyword]
    if lsi_keywords:
        # 将LSI关键词字符串分割并添加到tags中
        lsi_list = [kw.strip() for kw in lsi_keywords.split(',') if kw.strip()]
        tags.extend(lsi_list)
    
    tags_str = ', '.join('"{}"'.format(tag) for tag in tags)
    front_matter_lines = [
        '---',
        f'title: "{safe_title}"',
        f'description: "{safe_description}"',
        'category: "pcb"',
        f'date: "{date_str}"',
        'featured: false',
        'image: ""',
        f'readingTime: {reading_time}',
        f'tags: [{tags_str}]',
        '---',
        '',
    ]

    return '\n'.join(front_matter_lines) + content


def save_blog_to_file(content: str, filename: str) -> Optional[str]:
    """保存博客到文件"""
    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        filepath = OUTPUT_DIR / filename

        with filepath.open('w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ 博客已保存到: {filepath}")
        return str(filepath)
    except Exception as e:
        print(f"❌ 保存文件失败: {e}")
        return None


def update_keyword_status(keywords_data: Dict, selected_keyword: Dict, template_name: str) -> None:
    """更新关键词使用状态"""
    keyword_obj = selected_keyword["keyword_obj"]
    keyword_obj["used"] = True
    keyword_obj["template"] = template_name
    keyword_obj["usage_date"] = datetime.now().strftime('%Y-%m-%d')
    keyword_obj["notes"] = f"Generated by test script using {template_name}"
    
    print(f"✅ 关键词状态已更新:")
    print(f"   - used: True")
    print(f"   - template: {template_name}")
    print(f"   - usage_date: {keyword_obj['usage_date']}")


def main():
    """主函数"""
    print("=" * 80)
    print("PCB博客生成测试脚本")
    print("=" * 80)
    print(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"关键词文件: {KEYWORDS_PATH}")
    print(f"模板文件: {TEMPLATE_PATH}")
    print(f"输出目录: {OUTPUT_DIR}")
    print("=" * 80)
    
    # 1. 加载关键词和模板
    keywords_data = load_keywords()
    if not keywords_data:
        return
    
    template_content = load_template()
    if not template_content:
        return
    
    # 2. 选择未使用的关键词
    selected_keyword = select_unused_keyword(keywords_data)
    if not selected_keyword:
        return
    
    # 3. 获取LSI关键词
    lsi_keywords = get_lsi_keywords(selected_keyword, count=4)
    
    # 4. 填充模板变量
    filled_prompt = fill_template_variables(template_content, selected_keyword["keyword"], lsi_keywords)
    
    # 5. 生成博客
    print("\n" + "-" * 60)
    print("开始生成博客...")
    print("-" * 60)
    
    blog_content = generate_blog_with_gemini(filled_prompt)
    if not blog_content:
        print("❌ 博客生成失败")
        return
    
    # 6. 后处理内容
    blog_content = post_process_content(blog_content)
    language = detect_language(blog_content)
    blog_content = insert_quote_button(blog_content, language, selected_keyword["keyword"])
    # 将LSI关键词列表转换为字符串传入
    lsi_keywords_str = ", ".join(lsi_keywords) if lsi_keywords else None
    blog_content = build_front_matter(blog_content, selected_keyword["keyword"], TEMPLATE_PATH.stem, lsi_keywords_str)
    
    # 7. 保存博客
    keyword_slug = slugify(selected_keyword["keyword"])
    template_slug = slugify(TEMPLATE_PATH.stem)
    filename = f"{keyword_slug}-{template_slug}.md"
    
    saved_path = save_blog_to_file(blog_content, filename)
    if not saved_path:
        print("❌ 博客保存失败")
        return
    
    # 8. 更新关键词状态
    template_name = TEMPLATE_PATH.name
    update_keyword_status(keywords_data, selected_keyword, template_name)
    save_keywords(keywords_data)
    
    print("\n" + "=" * 80)
    print("🎉 博客生成测试完成！")
    print("=" * 80)
    print(f"✅ 主关键词: {selected_keyword['keyword']}")
    print(f"✅ LSI关键词: {', '.join(lsi_keywords)}")
    print(f"✅ 使用模板: {template_name}")
    print(f"✅ 博客文件: {filename}")
    print(f"✅ 字符数: {len(blog_content)}")
    print(f"✅ 语言: {'中文' if language == 'zh' else '英文'}")


if __name__ == "__main__":
    main()