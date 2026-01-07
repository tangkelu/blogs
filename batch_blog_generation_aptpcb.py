#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APTPCB entrypoint for `batch_blog_generation_openai.py`.

This keeps a stable default configuration for the APTPCB site, while still
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
        cmd += ["--prompts-dir", "prompts_aptpcb/blogs_prompt_v5"]
    if not _has_flag(argv, "--base-templates-dir"):
        cmd += ["--base-templates-dir", "prompts_aptpcb/blogs_prompt_v5/_base_templates_v2"]
    if not _has_flag(argv, "--internal-link-pool"):
        cmd += ["--internal-link-pool", "prompts_aptpcb/internal_link_pool.md"]
    if not _has_flag(argv, "--sitemap-file"):
        cmd += ["--sitemap-file", "aptpcb_sitemap.xml"]
    if not _has_flag(argv, "--output-lang"):
        cmd += ["--output-lang", "en"]
    if not _has_flag(argv, "--output-base-dir"):
        # Separate output to avoid slug/markdown collisions across sites.
        cmd += ["--output-base-dir", "blogs_aptpcb"]
    if not _has_flag(argv, "--delay-between-blogs"):
        # Default pacing to avoid hammering the API and to reduce transient errors.
        cmd += ["--delay-between-blogs", "15"]
    if not _has_flag(argv, "--strict-template"):
        cmd += ["--strict-template"]
    if not _has_flag(argv, "--keyword-serp-adapt"):
        # Rewrite off-target software SERP keywords into PCBA/PCB terms before generation.
        cmd += ["--keyword-serp-adapt", "rewrite"]

    cmd += argv
    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(main())
