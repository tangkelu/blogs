# 16-Layer PCB Evidence Pack

**Pack ID**: `consumption-16-layer-pcb`
**Date**: 2026-05-02
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "16-layer PCB manufacturing"
scope: |
  Conservative evidence pack for 16-layer high-layer builds.
  
  Supports material selection for high-layer stability, sequential lamination planning,
  and power/thermal architecture discussion. No process-window numerics or 
  power/thermal outcome guarantees included.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Material anchors (high-Tg, stable for high-layer)
  - "materials-panasonic-megtron-6"
  - "materials-isola-370hr"
  - "materials-isola-fr408hr"
  - "materials-panasonic-megtron-4"
  
  # Method posture cards
  - "methods-high-layer-rigid-board-manufacturability-context"
  - "methods-sequential-lamination-posture"
  - "methods-controlled-impedance-tdr-verification-posture"
  - "methods-thermal-pcb-platform-selection-posture"
  - "methods-high-layer-count-backdrill-and-registration-posture"

source_ids:
  # Official manufacturer sources
  - "panasonic-megtron-6-r5775n"
  - "panasonic-megtron-6-datasheet"
  - "panasonic-megtron-4-r5725-r5620"
  - "isola-370hr-datasheet"
  - "isola-fr408hr-datasheet"
  
  # Internal posture sources
  - "frontendapt-pcb-high-layer-count-pcb-page-en"
  - "frontendapt-pcb-multilayer-pcb-page-en"
  - "frontendapt-pcb-hdi-pcb-page-en"
  - "frontendapt-pcb-advanced-pcb-manufacturing-page-en"
  - "frontendapt-pcb-high-thermal-pcb-page-en"
  - "frontendhil-multilayer-pcb-product-page-en"

wiki_framing_support:
  - "wiki/processes/advanced-pcb-fabrication-and-stackup-planning"
  - "wiki/processes/current-carrying-and-high-current-layout-boundaries"

must_refresh:
  - claim: "High-layer capability specifically for 16L"
    value: true
  - claim: "Power/thermal performance outcomes"
    value: true
  - claim: "Sequential lamination cycle allowances"
    value: true

excluded_classes:
  - "B: Process-window numerics for 16L"
  - "D: Power/thermal outcome guarantees"
  - "E: High-layer reliability thresholds"
  - "F: Commercial claims for high-layer"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keyword** | `16 layer PCB manufacturing` |
| **Secondary Keywords** | `16 layer high layer PCB`, `16 layer power PCB`, `16 layer HDI` |
| **Page Type** | `query` |
| **Search Intent** | High-layer stability, power distribution, thermal planning |
| **Target Reader** | Hardware architects, power electronics designers, NPI engineers |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` for high-layer material stability and planning discussion.

---

## 3. Usable Facts

### 3.1 Material Stability Anchors

| Fact | fact_id | Safe Pattern |
|------|---------|--------------|
| MEGTRON 6 high-layer | `materials-panasonic-megtron-6` | "MEGTRON 6 for high-layer builds needing low-loss and thermal stability" |
| ISOLA 370HR high-Tg | `materials-isola-370hr` | "370HR as high-Tg FR-4 for thermal stability in high-layer counts" |
| FR408HR performance | `materials-isola-fr408hr` | "FR408HR when higher performance FR-4 needed" |

### 3.2 Posture Cards

| Posture | fact_id | Application |
|---------|---------|-------------|
| High-layer manufacturability | `methods-high-layer-rigid-board-manufacturability-context` | Lamination registration, stability planning |
| Sequential lamination | `methods-sequential-lamination-posture` | Route for complex 16L builds |
| Impedance verification | `methods-controlled-impedance-tdr-verification-posture` | High-layer measurement correlation |
| Thermal platform | `methods-thermal-pcb-platform-selection-posture` | When heat removal dominates |
| Backdrill/registration | `methods-high-layer-count-backdrill-and-registration-posture` | High-speed/RF in high-layer context |

---

## 4. Coverage vs Gaps

### 4.1 Covered

| Area | Coverage |
|------|----------|
| Material stability | ✅ High-Tg official anchors |
| Sequential lamination posture | ✅ Planning discussion |
| Power/thermal framing | ✅ Platform selection posture |

### 4.2 Gaps

| Gap | Reason |
|-----|--------|
| 16L specific stackup recipes | No governed reusable layer |
| Power delivery performance numbers | D-class blocked |
| Thermal outcome guarantees | D-class blocked |
| High-layer cost structures | F-class blocked |

---

## 5. Handoff

**Core Answer**:

> 16-layer enters high-layer territory where material thermal stability, sequential lamination planning, and power/thermal architecture become significant considerations. Current evidence supports material-family selection and process-planning posture, not fabrication-process windows or power/thermal performance guarantees.

**Planning Topics**:

| Consideration | Evidence Support |
|--------------|------------------|
| Material thermal stability | Official high-Tg anchors |
| Sequential lamination needs | Posture discussion only |
| Power plane allocation | Planning framing |
| Thermal management | Platform selection posture |

---

## 6. Pre-flight

- [x] High-Tg material anchors mapped
- [x] High-layer posture cards identified
- [x] Gaps documented

**Verdict**: ✅ `go_now_conservative` for high-layer planning.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
