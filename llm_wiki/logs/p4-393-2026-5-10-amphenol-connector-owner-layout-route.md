# P4-393 Amphenol Connector-Owner Layout Route

Date: 2026-05-10
Parent lane: `P4-315`
Execution mode: `controller_owned_source_and_boundary_strengthening`

## Purpose

Advance the still-open `connector-origin` lane by landing one additional current-public connector-owner drawing that adds named side-view and `pin-1` context, while explicitly staying below any universal connector-origin doctrine.

## Inputs

- official Amphenol current-public drawing `10122424.pdf`
- `logs/p4-317-2026-5-8-connector-origin-and-installation-mark-boundary-landing.md`
- `logs/p4-322-2026-5-8-samtec-connector-owner-layout-route-landing.md`
- `facts/methods/connector-origin-and-installation-mark-boundary.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## What Landed

### New source record

- `sources/registry/methods/amphenol-10122424-sfp-board-connector-recommended-pcb-layout.md`

### Route integration

Updated:

- `facts/methods/connector-origin-and-installation-mark-boundary.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one additional current-public connector-owner drawing with `RECOMMENDED PCB LAYOUT`
- one additional named-side vocabulary layer through `CONNECTOR MOUNTING SIDE` and `MATING PCB SIDE`
- one additional owner-scoped `PIN 1` anchor for a current-public connector family drawing

## What Did Not Land

- no universal connector-origin default
- no standards-grade connector-origin doctrine
- no board-level installation-mark geometry rule
- no closeout for residual `1.50 mm` or `0.75 mm`

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `connector_origin_lane_now_has_kicad_plus_molex_plus_samtec_plus_amphenol`
  - `universal_connector_origin_and_board_level_mark_geometry_still_open`
