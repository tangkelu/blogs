---
source_id: "renesas-bga-lga-mount-pad-dimensions-common-pitches"
title: "BGA,LGA MOUNT PAD DIMENSIONS"
organization: "Renesas Electronics"
owner: "Renesas Electronics"
source_type: "manufacturer_package_mount_pad_pdf"
url: "https://www.renesas.com/en/document/cpt/mount-pad-bga-lga-fig0013e"
jurisdiction: "global"
published_at: "2013"
checked_at: "2026-05-10"
retrieved_at: "2026-05-10"
trust_tier: "t1"
stability: "stable"
must_refresh: false
original_source_language: "en"
authority_class: "manufacturer_package_mount_pad_pdf"
exact_data_class: "vendor_scoped_exact_data"
scope_type: "vendor_scoped_bga_lga_mount_pad_pitch_rows"
source_origin_path: "official Renesas one-page mount pad dimensions PDF"
source_page_range: "single page"
confidence: "medium"
topic_tags: ["renesas", "bga", "lga", "mount-pad", "1.50-mm-pitch", "1.27-mm-pitch", "0.75-mm-pitch", "exact-data"]
status: "active"
notes: "Official Renesas one-page mount-pad table for common BGA/LGA lead pitches. Safe for the printed pitch rows and corresponding mount-pad diameter ranges only when the Renesas document context stays attached. Do not convert these rows into a universal cross-vendor pitch-to-pad law."
---

# Source Summary

## What It Covers

- Renesas one-page `BGA,LGA Mount Pad Dimensions` table
- lead-pitch rows from `1.50` through `0.40` mm
- one corresponding printed mount-pad diameter range row

## Why It Matters

- gives the `PCB资料` package residual lane a second current-public owner exact row for `1.50 mm`, stronger than the earlier Renesas named-package drawing that only exposed `e = 1.50`

## Extraction Notes

- Safe for the directly visible page wording:
  - `BGA,LGA Mount Pad Dimensions`
  - `Lead pitch(mm) 1.50 1.27 1.00 0.80 0.75 0.65 0.50 0.40`
  - `φ (mm) 0.55 to 0.65 0.55 to 0.65 0.45 to 0.55 0.35 to 0.45 0.25 to 0.35 0.30 to 0.40 0.20 to 0.30 0.15 to 0.25`
  - the note that mount-pad size should match package land diameter in this Renesas document context
- Not safe for:
  - all vendors
  - all BGA/LGA package families
  - package-library defaults outside Renesas document scope
  - any direct claim that this closes generic handbook `1.50 mm` or `0.75 mm` doctrine across vendors

## Refresh Notes

- Stable one-page PDF; refresh only if a later prompt needs newer Renesas revisions or package-family-specific exceptions.
