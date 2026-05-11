# P4-410 E5 BGA Process And Hidden-Joint Authority Recovery

Date: 2026-05-10
Lane owner: `E5 narrow authority recovery`
Execution mode: `fact_log_tracker`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/你想知道的BGA焊接问题都在这里.pdf`

Parent surfaces:
- `logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`
- `logs/p4-337-2026-5-9-e5-bga-soldering-route-integration.md`
- `facts/methods/bga-staged-process-review-and-hidden-joint-inspection-boundary.md`
- `facts/methods/low-void-bga-dfm-to-process-review.md`
- `facts/methods/low-void-bga-reflow-paste-vs-assembly-boundary.md`
- `facts/methods/hidden-joint-xray-inspection-boundary.md`
- `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md`

## Purpose

Advance one `E5` lane beyond `single_pdf_usage_route_only` by creating one dedicated fact boundary for staged BGA process review and hidden-joint inspection, using already-landed current-public official and public-standards-adjacent sources.

This pass stays narrow.
It does not attempt to promote pitch escape numerics, via-in-pad defaults, pad geometry, or universal inspection coverage.

## Official Source Support Reused

This pass does not need new source records, but it does add one dedicated fact boundary.
The repo already had current-public authority strong enough for this lane:

1. `indium-reflow-profile-to-paste-spec`
   - keeps reflow profiling tied to the chosen paste and real-board process context

2. `kester-standard-reflow-profile`
   - keeps reflow framed as a staged thermal process rather than one article-side recipe

3. `nasa-pcb-inspection-and-quality-control-2022-page`
   - keeps non-destructive inspection and quality-control workflow vocabulary inside a public inspection context

4. `ipc-a-610h-toc` and `ipc-j-std-001j-toc`
   - keep assembly acceptability and soldering-standard naming anchored at public metadata level without overclaiming clause content

These public anchors are now consolidated into a dedicated BGA article-side fact boundary rather than left only as background support in broader process cards.

## What Was Created

Created:

- `facts/methods/bga-staged-process-review-and-hidden-joint-inspection-boundary.md`

## What Was Promoted

Promoted into reusable `official_fact-backed` article-side coverage:

- BGA assembly discussion should stay inside a staged process-review chain rather than one oven-setting or one defect anecdote
- reflow language should remain paste-dependent and assembly-dependent
- X-ray or AXI may be used as the hidden-joint visibility layer for dense BGA context
- first-article confirmation and inspection governance belong to the same broader release-readiness flow

## What This Pass Does Not Promote

This pass still does not authorize:

- pitch escape numerics or line/space routing thresholds
- universal via-in-pad resin-fill or planarization defaults
- pad-to-ball ratio claims or solder-mask opening numerics
- void-percentage thresholds, X-ray coverage percentages, or class-specific accept/reject rules
- yield, reliability, throughput, cost, or supplier-capability claims

## E5 Lane Effect

`你想知道的BGA焊接问题都在这里.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `staged BGA process review and hidden-joint inspection` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Reused And Strengthened

- `facts/methods/bga-staged-process-review-and-hidden-joint-inspection-boundary.md`
- `facts/methods/low-void-bga-dfm-to-process-review.md`
- `facts/methods/low-void-bga-reflow-paste-vs-assembly-boundary.md`
- `facts/methods/hidden-joint-xray-inspection-boundary.md`
- `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the new BGA staged-process fact resolves cleanly with its public source IDs
- the BGA article entry in `p4-325` no longer understates the lane as route-only
- `p4-309` now records one official-fact raise inside `E5`
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
