#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


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
    level: int  # 2 or 3
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
    if "troubleshoot" in t or "failure" in t or "defect" in t or "root cause" in t:
        return "Troubleshooting / failure modes"
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


def _read_index_rows() -> dict[str, dict[str, str | list[str]]]:
    """
    md_path -> {site, url, keywords[]}
    """
    by_md: dict[str, dict[str, str | list[str]]] = {}
    with CSV_PATH.open(newline="", encoding="utf-8", errors="ignore") as f:
        r = csv.DictReader(f)
        for row in r:
            md = (row.get("MdPath") or "").strip()
            if not md:
                continue
            d = by_md.setdefault(
                md,
                {
                    "site": (row.get("Site") or "").strip(),
                    "url": (row.get("URL_norm") or row.get("URL") or "").strip(),
                    "keywords": [],
                },
            )
            kw = (row.get("Keyword") or "").strip()
            if kw and isinstance(d["keywords"], list) and len(d["keywords"]) < 12:
                d["keywords"].append(kw)
    return by_md


def _heading_stem(h: str, n_words: int = 4) -> str:
    toks = re.split(r"\s+", h.strip())
    return " ".join(toks[:n_words]).lower()


def _classify_question_modifier(q: str) -> str:
    t = q.lower()
    if "cost" in t or "price" in t:
        return "cost"
    if "lead time" in t or "turnaround" in t:
        return "lead_time"
    if "material" in t:
        return "materials"
    if "test" in t or "inspection" in t:
        return "testing"
    if "dfm" in t or "files" in t or "gerber" in t or "odb" in t or "ipc-2581" in t:
        return "dfm_files"
    if "accept" in t or "criteria" in t or "pass" in t:
        return "acceptance"
    if "difference" in t or "vs" in t or "versus" in t:
        return "comparison"
    return "other"


def _extract_faq_questions(body: str, headings: list[Heading]) -> list[str]:
    """
    Extract FAQ questions under an H2 that looks like FAQ.
    Prefer H3 questions (### ...?) and short lines ending with '?'.
    """
    lines = body.splitlines()
    # Find FAQ H2 ranges.
    faq_ranges: list[tuple[int, int]] = []
    h2_positions = [(h.line_idx, h.text) for h in headings if h.level == 2]
    for idx, (start, h2_text) in enumerate(h2_positions):
        if _canonicalize_section(h2_text) != "FAQ":
            continue
        end = h2_positions[idx + 1][0] if idx + 1 < len(h2_positions) else len(lines)
        faq_ranges.append((start, end))
    if not faq_ranges:
        return []

    qs: list[str] = []
    for start, end in faq_ranges:
        # H3 headings inside FAQ
        for h in headings:
            if h.level == 3 and start < h.line_idx < end:
                if h.text.endswith("?") and len(h.text) <= 140:
                    qs.append(h.text)

        # Lines ending with '?'
        for line in lines[start:end]:
            s = _strip_md_formatting(line.strip())
            if not s:
                continue
            if len(s) > 160:
                continue
            if s.endswith("?"):
                # Avoid capturing table separators or random punctuation.
                if re.match(r"^\|", line.strip()):
                    continue
                # Avoid duplicates of H3 questions.
                qs.append(s)
    # De-dup while preserving order
    out: list[str] = []
    seen: set[str] = set()
    for q in qs:
        q2 = re.sub(r"\s+", " ", q).strip()
        if not q2 or q2 in seen:
            continue
        seen.add(q2)
        out.append(q2)
    return out


def _extract_first_sentence_after_h2(body: str, h2_line_idx: int) -> str | None:
    lines = body.splitlines()
    i = h2_line_idx + 1
    # Skip blank lines and non-paragraph items.
    while i < len(lines):
        s = lines[i].strip()
        if not s:
            i += 1
            continue
        if s.startswith("<!--") and s.endswith("-->"):
            i += 1
            continue
        if re.match(r"^#{1,6}\s+", s):
            return None
        if s.startswith("![" ) and "](" in s:
            i += 1
            continue
        if s.startswith("|"):
            # table starts; no paragraph
            return None
        # start paragraph
        para: list[str] = []
        while i < len(lines):
            s2 = lines[i].strip()
            if not s2:
                break
            if re.match(r"^#{1,6}\s+", s2):
                break
            if s2.startswith("|"):
                break
            if s2.startswith("![" ) and "](" in s2:
                break
            para.append(s2)
            i += 1
        sent = _sentences(" ".join(para))
        return sent[0] if sent else None
    return None


