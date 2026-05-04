---
lane: "P4-60A formula local split-and-coverage recheck"
title: "Local recheck for 2025.11.10 Ohm's law and watts-to-amps formula lane"
status: "completed_at_claim_family_level"
reviewed_at: "2026-04-30"
owner_scope: "/code/blogs/llm_wiki/logs/p4-60a-2025-11-10-formula-lane-local-recheck.md"
input_root: "/code/blogs/tmps/2025.11.10/en"
---

# Purpose

- Assigned lane: `P4-60A formula local split-and-coverage recheck`
- Goal: recheck whether existing local `llm_wiki` support already covers unit identity or formula vocabulary, sharpen the exact split between institution-grade formula pedagogy and PCB consequence claims, and recommend the tightest main-agent promotion boundary if external sources land.
- Drafts were treated as claim inventory only, not as authority.
- Output-only boundary honored: no tracker edits, no fact/wiki/source-registry edits, and no edits outside this log.

# Inputs Reviewed

## Draft inputs

- `/code/blogs/tmps/2025.11.10/en/ohms-law.md`
- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`

## Prior local lane logs

- `/code/blogs/llm_wiki/logs/p4-58b-2025-11-10-formula-pedagogy-authority-scout.md`
- `/code/blogs/llm_wiki/logs/p4-59a-2025-11-10-formula-split-and-local-coverage-prep.md`

## Targeted local `llm_wiki` support checked

- `/code/blogs/llm_wiki/wiki/processes/power-energy-pcb-pcba-review-boundaries.md`
- `/code/blogs/llm_wiki/facts/methods/thermal-pcb-platform-selection-posture.md`
- `/code/blogs/llm_wiki/facts/methods/controlled-impedance-tdr-verification-posture.md`
- `/code/blogs/llm_wiki/facts/methods/parameter-scope-public-capability-impedance-and-validation.md`
- `/code/blogs/llm_wiki/facts/methods/power-energy-inverter-charger-rewrite-boundary.md`
- `/code/blogs/llm_wiki/sources/registry/methods/keysight-power-integrity-analysis-page.md`
- `/code/blogs/llm_wiki/logs/backlog.md`
- `/code/blogs/llm_wiki/logs/phase-status.md`

# Local Coverage Recheck

## What local support does cover

- `wiki/processes/power-energy-pcb-pcba-review-boundaries.md`
  - supports board-level review framing for power-energy articles: board partitioning, connector or harness handoff, thermal-platform choice, validation gates, and final functional validation.
  - does not authorize formula teaching or unit-identity pedagogy.
- `facts/methods/thermal-pcb-platform-selection-posture.md`
  - supports the split between MCPCB, heavy copper, and ceramic as distinct thermal platforms.
  - useful for conservative thermal-platform vocabulary, but not for current math or Ohm's-law exposition.
- `facts/methods/controlled-impedance-tdr-verification-posture.md`
  - supports controlled-impedance and verification vocabulary only.
  - adjacent to validation language, but not a formula source.
- `facts/methods/parameter-scope-public-capability-impedance-and-validation.md`
  - supports page-scoped impedance and validation claims.
  - still not a universal formula authority or a unit-definition source.
- `sources/registry/methods/keysight-power-integrity-analysis-page.md`
  - supports power-integrity vocabulary.
  - does not supply generic Ohm's-law pedagogy, watts-to-amps instruction, or unit identity.
- `logs/backlog.md` and `logs/phase-status.md`
  - continue to keep the November 2025 formula pages in a blocked / residual posture rather than a learned one.

## What local support does not cover

- No checked local file provides direct unit identity coverage for volt, ampere, ohm, or watt as authoritative teaching content.
- No checked local file provides a dedicated fact card for Ohm's-law pedagogy.
- No checked local file provides a dedicated fact card for watts-to-amps conversion pedagogy.
- No checked local file upgrades the drafts from claim inventory into reusable formula authority.

# Split Guidance

## Institution-grade formula pedagogy lane

- Keep `ohms-law.md` confined to formula identity, variable relationships, and basic pedagogy only after institution-grade or primary sources land.
- Keep `watts‑to‐amps.md` confined to conversion logic and unit relationships only after institution-grade or primary sources land.
- Treat historical framing, derivations, worked examples, calculator tables, and AC extensions as source-dependent teaching material, not as draft authority.
- Treat unit identity language as the first promotion gate: if the source pack does not explicitly anchor `volt`, `ampere`, `ohm`, and `watt`, the article should remain scout-only.

## PCB consequence lane

- Keep PCB trace-width, copper-weight, connector-rating, thermal, manufacturability, and simulation-adjacent claims separate from the formula pedagogy lane.
- Do not let basic formula identity automatically authorize board-design rules.
- Treat `IPC-2221` or similar standards mentions as blocked until a dedicated standards or current-carrying source lane exists.
- Treat any statement that converts a formula into a design rule as a second evidence lane, not as a continuation of the educational formula page.

# Recurring Claim Shapes In The Drafts

## Shared claim family

- formula identity presented as teaching authority without institutional or primary sources
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

## `watts‑to‑amps.md` claim shapes

- DC, AC, and three-phase conversion formulas as reusable authority
- power-factor teaching
- example tables and calculator framing
- trace-width, copper-weight, connector-rating, thermal, and manufacturability consequences stated as if formula alone were sufficient
- `IPC-2221` invocation without a dedicated current-carrying source lane

# Safe Reuse Classes

- blocked-status mention that `ohms-law.md` and `watts‑to‑amps.md` remain formula-pedagogy residuals in the `2025.11.10` batch
- board-level review context around power distribution, validation, connector or harness handoff, and thermal-platform choice
- thermal-platform split language for `MCPCB`, heavy copper, and ceramic as separate options
- controlled-impedance and validation vocabulary when the draft only needs guarded adjacent context
- deletion-safe preservation of the split between formula pedagogy and PCB consequence claims

# Blocked Claim Classes

- formula identity taught as authority without institutional or primary sources
- unit-identity instruction for volt, ampere, ohm, and watt without a dedicated source pack
- worked examples, calculator tables, pedagogical derivations, and historical framing
- ohmic vs non-ohmic device taxonomy and I-V curve teaching
- AC impedance / reactance and generalized `V = IZ` teaching
- DC / AC / three-phase conversion formulas and power-factor instruction
- PCB trace-width, copper-weight, connector-rating, thermal, and manufacturability consequences stated as standards-backed from basic formulas alone
- `IPC-2221` or similar standards invocation without an actual source lane

# Residual Source Gaps

- no direct institutional or primary-source pack yet for unit identity and formula pedagogy
- no direct `llm_wiki` fact card yet for Ohm's-law instruction
- no direct `llm_wiki` fact card yet for watts-to-amps instruction
- no dedicated source lane yet for current-carrying, trace-planning, or thermal consequence claims that the drafts attach to formula sections
- no dedicated standards lane yet for the `IPC-2221` references in the PCB consequence draft

# Promotion Boundary

- If external sources land, the tightest safe main-agent promotion boundary is:
  1. unit identity and formula vocabulary first, using institution-grade electrical fundamentals sources
  2. only then the minimal formula-identity and pedagogy layer for `V = I × R` and `current = power / voltage`
  3. only after that, a separate evidence lane for PCB consequences such as trace width, copper weight, thermal behavior, connector loading, and manufacturability
- Do not promote PCB consequence claims merely because formula identity is now sourced.
- Do not merge the educational formula lane with the board-design consequence lane until each has its own evidence pack.

# Verification Notes

- Existing local support depth is `adjacent_context_only`.
- The local repo currently supports board-review language and thermal/impedance posture, but not formula authority.
- This recheck did not find a local source that closes the unit-identity gap.
- The narrowest next recovery target remains institution-grade electrical fundamentals, not PCB consequence expansion.

# Completion Status

- lane status: `completed_at_claim_family_level`
- existing support depth: `adjacent_context_only`
- primary blocker: `blocked_pending_official_source`
- current posture: keep formula pedagogy separate from PCB consequence claims until institution-source recovery lands

# Final Disposition

- `ohms-law.md` and `watts‑to‐amps.md` remain scout-only today.
- Existing local `llm_wiki` support is enough for guarded board-review context, thermal-platform separation, and validation vocabulary.
- Existing local `llm_wiki` support is not enough for unit identity, formula pedagogy, or PCB design-rule authority.
