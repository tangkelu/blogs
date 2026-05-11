---
source_id: "amd-ug112-bg225-bgg225-1p50mm-bga-footprint-row"
title: "Device Package User Guide"
organization: "AMD"
owner: "AMD"
source_type: "manufacturer_package_user_guide_pdf"
url: "https://docs.amd.com/v/u/en-US/ug112"
jurisdiction: "global"
published_at: "2012-05-14"
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "stable"
must_refresh: false
original_source_language: "en"
authority_class: "manufacturer_package_user_guide_pdf"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_bga_footprint_table_row"
source_origin_path: "official AMD-hosted UG112 legacy Xilinx package guide"
source_page_range: "page 87 Table 5-4 BG225/BGG225 row"
confidence: "medium"
topic_tags: ["amd", "xilinx", "bg225", "bgg225", "1.50-mm-pitch", "bga", "footprint-row", "exact-data"]
status: "active"
notes: "Official AMD-hosted package guide. Safe for the printed BG225 / BGG225 row only. Use as a current-public third-owner exact row for the named 1.50 mm package context. Do not convert this owner-scoped row into a universal cross-vendor 1.50 mm pitch-to-land-pattern rule."
---

# Source Summary

## What It Covers

- AMD-hosted `UG112 Device Package User Guide`
- printed package row `BG225 / BGG225`
- printed `Pitch 1.50`
- same-table footprint geometry values for the same package row

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` a third materially independent current-public owner exact row for the still-open `1.50 mm` package lane
- Raises the local `1.50 mm` ceiling above `NXP exact row + Renesas named-package drawing + Renesas exact row`

## Extraction Notes

- Safe for the printed named package row:
  - `BG225`
  - `BGG225`
- Safe for the printed pitch value:
  - `1.50`
- Safe for the printed same-table geometry values:
  - `Component Land 0.63`
  - `Solder Land (NSMD) 0.58`
  - `Stencil Opening 0.68`
  - `Line Width 0.300`
  - `Distance 1.06`
  - `Via Land 0.65`
  - `Through Hole 0.356`
- Do not rewrite this source into a generic cross-vendor `1.50 mm` BGA footprint law

## Refresh Notes

- Stable AMD-hosted package guide; refresh only if a later prompt needs a newer AMD-hosted package-guide revision or broader `1.50 mm` owner coverage
- Preserve the printed `BG225 / BGG225` package-row scope whenever reusing any geometry
