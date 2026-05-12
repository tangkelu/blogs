# P4-541 J-STD-013 Public TOC CBGA/PBGA Land-Pattern Topic Visibility No-Reopen

Date: 2026-05-12
Parent surfaces:

- `logs/p4-507-2026-5-11-ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md`
- `logs/p4-538-2026-5-12-master-plan-resync-after-current-state-refresh.md`
- `logs/p4-540-2026-5-12-jcet-pbga-family-pitch-availability-source-and-boundary-landing.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_standards_side_topic_visibility_recheck`

## Purpose

Check whether one public IPC TOC surface adds anything useful to the still-open `1.50 mm` package residual without pretending that a formal public geometry row has been recovered.

This pass does not reopen `1.50 mm`.
It only tests whether the public `J-STD-013` TOC is worth preserving as standards-side topic visibility.

## Surface Rechecked

- `https://www.ipc.org/TOC/J-STD-013.pdf`

## What This Pass Confirmed

- the public `J-STD-013` TOC is a real current-public IPC surface
- it visibly exposes `CBGA/PBGA land pattern` as a standards topic rather than only document identity
- the visible TOC headings include:
  - `Land Pattern Comparisons`
  - `Solder Mask Defined Land Patterns for CBGA and PBGA`
  - `Land Defined Land Patterns for CBGA and PBGA`

## Why This Still Stays Below Reopen

- the public TOC does not expose:
  - one exact `1.50 mm` geometry row
  - one reusable `PBGA` land-pattern comparison table
  - one public criteria surface for pad diameter or solder-mask opening
- this keeps `J-STD-013` below the current `legitimately public formal standards geometry surface` gate
- the pass is therefore stronger than plain standards identity, but still weaker than the already-landed public IPC geometry boundary from `P4-507`

## What Landed Safely

### New source record

- `sources/registry/standards/j-std-013-toc.md`

### New standards boundary fact

- `facts/standards/j-std-013-cbga-pbga-land-pattern-topic-visibility-boundary.md`

## Final Status

- lane result:
  - `standards_topic_visibility_raise_only`
- continuation state:
  - `1p50mm_now_has_one_more_public_ipc_topic_visibility_anchor_but_still_no_public_formal_geometry_row`

## Continuation Rule

Future AI may now say:

- public IPC material visibly treats `CBGA/PBGA land pattern` as a named standards topic

Future AI still may not say:

- the public `J-STD-013` TOC exposes reusable `1.50 mm` land-pattern geometry
- the current `1.50 mm` residual is reopened or closed on this TOC alone

The clean continuation remains:

1. watch for one legitimately public formal standards geometry surface above the current `IEC + IPC-hosted` stack
2. or watch for one newly surfaced or newly retrievable owner surface with both true `1.50 mm` pitch identity and same-surface PCB geometry
