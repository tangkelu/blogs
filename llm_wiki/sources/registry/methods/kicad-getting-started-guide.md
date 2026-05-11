---
source_id: "kicad-getting-started-guide"
title: "Getting Started in KiCad"
organization: "KiCad Documentation Team"
source_type: "software_official_docs"
url: "https://docs.kicad.org/8.0/en/getting_started_in_kicad/getting_started_in_kicad.html"
jurisdiction: "global"
published_at: ""
checked_at: "2026-04-29"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
topic_tags: ["kicad", "getting-started", "schematic", "erc", "pcb-layout", "drc", "manufacturing-output", "beginner-workflow", "footprint-editor", "pin-1", "origin", "library-conventions"]
status: "active"
notes: "Official KiCad getting-started documentation. Use for beginner workflow identity, manufacturing-output handoff vocabulary, and guarded CAD-library conventions such as through-hole footprint origin handling and KLC-aware footprint construction. Do not treat it as universal package-owner or standards-owner authority, and do not freeze current version-specific UI details."
---

# Source Summary

## What It Covers

- Official beginner workflow for creating a project in KiCad
- Schematic capture, electrical-rules-check context, PCB layout, design-rule-check context, and manufacturing-output generation
- Tool-author-owned sequence for moving from circuit design into board files
- Footprint-editor tutorial context including through-hole footprint placement around `(0,0)` and explicit mention that official library footprints follow `KLC`

## Why It Matters

- It upgrades KiCad from tool-feature identity only into a usable official beginner-workflow anchor.
- It supports conservative `first-circuit-board` workflow language without turning one draft's recipe into a universal design rule.
- It also provides a narrow CAD-owner source for guarded footprint-library conventions such as using `pin 1 @ (0,0)` for through-hole footprints in the documented workflow and treating `KLC` as the basis for official library footprints.

## Extraction Notes

- Safe for staged workflow identity such as project setup, schematic capture, ERC, PCB layout, DRC, and fabrication-output generation.
- Safe for narrow CAD-library convention wording that the documented KiCad workflow places through-hole `pin 1` at `(0,0)` and uses `KLC` as the basis for official library footprints.
- Do not infer that KiCad is the best beginner tool, that this sequence is the only correct workflow, or that following the guide guarantees manufacturability.
- Do not rewrite KiCad's documented convention as a universal land-pattern, connector-origin, or standards-mandated rule for every package family.
- Do not freeze current UI wording, current version labels, plugin ecosystem, or library completeness without a dated follow-on source pass.

## Refresh Notes

- Refresh before publication if a draft cites current KiCad version, current screenshots, current menu wording, or recommendation language.
