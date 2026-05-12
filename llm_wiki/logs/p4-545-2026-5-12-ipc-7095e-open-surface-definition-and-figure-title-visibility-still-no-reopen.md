# P4-545 IPC-7095E Open Surface Definition And Figure-Title Visibility Still No-Reopen

Date: 2026-05-12
Parent surfaces:

- `logs/p4-543-2026-5-12-ipc-7095e-public-toc-bga-clause-title-visibility-no-reopen.md`
- `logs/p4-542-2026-5-12-j-std-013-open-toc-figure-title-visibility-still-no-reopen.md`
- `logs/p4-507-2026-5-11-ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_public_visibility_strengthening`

## Purpose

Recheck the public `IPC-7095E` surface directly and record the stronger visible content that is still below the `1.50 mm` reopen gate.

This pass does not reopen `1.50 mm`.
It only strengthens the public-visibility wording for the already-landed `IPC-7095E` source/fact.

## Surface Rechecked

- `https://www.ipc.org/TOC/IPC-7095E_toc.pdf`

## What This Pass Confirmed

- the public `IPC-7095E` surface exposes more than document identity and clause headings
- the visible public surface also reaches body-level terminology definitions for:
  - `Solder-Mask-Defined (SMD) BGA Land`
  - `Non-Solder-Mask Defined (NSMD) BGA Land`
- the visible public surface also reaches attachment-site clause-title level, including:
  - `Land Diameter Size and Its Impact on Routing`
  - `Solder-Mask-Defined (SMD) Land and Metal-Defined Land Designs`
  - `Metal-Defined Lands`
  - `Solder-Mask-Defined (SMD) Lands`
  - `Via Size and Location`
  - `Parameters Affecting Solder Mask on BGAs`
- the visible public surface also reaches figure-title level, including:
  - `Figure 6-2 Solder Lands for BGA Components`
  - `Figure 6-3 Metal-Defined Land Attachment Profile`
  - `Figure 6-5 Solder Joint Geometry Contrast`
  - `Figure 6-10 Balls Anywhere Land Pattern Design for a Balls Anywhere BGA Component`

## Why This Still Stays Below Reopen

- the public surface still does not expose:
  - one exact `1.50 mm` land-pattern row
  - one visible pad-diameter comparison table payload
  - one visible solder-mask-opening criteria row
  - one reusable standards geometry figure body
- this strengthens `visible definitions + clause-title + figure-title visibility`
  but still does not recover `public formal geometry`

## What Changed Since `P4-543`

- `P4-543` preserved the public `IPC-7095E` surface as clause-title visibility
- this successor records that public visibility is actually slightly stronger:
  - it reaches visible SMD / NSMD BGA-land terminology definitions
  - it reaches more precise `6.2` attachment-site clause titles
  - it reaches figure-title labels for solder-land and land-pattern-design topics
  - it still stops short of geometry payload

## Deliverables Strengthened

- `sources/registry/standards/ipc-7095e-toc.md`
- `facts/standards/ipc-7095e-bga-clause-title-visibility-boundary.md`

## Final Status

- lane result:
  - `stronger_public_visibility_only`
- continuation state:
  - `1p50mm_standards_side_now_has_visible_definitions_plus_clause_and_figure_title_visibility_but_still_no_public_formal_geometry`

## Continuation Rule

Future AI may now say:

- public `IPC-7095E` visibility reaches SMD / NSMD BGA-land terminology definitions
- public `IPC-7095E` visibility reaches attachment-site and land-pattern figure-title labels

Future AI still may not say:

- public `IPC-7095E` provides reusable `1.50 mm` land-pattern criteria
- the public surface closes or reopens the `1.50 mm` residual
