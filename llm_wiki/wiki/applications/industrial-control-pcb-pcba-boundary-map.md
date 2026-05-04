---
topic_id: "applications-industrial-control-pcb-pcba-boundary-map"
title: "Industrial Control PCB PCBA Boundary Map"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
activated_at: "2026-05-03"
activation_notes: "P4-168 review pass: boundary language stable, all 6 board families have safe/blocked pairs, standards and protocol identity table complete, must-refresh and cross-lane routing present. Promoted to active."
fact_ids:
  - "applications-industrial-control-coverage-gap-map"
  - "applications-application-coverage-gap-map"
  - "methods-industrial-robotics-control-review-gates-and-claim-boundary"
  - "methods-pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary"
  - "methods-pcba-flying-probe-vs-ict-selection-posture"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-low-void-bga-conservative-generation-gate"
  - "methods-hidden-joint-xray-inspection-boundary"
source_ids:
  - "frontendapt-industry-industrial-control-page-en"
  - "frontendapt-dfm-guidelines-resource-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
tags: ["industrial-control", "plc", "servo", "vfd", "hmi", "fieldbus", "automation", "pcb", "pcba", "boundary-map", "application-boundary"]
---

# Definition

> Industrial control PCB/PCBA writing is safe when it stays at board-class, layout-context, and process-review vocabulary. It becomes unsafe when it crosses into SIL/PL functional-safety claims, IEC 61131 compliance proof, fieldbus interoperability proof, 24/7 uptime guarantees, or field-reliability outcomes. Use this page to navigate which angle is supportable for each industrial control board family.

## Why This Topic Matters

- Industrial control vocabulary (`functional safety`, `24/7 reliability`, `SIL`, `IEC 61131`, `PROFINET`, `EtherCAT`) looks like compliance proof when it is only context or marketing framing.
- The existing process/method fact card layer (DFM/DFT, flying probe, test-vs-reliability boundary) already provides strong support for process-review content on these boards.
- Without this boundary page, writers conflate board-class description with safety certification, protocol compliance, or reliability outcomes.

---

## Board Family Routing

### PLC / Control Cabinet PCBs

**Safe angles:**
- Modular PLC board format vocabulary: CPU boards, IO cards, communication modules, base/backplane boards, plug-in card interface geometry
- Mixed-signal noise-separation layout vocabulary: low-level analog/digital logic separated from noisy power and field signals
- Field interface and isolation description: optocouplers, isolation transformers, surge arresters, protection component integration
- DIN-rail and cabinet-friendly mechanical format vocabulary

**Blocked:**
- IEC 61131 programming model, instruction set, or certification compliance claims
- PLC CPU performance, scan-time, or memory claims
- OEM approval, program-specific qualification, or field-deployment proof

---

### Motion Control / Servo Drive / VFD PCBs

**Safe angles:**
- High-current/high-voltage PCB design vocabulary: copper weights, trace widths, creepage/clearance, isolation slot description
- Power stage integration vocabulary: IGBT/MOSFET, gate drivers, current sensors, snubbers, protection circuit description
- Control and feedback electronics vocabulary: encoder/resolver interface, current/voltage sensing, digital control section routing framing
- EMC-aware layout vocabulary: routing and grounding approaches to minimize emissions framing

**Blocked:**
- Exact creepage/clearance values or IEC 60664/IEC 61800 compliance claims
- Drive efficiency, torque ripple, or dynamic performance claims
- SIL/PL safe-torque-off (STO) functional safety implementation proof
- EMC compliance outcomes (CISPR 11, IEC 61000-4-x pass/fail)

---

### IO Modules / Field Sensors / Signal Conditioning PCBs

**Safe angles:**
- Multi-channel IO density vocabulary: 8/16/32-channel IO board layout, consistent isolation and protection per channel
- Signal conditioning description: 4–20 mA loop, 0–10 V, thermocouple, filtering/amplification/isolation/surge protection
- Field connection layout vocabulary: terminal blocks, M8/M12 connectors, ruggedized field wiring considerations
- Environmental and coating description: coatings and clearances for IO electronics near machines

**Blocked:**
- Accuracy, linearity, or resolution claims for signal conditioning circuits
- Ingress protection (IP rating) proof
- Atex/Zone certification or intrinsic safety claims
- Exact isolation voltage or surge withstand claims

---

### HMI / Operator Panel / Industrial PC PCBs

**Safe angles:**
- Display interface vocabulary: LCD/TFT, LVDS/MIPI DSI, backlight driver, capacitive/resistive touch controller PCB routing description
- User input and indicator vocabulary: membrane keypad, pushbutton, rotary encoder, LED, buzzer PCB integration description
- Industrial PC mainboard and IO/fieldbus card vocabulary: board format, slot, connector interface description
- EMI and enclosure integration vocabulary: grounding and shielding layout for metal/plastic industrial enclosures

**Blocked:**
- Display brightness, contrast, or viewing-angle specification claims
- Touch response latency or accuracy claims
- Industrial PC benchmark, BIOS, or OS compatibility proof
- NEMA or IP enclosure rating proof (enclosure is not the PCB)

---

### Industrial Networking / Fieldbus / Edge Gateway PCBs

**Safe angles:**
- Protocol identity vocabulary (name-only): Modbus, PROFIBUS, CAN/CANopen, DeviceNet, EtherCAT, PROFINET, Ethernet/IP, Modbus TCP identity framing
- Physical layer design vocabulary: isolation transformers, surge protection, EMI filtering at communication ports
- Edge computing and IIoT gateway board vocabulary: industrial interface + Ethernet/Wi-Fi/cellular/LPWAN module integration description
- DIN-rail and panel-mount gateway format vocabulary

