# 18-Layer PCB Evidence Pack

**Pack ID**: `consumption-18-layer-pcb`
**Date**: 2026-05-02
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "18-layer PCB manufacturing"
scope: |
  Conservative evidence pack for 18-layer hybrid RF/digital builds.
  
  Supports hybrid material selection, mixed-material review posture, and 
  workflow-level validation framing. No RF geometry tables or qualification proof.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Low-loss/RF material anchors
  - "materials-panasonic-megtron-6"
  - "materials-rogers-ro4350b"
  - "materials-rogers-rt-duroid-5880"
  - "materials-taconic-rf-35"
  - "materials-agc-rf-10"
  
  # High-layer stability
  - "materials-isola-370hr"
  
  # Method posture cards
  - "methods-hybrid-rf-stackup-capability"
  - "methods-high-layer-rigid-board-manufacturability-context"
  - "methods-rf-validation-capability"
  - "methods-controlled-impedance-tdr-verification-posture"
  - "methods-sequential-lamination-posture"

source_ids:
  # Official manufacturer sources
  - "panasonic-megtron-6-r5775n"
  - "panasonic-megtron-6-datasheet"
  - "rogers-ro4350b-product-page"
  - "rogers-ro4000-datasheet"
  - "rogers-rt-duroid-5880-product-page"
  - "rogers-rt-duroid-5870-5880-datasheet"
  - "taconic-rf-35-product-page"
  - "agc-rf-10-product-page"
  - "agc-rf-10-datasheet"
  - "isola-370hr-datasheet"
  
  # Internal posture sources
  - "frontendapt-pcb-high-layer-count-pcb-page-en"
  - "frontendapt-pcb-high-frequency-pcb-page-en"
  - "frontendapt-pcb-microwave-pcb-page-en"
  - "frontendapt-pcb-hybrid-pcb-page-en"
  - "frontendhil-high-frequency-product-page-en"
  - "frontendhil-rogers-product-page-en"

wiki_framing_support:
  - "wiki/processes/hybrid-rf-stackup-strategy"
  - "wiki/processes/rf-transmission-line-structure-boundaries"

must_refresh:
  - claim: "Hybrid bonding capability"
    value: true
  - claim: "RF validation scope"
    value: true
  - claim: "18-layer specific manufacturing windows"
    value: true

excluded_classes:
  - "B: RF geometry tables, hybrid construction defaults"
  - "C: Qualification or certification proof"
  - "D: Impedance-budget claims, channel loss tables"
  - "E: Hybrid reliability thresholds"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keyword** | `18 layer PCB manufacturing` |
| **Secondary Keywords** | `18 layer hybrid RF PCB`, `18 layer high frequency PCB`, `18 layer mixed signal` |
| **Page Type** | `query` |
| **Search Intent** | Hybrid RF/digital, mixed-material, high-speed/high-layer |
| **Target Reader** | RF engineers, signal integrity engineers, hardware architects |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` for hybrid RF stackup discussion.

---

## 3. Hybrid Material Anchors

| Fact | fact_id | Application |
|------|---------|-------------|
| MEGTRON 6 low-loss | `materials-panasonic-megtron-6` | Digital high-speed sections |
| RO4350B RF hybrid | `materials-rogers-ro4350b` | RF sections with process-friendly lamination |
| RT/duroid 5880 PTFE | `materials-rogers-rt-duroid-5880` | Ultra-low-loss RF sections |
| Taconic RF-35 | `materials-taconic-rf-35` | RF antenna/power amp sections |
| AGC RF-10 high-Dk | `materials-agc-rf-10` | Compact RF sections |
| ISOLA 370HR | `materials-isola-370hr` | High-layer stability base |

---

## 4. Hybrid Stackup Posture

| Posture | fact_id | Safe Pattern |
|---------|---------|--------------|
| Hybrid capability | `methods-hybrid-rf-stackup-capability` | "Hybrid stackups as design strategy for RF+digital boards, not default recipe" |
| High-layer context | `methods-high-layer-rigid-board-manufacturability-context` | "18-layer hybrid as complex build requiring material compatibility planning" |
| RF validation | `methods-rf-validation-capability` | "RF validation through TDR/VNA/coupon/traceability planning" |
| Impedance control | `methods-controlled-impedance-tdr-verification-posture` | "Mixed-material impedance requires stackup alignment and measurement" |
| Sequential lamination | `methods-sequential-lamination-posture` | "Hybrid builds may use sequential lamination for material transitions" |

---

## 5. Coverage vs Gaps

### 5.1 Covered

| Area | Coverage |
|------|----------|
| Hybrid material selection | ✅ Official product anchors |
| Hybrid stackup strategy | ✅ Posture discussion |
| RF validation approach | ✅ Vocabulary and workflow |
| High-layer stability | ✅ Material anchors |

### 5.2 Gaps

| Gap | Reason |
|-----|--------|
| Hybrid bonding parameters | No governed layer |
| RF geometry rules | D-class blocked |
| Mixed-material impedance tables | D-class blocked |
| Hybrid qualification proof | C-class blocked |

---

## 6. Handoff

**Core Answer**:

> 18-layer hybrid RF/digital builds combine high-layer-count stability requirements with mixed-material RF performance needs. Current evidence supports material-family selection (low-loss digital, RF hybrid, PTFE) and hybrid stackup planning posture, not RF geometry tables or hybrid construction recipes.

**Hybrid Considerations**:

| Aspect | Treatment |
|--------|-----------|
| Material selection | Exact product anchors with frequency/condition context |
| Material transitions | Posture discussion (bonding, CTE compatibility) |
| RF validation | TDR/VNA/coupon vocabulary |
| Digital high-speed | Low-loss material anchors |

---

## 7. Pre-flight

- [x] Hybrid material anchors mapped
- [x] RF validation posture identified
- [x] Gaps (geometry tables) documented

**Verdict**: ✅ `go_now_conservative` for hybrid RF stackup discussion.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
