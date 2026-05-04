---
fact_id: "methods-connector-current-rating-selection-boundary"
title: "Connector current-aware writing is source-backed only at official current-field check boundary"
topic: "connector current rating selection boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-30"
source_ids:
  - "te-power-systems-connectors-in-power-systems"
  - "te-economy-power-2-5-connectors-page"
  - "molex-extreme-lphpower-page"
  - "phoenix-contact-hv-m5-1-nff-1056835-page"
tags: ["watts-to-amps", "connector", "current-rating", "nominal-current", "selection-boundary", "datasheet", "boundary"]
---

# Canonical Summary

> Current official connector-owner pages support one narrow connector-selection boundary only: after required current is known, check the candidate connector's manufacturer-published current field on the official product page or datasheet. The current corpus does not authorize safety-margin rules, per-pin aggregation laws, thermal-rise reasoning, universal part-selection claims, or generalized component-rating advice from this lane alone.

## Stable Facts

- Official connector-owner guidance can treat required current as one connector-selection input.
- Official connector pages publish current-related fields under varying names such as `Maximum Current Rating (A)`, `Current (MAX per contact)`, and `nominal current`.
- Once current is known, it is safe to compare candidate connectors against the manufacturer-published current field on the official page or datasheet.
- The connector current-field check remains separate from board trace sizing, route-selection, validation-workflow, and production-readiness lanes.

## Conditions And Methods

- Use this card for `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md` only after separating formula identity, conductor-sizing, validation-workflow, and named-tool claims from connector claims.
- Safe posture: say that current can be used as one screening input for connector review after the required current is known.
- Safe wording: tell readers to check the connector owner's published current field on the official product page or datasheet.
- Safe field wording: current fields may appear as `current rating`, `maximum current rating`, `current (MAX per contact)`, or `nominal current` depending on the connector owner and page.
- Pair this card with `methods-current-carrying-trace-width-and-copper-boundary` when a draft mixes board conductor sizing with connector review.
- Pair this card with `methods-tht-pressfit-terminal-route-boundary` only if the draft also needs to separate board-mounted connector route choice from off-board cable or harness integration.

## Limits And Non-Claims

- This card does not authorize `plus a safety margin` instructions or formulas.
- It does not authorize regulator-current, generic component-rating, or electromechanical-part claims outside connector-owner current fields.
- It does not authorize per-pin aggregation rules, current-sharing rules, thermal-rise explanations, derating rules, or voltage-drop budgets.
- It does not prove that a candidate connector is suitable, reliable, manufacturable, or production-ready.
- It does not authorize exact connector-family current numerics unless the exact owner page or datasheet is the cited authority in the publication workflow.

## Open Questions

- Add a separate current-rated component lane only if future drafts truly need regulator, contactor, relay, or other component-owner current fields.
- Add part-family datasheet support later if future copy needs exact connector numerics or application-conditioned suitability claims.

## Source Links

- https://www.te.com/en/products/connectors/power-connectors/intersection/communications-power-connectors.html
- https://www.te.com/en/products/connectors/power-connectors/intersection/economy-power-2-5-connectors.html
- https://www.molex.com/en-us/products/connectors/board-to-board-connectors/extreme-power-products/extreme-lphpower
- https://www.phoenixcontact.com/en-us/products/bolt-connection-terminal-block-hv-m51-nff-1056835
