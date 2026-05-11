# P4-424 E2 Silkscreen-Pad Conflict Authority Recovery

Date: 2026-05-10
Lane owner: `E2 narrow authority recovery`
Execution mode: `log_tracker_only`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf`

Parent surfaces:
- `logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`
- `logs/p4-384-2026-5-9-e2-safety-distance-taxonomy-and-spacing-boundary-route-integration.md`
- `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

## Purpose

Advance one `E2` lane beyond `single_pdf_usage_route_only` by confirming that this safety-distance article can now safely reuse an already-landed narrow official-fact boundary for silkscreen-to-pad overlap as a released-manufacturing-data conflict surface.

This pass is intentionally narrow.
It does not create a new fact card.
It promotes this PDF from route-only status because the repo already has enough support to keep its safest reusable surface inside the existing `released solder-mask / pad-definition manufacturing-data boundary + footprint review governance` posture.

## Existing Source Support Reused

This pass relies on already-landed support only:

1. `methods-ipc-solder-mask-layer-and-pad-definition-boundary`
   - already supports solder mask as released manufacturing data rather than only design-canvas intent
   - already supports guarded wording that pad-definition and solder-mask topics belong to controlled fabrication-data scope

2. `methods-padstack-origin-pin1-and-footprint-review-governance-boundary`
   - already supports pad, solder mask, footprint review, and documentation completeness as controlled review surfaces
   - already supports keeping silkscreen and adjacent review objects inside governance wording rather than numeric rule promotion

## What Was Promoted

Promoted for this single PDF only:

- silkscreen and solderable pad overlap may be reused as a released-manufacturing-data conflict topic
- spacing review may now keep silkscreen separate from conductor-spacing and mechanical-clearance families
- silkscreen conflict may be reused as a footprint-release and fabrication-output review surface before release
- this article's safest reuse may now stay attached to manufacturing-data completeness and conflict posture rather than generic spacing folklore

## What This Pass Does Not Promote

This pass still does not authorize:

- any exact silkscreen offset, text-size, stroke-width, or keepout numeric
- any exact trace, pad, via, hole, board-edge, or component spacing numeric
- any voltage-conditioned clearance truth or pass/fail threshold
- any CAD menu-path, auto-cleanup sufficiency, or factory-default correction claim
- any supplier capability, manufacturability guarantee, or promo/outcome claim

## E2 Lane Effect

`PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `silkscreen-to-pad overlap as released-manufacturing-data conflict` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `logs/p4-424-2026-5-10-e2-silkscreen-pad-conflict-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the reused boundaries remain narrower than any spacing table, silkscreen numeric rule, voltage rule, or factory-capability claim
- the per-PDF `E2` entry for `PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
