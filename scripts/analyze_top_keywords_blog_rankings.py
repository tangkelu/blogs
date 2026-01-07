#!/usr/bin/env python3
"""
Analyze why downloaded winner pages rank high by correlating Excel rank data with
on-page content features extracted from the saved Markdown under:

  /data/top_keywords_blog/<site>/*.md

Inputs:
  - top_blog_keywords/*.xlsx (Keyword/Position/URL/etc)
  - /data/top_keywords_blog/_manifest.jsonl (maps URL -> saved markdown path)

Outputs (default under /data/top_keywords_blog):
  - seo_features.csv
  - SEO_INSIGHTS.md
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Optional
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import pandas as pd

TRACKING_QUERY_KEYS = {
    "fbclid",
    "gclid",
    "mc_cid",
    "mc_eid",
    "igshid",
    "_ga",
    "ref",
    "source",
}
TRACKING_QUERY_PREFIXES = ("utm_",)


def normalize_url(url: str) -> str:
    url = str(url or "").strip()
    if not url:
        return ""
    parts = urlsplit(url)
    if not parts.scheme:
        parts = urlsplit("https://" + url)

    query_pairs = []
    for k, v in parse_qsl(parts.query, keep_blank_values=True):
        k_lower = k.lower()
        if k_lower in TRACKING_QUERY_KEYS:
            continue
        if any(k_lower.startswith(p) for p in TRACKING_QUERY_PREFIXES):
            continue
        query_pairs.append((k, v))

    new_query = urlencode(query_pairs, doseq=True)
    normalized = urlunsplit((parts.scheme, parts.netloc.lower(), parts.path, new_query, ""))
    return normalized


def domain_of(url: str) -> str:
    try:
        netloc = urlsplit(url).netloc.lower()
    except Exception:
        return ""
    if netloc.startswith("www."):
        netloc = netloc[4:]
    return netloc


@dataclass(frozen=True)
class MdFeatures:
    md_path: str
    title: str
    description: str
    date: str
    reading_time: Optional[int]
    word_count: int
    char_count: int
    h1: int
    h2: int
    h3: int
    images: int
    links_total: int
    links_internal: int
    links_external: int
    tables: int
    lists: int
    has_faq: bool
    has_conclusion: bool
    has_key_takeaways: bool


def parse_frontmatter(md_text: str) -> tuple[dict[str, str], str]:
    if not md_text.startswith("---\n"):
        return {}, md_text
    parts = md_text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, md_text
    fm_block = parts[0].splitlines()[1:]
    body = parts[1]
    fm: dict[str, str] = {}
    for line in fm_block:
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def extract_md_features(md_path: Path, *, site: str) -> Optional[MdFeatures]:
    try:
        text = md_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return None

    fm, body = parse_frontmatter(text)
    title = fm.get("title", "")
    description = fm.get("description", "")
    date = fm.get("date", "")
    reading_time = None
    if "readingTime" in fm:
        m = re.search(r"\d+", fm["readingTime"])
        if m:
            reading_time = int(m.group(0))

    # Basic structure counts
    h1 = len(re.findall(r"^#\s+", body, flags=re.MULTILINE))
    h2 = len(re.findall(r"^##\s+", body, flags=re.MULTILINE))
    h3 = len(re.findall(r"^###\s+", body, flags=re.MULTILINE))
    images = len(re.findall(r"!\[[^\]]*\]\([^)]+\)", body)) + len(re.findall(r"<img\b", body, flags=re.I))

    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", body)
    links_total = len(links)
    internal = 0
    external = 0
    for href in links:
        href = href.strip()
        if not href:
            continue
        if href.startswith("#"):
            continue
        if href.startswith("/"):
            internal += 1
            continue
        if href.startswith("http://") or href.startswith("https://"):
            if domain_of(href) == site:
                internal += 1
            else:
                external += 1
            continue
    links_internal = internal
    links_external = external

    # Tables: count markdown table separator lines like: | --- | --- |
    tables = len(
        re.findall(
            r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$",
            body,
            flags=re.MULTILINE,
        )
    )

    # Lists: count list item lines
    lists = len(re.findall(r"^(\s*)([-*+]\s+|\d+\.\s+)", body, flags=re.MULTILINE))

    # Word counts: approximate; include alnum tokens + CJK chars as 1 token
    tokens = re.findall(r"[A-Za-z0-9]+|[\u4e00-\u9fff]", body)
    word_count = len(tokens)
    char_count = len(body)

    lower = body.lower()
    has_faq = bool(re.search(r"\bfaq\b|frequently asked questions|常见问题|问题解答", lower))
    has_conclusion = bool(re.search(r"\bconclusion\b|\bsummary\b|结论|总结|小结", lower))
    has_key_takeaways = bool(re.search(r"key takeaways|要点|核心要点|重点摘要", lower))

    return MdFeatures(
        md_path=str(md_path),
        title=title,
        description=description,
        date=date,
        reading_time=reading_time,
        word_count=word_count,
        char_count=char_count,
        h1=h1,
        h2=h2,
        h3=h3,
        images=images,
        links_total=links_total,
        links_internal=links_internal,
        links_external=links_external,
        tables=tables,
        lists=lists,
        has_faq=has_faq,
        has_conclusion=has_conclusion,
        has_key_takeaways=has_key_takeaways,
    )


def load_manifest_ok(manifest_path: Path) -> dict[str, str]:
    """
    Return {normalized_url: md_path} using the latest ok record per URL.
    """
    url_to_md: dict[str, str] = {}
    if not manifest_path.exists():
        return url_to_md
    for line in manifest_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except Exception:
            continue
        if not rec.get("ok"):
            continue
        url = rec.get("url")
        md = rec.get("md")
        if not isinstance(url, str) or not isinstance(md, str):
            continue
        url_to_md[normalize_url(url)] = md
    return url_to_md


def spearman_rank_corr(xs: list[float], ys: list[float]) -> Optional[float]:
    if len(xs) != len(ys) or len(xs) < 8:
        return None

    def rank(vals: list[float]) -> list[float]:
        # average ranks for ties
        order = sorted(range(len(vals)), key=lambda i: vals[i])
        ranks = [0.0] * len(vals)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and vals[order[j + 1]] == vals[order[i]]:
                j += 1
            avg = (i + j + 2) / 2.0  # ranks are 1-based
            for k in range(i, j + 1):
                ranks[order[k]] = avg
            i = j + 1
        return ranks

    rx = rank(xs)
    ry = rank(ys)
    mx = sum(rx) / len(rx)
    my = sum(ry) / len(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    denx = sum((a - mx) ** 2 for a in rx) ** 0.5
    deny = sum((b - my) ** 2 for b in ry) ** 0.5
    if denx == 0 or deny == 0:
        return None
    return num / (denx * deny)


def median(values: list[float]) -> Optional[float]:
    values = [v for v in values if v is not None]
    if not values:
        return None
    return float(statistics.median(values))


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--excel-dir", default="top_blog_keywords")
    ap.add_argument("--output-dir", default="/data/top_keywords_blog")
    ap.add_argument("--manifest", default="/data/top_keywords_blog/_manifest.jsonl")
    ap.add_argument("--max-position", type=int, default=10, help="Only analyze rows with Position <= N (0 = all)")
    args = ap.parse_args(argv)

    excel_dir = Path(args.excel_dir)
    output_dir = Path(args.output_dir)
    manifest_path = Path(args.manifest)

    url_to_md = load_manifest_ok(manifest_path)
    if not url_to_md:
        raise SystemExit(f"No ok URLs found in manifest: {manifest_path}")

    excel_files = sorted(excel_dir.glob("*.xlsx"))
    if not excel_files:
        raise SystemExit(f"No Excel files under: {excel_dir}")

    wanted_cols = [
        "Keyword",
        "Position",
        "Previous position",
        "Search Volume",
        "Keyword Difficulty",
        "CPC",
        "URL",
    ]

    rows: list[dict[str, Any]] = []
    for xlsx in excel_files:
        try:
            df = pd.read_excel(xlsx)
        except Exception:
            continue
        if "URL" not in df.columns or "Position" not in df.columns:
            continue
        keep_cols = [c for c in wanted_cols if c in df.columns]
        df = df[keep_cols].copy()
        df["URL_norm"] = df["URL"].astype(str).map(normalize_url)
        df = df[df["URL_norm"].isin(url_to_md.keys())]
        if args.max_position and int(args.max_position) > 0:
            df["Position"] = pd.to_numeric(df["Position"], errors="coerce").fillna(999999).astype(int)
            df = df[df["Position"] <= int(args.max_position)]
        if df.empty:
            continue
        # add domain and md path
        df["Site"] = df["URL_norm"].map(domain_of)
        df["MdPath"] = df["URL_norm"].map(url_to_md.get)
        rows.append(df)

    if not rows:
        raise SystemExit("No matching rows after joining Excel with manifest.")

    rank_df = pd.concat(rows, ignore_index=True)

    # Extract md features once per md file
    md_cache: dict[str, MdFeatures] = {}
    unique_md_paths = sorted({p for p in rank_df["MdPath"].dropna().astype(str).tolist() if p})
    for md_str in unique_md_paths:
        md_path = Path(md_str)
        if not md_path.exists():
            continue
        site = md_path.parent.name  # /data/top_keywords_blog/<site>/<slug>.md
        feats = extract_md_features(md_path, site=site)
        if feats:
            md_cache[md_str] = feats

    def col(name: str):
        return rank_df["MdPath"].map(lambda p: getattr(md_cache.get(str(p), None), name, None))

    for field in (
        "title",
        "description",
        "date",
        "reading_time",
        "word_count",
        "char_count",
        "h1",
        "h2",
        "h3",
        "images",
        "links_total",
        "links_internal",
        "links_external",
        "tables",
        "lists",
        "has_faq",
        "has_conclusion",
        "has_key_takeaways",
    ):
        rank_df[field] = col(field)

    # Persist feature dataset
    out_csv = output_dir / "seo_features.csv"
    rank_df.to_csv(out_csv, index=False)

    # Summaries
    # bucket by position
    rank_df["Position"] = pd.to_numeric(rank_df["Position"], errors="coerce").fillna(999999).astype(int)
    buckets = {
        "pos_1_3": rank_df[(rank_df["Position"] >= 1) & (rank_df["Position"] <= 3)],
        "pos_4_10": rank_df[(rank_df["Position"] >= 4) & (rank_df["Position"] <= 10)],
        "pos_11_20": rank_df[(rank_df["Position"] >= 11) & (rank_df["Position"] <= 20)],
        "pos_21_100": rank_df[(rank_df["Position"] >= 21) & (rank_df["Position"] <= 100)],
    }

    def bucket_stats(df: pd.DataFrame) -> dict[str, Any]:
        def med(series_name: str) -> Optional[float]:
            vals = df[series_name].dropna().astype(float).tolist()
            return median(vals)

        def pct_true(series_name: str) -> Optional[float]:
            vals = df[series_name].dropna()
            if vals.empty:
                return None
            return float((vals.astype(bool).mean()) * 100.0)

        return {
            "n": int(len(df)),
            "med_word_count": med("word_count"),
            "med_h2": med("h2"),
            "med_images": med("images"),
            "med_links_total": med("links_total"),
            "pct_has_faq": pct_true("has_faq"),
            "pct_has_conclusion": pct_true("has_conclusion"),
            "pct_has_table": (
                float((df["tables"].fillna(0).astype(float) > 0).mean()) * 100.0 if len(df) else None
            ),
        }

    bucket_summary = {k: bucket_stats(v) for k, v in buckets.items()}

    # correlations (lower position is better)
    corr_fields = ["word_count", "h2", "images", "links_total", "tables", "lists"]
    corrs: dict[str, Optional[float]] = {}
    sample = rank_df.dropna(subset=corr_fields + ["Position"]).copy()
    if len(sample) >= 20:
        pos = sample["Position"].astype(float).tolist()
        for f in corr_fields:
            xs = sample[f].astype(float).tolist()
            corrs[f] = spearman_rank_corr(xs, pos)

    # Top sites by count of top3 rows
    top3 = buckets["pos_1_3"]
    top_sites = (
        top3.groupby("Site", dropna=True)
        .size()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
        .rename(columns={0: "top3_rows"})
    )

    # Write report
    out_md = output_dir / "SEO_INSIGHTS.md"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines: list[str] = []
    lines.append(f"# SEO Insights from /data/top_keywords_blog\n")
    lines.append(f"- Generated: {now}\n")
    lines.append(f"- Excel dir: `{excel_dir}`\n")
    lines.append(f"- Manifest: `{manifest_path}`\n")
    lines.append(f"- Output CSV: `{out_csv}`\n")
    lines.append("")
    lines.append("## Coverage\n")
    lines.append(f"- Joined Excel rows: **{len(rank_df)}** (each row = a keyword ranking for a URL)\n")
    lines.append(f"- Unique URLs (downloaded ok): **{len(url_to_md)}**\n")
    lines.append(f"- Unique markdown files used: **{len(md_cache)}**\n")
    lines.append("")
    lines.append("## On-page profile by position bucket\n")
    for name, s in bucket_summary.items():
        lines.append(f"### {name}\n")
        lines.append(f"- rows: {s['n']}\n")
        lines.append(f"- median word_count: {s['med_word_count']}\n")
        lines.append(f"- median h2: {s['med_h2']}\n")
        lines.append(f"- median images: {s['med_images']}\n")
        lines.append(f"- median links_total: {s['med_links_total']}\n")
        lines.append(f"- has FAQ (%): {s['pct_has_faq']}\n")
        lines.append(f"- has conclusion (%): {s['pct_has_conclusion']}\n")
        lines.append(f"- has table (%): {s['pct_has_table']}\n")
        lines.append("")
    lines.append("## Correlations (Spearman) with Position\n")
    lines.append("(Negative = higher value tends to rank better, i.e. lower Position.)\n")
    for f, v in corrs.items():
        lines.append(f"- {f}: {v}\n")
    lines.append("")
    lines.append("## Top sites by top-3 rows\n")
    for _, r in top_sites.iterrows():
        lines.append(f"- {r['Site']}: {int(r['top3_rows'])}\n")
    lines.append("")
    lines.append("## Practical next steps\n")
    lines.append("1. **Intent + format mapping**: For each high-volume keyword (Position<=3), label the content type (definition/How-to/list/comparison) and replicate the same format in your content.\n")
    lines.append("2. **Build topic clusters**: Use the tags/keywords in Excel to build hub pages + supporting articles, then add internal links between them (winner pages usually have stronger internal linking).\n")
    lines.append("3. **Add snippet-friendly sections**: Put a 2–3 sentence definition under H1, add short Q&A blocks (FAQ), and add tables where comparison/spec is relevant.\n")
    lines.append("4. **E-E-A-T signals**: Add author/about, references, publish/updated dates, and real images/diagrams where needed; many winners are comprehensive guides.\n")
    lines.append("5. **Technical + crawl**: Ensure canonical, clean URLs, fast pages, and avoid blocking bots; many failures here were 403/202 which also hints sites control crawling.\n")
    lines.append("")

    out_md.write_text("".join(lines), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
