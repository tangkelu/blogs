#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import batch_blog_generation_openai as gen  # noqa: E402


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Normalize generated APTPCB markdown posts for structure and metadata.")
    p.add_argument("--dir", required=True, help="Directory containing generated .md files (recursive).")
    p.add_argument(
        "--internal-link-pool",
        default=str(REPO_ROOT / "prompts_aptpcb" / "internal_link_pool.md"),
        help="Markdown file containing aptpcb.com internal link pool (default: prompts_aptpcb/internal_link_pool.md).",
    )
    p.add_argument(
        "--assets-image-catalog",
        default="/code/hileap/frontendAPT/docs/assets-img-filenames.md",
        help="Markdown file listing /assets/img paths (default: /code/hileap/frontendAPT/docs/assets-img-filenames.md).",
    )
    p.add_argument("--dry-run", action="store_true", help="Print actions but do not write files.")
    return p.parse_args()


def _parse_keyword_from_front_matter(text: str, fallback: str) -> str:
    split = gen._split_yaml_front_matter_lines(text)
    if not split:
        return fallback
    fm_lines, _ = split
    tags = gen._front_matter_get_value(fm_lines, "tags") or ""
    # Prefer the first tag if present.
    import re

    q = re.findall(r"""['"]([^'"]+)['"]""", tags)
    if q and q[0].strip():
        return q[0].strip()
    title = gen._front_matter_get_value(fm_lines, "title") or ""
    title = title.strip().strip('"').strip("'")
    return title or fallback


def main() -> int:
    args = parse_args()
    root = Path(args.dir)
    if not root.exists():
        raise SystemExit(f"Dir not found: {root}")

    internal_urls: List[str] = []
    internal_pool_file = Path(args.internal_link_pool) if args.internal_link_pool else None
    if internal_pool_file and internal_pool_file.exists():
        internal_urls = gen.extract_internal_link_pool_urls(gen._load_internal_link_pool_text(internal_pool_file))

    catalog_paths: List[str] = []
    assets_catalog_file = Path(args.assets_image_catalog) if args.assets_image_catalog else None
    if assets_catalog_file and assets_catalog_file.exists():
        catalog_paths = gen.load_assets_image_catalog_paths(assets_catalog_file)

    md_files = sorted([p for p in root.rglob("*.md") if p.is_file()])
    changed = 0
    for path in md_files:
        original = path.read_text(encoding="utf-8", errors="ignore")
        keyword = _parse_keyword_from_front_matter(original, fallback=path.stem.replace("-", " "))

        updated = original
        kind = gen._infer_article_kind_from_content(updated)
        # If the file lives under a story output directory, treat it as story even if the
        # title marker is missing (older runs sometimes omitted the narrative suffix).
        if "blogs_aptpcb_story_v3" in str(path).replace("\\", "/"):
            kind = "story"

        # For playbook posts, enforce a consistent “A-grade” structure even for older outputs.
        if kind == "playbook":
            missing = []
            import re

            if not re.search(r"(?im)^\s*##\s*Key\s*Takeaways\b", updated):
                missing.append("Key Takeaways")
            if not re.search(r"(?im)^\s*##\s*Specifications\s+to\s+Define\s+Upfront\b", updated):
                missing.append("Specifications to define upfront")
            if not re.search(r"(?im)^\s*##\s*Supplier\s+Qualification\s+Checklist\b", updated):
                missing.append("Supplier qualification checklist")
            if not re.search(r"(?im)^\s*##\s+.*\bFAQ\b", updated):
                missing.append("FAQ")
            if not re.search(r"(?im)^\s*##\s+.*\bGlossary\b", updated):
                missing.append("Glossary")
            if not re.search(r"(?im)^\s*##\s*Conclusion\b", updated):
                missing.append("Conclusion")

            if missing:
                updated = gen.repair_missing_required_sections_locally(
                    updated, keyword=keyword, lsi_keywords=[], missing_sections=missing
                )
            updated = gen.ensure_playbook_section_tables(updated, keyword=keyword)

        updated = gen.ensure_opening_paragraph(updated, keyword=keyword, kind=kind)
        updated = gen.ensure_highlights(updated, keyword=keyword, kind=kind)
        updated = gen.ensure_front_matter_description(updated, keyword=keyword)
        # These are EN blog folders; apply title case normalization for consistency.
        updated = gen.ensure_title_case_and_headings(updated, language="英文")
        updated = gen.normalize_h1_to_front_matter_title(updated, fallback_title=keyword)
        updated = gen.fix_malformed_conclusion_heading(updated)
        updated = gen.repair_truncated_key_takeaways(updated)
        updated = gen.ensure_blog_quick_quote_marker(updated, kind_hint=kind)
        updated = gen.fix_toc_leaked_into_key_takeaways(updated)
        if kind == "story":
            updated = gen.strip_story_key_takeaways(updated, kind_hint=kind)
            updated = gen.fix_story_context_heading(updated, kind_hint=kind)
            updated = gen.rebuild_contents_toc(updated, kind_hint=kind)
        else:
            updated = gen.ensure_contents_toc(updated, kind_hint=kind)

        # Enforce playbook/pillar extras for SEO consistency: 6–10 internal links + ≥2 images (hero + 1 in-body).
        if kind in {"playbook", "pillar"}:
            if internal_urls:
                updated = gen.prune_generic_related_resources_blocks(updated)
                updated = gen.ensure_internal_links(
                    updated,
                    internal_urls=internal_urls,
                    min_links=6,
                    max_links=10,
                    keyword=keyword,
                    lsi_keywords=[],
                )
            if catalog_paths:
                pool = gen.select_assets_image_pool(
                    catalog_paths=catalog_paths,
                    keyword=keyword,
                    lsi_keywords=[],
                    pool_size=18,
                )
                pool_paths = list(pool or [])
                hero_path = pool_paths[0] if pool_paths else ""
                if hero_path:
                    updated = gen.ensure_min_images(
                        updated, hero_path=hero_path, candidate_paths=pool_paths, min_images=2
                    )

        if updated.strip() + "\n" != original.strip() + "\n":
            changed += 1
            if args.dry_run:
                print(f"[DRY] {path}")
            else:
                path.write_text(updated, encoding="utf-8")
                print(f"[OK]  {path}")

    print(f"\nDone. changed={changed} total={len(md_files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
