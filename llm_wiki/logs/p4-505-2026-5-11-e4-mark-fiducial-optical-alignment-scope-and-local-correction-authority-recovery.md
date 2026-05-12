# P4-505 E4 Mark Fiducial Optical-Alignment Scope And Local-Correction Authority Recovery

Date: 2026-05-11
Lane owner: `E4 narrow authority recovery`
Execution mode: `source_fact_tracker_refresh`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/PCB板的Mark点设计对SMT重要性.pdf`

Parent surfaces:
- `logs/p4-312-2026-5-8-pcb-article-e4-usage-route-integration.md`
- `logs/p4-353-2026-5-9-e4-mark-fiducial-role-route-integration.md`
- `logs/p4-460-2026-5-11-e4-mark-fiducial-route-reaudit-and-no-write-closeout.md`
- `facts/methods/cam-data-exchange-format-boundary.md`
- `sources/registry/standards/ucamco-gerber-format-page.md`

## Purpose

Advance one `E4` lane beyond `single_pdf_usage_route_only` by adding materially stronger public authority for the safest promotable sub-surface of `PCB板的Mark点设计对SMT重要性.pdf`.

This pass is intentionally narrow.
It does create new source records and one fact card, but it still does not turn the whole article into reusable authority.

## New Source Support Landed

This pass adds three current-public official surfaces:

1. `yamaha-smt-glossary-fiducial-mark`
   - supports `fiducial mark` as a board reference point
   - supports placement / printing equipment alignment context

2. `yamaha-yrm-d-multiple-marks-and-local-correction`
   - supports `multiple marks`
   - supports `individual local marks`
   - supports `local correction`
   - supports guarded poor-accuracy-PCB context for local-mark usefulness

3. `kicad-pcb-editor-fiducial-fabrication-property`
   - supports the explicit CAD-owner split:
     - `Fiducial, global to board`
     - `Fiducial, local to footprint`

## Fact Boundary Landed

This pass adds:

- `facts/methods/fiducial-optical-alignment-global-local-scope-and-local-correction-boundary.md`

The new boundary is intentionally limited to:

- `Mark` / fiducial as optical alignment reference
- `board-global` versus `footprint-local` fiducial scope split
- `local marks` as local-correction posture

## What Was Promoted

Promoted for this single PDF only:

- fiducials may now be reused as `optical alignment reference` vocabulary with machine-owner support
- the article's safest `global vs local` sub-surface may now be reused as a controlled `board-global vs footprint-local` split
- local fiducials may now be reused as `local correction` posture rather than only as article-side high-precision wording

## What This Pass Does Not Promote

This pass still does not authorize:

- panel-level fiducial doctrine
- asymmetry as orientation-disambiguation doctrine
- visibility, cleanliness, contamination, or obstruction conditions as official reusable doctrine
- any fiducial geometry, opening, keepout, or copper-clearance numeric
- any count default, diagonal-corner arrangement, or panel-placement rule
- any package-specific mandatory `QFP` / `BGA` local-mark rule
- any no-mark workaround, fixture-added-mark, or stencil-substitution guidance
- any precision, efficiency, yield, cost, schedule, or machine-readiness guarantee

## Why P4-460 Was Still Correct

`P4-460` remains correct as a no-write re-audit of the older weak source set:

- `IPC-7525C` public metadata
- internal stencil-support wording
- `Ucamco` Gerber fiducial attribute vocabulary

Those sources still do stay below reopen on their own.
This lane moves only because a genuinely stronger machine-owner plus CAD-owner source layer has now been added.

## E4 Lane Effect

`PCB板的Mark点设计对SMT重要性.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `optical alignment + board-global vs footprint-local scope + local-correction posture` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `sources/registry/methods/yamaha-smt-glossary-fiducial-mark.md`
- `sources/registry/methods/yamaha-yrm-d-multiple-marks-and-local-correction.md`
- `sources/registry/methods/kicad-pcb-editor-fiducial-fabrication-property.md`
- `facts/methods/fiducial-optical-alignment-global-local-scope-and-local-correction-boundary.md`
- `logs/p4-505-2026-5-11-e4-mark-fiducial-optical-alignment-scope-and-local-correction-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the new fact remains narrower than panel doctrine, visibility doctrine, geometry/count rules, or workaround claims
- the per-PDF `E4` entry for `PCB板的Mark点设计对SMT重要性.pdf` no longer understates the promoted sub-surface as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
