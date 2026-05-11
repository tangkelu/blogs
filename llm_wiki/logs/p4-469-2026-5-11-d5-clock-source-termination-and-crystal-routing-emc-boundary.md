# P4-469 D5 Clock Source-Termination And Crystal Routing EMC Boundary

Date: 2026-05-11
Execution mode: `handbook_lane_authority_recovery`
Model: `gpt-5`
Lane owner: `P4-469 D5 narrow official-source recovery for 【PCB必备】194页-PCB设计规范经验之书.pdf`

## Purpose And Assigned Lane

Advance the `194页 RK3588 handbook` `D5` lane with one additional clock-specific route that is narrower than generic return-path continuity: `clock source-end termination`, `clock/crystal source-region keepout`, and `clock routing over a stable reference`.

This pass stays below all handbook numerics, exact clock distances, exact resistor values, shielding-via recipes, and EMC-pass implications.

## Input Files Inspected

- `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0171.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0172.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0173.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0174.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0175.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0176.txt`
- `/code/blogs/llm_wiki/logs/p4-282e-2026-5-7-rk3588-handbook-lane-emc-esd-and-dfm-review-boundaries.md`
- `/code/blogs/llm_wiki/facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`
- `/code/blogs/llm_wiki/facts/methods/via-transition-return-path-continuity-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/connector-near-surface-ground-continuity-and-exposed-zone-isolation-boundary.md`

## What Landed

### New source records

- `/code/blogs/llm_wiki/sources/registry/methods/ti-clock-source-series-termination-and-ground-plane-layout.md`
- `/code/blogs/llm_wiki/sources/registry/methods/microchip-crystal-layout-short-trace-and-no-under-routing.md`

### New fact card

- `/code/blogs/llm_wiki/facts/methods/clock-source-termination-and-crystal-routing-emc-boundary.md`

### Route integration

Updated:

- `/code/blogs/llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `/code/blogs/llm_wiki/logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `/code/blogs/llm_wiki/logs/backlog.md`
- `/code/blogs/llm_wiki/logs/phase-status.md`
- `/code/blogs/llm_wiki/logs/update-log.md`

## What Landed Safely

- one current-public TI owner-backed route for `series termination close to the clock source` and `solid GND under clock traces`
- one current-public Microchip owner-backed route for `crystal close to the device`, `short crystal traces`, and `no unrelated routing under the crystal region`
- one reusable `clock-specific EMC` boundary above the already-landed generic `return-path continuity` cards

## What Did Not Land

- no exact source-to-resistor distance rule
- no exact clock-spacing or board-edge numbers
- no exact resistor values
- no exact shielding-via or ground-fence recipes
- no jitter, timing-closure, SI-signoff, or EMC-pass claims
- no full `D5` closeout

## Explicit Route Decision

The `194页` handbook now has a third distinct `D5` route beyond the existing two:

- `connector-adjacent ESD entry-path interception`
- `surface-ground continuity and exposed-zone isolation`
- `clock source-end termination and crystal-routing EMC boundary` through this pass

This pass is narrower than generic high-speed routing doctrine and is justified because the repo previously lacked a dedicated clock-source / crystal-source boundary card.

## Completion Status

- `completed_for_one_additional_narrow_d5_route`
- `194_page_handbook_now_has_three_non_overlapping_narrow_official_routes`
- `not_completed_for_full_d5_or_full_corpus_closeout`
