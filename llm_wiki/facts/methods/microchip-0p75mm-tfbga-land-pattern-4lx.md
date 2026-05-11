---
fact_id: "methods-microchip-0p75mm-tfbga-land-pattern-4lx"
title: "Microchip 0.75 mm TFBGA values are reusable only as the named 176-ball 4LX package drawing and land-pattern row"
topic: "Microchip 0.75 mm TFBGA land pattern for the named 176-ball 4LX package"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-05-08"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_bga_land_pattern_drawing"
canonical_unit_policy: "Preserve original Microchip millimeter values, package identity, and drawing labels such as 0.75 BSC and Contact Pad Diameter. Do not normalize this drawing into a universal 0.75 mm pitch conversion table."
source_ids:
  - "microchip-176b-tfbga-4lx-package-drawing-0p75mm-land-pattern"
tags: ["microchip", "tfbga", "bga", "0.75-mm-pitch", "contact-pad-diameter", "land-pattern", "pin-1-index", "exact-data"]
---

# Canonical Summary

> Microchip's `176-Ball Thin Fine Pitch Ball Grid Array (4LX)` package drawing is strong enough to support one narrow exact-data layer for the `PCB资料` package lane: the local corpus may reuse this named-package `0.75 mm` pitch row and printed `RECOMMENDED LAND PATTERN` data when the package identity and drawing context stay attached. This card is a vendor-scoped named-package drawing only. It does not authorize a universal `0.75 mm pitch -> pad diameter` rule.

## Exact Data Scope

- exact for:
  - Microchip's printed `176-Ball Thin Fine Pitch Ball Grid Array (4LX) - 11x11 mm Body [TFBGA]` drawing
  - the printed `0.75 BSC` pitch for this named package
  - the printed `RECOMMENDED LAND PATTERN` value `Contact Pad Diameter (X176) X 0.40`
  - the printed package-mark boundary note for the `pin 1 visual index feature`
- not exact for:
  - all `0.75 mm` BGA or TFBGA packages
  - cross-vendor BGA land-pattern defaults
  - handbook `MIN / MAX / recommended` generic framing
  - residual `1.50 mm` pitch replacement

## Admitted Data

- Microchip prints this named package identity:
  - `176-Ball Thin Fine Pitch Ball Grid Array (4LX) - 11x11 mm Body [TFBGA]`
- Microchip prints this package pitch:
  - `0.75 BSC`
- Microchip prints this `RECOMMENDED LAND PATTERN` value:
  - `Contact Pad Diameter (X176) X 0.40`
- Microchip prints this package-mark boundary note:
  - `Pin 1 visual index feature may vary, but must be located within the hatched area.`
- Microchip prints this process note:
  - thermal vias, if used, should be filled or tented to avoid solder loss during reflow

## Conditions And Methods

- Treat this card as one owner-scoped package drawing for a named `176-ball` `4LX` TFBGA package.
- Keep the `0.75 BSC` pitch and `Contact Pad Diameter` value attached to the Microchip package identity and drawing context.
- Use this card when a prompt needs one safe official `0.75 mm` pitch replacement row and can stay inside named-package scope.
- Use this card to show that at least one official `0.75 mm` owner row exists without claiming that every `0.75 mm` package shares the same land-pattern geometry.
- Pair this card with:
  - [nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md](/code/blogs/llm_wiki/facts/methods/nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md)
  - [ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md](/code/blogs/llm_wiki/facts/methods/ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md)
  - [microchip-csp-bga-solder-land-and-pitch-examples.md](/code/blogs/llm_wiki/facts/methods/microchip-csp-bga-solder-land-and-pitch-examples.md)
  - [intel-bga-land-pad-guidelines-common-pitches-and-vbga.md](/code/blogs/llm_wiki/facts/methods/intel-bga-land-pad-guidelines-common-pitches-and-vbga.md)

## Limits And Non-Claims

- This card does not authorize a universal `0.75 mm` BGA conversion table.
- It does not authorize direct equivalence between this Microchip `Contact Pad Diameter` row and every other vendor's PCB pad terminology.
- It does not authorize package-library defaults outside the named `4LX` package drawing.
- It does not close the remaining `1.50 mm`, connector-origin, or installation-mark authority gaps.

## Relationship To Local PCB资料 Intake

- This card gives the package lane its first official owner-scoped replacement row for part of the handbook `0.75 mm` pitch pressure.
- It narrows the residual state from `0.75 mm completely unreplaced` to `0.75 mm partially replaced through one named-package Microchip route`.
- It still does not turn the blocked handbook table into a reusable generic pitch law.

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating secondary-PDF candidate:
  - `P4-215C2` page-28 `bga pitch-to-pad-diameter table`
- authority replacement used here:
  - official Microchip package drawing `176B_TFBGA_11x11x1_19mm_4LX_C04-00481a`
- exact-data shape:
  - vendor-scoped named-package BGA land-pattern drawing

## Source Links

- https://ww1.microchip.com/downloads/en/DeviceDoc/176B_TFBGA_11x11x1_19mm_4LX_C04-00481a.pdf
