# P4-60 Source-Backed Integration

Date: 2026-04-30

## Purpose

Controller-integrate the remaining `2025.11.10` formula residual lane after `P4-59`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote draft-originated history, calculator tables, AC / three-phase formulas, PCB current-carrying rules, `IPC-2221` consequences, or supplier-capability claims.

## Inputs Reviewed

- `logs/p4-58b-2025-11-10-formula-pedagogy-authority-scout.md`
- `logs/p4-59a-2025-11-10-formula-split-and-local-coverage-prep.md`
- `logs/p4-60a-2025-11-10-formula-lane-local-recheck.md`
- `logs/p4-60c-2025-11-10-watts-to-amps-institutional-authority-scout.md`
- `/code/blogs/tmps/2025.11.10/en/ohms-law.md`
- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`
- external institutional sources rechecked by the main agent:
  - NIST Guide to the SI, Chapter 4
  - NIST `Ampere: Introduction`
  - OpenStax `9.4 Ohm's Law`
  - OpenStax `9.5 Electrical Energy and Power`

## Parallel Work Pattern

- Main agent owned scope decisions, external verification, final source / fact / wiki writing, and tracker updates.
- One bounded `gpt-5.4-mini` worker produced `logs/p4-60a-2025-11-10-formula-lane-local-recheck.md` and confirmed that local support remained `adjacent_context_only`.
- One bounded `gpt-5.4` worker produced `logs/p4-60c-2025-11-10-watts-to-amps-institutional-authority-scout.md` and confirmed a narrow SI-vocabulary plus algebraic-conversion unlock.
- The separate `ohms-law` `gpt-5.4` scout lane hit rate-limit / usage-limit failures, so the main agent completed that official-source verification directly rather than leaving the lane blocked.

## Integrated Source-Backed Lane

### Electrical Formula Identity Boundary

Added official and institutional source records:

- `nist-guide-si-chapter-4-units-and-prefixes`
- `nist-ampere-introduction`
- `openstax-university-physics-v2-ohms-law`
- `openstax-university-physics-v2-electrical-energy-and-power`

Added fact card:

- `methods-electrical-formula-identity-boundary`

Added topic wiki:

- `processes-electrical-formula-identity-boundaries`

Supported draft families:

- `/code/blogs/tmps/2025.11.10/en/ohms-law.md`
- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`

What is now source-backed:

- SI unit identity for `ampere`, `volt`, `watt`, and `ohm`
- electric current as charge in motion per unit time and one ampere as one coulomb per second
- guarded `Ohm's law` identity at voltage-current-resistance relationship level
- guarded electric-power identity at `power equals current times voltage` level
- narrow `A = W / V` restatement when presented as algebraic rearrangement from sourced unit / power relationships

Still blocked:

- historical-origin framing, analogy-first pedagogy, and worked example packs
- nonohmic taxonomy, diode or I-V curve teaching, and generalized impedance / `V = IZ`
- AC, three-phase, reactive-power, apparent-power, and power-factor instruction
- calculator tables, FAQ grids, and broad formula-family expansion
- PCB trace-width, copper-weight, connector-rating, thermal, manufacturability, simulation, and `IPC-2221` consequence claims
- all HILPCB / APT service, quality, or capability claims

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft families:
  - `2025.11.10` `ohms-law.md` at formula-identity boundary level only
  - `2025.11.10` `watts‑to‐amps.md` at SI-vocabulary and narrow algebraic-conversion boundary level only
- next likely residual lane:
  - `PCB current-carrying / trace-planning / thermal consequence recovery` if those claims still need to survive in future rewrites
