# P4-320 Microchip Second 0.75 mm TFBGA Row Landing

Date: 2026-05-08
Parent lane: `P4-309`
Execution mode: `controller_owned_exact_data_landing`

## Purpose

Strengthen the `0.75 mm` residual lane without universalizing it by landing a second official Microchip owner-scoped named-package route.

## Inputs

- official Microchip package drawing `169L_TFBGA_10x10_7G_C04-377C-J.pdf`
- `logs/p4-316-2026-5-8-microchip-0p75mm-tfbga-land-pattern-landing.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

## What Landed

### New source record

- `sources/registry/methods/microchip-169b-tfbga-7g-package-drawing-0p75mm-land-pattern.md`

### New exact-data fact card

- `facts/methods/microchip-0p75mm-tfbga-land-pattern-7g.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

## What Landed Safely

- one additional official Microchip `0.75 BSC` named-package route
- one additional printed `RECOMMENDED LAND PATTERN` row with `Contact Pad Diameter (X169) b 0.35`
- one stronger continuation state where `0.75 mm` is supported by more than one owner-scoped row

## What Did Not Land

- no universal `0.75 mm pitch -> pad diameter` rule
- no cross-vendor `0.75 mm` closure
- no clean replacement yet for residual handbook pitch class `1.50 mm`
- no closeout for `connector-origin` or `installation-mark` authority gaps

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `0p75_mm_now_has_multiple_owner_scoped_replacement_rows`
  - `1p50_mm_and_non_bga_authority_gaps_still_open`
