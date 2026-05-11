# P4-466 NXP Third-Owner 0.75 mm Reflow-Footprint Landing

Date: 2026-05-11
Parent lane: `P4-315`
Execution mode: `subagent_aided_exact_data_landing`

## Purpose

Advance the `0.75 mm` residual lane beyond `three Microchip exact rows plus one Renesas second-owner exact-data page` by landing one directly verified current-public third-owner exact-data page set from an official NXP package-information PDF.

## Inputs

- official NXP current-public package-information PDF `SOT1908-1`
- current `0.75 mm` repo stack through:
  - `logs/p4-316-2026-5-8-microchip-0p75mm-tfbga-land-pattern-landing.md`
  - `logs/p4-320-2026-5-8-microchip-second-0p75mm-tfbga-row-landing.md`
  - `logs/p4-324-2026-5-8-microchip-third-0p75mm-tfbga-row-landing.md`
  - `logs/p4-400-2026-5-10-renesas-second-owner-0p75mm-exact-data-page-landing.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

## What Landed

### New source record

- `sources/registry/methods/nxp-sot1908-1-fbga448-0p75mm-reflow-footprint.md`

### New exact-data fact card

- `facts/methods/nxp-0p75mm-fbga448-reflow-footprint.md`

### Route integration

Updated:

- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## What Landed Safely

- one directly verified current-public third-owner exact-data page set for the named `FBGA448 / SOT1908-1` `0.75 mm` package
- one visible `Reflow soldering footprint part 1/2/3` page set carrying reusable visible values `448X φ0.45`, `448X φ0.35`, and `27X 0.75`
- one visible process-note value `recommended stencil thickness: 0.125`
- one stronger continuation state where `0.75 mm` no longer stops at `Microchip + Renesas`

## What Did Not Land

- no universal `0.75 mm pitch -> land pattern` rule
- no cross-vendor `0.75 mm` closeout
- no closure for residual handbook pitch class `1.50 mm`
- no closeout for `connector-origin` or stronger `installation-mark` authority

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `0p75_mm_now_has_three_microchip_exact_rows_plus_one_renesas_second_owner_exact_data_page_plus_one_nxp_third_owner_exact_data_page`
  - `1p50_mm_and_non_bga_authority_gaps_still_open`
