# P4-546 onsemi AND8075 Official BGA Guidance Wrong-Pitch No-Reopen

Date: 2026-05-12
Parent surfaces:

- `logs/p4-489-2026-5-11-1p50mm-owner-and-standards-candidate-scout-no-reopen-successor.md`
- `logs/p4-486-2026-5-11-microchip-ti-adi-1p50mm-candidate-class-scout-no-reopen.md`
- `logs/p4-536-2026-5-12-date-rollover-1p50mm-current-public-candidate-recheck-no-reopen.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_candidate_gated_negative_scout`

## Purpose

Record one more bounded recheck against the `onsemi` owner class using one directly retrievable official BGA guidance note, so future `/goal` work does not treat `onsemi` as an unreviewed blank for the still-open `1.50 mm` residual lane.

This pass is not a reopen.
It checks whether one current-public `onsemi` official BGA guidance surface clears the same `true 1.50 mm pitch + same-surface PCB geometry` gate.

## Surface Rechecked

- `https://www.onsemi.com/download/application-notes/pdf/and8075-d.pdf`

## Candidate Gate Rechecked

The lane should reopen only if one current-public owner surface visibly exposes both:

1. true `1.50 mm` pitch identity
2. printed PCB footprint or land-pattern geometry on the same owner-controlled surface

## Findings

### 1. `onsemi` current-public BGA guidance is real and stronger than vague package-hit noise

- the public `onsemi` application note `AND8075/D Board Mounting Considerations for FCBGA Packages` is directly retrievable
- the note is a real owner-controlled BGA guidance surface with:
  - explicit `SMD` and `NSMD` pad terminology
  - printed BGA pad-dimension tables
  - printed trace-tapering tables
  - process and inspection guidance

### 2. The visible pitch coverage still stays below the `1.50 mm` gate

- the note states that the most commonly used grid spacings are:
  - `0.8 mm`
  - `1.0 mm`
  - `1.27 mm`
- the printed pad-dimension tables themselves cover only:
  - `0.80 mm Ball Pitch`
  - `1.00 mm Ball Pitch`
- this means the current surfaced public `onsemi` note does not provide:
  - one true `1.50 mm` owner exact row
  - one same-surface `1.50 mm` pitch identity plus printed PCB land-pattern geometry

### 3. The safest result remains `no reopen`

- `onsemi` now has one cleaner current-public official BGA-guidance hit than vague package-drawing surfacing alone
- but the visible pitch class still stops below `1.50 mm`
- this keeps the current `onsemi` owner class in the same broad below-gate family as other wrong-pitch or non-target BGA guidance surfaces

## Audit Result

- no new `sources/registry/` record landed
- no new `facts/` card landed
- no `wiki/` route changed
- no completion threshold changed
- the safest result remains `no reopen`

## What This Pass Fixes

- future AI should not treat `onsemi` as an unreviewed current-public owner blank for the `1.50 mm` lane
- future AI should not treat public `onsemi` BGA guidance as if it already contains a `1.50 mm` owner exact row
- future AI may read `onsemi` more narrowly as:
  - one directly retrievable owner BGA-guidance surface
  - with real pad-geometry tables
  - but still wrong-pitch for the current `1.50 mm` gate

## Continuation Rule

Keep `1.50 mm` as a watch-only residual under the same candidate-gated standard.

Do not reopen it on current-public `onsemi` BGA guidance unless a later public owner surface also exposes:

1. one true package-scoped `1.50 mm` geometry row
2. or one same-surface footprint drawing with printed PCB land-pattern geometry
