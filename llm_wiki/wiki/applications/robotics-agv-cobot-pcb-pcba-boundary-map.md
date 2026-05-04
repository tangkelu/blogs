---
topic_id: "applications-robotics-agv-cobot-pcb-pcba-boundary-map"
title: "Robotics AGV Cobot PCB PCBA Boundary Map"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
activated_at: "2026-05-03"
activation_notes: "P4-169 review pass: boundary language stable, all 7 board families have safe/blocked pairs, standards context table complete, must-refresh and cross-lane routing present. Safety IO framing correctly states manufacturing support only. Promoted to active."
fact_ids:
  - "applications-robotics-coverage-gap-map"
  - "applications-application-coverage-gap-map"
  - "methods-industrial-robotics-control-review-gates-and-claim-boundary"
  - "methods-pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary"
  - "methods-pcba-flying-probe-vs-ict-selection-posture"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-low-void-bga-conservative-generation-gate"
  - "methods-hidden-joint-xray-inspection-boundary"
source_ids:
  - "frontendapt-industry-robotics-page-en"
  - "frontendapt-dfm-guidelines-resource-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
tags: ["robotics", "agv", "amr", "cobot", "industrial-robot", "servo", "bms", "safety-io", "pcb", "pcba", "boundary-map", "application-boundary"]
---

# Definition

> Robotics PCB/PCBA writing is safe at board-class, layout-context, and process-review vocabulary. It is unsafe when it crosses into ISO 10218/15066 robot safety compliance, SIL/PL functional safety certification for safety circuits, payload/speed/accuracy performance claims, or AGV/AMR navigation/fleet-routing outcomes. Use this page to navigate which angle is supportable for each robotics board family.

## Why This Topic Matters

- Robotics vocabulary (`field-proven`, `deterministic`, `vibration resistant`, `safety-rated E-stop`, `ISO 10218`, `cobot safe`) reads as performance or compliance proof when it is only marketing framing or context description.
- Robotics overlaps with industrial control (servo drives, IO modules, fieldbus), automotive/EV (BMS, motor control), and sensor/navigation (LiDAR, perception boards). This page establishes where robotics-specific vocabulary is valid and where cross-lane routing applies.
- Existing process/method fact cards (DFM/DFT, flying probe, test-vs-reliability) already cover significant ground for robotics board content — this page routes to them rather than duplicating.

---

## Board Family Routing

### Robot Controller / Main Board PCBs

**Safe angles:**
- Multilayer SoC/MCU/FPGA/memory routing vocabulary for motion control, kinematics, safety logic
- Multi-bus industrial communication interface vocabulary: CAN/CANopen, EtherCAT, PROFINET, Modbus, Ethernet/IP, serial links — identity-level only
- Robust IO and interface vocabulary: digital/analog IO, encoder interfaces, safety signal inputs, isolation/protection description
- Backplane and modular design vocabulary: plug-in motion/IO module, modular robot controller architecture description

**Blocked:**
- Real-time determinism guarantees, cycle-time, or jitter claims
- Robot kinematic accuracy, trajectory-following, or control-loop bandwidth claims
- ISO 10218 / ISO 15066 compliance for robot controller design
- Protocol conformance (EtherCAT, PROFINET) or interoperability proof

---

### Servo Drive / Motor Control / Power Stage PCBs

**Safe angles:**
- High-current/high-voltage design vocabulary: copper weights, creepage/clearance, isolation slot description
- Power stage integration vocabulary: MOSFET/IGBT, gate drivers, current sensors, shunts, snubbers, protection circuits description
- Feedback and control integration vocabulary: encoder/resolver/Hall sensor interface, current/voltage sensing for closed-loop control description
- EMC-aware layout vocabulary: routing, grounding, filtering for high-frequency switching in robot cabinets and mobile platforms

> **Overlap with industrial control:** For generic servo drive / VFD content, also consult `wiki/applications/industrial-control-pcb-pcba-boundary-map.md`. This page covers robotics-specific joint and traction drive contexts.

**Blocked:**
- Torque ripple, speed bandwidth, or positioning accuracy claims
- STO (safe torque off) functional safety compliance
- Exact creepage/clearance values as IEC 60664 compliance proof
- Drive efficiency, power loss, or thermal-rise performance claims

---

### Sensor / Perception / Feedback PCBs

