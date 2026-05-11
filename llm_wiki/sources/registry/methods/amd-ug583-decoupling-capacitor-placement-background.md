---
source_id: "amd-ug583-decoupling-capacitor-placement-background"
title: "AMD UG583 UltraScale PCB Design Guide: Capacitor Placement Background"
organization: "AMD"
owner: "AMD"
source_type: "design_guide_section"
url: "https://docs.amd.com/r/en-US/ug583-ultrascale-pcb-design/Capacitor-Placement-Background"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_design_guide"
exact_data_class: "method_boundary"
scope_type: "vendor_scoped_fpga_decoupling_placement_guidance"
source_origin_path: "official AMD UltraScale PCB design guide decoupling placement section"
source_page_range: "capacitor placement background"
confidence: "medium"
topic_tags: ["amd", "xilinx", "ultrascale", "fpga", "decoupling", "power-pins", "placement", "mounting-inductance"]
status: "active"
notes: "Official AMD design-guide section. Safe for guarded wording that decoupling capacitors belong close to the device being decoupled and that added spacing increases current-path length and mounting inductance. Do not use it for exact capacitor counts, values, backside-only rules, or device-independent placement recipes."
---

# Source Summary

## What It Covers

- decoupling-capacitor placement as a board-side distance and mounting-inductance problem
- keeping the capacitor close to the device being decoupled
- the effect of increased spacing on current-path length and inductive burden

## Why It Matters

- adds a current-public semiconductor-owner source for local processor / FPGA decoupling placement rather than only generic capacitor-role vocabulary
- helps separate near-device decoupling placement from broader switcher hot-loop and generic current-carrying lanes

## Extraction Notes

- Safe for guarded statements that local decoupling works best when the capacitor stays close to the device or power-pin region being decoupled.
- Safe for wording that increasing the current-path distance increases mounting inductance and weakens the local transient-current path.
- Do not use this section for universal capacitor ladders, exact capacitor geometry, or any per-rail implementation closure.

## Refresh Notes

- Refresh before reuse if the AMD guide revision or section anchor changes.
