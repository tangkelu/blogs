# 10-Layer PCB Evidence Pack

**Pack ID**: `consumption-10-layer-pcb`
**Date**: 2026-05-02
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "10-layer PCB manufacturing"
scope: |
  Conservative evidence pack for 10-layer architecture framing with HDI/multilayer posture.
  
  Supports material selection, stackup planning, BGA-density discussion, and guarded
  process/validation vocabulary. No fabrication-capability numerics included.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Material anchors
  - "materials-iteq-it-180a"
  - "materials-panasonic-megtron-4"
  - "materials-panasonic-megtron-6"
  - "materials-shengyi-s1000-2"
  - "materials-fr4-official-source-coverage"
  
  # Method posture cards
  - "methods-pcb-stackup-special-process-and-baseline-families"
  - "methods-hdi-microvia-and-vippo-process-posture"
  - "methods-controlled-impedance-tdr-verification-posture"
  - "methods-advanced-validation-scope-segmentation"
  - "methods-high-layer-rigid-board-manufacturability-context"
  - "methods-high-layer-count-backdrill-and-registration-posture"
  - "methods-pcb-prototype-quickturn-and-volume-routing"
  - "methods-rigid-flex-stackup-and-bend-reliability-posture"

source_ids:
  # Official manufacturer sources
  - "iteq-it-180a-page"
  - "panasonic-megtron-4-r5725-r5620"
  - "panasonic-megtron-4-datasheet"
  - "panasonic-megtron-6-r5775n"
  - "panasonic-megtron-6-datasheet"
  - "shengyi-s1000-2-product-page"
  - "isola-370hr-datasheet"
  
  # Internal posture sources
  - "frontendapt-pcb-fr4-pcb-page-en"
  - "frontendapt-pcb-high-tg-pcb-page-en"
  - "frontendapt-pcb-pcb-stack-up-page-en"
  - "frontendapt-pcb-multi-layer-laminated-structure-page-en"
  - "frontendapt-pcb-hdi-pcb-page-en"
  - "frontendapt-pcb-advanced-pcb-manufacturing-page-en"
  - "frontendhil-hdi-pcb-product-page-en"
  - "frontendapt-pcb-pcb-impedance-control-page-en"
  - "frontendapt-pcb-high-speed-pcb-page-en"
  - "frontendapt-pcb-multilayer-pcb-page-en"
  - "frontendhil-multilayer-pcb-product-page-en"
  - "frontendapt-pcb-pcb-prototype-page-en"
  - "frontendapt-pcb-quick-turn-pcb-page-en"
  - "frontendhil-pcb-prototype-landing-en"
  - "frontendhil-quick-turn-pcb-landing-en"
  - "frontendapt-pcb-rigid-flex-pcb-page-en"
  - "frontendhil-rigid-flex-pcb-product-page-en"

wiki_framing_support:
  - "wiki/processes/advanced-pcb-fabrication-and-stackup-planning"
  - "wiki/testing/validation-ladder-from-e-test-to-si-verification"

must_refresh:
  - claim: "Lead-time or turnaround promise"
    value: true
  - claim: "Prototype-to-volume routing as current service status"
    value: true
  - claim: "Explicit impedance tolerance band"
    value: true
  - claim: "Explicit registration value"
    value: true
  - claim: "Via geometry, feature size, annular-ring number"
    value: true
  - claim: "Compliance, approval, or coverage percentage"
    value: true

conflicts:
  - "Shengyi S1000-2: product page says Tg 170°C (DSC) in characteristic block, 
     but product-performance table lists Tg 180°C (DSC) and 185°C (DMA); 
     do not flatten into one invariant value"

excluded_numerics:
  - "±50μm registration"
  - "±8% impedance tolerance"
  - "0.1mm blind-via capability"
  - "20-30% cost uplift ranges"
  - "BGA pitch escape tables as prescriptive rules"
  - "Sequential-lamination cost tables"
  - "50-80μm RCC as retained default"
  - "3/3mil, 2.5/2.5mil feature-size"
  - "±4mil rigid-flex transition accuracy"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keyword** | `10 layer PCB manufacturing` |
| **Secondary Keywords** | `10 layer PCB stackup`, `10 layer HDI PCB`, `10 layer BGA escape routing`, `10 layer PCB material selection` |
| **Page Type** | `query` |
| **Search Intent** | Design decision, manufacturing planning, process control, risk analysis |
| **Target Reader** | Layout engineers, hardware engineers, sourcing/NPI engineers, project managers |
| **Site** | `HILPCB` |

**Working Posture**: First-wave conservative `query`. Supports architecture framing and material selection, not fabrication-capability numerics.

---

## 3. Usable Technical Facts

### 3.1 Official Material Anchors

