---
fact_id: "processes-process-governance-gap-map"
title: "Process governance coverage map: which PCB/PCBA process domains have wiki-layer aggregation and which remain at boundary-card or fact-only level"
topic: "Process governance coverage and gap mapping"
category: "processes"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-152 (HIL assembly) and P4-153 (HIL PCB board-type) wiki aggregation completed; updated in P4-154 and reconciled again after P4-164 inspection-governance navigation landing"
source_ids:
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-spi-inspection-page-en"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-npi-assembly-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "frontendapt-pcba-incoming-quality-control-page-en"
  - "frontendhil-fr4-pcb-product-en"
  - "frontendhil-high-tg-pcb-product-en"
  - "frontendhil-heavy-copper-pcb-product-en"
  - "frontendhil-halogen-free-pcb-product-en"
  - "frontendhil-high-speed-pcb-product-en"
  - "frontendhil-high-thermal-pcb-product-en"
  - "frontendhil-ic-substrate-pcb-product-en"
  - "frontendhil-backplane-pcb-product-en"
  - "frontendhil-high-frequency-pcb-product-en"
  - "frontendhil-teflon-pcb-product-en"
  - "frontendhil-rogers-pcb-product-en"
  - "frontendhil-multilayer-pcb-product-en"
  - "frontendhil-single-double-layer-pcb-product-en"
  - "frontendhil-hdi-pcb-product-en"
  - "frontendhil-rigid-flex-pcb-product-en"
  - "frontendhil-flex-pcb-product-en"
  - "frontendhil-smt-assembly-product-en"
  - "frontendhil-through-hole-assembly-product-en"
  - "frontendhil-small-batch-assembly-product-en"
  - "frontendhil-large-volume-assembly-product-en"
  - "frontendhil-turnkey-assembly-product-en"
  - "frontendhil-box-build-assembly-product-en"
tags: ["governance", "gap-map", "pcba", "pcb", "processes", "wiki-coverage", "fact-coverage", "hil", "apt"]
---

# Canonical Summary

> As of 2026-05-03 (post P4-164 reconciliation), the process knowledge base has full wiki-layer aggregation for: APT PCBA governance, APT PCB capability families, HIL PCB product-family capability map (16 families, P4-153), HIL assembly capability map (6 assembly types, P4-152), and the unified inspection-governance navigation frame (P4-164). The only remaining reopen condition is any new HIL or APT capability family added after this reconciliation date.

## Coverage Map by Domain

### PCBA Governance — Wiki-Layer Complete

| Governance Domain | Fact Card | Wiki Page |
|---|---|---|
| Inspection gate sequence (SPI→AOI→X-ray→ICT→FCT) | `methods-pcba-inspection-process-governance-boundary` | `wiki/processes/inspection-governance-navigation-map.md` ✅ |
| Screening / qualification / FAI three-layer separation | `methods-pcba-screening-qualification-governance-boundary` | `wiki/processes/inspection-governance-navigation-map.md` ✅ |
| Release / traceability evidence chain | `methods-pcba-release-traceability-governance-boundary` | `wiki/processes/inspection-governance-navigation-map.md` ✅ |
| NPI to mass production gated ramp | `methods-pcba-npi-to-mass-production-gates`, `methods-pcba-evt-dvt-pvt-gated-ramp-boundary` | `wiki/processes/pcba-npi-to-mass-production-flow.md` ✅ |
| Mixed technology assembly flow | `methods-pcba-mixed-technology-assembly-flow` | `wiki/processes/mixed-technology-solder-route-selection.md` ✅ |
| Conformal coating governance | multiple methods cards | `wiki/processes/conformal-coating-application-readiness-map.md` ✅ |
| DFM/DFT/DFA review positioning | `methods-pcba-dfm-dft-dfa-review-gate-positioning` | part of NPI wiki ✅ |
| Electrical test method comparison | `methods-pcba-electrical-testing-methods-comparison` | `wiki/processes/inspection-governance-navigation-map.md` ✅ |
| Low-void BGA reflow and hidden-joint inspection | multiple methods cards | `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md` ✅ |
| Selective solder fixture and access | multiple methods cards | `wiki/processes/selective-solder-fixture-and-access-planning.md` ✅ |

### APT PCB Capability Families — Wiki-Layer Complete

| Capability Family | Fact Card | Wiki Page |
|---|---|---|
| APT capability family overview | `methods-internal-capability-family-map` | `wiki/processes/apt-capability-family-map-and-boundaries.md` ✅ |
| APT PCB manufacturing capabilities (full) | `apt-pcb-process-technologies-summary` | `wiki/processes/apt-pcb-manufacturing-capabilities.md` ✅ |
| APT assembly process overview | `apt-assembly-process-overview` | `wiki/processes/pcba-npi-to-mass-production-flow.md` (absorbed) |
| APT NPI process capabilities | `apt-npi-process-capabilities` | `wiki/processes/pcba-npi-to-mass-production-flow.md` (absorbed) |
| APT rigid PCB capability specs | `processes-apt-rigid-capability-specs` | absorbed into APT wiki pages ✅ |
| APT flex PCB capability specs | `processes-apt-flex-capability-specs` | absorbed into APT wiki pages ✅ |
| APT HDI PCB capability specs | `processes-apt-hdi-capability-specs` | absorbed into APT wiki pages ✅ |
| APT rigid-flex capability specs | `processes-apt-rigid-flex-capability-specs` | absorbed into APT wiki pages ✅ |
| APT metal-core capability specs | `processes-apt-metal-core-capability-specs` | absorbed into APT wiki pages ✅ |
| APT ceramic capability specs | `processes-apt-ceramic-capability-specs` | absorbed into APT wiki pages ✅ |

