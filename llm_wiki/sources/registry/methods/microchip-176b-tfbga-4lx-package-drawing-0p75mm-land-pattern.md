---
source_id: "microchip-176b-tfbga-4lx-package-drawing-0p75mm-land-pattern"
title: "176-Ball Thin Fine Pitch Ball Grid Array (4LX) - 11x11 mm Body [TFBGA]"
organization: "Microchip Technology"
owner: "Microchip Technology"
source_type: "manufacturer_package_drawing"
url: "https://ww1.microchip.com/downloads/en/DeviceDoc/176B_TFBGA_11x11x1_19mm_4LX_C04-00481a.pdf"
jurisdiction: "global"
published_at: "2019"
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
source_page_range: "Sheet 1 dimension table and Sheet 2 recommended land pattern"
confidence: "medium"
topic_tags: ["microchip", "tfbga", "bga", "0.75-mm-pitch", "recommended-land-pattern", "contact-pad-diameter", "named-package", "package-drawing"]
status: "active"
notes: "Official Microchip package drawing. Safe for the named 176-ball 4LX TFBGA package only. Do not convert this owner-scoped 0.75 mm land-pattern row into a universal cross-vendor or all-package pitch-to-pad rule."
---

# Source Summary

## What It Covers

- Microchip package drawing `C04-481 Rev A` for `176-Ball Thin Fine Pitch Ball Grid Array (4LX) - 11x11 mm Body [TFBGA]`
- one printed package-dimension table on `Sheet 1`
- one printed `RECOMMENDED LAND PATTERN` panel on `Sheet 2`

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` its first official owner-scoped replacement surface for part of the blocked handbook `0.75 mm` pitch pressure
- Keeps the replacement tied to a named package drawing instead of pretending `0.75 mm` pitch has one universal PCB pad rule

## Extraction Notes

- Safe for the printed package identity:
  - `176-Ball Thin Fine Pitch Ball Grid Array (4LX) - 11x11 mm Body [TFBGA]`
- Safe for the printed package pitch:
  - `0.75 BSC`
- Safe for the printed `RECOMMENDED LAND PATTERN` row:
  - `Contact Pad Diameter (X176) X 0.40`
- Safe for the printed package-mark boundary note:
  - `Pin 1 visual index feature may vary, but must be located within the hatched area.`
- Safe for the printed process note:
  - thermal vias, if used, should be filled or tented to avoid solder loss during reflow
- Do not rewrite this drawing into a generic `0.75 mm pitch -> pad diameter` law

## Refresh Notes

- Stable package drawing PDF; refresh only if a later prompt needs a newer Microchip revision or broader package-family coverage beyond this named package
- Preserve the package code `4LX`, the `176-ball` identity, and the owner-scoped drawing context whenever reusing any value
