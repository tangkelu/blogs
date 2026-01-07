#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""根据现有批量脚本的 Gemini API 能力，对短篇博客进行扩写。"""

from __future__ import annotations

import argparse
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional

from batch_blog_generation import generate_blog_with_gemini, post_process_content

try:  # PyYAML 可能不存在，按需降级
    import yaml  # type: ignore
except Exception:  # pragma: no cover - 仅在 PyYAML 缺失时触发
    yaml = None

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
READING_TIME_RE = re.compile(r"^(readingTime:\s*)(\d+)", re.MULTILINE)
HTML_TAG_RE = re.compile(r"<[^>]+>")
CHINESE_CHAR_RE = re.compile(r"[\u4e00-\u9fff]")


@dataclass
class BlogPost:
    path: Path  # 原始文件
    relative_path: Path  # 相对 blog_root 的路径
    front_matter_block: Optional[str]
    metadata: Dict[str, object]
    body: str
    char_count: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="扫描指定日期目录下的博客，自动调用 Gemini 扩写至目标字数"
    )
    parser.add_argument(
        "--blog-root",
        default="blogs",
        type=Path,
        help="博客根目录（默认: blogs）",
    )
    parser.add_argument(
        "--start",
        default=1031,
        type=int,
        help="起始目录（形如1031代表10月31日）",
    )
    parser.add_argument(
        "--end",
        default=1108,
        type=int,
        help="结束目录（含）",
    )
    parser.add_argument(
        "--locale",
        default="cn",
        help="需要处理的语言子目录，例如cn/en；留空表示直接遍历日期目录",
    )
    parser.add_argument(
        "--min-chars",
        default=3000,
        type=int,
        help="触发扩写的最低正文字数",
    )
    parser.add_argument(
        "--max-chars",
        default=3500,
        type=int,
        help="扩写完成后的目标上限字数",
    )
    parser.add_argument(
        "--rewrite-retries",
        default=2,
        type=int,
        help="当长度未达标时的额外扩写轮次",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="仅统计字数，不触发扩写",
    )
    parser.add_argument(
        "--output-suffix",
        default="",
        help="为日期目录追加的后缀，例如 '-new'，留空表示直接覆盖原文件",
    )
    parser.add_argument(
        "--count-mode",
        choices=["all", "chinese"],
        default="all",
        help="all=去空白后的全部字符；chinese=去HTML后仅统计汉字",
    )
    return parser.parse_args()


def estimate_character_count(text: str, mode: str) -> int:
    """根据模式估算字数，可选择仅统计汉字。"""

    text = HTML_TAG_RE.sub("", text)
    if mode == "chinese":
        return len(CHINESE_CHAR_RE.findall(text))
    return len(re.sub(r"\s+", "", text))


def split_front_matter(content: str) -> tuple[Optional[str], str]:
    match = FRONT_MATTER_RE.match(content)
    if not match:
        return None, content
    block = match.group(0)
    body = content[match.end() :]
    return block, body.lstrip("\n")


def parse_front_matter(block: Optional[str]) -> Dict[str, object]:
    if not block or not yaml:
        return {}
    inner = block.strip()
    if inner.startswith("---"):
        inner = inner[3:]
    if inner.endswith("---"):
        inner = inner[:-3]
    try:
        data = yaml.safe_load(inner) or {}
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def iter_blog_files(base: Path, start: int, end: int, locale: Optional[str]) -> Iterable[Path]:
    for date_dir in sorted(base.iterdir()):
        if not date_dir.is_dir():
            continue
        name = date_dir.name
        if not name.isdigit():
            continue
        date_value = int(name)
        if not (start <= date_value <= end):
            continue
        target_dir = date_dir / locale if locale else date_dir
        if not target_dir.exists() or not target_dir.is_dir():
            continue
        for md_file in sorted(target_dir.glob("*.md")):
            yield md_file


def load_blog_post(path: Path, relative_path: Path, count_mode: str) -> BlogPost:
    content = path.read_text(encoding="utf-8")
    front_block, body = split_front_matter(content)
    metadata = parse_front_matter(front_block)
    char_count = estimate_character_count(body, count_mode)
    return BlogPost(
        path=path,
        relative_path=relative_path,
        front_matter_block=front_block,
        metadata=metadata,
        body=body,
        char_count=char_count,
    )


