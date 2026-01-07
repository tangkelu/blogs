#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rebuild APTPCB v5 keyword taxonomy from legacy prompt libraries.

Source:
  prompts_aptpcb/_legacy/blogs_prompt_v1..v4/**/keywords.json

Output:
  prompts_aptpcb/blogs_prompt_v5/??-*/keywords.json

Design goals:
- New v5 taxonomy: engineering topics + industry verticals
- Large keyword universe for a new site
- Dedupe aggressively (case-insensitive, whitespace normalized)
- Auto-tag `intent`: query vs pillar (heuristic)
- Reset all `used` to false
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


REPO_ROOT = Path(__file__).resolve().parents[1]
LEGACY_ROOT = REPO_ROOT / "prompts_aptpcb" / "_legacy"
V5_ROOT = REPO_ROOT / "prompts_aptpcb" / "blogs_prompt_v5"


@dataclass(frozen=True)
class LegacyKeyword:
    keyword: str
    source_version: str
    source_category: str
    source_subsection: str


@dataclass(frozen=True)
class TaxonomyBucket:
    number: int
    slug: str
    title: str
    # Match against legacy category folder name (without numeric prefix)
    category_patterns: Tuple[str, ...]


BUCKETS: List[TaxonomyBucket] = [
    TaxonomyBucket(
        1,
        "Manufacturing-Cost",
        "Manufacturing, Cost & Lead Time (APTPCB)",
        ("manufacturing", "cost", "lead", "quote", "rfq", "supplier", "npi"),
    ),
    TaxonomyBucket(
        2,
        "PCBA-Turnkey",
        "PCBA, Turnkey & Assembly (APTPCB)",
        ("pcba", "assembly", "turnkey", "smt", "tht", "box-build"),
    ),
    TaxonomyBucket(
        3,
        "Flex-RigidFlex",
        "Flex & Rigid-Flex (APTPCB)",
        ("flex", "rigid-flex", "fpc"),
    ),
    TaxonomyBucket(
        4,
        "HighSpeed-Impedance",
        "High-Speed, RF, Impedance & HDI (APTPCB)",
        ("high-speed", "si", "signal", "impedance", "hdi", "slp", "substrate-like", "mmwave", "antenna", "rf"),
    ),
    TaxonomyBucket(
        5,
        "Materials-LED-Thermal",
        "Materials, Thermal & Special Substrates (APTPCB)",
        ("materials", "stackup", "metal-core", "ims", "ceramic", "rogers", "taconic", "teflon", "arlon", "megtron", "isola", "led"),
    ),
    TaxonomyBucket(
        6,
        "Testing-Inspection",
        "Testing, Inspection & Quality (APTPCB)",
        ("testing", "inspection", "quality", "aoi", "xray", "x-ray", "ict", "fct", "flying-probe", "spi"),
    ),
    TaxonomyBucket(
        7,
        "Surface-Finishes",
        "PCB Surface Finishes (APTPCB)",
        ("finish", "enig", "enepig", "osp", "hasl", "immersion", "silver", "tin", "gold"),
    ),
    TaxonomyBucket(
        8,
        "Reliability-Compliance",
        "Reliability, Standards & Compliance (APTPCB)",
        ("reliability", "validation", "ipc", "compliance", "ul", "rohs", "reach", "caf", "thermal cycling", "damp heat", "emc", "emi"),
    ),
    # Industry verticals (09+)
    TaxonomyBucket(
        9,
        "Industry-DataCenter-AI",
        "Industry: Data Center, AI Server & Backplane (APTPCB)",
        ("datacenter", "data-center", "server", "ai-server", "ai-chip", "backplane", "optical-module"),
    ),
    TaxonomyBucket(
        10,
        "Industry-5G-RF-mmWave",
        "Industry: 5G/6G, RF & mmWave (APTPCB)",
        ("5g", "6g", "telecom", "communication", "rf", "mmwave", "antenna"),
    ),
    TaxonomyBucket(
        11,
        "Industry-Automotive",
        "Industry: Automotive & EV (APTPCB)",
        ("automotive", "adas", "ev", "ethernet", "t1", "bms", "battery-management"),
    ),
    TaxonomyBucket(
        12,
        "Industry-Power-Energy",
        "Industry: Power Electronics & Energy (APTPCB)",
        ("power", "inverter", "renewable", "sic", "gan", "power-module", "smart-grid", "cooling"),
    ),
    TaxonomyBucket(
        13,
        "Industry-Medical",
        "Industry: Medical Devices & Wearables (APTPCB)",
        ("medical", "implantable", "imaging", "wearable"),
    ),
    TaxonomyBucket(
        14,
        "Industry-Industrial-Robotics",
        "Industry: Industrial Control & Robotics (APTPCB)",
        ("industrial", "robot", "robotics", "servo", "encoder", "tsn"),
    ),
    TaxonomyBucket(
        15,
        "Industry-Consumer-IoT",
        "Industry: Consumer Electronics, IoT & Smart Home (APTPCB)",
        ("consumer", "iot", "smart", "wireless", "smart-home", "smartkitchen", "doorlock", "doorbell", "baby", "pet", "sleep", "wellness"),
    ),
    TaxonomyBucket(
        16,
        "Industry-Audio-ARVR-Display",
        "Industry: Audio, AR/VR & Display (APTPCB)",
        ("audio", "ar-vr", "headset", "display"),
    ),
    TaxonomyBucket(
        17,
        "Industry-Outdoor-Mobility",
        "Industry: Outdoor, Mobility & Drones (APTPCB)",
        ("ebike", "mobility", "camping", "outdoor", "drone", "uav", "transportation"),
    ),
    TaxonomyBucket(
        18,
        "Industry-Security-Surveillance",
        "Industry: Security & Surveillance (APTPCB)",
        ("security", "surveillance", "personal-safety"),
    ),
    TaxonomyBucket(
        19,
        "Industry-Environment-Agritech",
        "Industry: Environmental Monitoring & Agritech (APTPCB)",
        ("environment", "indoor-air", "agritech", "urban-gardening", "pool", "spa"),
    ),
    TaxonomyBucket(
        20,
        "Industry-Test-Measurement",
        "Industry: Test & Measurement (APTPCB)",
        ("test-measurement", "signal-integrity-lab", "lab"),
    ),
]


