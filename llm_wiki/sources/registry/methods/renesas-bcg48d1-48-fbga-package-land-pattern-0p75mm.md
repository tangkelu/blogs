---
source_id: "renesas-bcg48d1-48-fbga-package-land-pattern-0p75mm"
title: "48-FBGA, Package Land Pattern 10.0 x 10.0 x 1.27 mm Body, 0.75mm Pitch BCG48D1"
organization: "Renesas Electronics"
owner: "Renesas Electronics"
source_type: "manufacturer_package_land_pattern_pdf"
url: "https://www.renesas.com/us/en/document/psc/48-fbga-package-land-pattern-100-x-100-x-127-mm-body075mm-pitch-bcg48d1"
jurisdiction: "global"
published_at: "2022-07-12"
checked_at: "2026-05-10"
retrieved_at: "2026-05-10"
trust_tier: "t1"
stability: "stable"
must_refresh: false
original_source_language: "en"
authority_class: "manufacturer_package_land_pattern_pdf"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_bga_land_pattern_document"
source_origin_path: "official Renesas package land-pattern PDF"
source_page_range: "single-page land-pattern document title surface"
confidence: "medium"
topic_tags: ["renesas", "fbga", "bga", "0.75-mm-pitch", "package-land-pattern", "named-package", "bcg48d1", "second-owner"]
status: "active"
notes: "Official Renesas named-package land-pattern document. Direct text extraction plus page-image verification safely prove the document class, package identity, 0.75 mm pitch, visible recommended land-pattern geometry labels, and the printed note context. Do not convert this owner-scoped row into a universal cross-vendor 0.75 mm pitch-to-pad rule."
---

# Source Summary

## What It Covers

- Renesas single-page package land-pattern document for `BCG48D1`
- printed named-package identity `48-FBGA`
- printed body size `10.0 x 10.0 x 1.27 mm Body`
- printed package pitch `0.75mm Pitch`
- visible recommended land-pattern geometry values including `0.300`, `0.75`, `3.750`, `5.25`, and `10.000`
- visible note context tying the page to `RECOMMENDED LAND PATTERN DIMENSION`, `IPC-7351B Generic`, and `SMD pattern assumed`

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` its first directly verified current-public second-owner `0.75 mm` named-package land-pattern document above the prior `three Microchip owner-scoped rows` ceiling
- Strengthens the package residual lane from `single-vendor repetition` to `multi-owner named-package route availability`

## Extraction Notes

- Safe for the directly extracted header text:
  - `48-FBGA, Package Land Pattern`
  - `10.0 x 10.0 x 1.27 mm Body`
  - `0.75mm Pitch`
  - `BCG48D1`
- Safe for the visible recommended land-pattern page content:
  - `RECOMMENDED LAND PATTERN DIMENSION`
  - visible geometry values `0.300`, `0.75`, `3.750`, `5.25`, and `10.000`
  - `ALL DIMENSIONS ARE IN MM. ANGLES IN DEGREES.`
  - `LAND PATTERN RECOMMENDATION PER IPC-7351B GENERIC`
  - `SMD PATTERN ASSUMED`
- Safe for the document identity:
  - `PSC-4867-02, Rev 00, Page 1`
- Not safe for:
  - unlabeled interpretation beyond the visible page geometry and note context
  - universal `0.75 mm pitch -> pad diameter` reuse
  - cross-vendor defaulting beyond the named `BCG48D1` package document

## Refresh Notes

- Stable named-package PDF; refresh only if a later prompt needs a newer Renesas revision or broader second-owner `0.75 mm` coverage
- Preserve the package code `BCG48D1`, the `48-FBGA` identity, and the owner-scoped document context whenever reusing this route
