# P4-403 D5 ESD Entry-Path Boundary Owner-Source Strengthening

Date: 2026-05-10
Parent lane: `P4-402`
Execution mode: `handbook_lane_authority_strengthening`

## Purpose

Strengthen the new `D5` ESD entry-path boundary from `one owner-backed route landed` to a better `ST + TI primary owner-guide combination`, while keeping the lane narrow and below any exact-data or compliance overclaim.

## Inputs

- `logs/p4-402-2026-5-10-d5-connector-adjacent-esd-entry-path-boundary-route.md`
- `sources/registry/methods/st-an5686-pcb-layout-tips-to-maximize-esd-protection-efficiency.md`
- `sources/registry/methods/ti-slva680-esd-protection-layout-guide.md`
- `facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`
- `facts/methods/via-transition-return-path-continuity-boundary.md`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0167.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0168.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0169.txt`

## What Landed

### New source records

- `sources/registry/methods/st-an5686-pcb-layout-tips-to-maximize-esd-protection-efficiency.md`
- `sources/registry/methods/ti-slva680-esd-protection-layout-guide.md`

### Strengthened fact card

- `facts/methods/connector-adjacent-esd-protection-and-entry-path-boundary.md`

### Tracker / route refresh

Updated:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one stronger current-public owner-source pair for `connector-adjacent ESD protection`
- explicit support for `ESD source -> protection -> protected IC` routing order
- explicit support for avoiding stubs and keeping exposed protected traces away from clean unprotected traces
- explicit support for low-impedance local ground / return handling in the ESD path

## What Did Not Land

- no exact path lengths, via counts, or shielding dimensions
- no exact resistor, capacitor, or package-layout defaults
- no IEC level closeout, surge guarantee, or EMC pass claim
- no RK3588-specific implementation recipe
- no full `D5` closure

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `194_page_d5_now_has_st_plus_ti_owner_layout_boundary_for_connector_adjacent_esd_entry_path`
  - `full_d5_and_full_corpus_still_open`
