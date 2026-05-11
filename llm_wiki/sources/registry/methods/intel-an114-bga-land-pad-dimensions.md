---
source_id: "intel-an114-bga-land-pad-dimensions"
title: "AN 114: Surface Land Pad Dimension"
organization: "Intel"
owner: "Intel"
source_type: "manufacturer_official_docs"
url: "https://www.intel.co.jp/content/www/jp/ja/docs/programmable/683481/current/surface-land-pad-dimension"
jurisdiction: "global"
published_at: "2018-10-09"
checked_at: "2026-05-08"
retrieved_at: "2026-05-08"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "ja"
authority_class: "manufacturer_official_docs"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_bga_land_pad_guidelines"
source_origin_path: "official Intel localized documentation page for AN 114"
source_page_range: "section 1.3.1 Surface Land Pad Dimension"
confidence: "medium"
topic_tags: ["intel", "bga", "vbga", "wlcsp", "mbga", "ubga", "land-pad", "nsmd", "smd", "package-layout"]
status: "active"
notes: "Official Intel documentation page for AN 114 surface land pad guidance. Safe for Intel's printed BGA/VBGA land-pad recommendation rows only. Do not convert these Intel package-scoped rows into a universal cross-vendor pitch-to-pad rule."
---

# Source Summary

## What It Covers

- Intel's AN 114 section on `Surface Land Pad Dimension`
- recommended `SMD` and `NSMD` pad sizes for multiple Intel BGA package classes
- a separate `0.4 mm VBGA (WLCSP)` recommendation table

## Why It Matters

- Adds one more official package-owner route for BGA land-pad geometry inside the `PCB资料` package lane.
- Strengthens the current exact-geometry replacement surface with an official `0.4 mm VBGA/WLCSP` row and additional Intel-scoped BGA examples.

## Extraction Notes

- Safe for Intel's printed rows such as:
  - `1.27 mm` PBGA / SBGA / TBGA
  - `1.00 mm` wire-bond and flip-chip
  - `0.80 mm` UBGA
  - `0.50 mm` MBGA
  - `0.4 mm` VBGA / WLCSP
- Safe for Intel's printed distinction that `SMD` pads should match the BGA pad size and `NSMD` pads should be about `15%` smaller in this documented guidance context.
- Do not rewrite these rows into a generic all-package or all-vendor BGA conversion table.
- Do not treat this localized Intel document as a standards-owner source.

## Refresh Notes

- Refresh before publication if a draft depends on current Intel package families, current routing examples, or current AN 114 wording.
- Preserve Intel package-family framing and the `SMD/NSMD` distinction whenever reusing values.
