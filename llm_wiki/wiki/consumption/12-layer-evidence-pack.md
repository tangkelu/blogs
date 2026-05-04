# 12-Layer PCB Evidence Pack

**Pack ID**: `consumption-12-layer-pcb`
**Date**: 2026-05-02
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "12-layer PCB manufacturing"
scope: |
  Conservative evidence pack for 12-layer high-layer planning.
  
  Supports high-layer material selection, sequential lamination posture, 
  HDI/via architecture discussion, and validation planning.
  
  No fabrication windows, process recipes, or capability numerics included.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Material anchors
  - "materials-panasonic-megtron-4"
  - "materials-panasonic-megtron-6"
  - "materials-isola-370hr"
  - "materials-isola-fr408hr"
  - "materials-iteq-it-180a"
  
  # Method posture cards
  - "methods-high-layer-rigid-board-manufacturability-context"
  - "methods-sequential-lamination-posture"
  - "methods-hdi-microvia-and-vippo-process-posture"
  - "methods-controlled-impedance-tdr-verification-posture"
  - "methods-high-layer-count-backdrill-and-registration-posture"
  - "methods-advanced-validation-scope-segmentation"

source_ids:
  # Official manufacturer sources
  - "panasonic-megtron-4-r5725-r5620"
  - "panasonic-megtron-4-datasheet"
  - "panasonic-megtron-6-r5775n"
  - "panasonic-megtron-6-datasheet"
  - "isola-370hr-datasheet"
  - "isola-fr408hr-datasheet"
  - "iteq-it-180a-page"
  
  # Internal posture sources
  - "frontendapt-pcb-high-layer-count-pcb-page-en"
  - "frontendapt-pcb-multilayer-pcb-page-en"
  - "frontendapt-pcb-hdi-pcb-page-en"
  - "frontendapt-pcb-advanced-pcb-manufacturing-page-en"
  - "frontendapt-pcb-pcb-impedance-control-page-en"
  - "frontendapt-pcb-high-speed-pcb-page-en"
  - "frontendhil-hdi-pcb-product-page-en"
  - "frontendhil-multilayer-pcb-product-page-en"
  - "frontendhil-high-speed-product-page-en"

wiki_framing_support:
  - "wiki/processes/advanced-pcb-fabrication-and-stackup-planning"
  - "wiki/processes/bom-and-hdi-complexity-boundaries"

must_refresh:
  - claim: "Any HIL capability for 12-layer specifically"
    value: true
  - claim: "Sequential lamination count allowances"
    value: true
  - claim: "High-layer registration tolerances"
    value: true
  - claim: "HDI structure defaults for 12-layer"
    value: true

excluded_classes:
  - "B: Process-window numerics (feature size, registration, tolerance)"
  - "C: IPC Class 2/3/3A thresholds for 12-layer"
  - "D: Interface budget claims, channel loss tables"
  - "E: Sequential lamination recipe numbers, via reliability thresholds"
  - "F: Cost multipliers, lead time windows"
  - "G: Factory capability assertions"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keyword** | `12 layer PCB manufacturing` |
| **Secondary Keywords** | `12 layer HDI PCB`, `12 layer high layer PCB`, `12 layer sequential lamination` |
| **Page Type** | `query` |
| **Search Intent** | High-layer planning, HDI architecture, sequential lamination decisions |
| **Target Reader** | Senior PCB designers, hardware architects, NPI engineers |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` for high-layer planning discussion. Not a fabrication-capability unlock.

---

## 3. Usable Technical Facts

### 3.1 Material Anchors for High-Layer

| Fact | fact_id | Application |
|------|---------|-------------|
| MEGTRON 4 | `materials-panasonic-megtron-4` | Low-loss multilayer, high-Tg stability |
| MEGTRON 6 | `materials-panasonic-megtron-6` | Lower-loss for higher-speed needs |
| ISOLA 370HR | `materials-isola-370hr` | High-Tg FR-4 family anchor |
| ISOLA FR408HR | `materials-isola-fr408hr` | High-performance FR-4 |
| ITEQ IT-180A | `materials-iteq-it-180a` | High-Tg with published dielectric values |

### 3.2 High-Layer Posture Cards

| Posture | fact_id | Safe Writing Pattern |
|---------|---------|---------------------|
| High-layer manufacturability | `methods-high-layer-rigid-board-manufacturability-context` | "12-layer enters high-layer territory where lamination registration, via architecture, and material stability become planning priorities" |
| Sequential lamination | `methods-sequential-lamination-posture` | "Sequential lamination as a route for complex builds, not a default recipe" |
| HDI microvia | `methods-hdi-microvia-and-vippo-process-posture` | "HDI vocabulary for via architecture discussion, not prescriptive capability" |
| Impedance verification | `methods-controlled-impedance-tdr-verification-posture` | "High-layer impedance verification through stackup definition and measurement correlation" |
| Backdrill/registration | `methods-high-layer-count-backdrill-and-registration-posture` | "Backdrill and registration as high-layer planning topics" |
| Validation scope | `methods-advanced-validation-scope-segmentation` | "Validation ladder appropriate to layer count and design complexity" |

---

## 4. Coverage vs Gaps

### 4.1 Covered Areas

| Area | Coverage | Source |
|------|----------|--------|
| Material selection | ✅ Official product anchors | Panasonic, Isola, ITEQ fact cards |
| Stackup planning | ✅ Posture framing | `methods-high-layer-rigid-board-manufacturability-context` |
| HDI architecture | ✅ Vocabulary | `methods-hdi-microvia-and-vippo-process-posture` |
| Validation approach | ✅ Posture | `methods-advanced-validation-scope-segmentation` |

### 4.2 Identified Gaps

| Gap | Reason | Impact |
|-----|--------|--------|
| Exact 12-layer stackup recipes | No governed reusable layer | Cannot provide default stackup tables |
| Sequential lamination count limits | No current authority | Cannot state "X lamination cycles standard" |
| Registration tolerance for 12L | No B-class layer | Cannot quote ±μm values |
| HDI structure defaults | No E-class layer | Cannot prescribe 1+N+1 as default |

---

## 5. Handoff to Template

### 5.1 Core Answer

> A 12-layer PCB is typically the entry point into high-layer-count fabrication, where sequential lamination planning, via architecture choices, and material stability considerations become more prominent. Current evidence supports material-family selection and process-planning posture, not fabrication-process windows or default construction recipes.

### 5.2 Section Guidance

| Topic | Treatment |
|-------|-----------|
| Why 12 layers? | Keep as high-layer planning transition |
| Material systems | Exact product anchors with conditions |
| Sequential lamination | Posture and route discussion only |
| HDI architecture | Vocabulary and tradeoff framing |
| Stackup symmetry | Qualitative planning reminders |
| Impedance control | Verification workflow discussion |
| Validation scope | Ladder-appropriate framing |
| Cost/turnaround | **Exclude** - no F-class support |

---

## 6. Pre-flight

- [x] Official material anchors mapped
- [x] High-layer posture cards identified
- [x] Coverage/gaps documented
- [x] Excluded B/C/D/E/F/G classes noted

**Verdict**: ✅ `go_now_conservative` for high-layer planning `query` content.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
