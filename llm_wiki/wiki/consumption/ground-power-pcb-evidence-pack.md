---
title: "Ground Power PCB Evidence Pack"
category: "consumption"
status: "active"
last_reviewed_at: "2026-05-05"
tags: ["ground-power-pcb", "power-energy", "high-current", "thermal-platform", "connector-handoff", "review-boundary"]
---

# Ground Power PCB Evidence Pack

**Pack ID**: `consumption-ground-power-pcb`
**Date**: 2026-05-05
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Ground power PCB"
scope: |
  Conservative evidence pack for ground power PCB content.

  Supports board-level review boundaries for ground-based power equipment:
  power-stage and control partitioning, current-path geometry, thermal-platform choice,
  connector or harness handoff, mixed-technology assembly route, and staged validation.

  Does not support universal copper, current, creepage, clearance, Hi-Pot, certification,
  lead-time, cost, or field-life claims.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/aptpcb/query-overlay.md"

fact_ids:
  - "methods-power-energy-inverter-charger-rewrite-boundary"
  - "methods-current-carrying-trace-width-and-copper-boundary"
  - "methods-thermal-pcb-platform-selection-posture"
  - "methods-tht-pressfit-terminal-route-boundary"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"

source_ids:
  - "frontendapt-industry-power-energy-page-en"
  - "frontendapt-pcb-heavy-copper-pcb-page-en"
  - "frontendapt-pcb-high-thermal-pcb-page-en"
  - "frontendapt-pcb-metal-core-pcb-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "ipc-2152-current-carrying-capacity-toc"
  - "analog-devices-an136-pcb-layout-nonisold-switching-supplies"
  - "analog-devices-layout-considerations-for-high-power-circuits"

wiki_framing_support:
  - "wiki/consumption/power-energy-evidence-pack"
  - "wiki/applications/power-energy-pcb-pcba-review-boundaries"
  - "wiki/processes/current-carrying-and-high-current-layout-boundaries"
  - "wiki/processes/power-interface-connector-assembly-route-selection"

must_refresh:
  - claim: "Exact copper, current, temperature-rise, creepage, or clearance numerics"
    value: true
  - claim: "Hi-Pot levels, pass/fail thresholds, or qualification proof"
    value: true
  - claim: "Lead time, cost, or field-life claims"
    value: true

excluded_claim_classes:
  - "universal heavy-copper or trace-width numeric rules"
  - "creepage, clearance, Hi-Pot, or compliance proof"
  - "connector or harness current-rating guarantees"
  - "ground power unit performance or reliability numerics"
  - "cost, lead-time, yield, or field-life claims"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `ground power pcb`, `ground power board`, `ground-based power equipment pcb` |
| **Page Type** | `query` |
| **Search Intent** | High-current board review, power-board partitioning, thermal route, interface handoff, release preparation |
| **Target Reader** | Power electronics engineers, layout engineers, manufacturing engineers, sourcing and NPI teams |
| **Site** | `APTPCB` |

**Working Posture**: `go_now_conservative` at board-review boundary only.

---

## 3. Safe Article Frame

| Section Type | Safe Treatment |
|--------------|----------------|
| Definition | Treat `ground power PCB` as a board inside ground-based power equipment, not as a universal heavy-copper or high-voltage recipe |
| Design priorities | Power-stage and control partitioning, current-path geometry, thermal-platform route, connector/harness handoff |
| Validation | Separate DFM/DFA, fabrication evidence, powered functional checks, and system validation |
| Platform choice | Heavy copper, MCPCB, and other thermal routes as project-dependent options |
| Supplier handoff | Freeze stackup posture, interface route, thermal path, and validation scope before release |

---

## 4. Allowed vs Blocked Claims

### 4.1 Allowed

| Claim Type | Example |
|------------|---------|
| Partitioning | "Ground-based power boards should separate power-stage, control, and monitoring responsibilities before routing freezes." |
| High-current review | "Current-path geometry, copper route choice, planes, and layer transitions should be reviewed together." |
| Thermal-platform choice | "Heavy copper and MCPCB are different route choices, not interchangeable defaults." |
| Interface handoff | "A board-edge connector, press-fit zone, and cable or harness exit are different manufacturing paths." |
| Validation layering | "Board-level fabrication evidence and powered functional checks should stay distinct from system-level qualification." |

### 4.2 Blocked

| Claim Type | Example |
|------------|---------|
| Numeric recipe | "Use X oz copper or Y mm clearance for every ground power PCB" |
| Qualification proof | "This board is compliant with standard Z" |
| Interface guarantee | "Connector family A is always correct for ground power boards" |
| Commercial proof | "Typical lead time or cost uplift for ground power PCB" |

---

## 5. Coverage vs Gaps

### 5.1 Covered

| Area | Coverage |
|------|----------|
| Power-board partitioning | ✅ Supported |
| Conductor and current-path review | ✅ Supported |
| Thermal platform selection posture | ✅ Supported |
| Connector / harness route selection | ✅ Supported |
| DFM and powered validation workflow | ✅ Supported |

### 5.2 Gaps

| Gap | Reason |
|-----|--------|
| Exact ampacity or copper tables | Blocked at current evidence level |
| Exact creepage / clearance thresholds | Not supported in current reusable public lane |
| Program-specific compliance or field performance | Requires narrower official or project evidence |

---

## 6. Core Answer

> A ground power PCB can be written safely as a board-review problem for ground-based power equipment: define the board role, separate power and control regions, review current-path geometry and thermal route together, clarify whether the interface stays on the board or exits through connector or harness hardware, and keep release evidence distinct from system qualification.

---

## 7. Pre-flight

- [x] Local fact cards identified
- [x] Power-energy boundary page identified
- [x] High-current layout boundary identified
- [x] Interface-route boundary identified
- [x] Blocked claim classes documented

**Verdict**: ✅ `go_now_conservative` for board-level review content.
