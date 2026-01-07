#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sync APTPCB URL lists from `aptpcb_sitemap.xml`.

Outputs:
- `aptpcb_urls.md` (root)
- `prompts_aptpcb/internal_link_pool.md`

Rationale:
Use the sitemap as the single source of truth for currently indexable pages,
so blog generation prompts won't link to non-existing routes.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List
from urllib.parse import urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
SITEMAP_PATH = REPO_ROOT / "aptpcb_sitemap.xml"
APTPCB_URLS_MD = REPO_ROOT / "aptpcb_urls.md"
INTERNAL_LINK_POOL_MD = REPO_ROOT / "prompts_aptpcb" / "internal_link_pool.md"


@dataclass(frozen=True)
class UrlItem:
    url: str
    path: str


def _extract_loc_urls(xml_text: str) -> List[str]:
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml_text)


def _normalize_urls(urls: Iterable[str]) -> List[UrlItem]:
    items: List[UrlItem] = []
    seen = set()
    for raw in urls:
        try:
            parsed = urlparse(raw.strip())
        except Exception:
            continue
        if parsed.scheme not in {"http", "https"}:
            continue
        if not parsed.netloc.endswith("aptpcb.com"):
            continue
        path = parsed.path.rstrip("/") or "/"
        url = f"{parsed.scheme}://{parsed.netloc}{path}"
        if url in seen:
            continue
        seen.add(url)
        items.append(UrlItem(url=url, path=path))
    return items


def _is_policy_page(path: str) -> bool:
    return path in {
        "/en/privacy-policy",
        "/en/terms-of-service",
        "/en/environmental-policy",
        "/en/quality-policy",
    }


def _is_blog_post(path: str) -> bool:
    return path.startswith("/en/blog/") and path != "/en/blog"


def _group_key(path: str) -> str:
    if path in {"/", "/en"}:
        return "Core"
    if path in {"/en/about", "/en/contact", "/en/quote"}:
        return "Core"
    if path.startswith("/en/products") or path == "/en/pcb-manufacturing":
        return "Products & Manufacturing"
    if path.startswith("/en/materials"):
        return "Materials"
    if path.startswith("/en/tools"):
        return "Tools"
    if path.startswith("/en/resources"):
        return "Resources"
    if path.startswith("/en/blog"):
        return "Blog"
    return "Other"


def _md_list(urls: List[str]) -> str:
    return "\n".join(f"- {url}" for url in urls)


def build_aptpcb_urls_md(items: List[UrlItem]) -> str:
    grouped = {}
    for item in items:
        if _is_policy_page(item.path):
            continue
        grouped.setdefault(_group_key(item.path), []).append(item.url)

    order = [
        "Core",
        "Products & Manufacturing",
        "Materials",
        "Tools",
        "Resources",
        "Blog",
        "Other",
    ]

    lines: List[str] = []
    lines.append("# aptpcb.com URL Inventory (from aptpcb_sitemap.xml)")
    lines.append("")
    lines.append("This file is auto-synced from `aptpcb_sitemap.xml`.")
    lines.append("")
    for key in order:
        urls = sorted(grouped.get(key, []))
        if not urls:
            continue
        lines.append(f"## {key}")
        lines.append(_md_list(urls))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_internal_link_pool_md(items: List[UrlItem]) -> str:
    allowed = []
    for item in items:
        if _is_policy_page(item.path):
            continue
        if item.path == "/":
            # Prefer language-specific home for internal linking consistency.
            allowed.append("https://aptpcb.com/en")
            continue
        if _is_blog_post(item.path):
            # Skip blog posts in the default internal link pool to avoid cannibalization loops.
            continue
        allowed.append(item.url)

    def pick(prefix: str) -> List[str]:
        return sorted([u for u in allowed if urlparse(u).path.startswith(prefix)])

    core = sorted(
        {
            "https://aptpcb.com/en",
            "https://aptpcb.com/en/about",
            "https://aptpcb.com/en/contact",
            "https://aptpcb.com/en/quote",
            "https://aptpcb.com/en/products",
            "https://aptpcb.com/en/pcb-manufacturing",
            "https://aptpcb.com/en/blog",
        }
        & set(allowed)
        | {"https://aptpcb.com/en"}  # keep even if not in sitemap loc
    )

    materials = pick("/en/materials")
    tools = pick("/en/tools")
    resources = pick("/en/resources")

    lines: List[str] = []
    lines.append("## Internal Link Pool (3–6 per post)")
    lines.append("")
    lines.append("### Core & Conversion")
    lines.append(_md_list(core))
    lines.append("")
    if materials:
        lines.append("### Materials")
        lines.append(_md_list(materials))
        lines.append("")
    if tools:
        lines.append("### Tools")
        lines.append(_md_list(tools))
        lines.append("")
    if resources:
        lines.append("### Resources")
        lines.append(_md_list(resources))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    if not SITEMAP_PATH.exists():
        raise SystemExit(f"Missing sitemap: {SITEMAP_PATH}")

    xml_text = SITEMAP_PATH.read_text(encoding="utf-8")
    loc_urls = _extract_loc_urls(xml_text)
    items = _normalize_urls(loc_urls)

    APTPCB_URLS_MD.write_text(build_aptpcb_urls_md(items), encoding="utf-8")
    INTERNAL_LINK_POOL_MD.write_text(build_internal_link_pool_md(items), encoding="utf-8")

    print(f"✅ Wrote {APTPCB_URLS_MD}")
    print(f"✅ Wrote {INTERNAL_LINK_POOL_MD}")


if __name__ == "__main__":
    main()

