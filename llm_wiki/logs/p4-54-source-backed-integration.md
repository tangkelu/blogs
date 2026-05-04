# P4-54 Source-Backed Integration

Date: 2026-04-29

## Purpose

Convert the next narrow residual authority lane into reusable `llm_wiki` data by upgrading `4-layer-pcb-manufacturing.md` and `double-sided-pcb-manufacturer.md` only at the rigid-board family identity level.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote draft-originated stackup recipes, design-rule numerics, impedance or EMI outcomes, material prescriptions, manufacturer-selection advice, lead-time promises, MOQ claims, quality claims, or supplier rankings.

## Inputs Reviewed

- `logs/p4-40-2025-11-17-ceramic-power-basics-official-source-recovery-scout.md`
- `/code/blogs/tmps/2025.11.17/en/4-layer-pcb-manufacturing.md`
- `/code/blogs/tmps/2025.11.17/en/double-sided-pcb-manufacturer.md`
- existing public rigid-board standards metadata and internal baseline-versus-multilayer process layers already present in `llm_wiki`

## Parallel Work Pattern

- Main agent owned final scope decisions, integration, and tracker updates.
- Existing low-risk scout output was reused to keep this lane at architecture and family-identity level only.
- No new subagent was needed because the local corpus already had the exact narrow support set.

## Source Records Reused

No new source-record files were required in this pass.

This integration reuses the strongest existing source layers already in `llm_wiki`:

- `ipc-6012f-toc` for public rigid-board family identity
- `mil-prf-55110-general-spec-page` for legacy rigid single-sided / double-sided / multilayer scope wording
- internal HIL single/double-layer and multilayer records for baseline-versus-multilayer manufacturing split
- internal APT multilayer record for multilayer complexity framing

## Fact Card Added

- `facts/standards/rigid-board-family-identity-boundary.md`

This fact card upgrades the `4-layer` / `double-sided` family from scout-only into a conservative source-backed family boundary.

What is now source-backed:

- double-sided boards as part of the baseline rigid-board branch
- 4-layer rigid boards as part of the multilayer rigid-board branch
- the boundary that multilayer identity is not the same thing as advanced-feature or supplier-superiority proof

## Topic Wiki Added

- `wiki/processes/rigid-board-family-and-layer-boundaries.md`

This page makes the new boundary prompt-consumable for:

- `/code/blogs/tmps/2025.11.17/en/4-layer-pcb-manufacturing.md`
- `/code/blogs/tmps/2025.11.17/en/double-sided-pcb-manufacturer.md`

## What This Unlocks

- `4-layer-pcb-manufacturing.md` can now be conservatively rewritten as a multilayer rigid-board family article:
  - 4-layer belongs to the multilayer rigid-board branch
  - stackup and registration complexity increase relative to the low-layer baseline
  - advanced features remain conditional rather than assumed
- `double-sided-pcb-manufacturer.md` can now route through a baseline rigid-board family layer:
  - double-sided belongs to the lower-complexity rigid-board branch
  - plated-through-hole interconnection and routing flexibility are legitimate family-level distinctions
  - manufacturer-selection claims remain blocked

## Still Blocked

- default 4-layer stackups, plane assignments, impedance geometries, and EMI / PI / SI outcome claims
- manufacturer-selection advice, supplier rankings, `best manufacturer` wording, or current commercial recommendations
- current capability tables, lead times, MOQ, yield, quality-rate, certification, and delivery claims
- broad statements that every 4-layer board needs HDI, backdrill, low-loss material, or special lamination
- broad statements that double-sided boards are always low-end or always sufficient

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family: `2025.11.17` `4-layer-pcb-manufacturing` and `double-sided-pcb-manufacturer` family-identity lane
- next likely residual lane:
  - `microstrip / stripline / CPW` structure vocabulary
  - another electronics-basics or RF-structure evidence-dense residual lane
