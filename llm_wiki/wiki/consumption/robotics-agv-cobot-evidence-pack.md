# Robotics / AGV / Cobot PCB Evidence Pack

**Pack ID**: `consumption-robotics-agv-cobot`
**Date**: 2026-05-03
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Robotics / AGV / Cobot PCB/PCBA (industrial robot, cobot, AGV/AMR, service robot, mobile platform)"
scope: |
  Conservative evidence pack for robotics, AGV, and cobot PCB/PCBA content.

  Supports board-class and execution-context vocabulary for 7 board families:
  robot controller/main board, servo drive/motor control/power stage,
  sensor/perception/feedback, communication/fieldbus/gateway, HMI/teach pendant,
  safety IO/E-stop/expansion, and battery/BMS/power/charging.

  Protocol vocabulary (CAN, EtherCAT, PROFINET, Modbus, Ethernet/IP, Wi-Fi,
  Bluetooth) at identity level only. Trust-bar labels ("Field-Proven",
  "Deterministic", "Vibration Resistant") are marketing framing only.
  Safety IO section language is manufacturing support, not SIL/PL certification.

  No robot safety compliance, payload/accuracy/speed proof, SIL/PL certification,
  or AGV navigation performance claims.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Application boundary
  - "applications-robotics-coverage-gap-map"

  # Control / review gates
  - "methods-industrial-robotics-control-review-gates-and-claim-boundary"
  - "methods-pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary"

  # Test selection
  - "methods-pcba-flying-probe-vs-ict-selection-posture"

  # BGA / X-ray
  - "methods-low-void-bga-conservative-generation-gate"
  - "methods-low-void-bga-dfm-to-process-review"
  - "methods-hidden-joint-xray-inspection-boundary"

  # Assembly gates
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-npi-to-mass-production-gates"

source_ids:
  - "frontendapt-industry-robotics-page-en"
  - "frontendapt-dfm-guidelines-resource-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"

wiki_framing_support:
  - "wiki/applications/robotics-agv-cobot-pcb-pcba-boundary-map"
  - "wiki/applications/robotics-standards-routing-boundary"

must_refresh:
  - claim: "ISO 10218 / ISO 15066 standard revision or cobot safety requirement updates"
    value: true
  - claim: "Fieldbus conformance program status (EtherCAT, PROFINET)"
    value: true
  - claim: "Wireless qualification for mobile robots (Wi-Fi, cellular)"
    value: true

excluded_claim_classes:
  - "ISO 10218 / ISO 15066 robot safety compliance proof"
  - "Robot payload, speed, accuracy, or repeatability performance proof"
  - "SIL/PL functional safety certification for E-stop or safety circuits"
  - "AGV/AMR navigation accuracy, obstacle avoidance, or fleet routing proof"
  - "Protocol conformance certification (EtherCAT, PROFINET, Modbus)"
  - "Deployment volume, customer satisfaction, or field-reliability proof"
  - "Cost, lead-time, and yield claims"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `robotics PCB`, `robot controller board`, `AGV PCB`, `cobot PCB`, `servo drive board`, `AMR electronics` |
