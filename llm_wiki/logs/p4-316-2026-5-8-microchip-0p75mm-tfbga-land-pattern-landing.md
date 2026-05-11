# P4-316 Microchip 0.75 mm TFBGA Land-Pattern Landing

Date: 2026-05-08
Parent lane: `P4-315`
Execution mode: `controller_owned_exact_data_landing`

## Purpose

Convert the `P4-315` scout result into one real official replacement surface for the package residual lane by landing the narrowest safe `0.75 mm` owner-scoped package drawing route.

## Inputs

- official Microchip package drawing `176B_TFBGA_11x11x1_19mm_4LX_C04-00481a.pdf`
- `logs/p4-315-2026-5-8-package-residual-authority-recovery.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

## What Landed

### New source record

- `sources/registry/methods/microchip-176b-tfbga-4lx-package-drawing-0p75mm-land-pattern.md`

### New exact-data fact card

- `facts/methods/microchip-0p75mm-tfbga-land-pattern-4lx.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

## What Landed Safely

- one official Microchip `0.75 BSC` named-package route
- one printed `RECOMMENDED LAND PATTERN` row with `Contact Pad Diameter (X176) X 0.40`
- one owner-scoped package-mark boundary note for the `pin 1 visual index feature`
- one narrower continuation state where `0.75 mm` is no longer fully unreplaced

## What Did Not Land

- no universal `0.75 mm pitch -> pad diameter` rule
- no cross-vendor `0.75 mm` closure
- no clean replacement yet for residual handbook pitch class `1.50 mm`
- no closeout for `connector-origin` or `installation-mark` authority gaps

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `0p75_mm_now_has_one_owner_scoped_replacement_row`
  - `1p50_mm_and_non_bga_authority_gaps_still_open`
