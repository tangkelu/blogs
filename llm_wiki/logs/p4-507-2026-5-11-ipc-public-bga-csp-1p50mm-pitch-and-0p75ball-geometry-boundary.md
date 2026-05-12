# P4-507 IPC Public BGA/CSP 1.50 mm Pitch And 0.75-Ball Geometry Boundary

Date: 2026-05-11
Parent surfaces:

- `logs/p4-489-2026-5-11-1p50mm-owner-and-standards-candidate-scout-no-reopen-successor.md`
- `logs/p4-491-2026-5-11-completion-audit-successor-after-package-and-doctrine-candidate-tightening.md`
- `facts/methods/bga-1p50mm-pitch-standards-existence-boundary.md`
- `facts/methods/iec-area-array-land-pattern-geometry-family-boundary.md`
- `facts/methods/iec-square-bga-1mm-or-larger-outline-and-variation-boundary.md`
- `facts/methods/nxp-1p50mm-bga225-reflow-footprint.md`
- `facts/methods/renesas-1p50mm-bga-lga-mount-pad-dimensions-row.md`
- `facts/methods/amd-bg225-bgg225-1p50mm-bga-footprint-row.md`

Execution mode: `subagent_aided_non_article_residual_authority_recovery`

## Purpose

Strengthen the still-open `1.50 mm` package lane with one public IPC-hosted geometry surface that is stronger than metadata-only family framing, without pretending that a formal public IPC standards row has been recovered.

This pass targets one narrower question:

- can the repo safely add one public standards-adjacent geometry boundary linking `1.50 / 1.27 mm` BGA pitch family to nominal `0.75 mm` ball class and visible round-land example geometry?

## Inputs

- official IPC-hosted public technical paper `Principles for Implementing BGA and CSP Technology`
- current `1.50 mm` repo stack:
  - `IEC 60191-6-2` existence boundary
  - `IEC 60191-6-18` square-BGA family boundary
  - `IEC 61188-5-8 / 61188-6-2` area-array land-pattern family boundary
  - one NXP current-public exact row
  - one Renesas named-package drawing
  - one Renesas current-public exact row
  - one AMD-hosted third-owner exact row

## What Landed

### New source record

- `sources/registry/methods/ipc-bga-csp-technology-paper-1p50mm-pitch-and-0p75ball-geometry.md`

### New boundary fact card

- `facts/methods/ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one public IPC-hosted BGA/CSP paper that visibly names `1.50 mm` and `1.27 mm` pitch variation
- one public IPC-hosted mapping from that pitch family to nominal `0.75 mm` ball class
- one visible round-land geometry posture plus public `0.75 mm` ball example values for land diameter and solder-mask opening
- one standards-adjacent public geometry surface above pure metadata and family-framing pages

## What Did Not Land

- no formal public `IPC-7095A` standards table row
- no public exact `1.50 mm` IEC or IPC standards row
- no new manufacturer `1.50 mm` exact row
- no universal cross-vendor `1.50 mm pitch -> land pattern` rule
- no full closeout of the broader `1.50 mm` residual

## Why This Was The Right Recovery

- the current owner-side candidate classes had already been tightened and should not be blindly reopened on the same weak surfaces
- this public IPC-hosted paper is materially stronger than TOC-only or metadata-only framing because it exposes visible pitch-family and geometry content
- the pass therefore raises the non-owner public side of `1.50 mm` without pretending that the paid IPC standards themselves are publicly exposed

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `1p50mm_now_has_owner_exact_rows_plus_iec_family_boundaries_plus_one_public_ipc_hosted_geometry_boundary`

## Recommended Next Action

If `/goal` continues from here:

1. use this new IPC card only for standards-adjacent public geometry framing
2. do not convert it into a universal `1.50 mm` exact replacement row
3. reopen the `1.50 mm` residual again only for:
   - one materially stronger public owner exact row above the current owner stack
   - or one legitimately public formal standards geometry surface
