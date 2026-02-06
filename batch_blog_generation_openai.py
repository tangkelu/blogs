#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量博客生成脚本
遍历所有19个类别，为每个类别生成一篇博客
"""

import os
import argparse
import json
import random
import time
import re
import math
from datetime import datetime
from urllib.parse import urlparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import requests
from slugify import slugify
try:
    import numpy as np
except Exception:  # pragma: no cover - optional dependency
    np = None

# 配置
PROMPTS_DIR = Path("prompts/blogs_prompt_v3")
OUTPUT_BASE_DIR = Path("blogs")
# 站点 sitemap 路径（用于避免 /blog/slug 冲突）
SITEMAP_FILE = Path("/code/hileap/frontendAPT/public/sitemap.xml")
OUTPUT_LANG_MODE = "cn"  # cn / en / auto
TEMPLATE_KIND = "auto"  # auto / query / pillar
DRY_RUN = False
LIMIT_CATEGORIES: Optional[int] = None
BASE_TEMPLATES_DIR: Optional[Path] = None
KEYWORD_INTENT = "auto"  # auto / query / pillar
INTERNAL_LINK_POOL_FILE: Optional[Path] = None
MODULES_DIR: Optional[Path] = None
FORCE_MODULES: Optional[str] = None
KEYWORD_SERP_ADAPT = "off"  # off / rewrite / skip
ASSETS_IMAGE_CATALOG_FILE: Optional[Path] = None
ASSETS_IMAGE_POOL_SIZE: int = 18
STRICT_TEMPLATE = False
IMAGE_POLICY = "auto"  # auto / llm / none
MIN_WORDS_RATIO = 0.85
MIN_WORDS_FLOOR = 1800
MAX_GENERATION_ATTEMPTS = 5
API_KEY = "sk-BmfHbyJCQXY98kEe30hVkyk0vLFPisBchHJ6PM2S0VrHhrwL"

GEMINI_API_URL = "https://max.openai365.top/v1"
MODEL = "[满血Pro] gemini-3-pro-preview-maxthinking"
DELAY_BETWEEN_REQUESTS = 10  # 秒
RATE_LIMIT_WINDOW_SECONDS = 70
MAX_CALLS_PER_KEY_PER_WINDOW = 2
MAX_DAILY_CALLS_PER_KEY = 50
DISABLE_RATE_LIMITS = True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Batch generate blogs from prompt templates.")
    parser.add_argument(
        "--prompts-dir",
        default=str(PROMPTS_DIR),
        help="Prompt categories directory, e.g. prompts/blogs_prompt_v3 or prompts_aptpcb/blogs_prompt_v5",
    )
    parser.add_argument(
        "--output-base-dir",
        default=str(OUTPUT_BASE_DIR),
        help="Output base directory (default: blogs)",
    )
    parser.add_argument(
        "--sitemap-file",
        default=str(SITEMAP_FILE),
        help="Sitemap XML path used for /blog/<slug> conflict avoidance",
    )
    parser.add_argument(
        "--output-lang",
        choices=["cn", "en", "auto"],
        default=OUTPUT_LANG_MODE,
        help="Output language folder under date directory (cn/en), or auto-detect from content",
    )
    parser.add_argument(
        "--template-kind",
        choices=["auto", "query", "pillar", "playbook", "story"],
        default=TEMPLATE_KIND,
        help="Filter templates by filename containing 'query'/'pillar'/'playbook'/'story' (auto keeps all templates).",
    )
    parser.add_argument(
        "--base-templates-dir",
        default=None,
        help="Fallback templates directory used when a category has no templates/*.md.",
    )
    parser.add_argument(
        "--internal-link-pool",
        default=None,
        help="Optional markdown file containing internal link pool URLs to inject into templates via {{internal_link_pool}}.",
    )
    parser.add_argument(
        "--modules-dir",
        default=None,
        help="Optional directory of prompt modules to inject (APTPCB: prompts_aptpcb/blogs_prompt_v5/_modules_v1).",
    )
    parser.add_argument(
        "--modules",
        default=None,
        help="Optional comma-separated modules to force (e.g. comparison,application,capability). If omitted, modules are inferred from keyword.",
    )
    parser.add_argument(
        "--keyword-serp-adapt",
        choices=["off", "rewrite", "skip"],
        default=KEYWORD_SERP_ADAPT,
        help="Pre-generation SERP adaptation for off-target keywords (e.g., 'quality dashboard design' -> 'PCBA quality dashboard').",
    )
    parser.add_argument(
        "--assets-image-catalog",
        default=None,
        help="Optional markdown catalog listing /assets/img paths to inject into templates via {{assets_image_pool}} (APTPCB default: /code/hileap/frontendAPT/docs/assets-img-filenames.md).",
    )
    parser.add_argument(
        "--assets-image-pool-size",
        type=int,
        default=ASSETS_IMAGE_POOL_SIZE,
        help="How many candidate images to inject into {{assets_image_pool}} (default: 18).",
    )
    parser.add_argument(
        "--image-policy",
        choices=["auto", "llm", "none"],
        default=IMAGE_POLICY,
        help="Image insertion policy: auto injects a hero image (and respects manual front matter override); llm relies on the model to insert 0–3 images; none disables injection.",
    )
    parser.add_argument(
        "--keyword-intent",
        choices=["auto", "query", "pillar"],
        default=KEYWORD_INTENT,
        help="Prefer keywords with matching `intent` in keywords.json (auto keeps all).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Select keywords/templates and show prompt stats without calling the model or writing files.",
    )
    parser.add_argument(
        "--delay-between-blogs",
        type=float,
        default=DELAY_BETWEEN_REQUESTS,
        help="Delay in seconds between generating each blog (per category). Set 0 to disable.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Process at most N categories in this run.",
    )
    parser.add_argument(
        "--strict-template",
        action="store_true",
        help="Fail (do not save / mark used) when required sections or minimum length are missing.",
    )
    parser.add_argument(
        "--max-generation-attempts",
        type=int,
        default=MAX_GENERATION_ATTEMPTS,
        help="Max attempts per blog generation before falling back to the best candidate.",
    )
    parser.add_argument(
        "--min-words-ratio",
        type=float,
        default=MIN_WORDS_RATIO,
        help="Minimum word count ratio relative to the prompt's MIN target (e.g. 0.85).",
    )
    parser.add_argument(
        "--min-words-floor",
        type=int,
        default=MIN_WORDS_FLOOR,
        help="Absolute minimum word count floor used with --min-words-ratio (default: 1200).",
    )
    parser.add_argument(
        "--keyword-search",
        type=str,
        default=None,
        help="Filter keywords containing this string (case-insensitive). Overrides other selection logic.",
    )
    parser.add_argument(
        "--ignore-sitemap",
        action="store_true",
        help="Ignore existing slugs from sitemap (allow generating conflicting slugs). Useful for rewriting existing blogs.",
    )
    return parser.parse_args()


def chat_completions_request(
    *,
    base_url: str,
    api_key: str,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float = 0.1,
    max_tokens: int = 16000,
    timeout_seconds: int = 180,
) -> str:
    """Call OpenAI-compatible Chat Completions endpoint: POST /v1/chat/completions"""
    endpoint = f"{base_url.rstrip('/')}/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    resp = requests.post(endpoint, headers=headers, json=payload, timeout=timeout_seconds)
    if resp.status_code >= 400:
        try:
            detail = resp.json()
        except Exception:
            detail = resp.text
        raise RuntimeError(f"Chat Completions request failed ({resp.status_code}): {detail}")

    data = resp.json()
    try:
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        raise RuntimeError(f"Unexpected Chat Completions response format: {data}") from e


def _estimate_english_word_count(text: str) -> int:
    """Rough word count for English-ish markdown; ignores YAML front matter if present."""
    text = (text or "").strip()
    if not text:
        return 0
    if text.lstrip().startswith("---"):
        markers = list(re.finditer(r"^---\s*$", text, flags=re.MULTILINE))
        if len(markers) >= 2 and markers[0].start() < 10:
            text = text[markers[1].end() :].strip()
    return len(re.findall(r"[A-Za-z0-9']+", text))


def _infer_min_words_from_prompt(prompt: str) -> Optional[int]:
    """
    Infer a minimum word count from `Word count target: **MIN–MAX words**`.
    We use a configurable ratio of MIN to filter out truncated outputs.
    """
    if not prompt:
        return None
    m = re.search(r"Word count target:\s*\*\*(\d+)\s*[–-]\s*(\d+)\s*words", prompt, flags=re.IGNORECASE)
    if not m:
        return None
    min_target = int(m.group(1))
    ratio = float(MIN_WORDS_RATIO or 0)
    if ratio <= 0:
        ratio = 0.85
    floor = int(MIN_WORDS_FLOOR or 0)
    floor = max(0, floor)
    return max(floor, int(min_target * ratio))


def _looks_like_prompt_echo_or_readme(text: str) -> bool:
    if not text:
        return True
    bad_markers = [
        "Output Hard Rules",
        "You are writing an",
        "Use with:",
        "Templates:",
        "适用场景",
        "结构逻辑",
        "请发送您的主题",
    ]
    lower = text.lower()
    return any(m.lower() in lower for m in bad_markers)


def _has_h1(text: str) -> bool:
    return bool(re.search(r"(?m)^\s*#\s+\S", text or ""))


def _has_enough_structure(text: str) -> bool:
    return len(re.findall(r"(?m)^\s*##\s+\S", text or "")) >= 4


def _required_section_markers_from_prompt(prompt: str) -> List[str]:
    """Pick a small set of section markers that must appear in the generated output."""
    markers: List[str] = []
    if not prompt:
        return markers
    # Only treat literal *heading lines* in the prompt as required sections.
    # This avoids false positives from rules like: "Do NOT output a `## Key Takeaways` section".
    heading_candidates: List[Tuple[str, str]] = [
        ("## Quick Answer", r"(?m)^\s*##\s*Quick\s*Answer\b"),
        ("## Key Takeaways", r"(?m)^\s*##\s*Key\s*Takeaways\b"),
        ("## Specifications to define upfront", r"(?m)^\s*##\s*Specifications\s+to\s+define\s+upfront\b"),
        ("## Supplier qualification checklist", r"(?m)^\s*##\s*Supplier\s+qualification\s+checklist\b"),
        ("## Conclusion", r"(?m)^\s*##\s*Conclusion\b"),
    ]
    for label, pat in heading_candidates:
        if re.search(pat, prompt, flags=re.IGNORECASE):
            markers.append(label)
    # Always require Conclusion if the prompt expects it, otherwise skip.
    return markers


def _required_section_patterns_from_prompt(prompt: str) -> List[Tuple[str, str]]:
    """Return (label, regex) required section patterns inferred from the template prompt."""
    patterns: List[Tuple[str, str]] = []
    if not prompt:
        return patterns

    def has_heading(pat: str) -> bool:
        return bool(re.search(pat, prompt, flags=re.IGNORECASE | re.MULTILINE))

    # Story templates: require the full H2 outline (strictly) so outputs stay "pure story".
    if re.search(r"(?i)english\s+story\s+page", prompt or ""):
        lines = (prompt or "").splitlines()
        start_idx = None
        for i, ln in enumerate(lines):
            if re.match(r"^\s*##\s*The\s+Context:\s*", ln, flags=re.IGNORECASE):
                start_idx = i
                break
        if start_idx is not None:
            story_h2 = []
            for ln in lines[start_idx:]:
                m = re.match(r"^\s*##\s+(.+?)\s*$", ln)
                if not m:
                    continue
                title = m.group(1).strip()
                if not title:
                    continue
                story_h2.append(title)
            for title in story_h2:
                patterns.append((title, rf"(?im)^\s*##\s*{re.escape(title)}\s*$"))

            # Visual table blocks: treat them as required if the template includes them.
            # (We check for the H3 titles, which is less brittle than matching the full HTML.)
            if re.search(r"Decision\s+Matrix:\s*Technical\s+Choice", prompt, flags=re.IGNORECASE):
                patterns.append(
                    ("Decision Matrix (visual table)", r"(?im)^\s*<h3[^>]*>\s*Decision\s+Matrix:\s*Technical\s+Choice\b")
                )
            if re.search(r"5-Year\s+Performance\s+Trajectory", prompt, flags=re.IGNORECASE):
                patterns.append(
                    (
                        "5-Year Performance Trajectory (visual table)",
                        r"(?im)^\s*<h3[^>]*>\s*5-Year\s+Performance\s+Trajectory\b",
                    )
                )
            return patterns

    if has_heading(r"^\s*##\s*Quick\s*Answer\b"):
        patterns.append(("Quick Answer", r"(?im)^\s*##\s*Quick\s*Answer\b"))
    if has_heading(r"^\s*##\s*Key\s*Takeaways\b"):
        patterns.append(("Key Takeaways", r"(?im)^\s*##\s*Key\s*Takeaways\b"))
    # Query template core sections (match by phrase, since the keyword is dynamic).
    if "definition and scope" in prompt.lower():
        patterns.append(("Definition and scope", r"(?im)^\s*##\s+.*\bdefinition\s+and\s+scope\b"))
    if "rules and specifications" in prompt.lower():
        patterns.append(("Rules and specifications", r"(?im)^\s*##\s+.*\brules\s+and\s+specifications\b"))
    if "implementation steps" in prompt.lower():
        patterns.append(("Implementation steps", r"(?im)^\s*##\s+.*\bimplementation\s+steps\b"))
    if "troubleshooting" in prompt.lower():
        patterns.append(("Troubleshooting", r"(?im)^\s*##\s+.*\btroubleshooting\b"))
    # Only require FAQ/Glossary when they are explicitly section headings in the prompt.
    # Avoid false positives from internal link pools (URLs like /faq or /glossary).
    if re.search(r"(?im)^\s*##\s+.*\bfaq\b", prompt):
        patterns.append(("FAQ", r"(?im)^\s*##\s+.*\bfaq\b"))
    if re.search(r"(?im)^\s*##\s+.*\bglossary\b", prompt):
        patterns.append(("Glossary", r"(?im)^\s*##\s+.*\bglossary\b"))
    if has_heading(r"^\s*##\s*Specifications\s+to\s+define\s+upfront\b"):
        patterns.append(("Specifications to define upfront", r"(?im)^\s*##\s*Specifications\s+to\s+define\s+upfront\b"))
    if has_heading(r"^\s*##\s*Supplier\s+qualification\s+checklist\b"):
        patterns.append(("Supplier qualification checklist", r"(?im)^\s*##\s*Supplier\s+qualification\s+checklist\b"))
    if has_heading(r"^\s*##\s*Conclusion\b"):
        patterns.append(("Conclusion", r"(?im)^\s*##\s*Conclusion\b"))
    return patterns


def _missing_required_sections(text: str, required: List[Tuple[str, str]]) -> List[str]:
    missing: List[str] = []
    for label, pat in required:
        if not re.search(pat, text or ""):
            missing.append(label)
    return missing


def _detect_v2_template_kind(prompt: str) -> str:
    """Best-effort detect v2 template kind from prompt text."""
    p = (prompt or "").lower()
    if "english story page" in p:
        return "story"
    if "english query page" in p:
        return "query"
    if "english pillar page" in p:
        return "pillar"
    if "english buyer playbook" in p:
        return "playbook"
    return "unknown"


def _detect_v3_template_kind(prompt: str) -> str:
    """Best-effort detect v3 template kind from prompt text."""
    p = (prompt or "").lower()
    if "english story page v3" in p:
        return "story"
    if "english query page v3" in p:
        return "query"
    if "english pillar page v3" in p:
        return "pillar"
    if "english buyer playbook v3" in p:
        return "playbook"
    return "unknown"


def _extract_keyword_from_prompt(prompt: str) -> Optional[str]:
    m = re.search(r"primary keyword:\s*`([^`]+)`", prompt or "", flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m2 = re.search(r"(?m)^\s*#\s+(.+?)\s*$", prompt or "")
    if m2:
        return m2.group(1).strip()
    return None


def _extract_lsi_from_prompt(prompt: str) -> List[str]:
    m = re.search(
        r"Use LSI keywords naturally\s*\\(avoid stuffing\\):\s*(.+?)\s*$",
        prompt or "",
        flags=re.IGNORECASE | re.MULTILINE,
    )
    if not m:
        return []
    raw = m.group(1).strip()
    if not raw or "{" in raw:
        return []
    items = [s.strip() for s in raw.split(",") if s.strip()]
    return items[:12]


def _build_output_starter(kind: str, *, keyword: str, lsi_keywords: List[str]) -> str:
    """
    A short, high-salience starter block appended at the end of the prompt so the model
    is less likely to skip the opening sections.
    """
    title_suffix = {
        "query": "Practical Rules, Specs, and Troubleshooting Guide",
        "pillar": "A Practical End-to-End Guide (from basics to production)",
        "playbook": "Buyer-Friendly Playbook (Specs, Risks, Checklist)",
        "story": "A Narrative Technical Explainer (Design, Trade-Offs, and Reliability)",
    }.get(kind, "Practical Guide")
    title = f"{keyword}: {title_suffix}"
    if kind == "story":
        first_h2 = f"## The Context: What Makes {keyword} Challenging"
    elif kind == "pillar":
        first_h2 = "## Key Takeaways"
    else:
        first_h2 = "## Quick Answer (30 seconds)"
    date_str = datetime.now().strftime("%Y-%m-%d")
    tags = [keyword] + [s for s in (lsi_keywords or []) if s][:6]
    tags_yaml = "[" + ", ".join(json.dumps(t.replace('"', "'")) for t in tags) + "]"
    return (
        "FINAL OUTPUT STARTER (follow exactly; do not skip early sections):\n"
        "- Your response MUST start with YAML front matter (first char is `---`).\n"
        "- Then output exactly one H1 that matches the front-matter title.\n"
        f"- Then output `{first_h2}` as the first H2.\n\n"
        "Start your response like this (fill the content, keep headings):\n"
        "---\n"
        f'title: \"{title}\"\n'
        "description: \"\"\n"
        "category: technology\n"
        f'date: \"{date_str}\"\n'
        "featured: true\n"
        "image: \"\"\n"
        "readingTime: 8\n"
        f"tags: {tags_yaml}\n"
        "---\n\n"
        f"# {title}\n\n"
        "(Write the 2–3 sentence opening here.)\n\n"
        + (
            "### Contents\n"
            "- (Add bullet links to each H2 section.)\n\n"
            if kind == "story"
            else ""
        )
        + f"{first_h2}\n"
    )


def _first_h2_line_index(markdown: str) -> Optional[int]:
    lines = (markdown or "").splitlines()
    for i, line in enumerate(lines):
        if re.match(r"^\s*##\s+\S", line):
            return i
    return None


def _inject_prefix_before_first_h2(markdown: str, prefix: str) -> str:
    """Insert `prefix` right before the first H2 in `markdown`."""
    lines = (markdown or "").splitlines()
    idx = _first_h2_line_index(markdown)
    insert_at = idx if idx is not None else len(lines)
    prefix_lines = [l.rstrip("\n") for l in (prefix or "").strip("\n").splitlines()]
    if not prefix_lines:
        return (markdown or "").rstrip() + "\n"
    out_lines = lines[:insert_at] + [""] + prefix_lines + [""] + lines[insert_at:]
    return "\n".join(out_lines).strip() + "\n"


def _generate_query_prefix_sections(keyword: str, lsi_keywords: List[str]) -> Optional[str]:
    """
    Generate the missing "top" sections for Query template outputs.
    Returns markdown WITHOUT front matter and WITHOUT an H1.
    """
    lsi = [s for s in (lsi_keywords or []) if s][:6]
    lsi_text = ", ".join(lsi) if lsi else ""
    prompt = f"""Output Markdown only.

Write ONLY the missing early sections for this topic: {keyword}

Hard rules:
- Do NOT output YAML front matter.
- Do NOT output an H1.
- Do NOT output any sections after the rules/specs table (no steps, troubleshooting, FAQ, glossary, quote, conclusion).
- Keep it concise and practical.

Now write in this exact order:
1) A 2–3 sentence answer-first opening paragraph (no heading).
2) `## Quick Answer (30 seconds)` with 5–7 bullets (use `- ` bullets).
3) A **Highlights** list (5–7 bullets; no H2 heading).
4) `## {keyword}: definition and scope (what it is, what it isn’t)`:
   - "Applies when" (3–5 bullets)
   - "Doesn’t apply when" (3–5 bullets)
5) `## {keyword} rules and specifications (key parameters and limits)`:
   - A Markdown table: `Rule | Recommended value/range | Why it matters | How to verify | If ignored`
   - At least 8 rows, with at least 2 rows mentioning verification/acceptance criteria.

