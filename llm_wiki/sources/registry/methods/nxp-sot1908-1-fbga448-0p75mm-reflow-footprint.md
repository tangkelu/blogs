---
source_id: "nxp-sot1908-1-fbga448-0p75mm-reflow-footprint"
title: "FBGA448, fine-pitch ball grid array package, 448 terminals, 0.75 mm pitch, 17 mm x 17 mm x 2.46 mm body"
organization: "NXP Semiconductors"
owner: "NXP Semiconductors"
source_type: "manufacturer_package_information_pdf"
url: "https://www.nxp.com/docs/en/package-information/SOT1908-1.pdf"
jurisdiction: "global"
published_at: "2019-06-28"
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "stable"
must_refresh: false
original_source_language: "en"
authority_class: "manufacturer_package_information_pdf"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_bga_reflow_footprint_pages"
source_origin_path: "official NXP package-information PDF"
source_page_range: "package identity title plus pages 2 to 4 reflow soldering footprint parts 1 to 3"
confidence: "medium"
topic_tags: ["nxp", "fbga448", "sot1908-1", "0.75-mm-pitch", "reflow-footprint", "exact-data", "third-owner"]
status: "active"
notes: "Official NXP package-information PDF. Safe for the named FBGA448 / SOT1908-1 package only. Page-image verification safely proves the package identity, 0.75 mm pitch, and visible reflow-footprint geometry values such as 448X φ0.45, 448X φ0.35, 27X 0.75, and recommended stencil thickness 0.125. Do not convert this owner-scoped footprint set into a universal cross-vendor 0.75 mm pitch-to-pad rule."
---

# Source Summary

## What It Covers

- NXP package information PDF for `SOT1908-1`
- printed package identity for `FBGA448`
- printed package pitch `0.75 mm`
- visible `Reflow soldering footprint part 1`, `part 2`, and `part 3` pages for the same named package

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` one current-public third-owner exact-data route for the `0.75 mm` package residual lane, beyond the existing `Microchip + Renesas` stack
- Strengthens the lane from `two-owner exact-data coverage` to `three-owner exact-data coverage` without pretending that a universal `0.75 mm` geometry law now exists

## Extraction Notes

- Safe for the printed package identity:
  - `FBGA448`
  - `SOT1908-1`
- Safe for the printed package pitch and body statement:
  - `0.75 mm pitch`
  - `17 mm x 17 mm x 2.46 mm body`
- Safe for the visible reflow-footprint page wording:
  - `Reflow soldering footprint part 1`
  - `Reflow soldering footprint part 2`
  - `Reflow soldering footprint part 3`
- Safe for the visible page-scoped geometry values:
  - `448X φ0.45`
  - `448X φ0.35`
  - `27X 0.75`
  - `recommended stencil thickness: 0.125`
- Do not relabel unlabeled geometry beyond the visible page wording and value context
- Do not rewrite this owner-scoped footprint set into a generic `0.75 mm pitch -> pad diameter` rule

## Refresh Notes

- Stable package-information PDF; refresh only if a later prompt needs a newer NXP revision or broader third-owner `0.75 mm` coverage
- Preserve the named package `FBGA448 / SOT1908-1` scope whenever reusing any value
