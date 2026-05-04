# 6-Layer PCB Evidence Pack

**Pack ID**: `consumption-6-layer-pcb`
**Date**: 2026-05-02
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "6-layer PCB manufacturing"
scope: |
  Conservative public explanation of what 6-layer construction changes in 
  stackup planning, material selection, validation posture, and special-build branching.
  
  Allowed hard numerics are limited to official material datasheet or official 
  product-page anchors already normalized into stable material fact cards.
  
  Internal site/process pages may support posture, workflow, and boundary control only.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Material anchors (official product-grade)
  - "materials-fr4-official-source-coverage"
  - "materials-iteq-it-180a"
  - "materials-panasonic-megtron-6"
  - "materials-rogers-ro4350b"
  - "materials-rogers-rt-duroid-5880"
  - "materials-agc-rf-10"
  
  # Method posture cards (non-numeric framing)
  - "methods-pcb-stackup-special-process-and-baseline-families"
  - "methods-controlled-impedance-tdr-verification-posture"
  - "methods-rf-validation-capability"
  - "methods-thermal-pcb-platform-selection-posture"
  - "methods-rigid-flex-stackup-and-bend-reliability-posture"
  - "methods-backdrill-control-capability"

source_ids:
  # Official manufacturer sources
  - "isola-fr408-datasheet"
  - "isola-fr408hr-datasheet"
  - "iteq-it-180a-page"
  - "panasonic-megtron-6-r5775n"
  - "panasonic-megtron-6-datasheet"
  - "rogers-ro4350b-product-page"
  - "rogers-ro4000-datasheet"
  - "rogers-rt-duroid-5880-product-page"
  - "rogers-rt-duroid-5870-5880-datasheet"
  - "agc-rf-10-product-page"
  - "agc-rf-10-datasheet"
  - "agc-rf-microwave-laminates-page"
  
  # Internal posture sources
  - "frontendapt-materials-spread-glass-fr4-page-en"
  - "frontendapt-materials-isola-pcb-page-en"
  - "frontendapt-pcb-fr4-pcb-page-en"
  - "frontendapt-pcb-high-tg-pcb-page-en"
  - "frontendapt-pcb-pcb-stack-up-page-en"
  - "frontendapt-pcb-multi-layer-laminated-structure-page-en"
  - "frontendapt-pcb-special-pcb-manufacturing-page-en"
  - "frontendapt-pcb-pcb-impedance-control-page-en"
  - "frontendapt-pcb-high-speed-pcb-page-en"
  - "frontendapt-pcb-multilayer-pcb-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
  - "frontendapt-pcb-rigid-flex-pcb-page-en"
  - "frontendapt-pcb-flex-pcb-page-en"
  - "frontendapt-pcba-flex-rigid-flex-page-en"
  - "frontendapt-pcb-high-thermal-pcb-page-en"
  - "frontendapt-pcb-metal-core-pcb-page-en"
  - "frontendapt-pcb-ceramic-pcb-page-en"
  - "frontendhil-rigid-flex-pcb-product-page-en"
  - "frontendhil-flex-pcb-product-page-en"
  - "frontendhil-high-frequency-product-page-en"
  - "frontendhil-rogers-product-page-en"
  - "frontendhil-high-thermal-pcb-product-page-en"
  - "frontendhil-metal-core-pcb-product-page-en"
  - "frontendhil-ceramic-pcb-product-page-en"
  - "frontendhil-heavy-copper-pcb-product-page-en"

must_refresh:
  - claim: "Any HIL capability or service promise"
    value: true
    reason: "Dynamic commercial status"
  - claim: "Price, cost uplift, lead time, MOQ"
    value: true
    reason: "Quote-stage specifics"
  - claim: "Internal acceptance threshold or verification percentage"
    value: true
    reason: "Shop-specific capability"
  - claim: "Exact geometry-derived impedance table"
    value: true
    reason: "Project-specific derivation"

