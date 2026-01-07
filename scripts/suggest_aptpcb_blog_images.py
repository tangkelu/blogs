#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import batch_blog_generation_openai as gen  # noqa: E402


DEFAULT_CATALOG = Path("/code/hileap/frontendAPT/docs/assets-img-filenames.md")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Suggest /assets/img paths for an APTPCB blog topic.")
    p.add_argument("--keyword", required=True, help="Primary keyword / title concept.")
    p.add_argument("--lsi", default="", help="Comma-separated related keywords (optional).")
    p.add_argument("--catalog", default=str(DEFAULT_CATALOG), help="assets-img-filenames.md path.")
    p.add_argument("--pool-size", type=int, default=18, help="How many candidates to output.")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    catalog = Path(args.catalog)
    if not catalog.exists():
        raise SystemExit(f"Catalog not found: {catalog}")

    lsi = [s.strip() for s in (args.lsi or "").split(",") if s.strip()]
    catalog_paths = gen.load_assets_image_catalog_paths(catalog)
    pool = gen.select_assets_image_pool(
        catalog_paths=catalog_paths,
        keyword=args.keyword,
        lsi_keywords=lsi,
        pool_size=int(args.pool_size or 0),
    )
    print(gen.format_assets_image_pool_text(pool), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

