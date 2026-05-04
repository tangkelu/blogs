# Drone / UAV PCB Evidence Pack

**Pack ID**: `consumption-drone-uav`
**Date**: 2026-05-03
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Drone / UAV PCB/PCBA — civilian/commercial (flight controller, ESC/PDB, comm/RF/nav, payload/gimbal, BMS, GCS, GNSS/IMU)"
scope: |
  Conservative evidence pack for civilian and commercial drone/UAV PCB/PCBA content.

  Supports board-class vocabulary for 7 board families: flight controller/autopilot,
  ESC/power distribution, communication/RF/navigation, payload/gimbal control,
  battery/BMS/charging, ground control/remote controller, and GNSS/IMU navigation support.

  Regulatory vocabulary (FAA Part 107, EASA UAS, FCC equipment authorization,
  Remote ID) from P4-189 official-depth card at regulatory-identity level only.
  PX4/MAVLink/ExpressLRS at architecture identity level only.
  RF frequency vocabulary at architecture context only.

  No airworthiness, FAA/EASA certification, GNSS accuracy, RF link-budget,
  BVLOS, autonomy performance, or endurance claims.

  IMPORTANT: Covers CIVILIAN/COMMERCIAL drone content only.
  For defense/military UAV: use defense-ew-surveillance-evidence-pack.md.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Application boundary
  - "applications-drone-uav-coverage-gap-map"

  # Official regulatory depth (P4-189)
  - "standards-drone-uav-official-regulatory-depth"

  # Control stack
  - "methods-remote-control-and-drone-control-stack-boundary"

  # RF / GNSS
  - "methods-rf-validation-capability"
  - "standards-interface-wireless-positioning-product-level-boundary"

  # Assembly / inspection
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-npi-to-mass-production-gates"

source_ids:
  - "frontendapt-industry-drone-uav-page-en"
  - "px4-basic-concepts-guide"
  - "mavlink-overview-page"
  - "expresslrs-getting-started"
  - "frontendapt-pcba-quality-system-page-en"

wiki_framing_support:
  - "wiki/applications/drone-uav-pcb-pcba-boundary-map"
  - "wiki/applications/drone-uav-regulatory-routing-boundary"

must_refresh:
  - claim: "FAA Part 107 rule revision or Remote ID compliance date changes"
    value: true
  - claim: "EASA UAS category revision or open-category updates"
    value: true
  - claim: "FCC equipment authorization program changes for drone RF links"
    value: true
  - claim: "PX4 / ArduPilot major version changes"
    value: true

excluded_claim_classes:
  - "FAA Part 107 airworthiness, operator certification, or UAS registration proof"
  - "EASA UAS class or open-category compliance proof"
  - "Remote ID product approval or compliance proof"
  - "DO-254 airborne hardware assurance, DAL assignment, or compliance proof"
  - "GNSS accuracy, fix rate, RTK precision, or anti-jamming/spoofing proof"
  - "RF link range, EIRP, anti-interference, or link-budget claims"
  - "Flight endurance, range, payload capacity, speed, or autonomy claims"
  - "BVLOS or swarm-control performance claims"
  - "Cost, lead-time, and yield claims"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `drone PCB`, `UAV PCB`, `flight controller board`, `ESC board`, `FPV board`, `drone PCBA` |
