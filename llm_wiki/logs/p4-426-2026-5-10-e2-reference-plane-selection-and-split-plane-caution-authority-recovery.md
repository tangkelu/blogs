# P4-426 E2 Reference-Plane Selection And Split-Plane Caution Authority Recovery

Date: 2026-05-10
Lane owner: `E2 narrow authority recovery`
Execution mode: `log_tracker_only`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/PCB内层的可制造性设计.pdf`

Parent surfaces:
- `logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`
- `logs/p4-350-2026-5-9-e2-inner-layer-manufacturability-route-integration.md`
- `facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`
- `wiki/processes/rigid-board-family-and-layer-boundaries.md`

## Purpose

Advance one `E2` lane beyond `single_pdf_usage_route_only` by confirming that this inner-layer article can now safely reuse an already-landed narrow official-fact boundary for `reference-plane selection and split-plane crossing as return-path continuity caution`.

This pass is intentionally narrow.
It does not create a new fact card.
It promotes this PDF from route-only status because the repo already has enough support to keep its safest reusable surface inside the existing `ADI/TI-backed return-path continuity and split-plane caution` posture.

## Existing Source Support Reused

This pass relies on already-landed support only:

1. `methods-ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity`
   - already supports reference-plane choice as return-path and routing-discipline planning
   - already supports split-plane crossing as a return-current discontinuity caution
   - already keeps this wording inside continuity, routing discipline, and layer-transition handling rather than exact recipe or outcome claims

2. `P4-350`
   - already constrains this PDF to route-only posture
   - already separates reusable reference-plane and split-plane caution language from broader inner-layer taxonomy, stackup-organization, and capability wording

## What Was Promoted

Promoted for this single PDF only:

- reference-plane choice belongs to return-path and shielding-aware planning
- ground-plane preference may be kept only as qualitative reference-plane posture
- key-signal routing across plane splits can be kept as a return-path discontinuity caution class

## What This Pass Does Not Promote

This pass still does not authorize:

- any plane-size, offset, or setback numeric
- any exact stackup order, adjacency, or coupling recipe
- any BGA inner-region spacing, copper-bridge, or dense-geometry claim
- any current bottleneck, burn, or open-circuit certainty claim
- any yield, quality, capability, or cost-reduction claim
- any branded checker-completeness or tool-sufficiency claim

This pass also does not newly elevate these broader route-only surfaces:

- `inner_layer_power_ground_and_reference_plane_taxonomy`
- `power_ground_adjacency_as_stackup_organization_topic`
- `inner_layer_review_as_multilayer_process_branch_only`

## E2 Lane Effect

`PCB内层的可制造性设计.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `reference-plane selection and split-plane crossing as return-path continuity caution` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `logs/p4-426-2026-5-10-e2-reference-plane-selection-and-split-plane-caution-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the reused boundary remains narrower than broad inner-layer taxonomy, stackup-organization, exact recipe language, or capability claims
- the per-PDF `E2` entry for `PCB内层的可制造性设计.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
