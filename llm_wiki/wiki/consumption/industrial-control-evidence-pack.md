# Industrial Control PCB Evidence Pack

**Pack ID**: `consumption-industrial-control`
**Date**: 2026-05-03
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Industrial Control PCB/PCBA (PLC, servo/VFD, IO modules, HMI/IPC, fieldbus/gateway, industrial power/safety)"
scope: |
  Conservative evidence pack for industrial-control PCB/PCBA content.

  Supports board-class and execution-context vocabulary for 6 board families:
  PLC/control cabinet, motion/servo/VFD, IO modules/field sensors, HMI/IPC,
  industrial networking/fieldbus/gateway, and industrial power/safety controller.

  Fieldbus and protocol vocabulary (Modbus, PROFIBUS, CAN, EtherCAT, PROFINET,
  Ethernet/IP) at identity level only. "Functional safety" source mention is
  marketing framing — does NOT unlock SIL, PL, or IEC 62061 claims.

  No IEC 61131 compliance, SIL/PL certification, MTBF, protocol conformance proof.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Application boundary
  - "applications-industrial-control-coverage-gap-map"

  # Industrial control method cards
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
  - "frontendapt-industry-industrial-control-page-en"
  - "frontendapt-dfm-guidelines-resource-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"

wiki_framing_support:
  - "wiki/applications/industrial-control-pcb-pcba-boundary-map"
  - "wiki/applications/industrial-control-standards-routing-boundary"

must_refresh:
  - claim: "Fieldbus protocol version or conformance program updates (EtherCAT, PROFINET)"
    value: true
  - claim: "IEC 61131 or functional-safety standard revision claims"
    value: true
  - claim: "Industrial networking certification or interoperability test program status"
    value: true

excluded_claim_classes:
  - "IEC 61131-3 programming compliance or SIL/PL certification"
  - "ISO 13849 / IEC 62061 functional safety compliance or PL/SIL assignment"
  - "24/7 uptime, MTBF, DPPM, or field-failure rate claims"
  - "EMC compliance proof (CISPR 11, IEC 61000-4 series)"
  - "Fieldbus/protocol interoperability, conformance certification, or integration-test proof"
  - "Exact creepage/clearance/insulation compliance values for safety categories"
  - "Cost, lead-time, and yield claims"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `industrial PCB`, `PLC PCB`, `servo drive PCB`, `HMI board`, `fieldbus PCB`, `industrial control board` |
