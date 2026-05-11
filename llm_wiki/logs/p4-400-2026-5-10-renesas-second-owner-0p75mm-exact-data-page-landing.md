# P4-400 Renesas Second-Owner 0.75 mm Exact-Data Page Landing

Date: 2026-05-10
Parent lane: `P4-315`
Execution mode: `controller_owned_exact_data_landing`

## Purpose

Advance the `0.75 mm` residual lane beyond `three Microchip exact rows plus one Renesas second-owner named-package document` by landing one directly verified current-public second-owner exact-data page from an official Renesas package land-pattern PDF.

## Inputs

- official Renesas current-public document `48-FBGA, Package Land Pattern 10.0 x 10.0 x 1.27 mm Body, 0.75mm Pitch BCG48D1`
- `logs/p4-389-2026-5-10-renesas-second-owner-0p75mm-package-land-pattern-boundary.md`
- `logs/p4-387-2026-5-10-package-residual-live-recheck-no-closeout.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

## What Landed

### Updated source record

- `sources/registry/methods/renesas-bcg48d1-48-fbga-package-land-pattern-0p75mm.md`

### Updated exact-data fact card

- `facts/methods/renesas-0p75mm-fbga-package-land-pattern-bcg48d1.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one directly verified current-public second-owner exact-data page for the named `BCG48D1` `0.75 mm` package
- one visible `RECOMMENDED LAND PATTERN DIMENSION` page carrying reusable page-scoped values `0.300`, `0.75`, `3.750`, `5.25`, and `10.000`
- one visible page-note context carrying `ALL DIMENSIONS ARE IN MM. ANGLES IN DEGREES.`, `LAND PATTERN RECOMMENDATION PER IPC-7351B GENERIC`, and `SMD PATTERN ASSUMED`
- one stronger continuation state where `0.75 mm` no longer stops at `three Microchip exact rows plus one geometry-unverified second-owner document`

## What Did Not Land

- no universal `0.75 mm pitch -> land pattern` rule
- no cross-vendor `0.75 mm` closeout
- no closeout for residual handbook pitch class `1.50 mm`
- no closeout for `connector-origin` or stronger `installation-mark` authority

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `0p75_mm_now_has_three_microchip_exact_rows_plus_one_current_public_second_owner_exact_data_page`
  - `1p50_mm_and_non_bga_authority_gaps_still_open`
