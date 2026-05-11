# P4-464 IEC Area-Array Land-Pattern Family Boundary

Date: 2026-05-11
Parent surfaces:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/p4-399-2026-5-10-pcb-ziliao-completion-audit-successor-after-second-owner-1p50mm-raise.md`
- `logs/p4-401-2026-5-10-pcb-ziliao-completion-audit-successor-after-renesas-0p75mm-exact-data-raise.md`
- `logs/p4-459-2026-5-11-pcb-ziliao-continuation-rerank-and-tracker-correction.md`
- `facts/methods/bga-1p50mm-pitch-standards-existence-boundary.md`
- `facts/methods/nxp-1p50mm-bga225-reflow-footprint.md`
- `facts/methods/renesas-1p50mm-bga-package-drawing-prbg0225cb-a.md`
- `facts/methods/renesas-1p50mm-bga-lga-mount-pad-dimensions-row.md`

Execution mode: `subagent_aided_non_article_residual_authority_recovery`

## Purpose

Strengthen the standards-side `1.50 mm` package lane without pretending that a new public exact row has been found.

This pass targets one narrower question:

- can the repo safely raise `1.50 mm` above `IEC 60191-6-2 existence only` by landing a stronger official IEC metadata boundary for area-array land-pattern geometry family and later land-pattern-design maintenance?

## Inputs

- official IEC metadata page for `IEC 61188-5-8:2007`
- official IEC metadata page for `IEC 61188-6-2:2021`
- current `1.50 mm` repo stack:
  - `IEC 60191-6-2` existence boundary
  - one NXP current-public exact row
  - one Renesas named-package drawing
  - one Renesas current-public exact row

## What Landed

### New source records

- `sources/registry/standards/iec-61188-5-8-area-array-land-pattern-page.md`
- `sources/registry/standards/iec-61188-6-2-land-pattern-design-smd-page.md`

### New boundary fact card

- `facts/methods/iec-area-array-land-pattern-geometry-family-boundary.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`

## What Landed Safely

- one official IEC standards-owner boundary that `area array components (BGA, FBGA, CGA, LGA)` are a formal land-pattern-geometry topic
- one official lifecycle note that the older area-array attachment-considerations standard is partially replaced by later land-pattern-design standards
- one more accurate standards-side framing for the package residual lane:
  - `IEC 60191-6-2` = coarse-pitch package design-guide existence
  - `IEC 61188-5-8` = area-array land-pattern geometry family
  - `IEC 61188-6-2` = later maintained land-pattern-design standard family

## What Did Not Land

- no third current-public manufacturer `1.50 mm` exact row
- no public exact `1.50 mm` IEC geometry row
- no generic handbook-row replacement for pad diameter, solder-mask opening, or package-library defaults
- no full closeout of the broader `1.50 mm` residual

## Why This Was The Right Recovery

- a fresh subagent-aided scout did not produce a clearly stronger current-public third-owner exact row
- the official IEC metadata pages do provide a materially stronger standards-owner framing than `existence only`
- this is therefore a real authority raise, not a blind rerank or a no-write repetition of the same `NXP + Renesas` surface

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `1p50_mm_now_has_exact_owner_rows_plus_standards_owner_area_array_land_pattern_family_boundary`

## Recommended Next Action

If `/goal` continues from here:

1. do not claim that `1.50 mm` is universally closed
2. use the new IEC family boundary when prompts need standards-owner framing for area-array land-pattern design
3. reopen the `1.50 mm` residual again only if a materially stronger public exact-geometry surface appears, such as a third independent current-public owner row or a legitimately public official standards geometry surface
