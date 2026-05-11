---
source_id: "microchip-196b-tfbga-bab-package-drawing-0p75mm-land-pattern"
title: "196-Ball Thin Fine Pitch Ball Grid Array (BAB) - 11x11 mm Body [TFBGA]"
organization: "Microchip Technology"
owner: "Microchip Technology"
source_type: "manufacturer_package_drawing"
url: "https://ww1.microchip.com/downloads/en/DeviceDoc/196B_TFBGA_11x11_%5BBAB%5D_C04-21141a.pdf"
jurisdiction: "global"
published_at: "2018"
checked_at: "2026-05-08"
retrieved_at: "2026-05-08"
trust_tier: "t1"
stability: "stable"
must_refresh: false
original_source_language: "en"
authority_class: "manufacturer_package_drawing"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_bga_land_pattern_drawing"
source_origin_path: "official Microchip package drawing PDF"
source_page_range: "sheet 2 pitch table and page 3 recommended land pattern"
confidence: "medium"
topic_tags: ["microchip", "tfbga", "bga", "0.75-mm-pitch", "recommended-land-pattern", "contact-pad-diameter", "named-package", "package-drawing"]
status: "active"
notes: "Official Microchip package drawing. Safe for the named 196-ball BAB TFBGA package only. Do not convert this owner-scoped 0.75 mm land-pattern row into a universal cross-vendor or all-package pitch-to-pad rule."
---

# Source Summary

## What It Covers

- Microchip package drawing `C04-21141 Rev A` for `196-Ball Thin Fine Pitch Ball Grid Array (BAB) - 11x11 mm Body [TFBGA]`
- one printed package pitch table
- one printed `RECOMMENDED LAND PATTERN` page

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` a third official owner-scoped replacement surface for part of the blocked handbook `0.75 mm` pitch pressure
- Strengthens the route from `multiple Microchip owner rows exist` to `three named-package owner rows exist`, without pretending the whole `0.75 mm` pitch class is closed

## Extraction Notes

- Safe for the printed package identity:
  - `196-Ball Thin Fine Pitch Ball Grid Array (BAB) - 11x11 mm Body [TFBGA]`
- Safe for the printed package pitch:
  - `0.75 BSC`
- Safe for the printed `RECOMMENDED LAND PATTERN` value:
  - `Contact Pad Diameter (X196) X 0.35`
- Safe for the printed package-mark boundary note:
  - `Pin 1 visual index feature may vary, but must be located within the hatched area.`
- Do not rewrite this drawing into a generic `0.75 mm pitch -> pad diameter` law

## Refresh Notes

- Stable package drawing PDF; refresh only if a later prompt needs a newer Microchip revision or broader package-family coverage beyond this named package
- Preserve the package code `BAB`, the `196-ball` identity, and the owner-scoped drawing context whenever reusing any value
