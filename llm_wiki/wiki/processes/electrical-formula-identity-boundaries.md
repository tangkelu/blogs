---
topic_id: "processes-electrical-formula-identity-boundaries"
title: "Electrical Formula Identity Boundaries"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
fact_ids:
  - "methods-electrical-formula-identity-boundary"
  - "methods-power-energy-inverter-charger-rewrite-boundary"
source_ids:
  - "nist-guide-si-chapter-4-units-and-prefixes"
  - "nist-ampere-introduction"
  - "openstax-university-physics-v2-ohms-law"
  - "openstax-university-physics-v2-electrical-energy-and-power"
tags: ["ohms-law", "watts-to-amps", "voltage", "current", "resistance", "power", "formula-boundary", "identity-boundary"]
---

# Routing Guidance

> Route `ohms-law` and `watts-to-amps` drafts through a narrow formula-identity lane only. The stable local support here covers SI unit identity for `ampere`, `volt`, `watt`, and `ohm`, a guarded voltage-current-resistance relationship for `Ohm's law`, and a guarded power-current-voltage relationship including a narrow `A = W / V` restatement. This lane does not support a full tutorial, calculator content, AC or three-phase teaching, PCB design-rule consequences, or capability and service claims.

## Draft Routing Map

| Draft signal | Safe route | Block if draft asks for |
| --- | --- | --- |
| `what is Ohm's law` | voltage, current, resistance identity and guarded relationship wording | full electronics tutorial |
| `watts to amps` | narrow `A = W / V` restatement when voltage is known | calculator tables or worked-example packs |
| `power formula` | `power equals current times voltage` at identity level | extended formula families or application-specific sizing |
| `board current` | stop at formula identity and open a separate PCB evidence lane | trace width, copper, connector, or thermal consequences |
| `charger` or `inverter` adjacency | use only as PCB and PCBA rewrite-boundary context | capability, performance, or service proof |

# Stable Facts

- NIST anchors the SI identity of `ampere`, `volt`, `watt`, and `ohm`.
- NIST's ampere introduction supports current as charge in motion per unit time and supports one ampere as one coulomb per second.
- OpenStax supports a guarded `Ohm's law` relationship for voltage, current, and resistance at resistor-focused identity level.
- OpenStax supports electric power as the rate of energy transfer and supports the guarded relationship `power equals current times voltage`.
- A narrow `A = W / V` restatement is supportable only as algebraic rearrangement of the sourced power-voltage-current relationship.
- The adjacent power-energy inverter and charger boundary card is usable only as context for keeping board-review language separate from formula identity.

# Engineering Boundaries

- Keep `ohms-law` content on the identity layer for voltage, current, resistance, and the guarded Ohm's law relationship.
- Keep `watts-to-amps` content on the identity layer for power, current, voltage, and the guarded algebraic restatement used when voltage is known.
- Treat educational formula identity and PCB consequences as separate evidence lanes.
- Treat adjacent inverter or charger rewrite guidance as PCB and PCBA review context, not as proof that formula identity authorizes system or product claims.
- Keep this lane source-backed but partial; it is not a complete electrical-engineering teaching pack.

# Blocked Claims

- full tutorial and calculator claims
- AC or three-phase formula teaching
- PCB design-rule consequence claims
- capability or service claims
- worked-example batches, FAQ grids, or numeric lookup tables presented as reusable fact inventory
- extended formula families such as `P = I^2R` or `P = V^2 / R` unless a later source pass lands them explicitly

# Common Misreadings

- Formula identity support does not mean the corpus now supports a complete guide to basic electronics.
- A narrow `A = W / V` restatement does not authorize calculator pages, tables, or scenario libraries.
- `Ohm's law` support here is resistor-focused identity language, not a full lesson on nonohmic behavior, impedance, or AC analysis.
- Formula identity does not prove trace width, copper weight, connector loading, thermal rise, simulation, or `IPC-2221` conclusions.
- Adjacent power-energy rewrite cards do not convert this lane into charger, inverter, or supplier capability authority.

# Must Refresh Before Publishing

- Any formula page framed as a `complete guide`, `calculator`, or `design rule`
- Any wording that depends on exact textbook chapter phrasing or formatting
- Any statement linking formula identity to conductor sizing, thermal behavior, connector limits, or standards compliance
- Any statement extending this lane into AC, three-phase, impedance, reactive power, or application-specific advice
- Any capability, service, quality, or supplier-positioning statement

# Related Facts

- `methods-electrical-formula-identity-boundary`
- `methods-power-energy-inverter-charger-rewrite-boundary`

# Source Scope

- `nist-guide-si-chapter-4-units-and-prefixes`
- `nist-ampere-introduction`
- `openstax-university-physics-v2-ohms-law`
- `openstax-university-physics-v2-electrical-energy-and-power`

# Supported Draft Families

- `/code/blogs/tmps/2025.11.10/en/ohms-law.md`
- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`
