# P4-418 E3 Hole-Spacing Authority Recovery

Date: 2026-05-10
Lane owner: `E3 narrow authority recovery`
Execution mode: `log_tracker_only`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/PCB设计孔间距的DFM可靠性.pdf`

Parent surfaces:
- `logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
- `logs/p4-396-2026-5-10-e3-hole-spacing-reliability-boundary-route-integration.md`
- `facts/methods/hole-spacing-reliability-boundary.md`
- `facts/methods/cam-data-exchange-format-boundary.md`
- `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`

## Purpose

Advance one `E3` lane beyond `single_pdf_usage_route_only` by confirming that this hole-spacing article can now safely reuse an already-landed narrow official-fact boundary for hole spacing as a standards-adjacent reliability-review topic.

This pass is intentionally narrow.
It does not create a new fact card.
It promotes this PDF from route-only status because the repo already has enough support to keep its safest reusable surface inside the existing `hole wall to hole wall / hole-to-hole clearance / hole-to-object clearance` boundary.

## Existing Source Support Reused

This pass relies on already-landed support only:

1. `methods-hole-spacing-reliability-boundary`
   - already supports hole spacing as a standards-adjacent and CAD-owner reliability-review boundary
   - already supports annular-ring weakening, breakout-like damage, cracks and wicking, drill-wander caution, and CAF risk context

2. `methods-cam-data-exchange-format-boundary`
   - already supports fabrication-package completeness and explicit released-output expression

3. `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`
   - already supports design-intent versus released-output boundary and pre-release handoff review posture

## What Was Promoted

Promoted for this single PDF only:

- hole spacing may be reused as a reliability and failure-risk review topic
- hole wall to hole wall may be reused as governed design-rule vocabulary
- hole-to-hole clearance may be reused as CAD-owner manufacturing-rule vocabulary
- hole-to-object clearance may be reused as CAD-owner manufacturing-rule vocabulary
- annular-ring weakening, breakout-like damage, cracks and wicking, drill-wander caution, and CAF risk context may be reused as guarded review vocabulary

## What This Pass Does Not Promote

This pass still does not authorize:

- any universal spacing threshold or acceptance rule
- any exact annular-ring or breakout table
- any supplier-capability claim
- any exact numeric value extracted from the article's threshold text
- any manufacturability guarantee or reliability-outcome claim

## E3 Lane Effect

`PCB设计孔间距的DFM可靠性.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `hole-spacing as standards-adjacent reliability-review boundary` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `logs/p4-418-2026-5-10-e3-hole-spacing-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the reused fact boundary remains narrower than any universal spacing law or acceptance criterion
- the per-PDF `E3` entry for `PCB设计孔间距的DFM可靠性.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
