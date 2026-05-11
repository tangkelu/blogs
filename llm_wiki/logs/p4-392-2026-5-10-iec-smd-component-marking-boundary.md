# P4-392 IEC SMD Component-Marking Boundary

Date: 2026-05-10
Parent lane: `P4-315`
Execution mode: `controller_owned_standards_boundary_landing`

## Purpose

Advance the still-open `installation-mark / component-marking` side of the `package residual authority recovery` lane by landing one narrower IEC `component marking` boundary for `pin-1` and polarity-identification topic framing, while explicitly staying below any board-level installation-mark geometry doctrine or connector-origin default.

## Inputs

- official IEC webstore metadata page for `IEC 61760-1:2020`
- public preview surface for the `IEC 61760-1:2020` component-marking section family
- `logs/p4-391-2026-5-10-iec-zero-orientation-cad-library-boundary.md`
- `logs/p4-387-2026-5-10-package-residual-live-recheck-no-closeout.md`
- `facts/methods/iec-zero-orientation-cad-library-construction-boundary.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## What Landed

### New source records

- `sources/registry/standards/iec-61760-1-smd-specification-page.md`
- `sources/registry/standards/iec-61760-1-component-marking-preview-page.md`

### New boundary fact card

- `facts/methods/iec-smd-component-marking-boundary.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one standards-owner metadata anchor for SMD component specification
- one public-preview-supported route that component marking includes separate multipin and polarity-identification surfaces
- one stronger continuation state where the repo can explain `pin-1` and polarity-identification topics as controlled component-specification discipline rather than only local governance convention

## What Did Not Land

- no universal connector-origin default
- no board-level installation-mark geometry rule
- no universal silkscreen / fabrication-layer marker-shape doctrine
- no closeout for residual `1.50 mm`, `0.75 mm`, or connector-origin

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `installation_mark_component_marking_lane_now_has_public_iec_pin1_and_polarity_identification_route`
  - `connector_origin_and_board_level_mark_geometry_residuals_still_open`
