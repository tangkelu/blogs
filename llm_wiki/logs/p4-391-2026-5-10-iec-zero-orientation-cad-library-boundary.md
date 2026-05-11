# P4-391 IEC Zero-Orientation CAD-Library Boundary

Date: 2026-05-10
Parent lane: `P4-315`
Execution mode: `controller_owned_standards_boundary_landing`

## Purpose

Advance the still-open `installation-mark` side of the `package residual authority recovery` lane by landing one narrower standards-owner boundary for `zero orientation`, while explicitly staying below any claim about universal `pin-1`, polarity-mark, connector-origin, or board-level installation-mark geometry doctrine.

## Inputs

- official IEC webstore metadata page for `IEC 61188-7:2017`
- `logs/p4-317-2026-5-8-connector-origin-and-installation-mark-boundary-landing.md`
- `logs/p4-387-2026-5-10-package-residual-live-recheck-no-closeout.md`
- `facts/methods/connector-origin-and-installation-mark-boundary.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## What Landed

### New source record

- `sources/registry/standards/iec-61188-7-zero-orientation-cad-library-page.md`

### New boundary fact card

- `facts/methods/iec-zero-orientation-cad-library-construction-boundary.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one official standards-owner anchor that `zero orientation` is a CAD-library construction topic
- one narrower route that separates orientation-description doctrine from still-open board-level installation-mark geometry questions
- one stronger continuation state where the repo no longer relies only on `KiCad + owner drawings + local handbook context` for orientation-governance wording

## What Did Not Land

- no universal connector-origin default
- no universal `pin-1` or polarity-mark doctrine
- no board-level installation-mark geometry rule
- no closeout for residual `1.50 mm`, `0.75 mm`, or connector-origin

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `installation_mark_lane_now_has_standards_owner_zero_orientation_anchor`
  - `connector_origin_and_board_level_mark_geometry_residuals_still_open`