def build_expansion_prompt(post: BlogPost, min_chars: int, max_chars: int, attempt: int) -> str:
    title = str(post.metadata.get("title", post.path.stem)) if post.metadata else post.path.stem
    tags = post.metadata.get("tags", []) if isinstance(post.metadata, dict) else []
    tag_text = ", ".join(tags) if isinstance(tags, list) else str(tags)

    reinforcement = "" if attempt == 1 else f"\n请务必让正文达到{min_chars}-{max_chars}字，上一轮没有满足长度要求。"

    instructions = f"""
你是一名长期服务于车规/工业/高可靠 PCB 领域的资深技术营销写作者，擅长把复杂工程实践写得专业又易读。
现有一篇标题为《{title}》的博客需要扩写，核心主题与术语必须保留，可按逻辑重新组织段落、加入案例/数据/流程细节，语气保持专业可信、信息连贯，不得堆砌。
主要标签/语境：{tag_text or '（未提供标签，可结合正文自洽扩写）'}。

目标：
1. 在充分吸收原文观点的前提下扩展内容，深入解释每个关键论点或流程节点，可增加实操建议、指标拆解、对比案例、失败教训等高价值细节。
2. 输出全中文 Markdown，允许包含必要的列表、表格或轻量 HTML 块，并保持过渡自然。
3. 控制扩写后正文总字数为 {min_chars}-{max_chars} 字，信息密度优于原文。
4. 若原文包含链接或嵌入式 HTML，请保留（可上下文改写但不要删除）。
5. 输出只包含“正文”，不要再次生成 front matter。
{reinforcement}

以下为原始正文，请据此扩写：
"""

    return instructions + "\n```markdown\n" + post.body.strip() + "\n```\n"


def update_reading_time_block(block: Optional[str], char_count: int) -> Optional[str]:
    if not block:
        return block
    minutes = max(3, math.ceil(char_count / 500))

    def _repl(match: re.Match[str]) -> str:
        return f"{match.group(1)}{minutes}"

    updated = READING_TIME_RE.sub(_repl, block, count=1)
    return updated


def expand_post(post: BlogPost, min_chars: int, max_chars: int, retries: int, count_mode: str) -> Optional[str]:
    for attempt in range(1, retries + 2):
        prompt = build_expansion_prompt(post, min_chars, max_chars, attempt)
        new_body = generate_blog_with_gemini(prompt)
        if not new_body:
            return None
        new_body = post_process_content(new_body).strip() + "\n"
        new_chars = estimate_character_count(new_body, count_mode)
        print(f"➡️  {post.path}: 第{attempt}轮生成 {new_chars} 字")
        if min_chars <= new_chars <= max_chars:
            post.front_matter_block = update_reading_time_block(post.front_matter_block, new_chars)
            post.body = new_body
            post.char_count = new_chars
            return assemble_post(post)
        if attempt >= retries + 1:
            print(f"⚠️  {post.path} 扩写完成但字数 {new_chars} 未落在目标区间，仍将返回结果")
            post.front_matter_block = update_reading_time_block(post.front_matter_block, new_chars)
            post.body = new_body
            post.char_count = new_chars
            return assemble_post(post)
    return None


def assemble_post(post: BlogPost) -> str:
    if post.front_matter_block:
        front = post.front_matter_block
        if not front.endswith("\n"):
            front += "\n"
        body = post.body.lstrip("\n")
        return front + "\n" + body
    return post.body.lstrip("\n")


def resolve_output_path(post: BlogPost, blog_root: Path, suffix: str) -> Path:
    if not suffix:
        return post.path
    parts = post.relative_path.parts
    if not parts:
        return post.path
    new_first = parts[0] + suffix
    if len(parts) == 1:
        new_relative = Path(new_first)
    else:
        new_relative = Path(new_first, *parts[1:])
    return blog_root / new_relative


def main() -> None:
    args = parse_args()
    blog_root: Path = args.blog_root
    if not blog_root.exists():
        raise SystemExit(f"博客根目录不存在: {blog_root}")

    locale = args.locale if args.locale else None
    posts: List[BlogPost] = []
    for md_path in iter_blog_files(blog_root, args.start, args.end, locale):
        relative_path = md_path.relative_to(blog_root)
        post = load_blog_post(md_path, relative_path, args.count_mode)
        posts.append(post)

    if not posts:
        print("未找到符合日期范围的博客。")
        return

    short_posts = [p for p in posts if p.char_count < args.min_chars]
    print(f"共扫描 {len(posts)} 篇，低于 {args.min_chars} 字的有 {len(short_posts)} 篇。")

    if args.dry_run:
        for post in short_posts:
            print(f"· {post.path}: {post.char_count} 字")
        return

    updated = 0
    for post in short_posts:
        print(f"\n🛠  处理 {post.path} (当前 {post.char_count} 字)...")
        new_content = expand_post(
            post,
            args.min_chars,
            args.max_chars,
            args.rewrite_retries,
            args.count_mode,
        )
        if not new_content:
            print(f"❌  {post.path} 扩写失败，跳过")
            continue
        target_path = resolve_output_path(post, blog_root, args.output_suffix)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(new_content, encoding="utf-8")
        if target_path == post.path:
            print(f"✅  {post.path} 已扩写至 {post.char_count} 字")
        else:
            print(f"✅  {post.path} → {target_path} 已扩写至 {post.char_count} 字")
        updated += 1

    print(f"\n完成：成功扩写 {updated} 篇，剩余 {len(short_posts) - updated} 篇需人工检查。")


if __name__ == "__main__":
    main()
