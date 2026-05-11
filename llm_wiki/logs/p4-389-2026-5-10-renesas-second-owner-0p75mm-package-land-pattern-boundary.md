# P4-389 Renesas Second-Owner 0.75 mm Package Land-Pattern Boundary

Date: 2026-05-10
Parent lane: `P4-315`
Execution mode: `controller_owned_source_and_boundary_landing`

## Purpose

Advance the `0.75 mm` residual lane beyond the `three Microchip owner-scoped rows` ceiling by landing one directly verified current-public second-owner named-package land-pattern document, while staying below unextracted geometry overclaim.

## Inputs

- official Renesas current-public document `48-FBGA, Package Land Pattern 10.0 x 10.0 x 1.27 mm Body, 0.75mm Pitch BCG48D1`
- `logs/p4-315-2026-5-8-package-residual-authority-recovery.md`
- `logs/p4-387-2026-5-10-package-residual-live-recheck-no-closeout.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

## What Landed

### New source record

- `sources/registry/methods/renesas-bcg48d1-48-fbga-package-land-pattern-0p75mm.md`

### New boundary fact card

- `facts/methods/renesas-0p75mm-fbga-package-land-pattern-bcg48d1.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one directly verified current-public second-owner named-package `0.75 mm` land-pattern document
- one stronger continuation state where `0.75 mm` no longer stops at `three Microchip owner-scoped rows`
- one reusable boundary card that preserves the second-owner route without inventing unextracted geometry numerics

## What Did Not Land

- no Renesas pad-diameter or pad-geometry numeric promotion
- no universal `0.75 mm pitch -> pad diameter` rule
- no closure for residual handbook pitch class `1.50 mm`
- no closeout for `connector-origin` or stronger `installation-mark` authority

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `0p75_mm_now_has_three_microchip_rows_plus_one_current_public_second_owner_named_package_document`
  - `1p50_mm_and_non_bga_authority_gaps_still_open`
