# 8-Layer PCB Evidence Pack

**Pack ID**: `consumption-8-layer-pcb`
**Date**: 2026-05-02
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "8-layer PCB manufacturing"
scope: |
  First-wave conservative evidence pack for 8-layer architecture framing.
  
  Supports material-family selection, stackup planning, impedance/validation workflow,
  and controlled variant branching (RF, thermal, rigid-flex).
  
  Internal capability numbers and geometry tables excluded.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Material anchors
  - "materials-fr4-official-source-coverage"
  - "materials-non-isola-fr4-to-very-low-loss-coverage"
  - "materials-panasonic-megtron-4-low-loss-product-coverage"
  
  # Method posture cards
  - "methods-controlled-impedance-tdr-verification-posture"
  - "methods-high-layer-count-backdrill-and-registration-posture"
  - "methods-spread-glass-and-controlled-impedance-planning"
  - "methods-hybrid-rf-stackup-capability"
  - "methods-rigid-flex-stackup-and-bend-reliability-posture"

source_ids:
  # Official manufacturer sources
  - "isola-fr408-datasheet"
  - "isola-fr408hr-datasheet"
  - "panasonic-megtron-4-r5725-r5620"
  - "panasonic-megtron-4-datasheet"
  - "iteq-it-150da-page"
  - "shengyi-s1000-2m-product-page"
  
  # Internal posture sources
  - "frontendapt-materials-spread-glass-fr4-page-en"
  - "frontendapt-materials-controlled-impedance-stackups-page-en"
  - "frontendapt-materials-megtron-pcb-page-en"
  - "frontendapt-pcb-pcb-impedance-control-page-en"
  - "frontendapt-pcb-high-speed-pcb-page-en"
  - "frontendapt-pcb-multilayer-pcb-page-en"
  - "frontendapt-pcb-high-layer-count-pcb-page-en"
  - "frontendapt-pcb-advanced-pcb-manufacturing-page-en"
  - "frontendhil-high-speed-product-page-en"
  - "frontendhil-hdi-pcb-product-page-en"
  - "frontendhil-teflon-pcb-product-page-en"
  - "frontendhil-rogers-product-page-en"
  - "frontendhil-high-frequency-product-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
  - "frontendapt-pcb-rigid-flex-pcb-page-en"
  - "frontendapt-pcb-flex-pcb-page-en"
  - "frontendapt-pcba-flex-rigid-flex-page-en"
  - "frontendhil-rigid-flex-pcb-product-page-en"
  - "frontendhil-flex-pcb-product-page-en"

wiki_framing_support:
  - "wiki/processes/advanced-pcb-fabrication-and-stackup-planning"
  - "wiki/processes/hybrid-rf-stackup-strategy"
  - "wiki/testing/validation-ladder-from-e-test-to-si-verification"

must_refresh:
  - claim: "Any HIL capability values"
    value: true
  - claim: "Lead-time, quick-turn, scaling, same-day support"
    value: true
  - claim: "Exact impedance-tolerance or validation-scope numbers"
    value: true
  - claim: "Material stocking or availability"
    value: true

excluded_classes:
  - "B: Fabrication capability numerics (trace/space, drill, via, aspect ratio)"
  - "C: Standards/qualification numerics (IPC thresholds, plating minima)"
  - "D: Board-level SI/EMC numerics (dB reduction, channel budgets)"
  - "E: HDI/reliability numerics (bend radius, lamination counts)"
  - "F: Dynamic commercial numerics (cost, lead time)"
  - "G: Supplier-status assertions"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keyword** | `8 layer PCB manufacturing` |
| **Secondary Keywords** | `8 layer PCB stackup`, `8 layer mixed-signal PCB`, `8 layer RF PCB`, `8 layer rigid-flex PCB` |
| **Page Type** | `query` |
| **Search Intent** | Design decision, mixed-signal planning, RF/thermal branching |
| **Target Reader** | Layout engineers, hardware engineers, sourcing/NPI engineers |
| **Site** | `HILPCB` |

**Working Posture**: Conservative bridge-prep only. Not a high-numeric-density unlock.

---

## 3. Usable Technical Facts

### 3.1 Official Material Anchors