| Fact | fact_id | Safe Writing Pattern |
|------|---------|---------------------|
| IT-180A high-Tg | `materials-iteq-it-180a` | "ITEQ IT-180A official page gives Tg 175°C, Td 345°C, Dk 4.1, Df 0.017 at 10 GHz" |
| MEGTRON 4 low-loss | `materials-panasonic-megtron-4` | "Panasonic MEGTRON 4 R-5725/R-5620 public grades with conditions" |
| MEGTRON 6 lower-loss | `materials-panasonic-megtron-6` | "Panasonic MEGTRON 6 R-5775(N)/R-5670(N) for higher-speed needs" |
| Shengyi S1000-2 | `materials-shengyi-s1000-2` | "Shengyi S1000-2 with Tg values per table context (170°C DSC characteristics, 180°C DSC performance)" |
| FR-4 family boundary | `materials-fr4-official-source-coverage` | "FR-4 as family requiring exact product naming for hard values" |

### 3.2 Internal Posture Framing

| Posture | fact_id | Safe Writing Pattern |
|---------|---------|---------------------|
| Stackup planning | `methods-pcb-stackup-special-process-and-baseline-families` | "10-layer as stackup-planning category branching to HDI, RF, or rigid-flex" |
| HDI microvia posture | `methods-hdi-microvia-and-vippo-process-posture` | "HDI vocabulary (1+N+1, 2+6+2) as architecture notation, not default recipe" |
| Impedance verification | `methods-controlled-impedance-tdr-verification-posture` | "Impedance targets paired with TDR/coupon verification workflow" |
| Validation segmentation | `methods-advanced-validation-scope-segmentation` | "Electrical test, impedance, SI validation as different evidence layers" |
| High-layer manufacturability | `methods-high-layer-rigid-board-manufacturability-context` | "10-layer as high-layer count requiring planning discipline" |
| Backdrill/posture | `methods-high-layer-count-backdrill-and-registration-posture` | "Backdrill as high-speed/RF control, not default promise" |
| Prototype routing | `methods-pcb-prototype-quickturn-and-volume-routing` | "Prototype-to-volume as workflow discussion, not current service status" |
| Rigid-flex planning | `methods-rigid-flex-stackup-and-bend-reliability-posture` | "Rigid-flex as separate stackup/reliability planning branch" |

---

## 4. Claim Extraction & Disposition

| Current Pattern | Class | Disposition |
|-----------------|-------|-------------|
| `±50μm`, `±8%` tolerance claims | B | **Exclude** |
| `0.1mm` blind-via capability | B/E | **Exclude** |
| `20-30%`, `15-30%` cost adders | F | **Exclude** |
| BGA escape tables as prescriptive rules | B/D | **Exclude** |
| Sequential-lamination cost tables | F | **Exclude** |
| `50-80μm RCC` as default | B | **Exclude** |
| `3/3mil`, `2.5/2.5mil` feature-size | B | **Exclude** |
| `±4mil` rigid-flex accuracy | B | **Exclude** |
| `1+N+1`, `1+8+1`, `2+6+2` via-structure | notation | **Allow** as architecture vocabulary (clearly framed) |
| BGA-density pressure, signal-layer pressure | context | **Allow** as design-context wording |
| RF material-family selection | judgment | **Allow** without board-outcome promises |
| Rigid-flex coexistence | scope | **Allow** as variant scope |

---

## 5. Handoff to Template

### 5.1 Recommended Structure

**Core Answer**:

> A 10-layer board becomes relevant when routing density, plane planning, material choice, and validation scope are more constrained than lower-layer baselines. Current governed evidence strongly supports material-grade examples and process-planning posture. Current governed evidence does not support turning existing blog's escape-rule tables, feature-size numbers, cost adders, tolerance claims, or compliance claims into reusable hard facts.

### 5.2 Target Data

- Minimum official technical facts: 8
- Minimum early official anchors: 4
- Early fact table: **Yes**
- Second structured layer: **Yes** (decision table + comparison block)
- Glossary: No
- Supplier checklist: Yes

### 5.3 Recommended Early Table

```
| Decision Point | What 10 Layers Change | Material/Process Anchor | Verification Approach |
|----------------|----------------------|--------------------------|----------------------|
| BGA density | Escape routing pressure | HDI architecture vocabulary | Stackup + via planning review |
| Signal integrity | Loss budget priority | Low-loss family selection | TDR/coupon correlation |
| Power distribution | Plane allocation | Baseline vs high-Tg FR-4 | Target impedance planning |
| Hybrid RF needs | Material transitions | Hybrid stackup posture | Bonding + transition review |
```

---

## 6. Pre-flight Checklist

- [x] Official material anchors mapped (ITEQ, Panasonic, Shengyi, Isola)
- [x] Method posture cards identified for stackup/HDI/impedance/validation
- [x] Excluded numerics listed (B/C/D/E/F/G classes)
- [x] Conflict noted (Shengyi S1000-2 Tg values)
- [x] Wiki framing support noted (secondary only)
- [x] Must-refresh items identified

**Conservative Verdict**: ✅ `bridge_prep_only` for `query` template with controlled pruning.

---

*This evidence pack follows the specification in `policies/prompt-consumption-specification.md`*
