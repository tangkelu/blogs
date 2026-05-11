# P4-485 Infineon Package Portal 1.50 mm Candidate False-Positive No-Reopen

Date: 2026-05-11
Parent surfaces:

- `logs/p4-473-2026-5-11-1p50mm-candidate-gated-scout-no-reopen-successor.md`
- `logs/p4-479-2026-5-11-amd-third-owner-1p50mm-bga-footprint-row-landing.md`
- `logs/p4-480-2026-5-11-completion-audit-successor-after-amd-third-owner-1p50mm-raise.md`
- `logs/p4-484-2026-5-11-completion-audit-successor-after-altium-cad-owner-doctrine-raise.md`

Execution mode: `subagent_aided_candidate_gated_negative_scout`

## Purpose

Record one narrower candidate-gated scout against the still-open `1.50 mm` residual after the post-`P4-479` owner stack raise.

This pass is not a reopen.
It checks whether the current-public `official package portal with attached footprint drawing` candidate class actually produces one new owner exact row above the current `NXP + Renesas + AMD` ceiling.

## Candidate Gate Rechecked

The current lane should reopen only if one of the following appears:

1. a new materially stronger current-public owner exact row
2. a legitimately public official geometry surface above metadata level

## Candidate Class Rechecked

The highest-signal next candidate class was:

- official package-portal pages with attached footprint drawings

The current concrete near-hit rechecked in this pass was:

- Infineon `PG-BGA` package-portal class, including current-public package pages such as `PG-BGA-165-807`

## Findings

### 1. The package-portal class is structurally promising, but not sufficient by itself

- a current-public package portal can be stronger than a generic product page because it may expose:
  - named owner package identity
  - visible package pitch metadata
  - attached drawings or footprint assets in the same owner-controlled surface
- this keeps the class worth watching
- but the class still clears the reopen gate only if the same public owner surface yields:
  - a true `1.50 mm` BGA pitch identity
  - and printed PCB land-pattern geometry

### 2. The current Infineon near-hit stays below reopen

- the rechecked Infineon `PG-BGA-165-807` package page does show the right structural shape for a near-hit:
  - package-portal identity
  - image/documents area
  - attached footprint-drawing class
- but the current-public page pitch identity is not the needed residual class:
  - current visible `Min. Terminal Pitch` is `1.0`, not `1.50`
- this means the current Infineon near-hit does not produce:
  - a true `1.50 mm` owner exact row
  - a stronger `1.50 mm` current-public owner geometry surface

### 3. The safest result is still `no reopen`

- the package-portal candidate class remains useful as a search heuristic
- the current concrete Infineon public near-hit remains a false positive for the `1.50 mm` residual lane
- the repo-supported `1.50 mm` ceiling therefore still remains:
  - `IEC 60191-6-2` existence boundary
  - `IEC 61188-5-8 / 61188-6-2` standards-family boundary
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

- future AI should not treat `official package portal + footprint drawing` as enough by itself to reopen `1.50 mm`
- future AI should not mistake current Infineon `PG-BGA` near-hits for a real `1.50 mm` package exact-row recovery
- future AI should keep the stronger filter:
  - same owner surface
  - real `1.50 mm` pitch identity
  - printed PCB land-pattern geometry

## Continuation Rule

Keep `1.50 mm` as a watch-only residual under the same candidate-gated standard.

Do not reopen it again on Infineon package-portal pages unless a current-public page and attached owner drawing clearly expose both:

1. a true `1.50 mm` BGA package-pitch identity
2. printed PCB land-pattern geometry in the same owner-controlled public surface
