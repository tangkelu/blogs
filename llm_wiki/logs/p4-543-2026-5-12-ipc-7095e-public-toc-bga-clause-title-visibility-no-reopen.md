# P4-543 IPC-7095E Public TOC BGA Clause-Title Visibility No-Reopen

Date: 2026-05-12
Parent surfaces:

- `logs/p4-542-2026-5-12-j-std-013-open-toc-figure-title-visibility-still-no-reopen.md`
- `logs/p4-507-2026-5-11-ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_public_toc_visibility_strengthening`

## Purpose

Recheck a stronger public IPC standards surface and record the clause-title visibility that is still below the `1.50 mm` reopen gate.

This pass does not reopen `1.50 mm`.
It only strengthens the public-visibility wording for the already-landed IPC standards-side sources.

## Surface Rechecked

- `https://www.ipc.org/TOC/IPC-7095E_toc.pdf`

## What This Pass Confirmed

- the public `IPC-7095E` TOC exposes more than document identity and chapter numbers
- the visible public TOC also reaches clause-title level, including:
  - `Solder-Mask-Defined (SMD) BGA Land`
  - `Non-Solder-Mask Defined (NSMD) BGA Land`
  - `Land Patterns and Printed Board Considerations`
  - `BGA Package Pitch`
  - `Land Pattern Design`
  - `Ball Size Relationships`
- this is a stronger public standards anchor than `J-STD-013` TOC-only topic visibility, but it still does not expose reusable geometry payloads or criteria

## Why This Still Stays Below Reopen

- the public TOC still does not expose:
  - one exact `1.50 mm` land-pattern row
  - one visible pad-diameter comparison table payload
  - one visible solder-mask-opening criteria row
  - one reusable standards geometry figure body
- this strengthens `clause-title visibility`
  but still does not recover `public formal geometry`

## What Changed Since `P4-542`

- `P4-542` preserved the public `J-STD-013` TOC as topic and figure-title visibility
- this successor records that public IPC visibility is actually slightly stronger on the BGA guidance side:
  - it reaches clause-title labels for land pattern, pitch, and ball-size relationships
  - it still stops short of geometry payload

## Deliverables Strengthened

- `sources/registry/standards/ipc-7095e-toc.md`
- `facts/standards/ipc-7095e-bga-clause-title-visibility-boundary.md`

## Final Status

- lane result:
  - `stronger_public_toc_visibility_only`
- continuation state:
  - `1p50mm_standards_side_now_has_clause_title_visibility_but_still_no_public_formal_geometry`

## Continuation Rule

Future AI may now say:

- public `IPC-7095E` visibility reaches BGA land-pattern, pitch, and ball-size clause titles

Future AI still may not say:

- public `IPC-7095E` provides reusable `1.50 mm` land-pattern criteria
- the public TOC closes or reopens the `1.50 mm` residual
