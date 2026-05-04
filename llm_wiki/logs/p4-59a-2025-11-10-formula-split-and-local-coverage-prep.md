---
lane: "P4-59A formula split and local coverage prep"
title: "Deletion-safe prep for splitting institutional formula pedagogy from PCB consequence claims"
status: "completed_at_claim_family_level"
reviewed_at: "2026-04-30"
owner_scope: "/code/blogs/llm_wiki/logs/p4-59a-2025-11-10-formula-split-and-local-coverage-prep.md"
input_root: "/code/blogs/tmps/2025.11.10/en"
---

# Purpose

- Assigned lane: `P4-59A formula split and local coverage prep`
- Goal: produce a deletion-safe prep log for `ohms-law.md` and `watts‑to‐amps.md` that sharpens the split between institutional formula pedagogy and PCB trace / thermal consequence claims.
- Drafts were treated as claim inventory only, not as authority.
- Output-only boundary honored: no tracker edits, no fact/wiki/source-registry edits, and no edits outside this log.

# Input Files Inspected

## Draft inputs

- `/code/blogs/tmps/2025.11.10/en/ohms-law.md`
- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`

## Directly relevant existing `llm_wiki` files

- `/code/blogs/llm_wiki/logs/p4-58b-2025-11-10-formula-pedagogy-authority-scout.md`
- `/code/blogs/llm_wiki/logs/p4-40-2025-11-10-ems-electronics-rf-tools-official-source-recovery-scout.md`
- `/code/blogs/llm_wiki/logs/p4-44-source-backed-integration.md`
- `/code/blogs/llm_wiki/logs/backlog.md`
- `/code/blogs/llm_wiki/logs/phase-status.md`
- `/code/blogs/llm_wiki/wiki/processes/power-energy-pcb-pcba-review-boundaries.md`
- `/code/blogs/llm_wiki/facts/methods/power-energy-inverter-charger-rewrite-boundary.md`
- `/code/blogs/llm_wiki/sources/registry/methods/keysight-power-integrity-analysis-page.md`

# Existing `llm_wiki` Support Found

## Reusable support already present

- `logs/p4-58b-2025-11-10-formula-pedagogy-authority-scout.md`
  - already classifies `ohms-law.md` and `watts‑to‐amps.md` as `blocked_pending_official_source`.
  - isolates the remaining need as institution-source formula authority plus a separate evidence lane for PCB current / thermal consequence claims.
- `logs/p4-40-2025-11-10-ems-electronics-rf-tools-official-source-recovery-scout.md`
  - confirms both drafts were never promoted beyond claim-family inventory.
  - keeps `ohms-law.md` and `watts‑to‐amps.md` in the general-education blocker bucket.
- `logs/p4-44-source-backed-integration.md`
  - upgraded other November 2025 lanes, but did not add any formula-teaching layer.
- `wiki/processes/power-energy-pcb-pcba-review-boundaries.md`
  - supports conservative board-level review language around thermal-platform choice, connector or harness handoff, and validation gates.
  - does not authorize formula pedagogy or trace-current math.
- `facts/methods/power-energy-inverter-charger-rewrite-boundary.md`
  - supports separation between board-level review and downstream performance claims.
  - does not authorize current, voltage, power, efficiency, or field-life claims.
- `sources/registry/methods/keysight-power-integrity-analysis-page.md`
  - supports PDN and power-integrity vocabulary only.
  - does not support generic Ohm's-law teaching, watts-to-amps conversion teaching, or trace-width design rules.
- `logs/backlog.md` and `logs/phase-status.md`
  - already place `ohms-law.md` and `watts‑to‐amps.md` in the residual blocked queue after P4-58.

## Coverage conclusion

- Current `llm_wiki` support is useful for board-review framing and power-integrity vocabulary.
- Current `llm_wiki` support is weak for formula authority.
- The repo can safely support conservative language about board partitioning, validation gates, and thermal-platform review, but it cannot yet support formula teaching, worked examples, or PCB trace / thermal consequence claims as facts.

# Split Guidance

## Institutional formula pedagogy lane

- Keep `ohms-law.md` focused on formula identity, variable relationships, and basic pedagogy only after official or institutional sources are added.
- Keep `watts‑to‐amps.md` focused on conversion logic and unit relationships only after official or institutional sources are added.
- Treat historical framing, derivations, worked examples, and generalized AC extensions as source-dependent teaching material, not as draft authority.

## PCB consequence lane

- Keep PCB trace-width, copper-weight, connector-rating, thermal, manufacturability, and simulation-adjacent claims separate from the formula pedagogy lane.
- Treat any statement that converts basic formulas into board-design rules as a second evidence lane, not as an automatic extension of the educational formula page.
- Keep `IPC-2221` or similar standards mentions blocked until there is a dedicated standards or current-carrying source lane.

# Recurring Claim Shapes In The Drafts

## Shared lane claims

- formula identity framed as teaching authority without institutional or primary sources
- worked examples, calculator tables, and explanatory derivations
- transitions from formula teaching into PCB manufacturability or thermal consequence claims

## `ohms-law.md` claim shapes

- historical-origin claims such as publication date and inventor framing
- analogy-based explanation presented as authoritative instruction
- derivation and equation expansion around voltage, current, and resistance
- ohmic vs non-ohmic device taxonomy and device examples
- I-V curve interpretation and slope claims
- power-law expansion such as `P = VI`, `P = I^2R`, and `P = V^2/R`
- AC extension to impedance / reactance and `V = IZ`

## `watts‑to‐amps.md` claim shapes

- DC, AC, and three-phase conversion formulas as reusable authority
- power-factor teaching
- example tables and calculator framing
- trace-width, copper-weight, connector-rating, thermal, and manufacturability consequences stated as if formula alone were sufficient
- `IPC-2221` invocation without a dedicated current-carrying source lane

# Safe Reuse Classes

- blocked-status mention that `ohms-law.md` and `watts‑to‐amps.md` remain formula-pedagogy residuals in the `2025.11.10` batch
- board-level review context around power distribution, validation, connector or harness handoff, and thermal-platform choice
- deletion-safe preservation of the split between formula pedagogy and PCB consequence claims
- cautionary language that drafts are claim inventory only, not authority

# Blocked Claim Classes

- formula identity taught as authority without institutional or primary sources
- worked examples, calculator tables, pedagogical derivations, and historical framing
- ohmic vs non-ohmic device taxonomy and I-V curve teaching
- AC impedance / reactance and generalized `V = IZ` teaching
- DC / AC / three-phase conversion formulas and power-factor instruction
- PCB trace-width, copper-weight, connector-rating, thermal, and manufacturability consequences stated as standards-backed from basic formulas alone
- `IPC-2221` or similar standards invocation without an actual source lane

# Official-Source Gaps

- no direct institutional or primary-source pack yet for unit identity and formula pedagogy
- no direct `llm_wiki` fact card or wiki page yet for Ohm's law instruction
- no direct `llm_wiki` fact card or wiki page yet for watts-to-amps instruction
- no dedicated source lane yet for current-carrying, trace-planning, or thermal consequence claims that the drafts attach to formula sections
- no dedicated standards lane yet for the `IPC-2221` references in the PCB consequence draft

# Strongest Next Recovery Lane

- lane: `institutional electrical fundamentals formula recovery`
- status target: `source_backed_fact_layer_partial`
- best recovery sequence:
  1. `NIST` SI / unit-identity sources for volt, ampere, ohm, and watt
  2. one strong institutional teaching source for Ohm's law and power relations, such as `DOE` or a university EE / physics page
  3. if `watts‑to‐amps.md` must keep PCB consequence language, add a separate standards or institution lane for current-carrying and trace-planning context
- expected unlock:
  a narrow formula-identity and unit-pedagogy boundary
- still not unlocked even after that lane:
  board-current, trace-width, copper-weight, and thermal consequence claims unless a separate evidence lane is added

# Changed Files

- `/code/blogs/llm_wiki/logs/p4-59a-2025-11-10-formula-split-and-local-coverage-prep.md`

# Completion Status

- lane status: `completed_at_claim_family_level`
- existing support depth: `adjacent_context_only`
- primary blocker: `blocked_pending_official_source`
- current posture: keep formula pedagogy separate from PCB consequence claims until institution-source recovery lands

# Final Disposition

- `ohms-law.md` and `watts‑to‐amps.md` remain scout-only today.
- The narrowest next official-source lane is institution-grade electrical fundamentals, not PCB consequence or standards expansion.
- Current `llm_wiki` support is enough for board-review context, but not enough for formula teaching or design-rule authority.
