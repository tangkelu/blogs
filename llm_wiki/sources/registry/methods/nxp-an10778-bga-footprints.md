---
source_id: "nxp-an10778-bga-footprints"
title: "AN10778: PCB layout guidelines for NXP MCUs in BGA packages"
organization: "NXP Semiconductors"
owner: "NXP Semiconductors"
source_type: "manufacturer_application_note"
url: "https://www.nxp.com/docs/en/application-note/AN10778.pdf"
jurisdiction: "global"
published_at: "2011-04-15"
checked_at: "2026-05-07"
retrieved_at: "2026-05-07"
trust_tier: "t1"
stability: "stable"
must_refresh: false
original_source_language: "en"
authority_class: "manufacturer_application_note"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_bga_footprint_examples"
source_origin_path: "official NXP application note PDF"
source_page_range: "Table 2 on PDF page 6"
confidence: "medium"
topic_tags: ["nxp", "bga", "land-pattern", "footprint", "pcb-land-pad", "ball-pitch", "named-package", "package-layout"]
status: "active"
notes: "Official NXP application note. Safe for named-package BGA footprint example rows only. Do not convert these package-scoped values into a universal industry pitch-to-pad-diameter table."
---

# Source Summary

## What It Covers

- NXP publishes `Table 2. Recommended BGA footprints`
- the table includes named packages, ball pitch, ball diameter, BGA substrate land diameter, PCB land pad diameter, solder mask diameter, and package outline
- the table gives multiple package-scoped rows at `1.0 mm`, `0.8 mm`, `0.65 mm`, and `0.5 mm` ball pitch

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` a primary-source replacement path for part of the handbook's `BGA pitch-to-pad-diameter` table
- Lets the local corpus learn real BGA footprint numbers without pretending the secondary handbook table is universal authority

## Extraction Notes

- Safe for named-package rows such as:
  - `(L)BGA256`
  - `TFBGA100`
  - `TFBGA144`
  - `TFBGA180`
  - `TFBGA208`
  - `LFBGA208`
  - `LFBGA256`
  - `TFBGA296`
  - `LFBGA324`
  - `LFBGA320`
- Safe for the package-scoped pitch and PCB land pad diameter values printed in `Table 2`
- Safe for the distinction that the same pitch can map to more than one PCB land pad diameter depending on package family and routing context
- Do not rewrite this source into a generic cross-vendor `pitch -> pad diameter` law

## Refresh Notes

- This is a dated but stable PDF; refresh only if a later prompt needs current-package or current-process guidance beyond these printed example rows
- Preserve package names and NXP package-family scope when reusing any values