### HIL PCB Product Family — **WIKI-LAYER COMPLETE** ✅ (P4-153)

| Capability Family | Fact Card | Wiki Page |
|---|---|---|
| HIL FR-4 | `processes-hil-fr4-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL High-Tg | `processes-hil-high-tg-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL Heavy Copper | `processes-hil-heavy-copper-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL Halogen-Free | `processes-hil-halogen-free-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL High-Speed Digital | `processes-hil-high-speed-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL High-Thermal (MCPCB/Ceramic) | `processes-hil-high-thermal-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL High-Frequency RF | `processes-hil-high-frequency-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL IC Substrate | `processes-hil-ic-substrate-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL Backplane | `processes-hil-backplane-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL Teflon/PTFE PCB | `processes-hil-teflon-pcb-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL Rogers specialty | `processes-hil-rogers-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL Multilayer | `processes-hil-multilayer-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL Single/Double Layer | `processes-hil-single-double-layer-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL HDI | `processes-hil-hdi-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL Rigid-Flex | `processes-hil-rigid-flex-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |
| HIL Flex (FPC) | `processes-hil-flex-capability-specs` | `wiki/processes/hil-pcb-product-family-capability-map.md` ✅ |

**Resolved in P4-153**: `wiki/processes/hil-pcb-product-family-capability-map.md` now covers all 16 HIL PCB product families with routing, engineering boundaries, and misreadings prevention. Status upgraded from `draft` to `active`.

### Assembly Governance — **WIKI-LAYER COMPLETE** ✅ (P4-152)

| Governance Domain | Fact Card | Wiki Page |
|---|---|---|
| HIL SMT assembly | `processes-hil-smt-assembly-capability-specs` | `wiki/processes/hil-assembly-capability-map.md` ✅ |
| HIL through-hole assembly | `processes-hil-through-hole-assembly-capability-specs` | `wiki/processes/hil-assembly-capability-map.md` ✅ |
| HIL small-batch assembly | `processes-hil-small-batch-assembly-capability-specs` | `wiki/processes/hil-assembly-capability-map.md` ✅ |
| HIL large-volume assembly | `processes-hil-large-volume-assembly-capability-specs` | `wiki/processes/hil-assembly-capability-map.md` ✅ |
| HIL turnkey assembly | `processes-hil-turnkey-assembly-capability-specs` | `wiki/processes/hil-assembly-capability-map.md` ✅ |
| HIL box-build assembly | `processes-hil-box-build-assembly-capability-specs` | `wiki/processes/hil-assembly-capability-map.md` ✅ |
| HIL assembly gap map | `processes-hil-assembly-capability-gap-map` | `wiki/processes/hil-assembly-capability-map.md` ✅ |

**Resolved in P4-152**: `wiki/processes/hil-assembly-capability-map.md` now provides dedicated routing for all 6 HIL assembly types with per-type capability sections, misreadings prevention, and explicit blocked claims. Previously these were only indirectly absorbed into shared APT/HIL flow pages.

### Remaining Gaps

| Gap | Status | Reopen Condition |
|-----|--------|------------------|
| Unified inspection-governance navigation frame | Resolved in P4-164 | Reopen only if a new inspection governance domain appears that is not covered by `wiki/processes/inspection-governance-navigation-map.md` |
| New HIL/APT capability families (post-2026-05-03) | Watch only | Reopen when HIL or APT publishes a new product page not yet indexed |

## Blocked Claims (Maintained)

- Process windows, yield, DPPM, throughput claims
- Certification pass/fail status
- Supplier-proof or qualification proof
- Performance numerics not tied to published HIL/APT source records
- Lead-time commitments as universal claims

## Conditions And Methods

- Use this card to navigate which process domain has reusable wiki coverage vs. which still needs wiki aggregation
- When writing process-layer content, consult the wiki page (if present) rather than the fact card directly
- For HIL PCB product families: use `wiki/processes/hil-pcb-product-family-capability-map.md` as the primary routing frame
- For HIL assembly types: use `wiki/processes/hil-assembly-capability-map.md` as the primary routing frame
- This card was reconciled again after P4-164; update `last_reconciled_at` when a new process wiki page is created

## Source Links

- /code/blogs/llm_wiki/facts/processes/ (process fact cards; includes HIL assembly gap map added P4-152)
- /code/blogs/llm_wiki/facts/methods/ (all methods boundary cards)
- /code/blogs/llm_wiki/wiki/processes/ (wiki pages; includes inspection-governance-navigation-map.md added P4-164)
- `logs/p4-152-hil-assembly-capability-aggregation.md` — assembly lane completion record
- `logs/p4-153-hil-pcb-board-type-wiki-aggregation.md` — PCB board-type lane completion record
- `logs/p4-154-process-governance-coverage-map-reconciliation.md` — prior reconciliation lane log
- `logs/p4-164-inspection-governance-navigation-frame-consolidation.md` — inspection navigation closure lane log
