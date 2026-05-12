# P4-506 E7 Graphic Alignment Shared-Reference-Frame And Same-Coordinate-System Authority Recovery

Date: 2026-05-11
Lane owner: `E7 narrow authority recovery`
Execution mode: `source_fact_tracker_refresh`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/简单好用！再也不用担心PCB图形对齐问题.pdf`

Parent surfaces:
- `logs/p4-351-2026-5-9-e7-graphic-alignment-workflow-route-integration.md`
- `logs/p4-458-2026-5-11-e7-residual-route-reaudit-and-no-write-closeout.md`
- `logs/p4-430-2026-5-10-e7-handoff-format-identity-authority-recovery.md`
- `logs/p4-431-2026-5-10-e7-assembly-input-package-boundary-authority-recovery.md`
- `facts/methods/cam-data-exchange-format-boundary.md`
- `facts/methods/pcba-test-method-input-package-boundary.md`

## Purpose

Advance one `E7` lane beyond `single_pdf_usage_route_only` by adding a stronger public format-owner boundary for the safest promotable sub-surface of `简单好用！再也不用担心PCB图形对齐问题.pdf`.

This pass is intentionally narrow.
It creates one new format-owner source record, one new fact card, and one new lane log, but it does not turn the whole PDF into reusable authority.

## New Source Support Landed

This pass adds one current-public official surface:

1. `ucamco-gerber-layer-format-specification-revision-2024-05`
   - supports same-coordinate-system registration across Gerber layer data
   - supports `.SameCoordinates` as file alignment language
   - supports `ident` and `ProjectId` for revision / coordinate-system identification
   - supports same offset, no mirroring, and 1:1 scale posture

## Fact Boundary Landed

This pass adds:

- `facts/methods/gerber-layer-shared-reference-frame-and-same-coordinate-system-registration-boundary.md`

The new boundary is intentionally limited to:

- shared-reference-frame correction
- same-coordinate-system registration
- revision-comparison alignment

## What Was Promoted

Promoted for this single PDF only:

- graphic alignment may now be reused as a same-coordinate-system registration problem
- imported layer graphics may now be reused as a shared-reference-frame problem
- multi-layer revision comparison may now be reused as a registration problem with Ucamco format-owner support

## What This Pass Does Not Promote

This pass still does not authorize:

- UI shortcut or menu-path authority
- auto-fix sufficiency
- universal alignment-readiness
- branded convenience or superiority claims
- speed, cost, defect, or outcome claims
- local-subregion move workflow authority
- library-adjustment authority
- coordinate-to-footprint doctrine
- coordinate-to-graphic assembly-readiness claims

## Why P4-458 Was Still Correct

`P4-458` remains correct as a no-write re-audit of the older weaker surface.
This lane moves only because a genuinely stronger format-owner coordinate-registration specification has now been added.

## E7 Lane Effect

`简单好用！再也不用担心PCB图形对齐问题.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `shared-reference-frame + same-coordinate-system registration` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `sources/registry/standards/ucamco-gerber-layer-format-specification-revision-2024-05.md`
- `facts/methods/gerber-layer-shared-reference-frame-and-same-coordinate-system-registration-boundary.md`
- `logs/p4-506-2026-5-11-e7-graphic-alignment-shared-reference-frame-and-same-coordinate-system-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the new fact remains narrower than UI-step claims, package-library authority, or whole-package readiness claims
- the per-PDF `E7` entry for `简单好用！再也不用担心PCB图形对齐问题.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
