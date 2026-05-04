# P4-133 2026-05-02 Copper-Foil Exact-Product Profile Source-Backed Integration

Date: 2026-05-02
Status: `source_backed_fact_layer_partial`

## Purpose

Convert the `P4-125 Lane B` copper-foil branch from class-vocabulary-only posture into a narrow exact-product micro-lane for owner-scoped profile and `Rz` anchors.

This pass stays narrow. It does not claim supplier-neutral roughness tables, RF-loss outcomes, bend-life, or finished-board performance.

## Inputs Reviewed

- `facts/materials/copper-foil-classes-and-roughness-boundary.md`
- `wiki/materials/copper-foil-class-roughness-and-rf-boundaries.md`
- `logs/p4-126-2026-5-2-flex-copper-ceramic-recovery.md`
- current official JX rigid-board ED foil page
- current official JX `JXEFL` FPC ED foil page
- current official Furukawa `FZ-WS` page
- current official Furukawa `GTS-STD / GTS-MP` page

## Source-Backed Additions

Added source records:

- `sources/registry/materials/jx-rigid-ed-copper-foil-page.md`
- `sources/registry/materials/jx-jxefl-fpc-ed-copper-foil-page.md`
- `sources/registry/materials/furukawa-fz-ws-copper-foil-page.md`
- `sources/registry/materials/furukawa-gts-std-gts-mp-copper-foil-page.md`

Added reusable knowledge:

- `facts/materials/copper-foil-exact-product-profile-anchor-map.md`

## What Is Now Source-Backed

- exact JX rigid-board ED foil product nouns such as `JTCS-P1`, `JDLC`, and `HLP-II`
- exact JX FPC ED foil product nouns such as `JXEFL-V2` and `JXEFL-BHM`
- exact Furukawa product nouns such as `FZ-WS`, `GTS-STD`, and `GTS-MP`
- owner-scoped `Rz` / profile rows tied to exact product names and thickness rows
- guarded wording that copper-foil product rows exist beyond class-only ED / rolled taxonomy

## What Stays Blocked

- supplier-neutral roughness tables
- universal `ED` versus rolled rankings
- RF-loss, insertion-loss, impedance, or signal-integrity outcome claims
- bend-life, peel-strength ranking, current, thermal, or reliability claims
- stock, sourcing, lamination compatibility, lead time, quote, or supplier-capability claims

## Controller Result

`P4-126` should no longer treat the copper-foil branch as fully `hold-only`.

Current correct posture:

- class-level copper-foil vocabulary remains source-backed
- narrow exact-product profile recovery is now source-backed partial
- supplier-neutral roughness or RF-performance generalization remains blocked
