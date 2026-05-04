---
lane: "P4-58B formula pedagogy authority scout"
title: "Authority scout for 2025.11.10 Ohm's law and watts-to-amps drafts"
status: "completed_at_claim_family_level"
reviewed_at: "2026-04-30"
owner_scope: "/code/blogs/llm_wiki/logs/p4-58b-2025-11-10-formula-pedagogy-authority-scout.md"
input_root: "/code/blogs/tmps/2025.11.10/en"
---

# Purpose

- Assigned lane: `P4-58B formula pedagogy authority scout`
- Goal: inspect `ohms-law.md` and `watts‑to‐amps.md` together as one formula-pedagogy residual lane, cross-check current `llm_wiki` support, and leave a deletion-safe map for later institution-source recovery.
- Drafts were treated as claim inventory only, not as authority.
- Output-only boundary honored: no tracker edits, no fact/wiki/source-registry edits, and no edits outside this log.

# Exact Files Reviewed

## Draft inputs

- `/code/blogs/tmps/2025.11.10/en/ohms-law.md`
- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`

## Existing `llm_wiki` support checked

- `/code/blogs/llm_wiki/logs/p4-40-2025-11-10-ems-electronics-rf-tools-official-source-recovery-scout.md`
- `/code/blogs/llm_wiki/logs/p4-44-source-backed-integration.md`
- `/code/blogs/llm_wiki/wiki/processes/power-energy-pcb-pcba-review-boundaries.md`
- `/code/blogs/llm_wiki/facts/methods/power-energy-inverter-charger-rewrite-boundary.md`
- `/code/blogs/llm_wiki/sources/registry/methods/keysight-power-integrity-analysis-page.md`
- `/code/blogs/llm_wiki/logs/backlog.md`
- `/code/blogs/llm_wiki/logs/phase-status.md`

# Existing `llm_wiki` Support Found

- `logs/p4-40-2025-11-10-ems-electronics-rf-tools-official-source-recovery-scout.md`
  - already classifies both `ohms-law.md` and `watts‑to‐amps.md` as `blocked_pending_official_source`.
- `logs/p4-44-source-backed-integration.md`
  - upgraded other November 2025 lanes, but left formulas and general electronics education blocked.
- `wiki/processes/power-energy-pcb-pcba-review-boundaries.md`
  - supports guarded board-level review language around power distribution, validation, connectors, harness handoff, and thermal-platform choice.
- `facts/methods/power-energy-inverter-charger-rewrite-boundary.md`
  - supports rewrite-boundary handling for power-energy board context only.
- `sources/registry/methods/keysight-power-integrity-analysis-page.md`
  - supports adjacent validation context, not formula teaching.
- `logs/backlog.md` and `logs/phase-status.md`
  - still place `2025.11.10` formulas / general electronics education in the blocked bucket after `P4-44` and `P4-53`.

## Coverage conclusion

- There is still no direct `llm_wiki` fact card, wiki page, or source pack for Ohm's law or watts-to-amps pedagogy.
- Existing support is `adjacent_context_only`, not formula authority.
- The repo can safely support power-review, validation, and board-partitioning context, but it cannot yet support formula teaching, worked examples, historical claims, or draft-originated PCB consequence claims.

# Recurring Claim Shapes In The Drafts

## Shared lane claims

- formula identity taught as authority without institutional or primary sources
- worked examples, calculator tables, and pedagogical derivations
- transitions from basic formulas into PCB manufacturability or standards-backed consequence claims

## `ohms-law.md` claim shapes

- historical-origin claims such as publication date and inventor framing
- water-flow analogy presented as authoritative instruction
- derivation and equation expansion around voltage, current, and resistance
- ohmic vs non-ohmic taxonomy and device examples
- I-V curve interpretation and slope claims
- power-law expansion such as `P = VI`, `P = I^2R`, and `P = V^2/R`
- AC extension to impedance / reactance and `V = IZ`

## `watts‑to‐amps.md` claim shapes

- DC, AC, and three-phase conversion formulas as reusable authority
- power-factor teaching
- example tables and calculator framing
- trace-width, copper-weight, connector-rating, thermal, and manufacturability consequences stated as standards-backed
- `IPC-2221` invocation without a dedicated current-carrying source lane

# Safe Reuse Classes

- blocked-status mention that `ohms-law.md` and `watts‑to‐amps.md` remain formula-pedagogy residuals in the `2025.11.10` batch
- adjacent board-review context around power distribution, validation, and connector / harness handoff
- deletion-safe preservation of where formula pedagogy and PCB current / thermal claims are currently mixed together

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
- no direct `llm_wiki` fact layer yet for Ohm's law or watts-to-amps instruction
- no dedicated source lane yet for current-carrying, trace-planning, or thermal consequences that the drafts attach to formula sections

# Strongest Next Recovery Lane

- lane: `institutional electrical fundamentals formula recovery`
- status target: `source_backed_fact_layer_partial`
- best recovery sequence:
  1. `NIST` SI / unit-identity sources for volt, ampere, ohm, and watt
  2. one strong institutional teaching source for Ohm's law and power relations, such as `DOE` or a university EE / physics page
  3. if `watts‑to‐amps.md` must keep PCB consequence language, add a separate standards or institution lane for current-carrying and trace-planning context
- expected unlock:
  a narrow formula identity and unit-pedagogy boundary
- still not unlocked even after that lane:
  board-current, trace-width, copper-weight, and thermal consequence claims unless a separate evidence lane is added

# Completion Status

- lane status: `completed_at_claim_family_level`
- existing support found: `adjacent_context_only`
- residual claim class: `blocked_pending_official_source`
- publishing posture today:
  keep formula pedagogy in scout-only state until institution-source recovery lands and PCB consequences are split into a separate lane
