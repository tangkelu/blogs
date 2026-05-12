# P4-550 JEITA EDR-7315B Public BGA Geometry Surface Below 1.50 mm No-Reopen

Date: 2026-05-12
Parent surfaces:

- `logs/p4-545-2026-5-12-ipc-7095e-open-surface-definition-and-figure-title-visibility-still-no-reopen.md`
- `logs/p4-547-2026-5-12-jedec-home-jep95-discoverability-still-no-reopen.md`
- `logs/p4-536-2026-5-12-date-rollover-1p50mm-current-public-candidate-recheck-no-reopen.md`

Execution mode: `subagent_aided_public_standards_surface_strengthening_without_reopen`

## Purpose

Record one genuinely new public standards-owner BGA geometry surface for the still-open `1.50 mm` package residual.

This pass does not reopen the lane.
It lands a stronger standards-side surface than TOC-only, metadata-only, or discoverability-only anchors, while keeping the gate closed because the visible public geometry still stops below `1.50 mm`.

## Candidate Rechecked

- official JEITA public BGA design guide:
  - `https://home.jeita.or.jp/tsc/std-pdf/EDR-7315B.pdf`

## What Landed

### New source record

- `sources/registry/standards/jeita-edr-7315b-bga-design-guide.md`

### New standards boundary fact card

- `facts/standards/jeita-edr-7315b-bga-public-geometry-below-1p50mm-boundary.md`

### Route integration

Updated:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one official public standards-owner BGA design-guide PDF above TOC-only and discoverability-only surfaces
- one bounded standards-side fact that the visible public geometry-bearing payload reaches `1.27 mm` and `1.00 mm`
- one bounded negative result that no visible reusable public `1.50 mm` row was recovered

## What Did Not Land

- no public `1.50 mm` JEITA geometry row
- no public standards-owner exact replacement for the current `1.50 mm` residual
- no change to the top-level completion threshold

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `standards_side_now_includes_one_real_public_geometry_bearing_bga_guide_below_1p50mm`
  - `1p50mm_residual_still_requires_true_public_1p50mm_geometry`
