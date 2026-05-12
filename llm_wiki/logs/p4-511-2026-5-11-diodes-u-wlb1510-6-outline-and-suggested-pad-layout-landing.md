# P4-511 Diodes U-WLB1510-6 Outline And Suggested Pad Layout Landing

Date: 2026-05-11
Parent surfaces:

- `logs/p4-510-2026-5-11-post-p4-509-residual-rerank-keep-1p50mm-but-tighten-candidate-class.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

Execution mode: `subagent_aided_controller_owned_exact_data_landing`

## Purpose

Land one directly verified current-public owner-scoped exact-geometry page from an official Diodes datasheet while preserving the fact that the visible `1.50` in this document is package body size, not package pitch.

## Inputs

- official Diodes datasheet PDF `DMN1016UCB6`
- current package-route map
- post-`P4-510` same-surface owner exact-geometry scout

## What Landed

### New source record

- `sources/registry/methods/diodes-dmn1016ucb6-u-wlb1510-6-outline-and-suggested-pad-layout.md`

### New exact-data fact card

- `facts/methods/diodes-u-wlb1510-6-outline-and-suggested-pad-layout.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one directly verified current-public owner-scoped exact-geometry page for the named `U-WLB1510-6` package
- one package-outline block with printed `D`, `E`, and `e` values
- one same-page `Suggested Pad Layout` block with printed layout dimensions
- one stronger search-discipline note that visible `1.50` can belong to package body dimension `D`, not package pitch

## What Did Not Land

- no new `1.50 mm pitch` BGA/CSP exact row
- no reopening of the current `1.50 mm` BGA/CSP residual on this Diodes page
- no universal WLB or CSP footprint law
- no cross-vendor closeout

## Why This Was The Right Recovery

- the source is a real official owner PDF with named package identity and same-surface footprint geometry
- it therefore clears the package-lane bar for one reusable named-package exact-data page
- at the same time, it sharpens the current `1.50` search filter because the visible `1.50` here is not pitch

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `package_lane_now_has_one_more_named_package_exact_geometry_example`
  - `1p50_pitch_residual_still_requires_true_pitch_identity_plus_same_surface_geometry`
