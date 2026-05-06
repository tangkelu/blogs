# Hub Motor Inverter PCB Evidence Pack

**Pack ID**: `consumption-hub-motor-inverter-pcb`
**Date**: 2026-05-05
**Status**: `go_now_conservative`
**Template**: `blog-rewrite`

---

## 1. Traceability Core

```yaml
topic: "Hub motor inverter PCB rewrite"
scope: |
  Conservative evidence pack for rewriting a hub-motor inverter article.

  Supports a board-review article about inverter board role, power-stage
  versus control partitioning, high-current path geometry, thermal-platform
  choice, gate-drive and sensing separation, and staged validation ownership.

  Does not support universal current tables, trace-width-per-amp rules,
  switching-frequency claims, efficiency claims, thermal-rise guarantees,
  overload ratings, component-rating guarantees, or field-reliability claims.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  - "applications-automotive-ev-coverage-gap-map"
  - "methods-power-energy-inverter-charger-rewrite-boundary"
  - "methods-current-carrying-trace-width-and-copper-boundary"
  - "methods-thermal-pcb-platform-selection-posture"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-npi-to-mass-production-gates"

wiki_framing_support:
  - "wiki/applications/automotive-ev-pcb-pcba-boundary-map"
  - "wiki/applications/power-energy-pcb-pcba-review-boundaries"
  - "wiki/processes/current-carrying-and-high-current-layout-boundaries"
  - "wiki/processes/power-interface-connector-assembly-route-selection"

source_ids:
  - "frontendapt-industry-automotive-electronics-page-en"
  - "frontendapt-industry-power-energy-page-en"
  - "frontendapt-pcb-heavy-copper-pcb-page-en"
  - "frontendapt-pcb-high-thermal-pcb-page-en"
  - "frontendapt-pcb-metal-core-pcb-page-en"
  - "frontendhil-heavy-copper-pcb-product-page-en"

must_refresh:
  - claim: "Any exact current, copper thickness, thermal, or clearance claim"
    value: true
  - claim: "Any exact inverter efficiency, switching, or motor-performance claim"
    value: true
  - claim: "Any cost, lead-time, yield, or field-reliability claim"
    value: true

excluded_claim_classes:
  - "Motor-drive performance proof"
  - "Efficiency or thermal-rise guarantee"
  - "High-voltage safety threshold or creepage proof"
  - "Component-rating guarantee"
  - "Cost, lead-time, yield, or field-reliability claims"
```

---

## 2. Rewrite Posture

| Field | Value |
|---|---|
| **Primary keyword** | `hub motor inverter pcb` |
| **Reader intent** | Understand what to review before releasing an inverter board |
| **Safe angle** | Inverter board release-review boundary |
| **Unsafe angle** | Spec sheet, performance promise, or troubleshooting table |

**Working posture**: treat this topic as a `power stage + control separation + thermal route + validation` review. The article should explain how the board is structured, where the current path lives, and what evidence belongs to board release versus powered system testing.

---

## 3. Supported Content Shapes

### 3.1 Board role

- Safe to describe a hub-motor inverter board as a power-stage board that must coexist with control and sensing logic.
- Safe to explain that not every inverter is the same board family, even if the marketing label is similar.

### 3.2 Path separation

- Safe to split the design into high-current power paths, gate-drive routing, sensing paths, and low-voltage control.
- Safe to explain that the first risk is usually path geometry and local transition quality, not a giant numeric promise.

### 3.3 Thermal platform choice

- Safe to discuss heavy copper, MCPCB, and other thermal platforms as option families.
- Safe to explain that the correct platform depends on where the real thermal bottleneck lives.

### 3.4 Assembly and validation

- Safe to discuss DFM, assembly route, reflow concern, inspection, and powered functional test as separate gates.
- Safe to explain that powered behavior is not the same as proving a full system or field-life outcome.

---

## 4. Recommended Article Spine

1. What should engineers review first in a hub-motor inverter board?
2. Where do power, control, and sensing paths need to stay separate?
3. Why does the thermal route matter before layout is frozen?
4. What should be checked at fabrication, assembly, and powered test?
5. What should be frozen before RFQ or release?

---

## 5. Handoff Summary

> A safe rewrite of `hub motor inverter pcb` should behave like a board-release review article, not a parameter table. It should separate power stage from control and sensing, treat thermal-platform choice as project-dependent, and keep powered functional test distinct from performance or field-life proof.

**Verdict**: ✅ `go_now_conservative`
