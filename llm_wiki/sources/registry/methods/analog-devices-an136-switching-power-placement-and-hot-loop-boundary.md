---
source_id: "analog-devices-an136-switching-power-placement-and-hot-loop-boundary"
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
scope_type: "vendor_scoped_switching_power_stage_placement_and_hot_loop_layout_guidance"
source_origin_path: "official ADI application note switching-power layout and control-placement guidance"
source_page_range: "switching-power placement, control-circuit placement, and hot-loop guidance"
confidence: "medium"
topic_tags: ["analog-devices", "switching-regulator", "hot-loop", "switch-node", "control-circuitry", "layout", "emi"]
status: "active"
notes: "Official ADI application note. Safe for guarded wording that switching-power control circuitry should stay away from noisy switching copper, hot-loop circumference should be minimized, sensitive traces should avoid running under the supply, and unsynchronized supplies should keep separate input current paths. Do not use it for compensation, numeric keepouts, or EMI-pass claims."
---

# Source Summary

## What It Covers

- switching-power layout as a split between noisy power-stage copper and quieter control circuitry
- placing control circuitry away from noisy switching copper and closer to the quieter output side when practical
- shielding or ground-plane separation when control circuitry must live near the power stage
- avoiding sensitive trace routing under the power supply
- minimizing hot-loop circumference in switching-power layouts
- separating input current paths among different unsynchronized power supplies

## Why It Matters

- adds a direct owner-backed route for the still-open `194页 handbook D5 switch-mode power EMC placement` lane
- supports a narrower switching-power placement boundary than the existing `current-carrying` and `remote-feedback` cards

## Extraction Notes

- Safe for guarded statements that switching-power control or other sensitive circuitry should stay away from noisy switching copper.
- Safe for wording that hot-loop circumference should be minimized.
- Safe for wording that sensitive traces should avoid routing under the power supply.
- Safe for wording that separate unsynchronized supplies should keep separate input current paths.
- Do not use this source for exact distances, exact copper geometry, compensation networks, or EMI-compliance proof.

## Refresh Notes

- Refresh before publication if exact article wording or section anchors matter.
