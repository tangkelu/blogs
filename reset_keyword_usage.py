#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量取消指定日期区间内关键词的 used 标记，便于重新生成博客。"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

DATE_FMT = "%Y-%m-%d"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="重置 keywords.json 中的 used 标记")
    parser.add_argument(
        "--prompts-root",
        default="prompts",
        type=Path,
        help="包含 blogs_prompt_v* 的根目录 (默认: prompts)",
    )
    parser.add_argument(
        "--start",
        default="2025-10-31",
        help="开始日期 (含)，格式 YYYY-MM-DD",
    )
    parser.add_argument(
        "--end",
        default="2025-11-08",
        help="结束日期 (含)，格式 YYYY-MM-DD",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="仅打印统计，不写回文件",
    )
    return parser.parse_args()


def find_keyword_files(prompts_root: Path) -> List[Path]:
    return sorted(prompts_root.rglob("keywords.json"))


def should_reset(keyword: Dict[str, object], start_dt: datetime, end_dt: datetime) -> bool:
    date_str = keyword.get("usage_date")
    if not date_str:
        return False
    try:
        used_dt = datetime.strptime(str(date_str), DATE_FMT)
    except Exception:
        return False
    return start_dt <= used_dt <= end_dt


def reset_keyword(keyword: Dict[str, object]) -> None:
    keyword["used"] = False
    for field in ("template", "usage_date", "notes"):
        if field in keyword:
            keyword.pop(field)


def process_file(path: Path, start_dt: datetime, end_dt: datetime, dry_run: bool) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = 0
    for subsection in data.get("subsections", []):
        for keyword in subsection.get("keywords", []):
            if keyword.get("used") and should_reset(keyword, start_dt, end_dt):
                reset_keyword(keyword)
                changed += 1
    if changed and not dry_run:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return changed


def main() -> None:
    args = parse_args()
    start_dt = datetime.strptime(args.start, DATE_FMT)
    end_dt = datetime.strptime(args.end, DATE_FMT)
    if end_dt < start_dt:
        raise SystemExit("结束日期不能早于开始日期")

    keyword_files = find_keyword_files(args.prompts_root)
    if not keyword_files:
        raise SystemExit("未找到任何 keywords.json")

    total_reset = 0
    touched_files = 0
    for path in keyword_files:
        count = process_file(path, start_dt, end_dt, args.dry_run)
        if count:
            touched_files += 1
            total_reset += count
            status = "(dry-run)" if args.dry_run else ""
            print(f"{path}: 取消 {count} 个 used 标记 {status}")

    print(f"共处理 {len(keyword_files)} 个 keywords.json，重置 {total_reset} 个关键词，涉及 {touched_files} 个文件。")


if __name__ == "__main__":
    main()
