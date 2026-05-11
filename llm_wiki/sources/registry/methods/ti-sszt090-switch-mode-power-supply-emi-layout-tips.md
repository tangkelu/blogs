---
source_id: "ti-sszt090-switch-mode-power-supply-emi-layout-tips"
title: "Layout Tips to Pass EMI for Your Switch-Mode Power Supply"
organization: "Texas Instruments"
owner: "Texas Instruments"
source_type: "technical_article"
url: "https://www.ti.com/document-viewer/lit/html/SSZT090"
jurisdiction: "global"
published_at: "2016-10"
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_technical_article"
exact_data_class: "method_boundary"
scope_type: "vendor_scoped_switch_mode_power_supply_emi_layout_guidance"
source_origin_path: "official TI switch-mode power EMI layout article"
source_page_range: "board layout considerations for minimizing EMI"
confidence: "medium"
topic_tags: ["texas-instruments", "switch-mode-power-supply", "emi", "layout", "input-capacitor", "switch-node", "boot-capacitor"]
status: "active"
notes: "Official TI technical article. Safe for guarded wording that the input and bootstrap capacitors should stay close to the IC power pins, transient current loops should be minimized, and the switch node should stay as small as practical. Do not use it for exact filter values, exact copper shapes, or compliance guarantees."
---

# Source Summary

## What It Covers

- board-layout considerations for reducing switch-mode power-supply EMI
- placing the input capacitor and bootstrap capacitor close to the IC between `VIN` and `GND`
- minimizing high transient current loop area
- keeping the switch node as small as practical

## Why It Matters

- adds a direct owner-backed EMI layout source for local input-loop control and switch-node minimization
- strengthens the handbook `EMI filter close to chip power input` lane at the narrower and safer `local input decoupling / input-loop control` boundary

## Extraction Notes

- Safe for guarded statements that local input capacitors should stay close to the switcher power pins.
- Safe for wording that the transient input loop should be minimized for EMI-aware layout.
- Safe for wording that the switch node should stay as small as practical.
- Do not use this source for exact capacitor values, exact loop dimensions, exact EMI limits, or pass/fail claims.

## Refresh Notes

- Refresh before publication if TI updates the article revision or exact wording matters.
