# P4-509 Amkor PBGA 1.50 mm Family Near-Hit No-Reopen

Date: 2026-05-11
Parent surfaces:

- `logs/p4-489-2026-5-11-1p50mm-owner-and-standards-candidate-scout-no-reopen-successor.md`
- `logs/p4-507-2026-5-11-ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md`
- `logs/p4-508-2026-5-11-infineon-p-bga-pg-bga-current-access-blocker-no-reopen.md`

Execution mode: `subagent_aided_candidate_gated_negative_scout`

## Purpose

Record one more bounded scout against a new owner-side class for the still-open `1.50 mm` residual lane.

This pass is not a reopen.
It checks whether the current-public Amkor package-family page plus linked official datasheet exceed the current `1.50 mm` ceiling.

## Candidate Gate Rechecked

The current lane should reopen only if one of the following appears:

1. a new materially stronger current-public owner exact row
2. a legitimately public official geometry surface above the current public ceiling

## Candidate Rechecked

- official Amkor package-family page:
  - `https://amkor.com/packaging/laminate/pbga/`
- linked official datasheet:
  - `https://amkormarcomexternal.blob.core.windows.net/amkordotcom/wp-content/uploads/2018/02/PBGA_DS520.pdf`

## What This Pass Confirmed

- this is a real new owner-side class rather than search-noise or a repeated vendor
- the current-public Amkor package-family page and datasheet do expose true `1.50 mm` family identity:
  - page wording includes `1.00, 1.27 & 1.50 mm standard ball pitch available`
  - the official PDF also includes `1.00, 1.27 & 1.50 mm standard ball pitch available`
- the public package-family material is therefore stronger than:
  - metadata-only standards pages
  - generic app-note prose
  - coordinate-hit false positives where visible `1.50` does not mean true pitch identity

## Why It Still Stays Below Reopen

- the current surfaced Amkor public material does not expose:
  - one package-scoped printed PCB land-pattern geometry row
  - one same-surface footprint drawing with recommended PCB pad geometry
  - one owner exact row that exceeds the current `NXP + Renesas + AMD` stack
- the visible public content stays at package-family capability, offering, cross-section, thermal, and manufacturing framing
- this keeps the candidate below the reopen gate even though the `1.50 mm` package-family identity is real

## Audit Result

- no new `sources/registry/` record landed
- no new `facts/` card landed
- no `wiki/` route changed
- no completion threshold changed
- the safest result is `no reopen`

## What This Pass Fixes

- future AI should not treat true `1.50 mm` owner family identity by itself as enough to reopen the lane
- future AI should not mistake the Amkor family page plus linked datasheet for one same-surface public footprint-geometry authority
- future AI may keep Amkor as a stronger near-hit than noise, but still below the current reopen gate

## Continuation Rule

Keep `1.50 mm` as a watch-only residual under the same candidate-gated standard.

Do not reopen it on current-public Amkor package-family material unless a later public owner surface also exposes:

1. one true package-scoped `1.50 mm` geometry row
2. or one same-surface footprint drawing with printed PCB land-pattern geometry
