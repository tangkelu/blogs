---
source_id: "microchip-ac243-csp-pcb-design-guidelines"
title: "AC243: Assembly and PCB Layout Guidelines for Chip-Scale Packages"
organization: "Microchip Technology"
owner: "Microchip Technology"
source_type: "manufacturer_application_note"
url: "https://ww1.microchip.com/downloads/aemdocuments/documents/fpga/ApplicationNotes/ApplicationNotes/microsemi_assembly_and_pcb_layout_guidelines_for_chip_scale_packages_applicationnote_ac243_v4.pdf"
jurisdiction: "global"
published_at: "2016-06"
checked_at: "2026-05-07"
retrieved_at: "2026-05-07"
trust_tier: "t1"
stability: "stable"
must_refresh: false
original_source_language: "en"
authority_class: "manufacturer_application_note"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_csp_bga_board_layout_guidelines"
source_origin_path: "official Microchip application note PDF"
source_page_range: "Tables 3 and 4 on PDF pages 17 to 18"
confidence: "medium"
topic_tags: ["microchip", "microsemi", "csp", "bga", "0.4-mm-pitch", "0.5-mm-pitch", "0.8-mm-pitch", "solder-land-diameter", "board-layout"]
status: "active"
notes: "Official Microchip application note. Safe for named CSP package board-layout guideline rows only. Do not convert these CSP-specific solder-land dimensions into a universal BGA pitch-to-pad rule."
---

# Source Summary

## What It Covers

- Microchip publishes `Table 3` for `0.4 mm to 0.5 mm pitch BGA package` CSPs
- Microchip publishes `Table 4` for `0.8 mm pitch BGA package` CSPs
- the tables include package names plus `Solder Land Diameter`, `Solder Mask Opening Diameter`, `Solder Ball Land Pitch`, and routing-related geometry

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` an official replacement path for the handbook's `0.4` and `0.5` pitch classes
- Adds another official `0.8 mm` package-scoped reference so the corpus does not rely on a single owner for this pitch class

## Extraction Notes

- Safe for Microchip's package-scoped `Solder Land Diameter (SL)` rows:
  - `uC81`: pitch `0.40`, `SL 0.23`
  - `CS81`, `CS121`, `CS196`, `CS201`, `CS281`, `FCS325`: pitch `0.50`, `SL 0.25`
  - `CS49`, `CS128`, `CS180`: pitch `0.80`, `SL 0.30`
  - `VF400`: pitch `0.80`, `SL 0.40`
- Safe for the board-layout note that:
  - `0.8 mm to 0.5 mm` pitch recommends dog-bone style land pad layout
  - `0.4 mm` pitch uses via in pad
- Do not rewrite these rows into a generic all-package BGA conversion table

## Refresh Notes

- Stable PDF; refresh only if a later prompt needs current package-family or current process guidance beyond these printed package rows
- Preserve the named package scope when reusing any values
