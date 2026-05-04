---
fact_id: "applications-defense-ew-coverage-gap-map"
title: "Defense / EW / Surveillance / Targeting application coverage gap map: which board families have wiki-level routing and which remain overview-only"
topic: "Defense, EW, surveillance, and targeting PCB/PCBA application coverage"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-183 initial build; sourced from wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md (active as of P4-176), related defense/radar/imaging fact cards in facts/methods/ and facts/standards/"
source_ids:
  - "frontendapt-industry-aerospace-defense-page-en"
  - "frontendapt-industry-drone-uav-page-en"
  - "frontendapt-industry-security-equipment-page-en"
  - "exosens-image-intensifier-tube-page"
  - "sony-starvis-technology-page"
  - "lynred-about-our-technologies-page"
  - "mipi-csi-2-spec-page"
  - "ti-lvds-overview-page"
  - "mil-std-461-emi-control-standard-page"
  - "mil-std-810-environmental-engineering-tests-page"
  - "analog-devices-phased-array-radar"
  - "px4-basic-concepts-guide"
  - "mavlink-overview-page"
tags: ["defense", "electronic-warfare", "surveillance", "targeting", "rf-front-end", "eo-ir", "uav", "coverage-map", "gap-map"]
---

# Canonical Summary

> As of 2026-05-03 after P4-183 initial build, the defense/EW/surveillance/targeting application family has a dedicated wiki boundary page (`wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md`) and that page is now `active`. This fact card maps what the current internal and public source layer supports, which board families are addressable, and which capability/compliance layers remain blocked.

## Board Family Coverage State

### Supported at Scenario + Board-Class Level

All entries below are supported by the Tier-2 internal source (`frontendapt-industry-aerospace-defense-page-en`) plus owner-backed identity sources. They support board-class and execution-context vocabulary only. They do NOT prove mission capability, qualification pass-status, weapons authority, or defense program history.

| Board Family | Application Context | PCB/PCBA Vocabulary Supported |
|---|---|---|
| **Electronic Warfare Front-End** | EW, ESM, EA: RF partitioning, shielding, cavity, hybrid material context | RF partition review, hybrid stackup, shielding/cavity planning, MIL-STD-461/810 standards-context vocabulary, staged validation |
| **Surveillance / ISR Board** | Multi-sensor interface, EO/IR processing, video output, data-link context | Owner-backed EO/IR detector naming (Exosens, STARVIS, Lynred IR), guarded MIPI/LVDS interface vocabulary, UAV integration posture |
| **Targeting Control Board** | Timing-sensitive fire-control context, platform-bus interface, EO/IR sensor input | Platform-bus vocabulary (MIL-1553, CAN, fire-control interface), owner-backed EO/IR naming, guarded laser ToF/pulsed-driver vocabulary, staging/release workflow |
| **Phased Array / Radar Board** | Radar and beam-steering context; RF-system pressure | RF-system context, Analog Devices phased-array identity vocabulary — NOT beam-steering performance, radar-range, or mission proof |
| **UAV / Drone Control Board** | Telemetry, control-link, flight-controller board context | PX4, MAVLink, ExpressLRS identity-level vocabulary at architecture level; UAV board-execution vocabulary |
| **Defense Assembly / FAI Board** | Aerospace-defense assembly with FAI, traceability, qualification discipline | AS9102C FAI vocabulary, MIL-STD/DO-standard context, documentation-aware release workflow |

### Fact Cards Supported

| Fact Card | What It Supports |
|---|---|
| `methods-eo-ir-detector-owner-identity-and-interface-boundary` | EO/IR detector owner identity (Exosens, STARVIS, Lynred) and interface boundary |
| `methods-fire-control-platform-interface-boundary` | Fire control platform interface vocabulary (MIL-1553, CAN, fire-control bus) |
| `methods-laser-time-of-flight-pulsed-driver-and-safety-boundary` | Laser ToF, pulsed-driver, and laser safety-control vocabulary |
| `methods-rf-validation-capability` | RF validation (TDR/VNA/coupon) capability vocabulary |
| `methods-rf-impedance-sparameter-pdn-ota-boundaries` | RF impedance, S-parameters, PDN, OTA boundaries |
| `methods-phased-array-source-coverage` | Radar and phased-array source coverage; beam-steering vocabulary boundary |
| `methods-remote-control-and-drone-control-stack-boundary` | UAV/drone telemetry and control-stack boundary |
| `methods-pcba-dfm-dft-dfa-review-gate-positioning` | DFM/DFT/DFA review gate positioning |
| `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary` | FAI vs high-speed validation boundary |
| `standards-military-environmental-and-emi-qualification-boundary` | MIL-STD-461/810 standards-context boundary; NOT compliance proof |
| `standards-embedded-imaging-serial-interface-boundary` | MIPI CSI-2/D-PHY/DSI-2, LVDS interface boundary |
| `standards-automotive-medical-aerospace-application-qualification-boundary` | Aerospace/defense application qualification boundary |

