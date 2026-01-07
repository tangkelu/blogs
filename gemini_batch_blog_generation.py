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
from typing import Dict, List, Optional, Tuple#!/usr/bin/env python3
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
from urllib.parse import urlparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from openai import OpenAI
from slugify import slugify

# 配置
PROMPTS_DIR = Path("prompts/blogs_prompt_v3")
OUTPUT_BASE_DIR = Path("blogs")
# 站点 sitemap 路径（用于避免 /blog/slug 冲突）
SITEMAP_FILE = Path("/code/hileap/frontend/public/sitemap.xml")
#GEMINI_API_KEY_2 = "AIzaSyDNPpthbPLNonQmC8ybz6FEIuzqhHszBv8"
#GEMINI_API_KEY = "AIzaSyALnAc5TlHvjInfh1e3qpQarYAD1ePXz-U"
GEMINI_API_LIST = [
    "AIzaSyC8qD06o2aAYGphYqLq5WaeubiQYhXoqmo"
#    "AIzaSyDQCvOvFvqUl8-OmtWD9lIE4T5IMGfJInk",
#    "AIzaSyADTG0Da6X1kcgoQKGwi92AjQc6GCBNINY",
#    "AIzaSyBAH2LcqAuZsMgsPg3zoL-cU-N2M2LjLiQ",
#    "AIzaSyCzxZFiuS2fcht4oCmsoewqjCnMXpCpNjY",
#    "AIzaSyDEITF24Eppy2mezrWGh_knluLvrNTa3Ug",
#    "AIzaSyA5zziFytE2ev3_ITkkoAGRCYFq7wj0CG4",
#    "AIzaSyA-rmJt5JI5oocz4P9GU4e37c460HEuZqY",
#    "AIzaSyBr9yLHZAhA1im7yYLI9rGX_bbHpzO0PpI",
    "AIzaSyALnAc5TlHvjInfh1e3qpQarYAD1ePXz-U"
]
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
DELAY_BETWEEN_REQUESTS = 12  # 秒
RATE_LIMIT_WINDOW_SECONDS = 70
MAX_CALLS_PER_KEY_PER_WINDOW = 2
MAX_DAILY_CALLS_PER_KEY = 50
GEMINI_API_KEYS = GEMINI_API_LIST


class GeminiRateLimiter:
    """简单的Gemini API多Key速率限制器"""

    def __init__(self, api_keys: List[str]):
        self.api_keys = [key for key in api_keys if key]
        if not self.api_keys:
            raise ValueError("未配置任何Gemini API Key")
        self.usage_window: Dict[str, List[float]] = {key: [] for key in self.api_keys}
        self.daily_usage: Dict[str, int] = {key: 0 for key in self.api_keys}
        self.max_calls_per_window = MAX_CALLS_PER_KEY_PER_WINDOW * len(self.api_keys)
        self._rr_index = 0
        self.alias_map = {key: f"API-{idx + 1}" for idx, key in enumerate(self.api_keys)}

    def _cleanup(self, now: float):
        """移除时间窗口之外的调用记录"""
        for key in self.api_keys:
            self.usage_window[key] = [
                ts for ts in self.usage_window[key]
                if now - ts < RATE_LIMIT_WINDOW_SECONDS
            ]

    def _total_calls_in_window(self) -> int:
        return sum(len(calls) for calls in self.usage_window.values())

    def _has_daily_quota(self) -> bool:
        return any(count < MAX_DAILY_CALLS_PER_KEY for count in self.daily_usage.values())

    def acquire_key(self) -> Optional[str]:
        """阻塞式获取可用的API key"""
        while True:
            now = time.time()
            self._cleanup(now)

            if not self._has_daily_quota():
                print("❌ Gemini API 今日调用次数已耗尽")
                return None

            available_keys = [
                key for key in self.api_keys
                if len(self.usage_window[key]) < MAX_CALLS_PER_KEY_PER_WINDOW
                and self.daily_usage[key] < MAX_DAILY_CALLS_PER_KEY
            ]

            if available_keys and self._total_calls_in_window() < self.max_calls_per_window:
                selected = self._pick_next_key(available_keys)
                self.usage_window[selected].append(now)
                self.daily_usage[selected] += 1
                return selected

            wait_candidates = []
            for key in self.api_keys:
                calls = self.usage_window[key]
                if calls:
                    wait_time = (calls[0] + RATE_LIMIT_WINDOW_SECONDS) - now
                    if wait_time > 0:
                        wait_candidates.append(wait_time)

            if not wait_candidates:
                wait_candidates.append(RATE_LIMIT_WINDOW_SECONDS)

            wait_seconds = max(1, math.ceil(min(wait_candidates)))
            print(f"⏳ 触发Gemini速率限制，等待 {wait_seconds} 秒...")
            time.sleep(wait_seconds)

    def alias_for(self, api_key: str) -> str:
        return self.alias_map.get(api_key, "API")

    def _pick_next_key(self, available_keys: List[str]) -> str:
        """轮询选择下一个可用Key，确保均衡消耗"""
        available_set = set(available_keys)
        for _ in range(len(self.api_keys)):
            key = self.api_keys[self._rr_index]
            self._rr_index = (self._rr_index + 1) % len(self.api_keys)
            if key in available_set:
                return key
        return available_keys[0]


