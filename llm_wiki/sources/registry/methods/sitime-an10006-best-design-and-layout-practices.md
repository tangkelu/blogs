---
source_id: "sitime-an10006-best-design-and-layout-practices"
title: "AN10006 Best Design and Layout Practices"
organization: "SiTime"
owner: "SiTime"
source_type: "application_note"
url: "https://www.sitime.com/support/resource-library/application-notes/an10006-best-design-and-layout-practices"
jurisdiction: "global"
published_at: "2013-12-09"
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_application_note"
exact_data_class: "method_boundary"
scope_type: "vendor_scoped_clock_and_oscillator_layout_guidance"
source_origin_path: "official SiTime application note layout recommendations for clocks and oscillators"
source_page_range: "general layout techniques and layout recommendations for single-ended clocks"
confidence: "medium"
topic_tags: ["sitime", "clock", "oscillator", "series-termination", "short-trace", "ground-plane", "layout"]
status: "active"
notes: "Official SiTime application note. Safe for guarded wording that the clock source should stay close to the load, clock traces should be short, source-end series termination should be placed near the oscillator output when needed, noisy regions and board edges should be avoided, passive pads on clock traces should avoid branching, and multilayer boards should use a continuous ground plane under signal layers. Do not use it for exact impedance values, exact spacing numbers, or oscillator-performance guarantees."
---

# Source Summary

## What It Covers

- general PCB layout techniques for clock and oscillator devices
- short/direct clock routing and proximity between source and load
- source-end series termination placement for single-ended clocks
- avoid noisy board-edge or high-current modulated regions
- continuous ground-plane recommendation under signal layers in multilayer boards

## Why It Matters

- gives the `194页 handbook` `D5 clock-routing` lane a more direct owner-backed oscillator source than a generic processor board guide alone

## Extraction Notes

- Safe for guarded statements that clock source chips should be located close to the load and that shorter clock paths reduce emissions.
- Safe for wording that source-series termination should be placed close to the oscillator or resonator output when used for single-ended clocks.
- Safe for wording that clock traces should avoid unnecessary bends or branching and should avoid noisy or board-edge regions.
- Safe for wording that multilayer boards should use a continuous ground plane under signal layers for short return paths.
- Do not use this source for exact impedance targets, exact resistor values, or proof of jitter, SI, or EMC outcomes.

## Refresh Notes

- Refresh before publication if exact section wording or PDF revision matters.
