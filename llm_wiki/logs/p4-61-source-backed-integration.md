# P4-61 Source-Backed Integration

Date: 2026-04-30

## Purpose

Controller-integrate the next conditional lane after `P4-60`: the PCB consequence claims still attached to `watts‑to‐amps.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote generic trace-width tables, exact copper-ounce choices, connector-rating rules, simulation proof, testing proof, or `IPC-2221` shorthand as reusable design authority.

## Inputs Reviewed

- `logs/p4-61a-2025-11-10-watts-to-amps-pcb-consequence-split.md`
- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`
- `/code/blogs/tmps/2025.11.10/en/ohms-law.md`
- existing local support:
  - `facts/methods/electrical-formula-identity-boundary.md`
  - `facts/methods/thermal-pcb-platform-selection-posture.md`
  - `facts/methods/power-energy-inverter-charger-rewrite-boundary.md`
  - `wiki/processes/power-energy-pcb-pcba-review-boundaries.md`
- external primary sources rechecked by the main agent:
  - IPC `IPC-2152` public TOC PDF
  - Analog Devices `AN-136`
  - Analog Devices `Layout Considerations for High-Power Circuits`

## Parallel Work Pattern

- Main agent owned scope decisions, primary-source verification, final source / fact / wiki writing, and tracker updates.
- One bounded `gpt-5.4-mini` worker produced `logs/p4-61a-2025-11-10-watts-to-amps-pcb-consequence-split.md` and confirmed that the only meaningful surviving PCB consequence lane is the narrow `trace_width_and_copper_weight` style sublane.
- A second bounded `gpt-5.4-mini` local-coverage check was launched for redundancy, but the main agent completed the coverage judgment directly rather than waiting for it to block source recovery.

## Integrated Source-Backed Lane

### Current-Carrying And High-Current Layout Boundary

Added official and public source records:

- `ipc-2152-current-carrying-capacity-toc`
- `analog-devices-an136-pcb-layout-nonisold-switching-supplies`
- `analog-devices-layout-considerations-for-high-power-circuits`

Added fact card:

- `methods-current-carrying-trace-width-and-copper-boundary`

Added topic wiki:

- `processes-current-carrying-and-high-current-layout-boundaries`

Supported draft family:

- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`

What is now source-backed:

- the split between formula identity and board-design consequence
- the idea that current-carrying capacity in printed-board design is a separate conductor-sizing problem
- guarded current-path consequences around trace width, copper weight or thickness, planes, vias, and high-current path geometry
- guarded layout consequences around conduction loss, voltage drop, and thermal stress when current paths are undersized
- heavy copper and other thermal board routes as project-dependent options, not default rules

Still blocked:

- generic trace-width charts, per-amp formulas, and exact copper-ounce recommendations
- `IPC-2221` shorthand as standalone authority
- connector and component current-rating claims
- simulation, prototyping, validation, DFM, DFT, or manufacturability outcome claims
- product-specific current, temperature-rise, and reliability outcomes

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2025.11.10` `watts‑to‐amps.md` at current-carrying and high-current-layout boundary level only
- unaffected formula lane:
  - `2025.11.10` `ohms-law.md` remains formula-identity only and does not join this PCB consequence lane
- next likely residual lanes:
  - connector-rating authority only if a future rewrite keeps named connector or component current claims
  - simulation / testing authority only if a future rewrite keeps those verification claims