gemini_rate_limiter = GeminiRateLimiter(GEMINI_API_KEYS)
_openai_clients: Dict[str, OpenAI] = {}


def get_openai_client(api_key: str) -> OpenAI:
    if api_key not in _openai_clients:
        _openai_clients[api_key] = OpenAI(
            api_key=api_key,
            base_url=GEMINI_API_URL,
        )
    return _openai_clients[api_key]

def get_all_categories() -> List[Path]:
    """获取所有类别目录（兼容 v1 与 v2 前缀）"""
    categories: List[Path] = []
    if not PROMPTS_DIR.exists():
        print(f"❌ 提示目录不存在: {PROMPTS_DIR}")
        return categories
    for item in PROMPTS_DIR.iterdir():
        # 兼容 01-..29- 等两位数字前缀的目录命名
        if item.is_dir() and re.match(r"^\d{2}-", item.name):
            categories.append(item)
    return sorted(categories)


# ----------------------- URL/Slug 冲突避免相关 -----------------------
def _extract_blog_slug_from_url(url: str) -> Optional[str]:
    """从完整 URL 中提取 /blog/<slug> 的 slug（忽略语言前缀）"""
    try:
        path = urlparse(url).path  # e.g. /en/blog/abc-123
    except Exception:
        return None

    # 允许多语言前缀，如 /en/blog/xxx 或 /blog/xxx
    # 仅当存在 /blog/<slug> 时返回 slug
    parts = [p for p in path.split('/') if p]
    if not parts:
        return None
    # 寻找 "blog" 段落，并取其后一段作为 slug
    for i, p in enumerate(parts):
        if p == 'blog' and i + 1 < len(parts):
            candidate = parts[i + 1]
            # 过滤目录页（如 /en/blog）与多层路径
            if candidate and all(c not in candidate for c in ['/', '<', '>', '"']):
                return candidate
    return None


def load_sitemap_slugs(sitemap_file: Path) -> set:
    """从 sitemap.xml 中加载已有的 /blog/<slug> 集合。失败时返回空集合。"""
    slugs = set()
    try:
        if sitemap_file.exists():
            with open(sitemap_file, 'r', encoding='utf-8') as f:
                text = f.read()
            # 粗略解析 <loc>...</loc> 中的 URL
            for m in re.finditer(r"<loc>\s*([^<\s]+)\s*</loc>", text):
                url = m.group(1)
                slug = _extract_blog_slug_from_url(url)
                if slug:
                    slugs.add(slug)
    except Exception as e:
        print(f"⚠️ 读取 sitemap 失败（忽略并继续）：{e}")
    return slugs


