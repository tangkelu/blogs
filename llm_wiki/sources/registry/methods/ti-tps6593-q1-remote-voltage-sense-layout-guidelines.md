---
source_id: "ti-tps6593-q1-remote-voltage-sense-layout-guidelines"
title: "TPS6593-Q1 PMIC for ADAS and Infotainment Processors datasheet"
organization: "Texas Instruments"
owner: "Texas Instruments"
source_type: "manufacturer_datasheet"
url: "https://www.ti.com/lit/ds/symlink/tps6593-q1.pdf"
jurisdiction: "global"
published_at: "2024-01"
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "stable"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_datasheet"
exact_data_class: "method_boundary"
scope_type: "vendor_scoped_pmic_remote_voltage_sense_layout_guidance"
source_origin_path: "official TI datasheet layout-guidelines section"
source_page_range: "remote voltage sensing layout guidance section"
confidence: "medium"
topic_tags: ["texas-instruments", "pmic", "remote-sense", "feedback", "quiet-layer", "switching-power", "layout"]
status: "active"
notes: "Official TI PMIC datasheet. Safe for guarded wording that remote-voltage-sense and feedback lines are susceptible to noise, should stay short and direct, should be routed together when used as Kelvin sense, and should be kept away from noisy power or switch-node regions on a quiet layer. Do not use it for rail-specific numerics, compensation values, divider values, or PMIC-specific recipe closure."
---

# Source Summary

## What It Covers

- PMIC layout guidance for remote voltage sensing and feedback/sense routing
- remote-sense lines as noise-sensitive low-level inputs
- quiet-layer routing and separation from noisy switch-node or power regions
- short, direct, paired routing when remote sense is used

## Why It Matters

- gives the `194页 handbook` `D3 remote-feedback` lane one current-public owner-backed source for `quiet sense-point` and `remote feedback` posture without depending on RK3588-specific rail tables

## Extraction Notes

- Safe for guarded statements that remote-voltage-sense or feedback lines are susceptible to noise.
- Safe for wording that these lines should be short and direct and should stay away from noisy signals or noisy power areas.
- Safe for wording that paired remote-sense lines should be routed close together on a quiet layer when the owner guidance frames them that way.
- Do not use this source for exact rail names, voltage targets, divider values, compensation recipes, or guaranteed regulation outcomes.

## Refresh Notes

- Refresh before publication if exact TI revision or section wording matters.
