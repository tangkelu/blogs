# P4-428 E2 Board-Edge Copper And Milling-Path Authority Recovery

Date: 2026-05-10
Lane owner: `E2 narrow authority recovery`
Execution mode: `log_tracker_only`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/PCB可制造性设计及案例分析之线路篇.pdf`

Parent surfaces:
- `logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`
- `logs/p4-385-2026-5-9-e2-copper-balance-and-routing-expression-route-integration.md`
- `facts/methods/depanelization-cleanliness-and-edge-risk-boundary.md`

## Purpose

Advance one `E2` lane beyond `single_pdf_usage_route_only` by confirming that this copper-expression and routing article can now safely reuse an already-landed narrow official-fact boundary for `board-edge copper and milling-path conflict review`, with one guarded extension for `outer-layer bare-copper band as release-expression object`.

This pass is intentionally narrow.
It does not create a new fact card.
It promotes this PDF from route-only status because the repo already has enough support to keep its safest reusable surface inside the existing `edge-risk / profiling-intent / release-review` posture.

## Existing Source Support Reused

This pass relies on already-landed support only:

1. `methods-depanelization-cleanliness-and-edge-risk-boundary`
   - already supports cut-edge review, conductive-fragment review, and edge-risk handling as real singulation and downstream review topics
   - already supports writing edge-near conductive features as guarded release-review objects rather than as decorative layout wording
   - already keeps this wording inside qualitative engineering review posture rather than numeric clearance or guaranteed outcome claims

2. `P4-385`
   - already constrains this PDF to route-only posture
   - already separated reusable board-edge copper / milling-path conflict and outer-layer bare-copper expression wording from numerics, tool behavior, and capability language

Adjacent consistency note only:

3. `P4-421`
   - confirms that the repo already uses a similarly narrow board-edge review posture in a neighboring article cluster
   - is not the core authority for this `E2` pass and should not be read as broad cross-cluster promotion by itself

## What Was Promoted

Promoted for this single PDF only:

- board-edge nets, copper, and milling paths may be reused as `edge-conflict and release-review` topics
- edge-near conductive features may be reused as needing review against profiling intent before release
- outer-layer decorative or exposed copper bands may be reused as release-expression objects that should stay unambiguous relative to profiling or program intent

## What This Pass Does Not Promote

This pass still does not authorize:

- any exact milling offset, edge-clearance, bridge, annular, hole, or lead-spacing numeric
- any universal redesign prescription, board-edge keepout default, or profiling-program rule
- any `BGA` pad-definition preference or appearance-priority doctrine
- any stackup, opening, thermal-via, or decorative-copper implementation recipe
- any tool-behavior, vendor-default, or checker-sufficiency claim
- any quality, yield, cost, schedule, or manufacturability-outcome claim

## E2 Lane Effect

`PCB可制造性设计及案例分析之线路篇.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `board-edge copper and milling-path conflict review` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `logs/p4-428-2026-5-10-e2-board-edge-copper-and-milling-path-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the reused boundary remains narrower than board-edge numerics, profiling-program defaults, decorative-copper implementation recipes, or business-outcome claims
- the per-PDF `E2` entry for `PCB可制造性设计及案例分析之线路篇.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