| **Page Type** | `query` |
| **Search Intent** | Drone/UAV hardware, flight controller PCBs, ESC boards, drone manufacturing |
| **Target Reader** | Drone engineers, UAV platform designers, commercial UAV integrators, FPV/racing drone builders |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` — board-class vocabulary and regulatory-identity framing supported; airworthiness, GNSS accuracy, RF performance, and autonomy claims blocked.

> **Routing note**: This pack covers civilian/commercial drone content. For defense/military UAV (ISR, EW, MIL-STD): use `wiki/consumption/defense-ew-surveillance-evidence-pack.md`.
> **Trust-bar flags**: "Flight-Ready", "Weight Optimized", "Vibration Tested" are marketing framing — NOT airworthiness or qualification proof.

---

## 3. Board Families (Evidence Scope)

### 3.1 Flight Controller / Autopilot

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Flight computer, autopilot board, quadcopter/VTOL/fixed-wing controller context |
| Component vocabulary | MCU/SoC/IMU/magnetometer/barometer/GNSS integration layout vocabulary |
| Format vocabulary | Standard form-factor (20×20 mm, 30.5×30.5 mm stack) vocabulary |
| Control-stack identity | PX4, ArduPilot architecture-identity vocabulary (not performance proof) |
| Flight accuracy, loop frequency, determinism proof, airworthiness | ❌ Blocked |

### 3.2 ESC / Power Distribution (PDB)

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Electronic speed controller, power distribution board context |
| Design vocabulary | High-current copper weight/trace width/thermal via vocabulary |
| Circuit vocabulary | MOSFET array/driver IC/current-sense/protection layout vocabulary |
| EMI vocabulary | EMI/noise reduction context for motor drive boards |
| Efficiency, braking performance, motor compatibility proof | ❌ Blocked |

### 3.3 Communication / RF / Navigation

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | RC receiver, telemetry radio, VTX board, GNSS module board context |
| Frequency context | 2.4 GHz / 900 MHz / 1.2 GHz — architecture-level context only (no range, EIRP) |
| Protocol identity | ExpressLRS, MAVLink, CRSF/ELRS — architecture identity vocabulary |
| GNSS vocabulary | GNSS/GLONASS/BeiDou/Galileo multi-constellation module board vocabulary |
| Antenna vocabulary | Antenna feed network/ground-plane vocabulary |
| RF range, link quality, GNSS accuracy, fix rate, anti-jamming proof | ❌ Blocked |

### 3.4 Payload / Gimbal Control

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Gimbal controller, LiDAR interface, thermal camera board, payload power/control PCB context |
| Circuit vocabulary | Gimbal motor driver/IMU/control logic vocabulary |
| Interface vocabulary | HDMI/CSI/MIPI/analog camera interface vocabulary |
| Stabilization accuracy, payload lift, imaging quality proof | ❌ Blocked |

### 3.5 Battery / BMS / Charging

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | LiPo/Li-ion BMS PCB, charging hub/docking station PCB context |
| BMS vocabulary | Cell monitoring/balancing/protection board description |
| Power vocabulary | AC-DC/DC-DC power rail distribution vocabulary |
| Flight time, energy density, cycle life, charging speed proof | ❌ Blocked |

### 3.6 Ground Control / Remote Controller

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | RC handheld, GCS board, base station, repeater PCB context |
| UI vocabulary | Joystick/button/touchscreen/indicator board vocabulary |
| RF identity | RF/Wi-Fi/cellular module integration (identity-level only) |
| RF link range, control latency, redundancy proof | ❌ Blocked |

### 3.7 Navigation Support (GNSS / IMU Boards)

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | GNSS module PCB, compass/magnetometer board, RTK positioning board — hardware context |
| Module vocabulary | RTK board hardware vocabulary (NOT accuracy, fix-rate, or jamming-resistance claims) |
| GNSS accuracy, CEP, RTK precision, jamming resistance proof | ❌ Blocked |

---

## 4. Regulatory Context (Identity Only — from P4-189 Official-Depth Card)

| Regulation | Safe Use | Blocked Use |
|---|---|---|
| **FAA Part 107** | Small UAS rule identity; operator certification context vocabulary; registration requirement framing | Airworthiness proof, operator certification status, waiver approval |
| **FAA Remote ID** | Remote ID rule identity; broadcast requirement framing vocabulary | Remote ID product approval, compliance declaration |
| **EASA UAS (Open Category)** | EASA UAS open-category identity; CE class label framing vocabulary | Class compliance proof, EASA authorization |
| **FCC Equipment Authorization** | FCC authorization identity for drone RF links | FCC ID proof, RF compliance declaration |
| **GNSS / RTK (public identity)** | Multi-constellation receiver architecture vocabulary; RTK hardware-board context | Positioning accuracy, fix rate, jamming resistance proof |

---

## 5. Control-Stack Identity (Architecture Level Only)

| Stack | Safe Use | Blocked Use |
|---|---|---|
| **PX4** | Open-source autopilot platform identity; flight-stack architecture vocabulary | Performance proof, flight-mode reliability, certification |
| **ArduPilot** | Open-source autopilot platform identity; architecture vocabulary | Performance proof, commercial endorsement |
| **MAVLink** | UAV communication protocol identity; ground-to-air messaging vocabulary | Protocol compliance, latency, reliability proof |
| **ExpressLRS** | RC link protocol identity; 2.4 GHz / 900 MHz control-link architecture vocabulary | RF range, link quality, or anti-interference proof |

---

## 6. Civilian vs Defense Separation

| Context | Correct Pack |
|---|---|
| Consumer/hobbyist drones, FPV racing | This pack |
| Commercial agricultural / logistics UAVs | This pack |
| Industrial inspection UAVs | This pack |
| Commercial delivery drones (non-BVLOS claim) | This pack |
| Defense / military ISR UAVs | `defense-ew-surveillance-evidence-pack.md` |
| Defense drone EW / surveillance payload | `defense-ew-surveillance-evidence-pack.md` |

---

## 7. Allowed vs Blocked

### 7.1 Allowed (Board-Class and Regulatory-Identity Context)

| Claim Pattern | Example |
|---|---|
| Board-class naming | "Drone flight controllers integrate MCU/SoC, IMU, barometer, magnetometer, and GNSS in a compact multilayer board" |
| Regulatory-identity framing | "Commercial drone operations in the US reference FAA Part 107 requirements; the PCB provides the hardware platform for the aircraft" |
| Control-stack identity | "PX4 and ArduPilot are open-source autopilot frameworks providing the flight-stack architecture context for flight controller PCB design" |
| RF frequency context | "Drone RC links typically operate at 2.4 GHz or 900 MHz — the PCB provides the RF front-end and antenna interface layer" |

### 7.2 Blocked (Certification / Performance / Compliance)

| Blocked Claim | Reason |
|---|---|
| "FAA Part 107 compliant drone PCB" | FAA Part 107 certifies the operator and aircraft; the PCB alone is not the regulatory unit |
| "Remote ID compliant broadcast module" | Remote ID compliance requires device-level broadcast testing and FAA module approval |
| "RTK accuracy: ±2 cm" | RTK accuracy is a receiver + correction service + environmental outcome, not a PCB claim |
| "30-minute flight endurance" | Endurance is a system-level metric (battery + motors + payload + conditions) |
| "BVLOS capable autopilot board" | BVLOS authority requires FAA waiver for the complete aircraft operation |

---

## 8. Handoff

**Core Answer**:

> Civilian drone/UAV PCBs are addressed through 7 board families at board-class vocabulary level plus regulatory-identity framing for FAA Part 107, Remote ID, EASA UAS, and FCC equipment authorization. Control-stack vocabulary (PX4, MAVLink, ExpressLRS) is supported at architecture-identity level. GNSS vocabulary is hardware-board context only. Airworthiness, flight performance, GNSS accuracy, RF link-budget, and BVLOS claims are blocked.

**Safe Reusable Shapes**:

- "Drone PCB families (flight controller, ESC, comm/RF, gimbal, BMS, GCS) each create distinct board-level design requirements — compact weight-sensitive stackups, high-current power distribution, mixed-signal RF/sensor integration."
- "FAA Part 107 and EASA UAS frameworks are the regulatory context — they govern who can fly and where; the PCB is the hardware platform that must function within those constraints."
- "PX4, MAVLink, and ExpressLRS are open-source platform identities — naming them describes the software/protocol architecture; it does not certify the board's performance or compatibility."

---

## 9. Pre-flight

- [x] Drone/UAV wiki boundary page referenced
- [x] Application fact card referenced (`facts/applications/drone-uav-coverage-gap-map.md`)
- [x] P4-189 official regulatory depth card referenced (`facts/standards/drone-uav-official-regulatory-depth.md`)
- [x] All 7 fact_ids from existing landed records — no new records required
- [x] All 5 source_ids from existing landed registry records
- [x] Trust-bar marketing labels flagged (Flight-Ready, Weight Optimized, Vibration Tested)
- [x] Civilian vs defense UAV separation explicitly documented
- [x] `must_refresh` items identified for FAA/EASA rule revisions, FCC program changes

**Verdict**: ✅ `go_now_conservative` — civilian board-class vocabulary and regulatory-identity context. Exclude all airworthiness, GNSS accuracy, RF performance, autonomy, and BVLOS claims.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
