# P4-252 C2-R1 Microchip CSP/BGA Extension And Residual Narrowing

Date: 2026-05-07
Parent state: `after P4-251`
Execution mode: `c2_r1_follow_on_exact_data_landing`

## Purpose

Extend `C2-R1` again with an official source that can cover the previously unreplaced `0.40 mm` pitch class and reinforce `0.50 mm` and `0.80 mm`.

## Inputs Used

- `logs/p4-251-2026-5-7-c2-r1-ti-bga-pad-geometry-extension.md`
- local handbook image `cb091987d7d2b074.jpeg`
- official Microchip application note `AC243`

## What Landed

### New source record

- `sources/registry/methods/microchip-ac243-csp-pcb-design-guidelines.md`

### New exact-data fact card

- `facts/methods/microchip-csp-bga-solder-land-and-pitch-examples.md`

Reason:

- Microchip prints named-package `0.40`, `0.50`, and `0.80` pitch CSP/BGA rows
- this closes the `0.40 mm` gap that remained after `P4-251`
- it also strengthens `0.50 mm` and `0.80 mm` with another package-owner source

## What Changed In The Residual State

### No longer unreplaced after this pass

- `0.40 mm` pitch handbook row now has a primary-source replacement path

### Still unreplaced after this pass

- `1.50 mm`
- `0.75 mm`

### Still blocked as generic framing

- handbook `MIN / MAX / recommended` table shape
- universal cross-vendor `pitch -> pad diameter` rewrite

## Why This Was Still Not Full Completion

- Microchip's rows are named CSP package examples
- NXP's rows are named package examples
- TI's rows are `NSMD/SMD` guideline rows
- these three source shapes are useful together, but they still do not justify a single universal BGA pitch table

## Result Status

- `C2-R1`:
  - `multiple_partial_exact_data_artifacts_landed`
  - `source_backed_fact_layer_partial`
- remaining residual target classes:
  - `1.50 mm`
  - `0.75 mm`
  - universalized handbook framing

## Next Step

1. Only continue `C2-R1` if a strong official source appears for `1.50 mm` or `0.75 mm`.
2. Otherwise record those two pitch classes as current residual blockers and move to another bounded lane.
