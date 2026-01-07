#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


TARGET_DIRS = [
    Path("blogs_aptpcb/1223/en"),
    Path("blogs_aptpcb/1223-bak/en"),
]


@dataclass(frozen=True)
class DocContext:
    keyword: str
    kind: str  # playbook | query | pillar | unknown


CODE_FENCE_RE = re.compile(r"^\s*```")


def _parse_keyword(text: str, fallback_slug: str) -> str:
    m = re.search(r'^tags:\s*\[(.*?)\]\s*$', text, re.M)
    if m:
        inside = m.group(1)
        q = re.search(r'"([^"]+)"', inside)
        if q:
            return q.group(1).strip()
        q = re.search(r"'([^']+)'", inside)
        if q:
            return q.group(1).strip()

    m = re.search(r'^title:\s*"(.*?)"\s*$', text, re.M)
    if m:
        title = m.group(1).strip()
        if ":" in title:
            return title.split(":", 1)[0].strip()
        return title

    return fallback_slug.replace("-", " ").strip()


def _detect_kind(text: str) -> str:
    if "A Buyer-Friendly Playbook" in text:
        return "playbook"
    if re.search(r"^##\s+Quick Answer\b", text, re.M):
        return "query"
    if re.search(r"^##\s+Key Takeaways\b", text, re.M):
        return "pillar"
    return "unknown"


def _contains_kw(heading: str, kw: str) -> bool:
    return kw.lower() in heading.lower()


def _faq_longtail(ctx: DocContext, text_lc: str) -> str:
    def has(pattern: str) -> bool:
        return re.search(pattern, text_lc) is not None

    terms: list[str] = ["cost", "lead time"]
    if ctx.kind == "query":
        terms += ["common defects", "acceptance criteria"]
    terms += ["DFM files"]

    extras: list[str] = []
    if "stackup" in text_lc:
        extras.append("stackup")
    if "impedance" in text_lc:
        extras.append("impedance")
    if has(r"\bdk\b") or "d_k" in text_lc or "dk/d" in text_lc:
        extras.append("Dk/Df")
    if any(k in text_lc for k in ["vna", "s-parameter", "s21", "s11"]):
        extras.append("S-parameters")
    if any(k in text_lc for k in ["pim", "passive intermod"]):
        extras.append("PIM")
    if "aoi" in text_lc:
        extras.append("AOI inspection")
    if "x-ray" in text_lc or "xray" in text_lc:
        extras.append("X-ray inspection")
    if "ipc" in text_lc:
        extras.append("IPC class")
    if "rework" in text_lc:
        extras.append("rework limits")
    if any(k in text_lc for k in ["enig", "enepig", "immersion silver", "surface finish"]):
        extras.append("surface finish")
    if any(k in text_lc for k in ["thermal cycling", "thermal shock", "ist", "thb"]):
        extras.append("reliability tests")
    if ctx.kind != "query":
        extras.append("materials")
        extras.append("testing")

    seen: set[str] = set()
    merged: list[str] = []
    for item in terms + extras:
        if item.lower() in seen:
            continue
        seen.add(item.lower())
        merged.append(item)

    return ", ".join(merged[:6])


