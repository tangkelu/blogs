# P4-322 Samtec Connector-Owner Layout Route Landing

Date: 2026-05-08
Parent lane: `P4-309`
Execution mode: `controller_owned_boundary_landing`

## Purpose

Strengthen the current `connector-origin / installation mark` lane by adding one more publicly retrievable connector-owner drawing route that is safe at the named-series layout level.

## Inputs

- official Samtec footprint drawing `mb1-1xx-xx-xx-s-xx-sl-x-footprint.pdf`
- `facts/methods/connector-origin-and-installation-mark-boundary.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `logs/p4-317-2026-5-8-connector-origin-and-installation-mark-boundary-landing.md`

## What Landed

### New source record

- `sources/registry/methods/samtec-mb1-recommended-pcb-layout-and-mating-card.md`

### Route integration

Updated:

- `facts/methods/connector-origin-and-installation-mark-boundary.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## What Landed Safely

- one additional connector-owner named-series drawing that is publicly retrievable in this environment
- one additional owner route for:
  - `RECOMMENDED PCB LAYOUT`
  - `RECOMMENDED MATING CARD LAYOUT`
- one stronger continuation state where connector-owner support is no longer only `Molex 105133`

## What Did Not Land

- no universal connector-origin default across all connector families
- no new standards-grade cross-vendor installation-mark doctrine
- no promotion of Samtec page geometry into a generic connector rule

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `connector_owner_support_now_includes_molex_and_samtec_named_series_routes`
  - `installation_mark_doctrine_still_not_universalized`
