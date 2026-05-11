# P4-432 E5 Component-Spacing Access And Rework Authority Recovery

Date: 2026-05-10
Lane owner: `E5 narrow authority recovery`
Execution mode: `log_tracker_only`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/关于PCBA元器件布局的重要性.pdf`

Parent surfaces:
- `logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`
- `logs/p4-342-2026-5-9-e5-component-layout-importance-route-integration.md`
- `facts/methods/selective-solder-design-access-checks.md`
- `wiki/processes/mixed-technology-solder-route-selection.md`
- `wiki/processes/compact-closure-and-rework.md`
- `wiki/testing/pcba-quality-gates-and-test-strategy.md`

## Purpose

Advance one `E5` lane beyond `single_pdf_usage_route_only` by confirming that this component-layout article can now safely reuse an already-landed narrow official-fact boundary for `component spacing as access and rework boundary`, with dense mixed-technology neighborhood review, tall-part interference review, and inspection / test reach kept strictly inside access-planning and release-review posture.

This pass is intentionally narrow.
It does not create a new fact card.
It promotes this PDF from route-only status because the repo already has enough support to keep its safest reusable surface inside the existing `access-planning / mixed-technology route review / compact closure and re-entry` posture.

## Existing Source Support Reused

This pass relies on already-landed support only:

1. `methods-selective-solder-design-access-checks`
   - already supports selective-solder layout guidance as an access-planning problem
   - already supports nearby bodies, tall housings, connector overhang, thermal demand, inspection, and electrical-validation access as real review inputs
   - already blocks exact dimensions, universal reliability claims, and process-success guarantees

2. `processes-mixed-technology-solder-route-selection`
   - already supports route choice by board population, access, thermal sensitivity, and verification handoff
   - already supports nearby SMT density, overhang, shielding, access, and verification as mixed-technology route-review inputs

3. `processes-compact-closure-and-rework`
   - already supports keeping access for re-entry, inspection, service, and later rework
   - already supports dense connectors and compact neighborhoods as visibility / probe / rework constraints rather than as universal failure proof

4. `testing-pcba-quality-gates-and-test-strategy`
   - already supports inspection and validation as layered release gates
   - already supports dense-package and rework consequences as review-handoff context rather than as any one-gate sufficiency claim

5. `P4-342`
   - already constrained this PDF to route-only posture
   - already named `component_spacing_as_access_and_rework_boundary` as the safest reusable class and blocked spacing numerics, warpage certainty, and checker sufficiency claims

## What Was Promoted

Promoted for this single PDF only:

- component spacing may be reused as an `access and rework boundary`
- dense or tall component neighborhoods may be reused as mixed-technology assembly-review inputs because they change solder access, inspection reach, test reach, and later repair access
- connector overhang, tall-part adjacency, and large-part-over-small-part obstruction may be reused as explicit interference and re-entry review surfaces
- inspection and validation handoff may be reused as neighboring governance layers after dense-neighborhood layout decisions

## What This Pass Does Not Promote

This pass still does not authorize:

- any exact spacing minimum or safety-grade logic
- any `<0.25 mm` or other article-origin spacing numeric
- any stencil aperture, thickness, or bridging-threshold rule
- any warpage-causality certainty or reliability-failure certainty
- any universal statement that one dense layout is unreworkable or machine-blocking
- any tool-checker sufficiency or workflow-completeness claim
- any cost, cycle, quality, or reliability outcome claim

## E5 Lane Effect

`关于PCBA元器件布局的重要性.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `component-spacing access and rework boundary` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `logs/p4-432-2026-5-10-e5-component-spacing-access-and-rework-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the reused boundary remains narrower than spacing numerics, stencil rules, warpage certainty, checker sufficiency, or business-outcome claims
- the per-PDF `E5` entry for `关于PCBA元器件布局的重要性.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