Use these related keywords naturally (do not stuff): {lsi_text}
"""
    system_msg = (
        "You are a technical writer. Follow the user's section order exactly. "
        "Return only the requested sections."
    )
    try:
        return chat_completions_request(
            base_url=GEMINI_API_URL,
            api_key=API_KEY,
            model=MODEL,
            messages=[{"role": "system", "content": system_msg}, {"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=2500,
            timeout_seconds=180,
        ).strip()
    except Exception as e:
        print(f"⚠️ Query 前置补全生成失败（忽略并继续）：{e}")
        return None


def _extract_candidate_bullets_from_body(markdown: str, *, max_items: int = 6) -> List[str]:
    """
    Extract bullet-like lines from the body to build a summary without extra model calls.
    Prefer ordered steps and existing bullets.
    """
    text = (markdown or "").strip()
    if not text:
        return []
    # Strip YAML front matter.
    if text.lstrip().startswith("---"):
        markers = list(re.finditer(r"^---\s*$", text, flags=re.MULTILINE))
        if len(markers) >= 2 and markers[0].start() < 10:
            text = text[markers[1].end() :].strip()

    candidates: List[str] = []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            continue
        # Ordered list
        m_num = re.match(r"^\d+\.\s+(.*)$", s)
        if m_num:
            candidates.append(m_num.group(1).strip())
        # Dash bullets
        m_dash = re.match(r"^-+\s+(.*)$", s)
        if m_dash:
            candidates.append(m_dash.group(1).strip())
        if len(candidates) >= max_items * 3:
            break

    cleaned: List[str] = []
    seen = set()
    for c in candidates:
        c = re.sub(r"\s+", " ", c).strip()
        c = re.sub(r"\*\*(.*?)\*\*", r"\1", c)
        c = re.sub(r"`([^`]*)`", r"\1", c)
        # Avoid truncated/unfinished bullets in summary sections.
        if re.search(r"(\.\.\.|…)\s*$", c):
            continue
        if len(c) < 8:
            continue
        if len(c) > 140:
            c = c[:140].rstrip()
            if c and c[-1].isalnum():
                c += "."
        key = c.lower()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(c)
        if len(cleaned) >= max_items:
            break
    return cleaned


def _build_quick_answer_section_from_existing(markdown: str, *, keyword: str) -> str:
    bullets = _extract_candidate_bullets_from_body(markdown, max_items=6)
    if len(bullets) < 4:
        bullets = []
    lines = ["## Quick Answer (30 seconds)"]
    if bullets:
        for b in bullets[:6]:
            lines.append(f"- {b}")
    else:
        # Conservative fallback when we can't extract enough.
        lines += [
            f"- Define what `{keyword}` means in your context (scope, pass/fail criteria).",
            "- List the 3–5 parameters that drive yield, reliability, and cost.",
            "- Decide what to measure and how you will verify it (test/inspection/report).",
            "- Identify the top 3 failure modes and the quickest checks to confirm each.",
            "- Prepare DFM/RFQ inputs (Gerbers/ODB++, stackup, fab notes, quantities, lead time).",
        ]
    return "\n".join(lines).rstrip() + "\n"


def _build_key_takeaways_section_from_existing(markdown: str, *, keyword: str) -> str:
    bullets = _extract_candidate_bullets_from_body(markdown, max_items=7)
    if len(bullets) < 4:
        bullets = []
    lines = ["## Key Takeaways"]
    if bullets:
        for b in bullets[:7]:
            lines.append(f"- {b}")
    else:
        lines += [
            f"- Define `{keyword}` in measurable terms (scope + boundaries).",
            "- Choose 3–5 metrics that map to yield, reliability, and cost.",
            "- Set acceptance criteria and how you will verify each metric.",
            "- Identify the top failure modes and the fastest checks to confirm them.",
            "- Prepare RFQ inputs (data, stackup, quantities, lead time, compliance).",
        ]
    return "\n".join(lines).rstrip() + "\n"


def _build_glossary_section(*, keyword: str, lsi_keywords: List[str], min_rows: int = 10) -> str:
    """
    Build a practical glossary section to satisfy v2 templates when the model omits it.
    Keep terms broadly applicable to PCB/PCBA topics.
    """
    min_rows = max(8, int(min_rows or 0))
    text = " ".join([keyword] + list(lsi_keywords or [])).lower()

    base_terms: List[Tuple[str, str, str]] = [
        ("DFM", "Design for Manufacturability: layout rules that reduce defects.", "Prevents rework, delays, and hidden cost."),
        ("AOI", "Automated Optical Inspection used to find solder/assembly defects.", "Improves coverage and catches early escapes."),
        ("ICT", "In-Circuit Test that probes nets to verify opens/shorts/values.", "Fast structural test for volume builds."),
        ("FCT", "Functional Circuit Test that powers the board and checks behavior.", "Validates real function under load."),
        ("Flying Probe", "Fixtureless electrical test using moving probes on pads.", "Good for prototypes and low/medium volume."),
        ("Netlist", "Connectivity definition used to compare design vs manufactured PCB.", "Catches opens/shorts before assembly."),
        ("Stackup", "Layer build with cores/prepreg, copper weights, and thickness.", "Drives impedance, warpage, and reliability."),
        ("Impedance", "Controlled trace behavior for high-speed/RF signals (e.g., 50Ω).", "Avoids reflections and signal integrity failures."),
        ("ENIG", "Electroless Nickel Immersion Gold surface finish.", "Balances solderability and flatness; watch nickel thickness."),
        ("OSP", "Organic Solderability Preservative surface finish.", "Low cost; sensitive to handling and multiple reflows."),
        ("HASL", "Hot Air Solder Leveling surface finish.", "Economical; less flat for fine-pitch BGAs."),
        ("Microvia", "Laser-drilled small via for HDI build-up layers.", "Enables density but increases process risk."),
        ("Warpage", "Board bow/twist caused by stackup and process stresses.", "Can break assembly yield and BGA reliability."),
        ("Tg", "Glass transition temperature of the laminate.", "Higher Tg improves thermal reliability."),
        ("Dk/Df", "Dielectric constant / dissipation factor of laminate.", "Key for RF/high-speed loss control."),
    ]

    extra: List[Tuple[str, str, str]] = []
    if "flex" in text or "rigid-flex" in text or "rigid flex" in text:
        extra += [
            ("Coverlay", "Polyimide cover layer used instead of solder mask on flex.", "Improves bend reliability and insulation."),
            ("Stiffener", "Rigid reinforcement bonded to flex areas.", "Prevents connector damage and improves handling."),
            ("Bend Radius", "Minimum safe radius for repeated bending.", "Too tight causes copper cracking and opens."),
        ]
    if "ultrasound" in text or "highspeed" in text or "impedance" in text or "rf" in text:
        extra += [
            ("Return Path", "Continuous reference plane for controlled signals.", "Prevents EMI and impedance discontinuities."),
            ("Crosstalk", "Unwanted coupling between adjacent traces.", "Drives spacing/stackup decisions."),
        ]
    if "quote" in text or "rfq" in text or "checklist" in text:
        extra += [
            ("RFQ", "Request for Quote: package of data for pricing and DFM.", "Reduces back-and-forth and lead time."),
            ("COC", "Certificate of Conformance for materials/process compliance.", "Supports audits and traceability."),
        ]

    rows: List[Tuple[str, str, str]] = []
    seen = set()
    for t in base_terms + extra:
        key = t[0].lower()
        if key in seen:
            continue
        seen.add(key)
        rows.append(t)
        if len(rows) >= max(min_rows, 12):
            break

    lines = ["## Glossary (key terms)", "| Term | Meaning | Why it matters in practice |", "|---|---|---|"]
    for term, meaning, why in rows[: max(min_rows, 10)]:
        lines.append(f"| {term} | {meaning} | {why} |")
    return "\n".join(lines).rstrip() + "\n"


def _build_specifications_to_define_upfront_section(*, keyword: str) -> str:
    lines = [
        "## Specifications to define upfront (before you commit)",
        "Define these inputs early so your DFM review and quote are accurate and repeatable.",
        "",
        "- Product goal: prototype vs pilot vs mass production (expected volumes).",
        "- Data package: Gerbers/ODB++, NC drill, IPC-2581 (and how you name versions).",
        "- Stackup: layer count, finished thickness, copper weights, controlled impedance targets (if any).",
        "- Material: base laminate family (FR-4/high-Tg/halogen-free), special needs (low-Dk/low-Df).",
        "- Surface finish: ENIG/OSP/HASL/Immersion Silver (and why).",
        "- Solder mask & legend: color, matte/gloss, AOI readability constraints.",
        "- Minimum feature limits: trace/space, drill, annular ring, via types (microvia/via-in-pad).",
        "- Reliability targets: thermal cycling, vibration, humidity, operating temperature range.",
        "- Test/inspection: E-test/netlist, microsection, X-ray, AOI, IPC class requirements.",
        "- Delivery: lead time, panelization preference, packaging, and shipping constraints.",
        "",
        f"Use this checklist as the starting point for `{keyword}` so the supplier can confirm feasibility and risks up front.",
    ]
    return "\n".join(lines).rstrip() + "\n"


def _build_supplier_qualification_checklist_section(*, keyword: str) -> str:
    lines = [
        "## Supplier qualification checklist",
        "Use this checklist to avoid late surprises in yield, reliability, and lead time.",
        "",
        "- Can the supplier meet your minimum trace/space and drill limits with margin (not just “can do once”)?",
        "- Do they provide a DFM report that flags risks with recommended fixes (not only pass/fail)?",
        "- Do they support your required IPC class and provide evidence (COC, test reports)?",
        "- What is their electrical test method (fixture/flying probe) and netlist coverage?",
        "- How do they control critical processes (lamination, plating, etch compensation, solder mask registration)?",
        "- Do they have capability for controlled impedance (coupon strategy, measurement method, tolerance)?",
        "- What are typical defect modes for this product type and how are they prevented (and measured)?",
        "- How is traceability handled (lot control, material tracking, rework logs)?",
        "- Can they support assembly/test needs (panelization, fiducials, tooling holes, test points)?",
        "- What are their turnaround times for engineering questions (EQ) and issue containment?",
        "",
        f"If `{keyword}` is safety-critical or high-volume, require sample-level validation data before full release.",
    ]
    return "\n".join(lines).rstrip() + "\n"


def _build_conclusion_section(*, keyword: str) -> str:
    return (
        "## Conclusion\n"
        f"`{keyword}` is easiest to get right when you define the specifications and verification plan early, then confirm them through DFM and test coverage.\n"
        "Use the rules, checkpoints, and troubleshooting patterns above to reduce iteration loops and protect yield as volumes increase.\n"
        "If you’re unsure about a constraint, validate it with a small pilot build before locking the production release.\n"
    )


def _insert_section_before_conclusion(markdown: str, section_markdown: str) -> str:
    text = (markdown or "").rstrip("\n")
    if not text:
        return section_markdown.strip() + "\n"
    if re.search(r"(?im)^\s*##\s*Conclusion\b", text):
        parts = re.split(r"(?im)^\s*(##\s*Conclusion\b)", text, maxsplit=1)
        if len(parts) >= 3:
            before = parts[0].rstrip()
            marker = parts[1]
            after = parts[2].lstrip("\n")
            insert = section_markdown.strip("\n").rstrip()
            return (before + "\n\n" + insert + "\n\n" + marker + after).strip() + "\n"
    return (text + "\n\n" + section_markdown.strip("\n").rstrip()).strip() + "\n"



def repair_truncated_conclusion(markdown: str) -> str:
    """
    Detect if the blog content ends abruptly (no punctuation/newline) and fix it.
    Common with LLM max_token limits.
    """
    text = (markdown or "").strip()
    if not text:
        return text

    # Valid ending characters
    valid_endings = ('.', '!', '?', '>', ']', '}', '"', "'")
    if text.endswith(valid_endings):
        return text + "\n"

    print("⚠️ Detected truncated output at end of file. Attempting repair...")

    # Pattern 1: Cut off during a link "[Link Text](url..."
    if text.endswith("(") or text.endswith("["):
        text = text[:-1].strip()

    # Pattern 2: "to discuss your" -> "to discuss your project."
    if text.endswith("to discuss your"):
        return text + " project.\n"
    if text.endswith("to discuss"):
        return text + " your project.\n"
    if text.endswith("contact us"):
        return text + " today.\n"

    # Fallback: Trim to last sentence ending.
    last_punct = max(text.rfind('.'), text.rfind('!'), text.rfind('?'))
    
    if last_punct > len(text) - 200: 
        print(f"✂️  Trimming truncated tail: '{text[last_punct+1:]}'")
        text = text[:last_punct+1]
        if "Signed," not in text[-500:]:
             text += "\n\nSigned, The Engineering Team at APTPCB"
    else:
        text += "."
        
    return text + "\n"


def repair_missing_required_sections_locally(
    markdown: str,
    *,
    keyword: str,
    lsi_keywords: List[str],
    missing_sections: List[str],
) -> str:
    """Local (no extra model call) repairs for common v2 template omissions."""
    text = (markdown or "").strip() + "\n"
    miss = set(missing_sections or [])

    if "Key Takeaways" in miss:
        block = _build_key_takeaways_section_from_existing(text, keyword=keyword)
        text = _insert_block_after_h1_before_heading_or_table(text, block)
        text = normalize_h1_to_front_matter_title(text, fallback_title=keyword)

    if "Specifications to define upfront" in miss:
        block = _build_specifications_to_define_upfront_section(keyword=keyword)
        text = _insert_section_before_conclusion(text, block)

    if "Supplier qualification checklist" in miss:
        block = _build_supplier_qualification_checklist_section(keyword=keyword)
        text = _insert_section_before_conclusion(text, block)

    if "Glossary" in miss:
        block = _build_glossary_section(keyword=keyword, lsi_keywords=lsi_keywords, min_rows=10)
        text = _insert_section_before_conclusion(text, block)

    if "FAQ" in miss:
        # Add a concise FAQ section; expansion can add more if needed later.
        block = _build_faq_section(keyword=keyword, count=8)
        text = _insert_section_before_conclusion(text, block)

    if "Conclusion" in miss:
        text = (text.rstrip() + "\n\n" + _build_conclusion_section(keyword=keyword)).strip() + "\n"

    return text


def _build_faq_section(*, keyword: str, count: int = 8) -> str:
    count = max(6, int(count or 0))
    questions = [
        (f"What is `{keyword}` (in one sentence)?", "It’s a practical set of requirements and checks that defines how you will build, verify, and accept the product.", ["Clarify scope and boundaries.", "Define pass/fail criteria.", "Align DFM + test coverage."]),
        (f"How much does `{keyword}` typically cost?", "Cost depends on layer count, materials, finish, test method, and engineering review effort.", ["Provide quantities and stackup early.", "Call out impedance, via-in-pad, microvias.", "Ask for DFM notes before quoting."]),
        (f"What drives lead time for `{keyword}`?", "Lead time is driven by data completeness, material availability, and test/inspection requirements.", ["Avoid missing drill/stackup.", "Confirm material substitutions.", "Lock panelization early."]),
        (f"What files should I send for `{keyword}`?", "Send Gerbers/ODB++, NC drill, stackup notes, fab drawing, and test requirements.", ["Include version + date.", "Provide impedance targets and tolerances.", "Attach BOM if PCBA."]),
        (f"How do I define acceptance criteria for `{keyword}`?", "Use measurable criteria tied to IPC class, electrical test coverage, and functional validation.", ["State IPC class.", "Specify E-test/netlist.", "List functional test cases."]),
        (f"Which surface finish is best for `{keyword}`?", "Choose based on pitch/flatness needs, cost targets, and reliability requirements.", ["ENIG for fine pitch/BGA.", "OSP for low-cost builds.", "Avoid HASL for very fine pitch."]),
        (f"How many test points do I need for `{keyword}`?", "Enough to support the test strategy (flying probe/ICT/FCT) with margin.", ["Plan early in layout.", "Keep access away from tall parts.", "Document probe pad size."]),
        (f"What are the most common failures in `{keyword}`?", "Data issues, insufficient test coverage, and uncontrolled process limits are the most common causes.", ["Watch annular ring/registration.", "Control solder mask openings.", "Verify impedance and warpage."]),
        (f"How can I reduce risk when scaling `{keyword}` to production?", "Add a pilot build, tighten specs, and validate with repeatable test/inspection reports.", ["Run a controlled DOE if needed.", "Collect yield + failure Pareto.", "Freeze revisions before volume."]),
        (f"When should I use flying probe vs fixture-based ICT for `{keyword}`?", "Flying probe suits prototypes/low volume; ICT is best for high volume when a fixture is justified.", ["Consider net access.", "Compare test coverage vs cost.", "Plan fixture lead time."]),
    ]
    picked = questions[:count]
    lines = [f"## {keyword} FAQ", ""]
    for q, a, bullets in picked:
        lines.append(f"### {q}")
        lines.append(a)
        for b in bullets:
            lines.append(f"- {b}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _insert_or_expand_faq(markdown: str, *, keyword: str, needed_words: int) -> str:
    text = (markdown or "").strip() + "\n"
    if needed_words <= 0:
        return text

    # Find an existing FAQ section (H2 containing FAQ).
    lines = text.splitlines()
    faq_idx = None
    for i, line in enumerate(lines):
        if re.match(r"(?im)^\s*##\s+.*\bfaq\b", line):
            faq_idx = i
            break

    # If no FAQ, insert one before conclusion.
    if faq_idx is None:
        block = _build_faq_section(keyword=keyword, count=10)
        return _insert_section_before_conclusion(text, block)

    # Determine FAQ section end (next H2 or end).
    end = len(lines)
    for j in range(faq_idx + 1, len(lines)):
        if re.match(r"(?m)^\s*##\s+\S", lines[j]):
            end = j
            break

    existing_block = "\n".join(lines[faq_idx:end])
    existing_qs = {q.strip().lower() for q in re.findall(r"(?m)^\s*###\s+(.*)$", existing_block)}
    # Add more QAs until we cover the shortfall (best-effort).
    extra = _build_faq_section(keyword=keyword, count=12)
    extra_lines = extra.splitlines()
    # Strip the H2 header from the generated block; only keep QAs.
    extra_lines = [l for l in extra_lines if not re.match(r"(?im)^\s*##\s+", l)]

    appended: List[str] = []
    current_q = None
    buf: List[str] = []
    for l in extra_lines + ["### __END__"]:
        m = re.match(r"(?m)^\s*###\s+(.*)$", l)
        if m:
            # flush previous
            if current_q and buf:
                if current_q.lower() not in existing_qs:
                    appended.extend(buf)
                    appended.append("")
            current_q = m.group(1).strip()
            buf = [l]
        else:
            buf.append(l)

    if appended:
        new_block = existing_block.rstrip() + "\n\n" + "\n".join(appended).rstrip()
        out = "\n".join(lines[:faq_idx] + new_block.splitlines() + lines[end:]).strip() + "\n"
        return out
    return text


def _append_bullets_to_section(markdown: str, *, section_pat: str, bullets: List[str]) -> str:
    """Append bullets to an existing H2 section matched by `section_pat` (case-insensitive regex)."""
    text = (markdown or "").strip() + "\n"
    if not bullets:
        return text
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.search(section_pat, line, flags=re.IGNORECASE):
            if re.match(r"(?m)^\s*##\s+\S", line):
                start = i
                break
    if start is None:
        return text
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if re.match(r"(?m)^\s*##\s+\S", lines[j]):
            end = j
            break
    insert_at = end
    extra = [""] + [f"- {b}" for b in bullets if b.strip()] + [""]
    out = "\n".join(lines[:insert_at] + extra + lines[insert_at:]).strip() + "\n"
    return out


def expand_to_min_words_locally(
    markdown: str,
    *,
    keyword: str,
    lsi_keywords: List[str],
    min_words: int,
) -> str:
    """
    Expand the article to meet a minimum word count without extra model calls.
    Strategy:
    - Prefer adding/expanding FAQ (natural, user-intent aligned).
    - If still short, extend glossary rows (lightweight).
    """
    text = (markdown or "").strip() + "\n"
    target = int(min_words or 0)
    if target <= 0:
        return text

    wc = _estimate_english_word_count(text)
    if wc >= target:
        return text

    # 1) Expand FAQ.
    text = _insert_or_expand_faq(text, keyword=keyword, needed_words=target - wc)
    wc = _estimate_english_word_count(text)
    if wc >= target:
        return text

    # 2) Expand existing checklists/sections with more bullets (keeps structure natural).
    text = _append_bullets_to_section(
        text,
        section_pat=r"^\s*##\s+.*\bsupplier\s+qualification\s+checklist\b",
        bullets=[
            "Ask for example DFM reports and typical turn time for engineering questions (EQ).",
            "Confirm how they control solder mask registration and via tenting rules.",
            "Clarify how they validate impedance (coupon placement, tolerance, reporting).",
            "Require a traceability mechanism (lot codes, material batch, process logs).",
            "Define what constitutes a critical defect vs acceptable cosmetic defect.",
        ],
    )
    text = _append_bullets_to_section(
        text,
        section_pat=r"^\s*##\s+.*\bvalidation\b.*\bacceptance\b",
        bullets=[
            "Define the sampling plan for inspection and electrical test.",
            "Specify who owns the test fixture (if any) and its revision control.",
            "Add a failure-handling workflow: containment → analysis → corrective action → verification.",
        ],
    )
    text = _append_bullets_to_section(
        text,
        section_pat=r"^\s*##\s+.*\bkey\s+risks\b",
        bullets=[
            "Data mismatch (Gerber vs drill vs fab notes) leading to EQ holds or scrap.",
            "Uncontrolled substitutions (materials/finish) shifting performance or reliability.",
            "Insufficient test access reducing coverage and increasing escapes.",
        ],
    )
    wc = _estimate_english_word_count(text)
    if wc >= target:
        return text

    # 3) If the article already has a glossary section, extend it (do not create a new H2 if absent).
    if re.search(r"(?im)^\s*##\s+.*\bglossary\b", text):
        text = _insert_section_before_conclusion(text, _build_glossary_section(keyword=keyword, lsi_keywords=lsi_keywords, min_rows=16))
    return text


def _insert_block_after_h1_before_table_or_h2(markdown: str, block: str) -> str:
    """Insert a block after the first H1, before the first table or H2 that appears after it."""
    text = (markdown or "").rstrip("\n")
    if not text:
        return block.strip() + "\n"

    lines = text.splitlines()

    # Find front matter end.
    i = 0
    if lines and lines[0].strip() == "---":
        for j in range(1, min(len(lines), 200)):
            if lines[j].strip() == "---":
                i = j + 1
                break
    # Skip blank lines after FM.
    while i < len(lines) and not lines[i].strip():
        i += 1

    # Find H1.
    h1_idx = None
    for j in range(i, min(len(lines), i + 120)):
        if re.match(r"^\s*#\s+\S", lines[j]):
            h1_idx = j
            break
    if h1_idx is None:
        return _inject_prefix_before_first_h2(text, block)

    scan_start = h1_idx + 1
    # Move past immediate blank lines and optional hero image.
    while scan_start < len(lines) and not lines[scan_start].strip():
        scan_start += 1
    if scan_start < len(lines) and re.match(r"^!\[.*\]\(/assets/img/", lines[scan_start].strip()):
        scan_start += 1
        while scan_start < len(lines) and not lines[scan_start].strip():
            scan_start += 1

    first_h2 = None
    first_table = None
    for j in range(scan_start, min(len(lines), scan_start + 400)):
        s = lines[j].strip()
        if re.match(r"^\s*##\s+\S", lines[j]):
            first_h2 = j
            break
        if s.startswith("|") and j + 1 < len(lines) and re.match(r"^\s*\|?\s*:?[-]{3,}", lines[j + 1]):
            first_table = j
            break

    insert_at = first_h2 if first_h2 is not None else first_table if first_table is not None else scan_start
    block_lines = block.strip("\n").splitlines()
    out = lines[:insert_at] + [""] + block_lines + [""] + lines[insert_at:]
    return "\n".join(out).strip() + "\n"


def _insert_block_after_h1_before_heading_or_table(markdown: str, block: str) -> str:
    """Insert a block after the first H1, before the first heading (H2/H3/...) or table after it."""
    text = (markdown or "").rstrip("\n")
    if not text:
        return block.strip() + "\n"

    lines = text.splitlines()

    # Find front matter end.
    i = 0
    if lines and lines[0].strip() == "---":
        for j in range(1, min(len(lines), 200)):
            if lines[j].strip() == "---":
                i = j + 1
                break
    while i < len(lines) and not lines[i].strip():
        i += 1

    # Find H1.
    h1_idx = None
    for j in range(i, min(len(lines), i + 120)):
        if re.match(r"^\s*#\s+\S", lines[j]):
            h1_idx = j
            break
    if h1_idx is None:
        return _inject_prefix_before_first_h2(text, block)

    scan_start = h1_idx + 1
    while scan_start < len(lines) and not lines[scan_start].strip():
        scan_start += 1
    if scan_start < len(lines) and re.match(r"^!\[.*\]\(/assets/img/", lines[scan_start].strip()):
        scan_start += 1
        while scan_start < len(lines) and not lines[scan_start].strip():
            scan_start += 1

    first_heading = None
    first_table = None
    for j in range(scan_start, min(len(lines), scan_start + 500)):
        s = lines[j].strip()
        if re.match(r"^\s*#{2,6}\s+\S", lines[j]):
            first_heading = j
            break
        if s.startswith("|") and j + 1 < len(lines) and re.match(r"^\s*\|?\s*:?[-]{3,}", lines[j + 1]):
            first_table = j
            break

    insert_at = first_heading if first_heading is not None else first_table if first_table is not None else scan_start
    block_lines = block.strip("\n").splitlines()
    out = lines[:insert_at] + [""] + block_lines + [""] + lines[insert_at:]
    return "\n".join(out).strip() + "\n"


def _find_section_bounds(lines: List[str], heading_regex: str) -> Optional[Tuple[int, int]]:
    """Find a H2 section by heading regex; returns (start_idx, end_idx) in lines."""
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^\s*##\s+\S", line) and re.search(heading_regex, line, flags=re.IGNORECASE):
            start = i
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if re.match(r"^\s*##\s+\S", lines[j]):
            end = j
            break
    return (start, end)


def _section_has_markdown_table(section_lines: List[str]) -> bool:
    """Detect a markdown table within section lines (best effort)."""
    for i in range(0, max(0, len(section_lines) - 1)):
        a = section_lines[i].strip()
        b = section_lines[i + 1].strip()
        if a.startswith("|") and re.match(r"^\|?\s*:?-{3,}", b):
            return True
    return False


def _insert_table_under_section(markdown: str, *, heading_regex: str, table_md: str) -> str:
    """Insert a table block under a matching H2 section if the section has no table."""
    text = (markdown or "").strip() + "\n"
    split = _split_yaml_front_matter_lines(text)
    if not split:
        return text
    fm_lines, body_lines = split
    bounds = _find_section_bounds(body_lines, heading_regex)
    if not bounds:
        return text
    start, end = bounds
    section = body_lines[start:end]
    if _section_has_markdown_table(section):
        return text
    # Insert after the H2 heading + optional blank line.
    insert_at = start + 1
    while insert_at < end and not body_lines[insert_at].strip():
        insert_at += 1
    block_lines = table_md.strip("\n").splitlines()
    body_lines = body_lines[:insert_at] + [""] + block_lines + [""] + body_lines[insert_at:]
    return "\n".join(fm_lines + body_lines).strip() + "\n"


def ensure_playbook_section_tables(markdown: str, *, keyword: str) -> str:
    """
    For playbook posts, ensure key sections contain at least one table.
    This stabilizes A-grade “utility” without extra model calls.
    """
    text = (markdown or "").strip() + "\n"
    kind = _infer_article_kind_from_content(text)
    if kind != "playbook":
        return text

    specs_table = (
        "| Parameter | Recommended value / option | Why it matters | How to verify |\n"
        "|---|---|---|---|\n"
        "| Layer count | 4–8 (typical), higher as needed | Drives cost, yield, and routing margin | Stackup + DFM report |\n"
        "| Min trace/space | 4/4 mil (typical) | Impacts yield and lead time | DRC + fab capability |\n"
        "| Via strategy | Through vias vs VIPPO vs microvias | Affects assembly reliability | Microsection + IPC criteria |\n"
        "| Surface finish | ENIG/OSP/HASL | Impacts solderability and flatness | COC + solderability tests |\n"
        "| Solder mask | Matte green (default) | AOI readability and bridging risk | AOI trial + mask registration |\n"
        "| Test | Flying probe / ICT / FCT | Coverage vs cost trade-off | Coverage report + fixture plan |\n"
        "| Acceptance class | IPC Class 2 / 3 | Defines defect limits | Drawing notes + inspection report |\n"
        "| Lead time | Standard vs expedited | Schedule risk | Quote + capacity confirmation |\n"
    )

    acceptance_table = (
        "| Test / Check | Method | Pass criteria (example) | Evidence |\n"
        "|---|---|---|---|\n"
        "| Electrical continuity | Flying probe / fixture | 100% nets tested; no opens/shorts | E-test report |\n"
        "| Critical dimensions | Measurement | Meets drawing tolerances | Inspection record |\n"
        "| Plating / fill integrity | Microsection | No voids/cracks beyond IPC limits | Microsection photos |\n"
        "| Solderability | Wetting test | Acceptable wetting; no de-wet | Solderability report |\n"
        "| Warpage | Flatness measurement | Within spec (e.g., ≤0.75%) | Warpage record |\n"
        "| Functional validation | FCT | All cases pass; log stored | FCT logs |\n"
    )

    text = _insert_table_under_section(text, heading_regex=r"Specifications\s+to\s+Define\s+Upfront", table_md=specs_table)
    text = _insert_table_under_section(text, heading_regex=r"Validation\s*&\s*Acceptance", table_md=acceptance_table)
    return text


def _split_yaml_front_matter_lines(markdown: str) -> Optional[Tuple[List[str], List[str]]]:
    """Return (front_matter_lines, body_lines) if YAML front matter exists, else None."""
    text = (markdown or "").lstrip("\ufeff")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, min(len(lines), 200)):
        if lines[i].strip() == "---":
            return (lines[: i + 1], lines[i + 1 :])
    return None


def _front_matter_get_value(front_matter_lines: List[str], key: str) -> Optional[str]:
    pat = re.compile(rf"^\s*{re.escape(key)}\s*:\s*(.*?)\s*$")
    for line in front_matter_lines[1:]:
        if line.strip() == "---":
            break
        m = pat.match(line)
        if not m:
            continue
        val = m.group(1).strip()
        if not val:
            return ""
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1].strip()
        return val
    return None


def _front_matter_set_value(front_matter_lines: List[str], key: str, value: str) -> List[str]:
    """Set or insert a YAML key in front matter; returns updated lines."""
    val = (value or "").replace('"', "'").strip()
    out = list(front_matter_lines)
    pat = re.compile(rf"^\s*{re.escape(key)}\s*:\s*.*$")
    for i in range(1, len(out) - 1):
        if pat.match(out[i]):
            out[i] = f'{key}: "{val}"'
            return out
    # Insert before closing '---'
    if out and out[-1].strip() == "---":
        return out[:-1] + [f'{key}: "{val}"'] + out[-1:]
    return out + [f'{key}: "{val}"']


def _strip_md_inline(text: str) -> str:
    s = (text or "").strip()
    # links [text](url) -> text
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    # bold/italics/code
    s = re.sub(r"[*_`]+", "", s)
    # HTML tags
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _extract_opening_paragraph(markdown: str) -> str:
    """Extract the first non-table paragraph after H1/hero image."""
    split = _split_yaml_front_matter_lines(markdown or "")
    if not split:
        return ""
    _fm, body_lines = split

    # Find H1.
    i = 0
    while i < len(body_lines) and not body_lines[i].strip():
        i += 1
    for j in range(i, min(len(body_lines), i + 200)):
        if re.match(r"^\s*#\s+\S", body_lines[j]):
            i = j + 1
            break

    # Skip blank lines and optional hero image.
    while i < len(body_lines) and not body_lines[i].strip():
        i += 1
    if i < len(body_lines) and re.match(r"^!\[.*\]\(/assets/img/", body_lines[i].strip()):
        i += 1
    while i < len(body_lines) and not body_lines[i].strip():
        i += 1

    # If next thing is a heading/table/bullets, opening is missing.
    if i >= len(body_lines):
        return ""
    s0 = body_lines[i].strip()
    if s0.startswith("|") or s0.startswith("#") or re.match(r"^[-*]\s+", s0) or re.match(r"^\d+\.\s+", s0):
        return ""

    # Grab paragraph until blank line.
    para: List[str] = []
    for j in range(i, min(len(body_lines), i + 40)):
        s = body_lines[j].rstrip()
        if not s.strip():
            break
        if s.strip().startswith("|"):
            break
        if s.strip().startswith("#"):
            break
        para.append(s)
    text = _strip_md_inline(" ".join(para))
    # Require some substance.
    if len(re.findall(r"[A-Za-z0-9']+", text)) < 18:
        return ""
    return text


def ensure_front_matter_description(markdown: str, *, keyword: str) -> str:
    """Ensure YAML `description` is a clean sentence-like summary (avoid table snippets)."""
    split = _split_yaml_front_matter_lines(markdown or "")
    if not split:
        return (markdown or "").strip() + "\n"
    fm_lines, body_lines = split

    existing = (_front_matter_get_value(fm_lines, "description") or "").strip()
    existing_clean = _strip_md_inline(existing)
    bad = False
    if not existing_clean:
        bad = True
    if existing.strip().startswith("|") or existing_clean.startswith("|"):
        bad = True
    if len(existing_clean) < 30:
        bad = True

    opening = _extract_opening_paragraph("\n".join(fm_lines + body_lines))
    if not opening:
        opening = f"A practical guide to {keyword} with clear rules, recommended ranges, verification steps, and common failure fixes."

    desc = opening
    # Truncate to a reasonable meta description length.
    if len(desc) > 165:
        cut = 165
        for k in range(min(len(desc) - 1, 165), max(120, 0), -1):
            if desc[k] in ".;!?":
                cut = k + 1
                break
            if desc[k] == " " and k > 140:
                cut = k
                break
        desc = desc[:cut].strip()

    if bad:
        fm_lines = _front_matter_set_value(fm_lines, "description", desc)

    return "\n".join(fm_lines + body_lines).strip() + "\n"


def _build_opening_paragraph(*, keyword: str, kind: str) -> str:
    k = keyword.strip() or "PCB topic"
    if kind == "playbook":
        return (
            f"Sourcing {k} is easiest when you define specs and acceptance criteria up front, then validate the highest risks early. "
            f"This playbook explains what to specify, what can go wrong, how to test it, and how to qualify a supplier."
        )
    if kind == "pillar":
        return (
            f"{k} is best understood as a set of measurable requirements and trade-offs—from definition and metrics to implementation checkpoints and acceptance criteria. "
            f"This guide explains how to evaluate {k} and avoid common mistakes when moving from prototype to production."
        )
    # query/default
    return (
        f"{k} is easier to get right when you start from clear ranges, verification methods, and known failure modes. "
        f"This guide gives practical rules, recommended specs, and troubleshooting steps you can apply immediately."
    )


def ensure_opening_paragraph(markdown: str, *, keyword: str, kind: str) -> str:
    """Ensure there is a short opening paragraph right after H1/hero, before any tables/headings."""
    text = (markdown or "").strip() + "\n"
    split = _split_yaml_front_matter_lines(text)
    if not split:
        return text
    fm_lines, body_lines = split

    # Determine the ideal insertion point (right after H1 + optional hero).
    # Find H1.
    h1_idx = None
    for i, line in enumerate(body_lines[:200]):
        if re.match(r"^\s*#\s+\S", line):
            h1_idx = i
            break
    if h1_idx is None:
        # Fall back to simple insertion behavior.
        opening = _build_opening_paragraph(keyword=keyword, kind=kind).strip()
        return _insert_block_after_h1_before_heading_or_table(text, opening + "\n")

    insert_pos = h1_idx + 1
    while insert_pos < len(body_lines) and not body_lines[insert_pos].strip():
        insert_pos += 1
    if insert_pos < len(body_lines) and re.match(r"^!\[.*\]\(/assets/img/", body_lines[insert_pos].strip()):
        insert_pos += 1
        while insert_pos < len(body_lines) and not body_lines[insert_pos].strip():
            insert_pos += 1

    def is_para_line(s: str) -> bool:
        st = s.strip()
        if not st:
            return False
        if st.startswith("|"):
            return False
        if st.startswith("#"):
            return False
        if re.match(r"^[-*]\s+", st):
            return False
        if re.match(r"^\d+\.\s+", st):
            return False
        return True

    def next_paragraph(start: int) -> Optional[Tuple[int, int, str]]:
        i = start
        while i < len(body_lines) and not body_lines[i].strip():
            i += 1
        if i >= len(body_lines):
            return None
        # Stop if we hit an H2 (structure begins).
        if re.match(r"^\s*##\s+\S", body_lines[i]):
            return None
        if not is_para_line(body_lines[i]):
            return None
        j = i
        buf: List[str] = []
        while j < len(body_lines):
            if not body_lines[j].strip():
                break
            if re.match(r"^\s*#{2,6}\s+\S", body_lines[j]):
                break
            if body_lines[j].strip().startswith("|"):
                break
            buf.append(body_lines[j].rstrip())
            j += 1
        para_text = _strip_md_inline(" ".join(buf))
        if len(re.findall(r"[A-Za-z0-9']+", para_text)) < 18:
            return None
        return (i, j, para_text)

    # If the paragraph is already in the right place, keep it.
    current = next_paragraph(insert_pos)
    if current is None:
        # Look for a good opening paragraph later (before first H2); if found, move it up.
        scan = insert_pos
        found: Optional[Tuple[int, int, str]] = None
        for _ in range(60):
            candidate = next_paragraph(scan)
            if candidate:
                found = candidate
                break
            scan += 1
            if scan >= len(body_lines):
                break
            if re.match(r"^\s*##\s+\S", body_lines[scan]):
                break

        if found:
            start, end, para_text = found
            # Remove the paragraph block from its original location.
            del body_lines[start:end]
            if start < insert_pos:
                insert_pos -= (end - start)
            # Insert it at insert_pos.
            insert_lines = ["", para_text, ""]
            body_lines = body_lines[:insert_pos] + insert_lines + body_lines[insert_pos:]
        else:
            # No paragraph found; insert a generated opening.
            opening = _build_opening_paragraph(keyword=keyword, kind=kind).strip()
            body_lines = body_lines[:insert_pos] + ["", opening, ""] + body_lines[insert_pos:]

    # De-duplicate: remove subsequent paragraphs that exactly match the opening paragraph text.
    opening_text = next_paragraph(insert_pos)
    opening_clean = opening_text[2] if opening_text else ""
    if opening_clean:
        i = insert_pos + 1
        removed = 0
        while i < min(len(body_lines), insert_pos + 240) and removed < 2:
            cand = next_paragraph(i)
            if not cand:
                i += 1
                continue
            start, end, para_text = cand
            if para_text == opening_clean:
                del body_lines[start:end]
                removed += 1
                continue
            i = end + 1

    return "\n".join(fm_lines + body_lines).strip() + "\n"


def _has_highlights_block(markdown: str) -> bool:
    t = markdown or ""
    if re.search(r"(?im)^\s*\*\*Highlights\*\*\s*$", t):
        return True
    if re.search(r"(?im)^\s*#{2,3}\s*Highlights\b", t):
        return True
    return False


def _build_highlights_block(*, keyword: str, kind: str) -> str:
    k = keyword.strip() or "this topic"
    if kind == "playbook":
        bullets = [
            "What to specify upfront (data, stackup, materials, testing).",
            "Key risks and early detection signals.",
            "Validation plan and pass/fail criteria.",
            "Supplier qualification checklist and RFQ inputs.",
        ]
    elif kind == "pillar":
        bullets = [
            "Clear definition and scope boundaries.",
            "Metrics that matter and how to measure them.",
            "Decision rules to choose the right approach.",
            "Implementation checkpoints and common mistakes.",
        ]
    else:
        bullets = [
            "Quick rules and recommended ranges.",
            "How to verify and what to log as evidence.",
            "Common failure modes and fastest checks.",
            "Decision rules for trade-offs and constraints.",
        ]
    lines = ["**Highlights**"] + [f"- {b}" for b in bullets] + [""]
    return "\n".join(lines).rstrip() + "\n"


def ensure_highlights(markdown: str, *, keyword: str, kind: str) -> str:
    """
    Ensure a Highlights block exists when useful:
    - Query: required (prompt expects it).
    - Playbook: required when Key Takeaways is missing.
    - Pillar: optional (Key Takeaways already exists).
    """
    text = (markdown or "").strip() + "\n"
    if _has_highlights_block(text):
        return text

    has_qa = bool(re.search(r"(?im)^\s*##\s*Quick\s*Answer\b", text))
    has_kt = bool(re.search(r"(?im)^\s*##\s*Key\s*Takeaways\b", text))

    need = False
    if kind in {"query", "story"}:
        need = True
    elif kind == "playbook":
        need = not has_kt
    else:  # pillar/unknown
        need = False

    if not need:
        return text

    block = _build_highlights_block(keyword=keyword, kind=kind)
    # For query: insert after Quick Answer section if present; otherwise after opening.
    if has_qa:
        lines = text.splitlines()
        qa_idx = None
        for i, line in enumerate(lines):
            if re.match(r"(?im)^\s*##\s*Quick\s*Answer\b", line):
                qa_idx = i
                break
        if qa_idx is None:
            return _insert_block_after_h1_before_table_or_h2(text, block)
        end = len(lines)
        for j in range(qa_idx + 1, len(lines)):
            if re.match(r"(?m)^\s*##\s+\S", lines[j]):
                end = j
                break
        out = "\n".join(lines[:end] + [""] + block.strip("\n").splitlines() + [""] + lines[end:]).strip() + "\n"
        return out

    if kind == "story":
        split = _split_yaml_front_matter_lines(text)
        if not split:
            return text
        fm_lines, body_lines = split
        # Place Highlights right before the first H2 section (after TOC/opening if present).
        first_h2 = None
        for i, ln in enumerate(body_lines):
            if re.match(r"^\s*##\s+\S", ln):
                first_h2 = i
                break
        if first_h2 is None:
            return text
        insert_lines = ["", "### Highlights", ""] + [ln for ln in block.splitlines()[1:] if ln.strip()]
        body_lines = body_lines[:first_h2] + insert_lines + [""] + body_lines[first_h2:]
        return "\n".join(fm_lines + body_lines).strip() + "\n"

    return _insert_block_after_h1_before_table_or_h2(text, block)


def _infer_article_kind_from_content(markdown: str) -> str:
    t = markdown or ""
    if re.search(r"(?im)^\s*##\s*Quick\s*Answer\b", t):
        return "query"
    if re.search(r"Narrative Technical Explainer", t, flags=re.IGNORECASE):
        return "story"
    if re.search(r"Buyer-Friendly Playbook", t, flags=re.IGNORECASE):
        return "playbook"
    if re.search(r"A Practical End-to-End Guide", t, flags=re.IGNORECASE):
        return "pillar"
    # If playbook-style sections exist, assume playbook.
    if re.search(r"(?im)^\s*##\s*Specifications\s+to\s+define\s+upfront\b", t):
        return "playbook"
    return "unknown"


_TITLE_STOP_WORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "but",
    "by",
    "for",
    "from",
    "in",
    "into",
    "nor",
    "of",
    "on",
    "or",
    "over",
    "per",
    "the",
    "to",
    "up",
    "vs",
    "via",
    "with",
    "without",
}

_TITLE_ACRONYMS = {
    "pcb",
    "pcba",
    "fpc",
    "mcpcb",
    "dfm",
    "dft",
    "aoi",
    "spi",
    "ict",
    "fct",
    "vna",
    "emi",
    "esd",
    "rf",
    "rfq",
    "faq",
    "mes",
    "spc",
    "fpy",
    "adas",
    "lidar",
    "rffe",
    "lna",
    "pa",
    "v2x",
    "ul",
    "ce",
    "ipc",
    "iq",
    "smt",
    "tht",
    "bga",
    "qfn",
    "qfp",
    "lga",
    "ldo",
    "mosfet",
    "enig",
    "osp",
    "hasl",
    "enepig",
    "mtbf",
    "hal",
    "halt",
    "hass",
    "cxl",
    "pam4",
    "nrz",
    "tdr",
}


def _title_case_en(text: str) -> str:
    s = (text or "").strip()
    if not s:
        return s

    # Preserve inside backticks by temporarily masking.
    code_spans: List[str] = []

    def mask(m: re.Match) -> str:
        code_spans.append(m.group(0))
        return f"__CODE{len(code_spans)-1}__"

    masked = re.sub(r"`[^`]+`", mask, s)

    tokens = re.split(r"(\s+)", masked)
    out_tokens: List[str] = []
    prev_was_sep = True
    after_colon = True  # first significant word should be capitalized

    def cap_word(w: str, *, force: bool) -> str:
        # Keep punctuation around the word.
        m = re.match(r"^([^A-Za-z0-9]*)([A-Za-z0-9][A-Za-z0-9'/-]*)([^A-Za-z0-9]*)$", w)
        if not m:
            return w
        pre, core, post = m.group(1), m.group(2), m.group(3)

        core_low = core.lower()
        if core_low in _TITLE_ACRONYMS:
            core2 = core_low.upper()
        elif re.search(r"\d", core):
            core2 = core  # keep tokens with digits as-is
        elif not force and core_low in _TITLE_STOP_WORDS:
            core2 = core_low
        else:
            # Hyphenated words: Title Case each segment.
            parts = core.split("-")
            parts2 = []
            for idx, part in enumerate(parts):
                pl = part.lower()
                if pl in _TITLE_ACRONYMS:
                    parts2.append(pl.upper())
                elif idx > 0 and pl in _TITLE_STOP_WORDS:
                    parts2.append(pl)
                elif part:
                    parts2.append(part[0].upper() + part[1:].lower())
                else:
                    parts2.append(part)
            core2 = "-".join(parts2)
        return pre + core2 + post

    for t in tokens:
        if t.isspace():
            out_tokens.append(t)
            continue
        force = after_colon
        # Determine if this token ends a sentence/segment.
        cased = cap_word(t, force=force)
        out_tokens.append(cased)
        after_colon = bool(re.search(r"[:.!?]\s*$", t))
        prev_was_sep = False

    cased = "".join(out_tokens)

    # Unmask code spans.
    for i, span in enumerate(code_spans):
        cased = cased.replace(f"__CODE{i}__", span)
    return cased


def ensure_title_case_and_headings(markdown: str, *, language: str) -> str:
    """Title-case front matter title + all markdown headings (English only)."""
    if language != "英文":
        return (markdown or "").strip() + "\n"
    text = (markdown or "").strip() + "\n"
    split = _split_yaml_front_matter_lines(text)
    if not split:
        return text
    fm_lines, body_lines = split

    title = (_front_matter_get_value(fm_lines, "title") or "").strip()
    if title:
        new_title = _title_case_en(title)
        if new_title and new_title != title:
            fm_lines = _front_matter_set_value(fm_lines, "title", new_title)

    # Title-case headings (H1..H6), casing only.
    for i, line in enumerate(body_lines):
        m = re.match(r"^(\s*#{1,6}\s+)(.+?)\s*$", line)
        if not m:
            continue
        prefix, heading = m.group(1), m.group(2)
        # Skip component markers and empty headings.
        if "<!--" in heading or not heading.strip():
            continue
        body_lines[i] = prefix + _title_case_en(heading.strip())

    out = "\n".join(fm_lines + body_lines).strip() + "\n"
    return out

def ensure_hero_image(content: str, fallback_hero_image_path: str) -> str:
    """
    Ensure a deterministic hero image exists for SEO/UX consistency.
    - If front matter `image:` is set to a valid `/assets/img/...`, it wins (manual override).
    - Otherwise uses `fallback_hero_image_path`.
    - Sets front matter `image:` if empty/missing.
    - Inserts (or replaces) a single markdown hero image right after H1.
    """
    split = _split_yaml_front_matter_lines(content or "")
    if not split:
        return (content or "").strip() + "\n"
    fm_lines, body_lines = split

    # Manual override: prefer front matter image when valid.
    fm_image = (_front_matter_get_value(fm_lines, "image") or "").strip()
    fm_image = fm_image.strip('"').strip("'").strip()
    if fm_image.startswith("/assets/img/"):
        hero = fm_image
    else:
        hero = (fallback_hero_image_path or "").strip()
        if not hero.startswith("/assets/img/"):
            return (content or "").strip() + "\n"

    title = _front_matter_get_value(fm_lines, "title") or ""
    if not title:
        for line in body_lines[:80]:
            m = re.match(r"^\s*#\s+(.*)$", line)
            if m:
                title = m.group(1).strip()
                break
    alt_text = title or "APTPCB"

    # 1) Set front matter image if it's empty/missing.
    image_val = _front_matter_get_value(fm_lines, "image")
    if image_val is None:
        # Insert just before closing delimiter (the last line is '---').
        fm_lines = fm_lines[:-1] + [f'image: "{hero}"'] + fm_lines[-1:]
    else:
        if not str(image_val).strip() or str(image_val).strip().lower() in {"null", "none"}:
            for idx in range(1, len(fm_lines) - 1):
                if re.match(r"^\s*image\s*:", fm_lines[idx]):
                    fm_lines[idx] = f'image: "{hero}"'
                    break
        # Otherwise keep existing non-empty image.

    # 2) Ensure body has a hero image right after H1 (insert or replace).
    # Find the first H1.
    h1_idx = None
    for i, line in enumerate(body_lines[:200]):
        if re.match(r"^\s*#\s+\S", line):
            h1_idx = i
            break
        # If the body starts with H2, we still want to insert after it? Prefer not.
    if h1_idx is not None:
        # If a hero image already appears immediately after H1 (allow blank lines), do nothing.
        scan = h1_idx + 1
        while scan < len(body_lines) and not body_lines[scan].strip():
            scan += 1
        if scan < len(body_lines) and re.match(r"^!\[.*\]\(/assets/img/", body_lines[scan].strip()):
            # Replace existing hero image to match selected hero.
            hero_line = f"![{alt_text}]({hero})"
            body_lines[scan] = hero_line
        else:
            # Insert before the first non-blank line after H1.
            insert_at = h1_idx + 1
            while insert_at < len(body_lines) and not body_lines[insert_at].strip():
                insert_at += 1
            hero_line = f"![{alt_text}]({hero})"
            body_lines = body_lines[:insert_at] + ["", hero_line, ""] + body_lines[insert_at:]

    out = "\n".join(fm_lines + body_lines).strip() + "\n"
    return out

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


def _meaningful_slug_suffix_candidates(
    *,
    base_slug: str,
    keyword: Optional[str],
    lsi_keywords: Optional[List[str]],
    kind: str,
) -> List[str]:
    base_tokens = {t for t in (base_slug or "").split("-") if t}
    cands: List[str] = []
    stop = {
        "a",
        "an",
        "and",
        "as",
        "at",
        "by",
        "for",
        "from",
        "in",
        "into",
        "of",
        "on",
        "or",
        "over",
        "per",
        "the",
        "to",
        "up",
        "vs",
        "via",
        "with",
        "without",
    }

    # 1) Use LSI phrases as meaningful disambiguators (prefer tokens not already in base slug).
    for phrase in (lsi_keywords or [])[:10]:
        s = slugify(str(phrase))
        if not s:
            continue
        s = _strip_template_suffix_from_slug(s)
        toks = [t for t in s.split("-") if t and t not in base_tokens and t not in stop]
        if not toks:
            continue
        suffix = "-".join(toks[:5]).strip("-")
        if suffix and suffix not in cands:
            cands.append(suffix)

    # 2) Heuristic keyword-derived suffixes (short, meaningful).
    kw = (keyword or "").lower()
    if any(x in kw for x in ("rfq", "quote", "quotation")) and "rfq" not in base_tokens:
        cands.append("rfq")
    if "checklist" in kw and "checklist" not in base_tokens:
        cands.append("checklist")
    if any(x in kw for x in ("dfm", "manufacturability")) and "dfm" not in base_tokens:
        cands.append("dfm")
    if any(x in kw for x in ("cost", "price")) and "cost-drivers" not in cands:
        cands.append("cost-drivers")

    # 3) Last-resort (still meaningful): add a date marker (avoids meaningless -2/-3).
    # Keep it short and stable: yyyy-mm-dd.
    date_tag = datetime.now().strftime("%Y-%m-%d")
    cands.append(date_tag)

    # Deduplicate while preserving order.
    out: List[str] = []
    for s in cands:
        s = (s or "").strip().strip("-")
        if not s:
            continue
        if s not in out:
            out.append(s)
    return out


def ensure_unique_slug(
    base_slug: str,
    *,
    keyword: Optional[str] = None,
    lsi_keywords: Optional[List[str]] = None,
    kind: str = "unknown",
) -> str:
    """
    Ensure slug uniqueness without meaningless numeric suffixes when possible.
    Tries meaningful suffixes (LSI-derived / heuristics / date) before falling back to -2/-3.
    """
    slug = (base_slug or "").strip("-")
    if not slug:
        slug = f"post-{int(time.time())}"

    if slug not in USED_SLUGS:
        USED_SLUGS.add(slug)
        return slug

    for suffix in _meaningful_slug_suffix_candidates(
        base_slug=slug, keyword=keyword, lsi_keywords=lsi_keywords, kind=kind
    ):
        candidate = f"{slug}-{suffix}".strip("-")
        if candidate not in USED_SLUGS:
            USED_SLUGS.add(candidate)
            return candidate

    # Truly last resort: numeric.
    n = 2
    while True:
        candidate = f"{slug}-{n}"
        if candidate not in USED_SLUGS:
            USED_SLUGS.add(candidate)
            return candidate
        n += 1


def preview_unique_slug(
    base_slug: str,
    *,
    keyword: Optional[str] = None,
    lsi_keywords: Optional[List[str]] = None,
    kind: str = "unknown",
) -> str:
    """Preview a unique slug without mutating USED_SLUGS (useful for --dry-run)."""
    slug = (base_slug or "").strip("-")
    if not slug:
        slug = "post"

    if slug not in USED_SLUGS:
        return slug

    for suffix in _meaningful_slug_suffix_candidates(
        base_slug=slug, keyword=keyword, lsi_keywords=lsi_keywords, kind=kind
    ):
        candidate = f"{slug}-{suffix}".strip("-")
        if candidate not in USED_SLUGS:
            return candidate

    n = 2
    while True:
        candidate = f"{slug}-{n}"
        if candidate not in USED_SLUGS:
            return candidate
        n += 1

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
    # 收集候选词
    main_candidates = []
    lsi_pool = []
    
    for subsection in keywords_data.get("subsections", []):
        for keyword_obj in subsection.get("keywords", []):
            keyword_obj["subsection"] = subsection["name"]
            
            # LSI pool: include everything (even used ones can be LSIs)
            lsi_pool.append(keyword_obj)

            # Main Keyword Selection Logic
            if KEYWORD_SEARCH_FILTER:
                # Search mode: Must match filter. Ignore 'used' status.
                if KEYWORD_SEARCH_FILTER.lower() in keyword_obj["keyword"].lower():
                    main_candidates.append(keyword_obj)
            else:
                # Normal mode: Must NOT be used.
                if not keyword_obj.get("used", False):
                     if KEYWORD_INTENT != "auto":
                        if keyword_obj.get("intent") != KEYWORD_INTENT:
                            continue
                     main_candidates.append(keyword_obj)
    
    if not main_candidates:
        if KEYWORD_SEARCH_FILTER:
            return None, []

        if KEYWORD_INTENT != "auto":
            # Fallback: if no intent-matching keyword remains, relax the filter.
            print(f"⚠️ 没有找到 intent={KEYWORD_INTENT} 的未使用关键词，回退为任意未使用关键词")
            old_intent = KEYWORD_INTENT
            try:
                globals()["KEYWORD_INTENT"] = "auto"
                return select_keywords(keywords_data)
            finally:
                globals()["KEYWORD_INTENT"] = old_intent
        
        # print("❌ 没有找到未使用的关键词") # Suppressed by previous fix logic
        return None, []
    
    # 优先从 "Manufacturing & Assembly" 子类选择主关键词
    ma_candidates = [kw for kw in main_candidates if kw.get("subsection") == "Manufacturing & Assembly"]
    main_pool = ma_candidates if ma_candidates else main_candidates
    main_keyword = random.choice(main_pool)
    
    def _keyword_tokens(text: str) -> set:
        text = text.lower()
        tokens = re.findall(r"[a-z0-9]+", text)
        stop = {
            "the", "and", "or", "for", "of", "to", "in", "on", "with", "without",
            "a", "an", "vs", "how", "what", "when", "why", "guide", "checklist",
            "best", "practices", "rules", "design", "manufacturing", "assembly",
            "pcb", "pcba",
        }
        return {t for t in tokens if t not in stop and len(t) > 1}

    def _similarity(a: str, b: str) -> float:
        ta = _keyword_tokens(a)
        tb = _keyword_tokens(b)
        if not ta or not tb:
            return 0.0
        inter = len(ta & tb)
        union = len(ta | tb)
        return inter / union if union else 0.0

    # Prefer LSI keywords from the same subsection, and rank by token overlap to avoid topic drift.
    candidates = [
        kw for kw in lsi_pool
        if kw["subsection"] == main_keyword["subsection"] and kw != main_keyword
    ]

    scored = []
    for kw in candidates:
        scored.append((kw, _similarity(main_keyword["keyword"], kw["keyword"])))
    scored.sort(key=lambda x: x[1], reverse=True)

    # Pick up to 5 LSI keywords with non-zero similarity. If not enough, pick the best few anyway.
    picked: List[Dict] = []
    for kw, score in scored:
        if len(picked) >= 5:
            break
        if score <= 0 and len(picked) >= 2:
            continue
        picked.append(kw)

    lsi_keyword_names = [kw["keyword"] for kw in picked]
    
    return main_keyword, lsi_keyword_names

def get_least_used_template(
    templates_dir: Path,
    keywords_data: Dict,
    *,
    template_files: Optional[List[Path]] = None,
) -> Optional[Path]:
    """根据使用次数选择最少使用的模板文件"""
    template_files = template_files or list(templates_dir.glob("*.md"))
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
    else:
        # If new templates are introduced later, don't let them dominate selection by
        # defaulting to 0; instead align them with the current minimum usage in this
        # category so auto runs keep a mix of templates.
        candidate_names = {p.name for p in template_files}
        existing_counts = []
        for name, meta in template_stats.items():
            if name not in candidate_names:
                continue
            if not isinstance(meta, dict):
                continue
            existing_counts.append(meta.get("usage_count", 0))
        default_usage = min(existing_counts) if existing_counts else 0
        for template_file in template_files:
            if template_file.name not in template_stats:
                template_stats[template_file.name] = {
                    "usage_count": default_usage,
                    "last_used": None,
                    "created_blogs": []
                }
    
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
    
    
    # --- Asset Image Pool Injection (Simple Full Dump) ---
    assets_image_pool_str = "<!-- No image catalog found. Use placeholders. -->"
    try:
        # Assuming PROMPTS_DIR is available specifically, or hardcoding relative path for APTPCB
        # We try to locate the file in specific known locations relative to CWD or prompts_dir (if available)
        catalog_candidates = [
            Path("prompts_aptpcb/assets-img-filenames.md"),
            Path("prompts_aptpcb/blogs_prompt_v6/assets-img-filenames.md"),
             Path("prompts_aptpcb/blogs_prompt_v5/assets-img-filenames.md")
        ]
        
        for cand in catalog_candidates:
            if cand.exists():
                assets_image_pool_str = cand.read_text(encoding='utf-8')
                print(f"🖼️  Loaded image catalog from: {cand}")
                break
                
    except Exception as e:
        print(f"⚠️ Image catalog load error: {e}")

    # 替换变量
    filled_template = template_content.replace("{{keyword}}", keyword)
    filled_template = filled_template.replace("{{lsi}}", ", ".join(lsi_keywords))
    filled_template = filled_template.replace("{{date}}", date_str)
    filled_template = filled_template.replace("{{tags}}", tags_str)
    filled_template = filled_template.replace("{{assets_image_pool}}", assets_image_pool_str)
    
    return filled_template


def _compact_v2_prompt(
    *,
    kind: str,
    keyword: str,
    lsi_keywords: List[str],
    internal_link_pool: str,
    assets_image_pool: str,
    modules_text: str,
) -> str:
    """
    Build a shorter, higher-compliance v2 prompt (the raw template files are intentionally verbose).
    This is used to reduce "starts in the middle" failures on some model endpoints.
    """
    date_str = datetime.now().strftime("%Y-%m-%d")
    tags = [keyword] + [s for s in (lsi_keywords or []) if s][:8]
    tags_str = json.dumps(tags, ensure_ascii=False)
    lsi_inline = ", ".join(lsi_keywords or [])

    common_rules = f"""Output Markdown only.