def _bridge_bucket(sentence: str) -> str:
    s = sentence.lower()
    if re.search(r"\bnow that\b|\bwith that\b|\bwith the basics\b|\bwith (this|these) (in mind|defined)\b", s):
        return "bridge_now_that"
    if re.search(r"\bnext\b|\bthe next step\b|\bfrom here\b", s):
        return "bridge_next"
    if re.search(r"\bto (avoid|prevent)\b|\bcommon\b|\bp(itfall|itfalls)\b", s):
        return "bridge_avoid_failures"
    if re.search(r"\bin this section\b|\bhere we\b|\blet's\b", s):
        return "bridge_expository"
    return "bridge_none"


def main() -> int:
    ap = argparse.ArgumentParser(description="Deep-read phrase bank extraction from ranking-referenced blog markdown.")
    ap.add_argument("--limit", type=int, default=0, help="Limit pages for quick iteration (0 = no limit)")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    index = _read_index_rows()
    md_paths = [Path(p) for p in index.keys() if Path(p).exists()]
    md_paths.sort()
    if args.limit and args.limit > 0:
        md_paths = md_paths[: args.limit]

    # Aggregations
    h2_stems: dict[str, Counter[str]] = defaultdict(Counter)
    h3_stems: dict[str, Counter[str]] = defaultdict(Counter)
    section_label_counts: dict[str, Counter[str]] = defaultdict(Counter)
    faq_questions_by_intent: dict[str, Counter[str]] = defaultdict(Counter)
    faq_mods_by_intent: dict[str, Counter[str]] = defaultdict(Counter)
    bridge_buckets_by_intent: dict[str, Counter[str]] = defaultdict(Counter)
    opening_patterns: dict[str, Counter[str]] = defaultdict(Counter)

    processed = 0
    for md_path in md_paths:
        meta = index.get(str(md_path), {})
        url = str(meta.get("url") or "")
        kws = meta.get("keywords") if isinstance(meta.get("keywords"), list) else []

        raw = md_path.read_text(encoding="utf-8", errors="ignore")
        parts = _split_frontmatter(raw)
        if not parts:
            continue
        _fm, body = parts
        h1 = _extract_h1(body)

        headings = _extract_headings_with_positions(body)
        h2_list = [h.text for h in headings if h.level == 2]
        intent = _infer_page_intent(url, list(kws), h1, h2_list)

        # Opening paragraph pattern buckets (not copying sentences)
        opening_para = ""
        # Find first paragraph after H1
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
            para.append(s)
            i += 1
        opening_para = _strip_md_formatting(" ".join(para))
        first_sent = _sentences(opening_para)[:1]
        if first_sent:
            s = first_sent[0].lower()
            if re.search(r"\bis\b|\bare\b|\bmeans\b|\brefers to\b", s):
                opening_patterns[intent]["definition_like"] += 1
            if re.search(r"\bhelps\b|\bmatters\b|\bused\b|\bimportant\b", s):
                opening_patterns[intent]["why_like"] += 1
            if re.search(r"\bshows\b|\bexplains\b|\bprovides\b|\bguide\b", s):
                opening_patterns[intent]["promise_like"] += 1
            opening_patterns[intent]["has_opening"] += 1

        # Heading stems and section labels
        for h in headings:
            if h.level == 2:
                section_label_counts[intent][_canonicalize_section(h.text)] += 1
                h2_stems[intent][_heading_stem(h.text, n_words=4)] += 1
                # Bridge sentence bucket for H2
                sent = _extract_first_sentence_after_h2(body, h.line_idx)
                if sent:
                    bridge_buckets_by_intent[intent][_bridge_bucket(sent)] += 1
            elif h.level == 3:
                h3_stems[intent][_heading_stem(h.text, n_words=4)] += 1

        # FAQ questions
        qs = _extract_faq_questions(body, headings)
        for q in qs:
            faq_questions_by_intent[intent][q] += 1
            faq_mods_by_intent[intent][_classify_question_modifier(q)] += 1

        processed += 1

    # Write derived assets
    # 1) HEADING_PATTERNS.md
    lines: list[str] = []
    lines.append("# Deep Read: Heading Stem Patterns (rewrite-safe)")
    lines.append("")
    lines.append("These are **stem patterns** (first ~4 words) from H2/H3 headings, grouped by inferred intent.")
    lines.append("They are not full headings and are intended for prompt building without copying competitor phrasing.")
    lines.append("")
    for intent in INTENT_ORDER:
        counter = h2_stems.get(intent, Counter())
        if not counter:
            continue
        lines.append(f"## {intent}")
        lines.append("Top H2 stems:")
        for stem, c in counter.most_common(25):
            lines.append(f"- {c}×: `{stem} …`")
        counter3 = h3_stems.get(intent, Counter())
        if counter3:
            lines.append("")
            lines.append("Top H3 stems:")
            for stem, c in counter3.most_common(15):
                lines.append(f"- {c}×: `{stem} …`")
        lines.append("")
    (OUT_DIR / "HEADING_PATTERNS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # 2) FAQ_BANKS.md (pattern guidance + top modifiers distribution)
    flines: list[str] = []
    flines.append("# Deep Read: FAQ Banks (modifiers + question forms)")
    flines.append("")
    flines.append("This summarizes FAQ behavior observed in the ranking-referenced corpus.")
    flines.append("Use it to generate *your own* FAQs (do not copy exact competitor questions).")
    flines.append("")
    for intent in INTENT_ORDER:
        mod = faq_mods_by_intent.get(intent, Counter())
        if not mod:
            continue
        total = sum(mod.values())
        flines.append(f"## {intent} (faq_questions={total})")
        for k, c in mod.most_common():
            flines.append(f"- {k}: {c} ({(c/max(1,total))*100:.1f}%)")
        flines.append("")
        # Provide generic question forms based on observed modifiers.
        flines.append("Recommended long-tail FAQ forms:")
        flines.append("- `{{keyword}} cost`: What drives cost, and which choices change it most?")
        flines.append("- `{{keyword}} lead time`: What affects turnaround, and what to submit early?")
        flines.append("- `{{keyword}} materials`: Which materials/options fit which constraints?")
        flines.append("- `{{keyword}} testing`: Which test methods + pass criteria matter?")
        flines.append("- `{{keyword}} acceptance criteria`: What does “pass” mean in practice?")
        flines.append("- `{{keyword}} DFM files`: What files are required for an accurate quote/DFM review?")
        flines.append("")
    (OUT_DIR / "FAQ_BANKS.md").write_text("\n".join(flines) + "\n", encoding="utf-8")

    # 3) BRIDGING_PATTERNS.md (how often sections begin with a bridge-like sentence)
    blines: list[str] = []
    blines.append("# Deep Read: Bridging Sentence Buckets (first sentence under H2)")
    blines.append("")
    blines.append("We bucket the first sentence after each H2 into coarse categories to support the “bridge sentence” rule.")
    blines.append("")
    for intent in INTENT_ORDER:
        counter = bridge_buckets_by_intent.get(intent, Counter())
        if not counter:
            continue
        total = sum(counter.values())
        blines.append(f"## {intent} (h2_with_sentence={total})")
        for k, c in counter.most_common():
            blines.append(f"- {k}: {c} ({(c/max(1,total))*100:.1f}%)")
        blines.append("")
        blines.append("Suggested bridge sentence patterns (use rewrite-safe variants):")
        blines.append("- Now that the basics are clear, the next step is …")
        blines.append("- With the key constraints defined, let’s look at …")
        blines.append("- To avoid common failures, focus on …")
        blines.append("")
    (OUT_DIR / "BRIDGING_PATTERNS.md").write_text("\n".join(blines) + "\n", encoding="utf-8")

    # 4) OPENING_PATTERNS.md
    olines: list[str] = []
    olines.append("# Deep Read: Opening Sentence Signal Buckets (first paragraph under H1)")
    olines.append("")
    for intent in INTENT_ORDER:
        counter = opening_patterns.get(intent, Counter())
        if not counter:
            continue
        total = counter.get("has_opening", 0)
        if total == 0:
            continue
        olines.append(f"## {intent} (pages={total})")
        for k in ["definition_like", "why_like", "promise_like"]:
            c = counter.get(k, 0)
            olines.append(f"- {k}: {c} ({(c/max(1,total))*100:.1f}%)")
        olines.append("")
    (OUT_DIR / "OPENING_PATTERNS.md").write_text("\n".join(olines) + "\n", encoding="utf-8")

    print(f"✅ phrase-bank assets written to: {OUT_DIR}")
    print(f"- pages_processed={processed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

