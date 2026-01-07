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


POSTS: list[PostRef] = [
    PostRef("2025", "03", "data-center-ultrasound-probe-interface-pcb-2"),
    PostRef("2025", "10", "encoder-interface-board-checklist"),
    PostRef("2025", "07", "automotive-grade-mppt-controller-board"),
    PostRef("2025", "02", "ultra-clean-packaging-for-quantum"),
    PostRef("2025", "01", "automotive-ethernet-prototype"),
    PostRef("2025", "10", "handling-and-breakage-prevention"),
    PostRef("2025", "09", "audio-equipment-safety-compliance-pcb"),
    PostRef("2025", "07", "beauty-device-emi-compliance-pcb"),
    PostRef("2025", "06", "data-center-ai-server-motherboard-pcb"),
    PostRef("2025", "02", "mineral-cartridge-controller-pcb"),
    PostRef("2025", "12", "process-capability-cpk-for-fabrication-what-to-track"),
    PostRef("2025", "11", "spi-vs-aoi-when-to-run-each-in-pcba"),
    PostRef("2025", "10", "iec-60601-and-electrical-safety"),
    PostRef("2025", "10", "coax-launch-calibration-fixture"),
    PostRef("2025", "09", "low-magnetic-connector-assembly"),
    PostRef("2025", "06", "hermetic-sealing-interfaces-pcb"),
    PostRef("2025", "01", "mri-compatible-pcb-materials-testing"),
    PostRef("2025", "11", "dual-sim-emergency-communicator-pcb"),
    PostRef("2025", "05", "servo-motor-driver-pcb-testing"),
    PostRef("2025", "11", "home-robot-slam-processor-pcb"),
    PostRef("2025", "09", "ble-medical-gateway-pcb-compliance"),
    PostRef("2025", "07", "wearable-patch-pcb-validation"),
    PostRef("2025", "05", "visitor-location-register"),
    PostRef("2025", "03", "rigid-flex-bend-area-keepout-rules"),
    PostRef("2025", "01", "reliability-dashboard-metrics"),
    PostRef("2025", "11", "rogers-ptfe-hybrid-stackup-layout"),
    PostRef("2025", "11", "plc-communication-module-pcb"),
    PostRef("2025", "09", "soldermask-exposure-tutorial"),
    PostRef("2025", "09", "dimensional-inspection-guide"),
    PostRef("2025", "08", "rf-connector-launch-assembly"),
    PostRef("2025", "05", "pcie-gen6-backplane-pcb-prototype"),
    PostRef("2025", "01", "factory-ict-coverage-for-plc"),
    PostRef("2025", "12", "on-board-charger-pcb-design"),
    PostRef("2025", "09", "cxl-3-0-interface-pcb-validation"),
    PostRef("2025", "08", "die-attach-on-ceramic-substrates"),
    PostRef("2025", "04", "connector-selection-for-fpc"),
    PostRef("2025", "03", "ultrasonic-welding-interface-pcb"),
    PostRef("2025", "03", "low-thermal-conductivity-stackup"),
    PostRef("2025", "03", "cleaning-and-surface-preparation"),
    PostRef("2025", "02", "gan-power-stage-pcb-quality"),
]


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


def _split_frontmatter(md: str) -> tuple[str, str] | None:
    if not md.startswith("---\n"):
        return None
    parts = md.split("\n---\n", 1)
    if len(parts) != 2:
        return None
    return parts[0], parts[1]


def _extract_title_from_frontmatter(fm_text: str) -> str | None:
    m = re.search(r"^title:\s*(.+)\s*$", fm_text, re.M)
    if not m:
        return None
    raw = m.group(1).strip()
    if raw.startswith("'") and raw.endswith("'"):
        raw = raw[1:-1].replace("''", "'")
    elif raw.startswith('"') and raw.endswith('"'):
        raw = raw[1:-1]
    return raw


def _update_title_in_frontmatter(fm_text: str, *, title: str) -> str:
    lines = fm_text.splitlines()
    out: list[str] = []
    replaced = False
    for line in lines:
        if re.match(r"^title:\s*", line) and not replaced:
            out.append(f"title: {_yaml_single_quote(title)}")
            replaced = True
        else:
            out.append(line)
    if not replaced:
        out.insert(1, f"title: {_yaml_single_quote(title)}")
    return "\n".join(out) + "\n"