The first character MUST be `---` (YAML front matter). No preface, no analysis.
Language: English (US). Short sentences; translation-friendly.
Images:
- Insert **at least 2 images total** (hero + at least 1 in-body); do not exceed 3 images total.
- Only use `/assets/img/...` paths from the provided image pool. No external images.
- If you insert a hero image, it MUST appear immediately after the H1 and the YAML `image:` must match that hero path.
Do not mention SEO/SERP/PAA in the article.
Use `- ` bullets, `1. ` numbered lists, and Markdown tables.
Expand acronyms on first mention (e.g., Printed circuit board (PCB), Design for manufacturability (DFM)).
Headings:
- Use Title Case for H1/H2/H3.
- Avoid repeating the full primary keyword in every H2; keep H2 short and natural.

Quality bar (A-grade):
- Start with 2–3 sentence opening (no tables/headings first).
- Include at least 12 concrete numeric ranges/limits across the article.
- Every major section must include: a rule/range, why it matters, how to verify, and a common failure/pitfall.
- Prefer checklists, decision rules, and acceptance criteria over generic explanations.
- Avoid fluff. No “in conclusion” filler. No over-claiming; use careful wording (“typically”, “often”) when unsure.

Primary keyword: {keyword}
LSI keywords (use naturally; no stuffing): {lsi_inline}
"""

    resources = f"""Internal link pool (choose 6–10; distribute across the article; do not paste this list into the article):
{internal_link_pool.strip()}

