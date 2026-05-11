# P4-404 D5 Surface-Ground Continuity And Exposed-Zone Isolation Boundary

Date: 2026-05-10
Execution mode: `handbook_lane_authority_recovery`
Model: `gpt-5`
Lane owner: `P4-404 D5 narrow official-source recovery for 【PCB必备】194页-PCB设计规范经验之书.pdf`

## Purpose And Assigned Lane

Advance the `194页 RK3588 handbook` `D5` lane with one route adjacent to, but not overlapping with, the already-landed entry-path ESD lane: connector-near / board-edge surface-ground continuity and exposed-zone isolation.

This pass stays below all handbook numerics, copper-distance rules, and interface-specific recipes.

## Input Files Inspected

- `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0168.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0169.txt`
- `/code/blogs/llm_wiki/logs/p4-282e-2026-5-7-rk3588-handbook-lane-emc-esd-and-dfm-review-boundaries.md`
- `/code/blogs/llm_wiki/facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`
- `/code/blogs/llm_wiki/facts/methods/via-transition-return-path-continuity-boundary.md`

## What Landed

### New source record

- `/code/blogs/llm_wiki/sources/registry/methods/infineon-ap24026-emc-and-system-esd-design-guidelines-board-layout.md`

### New fact card

- `/code/blogs/llm_wiki/facts/methods/connector-near-surface-ground-continuity-and-exposed-zone-isolation-boundary.md`

### Route integration

Updated:

- `/code/blogs/llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `/code/blogs/llm_wiki/logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `/code/blogs/llm_wiki/logs/backlog.md`
- `/code/blogs/llm_wiki/logs/phase-status.md`
- `/code/blogs/llm_wiki/logs/update-log.md`

## What Landed Safely

- one current-public owner source for connector-near or board-edge return-path continuity posture
- one reusable boundary tying exposed-zone routing to continuous local return/reference handling
- one reusable boundary for separating externally exposed routing regions from cleaner sensitive internal traces

## What Did Not Land

- no exact board-edge distance or keepout value
- no exact copper-setback or exposed-copper geometry rule
- no exact stitch-via count or spacing rule
- no HDMI / reset / capacitor / resistor recipe
- no EMC / ESD pass guarantee
- no full `D5` closeout

## Explicit Route Decision

The `194页` handbook now has a second distinct `D5` route beyond the entry-path interception lane:

- `connector-adjacent ESD entry-path interception` through `P4-402` and `P4-403`
- `surface-ground continuity and exposed-zone isolation` through this pass

This still does not authorize exact edge numerics or complete the whole `D5` lane.

## Completion Status

- `completed_for_one_additional_narrow_official_route`
- `194_page_d5_now_has_two_adjacent_but_non_overlapping_official_routes`
- `not_completed_for_full_d5_or_full_corpus_closeout`
