#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


TRACKER_PATH = Path("/code/blogs/aptpcb_blog_changed_url.md")
EN_PATH_RE = re.compile(r"`(/code/hileap/frontendAPT/public/static/blogs/2025/\d\d/en/[^`]+\.md)`")


def main() -> int:
    if not TRACKER_PATH.exists():
        print(f"missing: {TRACKER_PATH}")
        return 2

    raw = TRACKER_PATH.read_text(encoding="utf-8", errors="ignore")
    lines = raw.splitlines(keepends=True)

    seen: set[str] = set()
    kept = 0
    dropped = 0
    out: list[str] = []

    for line in lines:
        m = EN_PATH_RE.search(line)
        if not m:
            out.append(line)
            continue
        path = m.group(1)
        if path in seen:
            dropped += 1
            continue
        seen.add(path)
        kept += 1
        out.append(line)

    new = "".join(out)
    if not new.endswith("\n"):
        new += "\n"

    if new != raw:
        TRACKER_PATH.write_text(new, encoding="utf-8")

    print(f"unique_en_paths={kept} dropped_duplicate_lines={dropped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

