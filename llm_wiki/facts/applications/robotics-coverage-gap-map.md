---
fact_id: "applications-robotics-coverage-gap-map"
title: "Robotics application coverage gap map: which board families have wiki-layer routing and which remain overview-only"
topic: "Robotics PCB/PCBA application coverage"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-160 initial build; sourced from frontendapt-industry-robotics-page-en (Tier-2), industrial-robotics-control-review-gates-and-claim-boundary, pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary, and industrial-robotics-control-rewrite-readiness-map"
source_ids:
  - "frontendapt-industry-robotics-page-en"
  - "frontendapt-dfm-guidelines-resource-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
tags: ["robotics", "agv", "amr", "cobot", "industrial-robot", "servo", "coverage-map", "gap-map"]
---

# Canonical Summary

> As of 2026-05-03 after P4-169 activation review, the robotics application family has a dedicated wiki boundary page (`wiki/applications/robotics-agv-cobot-pcb-pcba-boundary-map.md`) and that page is now `active`. Prior to P4-160, the segment was overview-only. The Tier-2 internal source supports board-class vocabulary for 7 board families across industrial robots, cobots, AGVs/AMRs, service robots, and mobile platforms. It does NOT prove ISO 10218 / ISO 15066 robot safety certification, functional safety (SIL/PL) for safety circuits, payload/accuracy/speed performance, or deployment-volume claims.

## Board Family Coverage State

### Supported at Scenario + Board-Class Level (Tier-2 Internal Source)

All entries below are extracted from `frontendapt-industry-robotics-page-en` (Tier-2). They support PCB/PCBA board-class vocabulary and engineering context only.

| Board Family | Application Context | PCB/PCBA Vocabulary Supported |
|---|---|---|
| **Robot Controller / Main Board** | Industrial robot, cobot, AGV/AMR central controller, CPU/SoC mainboard, motion controller | Multilayer MCU/SoC/FPGA/memory routing, multi-bus industrial communication interface (CAN/EtherCAT/PROFINET/Modbus), analog/digital IO with isolation, backplane and modular controller board format |
| **Servo Drive / Motor Control / Power Stage** | Joint servo amplifiers, BLDC/stepper drivers, traction drives, wheel drives | High-current/high-voltage creepage/clearance description, MOSFET/IGBT/gate driver/current sensor/snubber layout, encoder/resolver/Hall feedback interface, EMC-aware layout vocabulary |
| **Sensor / Perception / Feedback** | IMU/odometry, encoder interface, LiDAR/radar interface, 3D camera/depth, sensor fusion | Low-noise sensor front-end layout, MIPI/CSI/USB/Ethernet camera interface, sensor fusion + pre-processing board description, mechanical integration for arm/mobile-base mounting |
| **Communication / Fieldbus / Gateway** | Industrial Ethernet, fieldbus, wireless fleet comms, edge/cloud gateway | CAN/CANopen/EtherCAT/PROFINET/Modbus/Ethernet-IP/Wi-Fi/Bluetooth/cellular identity vocabulary, isolation/surge/EMI filtering at comm ports, gateway PCB board format |
| **HMI / Teach Pendant / Robot Panel** | Teach pendant, handheld HMI, robot panel, indicator/display boards | LCD/TFT/touchscreen/keypad display interface, teach pendant mechanical/electrical design, E-stop button and safety circuit integration (manufacturing support only), LED/buzzer/haptic |
| **Safety IO / Emergency Stop / Expansion** | Safety IO modules, E-stop relay PCBs, safety interlocks, standard IO, end-effector tool interface | E-stop/safety relay/interlock PCB description (customer-design basis), digital/analog IO module, optocoupler/surge/status LED/diagnostic circuit vocabulary |
| **Battery / BMS / Power / Charging** | AGV/AMR BMS, DC-DC converter, power distribution, docking/inductive charger | BMS PCB for Li-ion/LiFePO4 (cell monitoring/balancing/protection), DC-DC power distribution routing, dock/charger PCB board description, over-current/over-voltage/thermal protection |

### Process / Test Coverage Already Landed (Methods Fact Cards)

| Capability | Supporting Fact Card |
|---|---|
| DFM / DFT / DFA review gates for robotics / control boards | `methods-industrial-robotics-control-review-gates-and-claim-boundary` |
| Flying probe vs ICT for robotics/control PCBs | `methods-pcba-flying-probe-vs-ict-selection-posture` |
| Inspection / test / reliability evidence separation | `methods-pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary` |
| Low-void BGA process planning on robot controller boards | `methods-low-void-bga-conservative-generation-gate`, `methods-low-void-bga-dfm-to-process-review` |
| Hidden-joint X-ray for dense robot controller/drive boards | `methods-hidden-joint-xray-inspection-boundary` |

### Quality/Test Steps Supported (Tier-2 Internal Source)

- SPI → AOI → X-ray (BGA/LGA/QFN) → ICT/flying-probe → FCT → final inspection + traceability
- Lot-level or board-level traceability for fleet-level quality tracking (description level only)

## Stable Facts

- The Tier-2 internal robotics source covers 7 board families: robot controller/main board, servo drive/motor control, sensor/perception/feedback, communication/fieldbus/gateway, HMI/teach pendant, safety IO/E-stop/expansion, and battery/BMS/power/charging.
- The source uses `"Field-Proven"`, `"Deterministic"`, `"Vibration Resistant"` trust-bar labels; these are marketing framing, NOT lot-level qualification proof.
- The safety IO section uses "designed according to your functional safety architecture" language; this means manufacturing support for customer-designed safety boards — NOT SIL/PL certification.
- Protocol vocabulary (CAN, EtherCAT, PROFINET, Modbus, Ethernet/IP, Wi-Fi, Bluetooth) is identity-level only; conformance or interoperability proof is blocked.
- Robotics overlaps with industrial control (servo drives, IO modules, fieldbus) — use `wiki/applications/industrial-control-pcb-pcba-boundary-map.md` for generic industrial-control routing and this page for robotics-specific platform context.
- Robotics overlaps with automotive/EV (BMS, DC-DC, motor control) — use `wiki/applications/automotive-ev-pcb-pcba-boundary-map.md` for automotive-context motor-control routing and this page for robotics-context.

## Conditions And Methods

- Use this card to confirm what board-family vocabulary is safe before writing a robotics PCB article.
- For protocol identity depth, confirm identity-only use; do NOT advance to conformance.
- Update `last_reconciled_at` when new robotics-specific wiki boundary pages or official standard sources are added.

## Limits And Non-Claims

- ISO 10218 (industrial robot safety) or ISO 15066 (cobot safety) compliance is NOT supported.
- Robot payload, speed, accuracy, repeatability, or dynamic performance proof is NOT supported.
- SIL/PL functional safety certification for E-stop or safety circuits is NOT supported.
- AGV/AMR navigation accuracy, obstacle avoidance performance, or fleet routing proof is NOT supported.
- Deployment volume, customer satisfaction, or field-reliability outcome proof is NOT supported.
- Yield, throughput, cost, or lead-time claims are NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|-----|-----------------|
| ISO 10218 / ISO 15066 robot safety boundary | Official ISO source recovery |
| IEC 62061 / ISO 13849 functional safety for robot safety circuits | Official IEC/ISO functional safety source |
| Fieldbus conformance depth (EtherCAT, PROFINET) | ETG, PI official source recovery |
| Wireless qualification (Wi-Fi, Bluetooth, cellular for mobile robots) | Official certification body source |
| Dedicated robotics wiki page status | Reopen only if the page later regresses and requires demotion from `active` |
