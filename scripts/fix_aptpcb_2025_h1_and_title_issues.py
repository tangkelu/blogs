#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


BLOGS_ROOT = Path("/code/hileap/frontendAPT/public/static/blogs")
TARGET_LOCALES = ["en", "de", "it", "fr", "ru", "es", "ar"]


@dataclass(frozen=True)
class PostRef:
    year: str
    month: str
    slug: str


TITLE_SUFFIX_PATTERNS: dict[str, list[str]] = {
    "en": [
        r":\s*A Practical End-to-End Guide\b.*$",
        r":\s*A Buyer-Friendly Playbook\b.*$",
    ],
    "de": [
        r":\s*Ein praktischer End-to-End-Leitfaden\b.*$",
        r":\s*Ein Käuferfreundliches Handbuch\b.*$",
        r":\s*Ein käuferfreundliches Handbuch\b.*$",
    ],
    "it": [
        r":\s*Una guida pratica end-to-end\b.*$",
        r":\s*Un manuale per l'acquirente\b.*$",
        r":\s*Una guida amichevole per l'acquirente\b.*$",
        r":\s*Un playbook\b.*$",
    ],
    "fr": [
        r":\s*Un guide pratique\b.*$",
        r":\s*Un guide convivial pour l'acheteur\b.*$",
        r":\s*Un guide d'achat\b.*$",
        r":\s*Un playbook\b.*$",
    ],
    "es": [
        r":\s*Una guía práctica\b.*$",
        r":\s*Una guía amigable para el comprador\b.*$",
        r":\s*Una guía de compra\b.*$",
        r":\s*Un playbook\b.*$",
    ],
    "ru": [
        r":\s*Практическ(ое|ий) руководство\b.*$",
        r":\s*Покупательск(ий|ое) плейбук\b.*$",
        r":\s*Руководство для покупателя\b.*$",
    ],
    "ar": [
        r":\s*دليل عملي\b.*$",
        r":\s*دليل شامل\b.*$",
        r":\s*دليل سهل للمشتري\b.*$",
        r":\s*دليل مناسب للمشتري\b.*$",
    ],
}


ACRONYM_MAP_EN = {
    "pcb": "PCB",
    "pcba": "PCBA",
    "smt": "SMT",
    "ict": "ICT",
    "fct": "FCT",
    "aoi": "AOI",
    "spi": "SPI",
    "emi": "EMI",
    "emc": "EMC",
    "rf": "RF",
    "si/pi": "SI/PI",
    "ptfe": "PTFE",
    "cpk": "CPK",
    "iec": "IEC",
    "ul": "UL",
    "bms": "BMS",
    "cxl": "CXL",
    "pcie": "PCIe",
    "sic": "SiC",
    "gan": "GaN",
    "lidar": "LiDAR",
    "ethercat": "EtherCAT",
    "dfm": "DFM",
    "dfa": "DFA",
    "800g": "800G",
    "100g": "100G",
    "5g": "5G",
    "6g": "6G",
    "led": "LED",
    "mcpcb": "MCPCB",
}

SMALL_WORDS_EN = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "by",
    "for",
    "from",
    "in",
    "into",
    "of",
    "on",
    "or",
    "over",
    "the",
    "to",
    "vs",
    "with",
    "when",
    "what",
    "how",
}


def _yaml_single_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def _maybe_unwrap_fenced_frontmatter(text: str) -> str:
    if not text.startswith("```markdown\n---\n"):
        return text
    t = text[len("```markdown\n") :]
    t = re.sub(r"(\n---\n)\n?```\n", r"\1", t, count=1)
    return t


def _split_frontmatter(md: str) -> tuple[str, str] | None:
    if not md.startswith("---\n"):
        return None
    parts = md.split("\n---\n", 1)
    if len(parts) != 2:
        return None
    return parts[0], parts[1]


def _extract_title_from_frontmatter(fm_text: str) -> str | None:
    lines = fm_text.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^title:\s*(.*)\s*$", line)
        if not m:
            continue
        raw = m.group(1).strip()
        if raw.startswith("'") and raw.endswith("'"):
            raw = raw[1:-1].replace("''", "'")
        elif raw.startswith('"') and raw.endswith('"'):
            raw = raw[1:-1]

        if raw.startswith(">") or raw.startswith("|") or raw in {">-", "|-", ">+", "|+"}:
            cont: list[str] = []
            j = i + 1
            while j < len(lines) and (lines[j].startswith("  ") or lines[j].startswith("\t")):
                cont.append(lines[j].strip())
                j += 1
            return re.sub(r"\s+", " ", " ".join(cont)).strip() if cont else ""

        return raw
    return None


def _update_title_in_frontmatter(fm_text: str, *, title: str) -> str:
    lines = fm_text.splitlines()
    out: list[str] = []
    replaced = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^title:\s*", line) and not replaced:
            out.append(f"title: {_yaml_single_quote(title)}")
            replaced = True
            i += 1
            while i < len(lines) and (lines[i].startswith("  ") or lines[i].startswith("\t")):
                i += 1
            continue
        out.append(line)
        i += 1
    if not replaced:
        out.insert(1, f"title: {_yaml_single_quote(title)}")
    return "\n".join(out) + "\n"


def _clean_title(title: str, locale: str) -> str:
    t = title.strip()
    for pat in TITLE_SUFFIX_PATTERNS.get(locale, []):
        t = re.sub(pat, "", t, flags=re.I).strip()
    t = re.sub(r"\s+", " ", t).strip()
    return t


