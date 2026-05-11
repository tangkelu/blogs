# P4-495 D3 Exposed-Pad Ground Tie And Local Thermal Spreading Boundary

Date: 2026-05-11
Execution mode: `handbook_lane_authority_recovery`
Model: `gpt-5`
Lane owner: `P4-495 D3 narrow official-source recovery for 【PCB必备】194页-PCB设计规范经验之书.pdf`

## Purpose And Assigned Lane

Advance the `194页 RK3588 handbook` `D3` lane with one additional narrow route that is distinct from:

- the existing `remote feedback / quiet sense-point` route
- the existing `processor power-pin local decoupling capacitor placement` route
- the existing `switch-mode power EMC placement / hot-loop` route
- the generic `ground-and-return-path continuity` route

This pass is limited to `exposed pad / thermal pad grounding serves thermal and impedance goals` as a package-scoped board-attach, local heat-spreading, and conditional low-impedance electrical-tie boundary.

This pass stays below all handbook numerics, all exact via arrays, all paste-window or stencil rules, all universal `EPAD = GND` doctrine, all package-family generalization claims, and all deterministic thermal / EMI / reliability outcome claims.

## Input Files Inspected

- `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0080.txt`
- `/code/blogs/llm_wiki/logs/p4-282c-2026-5-7-rk3588-handbook-lane-power-delivery-and-grounding-layout.md`
- `/code/blogs/llm_wiki/facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`
- `/code/blogs/llm_wiki/facts/methods/processor-power-pin-local-decoupling-capacitor-placement-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/switch-mode-power-emc-placement-and-hot-loop-boundary.md`

## What Landed

### New source records

- `/code/blogs/llm_wiki/sources/registry/methods/analog-devices-exposed-pads-brief-introduction.md`
- `/code/blogs/llm_wiki/sources/registry/methods/ti-powerpad-thermally-enhanced-package.md`

### New fact card

- `/code/blogs/llm_wiki/facts/methods/exposed-pad-ground-tie-and-local-thermal-spreading-boundary.md`

### Route integration

Updated:

- `/code/blogs/llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `/code/blogs/llm_wiki/logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `/code/blogs/llm_wiki/logs/backlog.md`
- `/code/blogs/llm_wiki/logs/phase-status.md`
- `/code/blogs/llm_wiki/logs/update-log.md`

## Why This Lane Is Distinct

- `p4-282c` already named `thermal-pad grounding serves thermal and impedance goals`, but only at claim-family level.
- the current `ground-and-return-path` card covers reference-plane continuity and routing discipline, not exposed-pad package attach
- the current `processor power-pin local decoupling` card covers near-device capacitor placement, not exposed-pad package attach
- the current `switch-mode power` card covers noisy power-stage loop placement, not exposed-pad package attach
- the new lane therefore recovers one narrower owner-backed package-side authority surface that the repo did not previously have as a reusable fact card

## What Landed Safely

- one current-public Analog Devices owner route for treating the exposed paddle as a thermal path into the PCB
- one current-public Analog Devices owner route for treating the same paddle as a low-impedance electrical path only when the die attach is externally grounded
- one current-public TI owner route for treating the exposed thermal pad as a board-attach region that should be soldered to the PCB
- one current-public TI owner route for requiring device-specific verification because the exposed pad may connect to signal, power, or ground depending on the owner package definition
- one reusable `exposed pad ground tie and local thermal spreading` boundary above claim-family wording alone and distinct from broad ground continuity, local decoupling, or switcher hot-loop language

## What Did Not Land

- no universal `EPAD = GND` doctrine
- no exact via counts, via diameters, via-in-pad rules, or fill rules
- no exact stencil aperture, paste-window, or voiding rules
- no exact thermal-resistance or junction-temperature improvement values
- no exact impedance, EMI, EMC, or reliability outcome claims
- no package-family or vendor-crossing generalization beyond guarded owner-scoped wording
- no full `D3` closeout

## Explicit Route Decision

The `194页` handbook now has a third distinct `D3` route beyond the earlier `remote feedback` and `local decoupling` lanes:

- `remote feedback / quiet sense-point routing`
- `processor power-pin local decoupling capacitor placement`
- `exposed pad ground tie and local thermal spreading`

This pass is narrower than generic return-path continuity, generic heat-spreading language, or generic package-governance vocabulary and is justified because the repo previously lacked a dedicated owner-backed card for exposed-pad board attach and conditional grounded low-impedance role.

## Completion Status

- `completed_for_one_additional_narrow_d3_route`
- `194_page_handbook_now_has_three_d3_routes_plus_four_non_overlapping_d5_routes`
- `not_completed_for_full_d3_or_full_corpus_closeout`
