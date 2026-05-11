---
source_id: "ti-powerpad-thermally-enhanced-package"
title: "TI PowerPAD Thermally Enhanced Package"
organization: "Texas Instruments"
owner: "Texas Instruments"
source_type: "application_report"
url: "https://www.ti.com/lit/an/slma002h/slma002h.pdf"
jurisdiction: "global"
published_at: "2022-05"
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_packaging_note"
exact_data_class: "method_boundary"
scope_type: "vendor_scoped_exposed_pad_board_attach_and_plane_tie_guidance"
source_origin_path: "official TI PowerPAD package application report"
source_page_range: "package use and board connection guidance"
confidence: "medium"
topic_tags: ["texas-instruments", "powerpad", "exposed-pad", "thermal", "board-attach", "ground-plane", "signal-plane", "package"]
status: "active"
notes: "Official TI application report. Safe for guarded wording that the exposed pad is part of the package attach strategy and must be soldered to the PCB, while the correct plane tie must be verified from the device datasheet because it may connect to signal, power, or ground depending on the package. Do not use it as a universal `ground-only` rule."
---

# Source Summary

## What It Covers

- exposed-pad or PowerPAD board-attach expectation
- package thermal path into the PCB
- device-specific requirement to verify whether the exposed pad ties to signal, power, or ground

## Why It Matters

- gives the corpus one current-public semiconductor-owner source that is stronger than generic grounding prose because it explicitly governs how exposed-pad packages should be attached to the board
- adds a built-in anti-overclaim guard: the package pad does not universally mean ground and must be checked per device datasheet

## Extraction Notes

- Safe for guarded wording that an exposed thermal pad is meant to be soldered to the PCB as part of the package thermal and electrical attach path.
- Safe for wording that the correct board tie must be confirmed in the owner datasheet because exposed pads may connect to signal, power, or ground depending on the design.
- Safe for using TI `PowerPAD` as one owner-scoped package family that supports local thermal spreading and controlled board attach.
- Do not use this report for universal ground-net claims, exact via counts, exact stencil or paste recipes, or guaranteed thermal / EMI outcomes.

## Refresh Notes

- Refresh before reuse if TI updates the application report revision.
