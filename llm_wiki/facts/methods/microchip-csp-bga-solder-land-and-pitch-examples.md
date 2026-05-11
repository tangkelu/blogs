---
fact_id: "methods-microchip-csp-bga-solder-land-and-pitch-examples"
title: "Microchip CSP BGA values are reusable only as named-package solder-land and pitch examples"
topic: "Microchip CSP BGA solder land and pitch examples"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-05-07"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_csp_bga_board_layout_guidelines"
canonical_unit_policy: "Preserve original Microchip millimeter values, package names, and column labels such as Solder Land Diameter, Solder Mask Opening Diameter, and Solder Ball Land Pitch. Do not normalize these rows into a universal BGA pitch-to-pad table."
source_ids:
  - "microchip-ac243-csp-pcb-design-guidelines"
tags: ["microchip", "microsemi", "csp", "bga", "solder-land-diameter", "0.4-mm-pitch", "0.5-mm-pitch", "0.8-mm-pitch", "exact-data"]
---

# Canonical Summary

> Microchip's `AC243` is strong enough to support one narrow exact-data layer for `C2-R1`: the local corpus may reuse named-package CSP/BGA board-layout rows that tie package names and ball pitch to package-scoped `Solder Land Diameter` values. This card is a vendor-scoped named-package example only. It does not authorize the handbook's generic `pitch -> pad diameter` table as a universal industry rule.

## Exact Data Scope

- exact for:
  - Microchip's printed `Table 3` and `Table 4` rows
  - the named package examples
  - the printed `Solder Land Diameter`, `Solder Mask Opening Diameter`, and `Solder Ball Land Pitch` values
- not exact for:
  - all BGA packages at the same pitch
  - handbook `MIN / MAX / recommended` framing
  - cross-vendor universal conversion rules
  - package-library defaults outside the named CSP examples

## Admitted Data

- Microchip prints these `0.4 mm to 0.5 mm pitch` CSP package examples in `Table 3`:
  - `uC81`:
    - `Solder Land Diameter` `0.23`
    - `Solder Mask Opening Diameter` `0.33`
    - `Solder Ball Land Pitch` `0.40`
  - `CS81`, `CS121`, `CS196`, `CS201`, `CS281`, and `FCS325`:
    - `Solder Land Diameter` `0.25`
    - `Solder Mask Opening Diameter` `0.35`
    - `Solder Ball Land Pitch` `0.50`
- Microchip prints these `0.8 mm pitch` CSP package examples in `Table 4`:
  - `CS49`, `CS128`, `CS180`:
    - `Solder Land Diameter` `0.30`
    - `Solder Mask Opening Diameter` `0.45`
    - `Solder Ball Land Pitch` `0.80`
  - `VF400`:
    - `Solder Land Diameter` `0.40`
    - `Solder Mask Opening Diameter` `0.50`
    - `Solder Ball Land Pitch` `0.80`
- Microchip states:
  - `0.8 mm to 0.5 mm` land pitch recommends dog-bone style land pad layout
  - `0.4 mm` land pitch uses via in pad

## Conditions And Methods

- Treat this card as a package-scoped board-layout guideline set for Microchip CSPs.
- Keep every value attached to the named package row and printed column.
- Use this card when a prompt needs real official `0.4`, `0.5`, or `0.8` package-scoped BGA/CSP land data and can stay inside package-owner scope.
- Pair this card with:
  - [nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md](/code/blogs/llm_wiki/facts/methods/nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md)
  - [ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md](/code/blogs/llm_wiki/facts/methods/ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md)

## Limits And Non-Claims

- This card does not authorize a universal `BGA pitch -> pad diameter` table.
- It does not authorize handbook `1.50 mm` or `0.75 mm` pitch rows.
- It does not authorize direct equivalence between `Solder Land Diameter` here and every other vendor's `PCB pad diameter` terminology without preserving the source framing.
- It does not authorize routing-yield or manufacturability guarantees beyond the printed package guidance.

## Relationship To Local PCB资料 Intake

- This card gives primary-source support for the handbook's `0.40`, `0.50`, and part of the `0.80` pitch pressure.
- Together with `P4-250` and `P4-251`, the local batch now has primary-source-backed examples for:
  - `1.27 mm`
  - `1.0 mm`
  - `0.8 mm`
  - `0.65 mm`
  - `0.5 mm`
  - `0.4 mm`
- `1.5 mm` and `0.75 mm` remain the main unreplaced handbook pitch classes.

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating secondary-PDF candidate:
  - `P4-215C2` page-28 `bga pitch-to-pad-diameter table`
- authority replacement used here:
  - official Microchip `AC243` `Table 3` and `Table 4`
- exact-data shape:
  - vendor-scoped named-package CSP/BGA board-layout examples

## Source Links

- https://ww1.microchip.com/downloads/aemdocuments/documents/fpga/ApplicationNotes/ApplicationNotes/microsemi_assembly_and_pcb_layout_guidelines_for_chip_scale_packages_applicationnote_ac243_v4.pdf
