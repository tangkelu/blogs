---
source_id: "analog-devices-exposed-pads-brief-introduction"
title: "Analog Devices Exposed Pads: A Brief Introduction"
organization: "Analog Devices"
owner: "Analog Devices"
source_type: "design_note"
url: "https://www.analog.com/en/resources/design-notes/2022/07/16/08/51/exposed-pads-a-brief-introduction.html"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_packaging_note"
exact_data_class: "method_boundary"
scope_type: "vendor_scoped_exposed_pad_thermal_and_electrical_role_guidance"
source_origin_path: "official Analog Devices exposed-pad design note"
source_page_range: "entire note"
confidence: "medium"
topic_tags: ["analog-devices", "exposed-pad", "exposed-paddle", "thermal", "ground", "electrical-path", "package"]
status: "active"
notes: "Official Analog Devices note. Safe for guarded wording that an exposed paddle primarily provides a thermal path and may also provide a low-impedance electrical path when the die attach is externally grounded. Do not use it as a universal claim that every exposed pad must tie to ground."
---

# Source Summary

## What It Covers

- exposed-paddle purpose in package construction
- thermal-path function from die to PCB
- conditional low-impedance electrical-path role when the die attach is externally grounded

## Why It Matters

- gives the corpus one current-public semiconductor-owner source that explicitly ties exposed-pad language to both local heat spreading and possible electrical grounding role
- adds the caution that the electrical role depends on package-specific internal grounding rather than on universal pad doctrine

## Extraction Notes

- Safe for guarded wording that an exposed pad or paddle often exists to move heat from the package into the PCB.
- Safe for wording that the same paddle may also provide a low-impedance electrical path when the package design externally grounds that die-attach region.
- Safe for wording that package-specific internal construction matters and must be checked before universalizing the net tie.
- Do not use this note for universal `EPAD = GND` doctrine, exact via-array recipes, paste-window geometry, or thermal-performance guarantees.

## Refresh Notes

- Refresh before reuse if Analog Devices revises the page or relocates the note.
