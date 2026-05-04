---
source_id: "analog-devices-an136-pcb-layout-nonisold-switching-supplies"
title: "AN-136: PCB Layout Considerations for Non-Isolated Switching Power Supplies"
organization: "Analog Devices"
source_type: "application_note"
url: "https://www.analog.com/en/resources/app-notes/an-136.html"
jurisdiction: "global"
published_at: ""
checked_at: "2026-04-30"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
topic_tags: ["analog-devices", "pcb-layout", "switching-power-supplies", "high-current", "thick-copper", "multiple-layers", "vias", "hot-loop"]
status: "active"
notes: "Use for guarded high-current layout guidance: short and wide traces, thick copper or multiple layers, large copper planes, multiple vias in high-current loops, and reduced hot-loop area. Do not convert product-specific recommendations into universal board rules."
---

# Source Summary

## What It Covers

- high-current and high-di/dt path handling in PCB layout for switching power supplies
- short and wide high-current traces to reduce inductance, resistance, and voltage drop
- thick copper or multiple layers for high-current power layers
- use of large copper planes and multiple vias to reduce impedance and thermal stress
- minimizing hot-loop area in pulsating current paths

## Why It Matters

- Gives `llm_wiki` a manufacturer-owned source for the qualitative PCB consequences that appear after current is known.
- Supports a narrow board-layout boundary without pretending that one current number directly produces a universal trace recipe.

## Extraction Notes

- Safe for guarded layout-priority language around high-current paths.
- Safe for wording such as `high-current traces should be short and wide`, `thick copper or multiple layers may be used`, and `multiple vias may be needed in high-current loops`.
- Do not use this source alone for exact trace-width tables, current thresholds, or universal multilayer prescriptions.

## Refresh Notes

- Refresh before publication if exact layout checklist wording matters.
