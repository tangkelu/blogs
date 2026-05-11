# P4-251 C2-R1 TI BGA Pad Geometry Extension

Date: 2026-05-07
Parent state: `after P4-250`
Execution mode: `c2_r1_follow_on_exact_data_landing`

## Purpose

Extend the `C2-R1` BGA footprint recovery with another primary-source-backed card instead of leaving `1.27 mm` pitch permanently in residual state.

## Inputs Used

- `logs/p4-250-2026-5-7-c2-r1-bga-pitch-table-partial-official-replacement.md`
- local handbook image `cb091987d7d2b074.jpeg`
- official TI application note `AN-1126 BGA`

## What Landed

### New source record

- `sources/registry/methods/ti-an1126-bga-pad-geometry-guidelines.md`

### New exact-data fact card

- `facts/methods/ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md`

Reason:

- TI prints explicit `1.27 mm` and `1.0 mm` pitch pad-geometry rows
- this closes the `1.27 mm` gap that remained after `P4-250`
- it also gives a second primary-source perspective for `1.0 mm` pitch

## What Changed In The Residual State

### No longer unreplaced after this pass

- `1.27 mm` pitch handbook row now has a primary-source replacement path

### Still unreplaced after this pass

- `1.50 mm`
- `0.75 mm`
- `0.40 mm`

### Still blocked as generic framing

- handbook `MIN / MAX / recommended` table shape
- universal cross-vendor `pitch -> pad diameter` rewrite

## Why This Was Still Not A Universal Completion

- TI's rows are `NSMD/SMD` guideline rows, not a generic market-wide table
- NXP's rows are named-package examples
- those two source shapes are useful together, but they still do not justify one universal BGA pitch law

## Result Status

- `C2-R1`:
  - `multiple_partial_exact_data_artifacts_landed`
  - `source_backed_fact_layer_partial`
- remaining residual target classes:
  - `1.50 mm`
  - `0.75 mm`
  - `0.40 mm`
  - universalized handbook framing

## Next Step

1. Only continue `C2-R1` if a strong official source appears for `1.50`, `0.75`, or `0.40 mm`.
2. Otherwise mark those rows as current residual blockers and move to a different bounded lane.