| **Page Type** | `query` |
| **Search Intent** | Industrial robot electronics, cobot hardware, AGV/AMR boards, servo drive PCBs, robot controller manufacturing |
| **Target Reader** | Robotics engineers, automation hardware designers, AGV/AMR platform developers |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` — board-class execution context vocabulary supported; robot safety compliance, performance proof, and SIL/PL certification blocked.

> **Important flags**:
> - Trust-bar labels in source ("Field-Proven", "Deterministic", "Vibration Resistant") are marketing framing — NOT lot-level qualification proof.
> - Safety IO section language ("designed according to your functional safety architecture") means manufacturing support for customer-designed safety boards — NOT SIL/PL certification.

---

## 3. Board Families (Evidence Scope)

### 3.1 Robot Controller / Main Board

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Industrial robot, cobot, AGV/AMR central controller, CPU/SoC mainboard, motion controller board context |
| Routing vocabulary | Multilayer MCU/SoC/FPGA/memory routing, multi-bus industrial communication interface |
| Interface vocabulary | CAN/EtherCAT/PROFINET/Modbus identity vocabulary, analog/digital IO with isolation |
| Format vocabulary | Backplane and modular controller board format |
| Real-time determinism proof, ISO 10218 compliance, processing performance claims | ❌ Blocked |

### 3.2 Servo Drive / Motor Control / Power Stage

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Joint servo amplifier, BLDC/stepper driver, traction drive, wheel drive board context |
| Design vocabulary | High-current/high-voltage creepage/clearance description (vocabulary, not thresholds) |
| Component vocabulary | MOSFET/IGBT/gate driver/current sensor/snubber layout context |
| Feedback vocabulary | Encoder/resolver/Hall feedback interface vocabulary |
| Exact efficiency, dynamic performance, payload proof | ❌ Blocked |

### 3.3 Sensor / Perception / Feedback

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | IMU/odometry, encoder interface, LiDAR/radar interface, 3D camera/depth, sensor fusion board context |
| Interface vocabulary | MIPI/CSI/USB/Ethernet camera interface vocabulary |
| Board context | Sensor fusion + pre-processing board description; mechanical integration vocabulary |
| Sensor accuracy, detection range, perception performance proof | ❌ Blocked |

### 3.4 Communication / Fieldbus / Gateway

| Aspect | Evidence Support |
|--------|-----------------|
| Protocol identity | CAN/CANopen/EtherCAT/PROFINET/Modbus/Ethernet-IP/Wi-Fi/Bluetooth/cellular — identity-level vocabulary |
| Board-class vocabulary | Gateway PCB, industrial Ethernet board, wireless fleet communication board context |
| Protection vocabulary | Isolation/surge/EMI filtering at communication ports |
| Protocol conformance, interoperability certification, cycle-time guarantees | ❌ Blocked |

### 3.5 HMI / Teach Pendant / Robot Panel

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Teach pendant, handheld HMI, robot panel, indicator/display board context |
| Display vocabulary | LCD/TFT/touchscreen/keypad display interface vocabulary |
| E-stop vocabulary | E-stop button and safety circuit integration (manufacturing support vocabulary only) |
| SIL/PL certification for E-stop, safety function proof | ❌ Blocked |

### 3.6 Safety IO / Emergency Stop / Expansion

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Safety IO module, E-stop relay PCB, safety interlock, expansion IO board context |
| Circuit vocabulary | Optocoupler/surge/status LED/diagnostic circuit vocabulary |
| Manufacturing framing | Customer-design-basis manufacturing support only — NOT SIL/PL certification |
| SIL/PL functional safety certification for these boards | ❌ Blocked — manufacturing support ≠ safety certification |

### 3.7 Battery / BMS / Power / Charging

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | AGV/AMR BMS, DC-DC converter, power distribution, docking/inductive charger board context |
| BMS vocabulary | Li-ion/LiFePO4 cell monitoring/balancing/protection board description |
| Power vocabulary | DC-DC power distribution routing, over-current/over-voltage/thermal protection vocabulary |
| Battery capacity, energy density, cycle life, or charging performance proof | ❌ Blocked |

---

## 4. Protocol Vocabulary (Identity Only)

| Protocol | Safe Use | Blocked Use |
|---|---|---|
| **CAN / CANopen** | Bus-family identity; robot joint communication context | Protocol timing, error-frame behavior, conformance |
| **EtherCAT** | Real-time industrial Ethernet identity; robot motion network context | Conformance certification, cycle-time guarantees |
| **PROFINET** | Industrial Ethernet identity; factory automation context | PI conformance test, RT/IRT class claims |
| **Modbus / Ethernet/IP** | Protocol family identity; fieldbus integration vocabulary | Interoperability proof, conformance test |
| **Wi-Fi / Bluetooth / Cellular** | Wireless communication identity for mobile robot context | RF performance, certification, coverage proof |

---

## 5. Marketing Framing Flags

| Source Label | Status | What It Does NOT Unlock |
|---|---|---|
| "Field-Proven" (trust bar) | Marketing framing only | Field deployment count, MTBF, or reliability proof |
| "Deterministic" (trust bar) | Marketing framing only | Real-time determinism specification, cycle-time guarantee |
| "Vibration Resistant" (trust bar) | Marketing framing only | Vibration qualification test, g-force rating proof |
| "Designed according to your functional safety architecture" (safety IO) | Manufacturing support framing | SIL/PL certification of the PCB or safety function |

---

## 6. Routing Notes

- **Generic industrial-control routing** (servo drives, IO modules, fieldbus not specific to robotics): use `wiki/consumption/industrial-control-evidence-pack.md`
- **Automotive-context motor control / BMS** (EV traction, vehicle BMS): use `wiki/consumption/automotive-ev-evidence-pack.md`
- **Sensor front-end depth** (IMU, LiDAR interface, camera): use `wiki/consumption/sensor-navigation-imaging-evidence-pack.md`

---

## 7. Allowed vs Blocked

### 7.1 Allowed (Board-Class and Context)

| Claim Pattern | Example |
|---|---|
| Board-class naming | "Robot controller boards combine CPU/SoC processing, multi-bus communication, and analog/digital IO on dense multilayer PCBs" |
| Platform context | "Cobot and AGV/AMR platforms require servo drive, sensor, communication, and BMS boards as distinct PCB families" |
| Manufacturing context | "Robot electronics benefit from layered inspection (SPI→AOI→X-ray→ICT/FP→FCT) and board-level traceability for fleet-level quality tracking" |
| Safety board framing | "Safety IO and E-stop boards are manufactured to the customer's functional safety architecture — the PCB supplier provides manufacturing support" |

### 7.2 Blocked (Safety / Performance / Compliance)

| Blocked Claim | Reason |
|---|---|
| "ISO 10218 compliant robot controller" | Robot safety compliance is a system/integration-level certification |
| "SIL-2 E-stop relay PCB" | SIL rating requires full functional safety analysis of the complete safety function |
| "AGV navigation accuracy: ±5 mm" | Navigation accuracy is a system-level metric, not a PCB specification |
| "Cobot payload: 10 kg" | Payload is a robot mechanical/motor system specification |

---

## 8. Handoff

**Core Answer**:

> Robotics, AGV, and cobot PCBs are addressed through 7 board families at board-class execution-context level. The current evidence supports design vocabulary, protocol-identity framing, layered inspection descriptions, and manufacturing-control posture. Safety IO and E-stop boards are covered as manufacturing support only — not SIL/PL certification. Performance claims (payload, accuracy, navigation) and robot safety compliance are blocked.

**Safe Reusable Shapes**:

- "Robot electronics separate into distinct PCB families: controller, servo drive, sensor/perception, communication, HMI, safety IO, and BMS/power — each with distinct layout and interface requirements."
- "Safety IO and E-stop boards are manufactured to the customer's design — the PCB supplier's role is manufacturing discipline, not functional safety certification."
- "Protocol names (EtherCAT, PROFINET, CAN) describe the robot network communication context — conformance and interoperability require device-level testing beyond the PCB."

---

## 9. Pre-flight

- [x] Robotics wiki boundary page referenced
- [x] Application fact card referenced (`facts/applications/robotics-coverage-gap-map.md`)
- [x] All 9 fact_ids from existing landed records — no new records required
- [x] All 8 source_ids from existing landed registry records
- [x] Marketing framing labels explicitly flagged
- [x] Safety IO manufacturing-support framing explicitly separated from SIL/PL certification
- [x] Overlap routing to industrial-control, automotive, and sensor packs included
- [x] `must_refresh` items identified for ISO 10218 revisions and conformance programs

**Verdict**: ✅ `go_now_conservative` — board-class vocabulary and manufacturing context. Exclude all robot safety compliance, performance proof, SIL/PL certification, and navigation accuracy claims.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