Assets image pool (choose 2–3 total; hero + at least 1 in-body; do not paste this list into the article):
{assets_image_pool.strip()}
"""

    modules = (modules_text or "").strip()
    if modules:
        modules = "Optional modules (apply when relevant):\n" + modules + "\n"

    if kind == "query":
        return (
            common_rules
            + "\nWord count target: **2000–2800 words**.\n"
            + "\n"
            + modules
            + resources
            + f"""
Now output the full article in this exact order:
---
title: "{keyword}: Practical Rules, Specs, and Troubleshooting Guide"
description: "A practical guide to {keyword} with clear rules, recommended ranges, verification steps, and common failure fixes."
category: technology
date: "{date_str}"
featured: true
image: ""
readingTime: 9
tags: {tags_str}
---

# {keyword}: Practical Rules, Specs, and Troubleshooting Guide

Write a 2–3 sentence answer-first opening.

## Quick Answer (30 seconds)
Write 5–7 bullets that include: one rule/range, one pitfall, one verification method, one boundary case, one DFM/RFQ item.

Write **Highlights** (5–7 bullets) (no H2).

### Contents
Add 6–10 anchor links to the H2 sections below.

## Definition and Scope (What It Is, What It Isn’t)
Include: “applies when” (3–5 bullets) and “doesn’t apply when” (3–5 bullets).

## Rules and Specifications (Key Parameters and Limits)
Create a Markdown table: `Rule | Recommended value/range | Why it matters | How to verify | If ignored` (>= 8 rows).

## Implementation Steps (Process Checkpoints)
Write 6–10 steps; each step includes: action, key parameters, acceptance check.

## Troubleshooting (Failure Modes and Fixes)
Write 6–10 items: Symptom → likely causes → checks → fix → prevention.

## How to Choose (Design Decisions and Trade-Offs)
Write 6–10 “If..., choose...” decision rules.

## FAQ (Cost, Lead Time, Materials, Testing, Acceptance Criteria)
Write 8–10 questions; each answer: 1–2 sentence direct answer + 2–4 bullets.

## Glossary (Key Terms)
Create a Markdown table (>= 8 rows): `Term | Meaning | Why it matters in practice`.

## Request a Quote (DFM Review + Pricing)
<!-- COMPONENT: BlogQuickQuoteInline -->
Write 1 short paragraph + 6–10 bullets: what to send for DFM/quote.

## Conclusion (next steps)
2–4 sentences; restate {keyword}; no aggressive CTA.
"""
        ).strip() + "\n"

    if kind == "pillar":
        return (
            common_rules
            + "\nWord count target: **2300–3200 words**.\n"
            + "\n"
            + modules
            + resources
            + """
Section hard requirements (do not skip):
- Key Takeaways: 7 bullets; include 2 numeric thresholds and 1 validation tip.
- Metrics That Matter: 2 tables total (>= 10 metric rows across tables) and at least 6 numeric ranges.
- How to Choose: 10 decision rules in “If…, choose…” form.
- Implementation Checkpoints: 10 steps; each step includes action + acceptance check; include at least 3 measurable acceptance criteria.
- Common Mistakes: 8 items; each includes mistake → impact → fix → how to verify.
- FAQ: 8 questions; each answer has 1–2 sentences + 3 bullets; include lead time + cost + testing.
- Glossary: table with >= 12 rows.
"""
            + f"""
Now output the full article in this exact order:
---
title: "{keyword}: A Practical End-to-End Guide (from basics to production)"
description: "Learn {keyword} from definition to production: key metrics, selection trade-offs, implementation checkpoints, and acceptance criteria."
category: technology
date: "{date_str}"
featured: true
image: ""
readingTime: 10
tags: {tags_str}
---

# {keyword}: A Practical End-to-End Guide (from basics to production)

Write a 2–3 sentence definition-first opening.

## Key Takeaways
Write 5–7 bullets (definition, metrics, misconception, validation tip, decision rule).

<!-- COMPONENT: BlogQuickQuoteInline -->

### Contents
Add 7–10 anchor links to the H2 sections below.

## What It Really Means (Scope & Boundaries)

## Metrics That Matter (How to Evaluate It)
Include at least 1 Markdown table.

## How to Choose (Selection Guidance by Scenario)

## Implementation Checkpoints (Design to Manufacturing)

## Common Mistakes (and the Correct Approach)

## FAQ (Cost, Lead Time, Materials, Testing, Acceptance Criteria)
Write 6–8 questions; each answer: 1–2 sentences + 2–4 bullets.

## Glossary (key terms)
Markdown table (>= 10 rows).

## Conclusion (next steps)
"""
        ).strip() + "\n"

    if kind == "playbook":
        return (
            common_rules
            + "\nWord count target: **2200–3000 words**.\n"
            + "\n"
            + modules
            + resources
            + """
Section hard requirements (do not skip):
- Key Takeaways: 7 bullets; include 2 numeric thresholds and 1 validation tip.
- Scope/Success Criteria: include 3 measurable success metrics + 2 boundary cases.
- Specifications Upfront: >= 12 bullets + a table of key parameters (>= 8 rows).
- Key Risks: 8 risks; each is root cause → early detection → prevention; include at least 4 numeric limits.
- Validation & Acceptance: include 1 acceptance criteria table + 6 test items; include sampling/coverage hints.
- Supplier Qualification Checklist: >= 12 checklist bullets, include traceability + DFM + test coverage + change control.
- How to Choose: 10 decision rules in “If…, choose…” form.
- FAQ: 8 questions; each answer has 1–2 sentences + 3 bullets.
- Glossary: table with >= 10 rows.
"""
            + f"""
