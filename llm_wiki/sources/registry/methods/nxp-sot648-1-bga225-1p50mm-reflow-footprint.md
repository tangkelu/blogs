---
source_id: "nxp-sot648-1-bga225-1p50mm-reflow-footprint"
title: "SOT648-1 plastic ball grid array package; 225 balls; body 27 x 27 x 1.55 mm"
organization: "NXP Semiconductors"
owner: "NXP Semiconductors"
source_type: "manufacturer_package_information_pdf"
url: "https://www.nxp.com/docs/en/package-information/SOT648-1.pdf"
jurisdiction: "global"
published_at: "2016-02-08"
checked_at: "2026-05-10"
retrieved_at: "2026-05-10"
trust_tier: "t1"
stability: "stable"
must_refresh: false
original_source_language: "en"
authority_class: "manufacturer_package_information_pdf"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_bga_outline_and_reflow_footprint"
source_origin_path: "official NXP package-information PDF"
source_page_range: "page 2 package outline and page 3 soldering footprint"
confidence: "medium"
topic_tags: ["nxp", "bga225", "sot648-1", "1.50-mm-pitch", "reflow-footprint", "named-package", "land-pattern"]
status: "active"
notes: "Official NXP package-information PDF. Safe for the named BGA225 / SOT648-1 package only. Do not convert this owner-scoped 1.50 mm reflow footprint into a universal cross-vendor pitch-to-pad rule."
---

# Source Summary

## What It Covers

- NXP package information PDF for `SOT648-1`
- printed package outline for `BGA225`
- printed package pitch symbol `e` at `1.5`
- printed reflow soldering footprint geometry row for the same named package

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` its first directly verified current-public owner-scoped `1.50 mm` named-package exact-geometry route above the prior `IEC existence + AN1231 near-hit` ceiling
- Replaces the residual `1.50 mm` lane's status from `no clean public exact row in hand` to `one named-package current-public exact row landed`

## Extraction Notes

- Safe for the printed named package identity:
  - `BGA225`
  - `SOT648-1`
- Safe for the printed package outline pitch:
  - `e = 1.5`
- Safe for the printed reflow footprint row:
  - `P 1.50`
  - `SL 0.750`
  - `SP 0.650`
  - `SR 0.900`
  - `Hx 27.500`
  - `Hy 27.500`
- Safe for the printed figure identity:
  - `Reflow soldering footprint for BGA225 (SOT648-1)`
- Do not rewrite this source into a generic cross-vendor `1.50 mm pitch -> one land pattern` law

## Refresh Notes

- Stable package-information PDF; refresh only if a later prompt needs a newer NXP revision or broader 1.50 mm package coverage
- Preserve the named package `BGA225 / SOT648-1` scope whenever reusing any geometry