conflicts:
  - "Blog treats broad FR-4 families as one numeric ladder; material coverage requires product-specific handling"
  - "Blog mixes validation posture with unsupported tolerance numbers"
  - "Blog mixes special-build posture with unsupported thermal/flex thresholds"

wiki_framing_support:
  - "wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md"
  - "wiki/testing/validation-ladder-from-e-test-to-si-verification.md"
  
notes:
  - "Use wiki/process pages only as secondary framing support, not atomic facts"
  - "Do not invent or promote new fact_ids during prompt execution"
  - "If paragraph has no valid fact_id anchor, it is not eligible for publication"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keyword** | `6 layer PCB manufacturing` |
| **Secondary Keywords** | `6 layer PCB stackup`, `6 layer PCB materials`, `6 layer PCB impedance control`, `6 layer rigid-flex PCB`, `6 layer RF PCB` |
| **Page Type** | `query` |
| **Search Intent** | Engineering decision, stackup planning, manufacturing planning, supplier communication |
| **Target Reader** | Hardware engineer, PCB designer, sourcing/NPI engineer, technical buyer |
| **Site** | `HILPCB` |

**Working Posture**: First-wave conservative `query` rewrite. Usable for controlled evidence-pack assembly, not high-numeric-density unlock.

---

## 3. Usable Technical Facts

### 3.1 Official Material Anchors

| Fact | fact_id | Safe Writing Pattern |
|------|---------|---------------------|
| FR-4 is a family, not one universal material | `materials-fr4-official-source-coverage` | "FR-4 is a family label, so hard values should be tied to named products such as FR408, FR408HR, or IT-180A rather than generalized across all FR-4" |
| IT-180A high-Tg example | `materials-iteq-it-180a` | "ITEQ lists IT-180A with Tg 175°C, Td 345°C, and Dk 4.1 / Df 0.017 at 10 GHz with RC 50%" |
| MEGTRON 6 low-loss example | `materials-panasonic-megtron-6` | "Panasonic publishes a public MEGTRON 6 grade with Tg 185°C, Td 410°C, and low-loss dielectric values, but grade and frequency context should stay attached" |
| RO4350B RF hybrid example | `materials-rogers-ro4350b` | "Rogers publishes RO4350B as a low-loss RF laminate with epoxy/glass-style processing and a process Dk 3.48 ± 0.05 at 10 GHz / 23°C" |
| RT/duroid 5880 PTFE example | `materials-rogers-rt-duroid-5880` | "Rogers publishes RT/duroid 5880 with Dk 2.20 ± 0.02 and Df 0.0009 at 10 GHz, making it a useful PTFE benchmark" |
| RF-10 high-Dk RF example | `materials-agc-rf-10` | "AGC publishes RF-10 as a high-Dk RF laminate with Dk 10.2 ± 0.3 and Df 0.0025 at 10 GHz" |

### 3.2 Internal Posture Framing

| Posture | fact_id | Safe Writing Pattern |
|---------|---------|---------------------|
| 6-layer is a stackup-planning category | `methods-pcb-stackup-special-process-and-baseline-families` | "A 6-layer PCB is better treated as a stackup-planning category that can branch into baseline FR-4, RF hybrid, thermal, or flex routes" |
| Impedance should be paired with verification | `methods-controlled-impedance-tdr-verification-posture` | "Controlled impedance should be described as a stackup-and-measurement workflow, often paired with TDR or coupon-style validation, not just nominal target labels" |
| RF builds add validation planning | `methods-rf-validation-capability` | "RF and mixed RF/digital programs may add coupon, TDR, VNA, and traceability planning, depending on project scope" |
| Thermal platforms are separate routes | `methods-thermal-pcb-platform-selection-posture` | "When heat removal dominates, metal-core, ceramic, and heavy-copper options should be evaluated as separate build platforms rather than one generic 6-layer upgrade" |
| Rigid-flex requires stackup planning | `methods-rigid-flex-stackup-and-bend-reliability-posture` | "A 6-layer rigid-flex build should be framed around stackup, transition design, and bend reliability planning rather than generic layer-count capability" |

