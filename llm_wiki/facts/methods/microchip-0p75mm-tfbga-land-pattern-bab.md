---
fact_id: "methods-microchip-0p75mm-tfbga-land-pattern-bab"
title: "Microchip 0.75 mm TFBGA values are reusable only as the named 196-ball BAB package drawing and land-pattern row"
topic: "Microchip 0.75 mm TFBGA land pattern for the named 196-ball BAB package"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-05-08"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_bga_land_pattern_drawing"
canonical_unit_policy: "Preserve original Microchip millimeter values, package identity, and drawing labels such as 0.75 BSC and Contact Pad Diameter. Do not normalize this drawing into a universal 0.75 mm pitch conversion table."
source_ids:
  - "microchip-196b-tfbga-bab-package-drawing-0p75mm-land-pattern"
tags: ["microchip", "tfbga", "bga", "0.75-mm-pitch", "contact-pad-diameter", "land-pattern", "pin-1-index", "exact-data"]
---

# Canonical Summary

> Microchip's `196-Ball Thin Fine Pitch Ball Grid Array (BAB)` package drawing is strong enough to support one additional narrow exact-data layer for the `PCB资料` package lane: the local corpus may reuse this named-package `0.75 mm` pitch row and printed `RECOMMENDED LAND PATTERN` data when the package identity and drawing context stay attached. This card is a vendor-scoped named-package drawing only. It does not authorize a universal `0.75 mm pitch -> pad diameter` rule.

## Exact Data Scope

- exact for:
  - Microchip's printed `196-Ball Thin Fine Pitch Ball Grid Array (BAB) - 11x11 mm Body [TFBGA]` drawing
  - the printed `0.75 BSC` pitch for this named package
  - the printed `RECOMMENDED LAND PATTERN` value `Contact Pad Diameter (X196) X 0.35`
  - the printed package-mark boundary note for the `pin 1 visual index feature`
- not exact for:
  - all `0.75 mm` BGA or TFBGA packages
  - cross-vendor BGA land-pattern defaults
  - handbook `MIN / MAX / recommended` generic framing
  - residual `1.50 mm` pitch replacement

## Admitted Data

- Microchip prints this named package identity:
  - `196-Ball Thin Fine Pitch Ball Grid Array (BAB) - 11x11 mm Body [TFBGA]`
- Microchip prints this package pitch:
  - `0.75 BSC`
- Microchip prints this `RECOMMENDED LAND PATTERN` value:
  - `Contact Pad Diameter (X196) X 0.35`
- Microchip prints this package-mark boundary note:
  - `Pin 1 visual index feature may vary, but must be located within the hatched area.`

## Conditions And Methods

- Treat this card as one owner-scoped package drawing for a named `196-ball` `BAB` TFBGA package.
- Keep the `0.75 BSC` pitch and `Contact Pad Diameter` value attached to the Microchip package identity and drawing context.
- Use this card when a prompt needs another safe official `0.75 mm` pitch replacement row and can stay inside named-package scope.
- Use this card to show that at least three official `0.75 mm` owner rows exist in-repo without claiming that every `0.75 mm` package shares the same land-pattern geometry.
- Pair this card with:
  - [microchip-0p75mm-tfbga-land-pattern-4lx.md](/code/blogs/llm_wiki/facts/methods/microchip-0p75mm-tfbga-land-pattern-4lx.md)
  - [microchip-0p75mm-tfbga-land-pattern-7g.md](/code/blogs/llm_wiki/facts/methods/microchip-0p75mm-tfbga-land-pattern-7g.md)
  - [nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md](/code/blogs/llm_wiki/facts/methods/nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md)
  - [ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md](/code/blogs/llm_wiki/facts/methods/ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md)
  - [microchip-csp-bga-solder-land-and-pitch-examples.md](/code/blogs/llm_wiki/facts/methods/microchip-csp-bga-solder-land-and-pitch-examples.md)
  - [intel-bga-land-pad-guidelines-common-pitches-and-vbga.md](/code/blogs/llm_wiki/facts/methods/intel-bga-land-pad-guidelines-common-pitches-and-vbga.md)

## Limits And Non-Claims

- This card does not authorize a universal `0.75 mm` BGA conversion table.
- It does not authorize direct equivalence between this Microchip contact-pad row and every other vendor's PCB pad terminology.
- It does not authorize package-library defaults outside the named `BAB` package drawing.
- It does not close the remaining `1.50 mm`, connector-origin, or installation-mark authority gaps.

## Relationship To Local PCB资料 Intake

- This card gives the package lane a third official owner-scoped replacement row for part of the handbook `0.75 mm` pitch pressure.
- It narrows the residual state from `multiple owner rows exist` to `three owner-scoped Microchip rows exist`.
- It still does not turn the blocked handbook table into a reusable generic pitch law.

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating secondary-PDF candidate:
  - `P4-215C2` page-28 `bga pitch-to-pad-diameter table`
- authority replacement used here:
  - official Microchip package drawing `196B_TFBGA_11x11_[BAB]_C04-21141a`
- exact-data shape:
  - vendor-scoped named-package BGA land-pattern drawing

## Source Links

- https://ww1.microchip.com/downloads/en/DeviceDoc/196B_TFBGA_11x11_%5BBAB%5D_C04-21141a.pdf
