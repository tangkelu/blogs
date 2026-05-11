# P4-398 Renesas Second-Owner 1.50 mm BGA Package Drawing Boundary

Date: 2026-05-10
Parent lane: `P4-315`
Execution mode: `controller_owned_source_and_boundary_landing`

## Purpose

Advance the `1.50 mm` residual lane beyond the `one NXP exact row only` ceiling by landing one directly verified current-public second-owner named-package BGA drawing, while staying below unlanded geometry overclaim.

## Inputs

- official Renesas current-public package drawing for `225-pin Plastic BGA PRBG0225CB-A`
- `logs/p4-315-2026-5-8-package-residual-authority-recovery.md`
- `logs/p4-390-2026-5-10-nxp-sot648-1-1p50mm-reflow-footprint-landing.md`
- `logs/p4-394-2026-5-10-pcb-ziliao-completion-audit-successor-after-residual-lane-raises.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## What Landed

### New source record

- `sources/registry/methods/renesas-prbg0225cb-a-1p50mm-bga-package-drawing.md`

### New boundary fact card

- `facts/methods/renesas-1p50mm-bga-package-drawing-prbg0225cb-a.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one directly verified current-public second-owner named-package `1.50 mm` BGA drawing
- one stronger continuation state where `1.50 mm` no longer stops at `one NXP exact row`
- one reusable boundary card that preserves the second-owner route without inventing recommended land-pattern geometry

## What Did Not Land

- no Renesas recommended land-pattern geometry
- no universal `1.50 mm pitch -> land pattern` rule
- no cross-vendor `1.50 mm` closeout
- no closeout for `0.75 mm`, `connector-origin`, or stronger `installation-mark` authority

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `1p50_mm_now_has_one_nxp_exact_row_plus_one_current_public_second_owner_named_package_drawing`
  - `non_bga_authority_gaps_still_open`
