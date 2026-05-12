# P4-552 D4 eMMC HS400 Interface Routing And Simulation Governance Boundary

Date: 2026-05-12
Execution mode: `subagent_aided_official_source_recovery`
Lane owner: `P4-552 D4 narrow official-source recovery for 【PCB必备】194页-PCB设计规范经验之书.pdf`

## Purpose

Advance the `194页 RK3588 handbook` `D4` lane with one additional non-overlapping official-source-backed route for eMMC / HS400 interface routing and simulation governance.

This pass does not promote handbook pull-up / pull-down / matching tables, resistor values, impedance values, trace width / spacing, layer-count, via-count, delay / skew, timing, voltage, slew-rate, pass/fail numerics, or any platform-specific performance claim.

## Inputs

- `logs/p4-282d-2026-5-7-rk3588-handbook-lane-interface-and-memory-routing.md`
- `logs/p4-551-2026-5-12-d4-ddr-memory-interface-routing-governance-boundary.md`
- `sources/registry/methods/raspberry-pi-compute-module-5-product-page.md`
- official TI `AM62Px eMMC HS400 Board Design and Simulation Guidelines`, `SPRADP5`, January 2026
- subagent verification of the TI eMMC/HS400 lane

## What Landed

### New source record

- `sources/registry/methods/ti-am62px-emmc-hs400-board-design-and-simulation-guidelines.md`

### New fact card

- `facts/methods/emmc-hs400-interface-routing-and-simulation-governance-boundary.md`

### Route integration

Updated:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Why This Lane Is Distinct

- `P4-551` landed a DDR / EMIF memory-interface routing-governance boundary.
- This pass lands a separate eMMC / HS400 boundary around point-to-point routing, plane-split avoidance, return-current transition support, no-stub handling, and extraction/simulation governance.
- Existing generic return-path cards cover broad high-speed layout physics, but they do not provide eMMC/HS400-specific owner wording or the explicit simulation gate for full interface performance.

## What Landed Safely

- one current-public TI owner route for eMMC HS400 as a point-to-point high-speed interface
- one current-public TI owner route for solid ground/reference-plane and return-path continuity posture
- one current-public TI owner route for minimizing layer transitions and using nearby ground vias when return currents must transition between reference planes
- one current-public TI owner route for avoiding plane-split crossings and signal-routing stubs
- one current-public TI owner route for treating clock/strobe crosstalk as a sensitive routing concern
- one current-public TI owner route for using TI EVM/layout adherence or extraction/simulation before full interface performance claims
- one current-public Raspberry Pi owner route for CM5 system-on-module and eMMC-option vocabulary only, not for eMMC routing rules

## What Did Not Land

- no exact eMMC pull-up, pull-down, matching, resistor, impedance, trace-width, spacing, layer-count, via-count, via-distance, compensation-factor, slew, timing, skew, frequency, or pass/fail values
- no universal eMMC / HS400 / HS200 / DDR / LPDDR routing recipe
- no SI margin, eye opening, timing-closure, validation-pass, throughput, or board-level performance claim
- no proof that a specific supplier can build or validate eMMC HS400 designs
- no promotion of handbook-origin numeric tables or formulas
- no full `D4`, full handbook, or full corpus closeout

## Completion Status

- `completed_for_one_additional_narrow_d4_route`
- `194_page_handbook_now_has_four_d3_routes_plus_two_d4_routes_plus_five_non_overlapping_d5_routes`
- `not_completed_for_full_d4_or_full_corpus_closeout`
