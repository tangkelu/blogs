# P4-51 Source-Backed Integration

Date: 2026-04-29

## Purpose

Convert the remaining `P4-48C` residual lane into reusable `llm_wiki` data by adding a conservative `BOM / HDI / cost-reduction` complexity boundary.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote draft-originated prices, savings percentages, panelization outcomes, sourcing leverage, lead-time compression, yield / FPY, supplier optimization, competitiveness, or case-study results.

## Inputs Reviewed

- `logs/p4-48c-hdi-bom-cost-driver-evidence-scout.md`
- `logs/p4-50-source-backed-integration.md`
- `/code/blogs/tmps/2025.11.17/en/bom-cost.md`
- `/code/blogs/tmps/2025.11.27/en/hdi-pcb-cost.md`
- `/code/blogs/tmps/2025.11.27/en/pcb-cost-reduction.md`
- existing BOM sourcing, traceability, HDI, microvia-reliability, finish-taxonomy, and hi-rel metadata layers already present in `llm_wiki`

## Parallel Work Pattern

- Main agent owned scope decisions, integration, and tracker updates.
- One `mini` bounded explorer re-checked the smallest safe claim set and confirmed the lane can only be upgraded at complexity-boundary level.
- One stronger bounded explorer re-checked file-pattern shape and confirmed `P4-51` should follow the same `1 log + 1 fact + 1 wiki` integration form unless new official source records were strictly necessary.
- Explorer conclusions aligned with main-agent review:
  - `bom-cost.md` can now use BOM structure, sourcing-governance, and cost-input composition language only
  - `hdi-pcb-cost.md` can now use HDI build-up and sequential-lamination complexity language only
  - `pcb-cost-reduction.md` can now use guarded planning heuristics only, not optimization outcomes

## Source Records Reused

No new source-record files were required in this pass.

This integration reuses the strongest existing source layers already in `llm_wiki`:

- internal BOM sourcing, turnkey assembly, and quality-system records
- internal HDI and advanced-manufacturing records
- official Isola sequential-lamination process note
- official IPC finish-taxonomy metadata
- official IPC / SAE traceability and counterfeit-control metadata

## Fact Card Added

- `facts/methods/bom-and-hdi-complexity-boundary.md`

This fact card upgrades the `bom-cost` / `hdi-pcb-cost` / `pcb-cost-reduction` family from scout-only into a conservative source-backed complexity boundary.

What is now source-backed:

- BOM as a structured manufacturing input rather than a price-only list
- sourcing / lifecycle / authenticity / traceability posture as part of BOM governance
- HDI as a separate build-up interconnect family involving microvias, sequential build-up, and extra engineering review burden
- finish families named through corrected public taxonomy rather than cost ranking
- guarded planning language such as reviewing stack-up early, avoiding over-specification, and separating PCB / assembly / sourcing / test decisions

## Topic Wiki Added

- `wiki/processes/bom-and-hdi-complexity-boundaries.md`

This page makes the new boundary prompt-consumable for:

- `/code/blogs/tmps/2025.11.17/en/bom-cost.md`
- `/code/blogs/tmps/2025.11.27/en/hdi-pcb-cost.md`
- `/code/blogs/tmps/2025.11.27/en/pcb-cost-reduction.md`

## What This Unlocks

- `bom-cost.md` can now be conservatively rewritten as a planning-and-governance article:
  - BOM structure
  - sourcing / lifecycle / traceability review
  - component / bare-board / assembly / tooling as separate cost-input layers
- `hdi-pcb-cost.md` can now route through a conservative HDI complexity layer:
  - microvia and build-up identity
  - sequential-lamination and stress-factor context
  - finish and inspection context without cost ranking
- `pcb-cost-reduction.md` can now route through guarded planning heuristics:
  - avoid unnecessary complexity
  - align technology choice with real need
  - separate sourcing, fabrication, assembly, and release planning

## Still Blocked

- current prices, current quotes, component market dynamics, and margin / ROI conclusions
- panelization savings, CAM optimization outcomes, sourcing leverage, or alternate-material savings claims
- finish-cost ordering such as `HASL cheapest` or `ENIG more expensive` as a universal public rule
- lead-time, MOQ, availability, stock, or supply-chain-power claims
- supplier-specific optimization stories, global-supply-chain leverage, or broad material-database advantage claims
- yield, FPY, scrap, rework, stable mass production, and quality-rate claims
- case-study percentages such as `22%` reduction and similar launch / competitiveness outcomes

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family: `2025.11.17` and `2025.11.27` BOM / HDI / cost-reduction lane
- next likely residual lane:
  - dated internal quoting or panelization evidence if public cost language must survive
  - narrower material or finish owner sources only if future rewrite scope still needs stronger use-case guidance
