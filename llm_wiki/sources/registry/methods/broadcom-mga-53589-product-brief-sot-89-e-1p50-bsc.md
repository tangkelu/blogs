---
source_id: "broadcom-mga-53589-product-brief-sot-89-e-1p50-bsc"
title: "MGA-53589 Product Brief"
organization: "Broadcom"
owner: "Broadcom"
source_type: "manufacturer_product_brief_pdf"
url: "https://docs.broadcom.com/wcs-public/products/data-sheets--technical-specifications/product-brief/237/316/av02-1308en.pdf"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-12"
retrieved_at: "2026-05-12"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_product_brief_pdf"
exact_data_class: "boundary_convention"
scope_type: "owner_scoped_non_bga_pitch_identity_without_same_surface_geometry"
source_origin_path: "official Broadcom product brief PDF"
source_page_range: "package table with `e = 1.50 BSC` and package context"
confidence: "medium"
topic_tags: ["broadcom", "avago", "sot-89", "pitch", "1.50-bsc", "package-context", "false-positive-filter"]
status: "active"
notes: "Official Broadcom product brief. Safe only for the owner-scoped non-BGA pitch identity `e = 1.50 BSC` on the SOT-89 package surface. Do not convert this pitch identity into a BGA/CSP `1.50 mm` reopen or a same-surface PCB land-pattern authority."
---

# Source Summary

## What It Covers

- Broadcom owner product brief for MGA-53589
- package-table pitch identity `e = 1.50 BSC`
- SOT-89 package context

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` one concrete owner-scoped pitch-identity false-positive filter
- Preserves the distinction between a real `1.50 BSC` package pitch on a non-target package surface and the current `1.50 mm` BGA/CSP residual

## Extraction Notes

- Safe for the visible owner-scoped pitch statement `e = 1.50 BSC`
- Safe for the SOT-89 package context
- Not safe for same-surface PCB land-pattern geometry
- Not safe for BGA/CSP `1.50 mm` reopen

## Refresh Notes

- Refresh before publication if exact Broadcom revision or package-family context matters
- Preserve the non-BGA scope whenever reusing this source
