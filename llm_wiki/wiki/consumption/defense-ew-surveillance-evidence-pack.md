# Defense EW Surveillance Targeting PCB Evidence Pack

**Pack ID**: `consumption-defense-ew-surveillance`
**Date**: 2026-05-02
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Defense EW surveillance targeting PCB"
scope: |
  Conservative evidence pack for defense-adjacent PCB content.
  
  Supports board-level review boundaries: RF/mixed-signal partitioning, 
  shielding and transition planning, timing and isolation review, staged validation.
  
  No mission-authority, jammer/SIGINT/SAR claims, or weapon-system proof.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Application boundary
  - "applications-defense-ew-surveillance-targeting-pcb-review-boundaries"
  
  # RF/validation
  - "methods-rf-validation-capability"
  - "methods-rf-impedance-sparameter-pdn-ota-boundaries"
  - "methods-controlled-impedance-tdr-verification-posture"
  
  # Sensor/interface
  - "methods-eo-ir-detector-owner-identity-and-interface-boundary"
  - "methods-laser-time-of-flight-pulsed-driver-and-safety-boundary"
  - "methods-phased-array-source-coverage"
  - "methods-remote-control-and-drone-control-stack-boundary"
  
  # Standards context
  - "standards-military-environmental-and-emi-qualification-boundary"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"

source_ids:
  - "frontendapt-industry-aerospace-defense-page-en"
  - "frontendapt-industry-drone-uav-page-en"
  - "frontendapt-industry-security-equipment-page-en"
  - "frontendapt-antenna-pcb-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"

wiki_framing_support:
  - "wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries"

must_refresh:
  - claim: "MIL-STD compliance status"
    value: true
  - claim: "Defense program history or customer references"
    value: true
  - claim: "Mission-readiness or fielded-system proof"
    value: true

excluded_claim_classes:
  - "Jammer, ESM, EA, wideband receiver authority claims"
  - "Exact bandwidth, threat-detection, waveform-generation claims"
  - "SAR authority, encrypted-link authority, COMSEC/TEMPEST proof"
  - "MIL-STD pass-status or supplier-qualification proof"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `defense PCB`, `electronic warfare PCB`, `surveillance PCB`, `targeting PCB` |
| **Page Type** | `query` (boundary review) |
| **Search Intent** | Defense-adjacent board design, RF partitioning, shielding, validation |
| **Target Reader** | Defense contractors, RF engineers, systems integrators |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` at board-review boundary level only.

---

## 3. Safe Article Frames

| Slug | Status | Safe Frame |
|------|--------|------------|
| `electronic-warfare-pcb` | `go_now_conservative` | RF front-end partitioning, shielding/cavity planning, hybrid material review, power/receiver coexistence, guarded MIL-STD context |
| `surveillance-pcb` | `go_now_conservative` | Multi-sensor interface context, EO/IR detector naming, imaging serial-interface vocabulary, RF/data-link coexistence |
| `targeting-pcb` | `needs_refresh_then_go` | Timing-sensitive control-board context, laser ToF subset, platform-bus vocabulary, staged validation |

---

## 4. Allowed vs Blocked Claims

### 4.1 Allowed (Board-Review Level)

| Claim Type | Example |
|------------|---------|
| RF partitioning | "RF front-end planning requires shielding and cavity consideration" |
| Mixed-signal | "Digital/RF coexistence benefits from plane planning and isolation review" |
| Shielding | "High-energy areas may require fence vias or shielding structures" |
| Timing | "Time-of-flight systems require timing-distribution planning" |
| Validation | "Defense-adjacent builds often add staged validation and traceability" |

### 4.2 Blocked (Mission-System Level)

| Claim Type | Example |
|------------|---------|
| EW capability | "Jammer output power" or "ESM detection range" |
| Surveillance performance | "SAR resolution" or "ISR endurance" |
| Targeting accuracy | "Rangefinding accuracy" or "fire-control authority" |
| Qualification proof | "MIL-STD-461 certified" or "defense-prime approved" |

---

## 5. Coverage vs Gaps

### 5.1 Covered

| Area | Coverage |
|------|----------|
| RF boundary | ✅ Partitioning vocabulary |
| Sensor interface | ✅ EO/IR detector identity |
| Validation workflow | ✅ Staged validation posture |
| Standards context | ✅ MIL-STD vocabulary (not proof) |

### 5.2 Gaps

| Gap | Reason |
|-----|--------|
| MIL-STD exact methods | No current authority |
| Defense program proof | G-class blocked |
| Performance numerics | Mission-system level blocked |

---

## 6. Handoff

**Core Answer**:

> Defense-adjacent PCB design stays safe at board-level review boundaries: RF/mixed-signal partitioning, shielding and transition planning, timing/isolation review, and staged validation. The current evidence does not support mission-system claims about jamming, surveillance, targeting performance, or defense-program qualification.

**Safe Structure**:

| Section | Treatment |
|---------|-----------|
| Application context | Defense/surveillance as scenario family |
| RF design | Partitioning, shielding, material selection |
| Sensor integration | Detector identity, interface vocabulary |
| Validation | Staged workflow, traceability |
| Standards | MIL-STD vocabulary as context only |

---

## 7. Pre-flight

- [x] Boundary wiki page referenced
- [x] Fact cards mapped
- [x] Blocked claim classes documented

**Verdict**: ✅ `go_now_conservative` for board-review boundary content.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
