# P4-324 Microchip Third 0.75 mm TFBGA Row Landing

Date: 2026-05-08
Parent lane: `P4-309`
Execution mode: `controller_owned_exact_data_landing`

## Purpose

Strengthen the `0.75 mm` residual lane again by landing a third official Microchip owner-scoped named-package route.

## Inputs

- official Microchip package drawing `196B_TFBGA_11x11_[BAB]_C04-21141a.pdf`
- `logs/p4-316-2026-5-8-microchip-0p75mm-tfbga-land-pattern-landing.md`
- `logs/p4-320-2026-5-8-microchip-second-0p75mm-tfbga-row-landing.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

## What Landed

### New source record

- `sources/registry/methods/microchip-196b-tfbga-bab-package-drawing-0p75mm-land-pattern.md`

### New exact-data fact card

- `facts/methods/microchip-0p75mm-tfbga-land-pattern-bab.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

## What Landed Safely

- one third official Microchip `0.75 BSC` named-package route
- one additional printed `RECOMMENDED LAND PATTERN` row with `Contact Pad Diameter (X196) X 0.35`
- one stronger continuation state where `0.75 mm` is supported by three owner-scoped rows

## What Did Not Land

- no universal `0.75 mm pitch -> pad diameter` rule
- no cross-vendor `0.75 mm` closure
- no clean replacement yet for residual handbook pitch class `1.50 mm`
- no closeout for `connector-origin` or `installation-mark` authority gaps

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `0p75_mm_now_has_three_owner_scoped_replacement_rows`
  - `1p50_mm_and_non_bga_authority_gaps_still_open`
