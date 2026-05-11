# P4-470 D5 Clock-Routing Boundary Successor SiTime TI Strengthening

Date: 2026-05-11
Parent lane: `P4-469`
Execution mode: `handbook_lane_authority_strengthening`

## Purpose

Strengthen the new `194页 handbook D5` clock-routing boundary from `TI hardware-guide plus supplemental crystal-layout support` to a cleaner `SiTime + TI` owner-backed combination that better matches the handbook's remaining `clock-specific` EMC wording.

## Inputs

- `logs/p4-469-2026-5-11-d5-clock-source-termination-and-crystal-routing-emc-boundary.md`
- `sources/registry/methods/sitime-an10006-best-design-and-layout-practices.md`
- `sources/registry/methods/ti-clock-source-series-termination-and-ground-plane-layout.md`
- `sources/registry/methods/ti-high-speed-layout-guidelines.md`
- `facts/methods/clock-source-termination-and-crystal-routing-emc-boundary.md`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0171.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0172.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0173.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0175.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0176.txt`

## What Landed

### New source record

- `sources/registry/methods/sitime-an10006-best-design-and-layout-practices.md`

### Strengthened fact card

- `facts/methods/clock-source-termination-and-crystal-routing-emc-boundary.md`

### Tracker refresh

Updated:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one stronger oscillator-owner source for `source termination close to oscillator output`
- one stronger oscillator-owner source for `short/direct clock traces`, `avoid board-edge and noisy-region routing`, and `no branching on clock traces`
- clearer preferred authority split:
  - `SiTime` for clock/oscillator-specific routing posture
  - `TI high-speed` for split-crossing and layer-change return continuity
  - `TI hardware guide` for source-end termination and solid reference support

## What Did Not Land

- no exact resistor values
- no exact clock-spacing or impedance numbers
- no exact jitter, SI, timing-closure, or EMC-pass proof
- no full `D5` closeout

## Final Status

- lane result:
  - `source_backed_fact_layer_partial_strengthened`
- continuation state:
  - `194_page_d5_clock_boundary_now_prefers_sitime_plus_ti_owner_support`
  - `full_d5_and_full_corpus_still_open`
