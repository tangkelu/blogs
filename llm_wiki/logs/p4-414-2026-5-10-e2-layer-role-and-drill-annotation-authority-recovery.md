# P4-414 E2 Layer-Role And Drill-Annotation Authority Recovery

Date: 2026-05-10
Lane owner: `E2 narrow authority recovery`
Execution mode: `fact_log_tracker`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/一文带你读懂PCB电路板设计中各种层的定义.pdf`

Parent surfaces:
- `logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`
- `logs/p4-380-2026-5-9-e2-layer-definition-grammar-and-drill-annotation-route-integration.md`
- `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`
- `facts/methods/cam-data-exchange-format-boundary.md`
- `facts/methods/pcb-design-tool-official-feature-identity-boundary.md`
- `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`
- `wiki/processes/rigid-board-family-and-layer-boundaries.md`

## Purpose

Advance one `E2` lane beyond `single_pdf_usage_route_only` by landing a narrow official-fact boundary for layer-role vocabulary and released-output drill-annotation vocabulary.

This pass is intentionally narrow.
It does not try to close stackup, drill geometry, capability, or design-rule claims.

## Official And Existing Source Support Used

This pass reuses already-landed public and tool-owner support:

1. `ipc-t50-terms-and-definitions-toc`
   - supports the existence of a controlled IPC terminology-family context

2. `ucamco-gerber-format-page`
   - supports fabrication-data layer vocabulary such as solder mask, legend, drill, and route data

3. `ipc-dpmx-ipc-2581-consortium-home-page`
   - supports manufacturing-description and handoff vocabulary for PCB and assembly data

4. `kicad-official-pcb-design-suite-page`
   - supports official tool-owner feature identity and helps keep tool naming separate from universal standards truth

5. existing repo-backed boundary cards and route pages
   - support the distinction between layer-role naming, released manufacturing-data layers, and tool-side output labels

## What Was Promoted

Promoted into reusable `facts/` coverage:

- top layer, bottom layer, and multilayer can stay as board-family or layer-role identity wording
- solder mask, legend, and drill can stay as released manufacturing-data layer families
- `Drillguide`, `Drilldrawing`, `Drl`, and `NPTH` can stay as output-annotation vocabulary examples
- blind / buried layer-pair names can stay as released-output examples only
- tool naming and released manufacturing data must remain separate from universal standards or process-capability claims

## What This Pass Does Not Promote

This pass still does not authorize:

- hole-size, board-thickness, layer-count, stackup, or spacing numerics
- blind / buried capability closure or buildability claims
- keepout, DRC, or acceptability thresholds
- any claim that tool naming habits are universal standards
- supplier capability, quality, cost, schedule, or manufacturability claims
- exact drill-depth, impedance, or CAM-completeness claims

## E2 Lane Effect

`一文带你读懂PCB电路板设计中各种层的定义.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `layer-role and drill-output annotation vocabulary` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `facts/methods/layer-role-and-drill-output-annotation-vocabulary-boundary.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- source IDs resolve cleanly inside the new fact card
- the per-PDF `E2` entry for `一文带你读懂PCB电路板设计中各种层的定义.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
