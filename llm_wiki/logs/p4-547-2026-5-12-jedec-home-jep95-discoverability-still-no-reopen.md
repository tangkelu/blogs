# P4-547 JEDEC Home JEP95 Discoverability Still No-Reopen

Date: 2026-05-12
Parent surfaces:

- `logs/p4-489-2026-5-11-1p50mm-owner-and-standards-candidate-scout-no-reopen-successor.md`
- `logs/p4-545-2026-5-12-ipc-7095e-open-surface-definition-and-figure-title-visibility-still-no-reopen.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_public_discoverability_strengthening`

## Purpose

Recheck the official JEDEC public surface and record the stronger discoverability wording that is still below the `1.50 mm` reopen gate.

This pass does not reopen `1.50 mm`.
It only strengthens the public-discoverability wording for the JEDEC side of the standards lane.

## Surface Rechecked

- `https://www.jedec.org/`

## What This Pass Confirmed

- the official JEDEC homepage publicly exposes:
  - `Search & Download JEDEC Documents`
  - `Search by keyword or document number`
- the same official homepage publicly lists:
  - `Registered Outlines: JEP95`
- this is stronger than vague `JEDEC probably has something` wording because it makes:
  - official document-search discoverability visible
  - official `JEP95` registered-outlines discoverability visible

## Why This Still Stays Below Reopen

- the public homepage still does not expose:
  - one exact `1.50 mm` land-pattern row
  - one public JEP95 geometry table payload
  - one reusable BGA pad-diameter criteria row
  - one recoverable same-surface standards geometry figure body
- this strengthens `official discoverability only`
  but still does not recover `public formal geometry`

## What Changed Since `P4-489`

- `P4-489` preserved the JEDEC side as a primary lane that did not yet produce one recoverable current-public official surface strong enough to raise the ceiling
- this successor records that the official public side is at least slightly stronger than pure uncertainty:
  - the homepage itself visibly supports JEDEC document-search discoverability
  - the homepage itself visibly names `Registered Outlines: JEP95`
  - it still stops short of content recovery

## Deliverables Landed

- `sources/registry/standards/jedec-home-document-search-and-jep95-discoverability.md`
- `facts/standards/jedec-home-jep95-document-discoverability-boundary.md`

## Final Status

- lane result:
  - `stronger_public_discoverability_only`
- continuation state:
  - `1p50mm_standards_side_now_has_official_jedec_document_search_and_jep95_discoverability_but_still_no_public_formal_geometry`

## Continuation Rule

Future AI may now say:

- official JEDEC public discoverability exists for document search
- official JEDEC public discoverability visibly names `Registered Outlines: JEP95`

Future AI still may not say:

- public JEDEC geometry for `1.50 mm` BGA land-pattern design is recovered
- the official homepage closes or reopens the `1.50 mm` residual