def _ensure_h1(body: str, title: str) -> str:
    stripped = body.lstrip("\n")
    m = re.match(r"^(#\s+.*)\n", stripped)
    if m:
        rest = stripped[m.end() :]
        return f"# {title}\n\n{rest.lstrip()}"
    return f"# {title}\n\n{stripped}"


def _clean_title(title: str, locale: str) -> str:
    t = title.strip()
    for pat in TITLE_SUFFIX_PATTERNS.get(locale, []):
        t = re.sub(pat, "", t, flags=re.I).strip()
    t = re.sub(r"\s+", " ", t).strip()
    return t


def _title_case_en(text: str) -> str:
    # Title-case with acronym preservation; keep punctuation and existing separators.
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
        # Split hyphenated segments but keep slashes, dots as part of segment.
        parts = tok.split("-")
        new_parts: list[str] = []
        for i, part in enumerate(parts):
            # Strip surrounding punctuation for casing.
            m = re.match(r"^([(\"'“”‘’\[]*)(.*?)([)\"'“”‘’\],.;:!?]*)$", part)
            if not m:
                core = part
                pre = ""
                suf = ""
            else:
                pre, core, suf = m.groups()
            core_cased = title_word(
                core,
                is_first=not seen_word,
                force_cap=force_cap_next or (i > 0 and core.lower() in ACRONYM_MAP_EN),
            )
            if core:
                seen_word = True
            force_cap_next = False
            if ":" in suf:
                # After colon, force next word to be capitalized.
                force_cap_next = True
            new_parts.append(f"{pre}{core_cased}{suf}")
        out.append("-".join(new_parts))
    return "".join(out).strip()


