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
OUT_DIR = ROOT / "deep_read"


INTENT_ORDER = [
    "comparison_vs",
    "how_to",
    "definition_meaning",
    "cost",
    "lead_time",
    "troubleshooting",
    "other",
]


def _read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _split_frontmatter(md: str) -> tuple[str, str] | None:
    if not md.lstrip().startswith("---\n"):
        return None
    # Keep original frontmatter (we only need body).
    # Note: files in this dataset are normalized to start with `---\n`.
    parts = md.split("\n---\n", 1)
    if len(parts) != 2:
        return None
    return parts[0] + "\n---\n", parts[1]


def _strip_md_links(text: str) -> str:
    # Replace [text](url) -> text
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
    # Simple sentence splitter, good enough for “opening 2–3 sentences”.
    t = _strip_md_formatting(text)
    if not t:
        return []
    parts = re.split(r"(?<=[.!?])\s+", t)
    return [p.strip() for p in parts if p.strip()]


def _extract_h1(body: str) -> str | None:
    for line in body.splitlines():
        if line.strip() == "":
            continue
        m = re.match(r"^#\s+(.+)$", line.strip())
        if m:
            return _strip_md_formatting(m.group(1))
        break
    return None


def _extract_opening_paragraph(body: str) -> str:
    """
    Return the first non-empty paragraph after H1, skipping images and headings.
    """
    lines = body.splitlines()
    i = 0
    # Skip until after first H1.
    while i < len(lines):
        if re.match(r"^#\s+", lines[i].strip()):
            i += 1
            break
        i += 1

    # Skip blank lines / images / components.
    def is_skip(line: str) -> bool:
        s = line.strip()
        if s == "":
            return True
        if s.startswith("![" ) and "](" in s:
            return True
        if s.startswith("<!--") and s.endswith("-->"):
            return True
        if re.match(r"^#{2,}\s+", s):
            return True
        return False

    while i < len(lines) and is_skip(lines[i]):
        i += 1

    # Collect paragraph until blank line.
    para: list[str] = []
    while i < len(lines):
        s = lines[i].strip()
        if s == "":
            break
        if re.match(r"^#{1,6}\s+", s):
            break
        if s.startswith("![" ) and "](" in s:
            break
        para.append(s)
        i += 1
    return _strip_md_formatting(" ".join(para))


def _extract_headings(body: str) -> dict[str, list[str]]:
    h2: list[str] = []
    h3: list[str] = []
    for line in body.splitlines():
        s = line.strip()
        m2 = re.match(r"^##\s+(.+)$", s)
        if m2:
            h2.append(_strip_md_formatting(m2.group(1)))
            continue
        m3 = re.match(r"^###\s+(.+)$", s)
        if m3:
            h3.append(_strip_md_formatting(m3.group(1)))
            continue
    return {"h2": h2, "h3": h3}


def _detect_toc(body: str) -> bool:
    # Heuristic: early “Contents/Menu Navigation/Table of contents” + anchor list.
    lines = body.splitlines()
    head = "\n".join(lines[:140]).lower()
    if re.search(r"^\s*#{2,4}\s*(contents|table of contents|menu navigation)\b", head, flags=re.M):
        return True
    # Anchor list near top: - [..](#..)
    if re.search(r"^\s*[-*]\s+\[[^\]]+\]\(#[-a-z0-9]+\)\s*$", head, flags=re.M):
        return True
    return False


def _detect_highlights(body: str) -> bool:
    # Heuristic: early “Highlights/Key takeaways/Quick answer” with bullets nearby.
    lines = body.splitlines()[:140]
    for idx, line in enumerate(lines):
        s = line.strip().lower()
        if re.match(r"^(?:\*\*|#{2,4}\s+)?(highlights|key takeaways|quick answer|tl;dr)\b", s):
            window = "\n".join(lines[idx : idx + 30])
            if re.search(r"^\s*[-*]\s+", window, flags=re.M):
                return True
    return False