### Standards Context Supported (Public Sources)

| Standard | What It Supports |
|---|---|
| `MIL-STD-461` | Standards-context vocabulary for military EMI; NOT compliance proof or pass-status |
| `MIL-STD-810` | Standards-context vocabulary for military environmental qualification; NOT supplier qualification |
| `MIPI CSI-2 / D-PHY / DSI-2` | Sensor/display interface-family identity at compact imaging context; NOT protocol compliance |
| `LVDS (TI)` | Display interface-family identity for sensor/display link; NOT electrical compliance |
| `MIL-STD-1553` | Platform data-bus identity for fire-control context; NOT compliance or protocol-behavior proof |
| `PX4 / MAVLink / ExpressLRS` | UAV control-stack architecture vocabulary; NOT firmware behavior, certification, or version-specific claims |
| `Analog Devices phased-array` | Phased-array radar vocabulary at RF-system context level; NOT beam-steering performance or mission proof |

## Stable Facts

- The internal application layer supports aerospace-defense, drone-UAV, and security-equipment hardware as real scenario families at board-class vocabulary level.
- EO/IR detector vocabulary is supported via owner-backed pages (Exosens, STARVIS/Sony, Lynred); actual detector performance is NOT supported.
- Laser ToF and pulsed-driver vocabulary is supported at subsystem timing and review level only; laser accuracy, output power, or rangefinding claims are NOT supported.
- MIL-STD-461/810 vocabulary is supported at standards-context level only; compliance proof, pass-status, or supplier qualification claims are NOT supported.
- Phased-array radar vocabulary is supported as RF-system context; beam-steering performance or mission effectiveness claims are NOT supported.
- UAV control-stack vocabulary (PX4, MAVLink, ExpressLRS) is supported at architecture-level identity only; firmware stability or field-operation claims are NOT supported.
- Export control (ITAR/EAR) implications are NOT addressed by this wiki layer.

## Conditions And Methods

- Use this card to confirm what vocabulary is safe before writing a defense/EW/surveillance/targeting PCB article.
- For EO/IR detector vocabulary, route to `facts/methods/eo-ir-detector-owner-identity-and-interface-boundary`.
- For laser ToF/pulsed-driver vocabulary, route to `facts/methods/laser-time-of-flight-pulsed-driver-and-safety-boundary`.
- For MIL-STD environmental/EMI vocabulary, route to `facts/standards/military-environmental-and-emi-qualification-boundary`.
- For phased-array/radar vocabulary, route to `facts/methods/phased-array-source-coverage`.
- Update `last_reconciled_at` when a new defense/EW wiki boundary page is created.

## Limits And Non-Claims

- Mission capability, weapons authority, program history, or defense-prime proof is NOT supported.
- Exact bandwidth, range, detection, jamming, tracking, or targeting performance numerics are NOT supported.
- MIL-STD compliance proof, pass-status, or supplier qualification is NOT supported.
- Export control (ITAR/EAR) compliance or classification is NOT addressed.
- COMSEC, TEMPEST, or encrypted-link authority is NOT supported.
- Named customer, program, lab, or deployment claims are NOT supported.
- Yield, throughput, cost, or lead-time claims are NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|---|---|
| Dedicated defense/EW wiki boundary page | Closed — created and promoted to `active` in P4-176 |
| Companion fact card (this file) | Closed — created in P4-183 |
| MIL-STD-461/810 exact test-method vocabulary | Official DLA Quick Search or MIL-STD document page with stable public URL |
| Export control / ITAR/EAR vocabulary | Official DoD or BIS public guidance page recovery |
| Phased-array antenna performance vocabulary | Project-specific RF validation records, not wiki-layer |
| Laser driver / power / pulse vocabulary | Manufacturer-controlled laser product datasheet with public stable URL |
| EO/IR detector performance vocabulary | Project-specific detector characterization, not wiki-layer |
| Defense-prime / program vocabulary | Only addressable through customer-provided program documentation |
