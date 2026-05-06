# Mining Rig PCB Evidence Pack

**Pack ID**: `consumption-mining-rig-pcb`
**Date**: 2026-05-05
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Mining rig PCB / hashboard / GPU riser / PSU breakout review"
scope: |
  Conservative evidence pack for mining-hardware board review.

  Supports board-review language for hashboards, GPU risers or backplanes,
  PSU breakout boards, and control boards used inside mining systems.

  This pack is intentionally narrow. It does NOT support universal current
  tables, exact copper-weight recipes, hash-rate claims, uptime claims, or
  field-life promises.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/aptpcb/query-overlay.md"

fact_ids:
  - "applications-compute-infrastructure-pcb-review-boundaries"
  - "methods-current-carrying-trace-width-and-copper-boundary"
  - "methods-thermal-pcb-platform-selection-posture"
  - "methods-press-fit-and-backplane-integration-posture"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-npi-to-mass-production-gates"

source_ids:
  - "apt_industries_server_datacenter"
  - "frontendapt-pcb-heavy-copper-pcb-page-en"
  - "frontendapt-pcb-high-thermal-pcb-page-en"
  - "frontendapt-backplane-pcb-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"

wiki_framing_support:
  - "wiki/applications/compute-infrastructure-pcb-review-boundaries"
  - "wiki/processes/power-interface-connector-assembly-route-selection"
  - "wiki/processes/validation-ladder-from-e-test-to-si-verification"

must_refresh:
  - claim: "Any exact current, copper-weight, thermal, or connector-rating claim"
    value: true
  - claim: "Any exact hash-rate, uptime, or field-reliability claim"
    value: true
  - claim: "Any exact cooling or environment guarantee"
    value: true

excluded_claim_classes:
  - "Hash-rate proof"
  - "24/7 uptime or field-life guarantee"
  - "Immersion-cooling efficacy proof"
  - "Connector rating or per-amp recipe without part-owner datasheet"
  - "Mining-controller, wallet, or payment-device as if they were the same family as hashboards"
```

---

## 2. Topic Summary

| Field | Value |
| --- | --- |
| **Primary Keywords** | `mining rig pcb`, `hashboard pcb`, `gpu riser pcb`, `psu breakout board` |
| **Page Type** | `query` |
| **Search Intent** | Board-level review of mining hardware, not a generic crypto marketing page |
| **Target Reader** | Hardware engineers, platform architects, release reviewers |
| **Site** | `APTPCB` |

**Working Posture**: `go_now_conservative`

## 3. Board-Review Scope

### 3.1 Hashboards

- Use this lane for ASIC-heavy boards where current distribution and heat are the main review pressure.
- Safe vocabulary: board role, current path, thermal route, copper distribution, validation gates.
- Blocked vocabulary: hash-rate proof, uptime proof, or field-life guarantee.

### 3.2 GPU Risers / Backplanes

- Use this lane for spacing or connector-heavy boards where transition quality and interface routing matter.
- Safe vocabulary: connector-zone review, backplane posture, return-path continuity, release gating.
- Blocked vocabulary: generic performance proof or deployment-scale claims.

### 3.3 PSU Breakout Boards

- Use this lane for boards that distribute power from one supply architecture into multiple exits.
- Safe vocabulary: power-path review, connector handoff, thermal route, assembly evidence.
- Blocked vocabulary: exact per-connector current recipes without part-owner datasheets.

### 3.4 Control Boards

- Use this lane only when the article is about housekeeping logic or service interfaces inside the mining platform.
- Safe vocabulary: release-review boundary, access planning, validation layering.
- Blocked vocabulary: treating the control board as proof of mining performance.

## 4. Stable Facts

- Mining hardware can be discussed safely as a compute-infrastructure board family when the article stays at board-review level.
- High-current behavior should be handled as a separate conductor-sizing and layout problem, not as a slogan.
- Heavy copper, high-thermal, and backplane-style routes are distinct board families with different tradeoffs.
- DFM, first-build inspection, and NPI-to-volume gates remain separate from system-level uptime or hash-performance proof.

## 5. Allowed vs Blocked

### Allowed

- Hashboard, riser, backplane, and PSU breakout board-review language
- Current-path and thermal-route review
- Connector-zone and transition review
- Layered validation: DFM, FAI, electrical test, and later system bring-up

### Blocked

- Hash-rate, uptime, or field-life proof
- Exact current, temperature-rise, or cooling guarantees
- Immersion-cooling efficacy claims
- Connector-rating recipes without part-owner datasheets
- Treating wallet, payment, or mining-control boards as the same family as hashboards

## 6. Handoff

**Core Answer**:

> Mining-rig PCB writing is safest when it stays at board-review level: current-path discipline, thermal-route choice, connector or cable handoff, and validation gates. The current source layer supports release review, not hash-rate proof or uptime guarantees.

**Reusable Shapes**:

- `Treat mining hardware as a compute-heavy board family, not as one universal PCB spec.`
- `Separate hashboard, riser/backplane, PSU breakout, and control-board review paths.`
- `Keep current-path and thermal-route questions distinct from later system bring-up.`
