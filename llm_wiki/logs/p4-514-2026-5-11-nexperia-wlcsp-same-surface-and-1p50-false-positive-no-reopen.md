# P4-514 Nexperia WLCSP Same-Surface And 1.50 False-Positive No-Reopen

Date: 2026-05-11
Parent surfaces:

- `logs/p4-512-2026-5-11-post-p4-511-tighten-1p50mm-gate-to-true-pitch-identity.md`
- `logs/p4-513-2026-5-11-toshiba-wcsp20-and-bga-guide-true-pitch-no-reopen.md`

Execution mode: `controller_owned_candidate_gated_negative_scout`

## Purpose

Record one more bounded scout under the tightened post-`P4-512` gate for the still-open `1.50 mm` BGA/CSP residual.

This pass is not a reopen.
It checks whether current-public Nexperia package-information PDFs contain one owner same-surface hit with true `1.50 mm` pitch identity plus printed PCB geometry.

## Candidate Gate Rechecked

The current lane should reopen only if one public owner surface visibly exposes both:

1. true `1.50 mm` pitch identity
2. same-surface printed PCB land-pattern / footprint geometry

## Candidates Rechecked

- official Nexperia package-information PDF:
  - `https://assets.nexperia.com/documents/package-information/WLCSP12_SOT8088.pdf`
- official Nexperia package-information PDF:
  - `https://assets.nexperia.com/documents/package-information/WLCSP9_SOT8134.pdf`
- official Nexperia package-information PDF:
  - `https://assets.nexperia.com/documents/package-information/WLCSP6_SOT8090.pdf`

## Findings

### 1. `WLCSP12_SOT8088` is a real same-surface package-page near-hit, but the true pitch is `0.40`

- the current-public owner PDF visibly exposes:
  - package identity
  - printed reflow-soldering footprint geometry
  - true pitch identity
- but the printed pitch is `0.40`
- the visible `1.50` in the footprint figure is footprint-span context, not `1.50 mm` pitch identity

### 2. `WLCSP9_SOT8134` and `WLCSP6_SOT8090` reinforce the `visible 1.50 is not enough` filter

- both current-public owner PDFs visibly expose package identity and summary dimensions
- both also show visible `1.50` package body dimensions
- but the printed pitch identity remains `e = 0.50`
- this means they are additional owner-scoped false positives for the current `1.50 mm` residual rather than reopen candidates

### 3. The safest result remains `no reopen`

- Nexperia does provide current-public same-surface package-information PDFs with footprint or package geometry
- but the currently surfaced examples do not expose true `1.50 mm` pitch identity together with same-surface printed PCB geometry
- the new owner class therefore strengthens the search filter, not the reopen case

## Audit Result

- no new `sources/registry/` record landed
- no new `facts/` card landed
- no `wiki/` route changed
- no completion threshold changed
- the safest result is `no reopen`

## What This Pass Fixes

- future AI should not treat Nexperia WLCSP package-information PDFs as `1.50 mm` hits just because visible `1.50` appears in package or footprint-span context
- future AI should keep same-surface geometry candidates below reopen unless the printed pitch itself is `1.50`
- future AI should treat `Nexperia WLCSP` as another concrete false-positive owner class alongside the earlier `Diodes` and wrong-pitch `Toshiba` cases

## Continuation Rule

Keep the current `1.50 mm` BGA/CSP residual open only under the tightened `true pitch identity + same-surface geometry` gate.

Do not reopen it on the current-public Nexperia WLCSP package-information PDFs above.
