---
source_id: "microchip-vsc7420-differential-pair-mismatch-and-common-mode-current"
title: "VSC7420/1/2 Hardware Design Checklist"
organization: "Microchip"
owner: "Microchip"
source_type: "hardware_design_checklist"
url: "https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/DesignChecklist/VSC7420-1-2-Hardware-Design-Checklist-DS00005256.pdf"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_design_checklist"
exact_data_class: "method_boundary"
scope_type: "vendor_scoped_differential_pair_mismatch_and_common_mode_current_guidance"
source_origin_path: "official Microchip VSC7420 hardware design checklist differential routing checklist"
source_page_range: "differential routing and impedance checklist items"
confidence: "medium"
topic_tags: ["microchip", "differential-pair", "mismatch", "common-mode-current", "emi", "same-layer", "stub", "via", "electrical-length"]
status: "active"
notes: "Official Microchip hardware design checklist. Safe for guarded wording that mismatched differential-pair members create common-mode current, that reducing mismatch reduces common-mode current, that common-mode current is a primary EMI source, and that pairs should stay on the same layer with minimized vias and stub lengths. Do not use it for universal numeric skew limits or as a standards-body mandate."
---

# Source Summary

## What It Covers

- matched electrical lengths within a differential pair
- differential impedance as a true pair structure
- keeping pair members on the same layer and minimizing vias
- reducing mismatch to reduce common-mode current
- common-mode current as a primary EMI source

## Why It Matters

- gives the corpus one current-public semiconductor-owner source that directly names `common-mode current` as the outcome of pair mismatch and links that current to EMI risk

## Extraction Notes

- Safe for guarded wording that differential-pair members should be identical in electrical length and kept on the same layer when practical.
- Safe for wording that reduced mismatch reduces common-mode current and that common-mode current is a primary EMI source.
- Safe for wording that stub lengths and via count should be minimized in this pair-integrity context.
- Do not use this source for universal `100 ohm` doctrine, numeric budgets, or cross-interface closure claims.

## Refresh Notes

- Refresh before publication if the checklist revision or PDF path changes.
