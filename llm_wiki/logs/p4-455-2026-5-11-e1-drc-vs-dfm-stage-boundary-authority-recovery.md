# P4-455 E1 DRC-Versus-DFM Stage-Boundary Authority Recovery

Date: 2026-05-11
Lane owner: `E1 narrow authority recovery`
Execution mode: `log_tracker_only`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/PCB layout有DRC检查为什么还要用DFM.pdf`

Parent surfaces:
- `logs/p4-290-2026-5-7-pcb-article-e1-e7-controller-integration.md`
- `logs/p4-349-2026-5-9-e1-drc-vs-dfm-review-boundary-route-integration.md`
- `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`
- `wiki/consumption/pcb-design-for-manufacturing-2-evidence-pack.md`

## Purpose

Advance one `E1` single-PDF `DRC vs DFM` lane beyond `source_backed_route_available_without_new_fact_promotion` by confirming that this article can now safely reuse already-landed narrow support for `DRC as layout-stage rule-correctness checking` versus `DFM as separate staged manufacturability / assembly review posture before release`, while keeping all exact numeric examples, comparison-table rows, standards lists, and software-sufficiency language blocked.

This pass is intentionally narrow.
It does not create a new fact card.
It promotes this PDF from route-only status because the repo already has enough support to keep one sub-surface of this article inside the existing `layout-rule check boundary + early DFM review-gate posture`.

## Existing Source Support Reused

This pass relies on already-landed support only:

1. `methods-pcba-dfm-dft-dfa-review-gate-positioning`
   - already supports `DFM`, `DFT`, and `DFA` as front-end review gates before downstream release, inspection, and validation
   - already supports manufacturability and assembly-oriented review posture as distinct from later validation stages

2. `wiki/consumption/pcb-design-for-manufacturing-2-evidence-pack.md`
   - already supports `DFM` as a release-review boundary around build intent, file-package clarity, process branch, assembly assumptions, and test-access ownership
   - already blocks any attempt to turn DFM writing into universal numeric rule tables or checker-completeness claims

3. `P4-349`
   - already constrained this PDF to route-only posture
   - already isolated `DRC` versus `DFM` as separate review layers, `DRC` as layout-stage rule check, `DFM` as staged manufacturability / assembly review posture, and manufacturability findings as not always identical to online-layout-rule violations

4. `P4-290`
   - already holds the `E1` lane as governance / persuasion material that must stay narrow and guarded rather than broad process closure

## What Was Promoted

Promoted for this single PDF only:

- `DRC` may be reused only as layout-stage rule-correctness checking against preset design constraints
- `DFM` may be reused only as a separate staged manufacturability / assembly review posture before release
- `DRC` and `DFM` may be reused only as different review layers rather than interchangeable checks
- manufacturability findings may be reused only as review-ranked issues that are not always identical to online-layout-rule violations

## What This Pass Does Not Promote

This pass still does not authorize:

- any exact `DRC` numeric examples for spacing, width, mask, hole, silkscreen, or similar rules
- any `DRC` versus `DFM` comparison-table rows, rule counts, or standards-list authority
- any vendor software capability, rule-database completeness, or checker-sufficiency claim
- any universal severity scale, pass/fail doctrine, or claim that `DRC` alone settles manufacturability
- any cost-saving, trial-reduction, reliability, or other business-outcome claim

## E1 Lane Effect

`PCB layout有DRC检查为什么还要用DFM.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `DRC layout-stage check versus DFM staged review boundary` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `logs/p4-455-2026-5-11-e1-drc-vs-dfm-stage-boundary-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the reused boundaries remain narrower than any exact numeric rule, comparison table, standards-list authority, software completeness, or business-outcome claim
- the per-PDF `E1` entry for `PCB layout有DRC检查为什么还要用DFM.pdf` no longer understates the `DRC` versus `DFM` stage-boundary sub-surface as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