---

## 4. Claim Extraction & Disposition

| Current Section | Representative Claim | Class | Disposition |
|-----------------|----------------------|-------|-------------|
| Capability banner | `±8%`, `3/3mil`, `100% electrical testing`, same-day support | B/F/G | **Exclude entirely** |
| Why 6 Layers? | More planes improve planning options | judgment | **Keep** (remove price claims) |
| FR-4 section | Generic FR-4 numeric ladders | A mixed E | **Downgrade** (use exact product anchors only) |
| Stackup configurations | Copper weights, dielectric windows | B/D/E | **Delete** or rewrite without hard numbers |
| High-frequency section | Material family split | public | **Keep** (with exact-product cards) |
| RF hybrid table | Layer-by-layer recipe | A/D/B | **Downgrade** (keep concept, remove table) |
| Thermal section | Heat-flux thresholds | B/E/D | **Delete** |
| Flex/rigid-flex | Bend-cycle multipliers | B/E | **Delete** |
| Impedance section | Width tables, `±8-10%` | D/B/G | **Delete** |
| Via strategies | Hole minima, aspect ratio | B/C | **Delete** |
| DFM rules | Feature-size numbers | B | **Delete** |
| Cost section | Price and optimization numerics | F | **Exclude section** |
| HIL CTA | Capability/tolerance/turnaround claims | B/F/G | **Replace with neutral next-step** |

---

## 5. Handoff to Template

### 5.1 Recommended Structure

**Title Direction**:
- "What Is a 6-Layer PCB and When Should You Use One?"
- "6 Layer PCB Manufacturing: How to Choose Stackup, Materials, and Validation Path"

**Early Table**:
```
| Build Route | What 6 Layers Solve | Safe Material Anchor | What to Verify |
|-------------|---------------------|----------------------|----------------|
| Baseline FR-4 | Plane separation, routing density | FR-4 family (exact product for hard values) | Stackup symmetry, material grade |
| RF/low-loss hybrid | Controlled loss on critical paths | RO4350B, MEGTRON 6 (with conditions) | Hybrid bonding, transition planning |
| Thermal platform | Heat removal priority | MCPCB/ceramic/heavy-copper as separate platforms | Platform-specific DFM |
| Flex/rigid-flex | Bend architecture needs | Rigid-flex stackup family | Bend reliability planning |
```

### 5.2 Section Bridge Map

| Current Structure | Prompt Action |
|-------------------|---------------|
| Front matter and capability quote block | **Exclude** |
| Why 6 Layers? | Keep, remove price/performance claims |
| FR-4 section | Keep with family-level + exact-product anchors |
| Stackup configurations | Rewrite to non-numeric architecture comparison |
| High-frequency section | Keep with exact material cards |
| Thermal section | Keep as platform-selection posture |
| Rigid-flex section | Keep as posture and tradeoff framing |
| Impedance section | Keep as stackup + verification logic |
| Via strategies | Keep vocabulary and tradeoff logic only |
| Lamination/drilling/finish | Keep as qualitative workflow |
| DFM rules | Keep non-numeric engineering checks |
| Cost section | **Exclude** |
| HIL CTA | Replace with neutral next-step |

---

## 6. Pre-flight Checklist

- [x] Hard information extracted from official sources
- [x] Public facts / project judgments / unsupported separated
- [x] Primary official sources present for usable numerics
- [x] Unsupported numerics flagged for deletion
- [x] Wiki pages kept as secondary framing only
- [x] Early citation plan prepared
- [x] Quick answer material prepared
- [x] FAQ query phrasing seeds prepared
- [x] Template choice fixed to `query`

**Conservative Verdict**: ✅ Usable for first-wave `query` rewrite with controlled evidence-pack assembly.

---

*This evidence pack follows the specification in `policies/prompt-consumption-specification.md`*
