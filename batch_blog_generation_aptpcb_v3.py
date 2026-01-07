#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APTPCB v3 entrypoint for `batch_blog_generation_openai.py`.

Uses `_base_templates_v3` to test the v3 layout boosters inspired by
`iphone-consumer-electronics.md` (narrative hook + impact matrix).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def _has_flag(argv: list[str], flag: str) -> bool:
    if flag in argv:
        return True
    prefix = flag + "="
    return any(arg.startswith(prefix) for arg in argv)


def main() -> int:
    repo_dir = Path(__file__).resolve().parent
    runner = repo_dir / "batch_blog_generation_openai.py"

    argv = sys.argv[1:]

    cmd = [sys.executable, str(runner)]
    if not _has_flag(argv, "--prompts-dir"):
        cmd += ["--prompts-dir", "prompts_aptpcb/blogs_prompt_v5"]
    if not _has_flag(argv, "--base-templates-dir"):
        cmd += ["--base-templates-dir", "prompts_aptpcb/blogs_prompt_v5/_base_templates_v3"]
    if not _has_flag(argv, "--internal-link-pool"):
        cmd += ["--internal-link-pool", "prompts_aptpcb/internal_link_pool.md"]
    if not _has_flag(argv, "--sitemap-file"):
        cmd += ["--sitemap-file", "aptpcb_sitemap.xml"]
    if not _has_flag(argv, "--output-lang"):
        cmd += ["--output-lang", "en"]
    if not _has_flag(argv, "--output-base-dir"):
        # Keep v3 outputs separate for A/B comparison.
        cmd += ["--output-base-dir", "blogs_aptpcb_v3"]
    if not _has_flag(argv, "--delay-between-blogs"):
        cmd += ["--delay-between-blogs", "15"]
    if not _has_flag(argv, "--strict-template"):
        cmd += ["--strict-template"]
    if not _has_flag(argv, "--keyword-serp-adapt"):
        cmd += ["--keyword-serp-adapt", "rewrite"]

    cmd += argv
    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(main())
