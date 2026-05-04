---
topic_id: "processes-electrical-formula-identity-boundaries"
title: "Electrical Formula Identity Boundaries"
category: "processes"
status: "draft"
last_reviewed_at: "2026-04-30"
fact_ids:
  - "methods-electrical-formula-identity-boundary"
  - "methods-power-energy-inverter-charger-rewrite-boundary"
source_ids:
  - "nist-guide-si-chapter-4-units-and-prefixes"
  - "nist-ampere-introduction"
  - "openstax-university-physics-v2-ohms-law"
  - "openstax-university-physics-v2-electrical-energy-and-power"
tags: ["ohms-law", "watts-to-amps", "voltage", "current", "resistance", "power", "formula-boundary", "draft-boundary"]
---

# Definition

> `ohms-law.md` and `watts‑to‐amps.md` are now safe only at a conservative formula-identity boundary: SI unit identity for `ampere`, `volt`, `watt`, and `ohm`; guarded `Ohm's law` vocabulary around voltage, current, and resistance; and guarded electric-power vocabulary around `power equals current times voltage`, including a narrow `A = W / V` restatement. The current corpus is still not strong enough for full general-electronics teaching, calculator content, AC-power coverage, or PCB design-rule consequences.

## Why This Topic Matters

- The two `2025.11.10` drafts mix basic electrical formulas with unsourced pedagogy and with downstream PCB consequence claims.
- The new source pack creates a reusable middle ground: enough authority for minimal formula identity, but not enough to justify broad tutorial or board-design content.
- This page gives future rewrite work a prompt-consumable map so those drafts do not fall back into mixed formula-plus-PCB overclaiming.

## Stable Facts

- NIST now anchors the SI unit identity of `ampere`, `volt`, `watt`, and `ohm`.
- OpenStax now anchors the minimal relationship layer for `Ohm's law` and electric power in a teaching context.
- `ohms-law.md` can now route through voltage-current-resistance identity only, not through broad component taxonomy or AC extensions.
- `watts‑to‐amps.md` can now route through guarded power-current-voltage identity only, including a narrow `A = W / V` restatement, not through calculator-table or board-sizing content.
- Existing power-review boundary pages remain useful only as adjacent PCB / PCBA context, not as proof that basic formulas already authorize board design claims.

## Engineering Boundaries

- Keep `ohms-law.md` on the identity layer for voltage, current, resistance, and the guarded Ohm's law relationship.
- Keep `watts‑to‐amps.md` on the identity layer for power, current, voltage, and the guarded algebraic restatement used to convert power to current when voltage is known.
- Treat educational formula identity and PCB consequences as separate evidence lanes.
- Treat the current formula lane as source-backed partial, not as a full electrical-engineering tutorial pack.

## Common Overclaims To Block

- historical storytelling about Georg Ohm as if that were part of the reusable fact layer
- water-flow analogies, broad nonohmic examples, and I-V curve interpretation
- AC, three-phase, reactive-power, apparent-power, or power-factor formula teaching
- calculator tables, FAQ grids, or worked-example batches presented as source-backed inventory
- `trace width`, `copper weight`, `connector rating`, `thermal rise`, `simulation`, or `IPC-2221` conclusions inferred directly from the recovered formula layer
- `HILPCB` capability, service, quality, or design-assistance claims

## Must Refresh Before Publishing

- Any formula page framed as `complete guide`, `calculator`, or `design rule`
- Any current source wording that depends on exact textbook chapter formatting
- Any statement linking current math to conductor sizing, thermal behavior, or standards compliance
- Any statement extending the lane into AC, three-phase, or application-specific advice

## Supported Draft Families

- `/code/blogs/tmps/2025.11.10/en/ohms-law.md`
- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`

## Related Fact Cards

- `methods-electrical-formula-identity-boundary`
- `methods-power-energy-inverter-charger-rewrite-boundary`

## Primary Sources

- https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- https://www.nist.gov/si-redefinition/ampere-introduction
- https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law
- https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power
