# P4-425 E2 Reference-Plane And Return-Path Authority Recovery

Date: 2026-05-10
Lane owner: `E2 narrow authority recovery`
Execution mode: `log_tracker_only`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/PCB叠层顺序规划配置方案.pdf`

Parent surfaces:
- `logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`
- `logs/p4-381-2026-5-9-e2-stackup-planning-and-reference-plane-route-integration.md`
- `logs/p4-350-2026-5-9-e2-inner-layer-manufacturability-route-integration.md`
- `facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`

## Purpose

Advance one `E2` lane beyond `single_pdf_usage_route_only` by confirming that this stackup-planning article can now safely reuse an already-landed narrow official-fact boundary for `reference-plane continuity and return-path routing discipline`, including split-plane continuity caution.

This pass is intentionally narrow.
It does not create a new fact card.
It promotes this PDF from route-only status because the repo already has enough support to keep its safest reusable surface inside the existing `ADI/TI-backed return-path continuity and split-plane caution` posture.

## Existing Source Support Reused

This pass relies on already-landed support only:

1. `methods-ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity`
   - already supports reference-plane continuity and return-path quality as routing-planning concerns
   - already supports caution when signals cross plane splits or slots because return-current continuity degrades
   - already keeps this wording inside routing discipline and layer-transition handling rather than recipe or outcome claims

2. `P4-381` and `P4-350`
   - already constrain this PDF to a route-only posture
   - already separate the reusable return-path and split-plane continuity lane from broader stackup, decoupling, and capability language

## What Was Promoted

Promoted for this single PDF only:

- reference-plane continuity and return-path quality may be reused as routing-planning concerns
- high-speed signals may be reused as needing caution near split power-reference regions because return-path continuity can degrade
- this article may now keep its safest official reuse attached to return-path routing discipline rather than only to generic stackup-planning wording

## What This Pass Does Not Promote

This pass still does not authorize:

- any exact layer-count, board-thickness, dielectric-thickness, or material-thickness example
- any exact stackup ordering, spacing, coupling, or setback rule
- any `HDI`, laser-drill, controlled-depth, or build-capability closure
- any supplier, manufacturer, cost, yield, or lead-time claim
- any exact decoupling-loop, EMI, or performance-outcome claim
- any impedance-geometry recipe, tolerance, or coupon-coverage claim
- any universal split-plane keepout, crossing, or transition default

This pass also does not newly elevate these broader route-only surfaces:

- `stackup_planning_as_multivariable_tradeoff_posture`
- `signal_power_ground_as_distinct_layer_role_families`
- `decoupling_short_path_as_layout_planning_surface_only`
- `controlled_impedance_as_planning_and_validation_posture`

## E2 Lane Effect

`PCB叠层顺序规划配置方案.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `reference-plane continuity and return-path routing discipline` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `logs/p4-425-2026-5-10-e2-reference-plane-and-return-path-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the reused boundary remains narrower than broad stackup planning, impedance planning, exact recipe language, or capability claims
- the per-PDF `E2` entry for `PCB叠层顺序规划配置方案.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