**Blocked:**
- Protocol conformance certification (EtherCAT conformance, PROFINET certification, etc.)
- Protocol interoperability proof with specific controllers or devices
- Latency, determinism, or cycle-time claims for industrial Ethernet protocols
- OPC UA, MQTT, or cloud-platform integration behavior proof

---

### Industrial Power Supply / Safety Controller PCBs

**Safe angles:**
- AC-DC and DC-DC power stage layout vocabulary: switch-mode PSU, DC/DC module, auxiliary converter PCB description
- Creepage, clearance, and protection design description: isolation slots, fuses, surge protection layout vocabulary
- High-current and heat management vocabulary: copper distribution, thermal vias, mounting points for industrial loads
- Relay/contactor driver board vocabulary: relay switching, suppression circuit, LED status indication description
- Safety controller PCB description vocabulary (customer design basis): redundant channel layout, diagnostic monitoring, clearance/creepage for safety categories — framed as manufacturing support, NOT functional safety compliance proof

**Blocked:**
- Safety Integrity Level (SIL) claims (IEC 62061)
- Performance Level (PL) claims (ISO 13849)
- Diagnostic coverage (DC) percentage claims
- IEC 61511 / IEC 61508 compliance claims
- Exact safety-rated creepage/clearance values as compliance proof
- Release authority for safety-critical systems

---

## Process / Test Vocabulary

The following test and process vocabulary is already covered by existing method fact cards:

| Topic | Route To |
|---|---|
| DFM / DFT / DFA review gates for industrial control | `methods-industrial-robotics-control-review-gates-and-claim-boundary` |
| Flying probe vs ICT selection | `methods-pcba-flying-probe-vs-ict-selection-posture` |
| Test / inspection / reliability evidence separation | `methods-pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary` |
| Low-void BGA process planning on dense control boards | `methods-low-void-bga-conservative-generation-gate` + `methods-low-void-bga-dfm-to-process-review` |
| Hidden-joint X-ray inspection posture | `methods-hidden-joint-xray-inspection-boundary` |

**Do not duplicate these fact-card boundaries here.** Route prompts to the method cards directly for process-review content.

---

## Standards Context

| Standard / Protocol | Safe Use |
|---|---|
| `IEC 61131` | PLC programming language standard identity — NOT compliance or certification proof |
| `IEC 62061` | Machinery functional safety standard identity (SIL context) — NOT compliance proof |
| `ISO 13849` | Safety of machinery / control systems (PL context) — NOT compliance proof |
| `IEC 60664` | Insulation coordination for equipment — vocabulary reference; NOT compliance proof |
| `PROFINET / EtherCAT / Ethernet/IP` | Industrial Ethernet protocol identity names — NOT conformance or interoperability proof |
| `Modbus / PROFIBUS / CAN / CANopen` | Fieldbus protocol identity names — NOT compliance or certification proof |

---

## Engineering Boundaries

- Treat all industrial control board content as board-class and process-review stories, not as functional safety certification stories.
- Separate board-level PCB/PCBA engineering vocabulary from system safety lifecycle, SIL/PL allocation, and program-specific qualification.
- When a draft uses "safety controller" or "safety PLC", frame it as manufacturing support for customer-designed safety boards — NOT as certifying the functional safety function itself.
- Industrial networking protocol names (EtherCAT, PROFINET, Ethernet/IP) are identity-level only; do not advance to conformance, interoperability, or determinism claims.

---

## Common Misreadings

- `"Safety Ready"` or `"Functional Safety"` in source vocabulary → does NOT prove SIL, PL, IEC 62061, or ISO 13849 certification; it is marketing framing.
- `"-55 to 125 °C thermal shock"` trust-bar value → does NOT mean every board lot passes that test; it is capability-context framing.
- Protocol name appears in board description → does NOT prove conformance testing or interoperability with specific devices.
- DFM/DFT/DFA review completed → does NOT prove field reliability, uptime, or safety readiness.
- Flying probe or ICT used → does NOT prove long-term service robustness; see `methods-pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary`.

---

## Must Refresh Before Publishing

- Any SIL, PL, diagnostic coverage, or functional safety lifecycle claim
- Any IEC 61131, IEC 62061, ISO 13849, IEC 61508, or IEC 61511 compliance statement
- Any fieldbus conformance certification or interoperability claim
- Any EMC compliance outcome (CISPR 11, IEC 61000-4-x pass/fail)
- Any exact creepage, clearance, or insulation compliance value for safety categories
- Any 24/7 uptime, MTBF, DPPM, or field-reliability outcome claim
- Any IP-rating, Atex/Zone, or intrinsic-safety claim

---

## Cross-Lane Routing

| Content Type | Route To |
|---|---|
| DFM/DFT/DFA process review language | `facts/methods/industrial-robotics-control-review-gates-and-claim-boundary.md` |
| Flying probe vs ICT test selection | `facts/methods/pcba-flying-probe-vs-ict-selection-posture.md` |
| Test / inspection / reliability boundary | `facts/methods/pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary.md` |
| Robotics / AGV / cobot board routing | `wiki/applications/robotics-agv-cobot-pcb-pcba-boundary-map.md` (P4-160) |
| Power supply / thermal platform | `facts/methods/thermal-pcb-platform-selection-posture.md` |
| Conformal coating in industrial environments | `facts/methods/conformal-coating-lane-b-rewrite-gate.md` |

---

## Related Pages

- `facts/applications/industrial-control-coverage-gap-map.md`
- `wiki/applications/application-routing-and-boundary-map.md`
- `wiki/processes/industrial-robotics-control-rewrite-readiness-map.md`

## Primary Sources

- /code/hileap/frontendAPT/public/static/industries/en/industrial-control-pcb.json
- /code/hileap/frontendAPT/public/static/resources/en/dfm-guidelines.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/testing-quality.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
