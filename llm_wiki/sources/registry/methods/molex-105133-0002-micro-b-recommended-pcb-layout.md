---
source_id: "molex-105133-0002-micro-b-recommended-pcb-layout"
title: "Molex 105133-0001 / 105133-0002 Micro-USB B Receptacle Sales Drawing"
organization: "Molex"
owner: "Molex"
source_type: "manufacturer_sales_drawing"
url: "https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/salesdrawingpdf/105/105133/1051330002_sd.pdf"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-08"
retrieved_at: "2026-05-08"
trust_tier: "t1"
stability: "stable"
must_refresh: false
original_source_language: "en"
authority_class: "manufacturer_sales_drawing"
exact_data_class: "part_scoped_exact_data"
scope_type: "connector_owner_series_specific_layout_and_pin_numbering"
source_origin_path: "official Molex sales drawing PDF"
source_page_range: "single-page drawing with recommended PCB layout and pin assignment"
confidence: "medium"
topic_tags: ["molex", "micro-usb-b", "connector", "recommended-pcb-layout", "pin-1", "pin-numbering", "series-specific"]
status: "active"
notes: "Official Molex sales drawing. Safe for the named 105133 connector family only. Do not convert this series-specific recommended PCB layout into a universal connector-origin default."
---

# Source Summary

## What It Covers

- Molex `105133-0001` and `105133-0002` Micro-USB B receptacle drawing
- one printed `RECOMMENDED PCB LAYOUT (THICKNESS: 1.6mm)` panel
- printed `PIN 1` through `PIN 5` numbering plus pin assignment

## Why It Matters

- Gives the connector-origin lane one real connector-owner drawing rather than only CAD-library convention wording
- Supports the safe statement that connector orientation and pin numbering should come from the owner series drawing when the prompt is about a named connector family

## Extraction Notes

- Safe for the printed `RECOMMENDED PCB LAYOUT (THICKNESS: 1.6mm)` panel
- Safe for the printed numbering context `PIN 1` and `PIN 5`
- Safe for the printed pin assignment:
  - `1 VBUS`
  - `2 D-`
  - `3 D+`
  - `4 ID`
  - `5 GND`
- Safe for the fact that the drawing gives a connector-owner layout and numbering reference for this named series
- Do not rewrite this drawing into a universal left/right default for all connectors

## Refresh Notes

- Stable PDF drawing; refresh only if a later prompt depends on a current revision or a different Molex connector family
- Preserve the named Molex series scope whenever reusing any layout or numbering statement
