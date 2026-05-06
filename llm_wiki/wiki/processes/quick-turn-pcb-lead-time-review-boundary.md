---
topic_id: "processes-quick-turn-pcb-lead-time-review-boundary"
title: "Quick-Turn PCB Lead-Time Review Boundary"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-05"
fact_ids:
  - "methods-pcb-quickturn-lead-time-clock-separation"
  - "methods-pcb-prototype-quickturn-and-volume-routing"
  - "methods-pcb-cost-driver-review-and-quote-preparation-boundary"
  - "methods-international-pcb-shipping-customs-document-boundary"
source_ids:
  - "frontendapt-pcb-quick-turn-pcb-page-en"
  - "frontendapt-pcb-pcb-prototype-page-en"
  - "frontendapt-pcb-npi-small-batch-pcb-manufacturing-page-en"
  - "frontendapt-quote-index-en"
  - "icc-incoterms-rules"
  - "dhl-customs-clearance-documents"
tags: ["pcb", "quick-turn", "lead-time", "routing", "dfm", "shipping", "quote"]
---

# Definition

> Quick-turn PCB lead-time writing must review three separate clocks before publication: the `quote / DFM clock`, the `factory routing clock`, and the `shipping / customs clock`. Public content may explain how those clocks interact, but it should not collapse them into one universal promise.

## Why This Topic Matters

- Many low-quality quick-turn articles are inaccurate because they present `lead time` as a single number.
- The local source layer already supports a cleaner explanation: urgency changes the routing posture, while package completeness and board complexity change whether the route is even eligible.
- This page gives future blog rewrites a reusable boundary so quick-turn copy stays technical instead of promotional.

## Review Model

### Clock 1: Quote / DFM

| Clock | What it covers | Safe framing |
|---|---|---|
| Quote / DFM clock | File intake, stackup review, BOM clarity, engineering questions, manufacturability clarification | Review responsiveness and package readiness, not fabrication completion |

### Clock 2: Factory Routing

| Clock | What it covers | Safe framing |
|---|---|---|
| Factory routing clock | Production release after review, board-family fit, stackup route, process complexity, inspection path | Accelerated lane after engineering release, not universal same-day proof |

### Clock 3: Shipping / Customs

| Clock | What it covers | Safe framing |
|---|---|---|
| Shipping / customs clock | Export paperwork, customs readiness, carrier transit | Separate delivery lane after factory release |

## Stable Facts

- Quick-turn is best treated as a schedule-compression posture rather than a synonym for prototype.
- Simpler baseline FR-4 boards are the clearest public example of accelerated routing because advanced structures introduce more conditional gates.
- Incomplete documentation can delay the start of the factory clock because manufacturing review and clarification happen before production release.
- Shipping timing should remain separate from fabrication timing because customs and carrier transit are outside the factory route.
- Cost discussion should stay in `complexity / quote-preparation` language unless dated cost records are added.

## Engineering Boundaries

- Keep quick-turn, prototype, NPI, and mass production as separate routing labels.
- Keep quote timing, production timing, and shipping timing separate.
- Do not publish fixed expedite premiums, exact queue promises, or universal turnaround windows unless a dated owned capability record exists.
- Do not describe multilayer, HDI, RF, flex, ceramic, or specialty-material jobs as if they inherit the same timing as baseline boards.
- Do not write `delivered in X days` unless the clocks and assumptions are explicitly separated and source-backed.

## Must Refresh Before Publishing

- exact quick-turn day-count promises
- exact cut-off windows
- exact expedite-fee percentages
- live material-stock statements
- queue priority or weekend-shift claims
- carrier transit promises tied to total order delivery

## Related Fact Cards

- `methods-pcb-quickturn-lead-time-clock-separation`
- `methods-pcb-prototype-quickturn-and-volume-routing`
- `methods-pcb-cost-driver-review-and-quote-preparation-boundary`
- `methods-international-pcb-shipping-customs-document-boundary`

## Primary Sources

- /code/hileap/frontendAPT/public/static/pcb/en/quick-turn-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-prototype.json
- /code/hileap/frontendAPT/public/static/pcb/en/npi-small-batch-pcb-manufacturing.json
- /code/blogs/llm_wiki/sources/registry/internal/frontendapt-quote-index-en.md
- https://iccwbo.org/business-solutions/incoterms-rules/
- https://www.dhl.com/discover/en-global/logistics-advice/import-export-advice/customs-clearance-documents