Now output the full article in this exact order:
---
title: "{keyword}: Buyer-Friendly Playbook (Specs, Risks, Checklist)"
description: "A practical playbook for {keyword}: requirements to define upfront, key risks, validation plan, and a supplier qualification checklist."
category: technology
date: "{date_str}"
featured: true
image: ""
readingTime: 10
tags: {tags_str}
---

# {keyword}: Buyer-Friendly Playbook (Specs, Risks, Checklist)

Write a 2–3 sentence opening framed as a buyer decision.

## Key Takeaways
Write 7 bullets (include 2 numeric thresholds and 1 validation tip).

### Contents
Add 7–10 anchor links to the H2 sections below.

## Scope, Decision Context, and Success Criteria

## Specifications to Define Upfront (Before You Commit)

## Key Risks (Root Causes, Early Detection, Prevention)

## Validation & Acceptance (Tests and Pass Criteria)

## Supplier qualification checklist (RFQ, audit, traceability)

## How to Choose (Trade-Offs and Decision Rules)

## FAQ (cost, lead time, DFM files, materials, testing)
Write 6–8 questions; each answer: 1–2 sentences + 2–4 bullets.

## Request a quote / DFM review for {keyword} (what to send)
<!-- COMPONENT: BlogQuickQuoteInline -->

## Glossary (Key Terms)
Markdown table (>= 10 rows).

