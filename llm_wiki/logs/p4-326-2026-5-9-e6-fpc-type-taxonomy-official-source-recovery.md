# P4-326 E6 FPC Type Taxonomy Official-Source Recovery

Date: 2026-05-09
Parent lane: `P4-314`
Execution mode: `narrow_article_side_official_source_recovery`

## Purpose

Advance one bounded `E6` subtopic above controller-only routing by replacing the article-only `single / double / multilayer FPC` taxonomy with public IPC standards-owner terminology.

This pass is intentionally narrow.
It does not promote bend-radius rules, material stacks, procurement claims, or `0R` resistor guidance.

## Inputs

- `logs/p4-314-2026-5-8-pcb-article-e6-usage-route-integration.md`
- `logs/p4-283e6-2026-5-7-pcb-article-e6-packages-bom-and-component-selection-alignment-claim-family-map.md`
- `/code/blogs/tmps/PCB资料/PCB文章/单层双面多层FPC有何区别？.pdf`
- official IPC public records:
  - `ipc-2223e-toc`
  - `ipc-6013e-toc`
  - `ipc-2223e-flex-rigid-flex-design-standard-page`

## What Landed

### New source record

- `sources/registry/standards/ipc-2223e-toc.md`

### New standards fact card

- `facts/standards/ipc-flex-printed-board-type-taxonomy-boundary.md`

### New wiki route

- `wiki/processes/flex-printed-board-type-taxonomy-and-structure-map.md`

### Resume-surface integration

Updated:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`

## What Landed Safely

- one public IPC terminology route for:
  - `Type 1 - Single-Sided Flexible Printed Boards`
  - `Type 2 - Double-Sided Flexible Printed Boards`
  - `Type 3 - Multilayer Flexible Printed Boards`
  - `Type 4 - Multilayer Rigid-Flexible Printed Boards`
  - `Type 5 - Flexible or Rigid-Flexible Printed Boards without Plated Through Holes`
- one safe boundary that keeps `rigid-flex` distinct from ordinary multilayer `FPC`
- one per-PDF upgrade path where `单层双面多层FPC有何区别？.pdf` is no longer only article claim inventory for structure naming

## What Did Not Land

- no bend-radius, bend-cycle, copper-type, coverlay, adhesive, or stackup rules
- no supplier capability, lead-time, cost, or procurement guidance
- no `0R` resistor role closure
- no package-dimension or BOM-field promotion

## Final Status

- lane result:
  - `narrow_official_source_recovery_landed`
- continuation state:
  - `e6_now_has_one_standards_backed_fpc_structure_taxonomy_surface`
  - `package_residual_1p50_mm_still_remains_the_primary_global_open_gap`
