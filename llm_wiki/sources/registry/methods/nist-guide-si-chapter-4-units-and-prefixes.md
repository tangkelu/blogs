---
source_id: "nist-guide-si-chapter-4-units-and-prefixes"
title: "NIST Guide to the SI, Chapter 4: The Two Classes of SI Units and the SI Prefixes"
organization: "National Institute of Standards and Technology"
source_type: "government_reference"
url: "https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes"
jurisdiction: "United States"
published_at: ""
checked_at: "2026-04-30"
trust_tier: "t1"
stability: "stable"
must_refresh: false
topic_tags: ["nist", "si", "ampere", "volt", "watt", "ohm", "unit-identity", "electrical-formulas"]
status: "active"
notes: "Use for SI unit identity and the unit-expression relationships among ampere, volt, watt, and ohm. Do not stretch this source into worked examples, PCB current-carrying rules, or general design guidance."
---

# Source Summary

## What It Covers

- `ampere (A)` as the SI base unit of electric current
- `watt (W)` as the SI coherent derived unit for power
- `volt (V)` as the SI coherent derived unit for electric potential difference
- `ohm` as the SI coherent derived unit for electric resistance
- unit expressions including `V = W/A` and `ohm = V/A`

## Why It Matters

- Gives `llm_wiki` a primary standards-grade anchor for the unit-identity layer behind `ohms-law.md` and `watts‑to‐amps.md`.
- Supports narrow algebraic restatements when they are presented explicitly as inference from SI unit expressions rather than as a full teaching pack.

## Extraction Notes

- Safe for unit names, symbols, quantity names, and SI unit-expression relationships.
- Safe to infer `W = V x A`, `A = W / V`, and `V = I x R` only when that inference is clearly labeled as algebraic rearrangement from unit expressions or paired with a teaching source.
- Do not use this source alone for derivations, worked examples, AC / three-phase formulas, power-factor teaching, or PCB design consequences.

## Refresh Notes

- Stable NIST reference; refresh only if publication structure or line-level wording becomes important.
