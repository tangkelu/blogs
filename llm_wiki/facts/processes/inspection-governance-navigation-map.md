---
fact_id: "processes-inspection-governance-navigation-map"
title: "Inspection-governance navigation map: single entry point linking all PCBA inspection, testing, screening, qualification, and traceability fact cards"
topic: "PCBA inspection and testing governance navigation"
category: "processes"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-164 initial build; closes the final remaining gap in the process-governance-gap-map — a single navigation frame tying all inspection/testing/screening/release fact cards together."
source_ids:
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-spi-inspection-page-en"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "frontendapt-pcba-incoming-quality-control-page-en"
tags: ["pcba", "inspection", "testing", "governance", "spi", "aoi", "x-ray", "ict", "fct", "flying-probe", "screening", "qualification", "fai", "traceability", "navigation-map"]
---

# Canonical Summary

> The PCBA inspection-governance knowledge base is distributed across multiple fact cards. This map provides a single navigation entry point and summarizes which card governs which governance question, what is safe to write, and what is blocked at every layer. Use this fact card to find the right card before writing any inspection-related content.

## Navigation Index: Which Fact Card to Consult

| Governance Question | Fact Card to Consult | Wiki Page |
|---|---|---|
| "What is the gate sequence and who owns each defect class?" | `methods-pcba-inspection-process-governance-boundary` | `wiki/processes/inspection-governance-navigation-map.md` ✅ |
| "How do SPI/AOI/X-ray/ICT/FCT relate to NPI vs. mass production?" | `methods-pcba-inspection-process-governance-boundary` | `wiki/processes/pcba-npi-to-mass-production-flow.md` |
| "When should X-ray be used vs. not?" | `methods-hidden-joint-xray-inspection-boundary` | `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md` |
| "How is flying probe different from ICT?" | `methods-pcba-flying-probe-vs-ict-selection-posture` | `wiki/processes/inspection-governance-navigation-map.md` ✅ |
| "How do ICT vs. flying probe vs. boundary-scan compare?" | `pcba-electrical-testing-methods-comparison` (fact card) | `wiki/processes/inspection-governance-navigation-map.md` ✅ |
| "What is screening vs. qualification vs. FAI?" | `methods-pcba-screening-qualification-governance-boundary` | `wiki/processes/inspection-governance-navigation-map.md` ✅ |
| "What is the IQC → production → final-release evidence chain?" | `methods-pcba-release-traceability-governance-boundary` | `wiki/processes/inspection-governance-navigation-map.md` ✅ |
| "What DFM/DFT changes enable better test coverage?" | `methods-pcba-dfm-dft-dfa-review-gate-positioning` | `wiki/processes/pcba-npi-to-mass-production-flow.md` |
| "What is FAI scope and what it does NOT prove?" | `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary` | `wiki/processes/inspection-governance-navigation-map.md` ✅ |
| "What is the BGA void / hidden-joint governance?" | `methods-low-void-bga-conservative-generation-gate` | `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md` |
| "What can be written about burn-in and environmental screening?" | `methods-pcba-screening-qualification-governance-boundary` | `wiki/processes/inspection-governance-navigation-map.md` ✅ |

## Gate Sequence Summary (Stable)

| Gate | Position | Defect-Class Ownership | Required? |
|------|----------|----------------------|-----------|
| **SPI** | After printing, before placement | Solder paste volume/offset/bridging/missing | When SMT; 100% automatic |
| **Pre-reflow AOI** | After placement, before reflow | Component presence/orientation/polarity/position | Per project config |
| **Post-reflow AOI** | After reflow | Solder joint geometry, bridging, tombstone, shift | Per project config |
| **X-ray / AXI** | After reflow, on hidden-joint packages | BGA/QFN/CSP voids, hidden bridges, cold joints | When BGA/LGA/QFN present |
| **ICT (bed-of-nails)** | After assembly | Opens, shorts, component value, boundary-scan | When test point design supports it |
| **Flying Probe** | After assembly (no fixture) | Opens, shorts, component value; lower coverage | NPI, small volume, no ICT fixture |
| **FCT** | Final, powered | Powered behavior, protocols, firmware, load | Per customer test spec |
| **FAI** | First production build | Dimensional, BOM, workmanship, first-article vs. drawing | First build or design change |
| **Burn-in / ESS** | After assembly (screening) | Infant-mortality failures under temp/electrical stress | High-reliability per program requirement |
| **Final Inspection + Traceability** | Shipment authorization | Label, workmanship, packing; CoC, lot-to-serial linkage | All shipments |

## Three-Layer Governance Separation

| Layer | What It Is | What It Is NOT |
|-------|-----------|---------------|
| **Screening (ESS)** | Production-lot burn-in/thermal-cycle to precipitate latent defects | Qualification proof; FAI; certification evidence |
| **Qualification** | Program-level test to prove design/process meets reliability targets | Screening; FAI; PCB-supplier certification |
| **FAI (First Article Inspection)** | First-build verification against design documentation | Reliability qualification; ongoing production audit; certification |

## Safe Vocabulary at This Layer

- Gate identity and defect-class ownership vocabulary (SPI, AOI, X-ray, ICT, FCT, flying probe, FAI, burn-in)
- Sequencing and evidence-accumulation vocabulary (cumulative evidence chain, gated ramp)
- IQC → production traceability → final release chain description
- Three-layer separation vocabulary (screening / qualification / FAI)
- Flying probe vs. ICT selection posture (project stage, volume, test-point access)

## Blocked Claims

- Yield, DPPM, throughput, or coverage percentage numerics
- Process window, solder-joint acceptance threshold, or X-ray void-limit numerics
- Certification pass-status (IPC Class 3, AS9100, ISO 9001)
- Customer approval, program qualification, or FAI pass-status claims
- Universal gate-completeness claims ("every board receives every gate")
- Supplier qualification, airworthiness, or medical device registration

## Conditions And Methods

- Use this card as the entry point when an agent needs to write about PCBA inspection, testing, or quality governance
- Do NOT start from individual gate fact cards before checking this navigation map first
- The wiki page `wiki/processes/inspection-governance-navigation-map.md` is the prompt-consumable companion to this fact card

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/spi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/incoming-quality-control.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
