---
source_id: "murata-small-mlcc-board-bending-caution-pdf"
title: "Points of Downsizing the Chip Size of Capacitors"
organization: "Murata Manufacturing"
owner: "Murata Manufacturing"
source_type: "manufacturer_application_note"
url: "https://www.murata.com/-/media/webrenewal/products/capacitor/ceramiccapacitor/faq/mnt/small-mlcc-caution-ver3.ashx?la=en"
jurisdiction: "global"
checked_at: "2026-05-14"
retrieved_at: "2026-05-14"
trust_tier: "t1"
stability: "static"
must_refresh: false
original_source_language: "en"
authority_class: "manufacturer_small_mlcc_mounting_caution"
scope_type: "vendor_scoped_small_mlcc_board_bending_risk"
source_origin_path: "official Murata PDF"
source_page_range: "PDF body"
confidence: "medium"
topic_tags: ["murata", "mlcc", "0201", "0402", "downsizing", "board-bending", "cracking"]
status: "active"
notes: "Official Murata caution PDF for downsizing chip capacitors. Safe for guarded statements that shrinking to smaller packages such as 0402 and 0201 increases sensitivity to board-bending crack risk if the surrounding land and wiring approach is not redesigned accordingly. Do not infer universal pad or routing rules from this PDF alone."
---

# Source Summary

## What It Covers

- Murata warns that simply shrinking the land to match a smaller capacitor package is not enough when moving to very small MLCC sizes.
- Murata describes increasing crack sensitivity as chip size drops into very small families such as `0402` and `0201`.
- Murata explains that when the wiring width is left unchanged, stress concentration and crack risk increase as the component becomes smaller.

## Why It Matters

- Gives the local corpus one owner-backed source for why tiny MLCCs near dense ICT probe regions deserve stronger mechanical caution than larger passives.
- Supports guarded dense-layout wording around `0201` / `0402` fragility without inventing package-clearance numbers.

## Extraction Notes

- Safe for qualitative statements about small-MLCC downsizing and higher board-bending crack sensitivity.
- Safe for guarded wording that surrounding geometry must be reconsidered rather than only shrinking the footprint.
- Do not turn this PDF into universal land-pattern, trace-width, or probe-clearance design rules.

## Refresh Notes

- The PDF is currently static and does not require routine refresh for the narrow qualitative claims above.
