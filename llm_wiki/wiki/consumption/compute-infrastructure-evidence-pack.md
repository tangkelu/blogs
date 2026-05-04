# Compute Infrastructure PCB Evidence Pack

**Pack ID**: `consumption-compute-infrastructure`
**Date**: 2026-05-02
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Compute infrastructure PCB (cloud/edge/HPC/supercomputing/quantum)"
scope: |
  Conservative evidence pack for compute-infrastructure PCB content.
  
  Supports system-context pressure discussion, stackup and interconnect planning,
  power-path review, thermal-platform choice, assembly/validation gates.
  
  No performance, cooling efficacy, or program-lifecycle guarantees.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Application boundary
  - "applications-compute-infrastructure-pcb-review-boundaries"
  
  # High-speed/interface
  - "methods-high-speed-interface-system-context"
  - "methods-controlled-impedance-tdr-verification-posture"
  - "methods-press-fit-and-backplane-integration-posture"
  
  # Power/thermal
  - "methods-current-carrying-trace-width-and-copper-boundary"
  - "methods-thermal-pcb-platform-selection-posture"
  
  # Validation
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"
  - "methods-pcba-npi-to-mass-production-gates"
  
  # Interface identity
  - "interfaces-high-speed-pcb-interface-requirements-and-design-boundaries"

source_ids:
  - "frontendapt-industry-server-data-center-page-en"
  - "frontendapt-pcb-high-speed-pcb-page-en"
  - "frontendapt-backplane-pcb-page-en"
  - "frontendapt-pcb-high-thermal-pcb-page-en"
  - "frontendapt-pcb-heavy-copper-pcb-page-en"
  - "pcisig-pcie-5-faq"
  - "pcisig-pcie-6-faq"
  - "micron-ddr5-sdram-page"
  - "ethernet-alliance-112g-pam4"

wiki_framing_support:
  - "wiki/applications/compute-infrastructure-pcb-review-boundaries"
  - "wiki/interfaces/high-speed-pcb-interface-requirements-and-design-boundaries"

must_refresh:
  - claim: "Interface speed or transfer rate statements"
    value: true
  - claim: "Power, temperature, cooling figures"
    value: true
  - claim: "Production scale or lifecycle support claims"
    value: true

excluded_claim_classes:
  - "PCIe Gen6/DDR5/112G as board-capability proof"
  - "Liquid cooling solves thermal problem without architecture source"
  - "Quantum-grade signal purity, exascale readiness, AI-training reliability"
  - "5,000-board, national lab, decade-long lifecycle claims"
  - "Fanless, rugged, field-hardened, always-on as reliability evidence"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `cloud computing PCB`, `edge computing PCB`, `HPC PCB`, `data center PCB`, `AI server PCB` |
| **Page Type** | `query` |
| **Search Intent** | Compute infrastructure hardware, high-speed interconnect, thermal/power planning |
| **Target Reader** | System architects, hardware engineers, data center designers |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` for system-context pressure discussion.

---

## 3. Review Lanes

### 3.1 Cloud/Cluster/Distributed

| Aspect | Evidence Support |
|--------|------------------|
| Uptime sensitivity | Posture discussion |
| Interconnect density | Stackup planning context |
| Validation dependency | Staged production gates |

### 3.2 Edge Computing

| Aspect | Evidence Support |
|--------|------------------|
| Environmental exposure | Planning posture |
| Service access | Review consideration |
| Power/thermal discipline | Platform selection |

### 3.3 HPC/Supercomputing

| Aspect | Evidence Support |
|--------|------------------|
| Connector density | Backplane integration posture |
| Interface pressure | High-speed context vocabulary |
| Validation separation | Scope segmentation |

### 3.4 Quantum Control

| Aspect | Evidence Support |
|--------|------------------|
| Control electronics | Timing-distribution context |
| Readout interface | Signal-integrity planning |
| Staged validation | Workflow posture |

---

## 4. Allowed vs Blocked

### 4.1 Allowed (System Context)

| Claim | Example |
|-------|-----------|
| Interface context | "PCIe, DDR5, 112G increase stackup, channel, power demands" |
| Stackup pressure | "High-speed interfaces require low-loss stackup consideration" |
| Validation gates | "First-build confirmation and production-ramp gates help control risk" |
| Thermal compromise | "Edge hardware balances compute density with environmental exposure" |

### 4.2 Blocked (Performance/Deployment)

| Claim | Example |
|-------|-----------|
| Capability proof | "This board supports PCIe Gen6, DDR5, 800G networking" |
| Cooling solution | "Liquid cooling solves the thermal problem" |
| Reliability proof | "Quantum-grade signal purity" or "exascale readiness" |
| Deployment claims | "5,000-board national lab deployment" |

---

## 5. Interface Vocabulary (Context Only)

| Interface | Context Use | Blocked Use |
|-----------|-------------|---------------|
| PCIe Gen5/6 | Ecosystem pressure | Fabrication capability proof |
| DDR5 | Memory interface demand | Board performance guarantee |
| 112G | High-speed channel stress | Loss budget numerics |
| 400G Ethernet | Backplane interconnect | Channel compliance proof |

---

## 6. Handoff

**Core Answer**:

> Compute-infrastructure PCBs stress board design through system-context pressure: high-speed interface density, power delivery complexity, thermal constraints, and validation requirements. Current evidence supports stackup/interconnect planning and validation-gate discussion, not interface-performance proof, cooling efficacy, or deployment-scale claims.

**Safe Reusable Shapes**:

- "Compute infrastructure boards become harder at the review layer before they become harder at the marketing layer."
- "Named interface families are safer to use as system-context pressure than as board-capability proof."

---

## 7. Pre-flight

- [x] Compute boundary wiki referenced
- [x] High-speed interface fact cards mapped
- [x] Blocked performance claims documented

**Verdict**: ✅ `go_now_conservative` for system-context pressure discussion.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
