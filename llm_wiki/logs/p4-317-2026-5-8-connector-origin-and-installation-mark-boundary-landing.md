# P4-317 Connector Origin And Installation-Mark Boundary Landing

Date: 2026-05-08
Parent lane: `P4-315`
Execution mode: `controller_owned_boundary_landing`

## Purpose

Land the next safest package residual narrowing step after `P4-316` by converting the `connector-origin` and `installation-mark` scout route into one guarded boundary card built from a CAD-owner convention source plus one connector-owner drawing.

## Inputs

- official KiCad `KLC` page
- official Molex `105133-0001 / 0002` sales drawing
- `logs/p4-315-2026-5-8-package-residual-authority-recovery.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

## What Landed

### New source records

- `sources/registry/methods/kicad-library-conventions-footprint-orientation-and-marking.md`
- `sources/registry/methods/molex-105133-0002-micro-b-recommended-pcb-layout.md`

### New boundary fact card

- `facts/methods/connector-origin-and-installation-mark-boundary.md`

### Route integration

Updated:

- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## What Landed Safely

- one official KiCad library-convention layer for:
  - connector footprints horizontal with `pin 1` on the left side
  - `F.SilkS` pin-1 designator
  - `F.Fab` small arrow indicator next to `pin 1` for connectors
- one official Molex connector-owner drawing route for a named connector family with explicit recommended PCB layout and pin numbering
- one layered rule that separates:
  - CAD-owner default library posture
  - connector-owner series-specific exact layout

## What Did Not Land

- no universal connector-origin default across all connector families
- no standards-grade cross-vendor installation-mark doctrine
- no closeout for residual handbook `1.50 mm`

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `connector_origin_and_installation_mark_now_have_layered_boundary_support`
  - `1p50_mm_still_open`
