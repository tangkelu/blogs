# P4-489 1.50 mm Owner And Standards Candidate Scout No-Reopen Successor

Date: 2026-05-11
Parent surfaces:

- `logs/p4-486-2026-5-11-microchip-ti-adi-1p50mm-candidate-class-scout-no-reopen.md`
- `logs/p4-487-2026-5-11-iec-square-bga-1mm-or-larger-family-boundary.md`
- `logs/p4-488-2026-5-11-completion-audit-successor-after-iec-square-bga-family-raise.md`

Execution mode: `subagent_aided_candidate_gated_negative_scout`

## Purpose

Record one more bounded scout across both sides of the still-open `1.50 mm` residual lane after `P4-488`.

This pass is not a reopen.
It checks whether any newly surfaced current-public owner or standards-side candidate now clears the current repo ceiling.

## Candidate Gate Rechecked

The current lane should reopen only if one of the following appears:

1. a new materially stronger current-public owner exact row
2. a legitimately public official geometry surface above the current metadata-level standards ceiling

## Candidate Classes Rechecked

### Owner-side classes

1. Lattice current-public BGA layout-guidance class
2. Intel current-public package-support and mechanical-package pages
3. onsemi current-public package-drawing repository class

### Standards-side and quasi-standards-side classes

1. IEC `61188-6-1:2021`
2. IEC `61188-6-3:2024`
3. IEC `60191-6:2009`
4. IPC public standards pages and TOC/front-matter surfaces for `IPC-7095`, `IPC-7351`, and `IPC-7352`
5. JEDEC official primary lane as recoverable in the current environment

## Findings

### 1. No new owner-side surface exceeds the current `NXP + Renesas + AMD` stack

- Lattice is the strongest new owner-side near-hit from this pass because its current-public BGA layout note does expose real board-geometry rows
- but the surfaced visible pitch classes remain limited to:
  - `0.4 mm`
  - `0.5 mm`
  - `0.8 mm`
  - `1.0 mm`
- this means the current Lattice public surface still does not provide:
  - one true `1.50 mm` owner exact row
  - one same-surface `1.50 mm` pitch identity plus printed PCB land-pattern geometry
- Intel current-public package-support pages do show live package identity, but not one printed PCB land-pattern exact row
- onsemi current-public package-drawing hits surfaced in this pass stayed on non-target package classes rather than one verified `1.50 mm` area-array row

### 2. No new standards-side or quasi-standards-side surface exceeds the current IEC ceiling

- `IEC 61188-6-1:2021` and `IEC 60191-6:2009` are real current-public official metadata surfaces
- but they stay broader and more generic than the current `IEC 60191-6-18` plus `IEC 61188-5-8 / 61188-6-2` stack
- `IEC 61188-6-3:2024` is for through-hole land-pattern design, so it does not strengthen the BGA lane
- public IPC pages and TOC/front-matter PDFs do confirm relevant standards families exist
- but the currently visible public IPC surface still does not expose:
  - one public exact BGA geometry table
  - one public `1.50 mm` row
- JEDEC did not produce one recoverable current-public official primary surface strong enough to raise the ceiling in this environment

### 3. The safest result remains `no reopen`

- no new owner-controlled public surface exceeded the current `NXP + Renesas + AMD` owner stack
- no new standards-side or quasi-standards-side public surface exceeded the current `IEC 60191-6-18` plus `IEC 61188-5-8 / 61188-6-2` ceiling
- the repo-supported `1.50 mm` ceiling therefore still remains:
  - `IEC 60191-6-2` existence boundary
  - `IEC 60191-6-18` square-BGA `1 mm or larger` outline/dimension/recommended-variation boundary
  - `IEC 61188-5-8 / 61188-6-2` land-pattern family boundary
  - one NXP current-public exact row
  - one Renesas named-package drawing
  - one Renesas current-public exact row
  - one AMD-hosted third-owner exact row

## Audit Result

- no new `sources/registry/` record landed
- no new `facts/` card landed
- no `wiki/` route changed
- no completion threshold changed
- the safest result is `no reopen`

## What This Pass Fixes

- future AI should not treat current-public Lattice BGA layout guidance as if it already contains a `1.50 mm` owner exact row
- future AI should not treat current-public Intel package-support pages as if package identity alone is enough to reopen `1.50 mm`
- future AI should not treat current-public IPC TOC/front-matter pages as if they already expose public `1.50 mm` geometry
- future AI should not assume a JEDEC raise exists unless one recoverable current-public official primary surface is actually verified

## Continuation Rule

Keep `1.50 mm` as a watch-only residual under the same candidate-gated standard.

Do not reopen it again unless a future pass recovers either:

1. one same-surface public owner document with true `1.50 mm` pitch identity plus printed PCB land-pattern geometry
2. one legitimately public official geometry surface above the current IEC metadata ceiling
