#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


MARKER = "<!-- COMPONENT: BlogQuickQuoteInline -->"
BANNED_PATTERNS = [
    r"\bSERP\b",
    r"People Also Ask",
    r"\bPAA\b",
    r"internal links required",
    r"\byou might be searching\b",
]


@dataclass(frozen=True)
class LintIssue:
    path: Path
    code: str
    message: str


def _split_frontmatter(md: str) -> tuple[str, str] | None:
    if not md.lstrip().startswith("---\n"):
        return None
    parts = md.split("\n---\n", 1)
    if len(parts) != 2:
        return None
    return parts[0], parts[1]


def _extract_title_from_frontmatter(fm_without_end: str) -> str | None:
    # Support both single-line and folded (>-) title.
    lines = fm_without_end.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^title:\s*(.*)\s*$", line)
        if not m:
            continue
        raw = m.group(1).strip()
        if raw.startswith("'") and raw.endswith("'"):
            return raw[1:-1].replace("''", "'")
        if raw.startswith('"') and raw.endswith('"'):
            return raw[1:-1]
        if raw in {">-", ">", "|-", "|"} or raw.startswith(">") or raw.startswith("|"):
            cont: list[str] = []
            j = i + 1
            while j < len(lines) and (lines[j].startswith("  ") or lines[j].startswith("\t")):
                cont.append(lines[j].strip())
                j += 1
            return re.sub(r"\s+", " ", " ".join(cont)).strip()
        return raw
    return None


def _first_h1(body: str) -> str | None:
    for line in body.splitlines():
        s = line.strip()
        if not s:
            continue
        m = re.match(r"^#\s+(.+)$", s)
        return m.group(1).strip() if m else None
    return None


def _has_toc_near_top(body: str) -> bool:
    head = "\n".join(body.splitlines()[:160]).lower()
    if re.search(r"^\s*#{2,4}\s*(contents|table of contents|menu navigation)\b", head, flags=re.M):
        return True
    if re.search(r"^\s*[-*]\s+\[[^\]]+\]\(#[-a-z0-9]+\)\s*$", head, flags=re.M):
        return True
    return False


def _has_highlights_near_top(body: str) -> bool:
    head = body.splitlines()[:160]
    for idx, line in enumerate(head):
        s = line.strip().lower()
        if re.match(r"^(?:\*\*|#{2,4}\s+)?(highlights|key takeaways|quick answer|tl;dr)\b", s):
            window = "\n".join(head[idx : idx + 40])
            if re.search(r"^\s*[-*]\s+", window, flags=re.M):
                return True
    return False


def _count_h1(body: str) -> int:
    n = 0
    for line in body.splitlines():
        if re.match(r"^#\s+[^#]", line.strip()):
            n += 1
    return n


def _table_headers(body: str) -> list[list[str]]:
    headers: list[list[str]] = []
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("|") and "|" in line[1:]:
            if i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?[-]{3,}", lines[i + 1]):
                cols = [c.strip() for c in line.strip("|").split("|") if c.strip()]
                if cols:
                    headers.append(cols)
                i += 2
                while i < len(lines) and lines[i].strip().startswith("|"):
                    i += 1
                continue
        i += 1
    return headers


def lint_file(path: Path, *, require_toc_over_words: int | None) -> list[LintIssue]:
    issues: list[LintIssue] = []
    text = path.read_text(encoding="utf-8", errors="ignore")

    parts = _split_frontmatter(text)
    if not parts:
        issues.append(LintIssue(path, "frontmatter_missing", "missing YAML front matter"))
        return issues
    fm_without_end, body = parts

    title = _extract_title_from_frontmatter(fm_without_end)
    if not title:
        issues.append(LintIssue(path, "title_missing", "missing frontmatter title"))
    h1 = _first_h1(body)
    if not h1:
        issues.append(LintIssue(path, "h1_missing", "missing H1 in body"))
    if title and h1 and title.strip() != h1.strip():
        issues.append(LintIssue(path, "h1_title_mismatch", f"H1 != title ({h1!r} vs {title!r})"))

    h1_count = _count_h1(body)
    if h1_count != 1:
        issues.append(LintIssue(path, "h1_count", f"expected exactly 1 H1, found {h1_count}"))

    if text.count(MARKER) != 1:
        issues.append(LintIssue(path, "quote_marker_count", f"expected marker exactly once, found {text.count(MARKER)}"))

    banned_re = re.compile("|".join(f"(?:{p})" for p in BANNED_PATTERNS), flags=re.I)
    if banned_re.search(text):
        issues.append(LintIssue(path, "seo_metatalk", "contains banned SEO meta terms"))

    # Highlights and TOC are soft requirements but strongly recommended for long pages.
    words = len(re.findall(r"\b\w+\b", body))
    if not _has_highlights_near_top(body):
        issues.append(LintIssue(path, "highlights_missing", "missing Highlights/Takeaways near top (heuristic)"))
    if require_toc_over_words is not None and words >= require_toc_over_words and not _has_toc_near_top(body):
        issues.append(LintIssue(path, "toc_missing", f"missing TOC near top for long page (words={words})"))

    # Ensure at least one table exists for winner-shaped pages.
    if not _table_headers(body):
        issues.append(LintIssue(path, "table_missing", "no Markdown table detected"))

    return issues


def _iter_md_paths(inputs: list[str]) -> list[Path]:
    out: list[Path] = []
    for inp in inputs:
        p = Path(inp)
        if p.is_dir():
            out.extend(sorted(p.rglob("*.md")))
        elif p.exists():
            out.append(p)
    # Drop non-files
    out = [p for p in out if p.is_file()]
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Lint generated blog markdown for APTPCB quality gates.")
    ap.add_argument("paths", nargs="+", help="Files or directories to lint")
    ap.add_argument("--toc-over-words", type=int, default=1800, help="Require TOC when body words >= this value (default: 1800)")
    args = ap.parse_args()

    paths = _iter_md_paths(args.paths)
    if not paths:
        print("No markdown files found.", file=sys.stderr)
        return 2

    all_issues: list[LintIssue] = []
    for p in paths:
        all_issues.extend(lint_file(p, require_toc_over_words=args.toc_over_words))

    if not all_issues:
        print(f"✅ Lint passed: {len(paths)} files")
        return 0

    # Print grouped by file, concise.
    by: dict[Path, list[LintIssue]] = {}
    for it in all_issues:
        by.setdefault(it.path, []).append(it)

    print(f"❌ Lint failed: {len(by)} files, {len(all_issues)} issues")
    for path, issues in sorted(by.items(), key=lambda kv: str(kv[0])):
        print(f"\n{path}")
        for iss in issues:
            print(f"- {iss.code}: {iss.message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

