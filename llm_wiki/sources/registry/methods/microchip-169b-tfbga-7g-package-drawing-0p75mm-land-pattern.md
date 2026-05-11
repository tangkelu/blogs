---
source_id: "microchip-169b-tfbga-7g-package-drawing-0p75mm-land-pattern"
title: "169-Ball Thin Fine Pitch Ball Grid Array (7G) - 10x10 mm Body [TFBGA]"
organization: "Microchip Technology"
owner: "Microchip Technology"
source_type: "manufacturer_package_drawing"
url: "https://ww1.microchip.com/downloads/en/DeviceDoc/169L_TFBGA_10x10_7G_C04-377C-J.pdf"
jurisdiction: "global"
published_at: "2017"
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
source_page_range: "package-dimension sheet and recommended land pattern sheet"
confidence: "medium"
topic_tags: ["microchip", "tfbga", "bga", "0.75-mm-pitch", "recommended-land-pattern", "contact-pad-diameter", "named-package", "package-drawing"]
status: "active"
notes: "Official Microchip package drawing. Safe for the named 169-ball 7G TFBGA package only. Do not convert this owner-scoped 0.75 mm land-pattern row into a universal cross-vendor or all-package pitch-to-pad rule."
---

# Source Summary

## What It Covers

- Microchip package drawing `C04-377 Rev J` for `169-Ball Thin Fine Pitch Ball Grid Array (7G) - 10x10 mm Body [TFBGA]`
- one printed package-identity and package-pitch surface
- one printed `RECOMMENDED LAND PATTERN` panel

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` a second official owner-scoped replacement surface for part of the blocked handbook `0.75 mm` pitch pressure
- Strengthens the route from `one Microchip named-package row exists` to `more than one owner-scoped Microchip row exists`, without pretending the whole `0.75 mm` pitch class is closed

## Extraction Notes

- Safe for the printed package identity:
  - `169-Ball Thin Fine Pitch Ball Grid Array (7G) - 10x10x1.10 mm Body [TFBGA]`
- Safe for the printed package pitch:
  - `0.75 BSC`
- Safe for the printed `RECOMMENDED LAND PATTERN` panel:
  - `Contact Pad Diameter (X169) b 0.35`
- Safe for the printed package-mark boundary note:
  - `Terminal A1 visual index feature may vary, but must be located within the hatched area.`
- Do not rewrite this drawing into a generic `0.75 mm pitch -> pad diameter` law

## Refresh Notes

- Stable package drawing PDF; refresh only if a later prompt needs a newer Microchip revision or broader package-family coverage beyond this named package
- Preserve the package code `7G`, the `169-ball` identity, and the owner-scoped drawing context whenever reusing any value
