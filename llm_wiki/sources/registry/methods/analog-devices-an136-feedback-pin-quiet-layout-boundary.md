---
source_id: "analog-devices-an136-feedback-pin-quiet-layout-boundary"
title: "AN-136: PCB Layout Considerations for Non-Isolated Switching Power Supplies"
organization: "Analog Devices"
owner: "Analog Devices"
source_type: "application_note"
url: "https://www.analog.com/en/resources/app-notes/an-136.html"
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
scope_type: "vendor_scoped_switching_regulator_feedback_layout_guidance"
source_origin_path: "official ADI application note control and feedback layout guidance"
source_page_range: "feedback and low-level control input layout guidance"
confidence: "medium"
topic_tags: ["analog-devices", "switching-regulator", "feedback-pin", "quiet-ground", "switch-node", "layout"]
status: "active"
notes: "Official ADI application note. Safe for guarded wording that feedback or other low-level control pins should be kept away from switching nodes and noisy current paths, should avoid large loops, and should reference a quiet analog ground region. Do not use it for part-specific compensation, output-voltage setup, or numeric geometry rules."
---

# Source Summary

## What It Covers

- switching-power PCB layout considerations for low-level control and feedback signals
- feedback and control pins as noise-sensitive inputs
- routing away from switch nodes and noisy current loops
- quiet analog grounding and small-loop posture for sensitive control paths

## Why It Matters

- adds a second owner-backed source for the same `quiet sense-point` family, strengthening the new `D3 remote-feedback` lane above a single-owner wording surface

## Extraction Notes

- Safe for guarded statements that feedback or similar low-level control inputs should stay away from switching nodes and noisy current paths.
- Safe for wording that sensitive control routing should avoid unnecessary loop area.
- Safe for wording that quiet analog-ground reference handling matters for these low-level control paths.
- Do not use this source for exact compensation networks, regulator setup values, or numeric keepout rules.

## Refresh Notes

- Refresh before publication if exact article wording or section anchors matter.
