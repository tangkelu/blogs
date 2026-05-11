# P4-366 E3 Castellated / Half-Hole Terminology Gap Note

Date: 2026-05-09
Parent lane: `P4-311`
Execution mode: `controller_owned_negative_result_boundary_note`

## Purpose

Preserve one high-value negative result for the `E3-G` edge-feature subfamily so future `/goal` work does not reopen weak terminology recovery attempts for `castellated` and `half-hole` without a materially stronger source layer.

## Inputs

- `logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
- `logs/p4-357-2026-5-9-e4-irregular-shape-panelization-examples-route-integration.md`
- `logs/p4-39-2025-7-14-pcb-types-applications-official-source-recovery-scout.md`
- current repo-wide `sources/registry/`, `facts/`, and `logs` grep for:
  - `castellated`
  - `half-hole`
  - `half hole`

## What This Pass Confirmed

- the current repo already supports one safe controller-level taxonomy:
  - `castellated / half-hole / board-edge feature`
  - as special fabrication, handoff, and panelization review families
- the current repo also supports one adjacent route through panelization:
  - half-hole boards may require special branch review rather than ordinary adjacency assumptions
- however, the current repo still does not contain one clean official or owner-scoped terminology anchor that would justify a new reusable `castellated / half-hole` terminology fact card

## Why This Is Not A Clean Terminology Landing

- no local `sources/registry/` record currently provides standards-owner or package-owner terminology for `castellated` or `half-hole`
- the strongest current in-repo mention remains controller-level and article-adjacent rather than official terminology
- the older scout log already preserved the same gap:
  - no stable in-corpus official anchor was found for topic-specific `castellated PCB` taxonomy

## Safest Reuse Boundary

- safe to reuse only as:
  - `castellated / half-hole / edge-feature` as special handling taxonomy
  - board-edge feature identity that deserves extra fabrication or panelization review
  - a caution that ordinary pad, adjacency, and separation assumptions may not apply cleanly
- not safe to reuse as:
  - official or owner-scoped terminology definition
  - geometry or plating rule
  - manufacturability, reliability, or acceptability proof
  - supplier capability or process recipe

## Final Status

- lane result:
  - `negative_result_boundary_note_landed`
- continuation state:
  - `castellated_and_half_hole_remain_controller_level_taxonomy_only`
  - `future_reopen_should_require_a_real_official_or_owner_scoped_terminology_anchor`