def _normalize_keyword(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    return text


def _canonical_key(text: str) -> str:
    return _normalize_keyword(text).lower()


def _strip_prefix(folder_name: str) -> str:
    # "43-Smart-Kitchen-Appliance-PCB" -> "Smart-Kitchen-Appliance-PCB"
    return re.sub(r"^\d{2,3}-", "", folder_name)


def _iter_legacy_keyword_files() -> Iterable[Tuple[str, Path]]:
    # yields: (version_name, keywords.json path)
    if not LEGACY_ROOT.exists():
        return
    for version_dir in sorted(LEGACY_ROOT.iterdir()):
        if not version_dir.is_dir():
            continue
        version_name = version_dir.name
        for path in sorted(version_dir.rglob("keywords.json")):
            yield version_name, path


def load_legacy_keywords() -> List[LegacyKeyword]:
    items: List[LegacyKeyword] = []
    for version_name, path in _iter_legacy_keyword_files():
        # Ignore the auto-generated “legacy keywords” dump (too noisy + duplicates).
        if "Legacy-V1V2-Keywords" in str(path):
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        category_folder = path.parent.name  # .../<category>/keywords.json
        for subsection in data.get("subsections", []):
            subsection_name = str(subsection.get("name", "")).strip() or "General"
            for kw in subsection.get("keywords", []):
                keyword = _normalize_keyword(str(kw.get("keyword", "") or ""))
                if not keyword:
                    continue
                items.append(
                    LegacyKeyword(
                        keyword=keyword,
                        source_version=version_name,
                        source_category=category_folder,
                        source_subsection=subsection_name,
                    )
                )
    return items


def pick_bucket_for_category(category_folder: str) -> Optional[TaxonomyBucket]:
    name = _strip_prefix(category_folder).lower()
    best: Optional[TaxonomyBucket] = None
    best_score = 0
    best_weight = 0

    # Choose the best-matching bucket instead of first match.
    # This avoids broad patterns (e.g. "consumer"/"smart") swallowing more specific buckets.
    for bucket in BUCKETS:
        matches = [pat for pat in bucket.category_patterns if pat in name]
        if not matches:
            continue
        score = len(matches)
        weight = sum(len(pat) for pat in matches)
        if score > best_score or (score == best_score and weight > best_weight):
            best = bucket
            best_score = score
            best_weight = weight

    return best


def pick_bucket_for_keyword_text(keyword: str) -> TaxonomyBucket:
    text = keyword.lower()
    # Specific keyword-based fallbacks
    if any(t in text for t in ["enig", "enepig", "osp", "hasl", "immersion silver", "immersion tin"]):
        return next(b for b in BUCKETS if b.number == 7)
    if any(t in text for t in ["ipc-", "ipc ", "ul ", "rohs", "reach", "caf ", "delamination", "emc", "emi"]):
        return next(b for b in BUCKETS if b.number == 8)
    if any(t in text for t in ["aoi", "xray", "x-ray", "ict", "fct", "flying probe", "spi inspection"]):
        return next(b for b in BUCKETS if b.number == 6)
    if any(t in text for t in ["flex", "rigid-flex", "fpc", "coverlay", "stiffener"]):
        return next(b for b in BUCKETS if b.number == 3)
    if any(t in text for t in ["impedance", "stackup", "tdr", "gcpw", "microstrip", "stripline", "hdi", "slp", "mmwave", "antenna", "rf"]):
        return next(b for b in BUCKETS if b.number == 4)
    if any(t in text for t in ["rogers", "taconic", "teflon", "arlon", "megtron", "isola", "ceramic", "ims", "metal core", "mcpcb", "aluminum pcb"]):
        return next(b for b in BUCKETS if b.number == 5)
    if any(t in text for t in ["server", "backplane", "optical module", "ai server", "data center"]):
        return next(b for b in BUCKETS if b.number == 9)
    if any(t in text for t in ["5g", "6g", "telecom"]):
        return next(b for b in BUCKETS if b.number == 10)
    if any(t in text for t in ["automotive", "adas", "ethernet", "t1", "ev", "bms", "battery management"]):
        return next(b for b in BUCKETS if b.number == 11)
    if any(t in text for t in ["inverter", "sic", "gan", "power module", "smart grid"]):
        return next(b for b in BUCKETS if b.number == 12)
    if "medical" in text or "implant" in text:
        return next(b for b in BUCKETS if b.number == 13)
    if any(t in text for t in ["robot", "servo", "encoder", "industrial"]):
        return next(b for b in BUCKETS if b.number == 14)
    return next(b for b in BUCKETS if b.number == 15)


def infer_intent(bucket: TaxonomyBucket, keyword: str) -> str:
    text = keyword.lower().strip()
    if bucket.number >= 9:
        return "query"

    # Query signals
    if any(
        token in text
        for token in [
            "how to",
            "vs",
            "checklist",
            "guide",
            "best practices",
            "rules",
            "cost",
            "lead time",
            "pricing",
            "troubleshooting",
            "root causes",
            "prevention",
            "when to",
        ]
    ):
        return "query"

    # Very short head terms can be pillar candidates.
    words = re.findall(r"[a-z0-9]+", text)
    if 1 <= len(words) <= 4:
        return "pillar"

    return "query"


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_keywords_json(
    *,
    output_dir: Path,
    bucket: TaxonomyBucket,
    subsections: Dict[str, List[Dict[str, object]]],
) -> None:
    payload = {
        "section_number": bucket.number,
        "section_title": bucket.title,
        "subsections": [{"name": k, "keywords": v} for k, v in subsections.items()],
    }
    ensure_dir(output_dir)
    (output_dir / "keywords.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def rebuild() -> Dict[str, object]:
    legacy = load_legacy_keywords()

    # Dedupe keywords (global), but keep first seen provenance for subsection grouping.
    seen = set()
    deduped: List[LegacyKeyword] = []
    for item in legacy:
        key = _canonical_key(item.keyword)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(item)

    buckets_out: Dict[int, Dict[str, List[Dict[str, object]]]] = {}
    bucket_counts: Dict[int, int] = {}

    for item in deduped:
        bucket = pick_bucket_for_category(item.source_category) or pick_bucket_for_keyword_text(item.keyword)
        intent = infer_intent(bucket, item.keyword)

        # For engineering buckets keep the original subsection; for industry buckets keep a compact source label.
        if bucket.number <= 8:
            subsection_name = item.source_subsection
        else:
            subsection_name = _strip_prefix(item.source_category).replace("-", " ").strip() or "General"

        subsection_name = re.sub(r"\s+", " ", subsection_name)
        if len(subsection_name) > 60:
            subsection_name = subsection_name[:60].rstrip()

        record = {"keyword": item.keyword, "intent": intent, "used": False}
        buckets_out.setdefault(bucket.number, {}).setdefault(subsection_name, []).append(record)
        bucket_counts[bucket.number] = bucket_counts.get(bucket.number, 0) + 1

    # Write out: only for buckets 09+ (industry) and also allow enriching existing 01-08.
    for bucket in BUCKETS:
        out_dir = V5_ROOT / f"{bucket.number:02d}-{bucket.slug}"
        subsections = buckets_out.get(bucket.number, {})
        if not subsections:
            continue

        # Merge with existing v5 keywords if present, but always reset used=false.
        existing_path = out_dir / "keywords.json"
        if existing_path.exists():
            try:
                existing = json.loads(existing_path.read_text(encoding="utf-8"))
            except Exception:
                existing = None
            if existing:
                for sub in existing.get("subsections", []):
                    name = str(sub.get("name", "")).strip() or "General"
                    for kw in sub.get("keywords", []):
                        keyword = _normalize_keyword(str(kw.get("keyword", "") or ""))
                        if not keyword:
                            continue
                        intent = str(kw.get("intent") or infer_intent(bucket, keyword))
                        subsections.setdefault(name, []).append({"keyword": keyword, "intent": intent, "used": False})

                # Dedup within subsections after merge
                for name, arr in list(subsections.items()):
                    local_seen = set()
                    uniq = []
                    for rec in arr:
                        k = _canonical_key(rec["keyword"])
                        if k in local_seen:
                            continue
                        local_seen.add(k)
                        uniq.append(rec)
                    subsections[name] = uniq

        # Sort subsections and keywords for stable diffs
        ordered: Dict[str, List[Dict[str, object]]] = {}
        for sub_name in sorted(subsections.keys(), key=lambda s: s.lower()):
            ordered[sub_name] = sorted(subsections[sub_name], key=lambda r: r["keyword"].lower())

        write_keywords_json(output_dir=out_dir, bucket=bucket, subsections=ordered)

    return {
        "legacy_total": len(legacy),
        "deduped_total": len(deduped),
        "bucket_counts": {str(k): v for k, v in sorted(bucket_counts.items())},
    }


def main() -> None:
    if not LEGACY_ROOT.exists():
        raise SystemExit(f"Legacy prompts not found: {LEGACY_ROOT}")
    ensure_dir(V5_ROOT)
    report = rebuild()
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
