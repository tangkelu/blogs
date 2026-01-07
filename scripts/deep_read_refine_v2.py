#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path("/data/top_keywords_blog")
CSV_PATH = ROOT / "seo_features.csv"
OUT_DIR = ROOT / "deep_read_v2"


INTENT_ORDER = [
    "comparison_vs",
    "how_to",
    "definition_meaning",
    "cost",
    "lead_time",
    "troubleshooting",
    "other",
]


STOP_H2_RE = re.compile(
    r"^(?:"
    r"conclusion\b|summary\b|references?\b|faqs?\b|frequently asked questions\b"
    r"|talk to a\b|assemble \d+ pcbs\b|start a turn-?key pcb\b"
    r"|pcb manufacturing and assembly\b|related (?:articles|blogs)\b|older posts\b"
    r"|impedance calculator\b|bom checker\b|stackup designer\b"
    r")",
    flags=re.I,
)

STOP_H3_RE = re.compile(
    r"^(?:"
    r"no time now\b|stay cutting edge\b|table of contents\b|contents\b"
    r"|get instant pcb quotations\b|about\b|you may also be\b|related (?:articles|blogs)\b"
    r"|how good is my\b|on-demand webinar\b|download now\b|watch now\b"
    r"|pcb design tool\b|design for manufacturing handbook\b"
    r")",
    flags=re.I,
)


def _strip_md_links(text: str) -> str:
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)


