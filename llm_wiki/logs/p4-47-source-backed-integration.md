# P4-47 Source-Backed Integration

Date: 2026-04-29

## Purpose

Convert the strongest remaining `2025.11.17` `IGBT vs MOSFET` blocker into reusable `llm_wiki` data by adding official manufacturer source records, one methods boundary fact card, and one topic wiki page for power-device identity and packaging boundaries.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote draft-originated voltage, current, power, switching-frequency, efficiency, EMI, thermal, gate-drive, safe-operating-area, or replacement-rule claims.

## Inputs Reviewed

- `logs/p4-46-source-backed-integration.md`
- `logs/p4-40-2025-11-17-ceramic-power-basics-official-source-recovery-scout.md`
- `/code/blogs/tmps/2025.11.17/en/igbt-vs-mosfet.md`
- existing power / inverter boundary files already present in `llm_wiki`

## Source Records Added

- `sources/registry/methods/st-power-mosfets-page.md`
- `sources/registry/methods/infineon-igbt-discretes-page.md`
- `sources/registry/methods/infineon-bjt-mosfet-igbt-difference-page.md`

These official records add:

- MOSFET terminal and body-diode vocabulary from an official manufacturer page
- IGBT terminal vocabulary and anti-parallel-diode packaging boundary from an official manufacturer page
- high-level manufacturer-owned comparison language for MOSFET versus IGBT device classes

## Fact Card Added

- `facts/methods/igbt-vs-mosfet-device-identity-boundary.md`

This fact card upgrades the `igbt-vs-mosfet` family from `blocked_pending_official_source` to a conservative source-backed boundary layer.

What is now source-backed:

- MOSFET versus IGBT device-class identity
- terminal naming: `gate / drain / source` versus `gate / collector / emitter`
- MOSFET `RDS(on)` and body-diode vocabulary at high level
- IGBT anti-parallel-diode packaging boundary at high level
- broad application-family context only

## Topic Wiki Added

- `wiki/processes/igbt-and-mosfet-device-boundaries.md`

This page makes the new boundary prompt-consumable for:

- `/code/blogs/tmps/2025.11.17/en/igbt-vs-mosfet.md`

## What This Unlocks

- `igbt-vs-mosfet.md` can now be conservatively rewritten as a device-identity and packaging-boundary article:
  - device-class distinction
  - terminal vocabulary
  - body-diode versus anti-parallel-diode boundary
  - caution that exact substitution and performance depend on the exact part and circuit

## Still Blocked

- universal or current voltage / current / power / switching-frequency windows
- efficiency, switching-loss, conduction-loss, turn-off-tail, SOA, short-circuit, and thermal-performance claims
- direct selection rules, replacement rules, and topology-agnostic recommendations
- claims that one device is always faster, better, cheaper, or more reliable
- current product-lineup, market, or cost-comparison language without dated narrower sources

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family: `2025.11.17` `IGBT vs MOSFET` device-boundary lane
- next likely residual lanes:
  - remote-control protocol authority
  - RF cable / schematic-symbol / electronics-basics authority
  - HDI / BOM / PCB cost-driver evidence
  - dated APT / HIL capability records