| **Page Type** | `query` |
| **Search Intent** | Industrial automation hardware, PLC board manufacturing, servo/VFD PCBs, factory automation electronics |
| **Target Reader** | Industrial automation engineers, factory hardware designers, motion control engineers, IPC/HMI designers |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` — board-class and protocol-identity vocabulary supported; SIL/PL certification, protocol conformance, and MTBF claims blocked.

> **Important flag**: The Tier-2 source includes "functional safety" in marketing vocabulary. This does NOT unlock SIL, PL, IEC 62061, or ISO 13849 compliance claims. Use board-design-context vocabulary only.

---

## 3. Board Families (Evidence Scope)

### 3.1 PLC / Control Cabinet

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | PLC mainboard, CPU board, IO card, backplane, communication module board context |
| Layout vocabulary | Modular PLC format, mixed-signal/noise-separation layout, optocoupler/isolation/surge protection vocabulary |
| Mechanical format | DIN-rail mechanical format vocabulary |
| IEC 61131-3 compliance, SIL/PL certification, 24/7 uptime proof | ❌ Blocked |

### 3.2 Motion / Servo / VFD

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Servo drive, VFD, stepper/BLDC driver, CNC axis controller board context |
| Design vocabulary | High-current/high-voltage creepage/clearance description (vocabulary only, not thresholds) |
| Power stage vocabulary | IGBT/MOSFET/gate driver/current sensor integration context |
| Feedback vocabulary | Encoder/resolver feedback routing vocabulary |
| EMC layout vocabulary | EMC-aware layout context |
| Exact creepage/clearance thresholds, efficiency proof, drive qualification | ❌ Blocked |

### 3.3 IO Modules / Field Sensors

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Digital/analog IO module, sensor interface, signal conditioning, distributed IO board context |
| Signal vocabulary | Multi-channel IO density, isolation/surge/protection integration |
| Interface vocabulary | 4–20 mA / 0–10 V / thermocouple conditioning vocabulary |
| Connector vocabulary | Terminal block / M8/M12 connector layout context |
| IO accuracy, signal quality proof, SIL compliance | ❌ Blocked |

### 3.4 HMI / Industrial PC

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | HMI panel, keypad, touchscreen controller, industrial PC mainboard, interface card context |
| Display vocabulary | LCD/TFT, LVDS/MIPI, backlight driver, capacitive/resistive touch vocabulary |
| IPC vocabulary | IPC mainboard, IO/fieldbus card board description |
| IP rating, shock/vibration qualification, operating-temperature proof | ❌ Blocked |

### 3.5 Industrial Networking / Fieldbus / Gateway

| Aspect | Evidence Support |
|--------|-----------------|
| Protocol identity vocabulary | Modbus / PROFIBUS / CAN / CANopen / DeviceNet / EtherCAT / PROFINET / Ethernet/IP — identity-level naming only |
| Board-class vocabulary | Fieldbus PCB, industrial Ethernet, protocol converter, edge gateway, data logger board context |
| Protection vocabulary | Isolation transformer, surge protection, EMI filter at communication ports |
| Protocol conformance proof, interoperability certification, integration-test results | ❌ Blocked |

### 3.6 Industrial Power / Safety Controller

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | AC-DC PSU, DC-DC converter, relay board, contactor driver, safety PLC, interlock controller board context |
| Layout vocabulary | AC-DC/DC-DC power stage layout vocabulary, creepage/clearance/slot design description |
| Relay vocabulary | Relay/contactor drive with suppression vocabulary |
| SIL/PL compliance, safety PLC certification, relay MTTF/MTTFd proof | ❌ Blocked |

---

## 4. Protocol Vocabulary (Identity Only)

| Protocol | Safe Use | Blocked Use |
|---|---|---|
| **Modbus** | Protocol family identity; serial RS-485/TCP context vocabulary | Conformance proof, interoperability test, implementation compliance |
| **PROFIBUS** | Protocol family identity; industrial serial network vocabulary | PI certification, conformance test, interoperability proof |
| **CAN / CANopen / DeviceNet** | Protocol family identity; fieldbus network context | CAN FD timing, DeviceNet certification, protocol compliance |
| **EtherCAT** | Protocol family identity; real-time industrial Ethernet context | EtherCAT conformance certification, cycle-time guarantees |
| **PROFINET** | Protocol family identity; industrial Ethernet context | PI conformance test, PROFINET certification, cycle-time guarantees |
| **Ethernet/IP** | Protocol family identity; EtherNet/IP industrial context | ODVA conformance, interoperability proof |

---

## 5. Context Vocabulary Notes (Marketing Framing — Not Unlocked)

| Source Mention | Status | What It Does NOT Unlock |
|---|---|---|
| "Functional safety" (hero vocabulary in Tier-2 source) | Marketing framing only | SIL levels, PL categories, IEC 62061, ISO 13849 compliance claims |
| "-55 to 125 °C thermal shock" (trust bar in Tier-2 source) | Capability-context only | Lot-level qualification proof, environmental certification |

---

## 6. Allowed vs Blocked

### 6.1 Allowed (Board-Class and Protocol-Identity Context)

| Claim Pattern | Example |
|---|---|
| Board-class naming | "PLC boards combine CPU, IO, communication, and power supply modules in modular form factors" |
| Protocol identity framing | "Industrial control networks reference protocols such as EtherCAT, PROFINET, and Modbus — the board provides the physical communication interface layer" |
| Design consideration vocabulary | "Servo drive PCBs combine high-voltage power stage and low-voltage control circuitry, requiring careful isolation and EMC layout planning" |
| Test gate framing | "Industrial control boards benefit from layered test approaches: SPI, AOI, X-ray for BGA/QFN, ICT or flying probe, and FCT" |

### 6.2 Blocked (Compliance / Certification / Reliability)

| Blocked Claim | Reason |
|---|---|
| "IEC 61131-3 compliant PLC firmware" | IEC 61131-3 is a programming language standard — board manufacturing does not create this compliance |
| "SIL-2 rated safety controller" | SIL rating is a system-level functional safety outcome requiring full IEC 62061/ISO 13849 analysis |
| "EtherCAT conformance certified" | Conformance certification requires EtherCAT Technology Group testing of the complete device |
| "MTBF: 100,000 hours" | MTBF is a system-level reliability metric requiring specific methodology and conditions |

---

## 7. Handoff

**Core Answer**:

> Industrial control PCBs are addressed through 6 board families at board-class execution-context level. The current evidence supports design vocabulary, protocol-identity framing, and layered test approach descriptions. Fieldbus and safety-standard vocabulary is limited to identity-level only. "Functional safety" source mentions are marketing vocabulary, not SIL/PL unlocks.

**Safe Reusable Shapes**:

- "Industrial fieldbus names (EtherCAT, PROFINET, Modbus, CAN) describe the communication protocol context — the PCB provides the physical interface layer, but conformance and interoperability require device-level testing."
- "PLC and servo drive boards combine high-voltage power stages with low-voltage control electronics — design discipline at the isolation, layout, and test boundary is the core manufacturing value."
- "Layered test approaches (SPI→AOI→X-ray→ICT/flying probe→FCT) are the industrial-control quality-assurance vocabulary, not lot-level pass/fail guarantees."

---

## 8. Pre-flight

- [x] Industrial control wiki boundary page referenced
- [x] Application fact card referenced (`facts/applications/industrial-control-coverage-gap-map.md`)
- [x] All 9 fact_ids from existing landed records — no new records required
- [x] All 8 source_ids from existing landed registry records
- [x] Fieldbus vocabulary limited to identity-level
- [x] "Functional safety" source mention flagged as marketing framing — not SIL/PL unlock
- [x] Thermal-shock context vocabulary flagged as capability-context only
- [x] `must_refresh` items identified for fieldbus conformance programs and standard revisions

**Verdict**: ✅ `go_now_conservative` — board-class and protocol-identity vocabulary. Exclude all SIL/PL certification, protocol conformance, MTBF, and EMC compliance claims.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