## Conclusion (next steps)
"""
        ).strip() + "\n"

    # Fallback: return the original content unmodified.
    return common_rules + "\n" + resources + "\n"


def _compact_v3_prompt(
    *,
    kind: str,
    keyword: str,
    lsi_keywords: List[str],
    internal_link_pool: str,
    assets_image_pool: str,
    modules_text: str,
) -> str:
    """
    v3 prompt variant (based on v2) with layout boosters inspired by
    `iphone-consumer-electronics.md`:
    - narrative hook in the opening
    - a compact “Tech/Decision Lever → Practical Impact” matrix block near the top
    """
    base = _compact_v2_prompt(
        kind=kind,
        keyword=keyword,
        lsi_keywords=lsi_keywords,
        internal_link_pool=internal_link_pool,
        assets_image_pool=assets_image_pool,
        modules_text=modules_text,
    )

    matrix_block = (
        "\nInsert this compact matrix block (no H2). Keep it factual; avoid vendor claims. "
        "Replace all `…` placeholders with real content (no ellipsis in the final output).\n"
        "<div style=\"background-color:#F5F7FA;padding:18px;border-radius:10px;margin:20px 0;\">\n"
        "<h3 style=\"margin:0 0 12px 0;color:#000000;\">Tech / Decision Lever → Practical Impact</h3>\n"
        "<table style=\"width:100%;border-collapse:collapse;text-align:left;color:#000000;\">\n"
        "<thead style=\"background-color:#F0F0F0;\">\n"
        "<tr>\n"
        "<th style=\"padding:10px;border:1px solid #ddd;\">Decision lever</th>\n"
        "<th style=\"padding:10px;border:1px solid #ddd;\">Practical impact (yield / reliability / cost / lead time)</th>\n"
        "</tr>\n"
        "</thead>\n"
        "<tbody>\n"
        "<tr><td style=\"padding:10px;border:1px solid #ddd;\">…</td><td style=\"padding:10px;border:1px solid #ddd;\">…</td></tr>\n"
        "<tr><td style=\"padding:10px;border:1px solid #ddd;\">…</td><td style=\"padding:10px;border:1px solid #ddd;\">…</td></tr>\n"
        "<tr><td style=\"padding:10px;border:1px solid #ddd;\">…</td><td style=\"padding:10px;border:1px solid #ddd;\">…</td></tr>\n"
        "<tr><td style=\"padding:10px;border:1px solid #ddd;\">…</td><td style=\"padding:10px;border:1px solid #ddd;\">…</td></tr>\n"
        "<tr><td style=\"padding:10px;border:1px solid #ddd;\">…</td><td style=\"padding:10px;border:1px solid #ddd;\">…</td></tr>\n"
        "<tr><td style=\"padding:10px;border:1px solid #ddd;\">…</td><td style=\"padding:10px;border:1px solid #ddd;\">…</td></tr>\n"
        "</tbody>\n"
        "</table>\n"
        "</div>\n"
    )

    if kind == "query":
        needle = "Write **Highlights** (5–7 bullets) (no H2).\n\n### Contents\n"
        if needle in base:
            base = base.replace(needle, "Write **Highlights** (5–7 bullets) (no H2).\n" + matrix_block + "\n### Contents\n", 1)
        base = base.replace(
            "Write a 2–3 sentence answer-first opening.\n",
            "Write a 2–3 sentence answer-first opening. Start with a 1–2 sentence scenario hook, then define the term.\n",
            1,
        )
        return base

    if kind == "pillar":
        needle = "<!-- COMPONENT: BlogQuickQuoteInline -->\n\n### Contents\n"
        if needle in base:
            base = base.replace(needle, matrix_block + "\n<!-- COMPONENT: BlogQuickQuoteInline -->\n\n### Contents\n", 1)
        base = base.replace(
            "Write a 2–3 sentence definition-first opening.\n",
            "Write a 2–3 sentence opening. Start with a 1–2 sentence scenario hook, then define the term.\n",
            1,
        )
        return base

    if kind == "playbook":
        needle = "Write 7 bullets (include 2 numeric thresholds and 1 validation tip).\n\n### Contents\n"
        if needle in base:
            base = base.replace(
                needle,
                "Write 7 bullets (include 2 numeric thresholds and 1 validation tip).\n" + matrix_block + "\n### Contents\n",
                1,
            )
        base = base.replace(
            "Write a 2–3 sentence opening framed as a buyer decision.\n",
            "Write a 2–3 sentence opening framed as a buyer decision. Start with a 1–2 sentence scenario hook.\n",
            1,
        )
        return base

    return base


def _default_internal_link_pool_file(prompts_dir: Path) -> Optional[Path]:
    """Best-effort auto-detect internal link pool file for APTPCB prompts."""
    try:
        if "prompts_aptpcb" not in str(prompts_dir):
            return None
        repo_root = Path(__file__).resolve().parent
        candidate = repo_root / "prompts_aptpcb" / "internal_link_pool.md"
        return candidate if candidate.exists() else None
    except Exception:
        return None


def _default_assets_image_catalog_file(prompts_dir: Path) -> Optional[Path]:
    """Best-effort auto-detect assets image catalog file for APTPCB prompts."""
    try:
        if "prompts_aptpcb" not in str(prompts_dir):
            return None
        candidate = Path("/code/hileap/frontendAPT/docs/assets-img-filenames.md")
        return candidate if candidate.exists() else None
    except Exception:
        return None


def _load_internal_link_pool_text(pool_file: Path) -> str:
    """Load internal link pool URLs and format as a bullet list for prompt injection."""
    raw = pool_file.read_text(encoding="utf-8")
    urls: List[str] = []
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("-"):
            line = line[1:].strip()
        if line.startswith("http://") or line.startswith("https://"):
            urls.append(line)
    return "\n".join(f"- {u}" for u in urls) + ("\n" if urls else "")


def extract_internal_link_pool_urls(text: str) -> List[str]:
    """Parse internal link pool bullet list into URLs."""
    urls: List[str] = []
    seen = set()
    for line in (text or "").splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("-"):
            s = s[1:].strip()
        # Strip markdown formatting if present.
        s = s.strip("`").strip()
        if not (s.startswith("http://") or s.startswith("https://")):
            continue
        if "aptpcb.com" not in s:
            continue
        if s in seen:
            continue
        seen.add(s)
        urls.append(s)
    return urls


def _title_from_url(url: str) -> str:
    """Best-effort convert URL path to readable anchor text."""
    try:
        path = urlparse(url).path.strip("/")
    except Exception:
        path = ""
    if not path:
        return "APTPCB Resource"
    # Drop language prefix.
    parts = [p for p in path.split("/") if p]
    if parts and parts[0] in {"en", "cn", "de", "fr", "it", "es", "ru", "ar"}:
        parts = parts[1:]
    if not parts:
        return "APTPCB Resource"
    last = parts[-1].replace("-", " ").strip()
    last = re.sub(r"\s+", " ", last)
    # Keep common abbreviations uppercased.
    return _title_case_en(last)


def _count_internal_links(markdown: str) -> int:
    return len(_extract_internal_link_hrefs(markdown or ""))


_INTERNAL_LANG_PREFIXES = {"en", "cn", "de", "fr", "it", "es", "ru", "ar"}
_INTERNAL_GENERIC_PATHS = {
    "/",
    "/en/",
    "/en/about/",
    "/en/blog/",
    "/en/capabilities/",
    "/en/materials/",
    "/en/pcb/",
    "/en/pcba/",
    "/en/resources/",
    "/en/tools/",
    "/en/quote/",
    "/en/contact/",
}
_INTERNAL_GENERIC_SEGMENTS = {
    "about",
    "blog",
    "capabilities",
    "materials",
    "pcb",
    "pcba",
    "resources",
    "tools",
    "quote",
    "contact",
}
_INTERNAL_STOP_TOKENS = {
    "en",
    "cn",
    "de",
    "fr",
    "it",
    "es",
    "ru",
    "ar",
    "a",
    "an",
    "and",
    "or",
    "the",
    "to",
    "of",
    "for",
    "in",
    "on",
    "with",
    "without",
    "guide",
    "basics",
    "manufacturing",
    "assembly",
    "process",
    "services",
}


def _canonical_internal_href(href: str) -> Optional[str]:
    """Canonicalize an internal href to a site-relative path, ignoring query/hash."""
    s = (href or "").strip()
    if not s:
        return None
    if s.startswith("http://") or s.startswith("https://"):
        try:
            u = urlparse(s)
        except Exception:
            return None
        if "aptpcb.com" not in (u.netloc or ""):
            return None
        path = u.path or "/"
    elif s.startswith("/"):
        path = s
    else:
        return None
    path = path.split("#", 1)[0].split("?", 1)[0].strip()
    if not path.startswith("/"):
        path = "/" + path
    return path


def _extract_internal_link_hrefs(markdown: str) -> set[str]:
    """Extract unique internal links from markdown (absolute aptpcb.com + site-relative), excluding images/assets."""
    text = markdown or ""
    found: set[str] = set()
    # Absolute.
    for u in re.findall(r"\]\((https?://aptpcb\.com[^)\s]+)\)", text):
        canon = _canonical_internal_href(u)
        if canon:
            found.add(canon)
    # Relative links (exclude images via (?<!\!)).
    for u in re.findall(r"(?<!\!)\]\((/[^)\s]+)\)", text):
        canon = _canonical_internal_href(u)
        if not canon:
            continue
        if canon.startswith("/assets/"):
            continue
        found.add(canon)
    return found


def _internal_path_tokens(href_or_url: str) -> set[str]:
    canon = _canonical_internal_href(href_or_url) or ""
    if not canon:
        return set()
    parts = [p for p in canon.strip("/").split("/") if p]
    if parts and parts[0] in _INTERNAL_LANG_PREFIXES:
        parts = parts[1:]
    slug = " ".join(parts)
    toks = set(_tokenize_for_assets(slug))
    toks = {t for t in toks if t and t not in _INTERNAL_STOP_TOKENS}
    return toks


def _internal_path_depth(href_or_url: str) -> int:
    canon = _canonical_internal_href(href_or_url) or ""
    parts = [p for p in canon.strip("/").split("/") if p]
    if parts and parts[0] in _INTERNAL_LANG_PREFIXES:
        parts = parts[1:]
    return len(parts)


def _internal_generic_penalty(href_or_url: str) -> int:
    canon = _canonical_internal_href(href_or_url) or ""
    if not canon:
        return 100
    if canon in _INTERNAL_GENERIC_PATHS:
        return 80
    parts = [p for p in canon.strip("/").split("/") if p]
    if parts and parts[0] in _INTERNAL_LANG_PREFIXES:
        parts = parts[1:]
    if len(parts) <= 1:
        return 40
    if parts and parts[0] in _INTERNAL_GENERIC_SEGMENTS and len(parts) == 1:
        return 40
    return 0


def _select_internal_link_picks(
    *,
    markdown: str,
    internal_urls: List[str],
    existing_hrefs: set[str],
    need: int,
    keyword: Optional[str],
    lsi_keywords: Optional[List[str]],
) -> List[str]:
    """Pick the most relevant internal links from the pool; returns site-relative hrefs."""
    if need <= 0:
        return []

    context_text = keyword or ""
    if lsi_keywords:
        context_text += " " + " ".join(lsi_keywords)
    # Add headings for extra relevance.
    body = markdown or ""
    headings = re.findall(r"(?m)^\s*##+\s+(.+?)\s*$", body)
    if headings:
        context_text += " " + " ".join(headings[:30])

    context_tokens = set(_tokenize_for_assets(context_text))
    context_tokens = {t for t in context_tokens if t and t not in _INTERNAL_STOP_TOKENS}

    candidates: List[tuple[int, str]] = []
    for u in internal_urls or []:
        canon = _canonical_internal_href(u)
        if not canon:
            continue
        if canon in existing_hrefs:
            continue
        depth = _internal_path_depth(canon)
        toks = _internal_path_tokens(canon)
        overlap = len(toks & context_tokens)
        penalty = _internal_generic_penalty(canon)
        # Prefer depth, then lexical overlap.
        score = overlap * 10 + min(depth, 5) * 2 - penalty
        candidates.append((score, canon))

    candidates.sort(key=lambda x: x[0], reverse=True)
    picks: List[str] = []
    seen: set[str] = set()
    for score, canon in candidates:
        if canon in seen:
            continue
        seen.add(canon)
        picks.append(canon)
        if len(picks) >= need:
            break
    return picks


def ensure_internal_links(
    markdown: str,
    *,
    internal_urls: List[str],
    min_links: int = 6,
    max_links: int = 10,
    keyword: Optional[str] = None,
    lsi_keywords: Optional[List[str]] = None,
) -> str:
    """
    Ensure the article contains at least `min_links` aptpcb.com internal links.
    Inserts a short "Related resources" list near the end of selected sections.
    """
    text = (markdown or "").strip() + "\n"
    if not internal_urls:
        return text

    existing_hrefs = _extract_internal_link_hrefs(text)
    count = len(existing_hrefs)
    if count >= min_links:
        return text

    needed = min_links - count
    picks = _select_internal_link_picks(
        markdown=text,
        internal_urls=internal_urls,
        existing_hrefs=existing_hrefs,
        need=max(0, min(needed, max_links - count)),
        keyword=keyword,
        lsi_keywords=lsi_keywords,
    )
    if not picks:
        return text

    kind = _infer_article_kind_from_content(text)
    # Choose insertion targets by kind.
    if kind == "playbook":
        targets = [
            r"Specifications\s+to\s+Define\s+Upfront",
            r"Supplier\s+Qualification\s+Checklist",
            r"Request\s+a\s+Quote",
        ]
    elif kind == "pillar":
        targets = [
            r"Metrics\s+That\s+Matter",
            r"How\s+to\s+Choose",
            r"Implementation\s+Checkpoints",
        ]
    else:  # query/unknown
        targets = [
            r"Rules\s+and\s+Specifications",
            r"Troubleshooting",
            r"Request\s+a\s+Quote",
        ]

    split = _split_yaml_front_matter_lines(text)
    if not split:
        return text
    fm_lines, body_lines = split

    # Distribute picks across targets (1–2 per section).
    remaining = list(picks)
    for heading_regex in targets:
        if not remaining:
            break
        bounds = _find_section_bounds(body_lines, heading_regex)
        if not bounds:
            continue
        start, end = bounds
        # Insert before the next H2 (end), but after some content.
        insert_at = end
        block_urls = remaining[:2]
        remaining = remaining[2:]
        lines = ["", "**Related resources**"]
        for u in block_urls:
            lines.append(f"- [{_title_from_url(u)}]({u})")
        lines.append("")
        body_lines = body_lines[:insert_at] + lines + body_lines[insert_at:]

    out = "\n".join(fm_lines + body_lines).strip() + "\n"
    # If still short and we have room, append to the end (before Conclusion if present).
    current = _count_internal_links(out)
    if current < min_links:
        # Don't exceed max_links; only add what we need to reach min_links (up to cap).
        can_add = max(0, max_links - current)
        need = min(min_links - current, can_add)
        if need > 0:
            existing2 = _extract_internal_link_hrefs(out)
            leftovers = _select_internal_link_picks(
                markdown=out,
                internal_urls=internal_urls,
                existing_hrefs=existing2,
                need=need,
                keyword=keyword,
                lsi_keywords=lsi_keywords,
            )
            if leftovers:
                block_lines = ["", "**Related resources**"]
                block_lines += [f"- [{_title_from_url(u)}]({u})" for u in leftovers]
                block_lines.append("")
                out = _insert_section_before_conclusion(out, "\n".join(block_lines))
    return out


def prune_generic_related_resources_blocks(markdown: str) -> str:
    """
    Remove clearly-generic links (home/about/blog/capabilities index, etc.) from
    '**Related resources**' blocks to keep internal links relevant.
    """
    text = (markdown or "").strip() + "\n"
    split = _split_yaml_front_matter_lines(text)
    if not split:
        return text
    fm_lines, body_lines = split

    i = 0
    while i < len(body_lines):
        if body_lines[i].strip() != "**Related resources**":
            i += 1
            continue

        j = i + 1
        bullets: List[str] = []
        while j < len(body_lines) and body_lines[j].strip():
            line = body_lines[j].rstrip("\n")
            m = re.match(r"^\s*[-*]\s+\[[^\]]+\]\(([^)]+)\)\s*$", line)
            if m:
                href = m.group(1).strip()
                canon = _canonical_internal_href(href)
                if canon and _internal_generic_penalty(canon) >= 40:
                    # drop generic
                    pass
                else:
                    bullets.append(line)
            else:
                bullets.append(line)
            j += 1

        # Replace block [i:j) (excluding blank line at j) with pruned content.
        if bullets:
            replacement = ["**Related resources**"] + bullets
            body_lines = body_lines[:i] + replacement + body_lines[j:]
            i += len(replacement)
        else:
            # Drop the whole block heading; keep the blank separator (if any) as-is.
            body_lines = body_lines[:i] + body_lines[j:]
        continue

    return "\n".join(fm_lines + body_lines).strip() + "\n"


def fix_malformed_conclusion_heading(markdown: str) -> str:
    """Fix cases like '## Conclusion`...`' where the paragraph is glued to the heading."""
    text = (markdown or "").strip() + "\n"
    # Only fix when "Conclusion" is immediately followed by non-space and not a parenthetical subtitle.
    def repl(m: re.Match) -> str:
        head = m.group(1).rstrip()
        rest = m.group(2).strip()
        return f"{head}\n\n{rest}"

    text = re.sub(r"(?m)^(\s*##\s*Conclusion)(`.+)$", repl, text)
    # Also handle alnum glue (rare), but avoid 'Conclusion (Next Steps)'.
    text = re.sub(r"(?m)^(\s*##\s*Conclusion)([A-Za-z0-9][^\n]+)$", repl, text)
    return text.strip() + "\n"


def repair_truncated_key_takeaways(markdown: str) -> str:
    """
    If Key Takeaways contains ellipsis-truncated bullets, rebuild it deterministically from the
    rest of the article (no extra model calls). If TOC bullets leaked into the section, preserve
    them by restoring a dedicated '### Contents' block near the top.
    """
    text = (markdown or "").strip() + "\n"
    split = _split_yaml_front_matter_lines(text)
    if not split:
        return text
    fm_lines, body_lines = split

    kt_bounds = _find_section_bounds(body_lines, r"Key\s+Takeaways")
    if not kt_bounds:
        return text
    kt_start, kt_end = kt_bounds
    kt_section = "\n".join(body_lines[kt_start:kt_end])
    if not re.search(r"(?m)^\s*[-*]\s+.*(\.\.\.|…)\s*$", kt_section):
        return text

    # Preserve any TOC anchor links that were (incorrectly) placed in this section.
    toc_bullets = [
        ln.rstrip()
        for ln in body_lines[kt_start:kt_end]
        if re.match(r"^\s*[-*]\s+\[[^\]]+\]\(#[-a-z0-9]", ln.strip(), flags=re.IGNORECASE)
    ]

    # Infer a keyword-ish label from front matter.
    kw = (_front_matter_get_value(fm_lines, "title") or "").strip().strip('"').strip("'")
    tags_raw = _front_matter_get_value(fm_lines, "tags") or ""
    m = re.findall(r"""['"]([^'"]+)['"]""", str(tags_raw))
    if m and m[0].strip():
        kw = m[0].strip()
    kw = kw or "this topic"

    new_section = _build_key_takeaways_section_from_existing(text, keyword=kw).strip("\n").splitlines()
    body_lines = body_lines[:kt_start] + new_section + [""] + body_lines[kt_end:]

    # If we had a leaked TOC and there's no Contents block, insert it near the top.
    if toc_bullets and not re.search(r"(?im)^\s*###\s*Contents\b", "\n".join(body_lines[:260])):
        insert_at = None
        for i, ln in enumerate(body_lines[:260]):
            if ln.strip() == BLOG_QUICK_QUOTE_MARKER:
                insert_at = i + 1
                break
        if insert_at is None:
            insert_at = kt_start + len(new_section) + 1
        block = ["", "### Contents", ""] + toc_bullets + [""]
        body_lines = body_lines[:insert_at] + block + body_lines[insert_at:]

    return "\n".join(fm_lines + body_lines).strip() + "\n"


BLOG_QUICK_QUOTE_MARKER = "<!-- COMPONENT: BlogQuickQuoteInline -->"


def ensure_blog_quick_quote_marker(markdown: str, *, kind_hint: Optional[str] = None) -> str:
    """Ensure BlogQuickQuoteInline marker exists exactly once and is placed appropriately."""
    text = (markdown or "").strip() + "\n"
    split = _split_yaml_front_matter_lines(text)
    if not split:
        return text
    fm_lines, body_lines = split

    kind = kind_hint or _infer_article_kind_from_content(text)

    # Always normalize to exactly one marker by removing all, then inserting once.
    body_lines = [ln for ln in body_lines if ln.strip() != BLOG_QUICK_QUOTE_MARKER]

    # Insert location:
    # - query/story: inside the "Request a Quote" section (so the inline quote shows near CTA)
    # - pillar/playbook/unknown: near the top (before Contents if present, otherwise after Key Takeaways)
    insert_at = None
    if kind in {"query", "story"}:
        rq = _find_section_bounds(body_lines, r"Request\s+a\s+Quote")
        if rq:
            start, _end = rq
            insert_at = start + 1

    if insert_at is None:
        for i, ln in enumerate(body_lines[:220]):
            if re.match(r"^\s*###\s*Contents\b", ln, flags=re.IGNORECASE):
                insert_at = i
                break

    if insert_at is None:
        kt = _find_section_bounds(body_lines, r"Key\s+Takeaways")
        if kt:
            _, end = kt
            insert_at = end

    if insert_at is None:
        insert_at = 0
        for i, ln in enumerate(body_lines[:200]):
            if re.match(r"^\s*#\s+\S", ln):
                insert_at = i + 1
                while insert_at < len(body_lines) and not body_lines[insert_at].strip():
                    insert_at += 1
                if insert_at < len(body_lines) and re.match(r"^\s*!\[.*\]\(/assets/img/", body_lines[insert_at]):
                    insert_at += 1
                break

    body_lines = body_lines[:insert_at] + ["", BLOG_QUICK_QUOTE_MARKER, ""] + body_lines[insert_at:]
    return "\n".join(fm_lines + body_lines).strip() + "\n"


def fix_toc_leaked_into_key_takeaways(markdown: str) -> str:
    """Move TOC anchor links accidentally placed under Key Takeaways into a dedicated '### Contents' block."""
    text = (markdown or "").strip() + "\n"
    split = _split_yaml_front_matter_lines(text)
    if not split:
        return text
    fm_lines, body_lines = split

    kt = _find_section_bounds(body_lines, r"Key\s+Takeaways")
    if not kt:
        return text
    ks, ke = kt

    toc_bullets: List[str] = []
    cleaned_section: List[str] = []
    for ln in body_lines[ks:ke]:
        if re.match(r"^\s*[-*]\s+\[[^\]]+\]\(#[-a-z0-9]", ln.strip(), flags=re.IGNORECASE):
            toc_bullets.append(ln.rstrip())
        else:
            cleaned_section.append(ln.rstrip())
    if not toc_bullets:
        return text

    # Replace Key Takeaways section with cleaned version.
    body_lines = body_lines[:ks] + cleaned_section + body_lines[ke:]

    # If a Contents heading already exists near top, don't add another.
    if re.search(r"(?im)^\s*###\s*Contents\b", "\n".join(body_lines[:260])):
        return "\n".join(fm_lines + body_lines).strip() + "\n"

    # Insert TOC right after marker if present, otherwise after Key Takeaways section end.
    insert_at = None
    for i, ln in enumerate(body_lines[:260]):
        if ln.strip() == BLOG_QUICK_QUOTE_MARKER:
            insert_at = i + 1
            break
    if insert_at is None:
        kt2 = _find_section_bounds(body_lines, r"Key\s+Takeaways")
        insert_at = (kt2[1] if kt2 else 0)

    block = ["", "### Contents", ""] + toc_bullets + [""]
    body_lines = body_lines[:insert_at] + block + body_lines[insert_at:]
    return "\n".join(fm_lines + body_lines).strip() + "\n"


def _github_like_heading_anchor(heading: str, used: dict[str, int]) -> str:
    """
    Generate a GitHub-like anchor slug:
    - lowercase
    - remove non-alnum/non-space/non-hyphen characters (keep surrounding spaces)
    - replace spaces with hyphens (do NOT collapse consecutive hyphens)
    - de-duplicate with -1, -2, ...
    """
    s = (heading or "").strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)  # keep underscores; close enough for our renderer
    s = s.replace(" ", "-")
    s = s.strip("-")
    if not s:
        s = "section"
    n = used.get(s, 0)
    used[s] = n + 1
    if n == 0:
        return s
    return f"{s}-{n}"


def ensure_contents_toc(
    markdown: str,
    *,
    toc_over_words: int = 1800,
    max_items: int = 12,
    kind_hint: Optional[str] = None,
) -> str:
    """Ensure a '### Contents' TOC exists near the top for long pages."""
    text = (markdown or "").strip() + "\n"
    split = _split_yaml_front_matter_lines(text)
    if not split:
        return text
    fm_lines, body_lines = split

    body = "\n".join(body_lines)
    words = len(re.findall(r"\b\w+\b", body))
    if toc_over_words is not None and words < int(toc_over_words):
        return text

    # Already has a TOC near top.
    head = "\n".join(body_lines[:220]).lower()
    if re.search(r"(?m)^\s*###\s*contents\b", head):
        return text
    if re.search(r"(?m)^\s*[-*]\s+\[[^\]]+\]\(#[-a-z0-9]", head):
        return text

    # Collect H2 headings (exclude Key Takeaways / Quick Answer).
    headings: List[str] = []
    for ln in body_lines:
        m = re.match(r"^\s*##\s+(.+?)\s*$", ln)
        if not m:
            continue
        h = m.group(1).strip()
        if not h:
            continue
        if re.match(r"(?i)^key\s*takeaways\b", h):
            continue
        if re.match(r"(?i)^quick\s*answer\b", h):
            continue
        headings.append(h)
        if len(headings) >= max(6, int(max_items or 0)):
            break

    if len(headings) < 4:
        return text

    used: dict[str, int] = {}
    bullets = []
    for h in headings[: int(max_items or 12)]:
        anchor = _github_like_heading_anchor(h, used)
        bullets.append(f"- [{h}](#{anchor})")

    block = ["", "### Contents", ""] + bullets + [""]

    kind = kind_hint or _infer_article_kind_from_content(text)
    # Insert near the top:
    # - Prefer after quote marker if it appears early (<= 120 lines)
    # - Otherwise after Key Takeaways
    # - Otherwise after H1
    insert_at = None
    # NOTE: For query/story, the quote marker is intentionally near the end (inside the CTA section),
    # so we should never anchor the TOC to it.
    if kind not in {"query", "story"}:
        for i, ln in enumerate(body_lines[:140]):
            if ln.strip() == BLOG_QUICK_QUOTE_MARKER:
                insert_at = i + 1
                break
    if insert_at is None:
        kt = _find_section_bounds(body_lines, r"Key\s+Takeaways")
        if kt:
            _, end = kt
            insert_at = end
    if insert_at is None:
        insert_at = 0
        for i, ln in enumerate(body_lines[:200]):
            if re.match(r"^\s*#\s+\S", ln):
                insert_at = i + 1
                while insert_at < len(body_lines) and not body_lines[insert_at].strip():
                    insert_at += 1
                if insert_at < len(body_lines) and re.match(
                    r"^\s*!\[.*\]\(/assets/img/", body_lines[insert_at]
                ):
                    insert_at += 1
                break

    body_lines = body_lines[:insert_at] + block + body_lines[insert_at:]
    return "\n".join(fm_lines + body_lines).strip() + "\n"


def fix_story_context_heading(markdown: str, *, kind_hint: Optional[str] = None) -> str:
    """
    Story pages often used the phrase 'Became Harder', which reads like a risky claim.
    Normalize it to a neutral framing and avoid accidental time-based assertions.
    """
    text = (markdown or "").strip() + "\n"
    kind = kind_hint or _infer_article_kind_from_content(text)
    if kind != "story":
        return text
    split = _split_yaml_front_matter_lines(text)
    if not split:
        return text
    fm_lines, body_lines = split

    changed = False
    for i, ln in enumerate(body_lines):
        m = re.match(r"^\s*##\s*The\s+Context:\s*Why\s+(.+?)\s+Became\s+Harder\s*$", ln, flags=re.IGNORECASE)
        if not m:
            continue
        topic = m.group(1).strip()
        if not topic:
            continue
        body_lines[i] = f"## The Context: What Makes {topic} Challenging"
        changed = True

    if not changed:
        return text
    return "\n".join(fm_lines + body_lines).strip() + "\n"


def strip_story_key_takeaways(markdown: str, *, kind_hint: Optional[str] = None) -> str:
    """Story pages should not contain a 'Key Takeaways' section (it often duplicates TOC/highlights)."""
    text = (markdown or "").strip() + "\n"
    kind = kind_hint or _infer_article_kind_from_content(text)
    if kind != "story":
        return text
    split = _split_yaml_front_matter_lines(text)
    if not split:
        return text
    fm_lines, body_lines = split

    changed = False
    # Remove H2 Key Takeaways if present.
    bounds = _find_section_bounds(body_lines, r"Key\s*Takeaways")
    if bounds:
        start, end = bounds
        section = body_lines[start:end]
        # If the model nested other blocks (like "### Contents" / "### Highlights") under Key Takeaways,
        # we must NOT delete those; just delete the Key Takeaways heading + any immediately-following list lines.
        has_nested_h3 = any(re.match(r"^\s*###\s+\S", ln) for ln in section[1:])
        if has_nested_h3:
            del body_lines[start]  # remove heading line only
            changed = True
            # Remove leading blank/list lines that belonged to that heading, but stop at the next heading.
            i = start
            while i < len(body_lines):
                ln = body_lines[i]
                if re.match(r"^\s*#{2,6}\s+\S", ln):
                    break
                if not ln.strip() or re.match(r"^\s*[-*]\s+", ln) or re.match(r"^\s*\d+\.\s+", ln):
                    del body_lines[i]
                    changed = True
                    continue
                # Any other prose line right after the heading is also part of the takeaways; remove it until blank.
                del body_lines[i]
                changed = True
                continue
        else:
            del body_lines[start:end]
            changed = True

    # Also remove any stray H3 "Key Takeaways" blocks (rare, but seen in model outputs).
    i = 0
    while i < len(body_lines):
        if re.match(r"^\s*###\s*Key\s*Takeaways\b", body_lines[i], flags=re.IGNORECASE):
            j = i + 1
            while j < len(body_lines) and not re.match(r"^\s*#{2,6}\s+\S", body_lines[j]):
                j += 1
            del body_lines[i:j]
            changed = True
            continue
        i += 1

    if not changed:
        return text
    return "\n".join(fm_lines + body_lines).strip() + "\n"


def rebuild_contents_toc(markdown: str, *, max_items: int = 12, kind_hint: Optional[str] = None) -> str:
    """Remove an existing '### Contents' block near the top and rebuild it from current H2 headings."""
    text = (markdown or "").strip() + "\n"
    split = _split_yaml_front_matter_lines(text)
    if not split:
        return text
    fm_lines, body_lines = split

    # Remove the first Contents block within the first ~260 lines.
    head_limit = min(len(body_lines), 260)
    start = None
    for i in range(head_limit):
        if re.match(r"^\s*###\s*Contents\b", body_lines[i], flags=re.IGNORECASE):
            start = i
            break
    # Some older outputs had TOC bullets but no "### Contents" heading.
    if start is None:
        for i in range(head_limit):
            if re.match(r"^\s*[-*]\s+\[[^\]]+\]\(#[-a-z0-9]", body_lines[i].strip(), flags=re.IGNORECASE):
                start = i
                break
        if start is None:
            return ensure_contents_toc(text, toc_over_words=1800, max_items=max_items, kind_hint=kind_hint)

    end = start + 1
    # Skip blank lines right after the "### Contents" heading (or before the first bullet).
    while end < len(body_lines) and not body_lines[end].strip():
        end += 1
    while end < len(body_lines):
        if not body_lines[end].strip():
            end += 1
            break
        # Stop if another heading starts.
        if re.match(r"^\s*#{2,6}\s+\S", body_lines[end]):
            break
        # Stop if we hit a non-TOC list item (e.g., Highlights bullets).
        if start is not None and re.match(r"^\s*[-*]\s+", body_lines[end]) and not re.match(
            r"^\s*[-*]\s+\[[^\]]+\]\(#[-a-z0-9]", body_lines[end].strip(), flags=re.IGNORECASE
        ):
            break
        end += 1

    body_lines = body_lines[:start] + body_lines[end:]
    rebuilt = "\n".join(fm_lines + body_lines).strip() + "\n"
    return ensure_contents_toc(rebuilt, toc_over_words=0, max_items=max_items, kind_hint=kind_hint)


def _count_local_images(markdown: str) -> int:
    return len(re.findall(r"(?m)^!\[.*\]\(/assets/img/", markdown or ""))


def ensure_min_images(
    markdown: str,
    *,
    hero_path: str,
    candidate_paths: List[str],
    min_images: int = 2,
) -> str:
    """Ensure at least `min_images` local `/assets/img/...` images exist (hero + in-body)."""
    text = (markdown or "").strip() + "\n"
    if min_images <= 0:
        return text

    # Ensure hero first (also respects manual override).
    text = ensure_hero_image(text, hero_path)
    current = _count_local_images(text)
    if current >= min_images:
        return text

    # Pick an in-body image different from hero.
    hero = (hero_path or "").strip()
    extra = ""
    for p in candidate_paths or []:
        if not p or not p.startswith("/assets/img/"):
            continue
        if hero and p == hero:
            continue
        extra = p
        break
    if not extra:
        return text

    kind = _infer_article_kind_from_content(text)
    if kind == "playbook":
        target = r"Specifications\s+to\s+Define\s+Upfront"
    elif kind == "pillar":
        target = r"Metrics\s+That\s+Matter"
    else:
        target = r"Rules\s+and\s+Specifications"

    split = _split_yaml_front_matter_lines(text)
    if not split:
        return text
    fm_lines, body_lines = split
    bounds = _find_section_bounds(body_lines, target)
    if not bounds:
        return text
    start, end = bounds
    insert_at = start + 1
    while insert_at < end and not body_lines[insert_at].strip():
        insert_at += 1
    section_title = re.sub(r"^\s*##\s+", "", body_lines[start]).strip()
    body_lines = body_lines[:insert_at] + ["", f"![{section_title}]({extra})", ""] + body_lines[insert_at:]
    out = "\n".join(fm_lines + body_lines).strip() + "\n"
    return out


def _default_modules_dir(prompts_dir: Path) -> Optional[Path]:
    """Best-effort auto-detect modules dir for APTPCB prompts."""
    try:
        if "prompts_aptpcb" not in str(prompts_dir):
            return None
        candidate = prompts_dir / "_modules_v1"
        return candidate if candidate.exists() else None
    except Exception:
        return None


def load_assets_image_catalog_paths(catalog_file: Path) -> List[str]:
    """Load `/assets/img/...` paths from a markdown catalog file."""
    raw = catalog_file.read_text(encoding="utf-8", errors="ignore")
    paths: List[str] = []
    seen = set()
    for line in raw.splitlines():
        s = line.strip()
        if not s or not s.startswith("-"):
            continue
        s = s[1:].strip()
        if not s.startswith("`"):
            # allow plain - /assets/img/... and - `/assets/img/...`
            pass
        s = s.strip("`").strip()
        if not s.startswith("/assets/img/"):
            continue
        if s in seen:
            continue
        seen.add(s)
        paths.append(s)
    return paths


_TOKEN_RE = re.compile(r"[a-z0-9]+")


def _tokenize_for_assets(text: str) -> List[str]:
    return _TOKEN_RE.findall((text or "").lower())


def select_assets_image_pool(
    *,
    catalog_paths: List[str],
    keyword: str,
    lsi_keywords: List[str],
    pool_size: int = 18,
) -> List[str]:
    """
    Select a short list of relevant images from the assets catalog by lightweight filename matching.
    Returns paths like `/assets/img/...`.
    """
    pool_size = max(0, int(pool_size or 0))
    if pool_size == 0:
        return []

    keyword_tokens = _tokenize_for_assets(keyword)
    lsi_tokens: List[str] = []
    for s in (lsi_keywords or [])[:12]:
        lsi_tokens.extend(_tokenize_for_assets(s))
    # De-emphasize noise tokens.
    stop = {
        "and",
        "or",
        "the",
        "a",
        "an",
        "to",
        "of",
        "for",
        "with",
        "vs",
        "versus",
        "guide",
        "checklist",
        "tips",
        "best",
        "how",
        "what",
        "why",
        "when",
    }
    keyword_tokens = [t for t in keyword_tokens if t not in stop and len(t) >= 3]
    lsi_tokens = [t for t in lsi_tokens if t not in stop and len(t) >= 3]

    def score_path(p: str) -> float:
        tokens = set(_tokenize_for_assets(p))
        kw_hits = sum(1 for t in keyword_tokens if t in tokens)
        lsi_hits = sum(1 for t in lsi_tokens if t in tokens)
        score = kw_hits * 4.0 + lsi_hits * 1.5

        # Gentle boosts for generally useful images.
        if "/assets/img/blogs/" in p:
            score += 0.6
        if "/assets/img/pcb/" in p:
            score += 0.4
        if "hero" in tokens:
            score += 0.3
        if "pcb" in tokens:
            score += 0.2
        return score

    ranked = sorted(((score_path(p), p) for p in (catalog_paths or [])), key=lambda x: x[0], reverse=True)

    # Always keep a small set of generic fallbacks in case keyword matching is weak.
    fallbacks = [
        "/assets/img/home/pcb-manufacturing.webp",
        "/assets/img/home/production-floor-overview.webp",
        "/assets/img/home/smt-assembly-line.webp",
        "/assets/img/pcb/common/pcb-quality-inspection.webp",
        "/assets/img/pcb/common/pcb-design-review.webp",
        "/assets/img/pcb/common/pcb-validation-thermal.webp",
    ]
    existing = {p for _, p in ranked}
    for fb in fallbacks:
        if fb in existing:
            ranked.append((0.05, fb))
    # Re-rank after adding fallbacks (so they can beat zero-score matches).
    ranked = sorted(ranked, key=lambda x: x[0], reverse=True)

    selected: List[str] = []
    used_dirs: set = set()

    for score, p in ranked:
        if len(selected) >= pool_size:
            break
        if score <= 0 and selected:
            break
        parent_dir = "/".join(p.split("/")[:5])  # /assets/img/<group>/<subgroup?>
        if parent_dir in used_dirs and score < 3:
            continue
        used_dirs.add(parent_dir)
        selected.append(p)

    # Ensure pool is non-empty when possible.
    if not selected and ranked:
        selected.append(ranked[0][1])
    return selected[:pool_size]


_SOFTWARE_SERP_TOKENS = {
    "dashboard",
    "analytics",
    "report",
    "reporting",
    "bi",
    "kpi",
    "visualization",
    "workflow",
    "automation",
    "monitoring",
    "metrics",
    "tracker",
    "tracking",
    "quality",
    "insights",
    "data",
    "database",
    "etl",
}

_PCBA_CONTEXT_TOKENS = {
    "pcba",
    "assembly",
    "smt",
    "reflow",
    "stencil",
    "aoi",
    "spi",
    "ict",
    "fct",
    "xray",
    "x-ray",
    "bom",
    "pick",
    "place",
    "placement",
    "dfm",
    "dft",
    "turnkey",
    "conformal",
    "test",
    "fixture",
    "traceability",
    "mes",
    "fpy",
    "spc",
}

_PCB_CONTEXT_TOKENS = {
    "pcb",
    "stackup",
    "laminate",
    "impedance",
    "via",
    "microvia",
    "etch",
    "drill",
    "gerber",
    "hdi",
    "fr4",
    "enig",
    "osp",
    "hasl",
    "enepig",
    "warpage",
    "copper",
    "dk",
    "df",
}


def adapt_keyword_for_serp(keyword: str, lsi_keywords: List[str]) -> Tuple[str, str]:
    """
    Heuristically rewrite off-target keywords so they align with PCB/PCBA SERPs.
    Returns (adapted_keyword, reason). If unchanged, reason is "".
    """
    kw = (keyword or "").strip()
    if not kw:
        return kw, ""

    toks = set(_tokenize_for_assets(kw))
    lsi_text = " ".join(lsi_keywords or [])
    lsi_toks = set(_tokenize_for_assets(lsi_text))
    all_toks = toks | lsi_toks

    # Already PCB/PCBA explicit: keep.
    if {"pcb", "pcba", "fpc", "mcpcb"} & all_toks:
        return kw, ""

    # Determine context preference.
    ctx = "PCB"
    if _PCBA_CONTEXT_TOKENS & all_toks:
        ctx = "PCBA"
    elif _PCB_CONTEXT_TOKENS & all_toks:
        ctx = "PCB"

    # Off-target software SERP signals: dashboard/reporting/analytics without PCB tokens.
    if not (_SOFTWARE_SERP_TOKENS & all_toks):
        return kw, ""

    # Special handling: "quality dashboard design" and close variants.
    if "dashboard" in all_toks:
        base = "Quality Dashboard"
        if "traceability" in all_toks or "mes" in all_toks:
            base = "Traceability Dashboard"
        if "spc" in all_toks:
            base = "SPC Dashboard"
        if "design" in all_toks:
            base = base + " Design"
        adapted = f"{ctx} {base}".strip()
        return adapted, f"software-serp:dashboard -> {ctx}"

    if "report" in all_toks or "reporting" in all_toks:
        adapted = f"{ctx} Quality Reporting".strip()
        if "design" in all_toks:
            adapted += " Design"
        return adapted, f"software-serp:reporting -> {ctx}"

    if "analytics" in all_toks or "bi" in all_toks:
        adapted = f"{ctx} Manufacturing Analytics".strip()
        return adapted, f"software-serp:analytics -> {ctx}"

    return kw, ""


def format_assets_image_pool_text(paths: List[str]) -> str:
    """Format image paths as a bullet list for prompt injection."""
    cleaned = [p.strip() for p in (paths or []) if p and p.strip().startswith("/assets/img/")]
    return "\n".join(f"- `{p}`" for p in cleaned) + ("\n" if cleaned else "")


def _infer_modules(keyword: str, lsi_keywords: List[str]) -> List[str]:
    """
    Infer optional prompt modules from keyword text (and light LSI signals).
    Keep it conservative to avoid over-adding sections.
    """
    text = " ".join([keyword] + lsi_keywords).lower()
    mods: List[str] = []

    if re.search(r"\b(vs|versus)\b", text):
        mods.append("comparison")

    if re.search(r"\b(applications?|used in|industry|use case|use-case)\b", text):
        mods.append("application")

    if re.search(
        r"\b(manufacturer|manufacturing|factory|capability|service|quote|rfq|moq|lead time|turnaround|cost|price)\b",
        text,
    ):
        mods.append("capability")

    out: List[str] = []
    for m in mods:
        if m not in out:
            out.append(m)
    return out


def _load_modules_text(modules: List[str], *, keyword: str, lsi_keywords: List[str]) -> str:
    if not modules:
        return ""
    if not MODULES_DIR or not MODULES_DIR.exists():
        return ""
    chunks: List[str] = []
    for m in modules:
        mod_path = MODULES_DIR / f"{m}.md"
        if not mod_path.exists():
            continue
        raw = mod_path.read_text(encoding="utf-8")
        filled = fill_template_variables(raw, keyword, lsi_keywords)
        chunks.append(filled.strip())
    if not chunks:
        return ""
    return "\n\n".join(chunks) + "\n"


def _inject_modules(prompt: str, modules_text: str) -> str:
    if not modules_text.strip():
        return prompt
    if "{{modules}}" in prompt:
        return prompt.replace("{{modules}}", modules_text)
    m = re.search(r"^---\\s*$", prompt, flags=re.MULTILINE)
    if not m:
        return prompt + "\n\n" + modules_text
    insert_pos = m.start()
    return prompt[:insert_pos].rstrip() + "\n\n" + modules_text + "\n\n" + prompt[insert_pos:]


def generate_blog_with_gemini(prompt: str, max_retries: int = 3) -> Optional[str]:
    """使用Gemini生成博客内容"""
    base_prompt = prompt
    min_words = _infer_min_words_from_prompt(base_prompt)
    required_patterns = _required_section_patterns_from_prompt(base_prompt)
    kind = _detect_v3_template_kind(base_prompt)
    if kind == "unknown":
        kind = _detect_v2_template_kind(base_prompt)
    extracted_keyword = _extract_keyword_from_prompt(base_prompt) or "PCB"
    extracted_lsi = _extract_lsi_from_prompt(base_prompt)
    if kind == "story":
        system_msg = (
            "You are a meticulous technical writer. Follow the user's template strictly. "
            "Output ONLY the final Markdown blog. Start with YAML front matter ('---'). "
            "Include exactly one H1 and do not omit required sections. "
            "Near the top, include a '### Contents' TOC, then an opening paragraph and a '### Highlights' list. "
            "Do NOT output '## Key Takeaways' or '## Quick Answer'. "
            "Do not output template explanations or meta commentary."
        )
    else:
        system_msg = (
            "You are a meticulous technical writer. Follow the user's template strictly. "
            "Output ONLY the final Markdown blog. Start with YAML front matter ('---'). "
            "Include exactly one H1 and do not omit required sections. "
            "Start the body with a short opening paragraph and a 'Highlights' bullet list. "
            "Include '## Quick Answer' or '## Key Takeaways' before any tables. "
            "Do not output template explanations or meta commentary."
        )
    best: Optional[str] = None
    best_words = -1
    for attempt in range(max_retries):
        try:
            print(f"🤖 使用 {MODEL} 生成博客... (尝试 {attempt + 1}/{max_retries})")

            result = chat_completions_request(
                base_url=GEMINI_API_URL,
                api_key=API_KEY,
                model=MODEL,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.1,
                max_tokens=20000,
            )
            print(f"✅ Gemini 生成成功，字符数: {len(result)}")
            candidate = result.strip()
            candidate_for_checks = post_process_content(candidate)
            wc = _estimate_english_word_count(candidate)
            missing = _missing_required_sections(candidate_for_checks, required_patterns)

            # Minimal viability gate:
            # - Avoid wasting tokens on strict compliance retries; we can repair locally later.
            # - Only retry on clearly broken/truncated outputs.
            min_viable_words = 350
            if min_words is not None:
                min_viable_words = max(min_viable_words, int(min_words * 0.35))
            ok = True
            if _looks_like_prompt_echo_or_readme(candidate):
                ok = False
            if wc < min_viable_words:
                ok = False
            if not candidate_for_checks.lstrip().startswith("---"):
                ok = False

            if wc > best_words:
                best = result
                best_words = wc

            if ok:
                return result

            h2_count = len(re.findall(r"(?m)^##\s+\S", candidate))
            print(
                f"⚠️ 输出可能截断/异常，将重试：words={wc}, min_words={min_words}, "
                f"h1={_has_h1(candidate)}, h2={h2_count}, missing={missing}"
            )
            missing_note = ", ".join(missing) if missing else "structure/length"
            prefix = (
                "CRITICAL FIX:\n"
                f"- Your previous output missed required sections: {missing_note}.\n"
                "- Rewrite the FULL article from the beginning.\n"
                "- Use the exact section order shown in the template.\n"
                + (
                    "- Do not start with a table. Follow the Story template order; do NOT output 'Key Takeaways'.\n\n"
                    if kind == "story"
                    else "- Do not start with a table. The first H2 must be 'Quick Answer' or 'Key Takeaways' (as required by the template).\n\n"
                )
            )
            starter = _build_output_starter(kind, keyword=extracted_keyword, lsi_keywords=extracted_lsi)
            prompt = base_prompt + "\n\n" + prefix + starter
                
        except Exception as e:
            print(f"❌ Gemini API 调用失败 (尝试 {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 30
                print(f"⏳ 等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
            else:
                print("❌ Gemini: 所有重试都失败了")
                return best
    
    return best

def post_process_content(content: str) -> str:
    """后处理生成的内容"""
    # 移除可能的markdown代码块标记
    content = re.sub(r'^```[\w]*\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'\n```$', '', content, flags=re.MULTILINE)

    def looks_like_yaml_front_matter_start(lines: List[str], start_idx: int) -> bool:
        if start_idx < 0 or start_idx >= len(lines):
            return False
        if lines[start_idx].strip() != "---":
            return False
        # Front matter should have a closing '---' within a short window.
        end_idx = None
        for j in range(start_idx + 1, min(len(lines), start_idx + 80)):
            if lines[j].strip() == "---":
                end_idx = j
                break
        if end_idx is None:
            return False
        # And usually contains YAML-ish keys.
        block = "\n".join(lines[start_idx + 1 : end_idx])
        return bool(re.search(r"(?m)^\s*(title|description|date|category|tags)\s*:", block))

    def find_yaml_front_matter_end_pos(text: str) -> Optional[int]:
        stripped_local = text.lstrip()
        if not stripped_local.startswith("---"):
            return None
        # Work with keepends so we can compute char positions safely.
        lines_kept = text.splitlines(keepends=True)
        idx0 = None
        for i, line in enumerate(lines_kept[:200]):
            if line.strip() != "---":
                continue
            # Convert keepends to stripped list for the helper.
            stripped_lines = [l.rstrip("\n") for l in lines_kept]
            if looks_like_yaml_front_matter_start(stripped_lines, i):
                idx0 = i
                break
        if idx0 is None:
            return None
        # Find closing delimiter position.
        stripped_lines = [l.rstrip("\n") for l in lines_kept]
        end_idx = None
        for j in range(idx0 + 1, min(len(stripped_lines), idx0 + 120)):
            if stripped_lines[j].strip() == "---":
                end_idx = j
                break
        if end_idx is None:
            return None
        return sum(len(l) for l in lines_kept[: end_idx + 1])

    # 如果模型意外输出了前言/说明，裁剪到 front matter 起始处（仅在看起来确实是 YAML front matter 时）
    stripped = content.lstrip()
    if not stripped.startswith("---"):
        lines = content.splitlines()
        for i, line in enumerate(lines[:120]):
            if line.strip() != "---":
                continue
            if looks_like_yaml_front_matter_start(lines, i):
                content = "\n".join(lines[i:]).lstrip() + "\n"
                break

    # 标题规范化（避免出现 TL;DR / 括号说明等“旁白式”标题）
    replacements = [
        (r"^##\s*TL;DR.*$", "## Quick Answer (30 seconds)"),
        (r"^##\s*Key\s*takeaways.*$", "## Key Takeaways"),
        (r"^##\s*FAQ\s*\\(.*\\)\\s*$", "## FAQ"),
    ]
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content, flags=re.IGNORECASE | re.MULTILINE)

    # 去除常见“SEO 元话术/旁白”行（作为兜底；主控仍以提示词为准）
    banned_line_patterns = [
        r"\bSERP\b",
        r"People Also Ask",
        r"\byou might be searching\b",
        r"\bPAA\b",
        r"internal links required",
        r"Questions you might be searching for",
    ]
    if banned_line_patterns:
        banned_re = re.compile("|".join(f"(?:{p})" for p in banned_line_patterns), flags=re.IGNORECASE)
        kept: List[str] = []
        for line in content.splitlines():
            if banned_re.search(line):
                continue
            kept.append(line)
        content = "\n".join(kept) + "\n"

    # 确保 BlogQuickQuoteInline 组件“恰好一次”，且尽量放在 Quick Answer / Key Takeaways 后
    marker = "<!-- COMPONENT: BlogQuickQuoteInline -->"
    if content.count(marker) > 1:
        first = content.find(marker)
        before = content[: first + len(marker)]
        after = content[first + len(marker) :].replace(marker, "")
        content = before + after

    if marker not in content:
        def insert_marker_before_next_h2(section_re: str) -> Optional[str]:
            m = re.search(section_re, content, flags=re.IGNORECASE | re.MULTILINE)
            if not m:
                return None
            next_h2 = re.search(r"^##\s+", content[m.end() :], flags=re.MULTILINE)
            insert_pos = (m.end() + next_h2.start()) if next_h2 else len(content)
            insertion = "\n\n" + marker + "\n\n"
            return content[:insert_pos] + insertion + content[insert_pos:]

        updated = insert_marker_before_next_h2(r"^##\s*Quick Answer\b.*$") or insert_marker_before_next_h2(
            r"^##\s*Key Takeaways\b.*$"
        )
        if updated is not None:
            content = updated
        else:
            # 兜底：优先尝试插入到 “Request a quote ...” 章节；否则放在 front matter 之后；最后放到正文开头。
            m_quote = re.search(r"^##\s*Request a quote\b.*$", content, flags=re.IGNORECASE | re.MULTILINE)
            if m_quote:
                insert_pos = m_quote.end()
                content = content[:insert_pos] + "\n\n" + marker + "\n\n" + content[insert_pos:]
            else:
                fm_end = find_yaml_front_matter_end_pos(content)
                if fm_end is not None:
                    content = content[:fm_end] + "\n\n" + marker + "\n\n" + content[fm_end:]
                else:
                    content = marker + "\n\n" + content

    # 确保内容以换行符结尾
    if not content.endswith('\n'):
        content += '\n'
    
    return content


def is_valid_prompt_template_file(path: Path) -> bool:
    """Filter out non-prompt markdown files (e.g., README.md) from template candidates."""
    name = path.name.strip().lower()
    if name in {"readme.md", "readme.mdx"}:
        return False
    if name.startswith("_"):
        return False
    return True


def is_story_prompt_template_file(path: Path) -> bool:
    """Best-effort identify story templates by filename convention."""
    stem = (path.stem or "").strip().lower()
    return bool(re.search(r"(^|[-_])story($|[-_])", stem))

def detect_language(content: str) -> str:
    """检测内容语言"""
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', content))
    total_chars = len(content)
    
    if total_chars > 0 and chinese_chars / total_chars > 0.3:
        return "中文"
    return "英文"

def build_front_matter(
    content: str,
    keyword: str,
    template_name: str,
    lsi_keywords: List[str],
    slug: str,
    *,
    original_keyword: Optional[str] = None,
) -> str:
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

    # 构建tags：主关键词 + LSI关键词（保留原始关键词用于追溯/覆盖更多长尾）
    tags = [keyword] + lsi_keywords
    if original_keyword:
        ok = str(original_keyword).strip()
        if ok and ok.lower() != str(keyword).strip().lower() and ok not in tags:
            tags.append(ok)
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


def normalize_h1_to_front_matter_title(content: str, fallback_title: Optional[str] = None) -> str:
    """Ensure exactly one H1 exists and matches the YAML `title` when front matter is present."""
    text = (content or "").strip("\n")
    stripped = text.lstrip()
    if not stripped.startswith("---"):
        return text + "\n"

    lines = text.splitlines()
    # Find the first two '---' delimiters.
    fm_start = None
    fm_end = None
    for i, line in enumerate(lines[:200]):
        if line.strip() == "---":
            fm_start = i
            break
    if fm_start is None:
        return text + "\n"
    for j in range(fm_start + 1, min(len(lines), fm_start + 120)):
        if lines[j].strip() == "---":
            fm_end = j
            break
    if fm_end is None:
        return text + "\n"

    title_val: Optional[str] = None
    for k in range(fm_start + 1, fm_end):
        m = re.match(r'^\s*title:\s*(.+?)\s*$', lines[k])
        if m:
            title_val = m.group(1).strip()
            break
    if title_val:
        # Strip simple YAML quoting.
        if (title_val.startswith('"') and title_val.endswith('"')) or (title_val.startswith("'") and title_val.endswith("'")):
            title_val = title_val[1:-1].strip()
    title = title_val or (fallback_title or "").strip()
    if not title:
        return text + "\n"

    # Body starts after fm_end.
    body_start = fm_end + 1
    while body_start < len(lines) and not lines[body_start].strip():
        body_start += 1

    # Find first H1 after front matter, if any.
    h1_idx = None
    for idx in range(body_start, min(len(lines), body_start + 80)):
        if re.match(r"^\s*#\s+\S", lines[idx]):
            h1_idx = idx
            break
        if re.match(r"^\s*##\s+\S", lines[idx]):
            # If we already hit H2 before H1, we'll insert H1 at body_start.
            break

    if h1_idx is None:
        lines.insert(body_start, f"# {title}")
        lines.insert(body_start + 1, "")
    else:
        lines[h1_idx] = f"# {title}"

    out = "\n".join(lines).strip() + "\n"
    return out

def _strip_template_suffix_from_slug(slug: str) -> str:
    cleaned = slug.strip("-")
    for suffix in ("-aptpcb-query", "-aptpcb-pillar", "-aptpcb-playbook", "-aptpcb-story"):
        if cleaned.endswith(suffix):
            cleaned = cleaned[: -len(suffix)]
            break
    if cleaned.endswith("-aptpcb"):
        cleaned = cleaned[: -len("-aptpcb")]
    return cleaned.strip("-")


def _infer_intent_token(keyword: str, lsi_keywords: List[str]) -> Optional[str]:
    """Infer the strongest intent token to include in the slug."""
    haystack = " ".join([keyword] + list(lsi_keywords or []))
    if re.search(r"\bMCPCB\b", haystack, flags=re.IGNORECASE):
        return "mcpcb"
    if re.search(r"\bPCBA\b", haystack, flags=re.IGNORECASE):
        return "pcba"
    if re.search(r"\bFPC\b", haystack, flags=re.IGNORECASE):
        return "fpc"
    if re.search(r"\bPCB\b", haystack, flags=re.IGNORECASE):
        return "pcb"
    return None


def _slug_has_intent_token(slug: str) -> bool:
    return bool(re.search(r"\b(pcb|pcba|mcpcb|fpc)\b", slug, flags=re.IGNORECASE))


def _keyword_explicitly_has_intent(keyword: str) -> bool:
    return bool(re.search(r"\b(PCB|PCBA|MCPCB|FPC)\b", keyword, flags=re.IGNORECASE))


def generate_base_slug(main_keyword: Dict, template_name: str, lsi_keywords: List[str]) -> str:
    """根据关键词与模板生成基础 slug（未去重）。"""
    keyword_text = str(main_keyword.get("keyword") or "").strip()
    filename_hint = str(main_keyword.get("filename") or "").strip()

    template_clean = re.sub(r"-v\d+$", "", template_name)
    template_clean = re.sub(r"-pcb", "", template_clean, flags=re.IGNORECASE)
    template_slug = slugify(template_clean)

    keyword_slug = slugify(keyword_text) or slugify(template_name)

    if filename_hint:
        stem = Path(filename_hint).stem
        stem_slug = _strip_template_suffix_from_slug(slugify(stem))
        if stem_slug:
            keyword_slug = stem_slug

    # APTPCB v5 templates: don't leak template name into the slug (SEO/UX noise).
    # If a collision happens, ensure_unique_slug() will try meaningful suffixes before any numeric fallback.
    if template_slug in {"aptpcb-query", "aptpcb-pillar", "aptpcb-playbook", "aptpcb-story"}:
        base_slug = keyword_slug
    else:
        base_slug = f"{keyword_slug}-{template_slug}".strip("-")

    intent_token = _infer_intent_token(keyword_text, lsi_keywords)
    if intent_token and not _slug_has_intent_token(base_slug):
        # If the keyword explicitly includes PCB/PCBA/etc, always keep that signal in the slug.
        # If it's only implied by LSI, only force it for short/ambiguous slugs.
        parts = [p for p in base_slug.split("-") if p]
        if _keyword_explicitly_has_intent(keyword_text) or len(parts) <= 2:
            base_slug = f"{base_slug}-{intent_token}".strip("-")

    # 保底清理空 slug
    base_slug = base_slug.strip("-") or slugify(keyword_text) or slugify(template_name) or f"post-{int(time.time())}"
    return base_slug


def generate_filename_from_slug(slug: str) -> str:
    return f"{slug}.md"

def save_blog_to_file(content: str, filename: str, *, lang_dir: str = "cn") -> Path:
    """保存博客到文件"""
    # 创建日期目录
    today = datetime.now().strftime('%m%d')
    output_dir = OUTPUT_BASE_DIR / today / lang_dir
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

def update_keyword_usage(keywords_data: Dict, main_keyword: str, template_name: str) -> bool:
    """更新关键词使用状态（仅标记主关键词，LSI 不标记 used）。"""
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
        return "failed"
    
    keywords_data = load_keywords(keywords_file)
    if not keywords_data:
        return "failed"
    
    # 选择关键词
    main_keyword, lsi_keywords = select_keywords(keywords_data)
    if not main_keyword:
        if KEYWORD_SEARCH_FILTER:
            return "skipped"
        print(f"❌ 无法选择关键词")
        return "failed"
        print(f"❌ 无法选择关键词")
        return False
    
    original_keyword = main_keyword["keyword"]
    generation_keyword = original_keyword
    if KEYWORD_SERP_ADAPT != "off":
        adapted, reason = adapt_keyword_for_serp(original_keyword, lsi_keywords)
        if adapted and adapted.strip() and adapted.strip() != original_keyword.strip():
            if KEYWORD_SERP_ADAPT == "skip":
                print(f"⚠️ 关键词疑似偏离 SERP（{reason}），将跳过并尝试下一个关键词：{original_keyword} -> {adapted}")
                # Mark this keyword as used to avoid getting stuck on it repeatedly.
                try:
                    update_keyword_usage(keywords_data, original_keyword, "skipped-serp")
                    save_keywords(keywords_file, keywords_data)
                except Exception:
                    pass
                return process_category(category_dir)
            generation_keyword = adapted
            print(f"🔁 SERP 关键词重写: {original_keyword} -> {generation_keyword} ({reason})")

    print(f"🔑 主关键词: {generation_keyword}")
    print(f"🔗 LSI关键词: {', '.join(lsi_keywords)}")
    
    # 选择模板（使用最少使用的模板）
    templates_dir = category_dir / "templates"
    template_files = list(templates_dir.glob("*.md")) if templates_dir.exists() else []
    template_files = [p for p in template_files if is_valid_prompt_template_file(p)]
    if not template_files and BASE_TEMPLATES_DIR and BASE_TEMPLATES_DIR.exists():
        template_files = [p for p in BASE_TEMPLATES_DIR.glob("*.md") if is_valid_prompt_template_file(p)]
        if template_files:
            print(f"🧱 使用共享模板基座目录: {BASE_TEMPLATES_DIR}")

    if TEMPLATE_KIND != "auto":
        filtered = [p for p in template_files if TEMPLATE_KIND in p.stem.lower() or TEMPLATE_KIND in p.name.lower()]
        if filtered:
            template_files = filtered
        else:
            print(f"⚠️ 未找到匹配 template-kind={TEMPLATE_KIND} 的模板，回退为全部模板")

    # 优先匹配逻辑：Template > Intent > Load Balancing
    preferred_template = None
    
    # 1. Check explicit "template" field in keyword data
    explicit_template_name = main_keyword.get("template")
    if explicit_template_name:
        for p in template_files:
            if p.name == explicit_template_name:
                preferred_template = p
                print(f"🎯 精确匹配模板: {preferred_template.name}")
                break
        if not preferred_template:
            print(f"⚠️ 指定的模板 {explicit_template_name} 未在目录中找到，尝试 Intent 匹配...")

    # 2. Check "intent" field (fuzzy match)
    if not preferred_template:
        intent = main_keyword.get("intent")
        if intent:
            # map intent to filename keywords
            # e.g. intent="query" -> look for "*query*" in filename
            candidates = [p for p in template_files if intent.lower() in p.name.lower()]
            if candidates:
                # If multiple candidates (e.g. query-v6, query-v5), pick one (could use load balancing here too, but keep simple for now)
                # Ideally prefer v6 if available
                v6_candidates = [p for p in candidates if "-v6" in p.name]
                preferred_template = v6_candidates[0] if v6_candidates else candidates[0]
                print(f"🎯 Intent ('{intent}') 匹配模板: {preferred_template.name}")
            else:
                print(f"⚠️ 指定的 Intent ('{intent}') 无对应模板，回退为自动选择")

    if preferred_template:
        template_file = preferred_template
    else:
        template_file = get_least_used_template(templates_dir, keywords_data, template_files=template_files)
    if not template_file:
        print(f"❌ 没有找到模板文件")
        return "failed"

    print(f"📝 使用模板: {template_file.name}")
    is_v6_template = "-v6" in template_file.name
    if is_v6_template:
        print("🚀 检测到 v6 模板: 将禁用强制脚本注入 (Opening/Links)，完全依赖 Prompt。")
    
    # 加载并填充模板
    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except Exception as e:
        print(f"❌ 读取模板失败: {e}")
        return "failed"

    # ...


    
    internal_pool_text = ""
    if INTERNAL_LINK_POOL_FILE and INTERNAL_LINK_POOL_FILE.exists():
        internal_pool_text = _load_internal_link_pool_text(INTERNAL_LINK_POOL_FILE)

    assets_pool_text = ""
    assets_pool_paths: List[str] = []
    try:
        if ASSETS_IMAGE_CATALOG_FILE and ASSETS_IMAGE_CATALOG_FILE.exists():
            catalog_paths = load_assets_image_catalog_paths(ASSETS_IMAGE_CATALOG_FILE)
            pool = select_assets_image_pool(
                catalog_paths=catalog_paths,
                keyword=generation_keyword,
                lsi_keywords=lsi_keywords,
                pool_size=ASSETS_IMAGE_POOL_SIZE,
            )
            assets_pool_paths = list(pool or [])
            assets_pool_text = format_assets_image_pool_text(pool)
    except Exception as e:
        print(f"⚠️ 生成 assets image pool 失败（忽略并继续）：{e}")
        assets_pool_text = ""
        assets_pool_paths = []

    filled_prompt = fill_template_variables(template_content, generation_keyword, lsi_keywords)

    # Detect template kind early so we can avoid injecting extra modules into story templates.
    template_kind = _detect_v3_template_kind(filled_prompt)
    if template_kind == "unknown":
        template_kind = _detect_v2_template_kind(filled_prompt)

    # Inject optional modules (forced or inferred). Skip for story (pure narrative template).
    modules_text = ""
    if template_kind != "story":
        forced = [m.strip() for m in (FORCE_MODULES or "").split(",") if m.strip()]
        modules = forced if forced else _infer_modules(generation_keyword, lsi_keywords)
        modules_text = _load_modules_text(modules, keyword=generation_keyword, lsi_keywords=lsi_keywords)
        if modules_text:
            print(f"🧩 启用模块: {', '.join(modules)}")
    else:
        modules = []

    # Use a compact prompt to reduce "starts in the middle" failures on some endpoints.
    # NOTE: Story templates are already concise + order-sensitive; keep the raw template
    # so v3/v2 kind markers remain visible to downstream detectors and system prompts.
    v3_kind = _detect_v3_template_kind(filled_prompt)
    v2_kind = _detect_v2_template_kind(filled_prompt) if v3_kind == "unknown" else "unknown"
    if v3_kind != "unknown" and v3_kind != "story":
        filled_prompt = _compact_v3_prompt(
            kind=v3_kind,
            keyword=generation_keyword,
            lsi_keywords=lsi_keywords,
            internal_link_pool=internal_pool_text,
            assets_image_pool=assets_pool_text,
            modules_text=modules_text,
        )
    elif v2_kind != "unknown" and v2_kind != "story":
        filled_prompt = _compact_v2_prompt(
            kind=v2_kind,
            keyword=generation_keyword,
            lsi_keywords=lsi_keywords,
            internal_link_pool=internal_pool_text,
            assets_image_pool=assets_pool_text,
            modules_text=modules_text,
        )
    else:
        # Legacy placeholder injection path (also used for story templates).
        if "{{internal_link_pool}}" in filled_prompt:
            if internal_pool_text:
                pool_text = internal_pool_text
            else:
                print("⚠️ 模板包含 {{internal_link_pool}} 但未提供可用的 --internal-link-pool；将注入为空列表")
                pool_text = ""
            filled_prompt = filled_prompt.replace("{{internal_link_pool}}", pool_text)

        if "{{assets_image_pool}}" in filled_prompt:
            filled_prompt = filled_prompt.replace("{{assets_image_pool}}", assets_pool_text or "")

        if modules_text:
            filled_prompt = _inject_modules(filled_prompt, modules_text)

    # 如模板未声明字数要求，则追加统一字数要求
    if (
        "### 字数要求" not in filled_prompt
        and "总字数" not in filled_prompt
        and "Word count target" not in filled_prompt
    ):
        filled_prompt += "\n\n### 字数要求\n- 总字数：2800-3500词（依主题复杂度调整）\n"

    if DRY_RUN:
        main_keyword_for_slug = dict(main_keyword)
        main_keyword_for_slug["keyword"] = generation_keyword
        base_slug = generate_base_slug(main_keyword_for_slug, template_file.stem, lsi_keywords)
        kind_guess = _detect_v3_template_kind(filled_prompt)
        if kind_guess == "unknown":
            kind_guess = _detect_v2_template_kind(filled_prompt)
        unique_slug_preview = preview_unique_slug(
            base_slug,
            keyword=generation_keyword,
            lsi_keywords=lsi_keywords,
            kind=kind_guess,
        )
        print("🧪 DRY RUN: 不调用模型、不写文件")
        print(f"🧩 Template: {template_file}")
        print(f"🔑 Keyword: {main_keyword['keyword']}")
        print(f"🔗 LSI: {', '.join(lsi_keywords)}")
        print(f"🧷 Slug: {unique_slug_preview}")
        print(f"📏 Prompt chars: {len(filled_prompt)}")
        return True
    
    # 生成博客
    print(f"🤖 使用 {MODEL} 生成博客...")
    blog_content = generate_blog_with_gemini(filled_prompt, max_retries=int(MAX_GENERATION_ATTEMPTS or 3))
    
    if not blog_content:
        print(f"❌ 博客生成失败")
        return False
    
    print(f"✅ 博客生成成功，字符数: {len(blog_content)}")
    
    # 后处理内容
    blog_content = post_process_content(blog_content)
    language = detect_language(blog_content)

    # 先生成唯一 slug，再写入 front-matter，最后保存
    main_keyword_for_slug = dict(main_keyword)
    main_keyword_for_slug["keyword"] = generation_keyword
    base_slug = generate_base_slug(main_keyword_for_slug, template_file.stem, lsi_keywords)
    kind_hint = v3_kind if v3_kind != "unknown" else v2_kind
    kind_for_slug = kind_hint if kind_hint != "unknown" else _infer_article_kind_from_content(blog_content)
    unique_slug = ensure_unique_slug(
        base_slug,
        keyword=generation_keyword,
        lsi_keywords=lsi_keywords,
        kind=kind_for_slug,
    )

    blog_content = build_front_matter(
        blog_content,
        generation_keyword,
        template_file.stem,
        lsi_keywords,
        unique_slug,
        original_keyword=original_keyword,
    )
    blog_content = normalize_h1_to_front_matter_title(blog_content, fallback_title=generation_keyword)
    # Image policy:
    # - auto: deterministic hero injection (and respects manual front matter override)
    # - llm: rely on model (0–3 images); still sync/replace body hero if front matter is set
    # - none: no injection
    if IMAGE_POLICY == "auto":
        hero_path = assets_pool_paths[0] if assets_pool_paths else ""
        blog_content = ensure_hero_image(blog_content, hero_path)
    elif IMAGE_POLICY == "llm":
        blog_content = ensure_hero_image(blog_content, "")

    # Normalize opening + highlights + description for more consistent one-shot quality.
    kind = kind_hint if kind_hint != "unknown" else _infer_article_kind_from_content(blog_content)
    if kind != "story" and not is_v6_template:
        blog_content = ensure_opening_paragraph(blog_content, keyword=generation_keyword, kind=kind)
    blog_content = ensure_highlights(blog_content, keyword=generation_keyword, kind=kind)
    blog_content = ensure_front_matter_description(blog_content, keyword=generation_keyword)
    blog_content = ensure_title_case_and_headings(blog_content, language=language)
    blog_content = ensure_playbook_section_tables(blog_content, keyword=generation_keyword)
    blog_content = normalize_h1_to_front_matter_title(blog_content, fallback_title=generation_keyword)
    blog_content = fix_malformed_conclusion_heading(blog_content)
    blog_content = repair_truncated_key_takeaways(blog_content)
    blog_content = ensure_blog_quick_quote_marker(blog_content, kind_hint=kind)
    blog_content = repair_truncated_conclusion(blog_content)
    blog_content = fix_toc_leaked_into_key_takeaways(blog_content)
    if kind == "story":
        blog_content = strip_story_key_takeaways(blog_content, kind_hint=kind)
        blog_content = fix_story_context_heading(blog_content, kind_hint=kind)
        blog_content = rebuild_contents_toc(blog_content, kind_hint=kind)
    else:
        blog_content = ensure_contents_toc(blog_content, kind_hint=kind)

    # Pre-compute output location (used for both normal save and strict-mode debug dumps).
    filename = generate_filename_from_slug(unique_slug)
    if OUTPUT_LANG_MODE == "auto":
        lang_dir = "cn" if language == "中文" else "en"
    else:
        lang_dir = OUTPUT_LANG_MODE

    # Final quality check (optional strict mode).
    required_patterns = _required_section_patterns_from_prompt(filled_prompt)
    missing_sections = _missing_required_sections(blog_content, required_patterns)
    min_words = _infer_min_words_from_prompt(filled_prompt)
    wc = _estimate_english_word_count(blog_content)
    h2_count = len(re.findall(r"(?m)^\s*##\s+\S", blog_content))
    invalid_reasons: List[str] = []
    if _looks_like_prompt_echo_or_readme(blog_content):
        invalid_reasons.append("prompt-echo/readme")
    if min_words is not None and wc < min_words:
        invalid_reasons.append(f"word-count<{min_words} (got {wc})")
    if h2_count < 4:
        invalid_reasons.append(f"too-few-h2 (got {h2_count})")
    if missing_sections:
        invalid_reasons.append("missing-sections=" + ",".join(missing_sections))

    # Local repair (no extra API calls): synthesize missing required sections from existing content.
    if STRICT_TEMPLATE and missing_sections:
        if "Quick Answer" in missing_sections and "## Quick Answer" in filled_prompt:
            quick_answer = _build_quick_answer_section_from_existing(blog_content, keyword=main_keyword["keyword"])
            blog_content = _insert_block_after_h1_before_table_or_h2(blog_content, quick_answer)
            blog_content = normalize_h1_to_front_matter_title(blog_content, fallback_title=main_keyword["keyword"])

        blog_content = repair_missing_required_sections_locally(
            blog_content,
            keyword=main_keyword["keyword"],
            lsi_keywords=lsi_keywords,
            missing_sections=missing_sections,
        )
        blog_content = normalize_h1_to_front_matter_title(blog_content, fallback_title=main_keyword["keyword"])

        # Re-check after repair.
        missing_sections = _missing_required_sections(blog_content, required_patterns)
        wc = _estimate_english_word_count(blog_content)
        h2_count = len(re.findall(r"(?m)^\s*##\s+\S", blog_content))
        invalid_reasons = []
        if _looks_like_prompt_echo_or_readme(blog_content):
            invalid_reasons.append("prompt-echo/readme")
        if min_words is not None and wc < min_words:
            invalid_reasons.append(f"word-count<{min_words} (got {wc})")
        if h2_count < 4:
            invalid_reasons.append(f"too-few-h2 (got {h2_count})")
        if missing_sections:
            invalid_reasons.append("missing-sections=" + ",".join(missing_sections))

    # Local expansion (no extra API calls): ensure minimum word count for publishing.
    if STRICT_TEMPLATE and min_words is not None:
        wc = _estimate_english_word_count(blog_content)
        if wc < min_words:
            blog_content = expand_to_min_words_locally(
                blog_content,
                keyword=main_keyword["keyword"],
                lsi_keywords=lsi_keywords,
                min_words=min_words,
            )
            blog_content = normalize_h1_to_front_matter_title(blog_content, fallback_title=main_keyword["keyword"])
            # Re-check after expansion.
            wc = _estimate_english_word_count(blog_content)
            missing_sections = _missing_required_sections(blog_content, required_patterns)
            h2_count = len(re.findall(r"(?m)^\s*##\s+\S", blog_content))
            invalid_reasons = []
            if _looks_like_prompt_echo_or_readme(blog_content):
                invalid_reasons.append("prompt-echo/readme")
            if wc < min_words:
                invalid_reasons.append(f"word-count<{min_words} (got {wc})")
            if h2_count < 4:
                invalid_reasons.append(f"too-few-h2 (got {h2_count})")
            if missing_sections:
                invalid_reasons.append("missing-sections=" + ",".join(missing_sections))

    # Deterministic enforcement (no extra API calls):
    # - playbook/pillar: 6–10 internal links + at least 2 local images (hero + 1 in-body)
    kind = _infer_article_kind_from_content(blog_content)
    if kind in {"playbook", "pillar"} and not is_v6_template:
        try:
            internal_urls = extract_internal_link_pool_urls(internal_pool_text or "")
            if internal_urls:
                blog_content = prune_generic_related_resources_blocks(blog_content)
                blog_content = ensure_internal_links(
                    blog_content,
                    internal_urls=internal_urls,
                    min_links=6,
                    max_links=10,
                    keyword=generation_keyword,
                    lsi_keywords=lsi_keywords,
                )
        except Exception as e:
            print(f"⚠️ 内链自动插入失败（忽略并继续）：{e}")

        try:
            if IMAGE_POLICY != "none" and assets_pool_paths:
                hero_path = assets_pool_paths[0] if assets_pool_paths else ""
                blog_content = ensure_min_images(
                    blog_content,
                    hero_path=hero_path,
                    candidate_paths=assets_pool_paths,
                    min_images=2,
                )
        except Exception as e:
            print(f"⚠️ 图片自动插入失败（忽略并继续）：{e}")

        blog_content = fix_malformed_conclusion_heading(blog_content)
        blog_content = repair_truncated_key_takeaways(blog_content)
        blog_content = ensure_blog_quick_quote_marker(blog_content)
        blog_content = fix_toc_leaked_into_key_takeaways(blog_content)
        blog_content = ensure_contents_toc(blog_content)

        # Re-check strict criteria after deterministic inserts (they can affect word count).
        if STRICT_TEMPLATE:
            missing_sections = _missing_required_sections(blog_content, required_patterns)
            wc = _estimate_english_word_count(blog_content)
            h2_count = len(re.findall(r"(?m)^\s*##\s+\S", blog_content))
            invalid_reasons = []
            if _looks_like_prompt_echo_or_readme(blog_content):
                invalid_reasons.append("prompt-echo/readme")
            if min_words is not None and wc < min_words:
                invalid_reasons.append(f"word-count<{min_words} (got {wc})")
            if h2_count < 4:
                invalid_reasons.append(f"too-few-h2 (got {h2_count})")
            if missing_sections:
                invalid_reasons.append("missing-sections=" + ",".join(missing_sections))

    if invalid_reasons:
        msg = "；".join(invalid_reasons)
        if STRICT_TEMPLATE:
            print(f"❌ 输出未通过严格模板校验：{msg}")
            try:
                failed_name = filename.replace(".md", "-failed.md")
                failed_path = save_blog_to_file(blog_content, failed_name, lang_dir=lang_dir)
                print(f"🧾 已保存失败样例用于排查: {failed_path}")
            except Exception as e:
                print(f"⚠️ 保存失败样例时出错（忽略并继续）：{e}")
            return False
        print(f"⚠️ 输出未完全满足模板要求（仍会保存）：{msg}")

    # 生成文件名并保存（确保与 sitemap 不冲突的 slug）
    file_path = save_blog_to_file(blog_content, filename, lang_dir=lang_dir)
    
    print(f"✅ 博客已保存到: {file_path}")
    
    # 更新模板使用统计
    update_template_usage(keywords_data, template_file.name, filename)
    
    # 更新关键词状态
    if update_keyword_usage(keywords_data, main_keyword["keyword"], template_file.name):
        save_keywords(keywords_file, keywords_data)
        print("✅ 关键词状态已更新（仅主关键词；LSI 不标记 used）")
        print(f"✅ 模板使用统计已更新: {template_file.name}")
    
    return "generated"

def main():
    """主函数"""
    args = parse_args()
    global PROMPTS_DIR, OUTPUT_BASE_DIR, SITEMAP_FILE, OUTPUT_LANG_MODE, TEMPLATE_KIND, DELAY_BETWEEN_REQUESTS
    global DRY_RUN, LIMIT_CATEGORIES, BASE_TEMPLATES_DIR, KEYWORD_INTENT, INTERNAL_LINK_POOL_FILE
    global MODULES_DIR, FORCE_MODULES, ASSETS_IMAGE_CATALOG_FILE, ASSETS_IMAGE_POOL_SIZE, STRICT_TEMPLATE, IMAGE_POLICY
    global MIN_WORDS_RATIO, MIN_WORDS_FLOOR, MAX_GENERATION_ATTEMPTS
    PROMPTS_DIR = Path(args.prompts_dir)
    OUTPUT_BASE_DIR = Path(args.output_base_dir)
    SITEMAP_FILE = Path(args.sitemap_file)
    OUTPUT_LANG_MODE = args.output_lang
    TEMPLATE_KIND = args.template_kind
    KEYWORD_INTENT = args.keyword_intent
    DRY_RUN = bool(args.dry_run)
    DELAY_BETWEEN_REQUESTS = float(args.delay_between_blogs or 0)
    LIMIT_CATEGORIES = args.limit
    STRICT_TEMPLATE = bool(args.strict_template)
    BASE_TEMPLATES_DIR = Path(args.base_templates_dir) if args.base_templates_dir else None
    INTERNAL_LINK_POOL_FILE = Path(args.internal_link_pool) if args.internal_link_pool else _default_internal_link_pool_file(PROMPTS_DIR)
    FORCE_MODULES = args.modules
    MODULES_DIR = Path(args.modules_dir) if args.modules_dir else _default_modules_dir(PROMPTS_DIR)
    ASSETS_IMAGE_CATALOG_FILE = Path(args.assets_image_catalog) if args.assets_image_catalog else _default_assets_image_catalog_file(PROMPTS_DIR)
    ASSETS_IMAGE_POOL_SIZE = int(args.assets_image_pool_size or ASSETS_IMAGE_POOL_SIZE)
    IMAGE_POLICY = str(args.image_policy or IMAGE_POLICY)
    MIN_WORDS_RATIO = float(args.min_words_ratio or MIN_WORDS_RATIO)
    MIN_WORDS_FLOOR = int(args.min_words_floor or MIN_WORDS_FLOOR)
    MIN_WORDS_FLOOR = int(args.min_words_floor or MIN_WORDS_FLOOR)
    MAX_GENERATION_ATTEMPTS = int(args.max_generation_attempts or MAX_GENERATION_ATTEMPTS)
    
    global KEYWORD_SEARCH_FILTER
    KEYWORD_SEARCH_FILTER = args.keyword_search


    print("=" * 80)
    print("批量PCB博客生成脚本")
    print("=" * 80)
    print(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"输出目录: {OUTPUT_BASE_DIR}")
    print(f"提示词目录: {PROMPTS_DIR}")
    print(f"Sitemap: {SITEMAP_FILE}")
    print(f"输出语言目录: {OUTPUT_LANG_MODE}")
    print(f"模板筛选: {TEMPLATE_KIND}")
    if BASE_TEMPLATES_DIR:
        print(f"共享模板基座: {BASE_TEMPLATES_DIR}")
    if INTERNAL_LINK_POOL_FILE:
        print(f"内链池文件: {INTERNAL_LINK_POOL_FILE}")
    if MODULES_DIR:
        print(f"模块目录: {MODULES_DIR}")
    if FORCE_MODULES:
        print(f"强制模块: {FORCE_MODULES}")
    if ASSETS_IMAGE_CATALOG_FILE:
        print(f"图片资产目录: {ASSETS_IMAGE_CATALOG_FILE}")
        print(f"图片候选数量: {ASSETS_IMAGE_POOL_SIZE}")
        print(f"图片策略: {IMAGE_POLICY}")
    print(f"最少词数阈值: ratio={MIN_WORDS_RATIO:g}, floor={MIN_WORDS_FLOOR}")
    print(f"生成最大尝试次数: {MAX_GENERATION_ATTEMPTS}")
    print(f"严格模板校验: {STRICT_TEMPLATE}")
    if not DRY_RUN and DELAY_BETWEEN_REQUESTS > 0:
        print(f"生成间隔: {DELAY_BETWEEN_REQUESTS:g} 秒/篇")
    print(f"关键词意图偏好: {KEYWORD_INTENT}")
    print("=" * 80)
    
    # Load used slugs to prevent collisions
    global USED_SLUGS
    sitemap_slugs = load_sitemap_slugs(SITEMAP_FILE) if SITEMAP_FILE.exists() else set()
    local_slugs = load_local_blog_slugs(OUTPUT_BASE_DIR)
    
    if args.ignore_sitemap:
        print("⚠️ Ignoring sitemap/existing slugs (--ignore-sitemap). Collisions will be allowed (overwrite mode).")
        USED_SLUGS = set()
    else:
        USED_SLUGS = set(sitemap_slugs) | set(local_slugs)
    
    print(f"🔎 已有 /blog/slug 数量（sitemap+本地）：{len(USED_SLUGS)}")

    # 获取所有类别
    categories = get_all_categories()
    print(f"📁 找到 {len(categories)} 个类别")
    
    success_count = 0
    failed_categories = []
    
    for i, category_dir in enumerate(categories, 1):
        if LIMIT_CATEGORIES is not None and i > max(0, LIMIT_CATEGORIES):
            break
        print(f"\n[{i}/{len(categories)}] 处理类别: {category_dir.name}")
        
        status = "failed"
        try:
            status = process_category(category_dir)
            if status == "generated":
                success_count += 1
                print(f"✅ 类别 {category_dir.name} 处理成功")
                
                # OPTIMIZATION: If searching for a specific keyword, and we just generated it, 
                # we can stop checking other categories (assuming 1 keyword = 1 blog).
                if KEYWORD_SEARCH_FILTER:
                    print("⚡ 目标关键词已生成，停止遍历其他类别。")
                    break
                    
            elif status == "skipped":
                # Silently skip
                pass
            else:
                failed_categories.append(category_dir.name)
                print(f"❌ 类别 {category_dir.name} 处理失败")
        except Exception as e:
            failed_categories.append(category_dir.name)
            print(f"❌ 类别 {category_dir.name} 处理异常: {e}")
        
        # Delay logic: Only delay if we actually generated something OR failed (attempted).
        # Skip delay if we just skipped the category (status == "skipped").
        if not DRY_RUN and i < len(categories) and DELAY_BETWEEN_REQUESTS > 0:
            if status == "skipped":
                 pass
            else:
                print(f"⏳ 等待 {DELAY_BETWEEN_REQUESTS:g} 秒...")
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
