# P4-479 AMD Third-Owner 1.50 mm BGA Footprint Row Landing

Date: 2026-05-11
Parent lane: `P4-315`
Execution mode: `controller_owned_exact_data_landing`

## Purpose

Advance the `1.50 mm` residual lane beyond `IEC family boundary + one NXP exact row + one Renesas named-package drawing + one Renesas exact row` by landing one directly verified current-public third-owner exact row from the AMD-hosted `UG112 Device Package User Guide`.

## Inputs

- official AMD-hosted `UG112 Device Package User Guide`
- `logs/p4-465-2026-5-11-1p50mm-exact-lane-reaudit-after-iec-family-raise.md`
- `logs/p4-473-2026-5-11-1p50mm-candidate-gated-scout-no-reopen-successor.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## What Landed

### New source record

- `sources/registry/methods/amd-ug112-bg225-bgg225-1p50mm-bga-footprint-row.md`

### New exact-data fact card

- `facts/methods/amd-bg225-bgg225-1p50mm-bga-footprint-row.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one directly verified current-public AMD-hosted `BG225 / BGG225` exact row for `1.50 mm`
- one same-table footprint geometry surface with `Component Land`, `Solder Land (NSMD)`, `Stencil Opening`, `Line Width`, `Distance`, `Via Land`, and `Through Hole` values
- one stronger continuation state where `1.50 mm` no longer stops at `NXP + Renesas` exact-owner coverage only

## What Did Not Land

- no universal `1.50 mm pitch -> land pattern` rule
- no cross-vendor `1.50 mm` closeout
- no public official standards geometry row
- no connector-origin closeout
- no stronger landed board-level installation-mark doctrine

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `1p50mm_now_has_one_nxp_exact_row_plus_one_renesas_named_package_drawing_plus_one_renesas_exact_row_plus_one_amd_hosted_third_owner_exact_row`
  - `connector_origin_installation_mark_and_article_side_residuals_still_open`
