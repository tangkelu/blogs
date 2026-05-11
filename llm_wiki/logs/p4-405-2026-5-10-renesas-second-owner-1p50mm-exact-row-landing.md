# P4-405 Renesas Second-Owner 1.50 mm Exact Row Landing

Date: 2026-05-10
Parent lane: `P4-315`
Execution mode: `controller_owned_exact_data_landing`

## Purpose

Advance the `1.50 mm` residual lane beyond `one NXP exact row + one Renesas named-package drawing` by landing one directly verified current-public Renesas exact row from the official `BGA,LGA Mount Pad Dimensions` PDF.

## Inputs

- official Renesas one-page PDF `BGA,LGA Mount Pad Dimensions`
- `logs/p4-390-2026-5-10-nxp-sot648-1-1p50mm-reflow-footprint-landing.md`
- `logs/p4-398-2026-5-10-renesas-second-owner-1p50mm-bga-package-drawing-boundary.md`
- `logs/p4-399-2026-5-10-pcb-ziliao-completion-audit-successor-after-second-owner-1p50mm-raise.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## What Landed

### New source record

- `sources/registry/methods/renesas-bga-lga-mount-pad-dimensions-common-pitches.md`

### New exact-data fact card

- `facts/methods/renesas-1p50mm-bga-lga-mount-pad-dimensions-row.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one directly verified current-public Renesas exact row for `Lead pitch(mm) 1.50`
- one corresponding printed Renesas mount-pad range `φ(mm) 0.55 to 0.65`
- one stronger continuation state where `1.50 mm` no longer stops at `one NXP exact row + one Renesas named-package drawing`

## What Did Not Land

- no universal `1.50 mm pitch -> land pattern` rule
- no cross-vendor `1.50 mm` closeout
- no connector-origin closeout
- no stronger landed board-level installation-mark doctrine

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `1p50_mm_now_has_one_nxp_exact_row_plus_one_renesas_named_package_drawing_plus_one_renesas_exact_row`
  - `connector_origin_installation_mark_and_article_side_residuals_still_open`
