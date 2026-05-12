# P4-513 Toshiba WCSP20 And BGA Guide True-Pitch No-Reopen

Date: 2026-05-11
Parent surfaces:

- `logs/p4-512-2026-5-11-post-p4-511-tighten-1p50mm-gate-to-true-pitch-identity.md`
- `logs/p4-510-2026-5-11-post-p4-509-residual-rerank-keep-1p50mm-but-tighten-candidate-class.md`

Execution mode: `subagent_aided_candidate_gated_negative_scout`

## Purpose

Record one more bounded scout under the tightened post-`P4-512` gate for the still-open `1.50 mm` BGA/CSP residual.

This pass is not a reopen.
It checks whether the current-public Toshiba package-detail and BGA-mounting-guide surfaces contain one owner same-surface hit with true `1.50 mm` pitch identity plus printed PCB geometry.

## Candidate Gate Rechecked

The current lane should reopen only if one public owner surface visibly exposes both:

1. true `1.50 mm` pitch identity
2. same-surface printed PCB land-pattern / footprint geometry

## Candidate Rechecked

- official Toshiba package detail page:
  - `https://toshiba.semicon-storage.com/us/semiconductor/design-development/package/detail.WCSP20.html`
- official Toshiba BGA package mounting guide:
  - `https://toshiba.semicon-storage.com/info/MountManual_en_20170317.pdf?did=57586`

## Findings

### 1. The Toshiba package-detail page is a real near-hit, but at the wrong pitch

- the current-public `WCSP20` package-detail page does expose:
  - one real package identity
  - one visible `Land pattern dimensions for reference only`
- the Toshiba code also visibly carries a true pitch identity:
  - `S-UFBGA20-0202-0.40-001`
- but that identity is `0.40`, not `1.50`

### 2. The official Toshiba BGA guide also stays below the current gate

- the current-public Toshiba mounting guide is a real official BGA source
- it visibly lists package lineup and printed ball pitches
- but the public lineup only reaches:
  - `0.40`
  - `0.50`
  - `0.65`
  - `0.80`
- it does not expose one current-public `1.50 mm` pitch row with same-surface land-pattern geometry

### 3. The safest result remains `no reopen`

- Toshiba does provide one stronger example of a same-surface package page with pitch identity plus reference land pattern
- but the true pitch is not the target residual class
- the Toshiba public BGA guide also stays below the current `1.50 mm` gate

## Audit Result

- no new `sources/registry/` record landed
- no new `facts/` card landed
- no `wiki/` route changed
- no completion threshold changed
- the safest result is `no reopen`

## What This Pass Fixes

- future AI should not mistake `same-surface pitch identity plus land pattern` alone for a `1.50 mm` hit unless the printed pitch itself is `1.50`
- future AI should not treat current-public Toshiba BGA lineup pages as if they already expose `1.50 mm` pitch geometry
- future AI should keep the `1.50 mm` gate attached to true pitch identity, not merely same-surface geometry at some other pitch

## Continuation Rule

Keep the current `1.50 mm` BGA/CSP residual open only under the tightened `true pitch identity + same-surface geometry` gate.

Do not reopen it on current-public Toshiba package-detail or BGA-guide surfaces alone.
