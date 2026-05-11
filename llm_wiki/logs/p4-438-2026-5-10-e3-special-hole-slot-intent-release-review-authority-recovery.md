# P4-438 E3 Special Hole-Slot Intent Release-Review Authority Recovery

Date: 2026-05-10
Lane owner: `E3 narrow authority recovery`
Execution mode: `log_tracker_only`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/器件引脚的方槽、方孔如何避坑？.pdf`

Parent surfaces:
- `logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
- `logs/p4-376-2026-5-9-e3-square-lead-special-hole-intent-release-check-route-integration.md`
- `logs/p4-437-2026-5-10-e3-hole-slot-fabrication-intent-output-completeness-authority-recovery.md`
- `logs/p4-368-2026-5-9-e3-hole-slot-terminology-gap-note.md`
- `facts/methods/package-to-footprint-and-pin-count-alignment-review-boundary.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`

## Purpose

Advance one `E3` lane beyond `single_pdf_usage_route_only` by confirming that this square-lead special-hole article can now safely reuse an already-landed narrow official-fact boundary for `special hole-slot intent release review`, with non-round lead shape and explicit special-feature expression kept strictly inside package-review and released-output completeness posture.

This pass is intentionally narrow.
It does not create a new fact card.
It promotes this PDF from route-only status because the repo already has enough support to keep its safest reusable surface inside the existing `package-to-footprint review trigger + released-package completeness + special-feature annotation review` boundary.

## Existing Source Support Reused

This pass relies on already-landed support only:

1. `P4-437`
   - already established that intended `hole / slot` features may be reused as released fabrication-package completeness review surfaces
   - already established that omitted or misexpressed hole-slot intent may be reused as manufacturing-data completeness review topics
   - already established that release-check support surfaces must stay narrower than universal file-package doctrine or tool-specific recipes

2. `methods-package-to-footprint-and-pin-count-alignment-review-boundary`
   - already supports package identity and footprint-library alignment as explicit review-trigger language
   - already supports non-default package-to-footprint mismatch staying inside governance review rather than silent acceptance

3. `methods-padstack-origin-pin1-and-footprint-review-governance-boundary`
   - already supports footprint, pad, drill, and solder-mask objects as controlled review vocabulary rather than numeric defaults
   - already supports documentation-governance and released-package explicitness posture

4. `processes-pcb-design-data-exchange-and-tool-boundaries`
   - already supports the boundary that design-canvas presence does not equal released-output correctness

5. `P4-376`
   - already constrained this PDF to route-only posture
   - already named square or non-round lead shape as package-to-footprint review trigger, square-hole / square-slot request as explicit fabrication-intent expression, design-canvas appearance as separate from released-output correctness, and pre-release special-feature annotation review while blocking terminology closure, workaround defaults, tool behavior, and outcome claims

6. `P4-368`
   - already keeps hole-slot wording outside official terminology closure
   - already prevents this lane from expanding into square-hole or square-slot taxonomy truth

## What Was Promoted

Promoted for this single PDF only:

- square or non-round lead shape may be reused as a `package-to-footprint review trigger` when the required released feature is non-default
- square-hole or square-slot request may be reused only as `explicit special-feature intent that must be clearly carried into the released package`
- design-canvas square-like appearance may be reused only as `insufficient proof of released-output correctness`
- special hole-slot notes, drill-drawing support, or explicit annotation may be reused only as `release-check support surfaces`
- omitted or misexpressed special hole-slot intent may be reused only as a `guarded manufacturing-data completeness review` topic

## What This Pass Does Not Promote

This pass still does not authorize:

- any official square-hole or square-slot terminology closure
- any hole, slot, drill, clearance, or manufacturability numeric
- any workaround default, process default, or geometry default
- any CAD menu path, UI workflow, export-step recipe, or checker-sufficiency claim
- any manufacturability certainty, supplier capability, insertion-success, quality, cost, or cycle-time outcome claim
- any plated / non-plated taxonomy closure or mandatory annotation doctrine

## E3 Lane Effect

`器件引脚的方槽、方孔如何避坑？.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `special hole-slot intent release review` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `logs/p4-438-2026-5-10-e3-special-hole-slot-intent-release-review-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the reused boundary remains narrower than terminology closure, hole-slot numerics, workaround defaults, CAD-specific recipes, checker sufficiency, or manufacturability-outcome claims
- the per-PDF `E3` entry for `器件引脚的方槽、方孔如何避坑？.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
