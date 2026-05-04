---
fact_id: "methods-electrical-formula-identity-boundary"
title: "Electrical formula writing is source-backed only for SI unit identity plus minimal Ohm's law and electric-power relationships"
topic: "electrical formula identity boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-30"
source_ids:
  - "nist-guide-si-chapter-4-units-and-prefixes"
  - "nist-ampere-introduction"
  - "openstax-university-physics-v2-ohms-law"
  - "openstax-university-physics-v2-electrical-energy-and-power"
tags: ["ohms-law", "watts-to-amps", "voltage", "current", "resistance", "power", "si-units", "formula-boundary"]
---

# Canonical Summary

> Current NIST and OpenStax sources support a conservative electrical-formula boundary only at SI unit identity and minimal circuit-relationship level: `ampere` as electric current, `volt` as electric potential difference or voltage, `watt` as power, `ohm` as resistance, `Ohm's law` as the guarded voltage-current-resistance relationship, and electric power as the guarded `current times voltage` relationship. These sources do not authorize broad historical teaching, worked examples, AC or three-phase conversions, or PCB trace / thermal / connector consequence claims.

## Stable Facts

- NIST Chapter 4 supports `ampere (A)` as the SI base unit for electric current.
- The same NIST chapter supports `watt (W)` as the SI derived unit for power, `volt (V)` as the SI derived unit for electric potential difference, and `ohm` as the SI derived unit for electric resistance.
- The same NIST chapter provides the unit-expression relationships `V = W/A` and `ohm = V/A`.
- NIST's ampere introduction supports electric current as charge in motion per unit time and supports one ampere as one coulomb per second.
- OpenStax `9.4 Ohm's Law` supports the guarded teaching statement that current through many materials is directly proportional to the applied voltage and supports the voltage-current-resistance identity layer for a resistor-focused Ohm's law boundary.
- OpenStax `9.5 Electrical Energy and Power` supports electric power as the rate of energy transfer in a circuit and supports the guarded relationship that power supplied is equal to current times voltage.
- A narrow `A = W / V` restatement is supportable when it is presented as algebraic rearrangement from the sourced power-voltage-current relationship and NIST unit expressions, not as a full calculator or design-rule pack.

## Conditions And Methods

- Use this card for `/code/blogs/tmps/2025.11.10/en/ohms-law.md` and `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md` only after reducing them to unit identity and minimal formula-relationship wording.
- Safe `Ohm's law` posture: define voltage, current, and resistance conservatively, then keep the article on the resistor-focused relationship boundary.
- Safe `watts-to-amps` posture: define power, voltage, and current conservatively, then present `A = W / V` only as a narrow algebraic restatement for fixed-power and fixed-voltage framing.
- Pair this card with existing power-review and validation pages only when the article needs adjacent board-level context; do not let that adjacent context silently authorize PCB design rules.
- Open a separate evidence lane before publishing any statement that converts formula identity into trace width, copper weight, connector loading, thermal rise, manufacturability, simulation, or compliance guidance.

## Limits And Non-Claims

- This card does not authorize historical-origin storytelling, inventor biography, or analogy-driven pedagogy.
- It does not authorize worked examples, calculator tables, FAQ packs, or numeric lookup charts as reusable fact-layer content.
- It does not authorize nonohmic taxonomy, diode or I-V curve teaching, or generalized `V = IZ` / impedance lessons.
- It does not authorize AC, three-phase, apparent-power, reactive-power, or power-factor instruction.
- It does not authorize `P = I^2R`, `P = V^2/R`, or similar extended formula families unless a later source pass chooses to recover and write that lane explicitly.
- It does not authorize PCB trace-width, copper-weight, connector-rating, thermal, DFM, DFT, simulation, `IPC-2221`, or supplier-capability claims.

## Open Questions

- Add a dedicated standards or institutional lane if future drafts must connect current values to conductor sizing, trace planning, connector loading, or thermal behavior.
- Add a separate teaching lane if future formula pages must keep worked examples, broader power formulas, or AC / three-phase instruction.
- Add a separate standards lane if any future draft must mention `IPC-2221` or equivalent current-carrying guidance.

## Source Links

- https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- https://www.nist.gov/si-redefinition/ampere-introduction
- https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law
- https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power
