---
source_id: "ti-tm4c-differential-pair-symmetry-and-common-mode-noise"
title: "System Design Guidelines for the TM4C129x Family of Tiva C Series Microcontrollers"
organization: "Texas Instruments"
owner: "Texas Instruments"
source_type: "application_note"
url: "https://www.ti.com/lit/an/spma056/spma056.pdf"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_application_note"
exact_data_class: "method_boundary"
scope_type: "vendor_scoped_differential_pair_symmetry_and_common_mode_noise_layout_guidance"
source_origin_path: "official TI TM4C129x system design guidelines differential pair layout section"
source_page_range: "differential pair layout guidance"
confidence: "medium"
topic_tags: ["texas-instruments", "differential-pair", "symmetry", "parallel", "length-match", "common-mode-noise", "emi", "plane-split"]
status: "active"
notes: "Official TI application note. Safe for guarded wording that differential pairs should run parallel and be matched in length, that localized unavoidable asymmetry should be kept short, and that imbalance increases common-mode noise and EMI. Do not use it for universal skew numbers, impedance numerics, or compliance outcomes."
---

# Source Summary

## What It Covers

- differential pair traces running parallel and matched in length
- keeping unavoidable non-parallel sections short and localized
- avoiding stubs, minimizing vias, and avoiding plane-split crossings
- relationship between pair imbalance and increased common-mode noise or EMI

## Why It Matters

- gives the corpus one current-public semiconductor-owner source that ties pair symmetry and length matching directly to `common-mode noise` and `EMI`, rather than only to generic high-speed routing posture

## Extraction Notes

- Safe for guarded wording that differential pairs should remain parallel and matched in length so delay mismatch does not increase common-mode noise and EMI.
- Safe for wording that unavoidable asymmetry near connectors or protection parts should be kept short and localized.
- Safe for wording that differential pairs should avoid plane-split crossings, minimize stubs, and minimize unnecessary vias in this pair-balance context.
- Do not use this source for exact skew budgets, exact spacing numbers, or universal interface-independent doctrine.

## Refresh Notes

- Refresh before publication if TI revises the application note or section wording.