def _normalize_en_h2(body: str) -> str:
    lines = body.splitlines()
    out: list[str] = []
    for line in lines:
        m = re.match(r"^##\s+(.+)$", line)
        if not m:
            out.append(line)
            continue
        h = m.group(1).strip()

        if re.match(r"^Key takeaways\b", h, flags=re.I):
            out.append("## Key Takeaways")
            continue

        if re.match(r"^What .+ really means \\(scope & boundaries\\)$", h, flags=re.I):
            out.append("## What it means (scope & boundaries)")
            continue

        if re.match(r"^.+ metrics that matter \\(how to evaluate quality\\)$", h, flags=re.I):
            out.append("## Metrics that matter (how to evaluate quality)")
            continue

        if re.match(r"^How to choose .+: selection guidance by scenario \\(trade-offs\\)$", h, flags=re.I):
            out.append("## How to choose (trade-offs by scenario)")
            continue

        if re.match(r"^Selection guidance by scenario \\(trade-offs\\)$", h, flags=re.I):
            out.append("## Selection guidance by scenario (trade-offs)")
            continue

        if re.match(r"^From design to manufacturing \\(implementation checkpoints\\)$", h, flags=re.I):
            out.append("## Implementation checkpoints (design to manufacturing)")
            continue

        if re.match(r"^.+ implementation checkpoints \\(design to manufacturing\\)$", h, flags=re.I):
            out.append("## Implementation checkpoints (design to manufacturing)")
            continue

        if re.match(r"^.+ common mistakes \\(and the correct approach\\)$", h, flags=re.I):
            out.append("## Common mistakes (and the correct approach)")
            continue

        if re.match(r"^Resources for .+ \\(related pages and tools\\)$", h, flags=re.I):
            out.append("## Related pages & tools")
            continue

        if re.match(r"^Related pages & tools$", h, flags=re.I):
            out.append("## Related pages & tools")
            continue

        if re.match(r"^.+ glossary \\(key terms\\)$", h, flags=re.I):
            out.append("## Glossary (key terms)")
            continue

        if re.match(r"^Conclusion:? .+ next steps$", h, flags=re.I) or re.match(
            r"^Conclusion \\(next steps\\)$", h, flags=re.I
        ):
            out.append("## Conclusion (next steps)")
            continue

        if re.match(r"^FAQ\\b", h, flags=re.I):
            out.append("## FAQ")
            continue

        if re.match(r"^Request a quote\\b", h, flags=re.I):
            out.append("## Request a quote (DFM review + pricing)")
            continue

        # Buyer-friendly playbook style headings
        if re.match(r"^.+: definition, scope, and who this guide is for$", h, flags=re.I):
            out.append("## Definition, scope, and who this guide is for")
            continue
        if re.match(r"^.+: what this playbook covers \\(and who it.?s for\\)$", h, flags=re.I):
            out.append("## What this guide covers (and who it’s for)")
            continue
        if re.match(r"^When .+ is the right approach \\(and when it isn.?t\\)$", h, flags=re.I):
            out.append("## When to use this approach (and when it isn’t)")
            continue
        if re.match(r"^When to use .+ \\(and when a standard approach is better\\)$", h, flags=re.I):
            out.append("## When to use this approach (and when not to)")
            continue
        if re.match(r"^Requirements you must define before (finalizing )?the quote$", h, flags=re.I) or re.match(
            r"^Requirements you must define before quoting$", h, flags=re.I
        ):
            out.append("## Specs & requirements (before quoting)")
            continue
        if re.match(r"^.+ specifications \\(.+\\)$", h, flags=re.I):
            out.append("## Specs to define")
            continue
        if re.match(r"^.+ manufacturing risks \\(root causes and prevention\\)$", h, flags=re.I):
            out.append("## Manufacturing risks (root causes & prevention)")
            continue
        if re.match(r"^.+ validation and acceptance \\(tests and pass criteria\\)$", h, flags=re.I):
            out.append("## Validation & acceptance (tests and pass criteria)")
            continue
        if re.match(r"^.+ supplier qualification checklist \\(.+\\)$", h, flags=re.I):
            out.append("## Supplier qualification checklist (RFQ, audit, traceability)")
            continue
        if re.match(r"^Decision guidance \\(.+\\)$", h, flags=re.I):
            out.append("## Decision guidance (trade-offs and decision rules)")
            continue
        if re.match(r"^How to choose .+ \\(trade-offs and decision rules\\)$", h, flags=re.I):
            out.append("## Decision guidance (trade-offs and decision rules)")
            continue
        if re.match(r"^The hidden risks that break scale-up$", h, flags=re.I):
            out.append("## Hidden risks (root causes & prevention)")
            continue
        if re.match(r"^Validation plan \\(what to test, when, and what .+pass.+ means\\)$", h, flags=re.I):
            out.append("## Validation & acceptance (tests and pass criteria)")
            continue

        out.append(line)
    return "\n".join(out) + ("\n" if body.endswith("\n") else "")


def main() -> int:
    updated = 0
    missing = 0
    skipped = 0

    for post in POSTS:
        for locale in TARGET_LOCALES:
            md_path = BLOGS_ROOT / post.year / post.month / locale / f"{post.slug}.md"
            if not md_path.exists():
                print(f"missing: {md_path}")
                missing += 1
                continue

            raw = md_path.read_text(encoding="utf-8", errors="ignore")
            parts = _split_frontmatter(raw)
            if not parts:
                print(f"skip(no-frontmatter): {md_path}")
                skipped += 1
                continue
            fm_without_end, body = parts

            old_title = _extract_title_from_frontmatter(fm_without_end)
            if not old_title:
                print(f"skip(no-title): {md_path}")
                skipped += 1
                continue

            new_title = _clean_title(old_title, locale)
            if locale == "en":
                new_title = _title_case_en(new_title)
            elif locale in {"de", "it", "fr", "es"}:
                # Capitalize first character if it's lowercase Latin.
                if new_title[:1].islower():
                    new_title = new_title[:1].upper() + new_title[1:]

            fm_updated = _update_title_in_frontmatter(fm_without_end, title=new_title)
            body_updated = _ensure_h1(body, new_title)
            if locale == "en":
                body_updated = _normalize_en_h2(body_updated)

            new_text = fm_updated + "---\n" + body_updated.lstrip("\n")
            if new_text != raw:
                md_path.write_text(new_text, encoding="utf-8")
                updated += 1

    print(f"updated_files={updated} missing_files={missing} skipped_files={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
