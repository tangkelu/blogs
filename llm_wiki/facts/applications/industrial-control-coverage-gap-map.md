---
fact_id: "applications-industrial-control-coverage-gap-map"
title: "Industrial control application coverage gap map: which board families have wiki-layer routing and which remain overview-only"
topic: "Industrial control PCB/PCBA application coverage"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-158 initial build; sourced from frontendapt-industry-industrial-control-page-en (Tier-2), industrial-robotics-control-review-gates-and-claim-boundary, pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary, and industrial-robotics-control-rewrite-readiness-map"
source_ids:
  - "frontendapt-industry-industrial-control-page-en"
  - "frontendapt-dfm-guidelines-resource-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
tags: ["industrial-control", "plc", "servo", "hmi", "automation", "fieldbus", "coverage-map", "gap-map"]
---

# Canonical Summary

> As of 2026-05-03, the industrial control application family has a dedicated wiki boundary page (`wiki/applications/industrial-control-pcb-pcba-boundary-map.md`) created by P4-158. Prior to this lane, the segment was overview-only. The Tier-2 internal source supports board-class vocabulary for 6 board families. It does NOT prove IEC 61131 compliance, SIL/PL safety certification, 24/7 uptime outcomes, or field-reliability numerics.

## Board Family Coverage State

### Supported at Scenario + Board-Class Level (Tier-2 Internal Source)

All entries below are extracted from `frontendapt-industry-industrial-control-page-en` (Tier-2), plus existing process/method fact cards. They support PCB/PCBA board-class vocabulary and engineering context. They do NOT prove certification, qualification, or reliability outcomes.

| Board Family | Application Context | PCB/PCBA Vocabulary Supported |
|---|---|---|
| **PLC / Control Cabinet** | PLC mainboards, CPU boards, IO cards, backplanes, communication modules | Modular PLC board formats, mixed-signal/noise-separation layout, optocoupler/isolation/surge protection integration, DIN-rail mechanical format vocabulary |
| **Motion / Servo / VFD** | Servo drives, VFDs, stepper/BLDC drivers, CNC axis controllers | High-current/high-voltage creepage/clearance description, power stage (IGBT/MOSFET/gate driver/current sensor) integration, encoder/resolver feedback routing, EMC-aware layout vocabulary |
| **IO Modules / Field Sensors** | Digital/analog IO modules, sensor interface, signal conditioning, distributed IO | Multi-channel IO density, isolation/surge/protection integration, 4–20 mA / 0–10 V / thermocouple conditioning vocabulary, terminal block / M8/M12 connector layout |
| **HMI / Industrial PC** | HMI panels, keypads, touchscreen controllers, industrial PC mainboards, interface cards | LCD/TFT display, LVDS/MIPI, backlight driver, capacitive/resistive touch vocabulary; IPC mainboard and IO/fieldbus card board description |
| **Industrial Networking / Fieldbus / Gateway** | Fieldbus PCBs, industrial Ethernet, protocol converters, edge gateways, data loggers | Modbus/PROFIBUS/CAN/CANopen/DeviceNet/EtherCAT/PROFINET/Ethernet-IP identity vocabulary (no compliance proof), isolation transformer/surge/EMI filter at communication ports |
| **Industrial Power / Safety Controller** | AC-DC PSUs, DC-DC converters, relay boards, contactor drivers, safety PLCs, interlock controllers | AC-DC/DC-DC layout vocabulary, creepage/clearance/slot design description, relay/contactor drive with suppression; safety controller board description (customer design basis only) |

### Process / Test Coverage Already Landed (Methods Fact Cards)

| Capability | Supporting Fact Card |
|---|---|
| DFM / DFT / DFA review gates for industrial control boards | `methods-industrial-robotics-control-review-gates-and-claim-boundary` |
| Flying probe vs ICT electrical test selection | `methods-pcba-flying-probe-vs-ict-selection-posture` |
| Inspection / test / reliability evidence separation | `methods-pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary` |
| Low-void BGA process planning on dense control boards | `methods-low-void-bga-conservative-generation-gate`, `methods-low-void-bga-dfm-to-process-review` |
| Hidden-joint X-ray inspection posture | `methods-hidden-joint-xray-inspection-boundary` |

### Quality/Test Steps Supported (Tier-2 Internal Source)

- SPI → AOI → X-ray (BGA/LGA/QFN) → ICT/flying-probe → FCT → final inspection + traceability
- Layered test quality stack at description level; NOT lot-level pass/fail proof
- Lot-level or board-level traceability framing; NOT program-specific traceability system proof

## Stable Facts

- The Tier-2 internal industrial-control source covers 6 distinct board families: PLC/control cabinet, motion/servo/VFD, IO modules/field sensors, HMI/IPC, industrial networking/gateway, and industrial power/safety controller.
- The source mentions "functional safety" in hero vocabulary but this is marketing framing only; it does NOT unlock SIL, PL, IEC 62061, or ISO 13849 compliance claims.
- The source mentions "-55 to 125 °C thermal shock" in the trust bar; treat as capability-context only — NOT lot-level qualification proof.
- The fieldbus/protocol vocabulary (Modbus, PROFIBUS, CAN, EtherCAT, PROFINET, Ethernet/IP) is identity-level only; it does NOT prove interoperability, conformance testing, or protocol compliance.
- Prior process/method fact cards (from P4-114/P4-115/P4-116 era) already cover DFM/DFT/DFA, flying probe, and test-inspection-vs-reliability boundaries for industrial control content.

## Conditions And Methods

- Use this card to confirm which board-family vocabulary is safe before writing an industrial control PCB article.
- For fieldbus/protocol identity depth, do NOT use without explicit official protocol-organization source.
- For IEC 61131, IEC 62061, or ISO 13849 safety-standard depth, these sources do not exist in the current registry; do not use.
- Update `last_reconciled_at` when new industrial-control-specific fact cards or official standard sources are added.

## Limits And Non-Claims

- IEC 61131-3 programming compliance, SIL/PL functional safety certification, ISO 13849 / IEC 62061 claims are NOT supported.
- 24/7 uptime outcomes, MTBF, DPPM, or field-failure rate claims are NOT supported.
- Exact EMC compliance (CISPR 11, IEC 61000-4 series) proof is NOT supported.
- Exact creepage, clearance, or insulation compliance values for safety categories are NOT supported.
- Fieldbus/protocol interoperability, conformance certification, or integration-test proof is NOT supported.
- Yield, throughput, cost, or lead-time claims are NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|-----|-----------------|
| IEC 61131 exact programming standard vocabulary | Official IEC/PLCopen source recovery |
| IEC 62061 / ISO 13849 functional safety boundary | Official IEC/ISO functional safety source |
| Fieldbus conformance depth (EtherCAT, PROFINET, etc.) | EtherCAT Technology Group, PI (PROFIBUS & PROFINET International) source recovery |
| Industrial EMC boundary (CISPR 11, IEC 61000-4-x) | Official IEC EMC standard source |
| Dedicated industrial-control wiki page status | Reopen only if the page later regresses and requires demotion from `active` |
