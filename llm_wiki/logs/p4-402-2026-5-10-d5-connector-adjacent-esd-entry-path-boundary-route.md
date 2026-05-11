# P4-402 D5 Connector-Adjacent ESD Entry-Path Boundary Route

Date: 2026-05-10
Execution mode: `handbook_lane_authority_recovery`
Model: `gpt-5`
Lane owner: `P4-402 D5 narrow official-source recovery for 【PCB必备】194页-PCB设计规范经验之书.pdf`

## Purpose And Assigned Lane

Advance the `194页 RK3588 handbook` `D5` lane beyond `claim_family_level_only` by landing one current-public semiconductor-owner boundary for connector-adjacent ESD protection placement and short entry-path interception.

This lane was later strengthened the same day by `P4-403`, which adds `ST + TI` owner-layout guidance as the preferred primary support for this route.

This pass keeps the scope narrow. It does not promote handbook numerics, shield distances, resistor values, capacitor values, via counts, or compliance outcomes.

## Input Files Inspected

- `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0167.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0168.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0170.txt`

## Existing LLM Wiki Support Found

Related lane logs inspected:

- `/code/blogs/llm_wiki/logs/p4-282e-2026-5-7-rk3588-handbook-lane-emc-esd-and-dfm-review-boundaries.md`
- `/code/blogs/llm_wiki/logs/p4-347-2026-5-9-e4-board-edge-spacing-severity-route-integration.md`
- `/code/blogs/llm_wiki/logs/p4-348-2026-5-9-e4-board-edge-component-layout-importance-route-integration.md`

Repo-backed support surfaces inspected:

- `/code/blogs/llm_wiki/facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`
- `/code/blogs/llm_wiki/facts/methods/via-transition-return-path-continuity-boundary.md`

## Official Source Recovered

New source record:

- `/code/blogs/llm_wiki/sources/registry/methods/nexperia-pesd-layout-close-to-connector-boundary.md`

New fact card:

- `/code/blogs/llm_wiki/facts/methods/connector-adjacent-esd-protection-and-entry-path-boundary.md`

## What Landed Safely

- one current-public semiconductor-owner source saying the ESD protection element should sit close to the connector or other entry point
- one narrow reusable boundary that treats ESD layout as early interception of the entry path before the protected IC
- one integration path from handbook `D5` source-adjacent protection language into existing return-path continuity cards

## What Did Not Land

- no exact connector-to-TVS distances
- no exact grounding-via counts, stitching intervals, or shield-can spacing
- no exact resistor values, capacitor values, or reset-line recipes
- no IEC pass levels, surge guarantees, or EMC compliance claims
- no RK3588-specific implementation closeout

## Explicit Route Decision

The `194页` handbook no longer needs to stay purely at claim-family level for this narrow `D5` slice.

Current safe reuse now includes:

- ESD protection as a connector-adjacent or entry-point-adjacent placement family
- short exposure path before the protected IC as guarded board-review language
- local return/reference continuity as supporting posture for the clamp path

This still does not authorize universal board-edge spacing rules, connector keepout numbers, or full `D5` closeout.

## Completion Status

- `completed_for_one_narrow_official_source_route`
- `194_page_handbook_no_longer_pure_claim_family_only_for_this_d5_slice`
- `not_completed_for_full_d5_fact_closure`
