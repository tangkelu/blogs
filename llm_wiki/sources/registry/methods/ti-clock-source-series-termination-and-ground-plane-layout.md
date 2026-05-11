---
source_id: "ti-clock-source-series-termination-and-ground-plane-layout"
title: "TMS320C6472 Hardware Design Guide"
organization: "Texas Instruments"
owner: "Texas Instruments"
source_type: "hardware_design_guide"
url: "https://www.ti.com/lit/pdf/spraaq4"
jurisdiction: "global"
published_at: "2011-10"
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_hardware_design_guide"
exact_data_class: "method_boundary"
scope_type: "vendor_scoped_clock_layout_and_series_termination_guidance"
source_origin_path: "official TI hardware-design-guide clock-layout section"
source_page_range: "clocking and oscillator layout guidance section"
confidence: "medium"
topic_tags: ["texas-instruments", "clock", "series-termination", "ground-plane", "oscillator", "layout", "source-end"]
status: "active"
notes: "Official TI hardware design guide. Safe for guarded wording that series termination should be placed close to the clock source, clock traces should keep a solid GND reference plane underneath, and signal traces should not be routed near or under the clock source. Do not use it for exact distance limits, resistor values, or platform-specific timing closure."
---

# Source Summary

## What It Covers

- clocking and oscillator layout guidance in a processor hardware design guide
- source-end series termination placement
- solid ground-plane reference under clock traces
- keepout posture around the clock source or oscillator region

## Why It Matters

- gives the `194页 handbook` `D5 clock-routing` lane one current-public owner-backed source for the two clearest remaining clock-specific claims: `series termination close to source` and `clock-source keepout / solid GND reference`

## Extraction Notes

- Safe for guarded statements that a source-series termination element should be placed close to the clock source.
- Safe for wording that clock traces should keep a solid ground reference plane underneath.
- Safe for wording that other signal traces should not be routed near or under the clock source or oscillator region.
- Do not use this source for exact resistor values, exact spacing numbers, exact trace lengths, or device-specific timing guarantees.

## Refresh Notes

- Refresh before publication if exact TI revision or figure numbering matters.
