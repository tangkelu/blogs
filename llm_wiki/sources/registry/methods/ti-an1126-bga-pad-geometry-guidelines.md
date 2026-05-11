---
source_id: "ti-an1126-bga-pad-geometry-guidelines"
title: "AN-1126 BGA (Ball Grid Array)"
organization: "Texas Instruments"
owner: "Texas Instruments"
source_type: "manufacturer_application_note"
url: "https://www.ti.com/lit/pdf/snoa021"
jurisdiction: "global"
published_at: "2004-05"
checked_at: "2026-05-07"
retrieved_at: "2026-05-07"
trust_tier: "t1"
stability: "stable"
must_refresh: false
original_source_language: "en"
authority_class: "manufacturer_application_note"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_bga_pad_geometry_guidelines"
source_origin_path: "official TI application note PDF"
source_page_range: "Table 1 on PDF page 8"
confidence: "medium"
topic_tags: ["ti", "bga", "pad-geometry", "pcb-pad-diameter", "nsmd", "smd", "1.27-mm-pitch", "1.0-mm-pitch", "land-pattern"]
status: "active"
notes: "Official TI application note. Safe for TI's printed pad-geometry guideline rows for 1.27 mm and 1.0 mm pitch BGA under NSMD and SMD land-pattern framing only. Do not convert these rows into a generic all-vendor BGA table."
---

# Source Summary

## What It Covers

- TI publishes `Table 1. Guidelines for PCB Pad Design`
- the table covers `1.27 mm pitch` and `1.0 mm pitch`
- the table distinguishes `NSMD` and `SMD`
- the table prints solder ball diameter, PCB pad diameter, and solder mask opening diameter

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` a second primary-source replacement path for the handbook `BGA pitch-to-pad-diameter` pressure
- Specifically closes the `1.27 mm` pitch gap that remained uncovered after `P4-250`

## Extraction Notes

- Safe for TI's printed `1.27 mm` pitch rows:
  - `NSMD` PCB pad diameter `0.64 mm`
  - `SMD` PCB pad diameter `0.78 mm`
- Safe for TI's printed `1.0 mm` pitch rows:
  - `NSMD` PCB pad diameter `0.46 mm`
  - `SMD` PCB pad diameter `0.60 mm`
- Safe for the note that TI prefers `NSMD`
- Do not rewrite this source into a universal `pitch -> pad diameter` rule without preserving TI's `NSMD/SMD` framing

## Refresh Notes

- Stable PDF; refresh only if later prompts need current package-family or process-specific guidance beyond these printed pad-geometry rows
- Preserve the `NSMD` versus `SMD` distinction whenever reusing values
