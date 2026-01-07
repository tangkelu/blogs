#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


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


def _extract_h1(body: str) -> str | None:
    for line in body.splitlines():
        s = line.strip()
        if not s:
            continue
        m = re.match(r"^#\s+(.+)$", s)
        return _strip_md_formatting(m.group(1)) if m else None
    return None


def _extract_faq_questions(body: str, headings: list[Heading]) -> list[str]:
    lines = body.splitlines()
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
        for h in headings:
            if h.level == 3 and start < h.line_idx < end:
                if h.text.endswith("?") and len(h.text) <= 140:
                    qs.append(h.text)
        for line in lines[start:end]:
            s = _strip_md_formatting(line.strip())
            if not s or len(s) > 160:
                continue
            if s.endswith("?") and not line.strip().startswith("|"):
                qs.append(s)
    out: list[str] = []
    seen: set[str] = set()
    for q in qs:
        q2 = re.sub(r"\s+", " ", q).strip()
        if not q2 or q2 in seen:
            continue
        seen.add(q2)
        out.append(q2)
    return out


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


def _extract_first_sentence_after_h2(body: str, h2_line_idx: int) -> str | None:
    lines = body.splitlines()
    i = h2_line_idx + 1
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
        if s.startswith("|") or s.startswith("![" ):
            return None
        para: list[str] = []
        while i < len(lines):
            s2 = lines[i].strip()
            if not s2:
                break
            if re.match(r"^#{1,6}\s+", s2) or s2.startswith("|") or s2.startswith("![" ):
                break
            para.append(s2)
            i += 1
        sent = _sentences(" ".join(para))
        return sent[0] if sent else None
    return None


def _bridge_bucket(sentence: str) -> str:
    s = sentence.lower()
    if re.search(r"\bnow that\b|\bwith that\b|\bwith the basics\b", s):
        return "bridge_now_that"
    if re.search(r"\bnext\b|\bthe next step\b|\bfrom here\b", s):
        return "bridge_next"
    if re.search(r"\bto (avoid|prevent)\b|\bcommon\b|\bp(itfall|itfalls)\b", s):
        return "bridge_avoid_failures"
    if re.search(r"\bin this section\b|\bhere we\b|\blet's\b", s):
        return "bridge_expository"
    return "bridge_none"


def _load_top3_pages() -> dict[str, dict[str, object]]:
    by_md: dict[str, dict[str, object]] = {}
    minpos: dict[str, float] = defaultdict(lambda: 1e9)
    with CSV_PATH.open(newline="", encoding="utf-8", errors="ignore") as f:
        r = csv.DictReader(f)
        for row in r:
            md = (row.get("MdPath") or "").strip()
            if not md:
                continue
            try:
                pos = float(row.get("Position") or "")
            except Exception:
                continue
            if pos < minpos[md]:
                minpos[md] = pos
            d = by_md.setdefault(
                md,
                {
                    "site": (row.get("Site") or "").strip(),
                    "url": (row.get("URL_norm") or row.get("URL") or "").strip(),
                    "keywords": [],
                },
            )
            kw = (row.get("Keyword") or "").strip()
            if kw and len(d["keywords"]) < 8:
                d["keywords"].append(kw)

    out: dict[str, dict[str, object]] = {}
    for md, d in by_md.items():
        if minpos[md] <= 3 and Path(md).exists():
            out[md] = d
    return out


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    pages = _load_top3_pages()

    faq_mods_by_intent: dict[str, Counter[str]] = defaultdict(Counter)
    bridge_buckets_by_intent: dict[str, Counter[str]] = defaultdict(Counter)

    processed = 0
    for md_str, meta in pages.items():
        md_path = Path(md_str)
        raw = md_path.read_text(encoding="utf-8", errors="ignore")
        parts = _split_frontmatter(raw)
        if not parts:
            continue
        _fm, body = parts
        headings = _extract_headings_with_positions(body)
        h1 = _extract_h1(body)
        h2_list = [h.text for h in headings if h.level == 2 and not STOP_H2_RE.match(h.text)]
        intent = _infer_page_intent(str(meta.get("url") or ""), list(meta.get("keywords") or []), h1, h2_list)

        # FAQ modifiers
        qs = _extract_faq_questions(body, headings)
        for q in qs:
            faq_mods_by_intent[intent][_classify_question_modifier(q)] += 1

        # Bridge buckets (first sentence under each non-boilerplate H2)
        for h in headings:
            if h.level != 2:
                continue
            if STOP_H2_RE.match(h.text):
                continue
            sent = _extract_first_sentence_after_h2(body, h.line_idx)
            if sent:
                bridge_buckets_by_intent[intent][_bridge_bucket(sent)] += 1

        processed += 1

    # FAQ_BANKS.md
    flines: list[str] = []
    flines.append("# Deep Read v2: FAQ modifier distribution (Top3 only)")
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
    (OUT_DIR / "FAQ_BANKS.md").write_text("\n".join(flines) + "\n", encoding="utf-8")

    # BRIDGING_PATTERNS.md
    blines: list[str] = []
    blines.append("# Deep Read v2: Bridging sentence buckets (Top3 only, non-boilerplate H2)")
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
    (OUT_DIR / "BRIDGING_PATTERNS.md").write_text("\n".join(blines) + "\n", encoding="utf-8")

    print(f"✅ deep_read_v2 phrase banks written to: {OUT_DIR}")
    print(f"- pages_processed={processed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