def _strip_md_formatting(text: str) -> str:
    t = _strip_md_links(text)
    t = re.sub(r"`([^`]+)`", r"\1", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)
    t = re.sub(r"\*([^*]+)\*", r"\1", t)
    t = re.sub(r"_([^_]+)_", r"\1", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def _sentences(text: str) -> list[str]:
    t = _strip_md_formatting(text)
    if not t:
        return []
    parts = re.split(r"(?<=[.!?])\s+", t)
    return [p.strip() for p in parts if p.strip()]


def _split_frontmatter(md: str) -> tuple[str, str] | None:
    if not md.lstrip().startswith("---\n"):
        return None
    parts = md.split("\n---\n", 1)
    if len(parts) != 2:
        return None
    return parts[0] + "\n---\n", parts[1]


def _extract_h1(body: str) -> str | None:
    for line in body.splitlines():
        s = line.strip()
        if not s:
            continue
        m = re.match(r"^#\s+(.+)$", s)
        return _strip_md_formatting(m.group(1)) if m else None
    return None


@dataclass(frozen=True)
class Heading:
    level: int
    text: str
    line_idx: int


def _extract_headings_with_positions(body: str) -> list[Heading]:
    out: list[Heading] = []
    for idx, line in enumerate(body.splitlines()):
        s = line.strip()
        m2 = re.match(r"^##\s+(.+)$", s)
        if m2:
            out.append(Heading(2, _strip_md_formatting(m2.group(1)), idx))
            continue
        m3 = re.match(r"^###\s+(.+)$", s)
        if m3:
            out.append(Heading(3, _strip_md_formatting(m3.group(1)), idx))
            continue
    return out


def _canonicalize_section(h2: str) -> str:
    t = h2.lower().replace("’", "'")
    if "faq" in t or t.startswith("frequently asked"):
        return "FAQ"
    if "glossary" in t:
        return "Glossary"
    if t.startswith("conclusion") or "next steps" in t:
        return "Conclusion"
    if "quick answer" in t or "tl;dr" in t or "key takeaways" in t or "highlights" in t:
        return "Quick answer / takeaways"
    if "table of contents" in t or t == "contents" or "menu navigation" in t:
        return "TOC"
    if "troubleshoot" in t or "failure" in t or "defect" in t or "root cause" in t:
        return "Troubleshooting / failure modes"
    if "common mistakes" in t or "pitfalls" in t:
        return "Common mistakes"
    if "how to" in t or "steps" in t or "process" in t or "procedure" in t:
        return "Steps / process"
    if "cost" in t or "price" in t:
        return "Cost"
    if "lead time" in t or "turnaround" in t:
        return "Lead time"
    if "vs" in t or "versus" in t or "difference" in t or "compare" in t or "how to choose" in t:
        return "Comparison / selection"
    if "spec" in t or "rules" in t or "requirements" in t or "tolerance" in t or "parameters" in t:
        return "Rules / specs"
    if "test" in t or "validation" in t or "acceptance" in t or "inspection" in t:
        return "Validation / acceptance"
    if "standard" in t or "ipc" in t or "iec" in t or "ul" in t:
        return "Standards / references"
    if "material" in t or "stackup" in t:
        return "Materials / stackup"
    if "application" in t or "industry" in t or "use case" in t:
        return "Applications"
    if "related" in t or "resources" in t or "tools" in t:
        return "Related resources"
    if "what is" in t or "meaning" in t or "definition" in t or "scope" in t or "overview" in t:
        return "Definition & scope"
    return "Other"


def _infer_page_intent(url: str, keyword_examples: list[str], h1: str | None, h2_list: list[str]) -> str:
    u = (url or "").lower()
    k = " ".join(kw.lower() for kw in keyword_examples[:5])
    text = " ".join([u, k, (h1 or "").lower(), " ".join(h.lower() for h in h2_list[:10])])
    if re.search(r"\b(vs|versus)\b", text) or re.search(r"/[^/]*-vs-[^/]*", u):
        return "comparison_vs"
    if re.search(r"\bhow to\b", text) or "/how" in u:
        return "how_to"
    if re.search(r"\b(meaning|definition|what is|what does)\b", text) or "/what" in u:
        return "definition_meaning"
    if re.search(r"\b(cost|price)\b", text):
        return "cost"
    if re.search(r"\b(lead time|turnaround)\b", text):
        return "lead_time"
    if re.search(r"\b(troubleshoot|defect|failure|root cause)\b", text):
        return "troubleshooting"
    return "other"


def _read_csv_minpos_and_meta() -> dict[str, dict[str, Any]]:
    by_md: dict[str, dict[str, Any]] = {}
    with CSV_PATH.open(newline="", encoding="utf-8", errors="ignore") as f:
        r = csv.DictReader(f)
        for row in r:
            md = (row.get("MdPath") or "").strip()
            if not md:
                continue
            d = by_md.setdefault(
                md,
                {
                    "md_path": md,
                    "site": (row.get("Site") or "").strip(),
                    "url": (row.get("URL_norm") or row.get("URL") or "").strip(),
                    "keywords": [],
                    "min_pos": 1e9,
                },
            )
            kw = (row.get("Keyword") or "").strip()
            if kw and len(d["keywords"]) < 10:
                d["keywords"].append(kw)
            try:
                pos = float(row.get("Position") or "")
                if pos < d["min_pos"]:
                    d["min_pos"] = pos
            except Exception:
                pass
    return by_md


def _heading_stem(h: str, n_words: int = 4) -> str:
    toks = re.split(r"\s+", h.strip())
    return " ".join(toks[:n_words]).lower()


def _extract_opening_paragraph(body: str) -> str:
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        if re.match(r"^#\s+", lines[i].strip()):
            i += 1
            break
        i += 1
    while i < len(lines) and (lines[i].strip() == "" or lines[i].strip().startswith("![")):
        i += 1
    para: list[str] = []
    while i < len(lines):
        s = lines[i].strip()
        if not s:
            break
        if re.match(r"^#{1,6}\s+", s):
            break
        if s.startswith("|"):
            break
        para.append(s)
        i += 1
    return _strip_md_formatting(" ".join(para))


def _detect_tables(body: str) -> list[list[str]]:
    lines = body.splitlines()
    headers: list[list[str]] = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("|") and "|" in line[1:]:
            if i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?[-]{3,}", lines[i + 1]):
                cols = [c.strip() for c in line.strip("|").split("|")]
                cols = [_strip_md_formatting(c) for c in cols if c.strip()]
                if cols:
                    headers.append(cols)
                i += 2
                while i < len(lines) and lines[i].strip().startswith("|"):
                    i += 1
                continue
        i += 1
    return headers


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    meta = _read_csv_minpos_and_meta()

    pages = []
    for md, d in meta.items():
        p = Path(md)
        if not p.exists():
            continue
        if d["min_pos"] <= 3:
            pages.append(d)

    # Aggregations
    h2_stems: dict[str, Counter[str]] = defaultdict(Counter)
    h3_stems: dict[str, Counter[str]] = defaultdict(Counter)
    seq_counts: dict[str, Counter[tuple[str, ...]]] = defaultdict(Counter)
    opening_patterns: dict[str, Counter[str]] = defaultdict(Counter)
    table_header_counts: dict[str, Counter[tuple[str, ...]]] = defaultdict(Counter)
    removed_h2: Counter[str] = Counter()
    removed_h3: Counter[str] = Counter()

    for d in pages:
        md_path = Path(d["md_path"])
        raw = md_path.read_text(encoding="utf-8", errors="ignore")
        parts = _split_frontmatter(raw)
        if not parts:
            continue
        _fm, body = parts
        headings = _extract_headings_with_positions(body)
        h1 = _extract_h1(body)
        h2_list = [h.text for h in headings if h.level == 2]
        intent = _infer_page_intent(d["url"], d["keywords"], h1, h2_list)

        # Opening sentence signal buckets
        opening_para = _extract_opening_paragraph(body)
        first = _sentences(opening_para)[:1]
        if first:
            s = first[0].lower()
            if re.search(r"\bis\b|\bare\b|\bmeans\b|\brefers to\b", s):
                opening_patterns[intent]["definition_like"] += 1
            if re.search(r"\bhelps\b|\bmatters\b|\bused\b|\bimportant\b", s):
                opening_patterns[intent]["why_like"] += 1
            if re.search(r"\bshows\b|\bexplains\b|\bprovides\b|\bguide\b", s):
                opening_patterns[intent]["promise_like"] += 1
            opening_patterns[intent]["has_opening"] += 1

        # Tables
        for hdr in _detect_tables(body):
            # Drop obviously irrelevant schemas (polls, rankings) unless useful.
            if len(hdr) >= 2 and hdr[0].lower() in {"ranking", "rank"} and "answers" in " ".join(h.lower() for h in hdr):
                continue
            table_header_counts[intent][tuple(hdr)] += 1

        # Headings
        seq: list[str] = []
        for h in headings:
            if h.level == 2:
                if STOP_H2_RE.match(h.text):
                    removed_h2[_heading_stem(h.text, 6)] += 1
                    continue
                seq.append(_canonicalize_section(h.text))
                h2_stems[intent][_heading_stem(h.text, 4)] += 1
            elif h.level == 3:
                if STOP_H3_RE.match(h.text):
                    removed_h3[_heading_stem(h.text, 6)] += 1
                    continue
                h3_stems[intent][_heading_stem(h.text, 4)] += 1
        if seq:
            seq_counts[intent][tuple(seq)] += 1

    # Write assets
    # SECTION_BLUEPRINTS.md
    lines: list[str] = []
    lines.append("# Deep Read v2: Section Blueprints (Top3 only, boilerplate removed)")
    lines.append("")
    for intent in INTENT_ORDER:
        counter = seq_counts.get(intent, Counter())
        total = sum(counter.values())
        if total == 0:
            continue
        lines.append(f"## {intent} (pages={total})")
        for seq, c in counter.most_common(8):
            lines.append(f"- {c}×: " + " > ".join(seq))
        lines.append("")
    (OUT_DIR / "SECTION_BLUEPRINTS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # TABLE_SCHEMAS.md
    tlines: list[str] = []
    tlines.append("# Deep Read v2: Table Schemas (Top3 only)")
    tlines.append("")
    for intent in INTENT_ORDER:
        counter = table_header_counts.get(intent, Counter())
        if not counter:
            continue
        tlines.append(f"## {intent}")
        for hdr, c in counter.most_common(15):
            tlines.append(f"- {c}×: " + " | ".join(hdr))
        tlines.append("")
    (OUT_DIR / "TABLE_SCHEMAS.md").write_text("\n".join(tlines) + "\n", encoding="utf-8")

    # HEADING_PATTERNS.md
    hl: list[str] = []
    hl.append("# Deep Read v2: Heading Stem Patterns (Top3 only, boilerplate removed)")
    hl.append("")
    for intent in INTENT_ORDER:
        c2 = h2_stems.get(intent, Counter())
        if not c2:
            continue
        hl.append(f"## {intent}")
        hl.append("Top H2 stems:")
        for stem, c in c2.most_common(30):
            hl.append(f"- {c}×: `{stem} …`")
        c3 = h3_stems.get(intent, Counter())
        if c3:
            hl.append("")
            hl.append("Top H3 stems:")
            for stem, c in c3.most_common(18):
                hl.append(f"- {c}×: `{stem} …`")
        hl.append("")
    (OUT_DIR / "HEADING_PATTERNS.md").write_text("\n".join(hl) + "\n", encoding="utf-8")

    # OPENING_PATTERNS.md
    ol: list[str] = []
    ol.append("# Deep Read v2: Opening Sentence Signal Buckets (Top3 only)")
    ol.append("")
    for intent in INTENT_ORDER:
        counter = opening_patterns.get(intent, Counter())
        total = counter.get("has_opening", 0)
        if total == 0:
            continue
        ol.append(f"## {intent} (pages={total})")
        for k in ["definition_like", "why_like", "promise_like"]:
            c = counter.get(k, 0)
            ol.append(f"- {k}: {c} ({(c/max(1,total))*100:.1f}%)")
        ol.append("")
    (OUT_DIR / "OPENING_PATTERNS.md").write_text("\n".join(ol) + "\n", encoding="utf-8")

    # BOILERPLATE_REMOVED.md
    bl: list[str] = []
    bl.append("# Deep Read v2: Removed boilerplate heading stems")
    bl.append("")
    bl.append("These frequent headings were filtered out before computing patterns.")
    bl.append("")
    bl.append("## H2 removed (top 30)")
    for stem, c in removed_h2.most_common(30):
        bl.append(f"- {c}×: `{stem} …`")
    bl.append("")
    bl.append("## H3 removed (top 30)")
    for stem, c in removed_h3.most_common(30):
        bl.append(f"- {c}×: `{stem} …`")
    bl.append("")
    (OUT_DIR / "BOILERPLATE_REMOVED.md").write_text("\n".join(bl) + "\n", encoding="utf-8")

    # Small JSON summary for programmatic use
    summary = {
        "pages_total_top3": len(pages),
        "intents": {intent: sum(seq_counts.get(intent, Counter()).values()) for intent in INTENT_ORDER},
        "removed_h2_top10": removed_h2.most_common(10),
        "removed_h3_top10": removed_h3.most_common(10),
    }
    (OUT_DIR / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"✅ deep_read_v2 assets written to: {OUT_DIR}")
    print(f"- pages_top3={len(pages)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