def _rewrite_h2(title: str, ctx: DocContext, text_lc: str) -> str:
    kw = ctx.keyword
    t = title.strip()

    # Common (all kinds)
    if t == "FAQ" or re.search(r"\bFAQ\s*\(", t):
        return f"{kw} FAQ ({_faq_longtail(ctx, text_lc)})"
    if t in {"Related pages & tools", "Related resources and tools"}:
        return f"Resources for {kw} (related pages and tools)"
    if t.startswith("Request a quote"):
        return f"Request a quote for {kw} (DFM review + pricing)"
    if t == "Request a quote":
        return f"Request a quote for {kw} (DFM review + pricing)"
    if t.startswith("Conclusion"):
        return f"Conclusion: {kw} next steps"
    if t == "Conclusion":
        return f"Conclusion: {kw} next steps"

    # Playbook-specific
    if ctx.kind == "playbook":
        if re.search(r"what this playbook covers", t, re.I):
            return f"{kw}: definition, scope, and who this guide is for"
        if re.search(r"^When .* is the right approach", t, re.I):
            return f"When to use {kw} (and when a standard approach is better)"
        if t == "Requirements you must define before quoting":
            return f"{kw} specifications (materials, stackup, tolerances)"
        if t == "Key specifications and requirements to define upfront":
            return f"{kw} specifications (materials, stackup, tolerances)"
        if t in {"The hidden risks that break scale-up", "Scale-up risks that cause field failures (and how to prevent them)"}:
            return f"{kw} manufacturing risks (root causes and prevention)"
        if t.startswith("Validation plan") or t.startswith("Validation and acceptance plan") or t.startswith("Validation and qualification plan"):
            return f"{kw} validation and acceptance (tests and pass criteria)"
        if t in {"Supplier checklist (RFQ + audit questions)", "Supplier qualification checklist (RFQ and audit questions)"}:
            return f"{kw} supplier qualification checklist (RFQ, audit, traceability)"
        if t.startswith("Decision guidance"):
            return f"How to choose {kw} (trade-offs and decision rules)"
        if re.search(r"^When to use\b", t, re.I):
            # keep, but ensure keyword is present
            if _contains_kw(t, kw):
                return t
            return f"When to use {kw} (and when a standard approach is better)"
        if re.search(r"definition, scope", t, re.I):
            # normalize first H2 if keyword prefix is wrong
            if t.lower().startswith(kw.lower()):
                return t
            if ":" in t:
                return f"{kw}: definition, scope, and who this guide is for"
            return f"{kw}: definition, scope, and who this guide is for"

        if not _contains_kw(t, kw):
            return f"{kw}: {t}"
        return t

    # Query-specific
    if ctx.kind == "query":
        if t == "Quick Answer (30 seconds)":
            return f"{kw} quick answer (30 seconds)"
        if re.search(r"^When .* applies \(and when it doesn", t, re.I):
            return f"When {kw} applies (and when it doesn’t)"
        if t == "Rules & specifications":
            return f"{kw} rules and specifications (key parameters and limits)"
        if t == "Implementation steps":
            return f"{kw} implementation steps (process checkpoints)"
        if t == "Failure modes & troubleshooting":
            return f"{kw} troubleshooting (failure modes and fixes)"
        if t == "Design decisions":
            return f"How to choose {kw} (design decisions and trade-offs)"
        if t.startswith("Design decisions:"):
            rest = t.split(":", 1)[1].strip()
            return f"How to choose {kw} ({rest})"
        if t == "Glossary (key terms)":
            return f"{kw} glossary (key terms)"
        if t == "Related pages & tools":
            return f"Resources for {kw} (related pages and tools)"
        if not _contains_kw(t, kw):
            return f"{kw}: {t}"
        return t

    # Pillar-specific
    if ctx.kind == "pillar":
        if t == "Key Takeaways":
            return f"Key takeaways for {kw}"
        if t == "Metrics that matter (how to evaluate quality)":
            return f"{kw} metrics that matter (how to evaluate quality)"
        if t.startswith("Selection guidance by scenario"):
            return f"How to choose {kw}: selection guidance by scenario (trade-offs)"
        if t == "How to choose: Selection guidance by scenario":
            return f"How to choose {kw}: selection guidance by scenario"
        if t == "From design to manufacturing (implementation checkpoints)":
            return f"{kw} implementation checkpoints (design to manufacturing)"
        if t == "Common mistakes (and the correct approach)":
            return f"{kw} common mistakes (and the correct approach)"
        if t == "Glossary (key terms)":
            return f"{kw} glossary (key terms)"
        if t == "Related pages & tools":
            return f"Resources for {kw} (related pages and tools)"
        if t == "Conclusion (next steps)":
            return f"Conclusion: {kw} next steps"
        if not _contains_kw(t, kw) and not t.startswith("What "):
            return f"{kw}: {t}"
        return t

    # Unknown: keep minimal, but enforce FAQ longtail and keyword prefix on generic headings.
    if t in {"Quick Answer (30 seconds)", "Key Takeaways"}:
        return f"{kw}: {t}"
    if not _contains_kw(t, kw) and t in {"Rules & specifications", "Implementation steps", "Failure modes & troubleshooting", "Design decisions"}:
        return f"{kw}: {t}"
    return t