def _detect_tables(body: str) -> list[list[str]]:
    # Extract table header rows: | a | b | c |
    lines = body.splitlines()
    headers: list[list[str]] = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("|") and "|" in line[1:]:
            # Next line must look like separator.
            if i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?[-]{3,}", lines[i + 1]):
                cols = [c.strip() for c in line.strip("|").split("|")]
                cols = [_strip_md_formatting(c) for c in cols if c.strip()]
                if cols:
                    headers.append(cols)
                # Skip ahead until table ends.
                i += 2
                while i < len(lines) and lines[i].strip().startswith("|"):
                    i += 1
                continue
        i += 1
    return headers


def _canonicalize_section(h: str) -> str:
    t = h.lower()
    t = t.replace("’", "'")
    if "faq" in t or t.startswith("frequently asked"):
        return "FAQ"
    if "glossary" in t:
        return "Glossary"
    if t.startswith("conclusion") or "next steps" in t:
        return "Conclusion"
    if "quick answer" in t or "tl;dr" in t or "key takeaways" in t or "highlights" in t:
        return "Quick answer / takeaways"
    if "troubleshoot" in t or "failure" in t or "defect" in t or "root cause" in t:
        return "Troubleshooting / failure modes"
    if "how to" in t or "steps" in t or "process" in t or "procedure" in t:
        return "Steps / process"
    if "cost" in t or "price" in t:
        return "Cost"
    if "lead time" in t or "turnaround" in t or "timeline" in t:
        return "Lead time"
    if "vs" in t or "versus" in t or "difference" in t or "compare" in t or "how to choose" in t:
        return "Comparison / selection"
    if "spec" in t or "rules" in t or "requirements" in t or "tolerance" in t or "parameters" in t:
        return "Rules / specs"
    if "test" in t or "validation" in t or "acceptance" in t or "inspection" in t:
        return "Validation / acceptance"
    if "mistake" in t or "pitfall" in t:
        return "Common mistakes"
    if "standard" in t or "ipc" in t or "iec" in t or "ul" in t:
        return "Standards / references"
    if "what is" in t or "meaning" in t or "definition" in t or "scope" in t or "overview" in t:
        return "Definition & scope"
    if "material" in t or "stackup" in t:
        return "Materials / stackup"
    if "related" in t or "resources" in t or "tools" in t:
        return "Related resources"
    return "Other"


def _infer_page_intent(url: str, keyword_examples: list[str], h1: str | None, h2: list[str]) -> tuple[str, list[str]]:
    """
    Primary intent is page-level (not keyword-level) inferred mainly from URL path,
    backed by keyword examples and headings.
    """
    u = (url or "").lower()
    k = " ".join(kw.lower() for kw in keyword_examples[:5])
    text = " ".join([u, k, (h1 or "").lower(), " ".join(h.lower() for h in h2[:8])])

    secondary: list[str] = []
    if re.search(r"\b(vs|versus)\b", text) or re.search(r"/[^/]*-vs-[^/]*", u):
        primary = "comparison_vs"
    elif re.search(r"\bhow to\b", text) or "/how" in u:
        primary = "how_to"
    elif re.search(r"\b(meaning|definition|what is|what does)\b", text) or "/what" in u:
        primary = "definition_meaning"
    elif re.search(r"\b(cost|price)\b", text):
        primary = "cost"
    elif re.search(r"\b(lead time|turnaround)\b", text):
        primary = "lead_time"
    elif re.search(r"\b(troubleshoot|defect|failure|root cause)\b", text):
        primary = "troubleshooting"
    else:
        primary = "other"

    # Secondary signals
    if primary != "comparison_vs" and re.search(r"\b(vs|versus|difference|how to choose)\b", text):
        secondary.append("comparison_vs")
    if primary != "how_to" and re.search(r"\bhow to\b", text):
        secondary.append("how_to")
    if primary != "troubleshooting" and re.search(r"\b(troubleshoot|defect|failure)\b", text):
        secondary.append("troubleshooting")
    if primary != "cost" and re.search(r"\bcost|price\b", text):
        secondary.append("cost")
    if primary != "lead_time" and re.search(r"\blead time|turnaround\b", text):
        secondary.append("lead_time")
    if primary != "definition_meaning" and re.search(r"\b(meaning|definition|what is)\b", text):
        secondary.append("definition_meaning")

    # De-dup, preserve order
    out_secondary: list[str] = []
    for it in secondary:
        if it not in out_secondary and it != primary:
            out_secondary.append(it)
    return primary, out_secondary


