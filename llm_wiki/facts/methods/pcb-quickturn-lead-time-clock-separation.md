---
fact_id: "methods-pcb-quickturn-lead-time-clock-separation"
title: "Quick-turn PCB lead-time writing must separate quote clock, factory clock, and shipping clock"
topic: "Quick-turn PCB lead-time clock separation"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-05"
source_ids:
  - "frontendapt-pcb-quick-turn-pcb-page-en"
  - "frontendapt-pcb-pcb-prototype-page-en"
  - "frontendapt-pcb-npi-small-batch-pcb-manufacturing-page-en"
  - "frontendapt-quote-index-en"
  - "methods-international-pcb-shipping-customs-document-boundary"
tags: ["pcb", "quick-turn", "lead-time", "quote", "shipping", "dfm", "clock-separation"]
---

# Canonical Summary

> Public quick-turn PCB content should not present `lead time` as one universal timer. The stable route is to separate `quote / DFM response time`, `factory build time after engineering release`, and `shipping / customs time`. This keeps urgent-routing copy useful without turning it into unsupported delivery promises.

## Stable Facts

- The internal quick-turn service layer supports describing accelerated handling as a distinct routing posture, not as a universal entitlement for every board family.
- The quote layer supports `DFM feedback within 24 hours` as a response commitment for intake and review, not as proof that every job can be fabricated or delivered in the same window.
- Prototype, quick-turn, NPI, and mass-production routing are already separated in the local corpus, so schedule wording should respect those boundaries instead of collapsing them.
- Shipping and customs sources support a separate `shipping clock` with document completeness, customs processing, and carrier transit as distinct variables.
- Board family, stackup complexity, special process selection, and package completeness all influence whether a build can enter an accelerated lane without proving any fixed number of days.

## Conditions And Methods

- Use this card when a draft wants to explain quick-turn PCB timing, urgent fabrication, or expedited quote posture.
- Safe structure:
  - `Quote / DFM clock`: starts when the package is submitted for review and covers data completeness, engineering questions, and manufacturability clarification.
  - `Factory clock`: starts only after the package is clear enough to release into production and should be described as route-dependent, not universal.
  - `Shipping clock`: covers export documents, customs readiness, and carrier transit after factory release.
- Safe public framing is:
  - quick-turn is a compressed routing posture
  - simple baseline boards are the clearest fit
  - multilayer, HDI, specialty materials, and incomplete packages make the route more conditional
  - timing should be discussed as `what changes the route`, not `what is always guaranteed`

## Limits And Non-Claims

- This card does not support universal `24h`, `48h`, or `72h` fabrication guarantees.
- It does not support cut-off-time guarantees, weekend-operation guarantees, or queue-priority guarantees as stable public facts.
- It does not support exact expedite price multipliers, fixed urgent-order surcharges, or universal standard-vs-expedite comparisons.
- It does not support live stock availability, current laminate inventory, or current assembly-line loading claims.
- It does not support total-delivery promises that merge factory time and shipping time into one number.

## Open Questions

- If the business wants stronger public timing commitments by board family, add dated plant-specific capability records with owner, scope, and refresh rules.

## Source Links

- /code/hileap/frontendAPT/public/static/pcb/en/quick-turn-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-prototype.json
- /code/hileap/frontendAPT/public/static/pcb/en/npi-small-batch-pcb-manufacturing.json
- /code/blogs/llm_wiki/sources/registry/internal/frontendapt-quote-index-en.md
- /code/blogs/llm_wiki/facts/methods/international-pcb-shipping-customs-document-boundary.md
