# P4-487 IEC Square-BGA 1 mm-Or-Larger Family Boundary

Date: 2026-05-11
Parent surfaces:

- `logs/p4-464-2026-5-11-iec-area-array-land-pattern-family-boundary.md`
- `logs/p4-465-2026-5-11-1p50mm-exact-lane-reaudit-after-iec-family-raise.md`
- `logs/p4-479-2026-5-11-amd-third-owner-1p50mm-bga-footprint-row-landing.md`
- `logs/p4-484-2026-5-11-completion-audit-successor-after-altium-cad-owner-doctrine-raise.md`
- `logs/p4-485-2026-5-11-infineon-package-portal-1p50mm-candidate-false-positive-no-reopen.md`
- `logs/p4-486-2026-5-11-microchip-ti-adi-1p50mm-candidate-class-scout-no-reopen.md`

Execution mode: `subagent_aided_non_article_residual_authority_recovery`

## Purpose

Strengthen the standards-side `1.50 mm` package lane again without pretending that a new public exact row has been found.

This pass targets one narrower question:

- can the repo safely raise `1.50 mm` above the current `IEC 60191-6-2 + IEC 61188-5-8 / 61188-6-2` framing by landing one tighter official IEC metadata boundary for square-BGA package scope with public outline, dimension, and recommended-variation wording?

## Inputs

- official IEC metadata page for `IEC 60191-6-18:2010`
- current `1.50 mm` repo stack:
  - `IEC 60191-6-2` existence boundary
  - `IEC 61188-5-8 / 61188-6-2` area-array land-pattern family boundary
  - one NXP current-public exact row
  - one Renesas named-package drawing
  - one Renesas current-public exact row
  - one AMD-hosted third-owner exact row

## What Landed

### New source record

- `sources/registry/standards/iec-60191-6-18-square-bga-design-guide-page.md`

### New boundary fact card

- `facts/methods/iec-square-bga-1mm-or-larger-outline-and-variation-boundary.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`

## What Landed Safely

- one official IEC standards-owner boundary that `all square ball grid array packages (BGA), whose terminal pitch is 1 mm or larger` are covered by a formal package-guide family
- one public IEC scope statement that this family includes:
  - `standard outline drawings`
  - `dimensions`
  - `recommended variations`
- one more accurate standards-side framing for the package residual lane:
  - `IEC 60191-6-2` = coarse-pitch ball/column package-guide existence
  - `IEC 60191-6-18` = square-BGA `1 mm or larger` outline/dimension/recommended-variation family
  - `IEC 61188-5-8` = area-array land-pattern geometry family
  - `IEC 61188-6-2` = later maintained land-pattern-design standard family

## What Did Not Land

- no new manufacturer `1.50 mm` exact row
- no public exact `1.50 mm` IEC PCB land-pattern row
- no generic handbook-row replacement for pad diameter, solder-mask opening, or package-library defaults
- no full closeout of the broader `1.50 mm` residual

## Why This Was The Right Recovery

- the latest subagent-aided owner scouts did not produce a clearly stronger current-public owner exact row above `NXP + Renesas + AMD`
- the official IEC metadata page does provide a materially tighter standards-owner package-family framing than the current repo ceiling
- this is therefore a real authority raise, not another repetition of the same `Infineon / Microchip / TI / ADI` candidate classes

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `1p50mm_now_has_owner_exact_rows_plus_square_bga_package_family_boundary_plus_area_array_land_pattern_family_boundary`

## Recommended Next Action

If `/goal` continues from here:

1. do not claim that `1.50 mm` is universally closed
2. use the new `IEC 60191-6-18` boundary when prompts need standards-owner square-BGA package-family framing
3. reopen the `1.50 mm` residual again only if a materially stronger public exact-geometry surface appears, such as one new owner exact row or a legitimately public official geometry surface