**Safe angles:**
- Low-noise sensor front-end vocabulary: IMU/encoder/force-torque sensor PCB, analog layout and grounding description
- High-speed vision and LiDAR interface vocabulary: MIPI/CSI, USB, Ethernet, custom interface board description
- Sensor fusion and pre-processing board vocabulary: multi-sensor combination, data-near-sensor description
- Mechanical integration vocabulary: sensor board in robot arm, end-effector, mobile base, or housing; vibration and cable routing considerations

> **Overlap with sensor/navigation:** For radar/LiDAR RF front-end depth, consult `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md`.

**Blocked:**
- LiDAR range, point-cloud density, or angular resolution claims
- Camera resolution, frame rate, or imaging performance claims
- SLAM accuracy, map quality, or localization-error claims
- Sensor calibration stability or long-term drift claims

---

### Communication / Fieldbus / Gateway PCBs

**Safe angles:**
- Industrial communication protocol identity vocabulary: CAN/CANopen, EtherCAT, PROFINET, Modbus, Ethernet/IP naming (identity-level only)
- Wireless connectivity vocabulary: Wi-Fi, Bluetooth, cellular, proprietary RF module integration description (identity-level only)
- Gateway and edge controller vocabulary: protocol conversion and data aggregation PCB description
- Physical layer protection vocabulary: isolation transformer, surge protection, EMI filtering at communication ports

**Blocked:**
- Protocol conformance, certification, or interoperability proof
- Wi-Fi, Bluetooth, or cellular qualification (FCC/CE/RED) claims
- Wireless throughput, latency, or coverage claims
- Fleet coordination, cloud-sync, or OTA update reliability claims

---

### HMI / Teach Pendant / Robot Panel PCBs

**Safe angles:**
- Display and input integration vocabulary: LCD/TFT, touchscreen, keypad, joystick, E-stop button, function key PCB description
- Industrial-grade construction vocabulary: frequent handling, shock, vibration, dust/oil exposure considerations
- Communication and power interface vocabulary: cable/wireless link to robot controller, power and safety circuit on pendant board description
- User feedback vocabulary: LED, buzzer, haptic feedback PCB integration description

**Blocked:**
- E-stop category or safety-performance level (PLd, PLe, Cat.3/Cat.4) compliance claims for the pendant E-stop circuit
- Ergonomic compliance or human-factors certification claims
- IP ingress protection rating (IP54, IP65) proof

---

### Safety IO / Emergency Stop / Expansion PCBs

**Safe angles:**
- E-stop and safety relay circuit vocabulary: E-stop circuit, safety relay, interlock PCB description — framed as manufacturing support for customer-designed safety architecture
- Standard IO module vocabulary: digital/analog IO for external sensors, actuators, tooling
- End-effector tool interface board vocabulary: PCB on gripper, welding gun, suction, screwdriver tool
- Diagnostic circuit vocabulary: optocoupler, surge, status LED, diagnostic circuit description

**Blocked:**
- Safety Integrity Level (SIL) or Performance Level (PL) certification for safety circuits (IEC 62061, ISO 13849)
- ISO 10218 / ISO 15066 safety-function compliance for E-stop or safety-relay design
- Diagnostic coverage (DC) percentage claims
- Release authority for robot safety functions

---

### Battery / BMS / Power / Charging PCBs (Mobile Robots)

**Safe angles:**
- BMS PCB vocabulary: Li-ion/LiFePO4 cell monitoring, balancing, protection circuit description
- DC-DC and power distribution vocabulary: voltage rail conversion, power routing, component placement description
- Dock/charging station PCB vocabulary: plug-in and auto-docking charger board description
- Protection circuit vocabulary: over-current, over-voltage, under-voltage, short-circuit, thermal protection description

> **Overlap with automotive/EV:** For EV-context BMS and charger protocol claims, consult `wiki/applications/automotive-ev-pcb-pcba-boundary-map.md`.

**Blocked:**
- Battery capacity, runtime, cycle life, or energy density claims
- Charging speed, dock alignment accuracy, or wireless charging efficiency claims
- BMS SOC/SOH accuracy or pack-safety outcome claims
- Fleet runtime statistics or deployment reliability outcomes

---

## Process / Test Vocabulary

**Do not re-derive these boundaries here. Route to existing fact cards:**

