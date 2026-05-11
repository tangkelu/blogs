# P4-481 Intel Fourth-Owner 0.75 mm µBGA CSP Guidelines Table Landing

Date: 2026-05-11
Parent lane: `P4-315`
Execution mode: `subagent_aided_exact_data_landing`

## Purpose

Advance the `0.75 mm` residual lane beyond `three Microchip exact rows plus one Renesas second-owner exact-data page plus one NXP third-owner exact-data page` by landing one directly verified current-public fourth-owner exact table from the Intel-hosted `Packaging Chapter 15 Databook`.

## Inputs

- official Intel-hosted packaging databook PDF `Packaging Chapter 15 Databook`
- current `0.75 mm` repo stack through:
  - `logs/p4-316-2026-5-8-microchip-0p75mm-tfbga-land-pattern-landing.md`
  - `logs/p4-320-2026-5-8-microchip-second-0p75mm-tfbga-row-landing.md`
  - `logs/p4-324-2026-5-8-microchip-third-0p75mm-tfbga-row-landing.md`
  - `logs/p4-400-2026-5-10-renesas-second-owner-0p75mm-exact-data-page-landing.md`
  - `logs/p4-466-2026-5-11-nxp-third-owner-0p75mm-reflow-footprint-landing.md`
- `logs/p4-474-2026-5-11-0p75mm-candidate-gated-scout-no-reopen-successor.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## What Landed

### New source record

- `sources/registry/methods/intel-0p75mm-ubga-csp-pcb-design-guidelines-table.md`

### New exact-data fact card

- `facts/methods/intel-0p75mm-ubga-csp-pcb-design-guidelines-table.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one directly verified current-public Intel-hosted fourth-owner exact table for `.75mm µBGA CSP Package`
- one same-table guideline surface with `Soldermask Opening Dia 0.375-0.425`, `Pad Diameter 0.325-0.375`, `Via Diameter 0.25-0.30`, and `Number of Traces Between Pads 1`
- one stronger continuation state where `0.75 mm` no longer stops at `Microchip + Renesas + NXP`

## What Did Not Land

- no universal `0.75 mm pitch -> land pattern` rule
- no cross-vendor `0.75 mm` closeout
- no public official standards geometry row
- no closure for residual handbook pitch class `1.50 mm`
- no closeout for `connector-origin` or stronger `installation-mark` authority

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `0p75_mm_now_has_three_microchip_exact_rows_plus_one_renesas_second_owner_exact_data_page_plus_one_nxp_third_owner_exact_data_page_plus_one_intel_hosted_fourth_owner_exact_table`
  - `1p50_mm_and_non_bga_authority_gaps_still_open`