def _title_case_en(text: str) -> str:
    def title_word(word: str, *, is_first: bool, force_cap: bool) -> str:
        lower = word.lower()
        if lower in ACRONYM_MAP_EN:
            return ACRONYM_MAP_EN[lower]
        if not is_first and not force_cap and lower in SMALL_WORDS_EN:
            return lower
        if any(ch.isdigit() for ch in word):
            mapped = ACRONYM_MAP_EN.get(lower)
            return mapped if mapped else word
        return word[:1].upper() + word[1:].lower() if word else word

    tokens = re.split(r"(\s+)", text)
    out: list[str] = []
    seen_word = False
    force_cap_next = False
    for tok in tokens:
        if tok.isspace() or tok == "":
            out.append(tok)
            continue
        parts = tok.split("-")
        new_parts: list[str] = []
        for part in parts:
            m = re.match(r"^([(\"'“”‘’\\[]*)(.*?)([)\"'“”‘’\\],.;:!?]*)$", part)
            if not m:
                pre = ""
                core = part
                suf = ""
            else:
                pre, core, suf = m.groups()
            core_cased = title_word(core, is_first=not seen_word, force_cap=force_cap_next)
            if core:
                seen_word = True
            force_cap_next = ":" in suf
            new_parts.append(f"{pre}{core_cased}{suf}")
        out.append("-".join(new_parts))
    return "".join(out).strip()


def _ensure_single_h1_at_top(body: str, title: str) -> str:
    stripped = body.lstrip("\n")
    lines = stripped.splitlines()
    desired = f"# {title}"

    def is_h1(line: str) -> bool:
        return bool(re.match(r"^#\s+[^#]", line))

    def is_h2_or_more(line: str) -> bool:
        return bool(re.match(r"^##\s+", line))

    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    if i < len(lines) and is_h1(lines[i]):
        lines[i] = desired
        start_idx = i + 1
    else:
        lines = [desired, ""] + lines
        start_idx = 2

    out: list[str] = []
    removed_extra_h1 = False
    for idx, line in enumerate(lines):
        if idx >= start_idx and not removed_extra_h1 and is_h2_or_more(line):
            out.extend(lines[idx:])
            break
        if idx >= start_idx and is_h1(line) and not removed_extra_h1:
            removed_extra_h1 = True
            continue
        out.append(line)

    return "\n".join(out).lstrip("\n") + ("\n" if body.endswith("\n") else "")


def _needs_fix(en_path: Path) -> bool:
    raw = en_path.read_text(encoding="utf-8", errors="ignore")
    parts = raw.split("\n---\n", 1) if raw.startswith("---\n") else None
    if not parts or len(parts) != 2:
        return False
    body = parts[1]
    h1s = 0
    for line in body.splitlines()[:80]:
        if re.match(r"^##\s+", line):
            break
        if re.match(r"^#\s+[^#]", line):
            h1s += 1
    if h1s > 1:
        return True
    return bool(re.search(r"^title:\s*'?>-\s*$", parts[0], flags=re.M))


def _find_posts_to_fix() -> list[PostRef]:
    year_dir = BLOGS_ROOT / "2025"
    posts: list[PostRef] = []
    for month_dir in sorted(year_dir.iterdir()):
        if not month_dir.is_dir():
            continue
        month = month_dir.name
        en_dir = month_dir / "en"
        if not en_dir.exists():
            continue
        for md in sorted(en_dir.glob("*.md")):
            if _needs_fix(md):
                posts.append(PostRef("2025", month, md.stem))
    return posts


def main() -> int:
    posts = _find_posts_to_fix()
    print(f"posts_to_fix={len(posts)}")
    if not posts:
        return 0

    updated = 0
    missing = 0
    skipped = 0
    unwrapped = 0

    for post in posts:
        for locale in TARGET_LOCALES:
            md_path = BLOGS_ROOT / post.year / post.month / locale / f"{post.slug}.md"
            if not md_path.exists():
                print(f"missing: {md_path}")
                missing += 1
                continue

            raw0 = md_path.read_text(encoding="utf-8", errors="ignore")
            raw = _maybe_unwrap_fenced_frontmatter(raw0)
            if raw != raw0:
                unwrapped += 1

            parts = _split_frontmatter(raw)
            if not parts:
                print(f"skip(no-frontmatter): {md_path}")
                skipped += 1
                continue
            fm_without_end, body = parts

            old_title = _extract_title_from_frontmatter(fm_without_end)
            if old_title is None:
                print(f"skip(no-title): {md_path}")
                skipped += 1
                continue

            new_title = _clean_title(old_title, locale)
            if locale == "en":
                new_title = _title_case_en(new_title)
            elif locale in {"de", "it", "fr", "es"} and new_title[:1].islower():
                new_title = new_title[:1].upper() + new_title[1:]

            fm_updated = _update_title_in_frontmatter(fm_without_end, title=new_title)
            body_updated = _ensure_single_h1_at_top(body, new_title)
            new_text = fm_updated + "---\n" + body_updated.lstrip("\n")

            if new_text != raw0:
                md_path.write_text(new_text, encoding="utf-8")
                updated += 1

    print(f"updated_files={updated} missing_files={missing} skipped_files={skipped} unwrapped={unwrapped}")
    return 0 if missing == 0 and skipped == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())