def _intent_to_skeleton(intent: str) -> str:
    if intent in {"definition_meaning", "how_to", "cost", "lead_time", "troubleshooting"}:
        return "query"
    if intent == "comparison_vs":
        return "query"  # query skeleton + comparison module works best
    return "pillar"


def _angle_modules(intent: str, h2: list[str]) -> list[str]:
    mods: list[str] = []
    if intent == "comparison_vs":
        mods.append("comparison")
    # capability angle cues
    joined = " ".join(h.lower() for h in h2)
    if re.search(r"\b(moq|lead time|ordering|request a quote|quote)\b", joined):
        mods.append("capability")
    if re.search(r"\b(application|industry|use case|industries)\b", joined):
        mods.append("application")
    # de-dup
    out: list[str] = []
    for m in mods:
        if m not in out:
            out.append(m)
    return out


@dataclass(frozen=True)
class PageIndexRow:
    md_path: str
    site: str
    url: str
    position_min: float | None
    position_median: float | None
    keyword_examples: list[str]


def _load_index_from_csv() -> list[PageIndexRow]:
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
                    "positions": [],
                    "keywords": [],
                },
            )
            kw = (row.get("Keyword") or "").strip()
            if kw and len(d["keywords"]) < 12:
                d["keywords"].append(kw)
            try:
                pos = float(row.get("Position") or "")
                d["positions"].append(pos)
            except Exception:
                pass

    rows: list[PageIndexRow] = []
    for md, d in by_md.items():
        pos_list = sorted(p for p in d["positions"] if p > 0)
        if pos_list:
            pos_min = pos_list[0]
            pos_med = pos_list[len(pos_list) // 2]
        else:
            pos_min = None
            pos_med = None
        rows.append(
            PageIndexRow(
                md_path=md,
                site=d["site"],
                url=d["url"],
                position_min=pos_min,
                position_median=pos_med,
                keyword_examples=d["keywords"],
            )
        )
    return rows


def _safe_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    pages = _load_index_from_csv()
    # Keep only existing md paths.
    pages = [p for p in pages if Path(p.md_path).exists()]

    # Outputs
    index_csv = OUT_DIR / "index_pages.csv"
    intents_csv = OUT_DIR / "page_intents.csv"
    features_jsonl = OUT_DIR / "page_features.jsonl"
    sequences_csv = OUT_DIR / "section_sequences.csv"

    # Aggregations
    seq_counts: dict[str, Counter[tuple[str, ...]]] = defaultdict(Counter)
    toc_counts: Counter[str] = Counter()
    highlights_counts: Counter[str] = Counter()
    table_header_counts: dict[str, Counter[tuple[str, ...]]] = defaultdict(Counter)
    opening_sentence_stats: dict[str, Counter[str]] = defaultdict(Counter)
    skeleton_counts: Counter[str] = Counter()
    module_counts: Counter[str] = Counter()

    # Write headers
    with index_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["MdPath", "Site", "URL_norm", "position_min", "position_median", "keyword_examples"])
        for p in pages:
            w.writerow([p.md_path, p.site, p.url, p.position_min, p.position_median, " | ".join(p.keyword_examples[:6])])

    with intents_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["MdPath", "Site", "URL_norm", "intent_primary", "intent_secondary", "skeleton", "modules"])

        with features_jsonl.open("w", encoding="utf-8") as jf:
            for p in pages:
                path = Path(p.md_path)
                raw = _read_file(path)
                parts = _split_frontmatter(raw)
                if not parts:
                    continue
                _fm, body = parts

                headings = _extract_headings(body)
                h1 = _extract_h1(body)
                opening_para = _extract_opening_paragraph(body)
                opening_sents = _sentences(opening_para)[:3]

                has_toc = _detect_toc(body)
                has_highlights = _detect_highlights(body)
                table_headers = _detect_tables(body)

                intent_primary, intent_secondary = _infer_page_intent(p.url, p.keyword_examples, h1, headings["h2"])
                skeleton = _intent_to_skeleton(intent_primary)
                modules = _angle_modules(intent_primary, headings["h2"])

                w.writerow([p.md_path, p.site, p.url, intent_primary, "|".join(intent_secondary), skeleton, "|".join(modules)])

                # Canonical section sequence from H2 headings
                seq = tuple(_canonicalize_section(h) for h in headings["h2"])
                if seq:
                    seq_counts[intent_primary][seq] += 1

                toc_counts[intent_primary] += 1 if has_toc else 0
                highlights_counts[intent_primary] += 1 if has_highlights else 0
                skeleton_counts[skeleton] += 1
                for m in modules:
                    module_counts[m] += 1

                for hdr in table_headers:
                    table_header_counts[intent_primary][tuple(hdr)] += 1

                if opening_sents:
                    first = opening_sents[0]
                    # Coarse pattern buckets
                    if re.search(r"\bis\b|\bare\b|\brefers to\b|\bmeans\b", first, flags=re.I):
                        opening_sentence_stats[intent_primary]["definition_like"] += 1
                    if re.search(r"\bhelps\b|\bmatters\b|\bused\b|\bimportant\b", first, flags=re.I):
                        opening_sentence_stats[intent_primary]["why_like"] += 1
                    opening_sentence_stats[intent_primary]["has_opening"] += 1

                jf.write(
                    json.dumps(
                        {
                            "md_path": p.md_path,
                            "site": p.site,
                            "url": p.url,
                            "intent_primary": intent_primary,
                            "intent_secondary": intent_secondary,
                            "skeleton": skeleton,
                            "modules": modules,
                            "position_min": p.position_min,
                            "position_median": p.position_median,
                            "h1": h1,
                            "h2_count": len(headings["h2"]),
                            "h3_count": len(headings["h3"]),
                            "has_toc": has_toc,
                            "has_highlights": has_highlights,
                            "opening_sentences": opening_sents,
                            "table_headers": table_headers[:5],
                            "canonical_h2_sequence": list(seq),
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )

    # Section sequence summary
    with sequences_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["intent", "sequence", "count"])
        for intent in INTENT_ORDER:
            counter = seq_counts.get(intent, Counter())
            for seq, c in counter.most_common(30):
                w.writerow([intent, " > ".join(seq), c])

    # Write human-readable assets (first iteration)
    # SECTION_BLUEPRINTS.md
    lines: list[str] = []
    lines.append("# Deep Read: Section Blueprints (derived from top pages)")
    lines.append("")
    lines.append("This file summarizes common section sequences found in the ranking-referenced corpus.")
    lines.append("It is **pattern-level only** (no competitor text copying).")
    lines.append("")

    total_by_intent = Counter()
    for intent in INTENT_ORDER:
        total_by_intent[intent] = sum(seq_counts.get(intent, Counter()).values())

    for intent in INTENT_ORDER:
        n = total_by_intent[intent]
        if n == 0:
            continue
        toc_pct = (toc_counts[intent] / max(1, n)) * 100
        hl_pct = (highlights_counts[intent] / max(1, n)) * 100
        lines.append(f"## {intent} (pages={n})")
        lines.append(f"- has TOC (heuristic): {toc_pct:.1f}%")
        lines.append(f"- has Highlights/Takeaways (heuristic): {hl_pct:.1f}%")
        lines.append("")
        lines.append("Top canonical H2 sequences (first 5):")
        for seq, c in seq_counts[intent].most_common(5):
            lines.append(f"- {c}×: {' > '.join(seq)}")
        lines.append("")

    _safe_write(OUT_DIR / "SECTION_BLUEPRINTS.md", "\n".join(lines))

    # TABLE_SCHEMAS.md
    tlines: list[str] = []
    tlines.append("# Deep Read: Table Schemas (derived from top pages)")
    tlines.append("")
    tlines.append("This is a list of frequent table header schemas. Use them as *formats*, not as copied content.")
    tlines.append("")
    for intent in INTENT_ORDER:
        counter = table_header_counts.get(intent, Counter())
        if not counter:
            continue
        tlines.append(f"## {intent}")
        for hdr, c in counter.most_common(12):
            tlines.append(f"- {c}×: " + " | ".join(hdr))
        tlines.append("")
    _safe_write(OUT_DIR / "TABLE_SCHEMAS.md", "\n".join(tlines))

    # PHRASE_BANKS.md (pattern library, not copied phrases)
    plines: list[str] = []
    plines.append("# Deep Read: Phrase Banks (rewrite-safe patterns)")
    plines.append("")
    plines.append("These are **rewrite-safe** patterns derived from common section functions in top pages.")
    plines.append("Do not copy competitor sentences; use these patterns with `{{keyword}}`.")
    plines.append("")
    plines.append("## Answer-first opening (2–3 sentences)")
    plines.append("- `{{keyword}}` is … (definition in plain English).")
    plines.append("- It matters when … (use-case / boundary).")
    plines.append("- In this guide you’ll get … (rules + checks + next steps).")
    plines.append("")
    plines.append("## Bridging sentence (first line of each H2)")
    plines.append("- Now that the basics are clear, the next step is …")
    plines.append("- With the key constraints defined, let’s look at …")
    plines.append("- To avoid common failures, focus on …")
    plines.append("")
    plines.append("## Decision rules")
    plines.append("- If you prioritize **X**, choose **Y** because …; otherwise choose **Z** (trade-off).")
    plines.append("- If **environment/volume/test** is the constraint, lock these parameters first: …")
    plines.append("")
    plines.append("## Troubleshooting micro-template")
    plines.append("- **Symptom → likely causes → checks → fix → prevention**")
    plines.append("")
    plines.append("## FAQ question patterns (long-tail modifiers)")
    plines.append("- `{{keyword}} cost`: What drives cost, and how to reduce risk?")
    plines.append("- `{{keyword}} lead time`: What changes timeline, and what to send early?")
    plines.append("- `{{keyword}} materials`: Which materials fit which constraints?")
    plines.append("- `{{keyword}} testing`: What test methods + pass criteria matter?")
    plines.append("- `{{keyword}} acceptance criteria`: What does “pass” mean in practice?")
    plines.append("")
    _safe_write(OUT_DIR / "PHRASE_BANKS.md", "\n".join(plines))

    # A compact intent selector artifact (for prompts usage)
    slines: list[str] = []
    slines.append("# Deep Read: Intent → skeleton + modules (selector)")
    slines.append("")
    slines.append("This selector is derived from URL/keyword/heading signals across the ranking-referenced corpus.")
    slines.append("")
    slines.append("## Primary intent mapping")
    slines.append("- `comparison_vs` → skeleton: `query` + module: `comparison`")
    slines.append("- `how_to` → skeleton: `query` (+ module: `capability` if ordering/quote cues exist)")
    slines.append("- `definition_meaning` → skeleton: `query` (add glossary if term-heavy)")
    slines.append("- `cost` / `lead_time` → skeleton: `query` + stronger tables")
    slines.append("- `troubleshooting` → skeleton: `query` + failure-mode template")
    slines.append("- `other` → skeleton: `pillar` (use as hub when broad)")
    slines.append("")
    slines.append("## Observed skeleton distribution (from inference)")
    for sk, c in skeleton_counts.most_common():
        slines.append(f"- {sk}: {c}")
    slines.append("")
    slines.append("## Observed module cues (from headings)")
    for m, c in module_counts.most_common():
        slines.append(f"- {m}: {c}")
    slines.append("")
    _safe_write(OUT_DIR / "INTENT_SELECTOR.md", "\n".join(slines))

    print(f"✅ deep_read assets written to: {OUT_DIR}")
    print(f"- pages_indexed={len(pages)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

