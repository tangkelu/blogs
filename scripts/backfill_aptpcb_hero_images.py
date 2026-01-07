#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import batch_blog_generation_openai as gen  # noqa: E402


DEFAULT_CATALOG = Path("/code/hileap/frontendAPT/docs/assets-img-filenames.md")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Backfill hero images for generated APTPCB markdown blogs.")
    p.add_argument("--dir", required=True, help="Directory containing generated .md files (recursive).")
    p.add_argument("--catalog", default=str(DEFAULT_CATALOG), help="assets-img-filenames.md path.")
    p.add_argument("--pool-size", type=int, default=18, help="How many candidates to consider per post.")
    p.add_argument("--dry-run", action="store_true", help="Print actions but do not write files.")
    return p.parse_args()


def _split_front_matter(text: str) -> Optional[Tuple[List[str], List[str]]]:
    lines = (text or "").lstrip("\ufeff").splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, min(len(lines), 200)):
        if lines[i].strip() == "---":
            return lines[: i + 1], lines[i + 1 :]
    return None


def _fm_get(fm_lines: List[str], key: str) -> Optional[str]:
    pat = re.compile(rf"^\s*{re.escape(key)}\s*:\s*(.*?)\s*$")
    for line in fm_lines[1:]:
        if line.strip() == "---":
            break
        m = pat.match(line)
        if not m:
            continue
        val = m.group(1).strip()
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1].strip()
        return val
    return None


def _parse_tags(fm_lines: List[str]) -> List[str]:
    raw = _fm_get(fm_lines, "tags") or ""
    if not raw:
        return []
    # tags: ["a", "b"] / ['a','b'] / [a, b] (best effort)
    quoted = re.findall(r"""['"]([^'"]+)['"]""", raw)
    if quoted:
        return [t.strip() for t in quoted if t.strip()]
    # fallback: split by comma inside brackets
    raw = raw.strip().strip("[]").strip()
    parts = [p.strip().strip("'\"") for p in raw.split(",") if p.strip()]
    return [p for p in parts if p]


def main() -> int:
    args = parse_args()
    target_dir = Path(args.dir)
    catalog = Path(args.catalog)

    if not target_dir.exists():
        raise SystemExit(f"Dir not found: {target_dir}")
    if not catalog.exists():
        raise SystemExit(f"Catalog not found: {catalog}")

    catalog_paths = gen.load_assets_image_catalog_paths(catalog)
    if not catalog_paths:
        raise SystemExit(f"No /assets/img paths found in catalog: {catalog}")

    md_files = sorted([p for p in target_dir.rglob("*.md") if p.is_file()])
    changed = 0
    skipped = 0
    for path in md_files:
        original = path.read_text(encoding="utf-8", errors="ignore")
        split = _split_front_matter(original)
        if not split:
            skipped += 1
            continue
        fm_lines, _body_lines = split
        title = (_fm_get(fm_lines, "title") or "").strip()
        tags = _parse_tags(fm_lines)
        keyword = (tags[0] if tags else title) or path.stem.replace("-", " ")
        lsi = tags[1:] if len(tags) > 1 else []

        pool = gen.select_assets_image_pool(
            catalog_paths=catalog_paths,
            keyword=keyword,
            lsi_keywords=lsi,
            pool_size=int(args.pool_size or 0),
        )
        hero = pool[0] if pool else ""
        updated = gen.ensure_hero_image(original, hero)
        if updated != (original.strip() + "\n"):
            changed += 1
            if args.dry_run:
                print(f"[DRY] {path} -> hero={hero}")
            else:
                path.write_text(updated, encoding="utf-8")
                print(f"[OK]  {path} -> hero={hero}")
        else:
            skipped += 1

    print(f"\nDone. changed={changed} skipped={skipped} total={len(md_files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
