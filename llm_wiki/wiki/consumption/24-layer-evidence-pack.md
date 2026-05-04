# 24-Layer PCB Evidence Pack

**Pack ID**: `consumption-24-layer-pcb`
**Date**: 2026-05-02
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "24-layer PCB manufacturing"
scope: |
  Conservative evidence pack for 24-layer high-speed system context.
  
  Supports high-speed material ladder, backplane/connector integration posture,
  and workflow-level validation framing. No channel-budget numerics or 
  compliance authority claims.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # High-speed material anchors
  - "materials-panasonic-megtron-6"
  - "materials-panasonic-megtron-7"
  - "materials-isola-tachyon-100g"
  - "materials-taconic-fastrise"
  
  # High-layer/validation
  - "methods-high-layer-rigid-board-manufacturability-context"
  - "methods-high-speed-interface-system-context"
  - "methods-controlled-impedance-tdr-verification-posture"
  - "methods-press-fit-and-backplane-integration-posture"
  - "methods-advanced-validation-scope-segmentation"
  - "methods-backdrill-control-capability"

source_ids:
  # Official manufacturer sources
  - "panasonic-megtron-6-r5775n"
  - "panasonic-megtron-6-datasheet"
  - "panasonic-megtron-7-product-page"
  - "isola-tachyon-100g-datasheet"
  - "taconic-fastrise-product-page"
  
  # Internal posture sources
  - "frontendapt-pcb-high-layer-count-pcb-page-en"
  - "frontendapt-pcb-high-speed-pcb-page-en"
  - "frontendapt-pcb-backplane-pcb-page-en"
  - "frontendapt-pcb-pcb-impedance-control-page-en"
  - "frontendhil-high-speed-product-page-en"
  - "frontendhil-backplane-product-page-en"

wiki_framing_support:
  - "wiki/processes/backplane-execution-and-connector-integration"
  - "wiki/interfaces/high-speed-pcb-interface-requirements-and-design-boundaries"

must_refresh:
  - claim: "High-speed capability specifically for 24L"
    value: true
  - claim: "Backplane/connector integration claims"
    value: true
  - claim: "Insertion loss or channel budget numbers"
    value: true

excluded_classes:
  - "B: High-layer fabrication windows for 24L"
  - "C: Compliance or qualification authority"
  - "D: Channel-loss budgets, insertion-loss tables, Nyquist claims"
  - "E: High-layer reliability or process-window claims"
  - "F: Commercial claims for 24-layer builds"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keyword** | `24 layer PCB manufacturing` |
| **Secondary Keywords** | `24 layer high speed PCB`, `24 layer backplane`, `24 layer 112G` |
| **Page Type** | `query` |
| **Search Intent** | High-speed backplane, data center, 56G/112G, system context |
| **Target Reader** | System architects, SI engineers, backplane designers |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` for high-speed system context.

---

## 3. High-Speed Material Ladder

| Speed | Material | fact_id | Df Target |
|-------|----------|---------|-----------|
| 56G PAM4 | MEGTRON 6 | `materials-panasonic-megtron-6` | < 0.004 |
| 112G PAM4 | MEGTRON 7 | `materials-panasonic-megtron-7` | < 0.002 |
| 100G Ethernet | Tachyon 100G | `materials-isola-tachyon-100g` | Low-loss |
| Ultra-low loss | fastRise | `materials-taconic-fastrise` | Very low Df |

---

## 4. High-Speed System Context

| Posture | fact_id | Safe Pattern |
|---------|---------|--------------|
| High-speed interface context | `methods-high-speed-interface-system-context` | "PCIe, DDR5, 112G as system-context pressure increasing stackup demands" |
| Backplane integration | `methods-press-fit-and-backplane-integration-posture` | "Backplane builds require connector integration and validation planning" |
| Impedance verification | `methods-controlled-impedance-tdr-verification-posture` | "High-speed impedance through TDR/VNA correlation" |
| Validation scope | `methods-advanced-validation-scope-segmentation` | "Validation ladder from e-test to SI verification for high-speed" |
| Backdrill | `methods-backdrill-control-capability` | "Backdrill for stub control in high-speed layers" |
| High-layer context | `methods-high-layer-rigid-board-manufacturability-context` | "24-layer as high-layer build requiring discipline" |

---

## 5. Coverage vs Gaps

### 5.1 Covered

| Area | Coverage |
|------|----------|
| High-speed material ladder | ✅ Official product anchors |
| System context framing | ✅ Posture cards |
| Backplane integration | ✅ Planning posture |
| Validation approach | ✅ Scope segmentation |

### 5.2 Gaps

| Gap | Reason |
|-----|--------|
| 112G channel budgets | D-class blocked |
| Insertion loss tables | D-class blocked |
| COM/BER compliance proof | C-class blocked |
| 24L specific stackup recipes | No governed layer |

---

## 6. Handoff

**Core Answer**:

> 24-layer PCBs are typically used in high-speed system contexts (data center backplanes, 56G/112G, high-speed compute) where material loss characteristics and stackup planning become critical. Current evidence supports high-speed material-family selection and system-context framing, not channel-budget numerics or compliance authority claims.

**Speed-to-Material Reference** (with conditions):

| Interface | Speed | Material Direction | Validation |
|-----------|-------|-------------------|------------|
| PCIe Gen5 | 32 GT/s | Low-loss (MEGTRON 6 class) | TDR/VNA |
| PCIe Gen6 | 64 GT/s | Very-low-loss (MEGTRON 7 class) | TDR/VNA/COM |
| 56G PAM4 | 56 Gbps | Low-loss with backdrill | S-parameter |
| 112G PAM4 | 112 Gbps | Ultra-low-loss | Full SI validation |

---

## 7. Pre-flight

- [x] High-speed material ladder mapped
- [x] System context posture cards identified
- [x] Gaps (channel budgets) documented

**Verdict**: ✅ `go_now_conservative` for high-speed system context.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
