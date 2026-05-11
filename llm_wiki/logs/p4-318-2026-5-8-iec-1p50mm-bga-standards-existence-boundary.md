# P4-318 IEC 1.50 mm BGA Standards Existence Boundary

Date: 2026-05-08
Parent lane: `P4-315`
Execution mode: `controller_owned_standards_metadata_boundary_landing`

## Purpose

Narrow the remaining `1.50 mm` package residual without overstating it as an exact-data recovery by landing one standards-owner existence-and-scope boundary from the official IEC metadata page.

## Inputs

- official IEC metadata page for `IEC 60191-6-2:2001`
- `logs/p4-315-2026-5-8-package-residual-authority-recovery.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`

## What Landed

### New source record

- `sources/registry/standards/iec-60191-6-2-ball-column-package-design-guide-page.md`

### New boundary fact card

- `facts/methods/bga-1p50mm-pitch-standards-existence-boundary.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`

## What Landed Safely

- one official IEC standards-owner proof that a design-guide family exists for `1.50 mm`, `1.27 mm`, and `1.00 mm` pitch ball and column terminal packages
- one official package-class scope that names `C-BGA`, `P-BGA`, `T-BGA`, and `C-CGA`
- one narrower continuation state where `1.50 mm` is no longer only a discovery noun gap

## What Did Not Land

- no public exact `1.50 mm` geometry row
- no handbook-row replacement for PCB pad diameter or solder-mask values
- no owner-scoped land-pattern drawing for a named `1.50 mm` package

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `1p50_mm_now_has_standards_owner_existence_boundary_but_no_exact_geometry`
