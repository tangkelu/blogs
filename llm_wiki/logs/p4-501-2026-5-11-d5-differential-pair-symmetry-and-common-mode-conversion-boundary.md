# P4-501 D5 Differential-Pair Symmetry And Common-Mode Conversion Boundary

Date: 2026-05-11
Execution mode: `handbook_lane_authority_recovery`
Model: `gpt-5`
Lane owner: `P4-501 D5 narrow official-source recovery for 【PCB必备】194页-PCB设计规范经验之书.pdf`

## Purpose And Assigned Lane

Advance the `194页 RK3588 handbook` `D5` lane with one additional differential-pair-specific route that is narrower than generic return-path continuity, generic high-speed checklist language, or generic impedance planning: `pair symmetry`, `balance preserved through localized discontinuities`, and `common-mode-conversion risk from pair asymmetry or mismatch`.

This pass stays below all handbook numerics, exact skew limits, exact impedance numbers, exact spacing or via recipes, and EMC-pass implications.

## Input Files Inspected

- `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0115.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0172.txt`
- `/code/blogs/llm_wiki/logs/p4-282b-2026-5-7-rk3588-handbook-lane-stackup-impedance-and-routing-governance.md`
- `/code/blogs/llm_wiki/logs/p4-282e-2026-5-7-rk3588-handbook-lane-emc-esd-and-dfm-review-boundaries.md`
- `/code/blogs/llm_wiki/facts/interfaces/high-speed-pcb-interface-requirements-and-design-boundaries.md`
- `/code/blogs/llm_wiki/facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`
- `/code/blogs/llm_wiki/facts/methods/via-transition-return-path-continuity-boundary.md`

## What Landed

### New source records

- `/code/blogs/llm_wiki/sources/registry/methods/ti-tm4c-differential-pair-symmetry-and-common-mode-noise.md`
- `/code/blogs/llm_wiki/sources/registry/methods/microchip-vsc7420-differential-pair-mismatch-and-common-mode-current.md`
- `/code/blogs/llm_wiki/sources/registry/methods/microchip-polarfire-differential-length-asymmetry-mode-conversion.md`

### New fact card

- `/code/blogs/llm_wiki/facts/methods/differential-pair-symmetry-and-common-mode-conversion-boundary.md`

### Route integration

Updated:

- `/code/blogs/llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `/code/blogs/llm_wiki/logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `/code/blogs/llm_wiki/logs/backlog.md`
- `/code/blogs/llm_wiki/logs/phase-status.md`
- `/code/blogs/llm_wiki/logs/update-log.md`

## Why This Lane Is Distinct

- `p4-282e` already named `differential symmetry and coupling preservation` as an EMC-relevant routing family, but the repo still lacked a dedicated official fact card for the specific risk transition into `common-mode noise`, `common-mode current`, or `differential-to-common-mode conversion`.
- `p4-282b` already kept `symmetry` and `coupling preservation` at claim-family level, but not as a separately landed owner-backed boundary.
- the current `ground-and-return-path` and `via-transition` cards cover reference continuity and layer-change cleanup, not pair imbalance as a common-mode conversion surface.
- the existing high-speed interface boundary owns broad interface checklist language, not this narrower pair-balance-as-EMC-risk lane.

## What Landed Safely

- one current-public TI owner route for pair members staying parallel and matched in length so delay mismatch does not raise common-mode noise and EMI
- one current-public TI owner route for keeping unavoidable disturbed or non-parallel pair sections short and localized
- one current-public Microchip owner route for mismatched pair members creating common-mode current and for reducing mismatch to reduce that current
- one current-public Microchip owner route for naming common-mode current as a primary EMI source in this checklist context
- one current-public Microchip owner route for asymmetry in pair length causing conversion into common-mode behavior
- one reusable `differential-pair symmetry and common-mode-conversion` boundary above claim-family wording alone and distinct from generic return-path continuity

## What Did Not Land

- no universal skew budgets or cross-interface numeric mismatch limits
- no universal `90 ohm`, `100 ohm`, or `120 ohm` doctrine
- no exact spacing, coupling, meander, via, backdrill, or stitching recipes
- no claim that tighter coupling is always better
- no SI, jitter, BER, EMC-pass, or compliance outcomes
- no full `D5` closeout

## Explicit Route Decision

The `194页` handbook now has a fifth distinct `D5` route beyond the existing four:

- `connector-adjacent ESD entry-path interception`
- `surface-ground continuity / exposed-zone isolation`
- `clock source-end termination / crystal-routing EMC`
- `switch-mode power EMC placement / hot-loop control`
- `differential-pair symmetry and common-mode-conversion boundary` through this pass

This pass is narrower than generic high-speed differential doctrine and is justified because the repo previously lacked a dedicated owner-backed card for pair imbalance as a common-mode conversion and EMI risk surface.

## Completion Status

- `completed_for_one_additional_narrow_d5_route`
- `194_page_handbook_now_has_four_d3_routes_plus_five_non_overlapping_d5_routes`
- `not_completed_for_full_d5_or_full_corpus_closeout`