| Fact | fact_id | Safe Writing Pattern |
|------|---------|---------------------|
| FR-4 family framing | `materials-fr4-official-source-coverage` | Use exact product names (FR408, FR408HR) for hard values |
| Non-Isola FR-4 coverage | `materials-non-isola-fr4-to-very-low-loss-coverage` | ITEQ IT-150DA, Shengyi S1000-2M as exact product examples |
| MEGTRON 4 low-loss | `materials-panasonic-megtron-4-low-loss-product-coverage` | R-5725/R-5620 public grades with conditions attached |

### 3.2 Internal Posture Framing

| Posture | fact_id | Safe Writing Pattern |
|---------|---------|---------------------|
| Impedance verification | `methods-controlled-impedance-tdr-verification-posture` | Pair impedance targets with TDR/coupon correlation |
| High-layer registration | `methods-high-layer-count-backdrill-and-registration-posture` | Discuss registration and backdrill as planning topics |
| Spread-glass planning | `methods-spread-glass-and-controlled-impedance-planning` | Mention skew mitigation through material choice |
| RF hybrid capability | `methods-hybrid-rf-stackup-capability` | Hybrid stackups as design strategy, not default recipe |
| Rigid-flex reliability | `methods-rigid-flex-stackup-and-bend-reliability-posture` | Bend reliability as stackup/process planning issue |

---

## 4. Section Bridge Guidance

| Section | Safe Treatment | Excluded Content |
|---------|---------------|----------------|
| When 6 layers not enough | Qualitative 8-layer flexibility framing | `10dB` reduction claims, `25-35%` cost uplift |
| Three stack-up architectures | Architecture vocabulary, tradeoff framing | `3-5mil` spacing, `200-400pF/cm²` values |
| Mixed-signal design | Unified vs split-ground caution | `100MHz`, `15mm`, `λ/20` numerics |
| Material systems | Exact product examples with conditions | Generic 8-layer thickness defaults |
| Wireless/RF | Hybrid stackup posture | Via-transition geometry rules |
| Rigid-flex medical/aerospace | Separate construction branch posture | `8R-2F`, `25-50μm`, `±4mil` numbers |
| Via architecture | Vocabulary only | `10:1`, `0.15mm`, `15-25%` cost |
| Lamination/thickness | Qualitative symmetry/copper balance | `±10%`, `±5-8%` tolerances |
| Impedance/crosstalk | Planning-plus-verification workflow | `90Ω`, `100Ω` universal tables, `3W rule` |
| Testing/verification | Validation-ladder framing | `100% electrical testing`, `3-5` coupons |
| DFM checklist | Qualitative review prompts | `±20%`, `5GHz`, `≥3mil` thresholds |

---

## 5. Handoff to Template

### 5.1 Recommended Structure

**Title Direction**: "8-Layer PCB Design: Stackup Planning for Mixed-Signal and RF"

**Core Message**: 
8-layer is the point where plane allocation, partitioning, and material choice become more explicit engineering decisions. Current evidence supports material-grade examples and process-planning posture, not fabrication-capability numerics.

### 5.2 Section Map

| Current Structure | Prompt Action |
|-------------------|---------------|
| When 6 layers not enough | Keep qualitative framing, remove emission/cost numerics |
| Three stack-up architectures | Keep architecture vocabulary, remove spacing/capacitance numbers |
| Mixed-signal design | Keep grounding caution, remove via-fencing numerics |
| Material systems | Use exact product examples, remove generic defaults |
| Wireless/RF | Keep hybrid posture, remove performance promises |
| Rigid-flex | Keep branch posture, remove mechanical numbers |
| Via architecture | Keep vocabulary, remove size/cost tables |
| Lamination | Keep qualitative controls, remove tolerance claims |
| Impedance/crosstalk | Keep verification workflow, remove universal tables |
| Testing | Keep validation ladder, remove coverage numbers |
| DFM | Keep qualitative prompts, remove threshold numerics |

---

## 6. Pre-flight Checklist

- [x] Official material anchors identified
- [x] Non-numeric posture cards mapped
- [x] B/C/D/E/F/G exclusions documented
- [x] Section-by-section guidance complete
- [x] Wiki framing support noted (secondary only)
- [x] Must-refresh items identified

**Conservative Verdict**: ✅ `bridge_prep_only` for `query` template use with controlled pruning.

---

*This evidence pack follows the specification in `policies/prompt-consumption-specification.md`*