def load_local_blog_slugs(base_dir: Path) -> set:
    """从本地 blogs 目录收集已存在的文件名作为潜在 slug（去掉扩展名）。"""
    slugs = set()
    try:
        for path in base_dir.rglob('*.md'):
            slugs.add(path.stem)
    except Exception as e:
        print(f"⚠️ 扫描本地博客目录失败（忽略并继续）：{e}")
    return slugs


USED_SLUGS: set = set()


def ensure_unique_slug(base_slug: str) -> str:
    """若 base_slug 已被占用，追加 -2/-3 直至唯一，并记录到 USED_SLUGS。"""
    slug = base_slug
    suffix = 2
    while slug in USED_SLUGS:
        slug = f"{base_slug}-{suffix}"
        suffix += 1
    USED_SLUGS.add(slug)
    return slug

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
    
    # 优先从 "Manufacturing & Assembly" 子类选择主关键词
    ma_candidates = [kw for kw in all_unused_keywords if kw.get("subsection") == "Manufacturing & Assembly"]
    main_pool = ma_candidates if ma_candidates else all_unused_keywords
    main_keyword = random.choice(main_pool)
    
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

            api_key = gemini_rate_limiter.acquire_key()
            if not api_key:
                return None

            api_alias = gemini_rate_limiter.alias_for(api_key)
            print(f"🔐 本次调用使用 {api_alias}")

            client = get_openai_client(api_key)
            
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

def build_front_matter(content: str, keyword: str, template_name: str, lsi_keywords: List[str], slug: str) -> str:
    """构建或增强前置元数据。
    """
    content = content.strip()
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

def generate_base_slug(keyword: str, template_name: str) -> str:
    """根据关键词与模板生成基础 slug（未去重）。"""
    keyword_clean = re.sub(r'\s*PCB\s*', ' ', keyword, flags=re.IGNORECASE).strip()
    template_clean = re.sub(r'-v\d+$', '', template_name)
    template_clean = re.sub(r'-pcb', '', template_clean, flags=re.IGNORECASE)

    keyword_slug = slugify(keyword_clean)
    template_slug = slugify(template_clean)
    base_slug = f"{keyword_slug}-{template_slug}"
    # 保底清理空/短 slug
    base_slug = base_slug.strip('-') or slugify(keyword) or slugify(template_name) or f"post-{int(time.time())}"
    return base_slug


def generate_filename_from_slug(slug: str) -> str:
    return f"{slug}.md"

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
    """更新关键词使用状态（仅标记主关键词，LSI 不标记 used）"""
    updated = False
    for subsection in keywords_data.get("subsections", []):
        for keyword_obj in subsection.get("keywords", []):
            if keyword_obj["keyword"] == main_keyword:
                keyword_obj["used"] = True
                keyword_obj["template"] = template_name
                keyword_obj["usage_date"] = datetime.now().strftime('%Y-%m-%d')
                keyword_obj["notes"] = "Generated by batch script"
                updated = True
                break
        if updated:
            break
    return updated

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

    # 如模板未声明字数要求，则追加统一字数要求
    if "### 字数要求" not in filled_prompt and "总字数" not in filled_prompt:
        filled_prompt += "\n\n### 字数要求\n- 总字数：2800-3500词（依主题复杂度调整）\n"
    
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

    # 先生成唯一 slug，再写入 front-matter，最后保存
    base_slug = generate_base_slug(main_keyword["keyword"], template_file.stem)
    unique_slug = ensure_unique_slug(base_slug)

    blog_content = build_front_matter(blog_content, main_keyword["keyword"], template_file.stem, lsi_keywords, unique_slug)

    # 生成文件名并保存（确保与 sitemap 不冲突的 slug）
    filename = generate_filename_from_slug(unique_slug)
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
    
    # 预加载已存在的 slug：sitemap + 本地 blogs
    global USED_SLUGS
    sitemap_slugs = load_sitemap_slugs(SITEMAP_FILE)
    local_slugs = load_local_blog_slugs(OUTPUT_BASE_DIR)
    USED_SLUGS = set(sitemap_slugs) | set(local_slugs)
    print(f"🔎 已有 /blog/slug 数量（sitemap+本地）：{len(USED_SLUGS)}")

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
