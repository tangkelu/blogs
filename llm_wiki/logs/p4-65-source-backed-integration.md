# P4-65 Source-Backed Integration

Date: 2026-04-30

## Purpose

Controller-integrate the next residual lane after `P4-64`: the remaining regulator half of the draft's broad `regulator or connector` current-rating wording, plus a deletion-safe residual map for what still remains blocked after that split.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote safety-margin rules, generic component-rating claims, current-limit-equals-output-current claims, thermal or derating explanations, or manufacturability and production-outcome claims.

## Inputs Reviewed

- `logs/p4-65a-2025-11-10-watts-to-amps-post-connector-residual-map.md`
- `logs/p4-65b-2025-11-10-regulator-current-limit-official-source-scout.md`
- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`
- existing local support:
  - `facts/methods/connector-current-rating-selection-boundary.md`
  - `facts/methods/current-carrying-trace-width-and-copper-boundary.md`
  - `facts/methods/pre-fabrication-validation-workflow-boundary.md`
  - `facts/methods/named-simulation-tool-entry-identity-boundary.md`

## Parallel Work Pattern

- Main agent owned scope decisions, source / fact / wiki writing, tracker updates, and verification.
- One bounded `gpt-5.4-mini` worker produced `logs/p4-65a-2025-11-10-watts-to-amps-post-connector-residual-map.md` and mapped the claim families that must remain blocked or be rewritten out after connector integration.
- One bounded `gpt-5.4` worker produced `logs/p4-65b-2025-11-10-regulator-current-limit-official-source-scout.md` and recovered the narrow official-source lane used here.

## Integrated Source-Backed Lane

### Regulator Current Field Selection Boundary

Added official source records:

- `ti-tps7a47-product-page`
- `ti-tps63027-product-page`
- `ti-tps631000-product-page`
- `analog-devices-lt1763-product-page`

Added fact card:

- `methods-regulator-current-field-selection-boundary`

Added topic wiki:

- `processes-regulator-current-field-selection-boundaries`

Supported draft family:

- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`

What is now source-backed:

- after load current is known, regulator review may include checking the owner-published current-related field on the official product page or datasheet
- `Output Current` or `Iout (max)` can be used as a direct screening field when the manufacturer presents that field
- `Current Limit` or `Switch Current Limit` may also appear on official regulator pages, but those fields stay separate from direct output-current wording unless the exact owner documentation defines the mapping

Still blocked:

- `plus a safety margin` instructions or formulas
- claims that `Current Limit` or `Switch Current Limit` equals safe continuous output current
- generic `component rating` wording that merges regulator, connector, and other part classes together
- thermal, derating, dropout, efficiency, reliability, manufacturability, or production-readiness claims
- exact unnamed regulator numerics unless the exact owner page or datasheet is the publication authority

## Residual Disposition After P4-65

- `watts‑to‑amps.md` now has narrow source-backed coverage for:
  - formula identity
  - board conductor-sizing boundary
  - pre-fabrication validation workflow boundary
  - named simulation-tool entry identity
  - connector current-field check boundary
  - regulator current-field check boundary
- The remaining unsafe residue is now mostly rewrite-governance work, not broad evidence recovery:
  - safety-margin language
  - validation or simulation as proof
  - manufacturability, reliability, and production-outcome claims
  - any attempt to merge board-consequence, connector, and regulator claims back into one generic sentence

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2025.11.10` `watts‑to‑amps.md` at regulator current-field selection boundary level only
- next likely action:
  - keep the remaining safety-margin and production-outcome residue blocked and push future rewrite work to use the recovered narrow lanes instead of searching for one universal component-rating rule
