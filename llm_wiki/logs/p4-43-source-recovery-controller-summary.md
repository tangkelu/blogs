# P4-43 Source-Recovery Controller Summary

Date: 2026-04-28

Status: `source_backed_fact_layer_partial`

## Purpose

This controller pass consolidates the P4-43 `gpt-5.4` scout lanes for the remaining English blog folders currently under `/code/blogs/tmps`. It records deletion-safe coverage, existing reusable `llm_wiki` support, and blocked claim classes. It does not promote draft-originated cost, lead time, MOQ, stock, supplier capability, equipment, process-window, yield, quality-rate, RF / thermal / SI performance, stackup defaults, certification, compliance, or legal conclusions.

## Inputs Reviewed

- `logs/p4-43-2026-3-ro3003-ro3006-rogers-official-source-recovery-scout.md`
- `logs/p4-43b-2026-3-full-ro3003-ro3006-rogers-official-source-recovery-scout.md`
- `logs/p4-43-2026-4-1-two-layer-specialty-pcb-official-source-recovery-scout.md`
- `logs/p4-43-2026-4-24-layer-count-pcb-manufacturing-official-source-recovery-scout.md`

Note: `logs/p4-43-2026-3-ro3003-ro3006-rogers-official-source-recovery-scout.md` is retained as a narrow scout for `ro3003-pcb-cost.md` only. The full-directory source for `2026.3/en` is `logs/p4-43b-2026-3-full-ro3003-ro3006-rogers-official-source-recovery-scout.md`.

## Batch Results

### 2026.3 RO3003 / RO3006 / Rogers

- status: `completed_at_claim_family_level`
- existing support: `source_backed_fact_layer_partial`
- correction: the full-directory P4-43b scout inspected all `20` drafts in `/code/blogs/tmps/2026.3/en`
- safe reuse:
  - Rogers `RO3003` and `RO3006` exact-product facts from existing official-source-backed cards
  - RO3000 family and RF material selector framing
  - hybrid RF stackup as a mixed-material planning strategy
  - PTFE processing, controlled-impedance verification, RF validation ladder, and prototype / quick-turn route separation
  - PCBA assembly flow, hidden-joint inspection posture, cavity / shield / finish-zoning planning, and RF transition-control boundaries where relevant to the full 20-file set
- blocked:
  - draft-originated cost / savings percentages, material price multipliers, stock / VMI / MOQ, material lead time, panel utilization savings, quote economics, yield, consumable economics, current APT equipment, supplier qualification proof, certifications, default inspection / validation coverage, exact RF geometry, mmWave formulas, process numerics, and RF / mmWave performance-preservation claims

### 2026.4.1 Two-Layer Specialty PCB

- status: `completed_at_claim_family_level`
- existing support: `source_backed_fact_layer_partial`
- safe reuse:
  - existing `APTPCB260401` 2-layer draft-consumption boundary and ingestion-map handling
  - single / double-layer as a low-complexity product-family route
  - FR-4 and high-Tg as product-specific material families, not universal property rows
  - IMS / metal-core, ceramic, surface finishes, PTFE / Rogers / Teflon, polyimide / flex, PCBA, prototype, quick-turn, and service-routing boundaries from existing cards
- blocked:
  - universal 2-layer stackup defaults, design-rule numerics, unnamed material parameters, finish thickness / shelf life / black-pad / planarity / solderability claims, copper-core claims, RF / microwave / thermal outcomes, quick-turn promises, cost claims, supplier capability, certifications, yield, quality rate, lead time, and MOQ

### 2026.4.24 Layer-Count PCB Manufacturing

- status: `source_backed_fact_layer_partial`
- safe reuse:
  - existing layer-count generation gates, readiness logs, and high-density numeric-containment governance
  - architecture-pressure framing from `6-layer` through `24-layer`
  - high-layer registration sensitivity, HDI / microvia vocabulary, backdrill rationale, TDR / VNA validation ladder, rigid-flex branch framing, and high-layer workflow boundaries
- blocked:
  - draft-originated stackup defaults, layer-assignment recipes, impedance tolerances, skew / loss budgets, frequency ceilings, BGA escape geometry tables, microvia reliability thresholds, rigid-flex bend-life values, thermal / PDN / current-density outcomes, Class 3 / addendum acceptance thresholds, 20-layer / 22-layer supplier proof, lead time, price, MOQ, yield, quality rate, and current capability claims

## Controller Disposition

- The remaining English `tmps` blog folders in this P4-43 slice are deletion-safe at claim-family level.
- `2026.3` and `2026.4.24` have meaningful existing source-backed boundary support for conservative rewrite routing.
- `2026.4.1` is source-backed partial for surrounding material / finish / service boundaries, but the 2-layer draft family itself remains governed by the existing APTPCB260401 consumption boundary.
- No new source records, fact cards, or topic wiki pages were created in this controller pass because the scouts primarily confirmed existing reusable support and blocked gaps.

## Next Recovery Lanes

- RO3003 / RO3006: recover dated APT records only if current quick-turn, stock, quote, validation, or supplier-capability claims must be used.
- 2-layer specialty: recover copper-core official sources, deeper finish-chemistry sources, broader polyimide exact-product sources, and dated APT / HIL records for quick-turn / supplier claims.
- Layer-count: prioritize Tier 1 dated capability records for `20-layer` / `22-layer` supplier-proof claims; add narrower official-source lanes for high-speed validation authority and rigid-flex reliability boundaries if those articles must include stronger claims.

## Status

- controller summary status: `source_backed_fact_layer_partial`
- reusable data added: `no`
- deletion-safe batch coverage added: `yes`
- remaining English blog folder scout coverage: `current tmps English folders covered, excluding paused materias_pdf`
