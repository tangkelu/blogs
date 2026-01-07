#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HILPCB entrypoint for `batch_blog_generation_openai.py`.

This keeps a stable default configuration for the HILPCB site, while still
allowing overrides by passing additional CLI flags.
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
        cmd += ["--prompts-dir", "prompts/blogs_prompt_v3"]
    if not _has_flag(argv, "--sitemap-file"):
        cmd += ["--sitemap-file", "/code/hileap/frontend/public/sitemap.xml"]
    if not _has_flag(argv, "--output-lang"):
        cmd += ["--output-lang", "cn"]
    if not _has_flag(argv, "--output-base-dir"):
        # Keep legacy output structure for existing HILPCB pipeline.
        cmd += ["--output-base-dir", "blogs"]

    cmd += argv
    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(main())

