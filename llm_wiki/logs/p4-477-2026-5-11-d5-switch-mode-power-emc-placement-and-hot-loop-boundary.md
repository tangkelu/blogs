# P4-477 D5 Switch-Mode Power EMC Placement And Hot-Loop Boundary

Date: 2026-05-11
Execution mode: `handbook_lane_authority_recovery`
Model: `gpt-5`
Lane owner: `P4-477 D5 narrow official-source recovery for 【PCB必备】194页-PCB设计规范经验之书.pdf`

## Purpose And Assigned Lane

Advance the `194页 RK3588 handbook` `D5` lane with one additional switching-power-specific route that is narrower than generic high-current or generic feedback guidance: `switching-power stage placement`, `compact local input/output current loops`, `local input-loop control near the power pins`, and `hot-loop / switch-node minimization`.

This pass stays below all handbook numerics, exact filter values, exact component distances, exact copper geometry, and EMI-pass implications.

## Input Files Inspected

- `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0173.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0174.txt`
- `/code/blogs/llm_wiki/logs/p4-282e-2026-5-7-rk3588-handbook-lane-emc-esd-and-dfm-review-boundaries.md`
- `/code/blogs/llm_wiki/logs/p4-471-2026-5-11-194-page-handbook-four-route-successor-no-write-closeout.md`
- `/code/blogs/llm_wiki/facts/methods/current-carrying-trace-width-and-copper-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`
- `/code/blogs/llm_wiki/facts/methods/remote-feedback-and-quiet-sense-point-routing-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/clock-source-termination-and-crystal-routing-emc-boundary.md`

## What Landed

### New source records

- `/code/blogs/llm_wiki/sources/registry/methods/analog-devices-an136-switching-power-placement-and-hot-loop-boundary.md`
- `/code/blogs/llm_wiki/sources/registry/methods/analog-devices-basic-switching-regulator-layout-techniques.md`
- `/code/blogs/llm_wiki/sources/registry/methods/ti-sszt090-switch-mode-power-supply-emi-layout-tips.md`

### New fact card

- `/code/blogs/llm_wiki/facts/methods/switch-mode-power-emc-placement-and-hot-loop-boundary.md`

### Route integration

Updated:

- `/code/blogs/llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `/code/blogs/llm_wiki/logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `/code/blogs/llm_wiki/logs/backlog.md`
- `/code/blogs/llm_wiki/logs/phase-status.md`
- `/code/blogs/llm_wiki/logs/update-log.md`

## What Landed Safely

- one current-public ADI owner-backed route for separating the switching-power stage from small-signal control or other sensitive circuitry
- one current-public ADI owner-backed route for keeping input and output current-loop components compact so high currents stay in the power section
- one current-public ADI owner-backed route for placing local input bypass close to the power loops
- one current-public ADI owner-backed route for keeping sensitive traces away from noisy switching copper and from routing under the supply
- one current-public ADI and TI route for minimizing hot-loop circumference, minimizing the transient input loop, and minimizing switch-node area
- one reusable `switch-mode power EMC placement` boundary above the existing `current-carrying`, `return-path`, `remote-feedback`, and `clock-specific EMC` cards

## What Did Not Land

- no exact EMI-filter values or exact filter-topology recipe
- no exact input/output spacing or exact analog/clock keepout distance
- no exact copper widths, via counts, or plane-shape rules
- no exact loop dimensions or switch-node geometry numbers
- no EMI, EMC, ripple, efficiency, or compliance-pass claims
- no full `D5` closeout

## Explicit Route Decision

The `194页` handbook now has a fourth distinct `D5` route beyond the existing three:

- `connector-adjacent ESD entry-path interception`
- `surface-ground continuity and exposed-zone isolation`
- `clock source-end termination and crystal-routing EMC boundary`
- `switch-mode power EMC placement and hot-loop boundary` through this pass

This pass is narrower than broad regulator doctrine and is justified because the repo previously lacked a dedicated switching-power-stage placement and local-input-loop boundary card.

## Completion Status

- `completed_for_one_additional_narrow_d5_route`
- `194_page_handbook_now_has_one_d3_route_plus_four_non_overlapping_d5_routes`
- `not_completed_for_full_d5_or_full_corpus_closeout`
