# P4-512 Post-P4-511 Tighten 1.50 mm Gate To True Pitch Identity

Date: 2026-05-11
Parent surfaces:

- `logs/p4-510-2026-5-11-post-p4-509-residual-rerank-keep-1p50mm-but-tighten-candidate-class.md`
- `logs/p4-511-2026-5-11-diodes-u-wlb1510-6-outline-and-suggested-pad-layout-landing.md`

Execution mode: `controller_owned_gate_tightening`

## Purpose

Refresh the current `1.50 mm` reopen gate again after `P4-511`.

This pass does not land new `sources/`, `facts/`, or `wiki/`.
It only fixes one ambiguity in the current continuation wording: visible `1.50` package geometry is not enough by itself unless the document also shows that `1.50` is the package pitch rather than a body dimension.

## Rechecked Surfaces

1. the post-`P4-510` same-surface owner exact-geometry gate
2. the new Diodes `U-WLB1510-6` exact-geometry page from `P4-511`

## Findings

### 1. `P4-511` landed a real exact-geometry page, but not a `1.50 mm pitch` reopen

- the Diodes datasheet is a real owner-scoped exact-geometry page with named package identity and same-surface footprint geometry
- but the printed package pitch is `e = 0.50`
- the visible `1.50` belongs to package body dimension `D`
- this means `P4-511` strengthens the package lane and the search filter, but it does not satisfy the current BGA/CSP `1.50 mm pitch` reopen bar

### 2. The current gate must therefore be tightened from `package identity` to `pitch identity`

- after `P4-510`, the wording `true 1.50 mm package identity + same-surface geometry` is now too loose
- the safer rule is:
  - visible `1.50` must be the true package pitch identity
  - and the same public owner surface must also expose printed PCB land-pattern / footprint geometry

## Audit Result

- no new residual lane was landed
- no per-PDF state changed
- tracker wording required refresh because the previous `package identity` gate is now too permissive

## Recommended Gate

If `/goal` continues from here, treat the `1.50 mm` BGA/CSP residual as reopened only when a candidate visibly exposes both:

1. true `1.50 mm` pitch identity
2. same-surface printed PCB land-pattern / footprint geometry

Do not reopen it on:

- package body dimensions such as `D = 1.50`
- package-family identity alone
- package-portal structure alone
- TOC, front-matter, or metadata-only standards pages

## What This Pass Fixes

- future AI should not treat any visible `1.50` package dimension as if it were automatically a pitch hit
- future AI should keep `P4-511` as a reusable exact-geometry example without misclassifying it as a BGA/CSP `1.50 mm pitch` raise
- future AI should use `true pitch identity + same-surface geometry` as the only clean `1.50 mm` reopen gate
