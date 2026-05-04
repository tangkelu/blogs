# 14-Layer PCB Evidence Pack

**Pack ID**: `consumption-14-layer-pcb`
**Date**: 2026-05-02
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "14-layer PCB manufacturing"
scope: |
  Conservative evidence pack for 14-layer rigid vs rigid-flex branching.
  
  Supports rigid high-layer builds and rigid-flex variant planning with 
  explicit branch containment. No rigid-flex reliability thresholds included.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Material anchors
  - "materials-panasonic-megtron-6"
  - "materials-isola-370hr"
  - "materials-isola-fr408hr"
  - "materials-iteq-it-180a"
  - "materials-taconic-rf-35"
  
  # Method posture cards
  - "methods-high-layer-rigid-board-manufacturability-context"
  - "methods-rigid-flex-stackup-and-bend-reliability-posture"
  - "methods-sequential-lamination-posture"
  - "methods-controlled-impedance-tdr-verification-posture"
  - "14-layer-standards-threshold-boundary"

source_ids:
  # Official manufacturer sources
  - "panasonic-megtron-6-r5775n"
  - "panasonic-megtron-6-datasheet"
  - "isola-370hr-datasheet"
  - "isola-fr408hr-datasheet"
  - "iteq-it-180a-page"
  - "taconic-rf-35-product-page"
  
  # Internal posture sources
  - "frontendapt-pcb-high-layer-count-pcb-page-en"
  - "frontendapt-pcb-rigid-flex-pcb-page-en"
  - "frontendapt-pcb-multilayer-pcb-page-en"
  - "frontendhil-rigid-flex-pcb-product-page-en"
  - "frontendhil-multilayer-pcb-product-page-en"

wiki_framing_support:
  - "wiki/processes/rigid-board-family-and-layer-boundaries"
  - "wiki/processes/rigid-flex-handling-lane"

must_refresh:
  - claim: "Rigid-flex capability for 14-layer specifically"
    value: true
  - claim: "Bend radius or flex-life numbers"
    value: true
  - claim: "High-layer registration claims"
    value: true

excluded_classes:
  - "B: Rigid-flex mechanical accuracy, transition tolerances"
  - "C: IPC-6013 thresholds for 14-layer rigid-flex"
  - "E: Bend-cycle thresholds, flex thickness defaults"
  - "G: Rigid-flex qualification or capability proof"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keyword** | `14 layer PCB manufacturing` |
| **Secondary Keywords** | `14 layer rigid-flex PCB`, `14 layer high layer count`, `14 layer HDI` |
| **Page Type** | `query` |
| **Search Intent** | Rigid-flex decision, high-layer branching, stackup complexity |
| **Target Reader** | PCB designers, mechanical engineers, NPI engineers |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` with explicit rigid vs rigid-flex branch containment.

---

## 3. Branch Containment

### 3.1 Rigid Branch

| Fact | fact_id | Treatment |
|------|---------|-----------|
| High-layer manufacturability | `methods-high-layer-rigid-board-manufacturability-context` | Planning posture only |
| Sequential lamination | `methods-sequential-lamination-posture` | Route discussion |
| Impedance verification | `methods-controlled-impedance-tdr-verification-posture` | Workflow discussion |
| Standards boundary | `14-layer-standards-threshold-boundary` | Context only, not threshold proof |

### 3.2 Rigid-Flex Branch

| Fact | fact_id | Treatment |
|------|---------|-----------|
| Rigid-flex posture | `methods-rigid-flex-stackup-and-bend-reliability-posture` | Stackup planning only |
| Bend reliability | (posture only) | Qualitative discussion |

**Critical Containment**: No rigid-flex reliability thresholds, bend-cycle numbers, or transition accuracy claims.

---

## 4. Coverage vs Gaps

### 4.1 Covered

| Area | Coverage |
|------|----------|
| Rigid high-layer | ✅ Material + posture |
| Rigid-flex branch | ✅ Posture only (no reliability numbers) |
| Standards context | ✅ Boundary card only |

### 4.2 Gaps

| Gap | Reason |
|-----|--------|
| Rigid-flex mechanical numbers | No governed layer |
| IPC-6013 Class 2/3 thresholds | C-class blocked |
| Bend-cycle performance | E-class blocked |

---

## 5. Handoff

**Core Answer**:

> 14-layer spans two distinct construction branches: rigid high-layer with sequential lamination considerations, and rigid-flex with stackup and bend-reliability planning needs. Current evidence supports material selection and process-planning posture for both branches, but does not support rigid-flex reliability thresholds or mechanical accuracy numbers.

**Branch Table**:

```
| Branch | When to Consider | Planning Focus | Evidence Support |
|--------|-----------------|----------------|------------------|
| Rigid 14L | High density, complex routing | Sequential lamination, via architecture | Material + posture |
| Rigid-flex 14L | Dynamic flex needs, packaging constraints | Stackup, transition zones, bend planning | Posture only (no reliability numbers) |
```

---

## 6. Pre-flight

- [x] Rigid vs rigid-flex branches contained
- [x] Material anchors mapped
- [x] Posture cards identified
- [x] Gaps (reliability thresholds) documented

**Verdict**: ✅ `go_now_conservative` with explicit branch containment.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
