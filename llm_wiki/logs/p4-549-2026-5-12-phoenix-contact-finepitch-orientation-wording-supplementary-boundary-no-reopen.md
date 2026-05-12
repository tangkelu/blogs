# P4-549 Phoenix Contact FINEPITCH Orientation Wording Supplementary Boundary No-Reopen

Date: 2026-05-12
Parent surfaces:

- `logs/p4-490-2026-5-11-doctrine-owner-and-installation-mark-candidate-scout-no-reopen-successor.md`
- `logs/p4-317-2026-5-8-connector-origin-and-installation-mark-boundary-landing.md`
- `logs/p4-483-2026-5-11-altium-cad-owner-footprint-reference-point-and-layer-boundary.md`

Execution mode: `subagent_aided_named_series_owner_boundary_supplement`

## Purpose

Record one more bounded owner-side strengthening pass for the still-open doctrine lane after `P4-490`.

This pass does not reopen universal `connector-origin` or board-level `installation mark` doctrine.
It only lands one current-public Phoenix Contact FINEPITCH owner statement as a narrow supplementary boundary.

## Candidate Rechecked

- official Phoenix Contact product page:
  - `https://www.phoenixcontact.com/en-us/products/smd-male-connector-fp-08-80-mv-265-1061704`

## What Landed

### New source record

- `sources/registry/methods/phoenix-contact-finepitch-fp-08-80-mv-265-orientation-page.md`

### New boundary fact card

- `facts/methods/phoenix-contact-finepitch-orientation-and-plug-direction-boundary.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one current-public named-series owner route that explicitly marks `position a1 / row a / pin 1`
- one current-public named-series owner route that explicitly ties item marking plus owner drawing marking to PCB-assembly orientation and plug-in direction
- one explicit owner-side `customer may redefine it in project documentation` clause that keeps this surface below universal doctrine

## What Did Not Land

- no universal connector-origin default
- no standards-owner doctrine
- no board-level installation-mark geometry rule
- no change to the `1.50 mm` package residual
- no completion-threshold change

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `connector_origin_named_series_owner_support_now_includes_phoenix_contact`
  - `universal_connector_origin_and_board_level_mark_geometry_still_open`
