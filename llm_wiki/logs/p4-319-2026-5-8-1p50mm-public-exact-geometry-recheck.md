# P4-319 1.50 mm Public Exact-Geometry Recheck

Date: 2026-05-08
Parent lane: `P4-309`
Execution mode: `controller_owned_public_exact_geometry_recheck`

## Purpose

Recheck whether the current public package-owner surface can advance the `1.50 mm` residual beyond the existing `P4-318` standards-owner existence boundary.

This pass does not create new `sources/registry/` or `facts/` records unless a true public exact-geometry row appears.

## Inputs

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-315-2026-5-8-package-residual-authority-recovery.md`
- `logs/p4-318-2026-5-8-iec-1p50mm-bga-standards-existence-boundary.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## Public Recheck Surface Used

- package-owner search attempts across `NXP`, `Microchip`, `TI`, and `Analog Devices`
- one downloaded NXP package-information sample:
  - `SOT1908-1.pdf`
- one downloaded Microchip package-drawing sample:
  - `176B_TFBGA_11x11x1_19mm_4LX_C04-00481a.pdf`

## What This Pass Confirmed

- the current public package-owner surface is still easy to find for:
  - named-package identity
  - ball count
  - body size
  - some already-known exact geometry rows such as `0.75 mm`
- the current public package-owner surface did not produce one clean, directly reusable `1.50 mm` land-pattern row during this pass
- `P4-318` remains the strongest safe in-repo statement for `1.50 mm`

## Negative Findings Worth Preserving

- the sampled NXP package-information PDF did expose package identity text, but the sampled hit was still a `0.75 mm pitch` package rather than a new `1.50 mm` exact-geometry route
- this pass did not recover a named package-owner document that safely exposes:
  - `1.50 mm` pitch
  - and a printed `RECOMMENDED LAND PATTERN` or equivalent PCB land-geometry row
- no stronger public route was found that would justify creating a new `sources/registry/` record or replacing the current `P4-318` ceiling

## What Did Not Land

- no new official source record
- no new exact-data fact card
- no new wiki route change

## Final Status

- lane result:
  - `no_authority_upgrade_landed`
- continuation state:
  - `1p50_mm_public_exact_geometry_still_not_recovered_above_p4_318`
  - `future_reopen_should_require_a_real_owner_scoped_or_standards_owner_public_row`