| Topic | Route To |
|---|---|
| DFM / DFT / DFA review gates for robotics/control boards | `facts/methods/industrial-robotics-control-review-gates-and-claim-boundary.md` |
| Flying probe vs ICT for robotics PCBs | `facts/methods/pcba-flying-probe-vs-ict-selection-posture.md` |
| Test / inspection / reliability evidence separation | `facts/methods/pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary.md` |
| Low-void BGA process planning on robot controller / drive boards | `facts/methods/low-void-bga-conservative-generation-gate.md` + `facts/methods/low-void-bga-dfm-to-process-review.md` |
| Hidden-joint X-ray inspection | `facts/methods/hidden-joint-xray-inspection-boundary.md` |

---

## Standards Context

| Standard | Safe Use |
|---|---|
| `ISO 10218-1 / ISO 10218-2` | Industrial robot safety standard identity — NOT compliance proof |
| `ISO 15066` | Collaborative robot (cobot) safety standard identity — NOT compliance proof |
| `IEC 62061` | Machinery functional safety (SIL) standard identity — NOT compliance proof |
| `ISO 13849` | Safety of machinery / control systems (PL) standard identity — NOT compliance proof |
| `EtherCAT / PROFINET / CAN / CANopen` | Industrial communication protocol identity names — NOT conformance proof |

---

## Cross-Lane Routing

| Content Type | Route To |
|---|---|
| Generic industrial control boards (PLC, VFD, HMI, IO) | `wiki/applications/industrial-control-pcb-pcba-boundary-map.md` |
| Automotive/EV BMS and motor control (vehicle context) | `wiki/applications/automotive-ev-pcb-pcba-boundary-map.md` |
| Radar / LiDAR RF front-end depth | `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md` |
| DFM/DFT/DFA review language | `facts/methods/industrial-robotics-control-review-gates-and-claim-boundary.md` |
| Test / inspection / reliability boundary | `facts/methods/pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary.md` |
| Robot safety standards qualification boundary | `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md` (nearest applicable card) |

---

## Engineering Boundaries

- Treat all robotics board content as board-class and process-review stories, not as robot-safety certification or performance stories.
- Safety IO and E-stop boards: frame as manufacturing support for customer-designed functional safety architectures — NOT as certifying the safety function.
- Trust-bar marketing labels (`"Field-Proven"`, `"Deterministic"`, `"Vibration Resistant"`) must not appear in public content as performance specifications.
- Robot type names (industrial robot, cobot, AGV, AMR, service robot) are valid application-context labels; they do NOT change the blocked-claim boundaries.

---

## Common Misreadings

- `"Field-Proven"` trust-bar label → does NOT prove MTBF, deployment volume, or reliability statistics.
- `"Deterministic"` trust-bar label → does NOT prove real-time OS latency, EtherCAT cycle jitter, or control-loop bandwidth.
- `"Safety Ready"` or E-stop PCB manufactured → does NOT prove SIL/PL certification or ISO 10218/15066 compliance.
- Protocol name on robot controller PCB → does NOT prove EtherCAT/PROFINET conformance or interoperability with specific drives/sensors.
- BMS PCB for mobile robot → does NOT prove battery cycle-life, runtime, or fleet energy-management outcomes.
- Sensor/perception PCB manufactured → does NOT prove SLAM accuracy, LiDAR range, or camera resolution.

---

## Must Refresh Before Publishing

- Any ISO 10218 / ISO 15066 robot safety compliance or functional safety claims
- Any SIL, PL, diagnostic coverage, or IEC 62061 / ISO 13849 certification claims
- Any robot payload, speed, accuracy, repeatability, or trajectory-following performance claims
- Any AGV/AMR navigation accuracy, obstacle avoidance, or fleet routing claims
- Any protocol conformance (EtherCAT, PROFINET, Wi-Fi, Bluetooth) certification claims
- Any battery runtime, charge cycle, or energy density claims
- Any field-reliability, MTBF, DPPM, or fleet deployment statistics

---

## Related Pages

- `facts/applications/robotics-coverage-gap-map.md`
- `wiki/applications/application-routing-and-boundary-map.md`
- `wiki/applications/industrial-control-pcb-pcba-boundary-map.md`
- `wiki/processes/industrial-robotics-control-rewrite-readiness-map.md`

## Primary Sources

- /code/hileap/frontendAPT/public/static/industries/en/robotics-pcb.json
- /code/hileap/frontendAPT/public/static/resources/en/dfm-guidelines.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/testing-quality.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
