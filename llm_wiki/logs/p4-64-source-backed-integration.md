# P4-64 Source-Backed Integration

Date: 2026-04-30

## Purpose

Controller-integrate the next residual lane after `P4-63`: the remaining connector-rating claims still attached to `watts‑to‑amps.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote safety-margin rules, regulator claims, generic component-rating claims, thermal or derating claims, or manufacturability and production-outcome claims.

## Inputs Reviewed

- `logs/p4-64a-2025-11-10-connector-rating-split.md`
- `logs/p4-64b-2025-11-10-connector-rating-local-coverage-recheck.md`
- `logs/p4-64c-2025-11-10-connector-rating-official-source-scout.md`
- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`
- existing local support:
  - `facts/methods/current-carrying-trace-width-and-copper-boundary.md`
  - `facts/methods/tht-pressfit-terminal-route-boundary.md`
  - `wiki/processes/power-interface-connector-assembly-route-selection.md`

## Parallel Work Pattern

- Main agent owned scope decisions, source / fact / wiki writing, tracker updates, and verification.
- One bounded `gpt-5.4-mini` worker produced `logs/p4-64a-2025-11-10-connector-rating-split.md` and cut the residual down to the narrowest plausible connector-selection boundary.
- One bounded `gpt-5.4-mini` worker produced `logs/p4-64b-2025-11-10-connector-rating-local-coverage-recheck.md` and confirmed that the pre-existing local corpus was not enough to promote connector-rating claims by itself.
- One bounded `gpt-5.4` worker produced `logs/p4-64c-2025-11-10-connector-rating-official-source-scout.md` and recovered the narrow official-source lane used here.

## Integrated Source-Backed Lane

### Connector Current Rating Selection Boundary

Added official source records:

- `te-power-systems-connectors-in-power-systems`
- `te-economy-power-2-5-connectors-page`
- `molex-extreme-lphpower-page`
- `phoenix-contact-hv-m5-1-nff-1056835-page`

Added fact card:

- `methods-connector-current-rating-selection-boundary`

Added topic wiki:

- `processes-connector-current-rating-selection-boundaries`

Supported draft family:

- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`

What is now source-backed:

- after current is known, connector review may include checking the candidate connector's manufacturer-published current field on the official product page or datasheet
- official connector pages expose current-related fields under different names such as `Maximum Current Rating (A)`, `Current (MAX per contact)`, and `nominal current`
- current can be used as one connector-screening input after the required current is known

Still blocked:

- `plus a safety margin` instructions or formulas
- regulator-current and generic component-rating claims
- per-pin aggregation, current-sharing, voltage-drop, thermal-rise, and derating explanations
- claims that connector-current review proves suitability, reliability, manufacturability, or production readiness
- exact connector current numerics unless the exact owner page or datasheet is the publication authority

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2025.11.10` `watts‑to‐amps.md` at connector current-rating selection boundary level only
- still separate lanes:
  - regulator-current and generic component-rating claims remain unrecovered
  - safety-margin and outcome claims remain unrecovered
