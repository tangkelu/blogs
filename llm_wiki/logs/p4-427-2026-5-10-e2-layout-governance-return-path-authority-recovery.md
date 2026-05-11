# P4-427 E2 Layout-Governance Return-Path Authority Recovery

Date: 2026-05-10
Lane owner: `E2 narrow authority recovery`
Execution mode: `log_tracker_only`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/印制电路板设计重点.pdf`

Parent surfaces:
- `logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`
- `logs/p4-383-2026-5-9-e2-design-priority-and-layout-governance-route-integration.md`
- `facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`
- `logs/p4-425-2026-5-10-e2-reference-plane-and-return-path-authority-recovery.md`

## Purpose

Advance one `E2` lane beyond `single_pdf_usage_route_only` by confirming that this design-priority article can now safely reuse an already-landed narrow official-fact boundary for `reference-plane continuity and return-path routing discipline`, including split-plane caution.

This pass is intentionally narrow.
It does not create a new fact card.
It promotes this PDF from route-only status because the repo already has enough support to keep its safest reusable surface inside the existing `ADI/TI-backed return-path continuity and split-plane caution` posture.

## Existing Source Support Reused

This pass relies on already-landed support only:

1. `methods-ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity`
   - already supports reference-plane continuity and return-path quality as routing-planning concerns
   - already supports split-plane caution when return-current continuity can degrade
   - already keeps this wording inside execution-boundary routing discipline rather than formula or outcome claims

2. `P4-383`
   - already constrains this PDF to route-only posture
   - already separates reusable routing priority, loop-awareness, and return-path wording from spacing tables, formulas, and capability language

3. `P4-425`
   - already fixed the same narrow authority lane for one adjacent `E2` article
   - strengthens consistency that this pass is limited to the same reused return-path continuity boundary rather than a broader layout-governance promotion

## What Was Promoted

Promoted for this single PDF only:

- routing priorities, loop-area awareness, split-plane caution, and return-path continuity may be written as execution-boundary language
- reference-plane continuity and return-path quality may be reused as routing-planning concerns
- high-speed signals may be reused as needing caution near split power-reference regions because return-path continuity can degrade

## What This Pass Does Not Promote

This pass still does not authorize:

- any exact component, pad, board-edge, or package spacing numeric
- any `3W/10W/20H` or exact angle-formula rule
- any exact current-carrying trace table or via-table claim
- any exact impedance geometry or tolerance rule
- any universal performance, quality, EMI, or manufacturability outcome claim
- any tool-recipe, vendor-default, or process-capability claim
- any universal split-plane keepout, crossing, or transition default

## E2 Lane Effect

`印制电路板设计重点.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `reference-plane continuity and return-path routing discipline` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `logs/p4-427-2026-5-10-e2-layout-governance-return-path-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the reused boundary remains narrower than broad layout-governance posture, spacing formulas, exact current or impedance tables, or capability claims
- the per-PDF `E2` entry for `印制电路板设计重点.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
