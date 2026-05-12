# P4-542 J-STD-013 Open TOC Figure-Title Visibility Still No-Reopen

Date: 2026-05-12
Parent surfaces:

- `logs/p4-541-2026-5-12-j-std-013-public-toc-cbga-pbga-land-pattern-topic-visibility-no-reopen.md`
- `logs/p4-507-2026-5-11-ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_public_toc_visibility_strengthening`

## Purpose

Recheck the public `J-STD-013` TOC directly and record the stronger visible content that is still below the `1.50 mm` reopen gate.

This pass does not reopen `1.50 mm`.
It only strengthens the public-visibility wording for the already-landed `J-STD-013` TOC source/fact.

## Surface Rechecked

- `https://www.ipc.org/TOC/J-STD-013.pdf`
- `https://www.ipc.org/ipc-document-revision-table`

## What This Pass Confirmed

- the public `J-STD-013` TOC exposes more than document identity and top-level headings
- the visible public TOC also reaches figure-title level, including:
  - `Figure 4-3 Land Pattern Comparisons`
  - `Figure 5-2 Solder Mask Defined Land Patterns for CBGA and PBGA`
  - `Figure 5-3 Land Defined Land Patterns for CBGA and PBGA`
- the visible TOC also includes one `Variations - 1.50 Pitch` entry in the BGA package-details figure list
- the IPC revision table publicly marks `J-STD-013` as superseded by `IPC-7095`

## Why This Still Stays Below Reopen

- the public TOC still does not expose:
  - one exact `1.50 mm` land-pattern row
  - one visible pad-diameter comparison table payload
  - one visible solder-mask-opening criteria row
  - one reusable standards geometry figure body
- this strengthens `topic and figure-title visibility`
  but still does not recover `public formal geometry`

## What Changed Since `P4-541`

- `P4-541` preserved the public `J-STD-013` TOC as topic visibility
- this successor records that public visibility is actually slightly stronger:
  - it reaches figure-title labels
  - it reaches one visible `1.50 Pitch` figure-list entry
  - it still stops short of geometry payload

## Deliverables Strengthened

- `sources/registry/standards/j-std-013-toc.md`
- `facts/standards/j-std-013-cbga-pbga-land-pattern-topic-visibility-boundary.md`

## Final Status

- lane result:
  - `stronger_public_toc_visibility_only`
- continuation state:
  - `1p50mm_standards_side_now_has_topic_and_figure_title_visibility_but_still_no_public_formal_geometry`

## Continuation Rule

Future AI may now say:

- public `J-STD-013` visibility reaches `CBGA/PBGA land-pattern` topic headings and figure-title labels, including one visible `1.50 Pitch` entry

Future AI still may not say:

- public `J-STD-013` provides reusable `1.50 mm` land-pattern criteria
- the public TOC closes or reopens the `1.50 mm` residual
