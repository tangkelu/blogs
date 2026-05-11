# P4-308 Intel BGA Land Pad Guideline Landing

Date: 2026-05-08
Parent lane: `P4-307`
Execution mode: `controller_owned_exact_data_landing`

## Purpose

Add one more official package-owner BGA guidance source to the `PCB资料` package lane, with special value for the `0.4 mm VBGA/WLCSP` case that remained underrepresented in the current replacement surface.

## Inputs

- official Intel `AN 114` section `1.3.1 Surface Land Pad Dimension`
- `logs/p4-299-2026-5-8-pcb-ziliao-package-blocked-exact-data-evidence-batch-2.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## What Landed

### New source record

- `sources/registry/methods/intel-an114-bga-land-pad-dimensions.md`

### New exact-data fact card

- `facts/methods/intel-bga-land-pad-guidelines-common-pitches-and-vbga.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

## What Landed Safely

- Intel owner-scoped `1.27 mm`, `1.00 mm`, `0.80 mm`, and `0.50 mm` BGA land-pad guidance rows
- one direct official `0.4 mm VBGA/WLCSP` land-pad row
- one more exact-geometry route that stays inside package-owner scope rather than reopening the handbook table

## What Did Not Land

- no universal cross-vendor BGA table
- no clean replacement for residual handbook pitch classes `0.75 mm` or `1.50 mm`
- no closeout for `pin-1 / connector-origin / installation-mark` authority gaps

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `residual_0p75_and_1p50_pitch_classes_still_open`