def _rewrite_h3(title: str, ctx: DocContext, current_h2: str | None) -> str:
    kw = ctx.keyword
    t = title.strip()

    # Supplier checklist group headings (playbook)
    if ctx.kind == "playbook" and current_h2 and "supplier qualification checklist" in current_h2.lower():
        # Normalize common group labels, adding keyword once for clarity.
        m = re.match(r"^(Group\s+\d+:\s*)?(RFQ\s+Inputs?)\s*\((.*?)\)\s*$", t, re.I)
        if m:
            prefix = m.group(1) or ""
            return f"{prefix}RFQ inputs for {kw} ({m.group(3)})"
        m = re.match(r"^(Group\s+\d+:\s*)?(Capability\s+Proof|Capability\s+evidence)\s*\((.*?)\)\s*$", t, re.I)
        if m:
            prefix = m.group(1) or ""
            return f"{prefix}Capability evidence for {kw} ({m.group(3)})"
        if t.lower().startswith("quality system"):
            return f"Quality system and traceability for {kw}"
        if t.lower().startswith("change control"):
            return f"Change control and delivery for {kw}"
        if t.lower().startswith("rfq inputs"):
            return f"RFQ inputs for {kw} (what you provide)"
        if t.lower().startswith("capability proof"):
            return f"Capability evidence for {kw} (what the supplier must prove)"

    # Query: "When it applies" subheads
    if ctx.kind == "query" and current_h2 and current_h2.lower().startswith("when "):
        if t.lower() in {"when it applies", "when this standard applies"}:
            return f"When {kw} applies"
        if t.lower() in {"when it doesn’t apply", "when this standard doesn’t apply"}:
            return f"When {kw} does not apply"

    # Query: failure mode numbered headings -> add keyword in parentheses once
    if ctx.kind == "query" and current_h2 and "troubleshooting" in current_h2.lower():
        if re.match(r"^\\d+\\.", t) and kw.lower() not in t.lower():
            return f"{t} ({kw})"

    return t


def update_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    slug_kw = path.stem
    keyword = _parse_keyword(text, slug_kw)
    kind = _detect_kind(text)
    ctx = DocContext(keyword=keyword, kind=kind)
    text_lc = text.lower()

    has_trailing_newline = text.endswith("\n")
    lines = text.splitlines()
    out: list[str] = []
    changed = False

    in_code_fence = False
    current_h2: str | None = None

    for line in lines:
        if CODE_FENCE_RE.match(line):
            in_code_fence = not in_code_fence
            out.append(line)
            continue

        if in_code_fence:
            out.append(line)
            continue

        m2 = re.match(r"^##(?!#)\s+(.*)$", line)
        if m2:
            title = m2.group(1)
            rewritten = _rewrite_h2(title, ctx, text_lc)
            current_h2 = rewritten
            new_line = f"## {rewritten}"
            if new_line != line:
                changed = True
                out.append(new_line)
            else:
                out.append(line)
            continue

        m3 = re.match(r"^###(?!#)\s+(.*)$", line)
        if m3:
            title = m3.group(1)
            rewritten = _rewrite_h3(title, ctx, current_h2)
            new_line = f"### {rewritten}"
            if new_line != line:
                changed = True
                out.append(new_line)
            else:
                out.append(line)
            continue

        out.append(line)

    if changed:
        new_text = "\n".join(out) + ("\n" if has_trailing_newline else "")
        path.write_text(new_text, encoding="utf-8")
    return changed


def main() -> None:
    changed_files: list[Path] = []
    for d in TARGET_DIRS:
        if not d.exists():
            continue
        for path in sorted(d.glob("*.md")):
            if update_file(path):
                changed_files.append(path)

    print(f"Updated {len(changed_files)} files.")
    for p in changed_files:
        print(f"- {p}")


if __name__ == "__main__":
    main()
