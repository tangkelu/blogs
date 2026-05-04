---
fact_id: "applications-compute-infrastructure-coverage-gap-map"
title: "Compute Infrastructure application coverage gap map: which board families and review lanes have wiki-level routing and which remain overview-only"
topic: "Compute infrastructure PCB/PCBA application coverage"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-182 initial build; sourced from wiki/applications/compute-infrastructure-pcb-review-boundaries.md (active as of P4-175), related compute/high-speed fact cards in facts/methods/"
source_ids:
  - "frontendapt-industry-server-data-center-page-en"
  - "frontendapt-pcb-high-speed-pcb-page-en"
  - "frontendapt-backplane-pcb-page-en"
  - "frontendapt-materials-controlled-impedance-stackups-page-en"
  - "pcisig-pcie-5-faq"
  - "pcisig-pcie-6-faq"
  - "micron-ddr5-sdram-page"
  - "ethernet-alliance-112g-pam4"
tags: ["compute-infrastructure", "cloud", "edge", "hpc", "supercomputing", "quantum-computing", "high-speed", "backplane", "coverage-map", "gap-map"]
---

# Canonical Summary

> As of 2026-05-03 after P4-182 initial build, the compute infrastructure application family has a dedicated wiki boundary page (`wiki/applications/compute-infrastructure-pcb-review-boundaries.md`) and that page is now `active`. This fact card maps what the current internal and public source layer supports, which execution lanes are addressable, and which performance/compliance layers remain blocked.

## Board Family Coverage State

### Supported at Scenario + Board-Class Level

All entries below are supported by the Tier-2 internal source (`frontendapt-industry-server-data-center-page-en`) plus public interface-identity sources. They support board-class and execution-context vocabulary only. They do NOT prove interface performance, cooling efficacy, deployment scale, or quantum-system outcomes.

| Board Family | Application Context | PCB/PCBA Vocabulary Supported |
|---|---|---|
| **Server Motherboard / NIC** | Cloud server, rack server, blade server; uptime-sensitive hardware | High-speed interface context (PCIe, DDR5, Ethernet), controlled-impedance stackup review, power-path review, connector-integration planning |
| **Storage Backplane** | Storage array, JBOD, NVMe backplane; connector-dense boards | Press-fit connector review, backplane stackup and impedance discipline, power-distribution review, validation-structure planning |
| **Switch/Router Board** | Datacenter fabric, ToR/leaf/spine switch boards | High-density routing, interface pressure (112G/400G/800G), power-path review, backplane or cable-head transitions |
| **Edge Compute Board** | Industrial PC, embedded compute, field-deployed node | Environmental exposure framing, power/thermal review, staged launch control, service-access preservation |
| **HPC / Supercomputing Board** | Compute blade, interconnect board, accelerator card | Connector-dense layout, backplane integration, high-layer count review, validation-stage separation |
| **Parallel Compute / Accelerator** | GPU boards, FPGA cards, DPU accelerators | Memory-interface pressure (DDR5, HBM context), power-path review, first-build governance |
| **Quantum Control Electronics** | Control boards for qubit systems: timing distribution, readout interface, signal-path | Board-level signal-integrity planning, controlled-impedance review, staged validation posture |
| **Liquid-Cooled Board** | Server boards with cold-plate or direct-liquid cooling integration | Thermal-platform selection review, thermal-mechanical integration vocabulary — NOT cooling efficacy proof |

### Review Lanes Supported

| Review Lane | Safe Vocabulary |
|---|---|
| Cloud / Cluster / Distributed / Grid / Fog | Uptime-sensitive board review framing, interconnect-density pressure, power-path discipline, staged production gates |
| Edge Computing / Field-Deployed | Environmental exposure review, power/thermal review, staged launch control |
| HPC / Parallel / Supercomputing | Interface pressure, backplane discipline, power/current path, validation-separation framing |
| Quantum Control Electronics | Control/timing/readout context, signal-integrity planning, staged validation posture |

### Fact Cards Supported

| Fact Card | What It Supports |
|---|---|
| `methods-ai-server-optical-high-speed-empty-image-boundary` | AI server, optical module, high-speed empty-image boundary |
| `methods-high-speed-interface-system-context` | PCIe/DDR5/Ethernet/CXL interface naming as system-context pressure |
| `methods-controlled-impedance-tdr-verification-posture` | Controlled impedance, TDR/VNA verification posture |
| `methods-press-fit-and-backplane-integration-posture` | Press-fit connector and backplane integration posture |
| `methods-pcba-dfm-dft-dfa-review-gate-positioning` | DFM/DFT/DFA review gate positioning |
| `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary` | FAI vs high-speed signal-path validation boundary |
| `methods-pcba-npi-to-mass-production-gates` | NPI-to-mass-production gate separation |
| `methods-current-carrying-trace-width-and-copper-boundary` | High-current trace, copper weight, and power-path thermal boundary |
| `methods-thermal-pcb-platform-selection-posture` | Thermal platform selection posture (heavy copper, MCPCB, etc.) |

### Standards Context Supported (Public Sources)

| Standard/Technology | What It Supports |
|---|---|
| `PCIe Gen 5 / PCIe Gen 6` | Interface naming as system-context pressure only; NOT exact lane counts, throughput, board-capability proof |
| `DDR5 SDRAM` | Memory interface naming as design-pressure vocabulary; NOT performance claims, timing, signal-integrity proof |
| `112G PAM4 Ethernet` | High-speed interconnect naming as stackup-pressure vocabulary; NOT speed proof, link budget, optical/copper performance |
| `CXL / NVLink` | Interconnect protocol naming as architecture context only; NOT compliance, interoperability proof |
| `Liquid Cooling` | Cooling method vocabulary at review-posture level only; NOT cooling efficacy, thermal outcome guarantees |
| `Quantum Control` | Control-electronics / timing / readout-interface context; NOT qubit fidelity, cryogenic performance, microwave purity |

## Stable Facts

- The internal source (`frontendapt-industry-server-data-center-page-en`) supports 8 distinct compute infrastructure board families at scenario and board-class level.
- The source supports execution-context vocabulary, not performance proof or standards-compliance claims.
- PCIe, DDR5, and 112G vocabulary is safely supported as system-context pressure (demand context), not as board fabrication or assembly capability proof.
- Liquid cooling and thermal platform vocabulary is supported at selection-posture level only; no cooling-outcome proof.
- Quantum control electronics vocabulary is limited to board-role context; qubit or cryogenic performance is not supported.
- Deployment-scale vocabulary ("5,000-board", "decade-long lifecycle") is blocked without dated capability records.

## Conditions And Methods

- Use this card to confirm what vocabulary is safe before writing a compute infrastructure PCB/PCBA article.
- For high-speed interface system context, route to `facts/methods/high-speed-interface-system-context`.
- For backplane and press-fit vocabulary, route to `facts/methods/press-fit-and-backplane-integration-posture`.
- For TDR/VNA controlled impedance vocabulary, route to `facts/methods/controlled-impedance-tdr-verification-posture`.
- For thermal platform selection vocabulary, route to `facts/methods/thermal-pcb-platform-selection-posture`.
- Update `last_reconciled_at` when a new compute-infrastructure wiki boundary page is created.

## Limits And Non-Claims

- Exact interface speed, transfer rate, lane count, or throughput claims are NOT supported.
- Cooling efficacy, thermal-rise outcome, or "solves thermal problem" claims are NOT supported.
- Quantum fidelity, cryogenic performance, microwave purity, or qubit-system outcomes are NOT supported.
- Named program, customer, lab, defense, or infrastructure deployment claims are NOT supported.
- Deployment scale, production continuity, or field-life guarantees are NOT supported.
- Yield, throughput, cost, or lead-time claims are NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|---|---|
| Dedicated compute infrastructure wiki boundary page | Closed — created and promoted to `active` in P4-175 |
| Companion fact card (this file) | Closed — created in P4-182 |
| PCIe Gen 5/6 exact electrical specification depth | PCI-SIG member specification pages with stable public access |
| DDR5 exact timing / topology vocabulary | JEDEC official DDR5 standard page recovery |
| 112G / 400G / 800G Ethernet signal-integrity depth | IEEE 802.3 / Ethernet Alliance official published pages |
| CXL / NVLink interoperability vocabulary | CXL Consortium / NVIDIA official public specification pages |
| Liquid cooling / cold-plate vocabulary depth | Official thermal architecture standard or vendor design guide |
| Quantum control electronics PCB vocabulary | Manufacturer-controlled cryogenic-electronics board design guide |
