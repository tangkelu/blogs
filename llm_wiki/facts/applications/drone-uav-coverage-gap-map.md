---
fact_id: "applications-drone-uav-coverage-gap-map"
title: "Drone / UAV application coverage gap map: which board families have wiki-layer routing and which remain blocked"
topic: "Drone and UAV PCB/PCBA application coverage"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-162 initial build; sourced from frontendapt-industry-drone-uav-page-en (Tier-2), remote-control-and-drone-control-stack-boundary, and defense-ew-surveillance-targeting-pcb-review-boundaries. Civilian/commercial drone content is now separated from defense/EW/surveillance overlap."
source_ids:
  - "frontendapt-industry-drone-uav-page-en"
  - "px4-basic-concepts-guide"
  - "mavlink-overview-page"
  - "expresslrs-getting-started"
  - "frontendapt-pcba-quality-system-page-en"
tags: ["drone", "uav", "flight-controller", "esc", "fpv", "gnss", "telemetry", "coverage-map", "gap-map"]
---

# Canonical Summary

> As of 2026-05-03, the drone/UAV application family has a dedicated wiki boundary page (`wiki/applications/drone-uav-pcb-pcba-boundary-map.md`) created by P4-162. Prior to this lane, drone/UAV content was partially covered under `defense-ew-surveillance-targeting-pcb-review-boundaries.md` and the `remote-control-and-drone-control-stack-boundary` fact card. The Tier-2 internal source supports 7 board families. It does NOT prove airworthiness, FAA/EASA certification, autonomy performance, endurance, payload capacity, or navigation-accuracy claims.

## Board Family Coverage State

### Supported at Scenario + Board-Class Level (Tier-2 Internal Source + Existing Fact Cards)

| Board Family | Application Context | PCB/PCBA Vocabulary Supported |
|---|---|---|
| **Flight Controller / Autopilot** | Quadcopters, VTOL, fixed-wing, industrial UAVs | MCU/SoC/IMU/magnetometer/barometer/GNSS integration, low-noise mixed-signal layout, compact/lightweight multilayer stackup, standard form-factor (20×20, 30.5×30.5) vocabulary |
| **ESC / Power Distribution (PDB)** | All drone propulsion platforms | High-current copper weight/trace width/thermal via, MOSFET array/driver IC/current-sense/protection layout, PDB power distribution routing, EMI/noise reduction vocabulary |
| **Communication / RF / Navigation** | RC link, telemetry, FPV video, GNSS | RC receiver, telemetry radio, VTX board description; 2.4 GHz / 900 MHz / 1.2 GHz identity vocabulary (architecture-level only); GNSS/GLONASS/BeiDou/Galileo module board; antenna feed network/ground-plane vocabulary |
| **Payload / Gimbal Control** | Camera gimbals, LiDAR, thermal, sprayer, delivery | Gimbal motor driver/IMU/control logic, camera interface (HDMI/CSI/MIPI/analog), LiDAR data interface, payload power/control PCB vocabulary |
| **Battery / BMS / Charging** | All platforms (airborne + ground) | BMS PCB for LiPo/Li-ion cell monitoring/balancing/protection, charging hub/docking station PCB, AC-DC/DC-DC power rail distribution vocabulary |
| **Ground Control / Remote Controller** | RC, GCS, base stations, repeaters | Joystick/button/touchscreen/indicator UI board, RF/Wi-Fi/cellular module integration (identity-level), rugged field-ready layout vocabulary |
| **Navigation Support (GNSS/IMU boards)** | All autonomous/semi-autonomous platforms | GNSS module PCB, compass/magnetometer board, RTK positioning board vocabulary (hardware only — NOT accuracy, fix-rate, or jamming-resistance claims) |

### Control-Stack Architecture Already Covered (Fact Card Layer)

| Coverage | Fact Card | What It Covers |
|---|---|---|
| Drone control-stack architecture identity | `methods-remote-control-and-drone-control-stack-boundary` | RC control link → autopilot layer → actuator outputs; MAVLink, PX4, ExpressLRS identity vocabulary (architecture-level only) |
| Drone slug partial routing | `wiki/processes/remote-control-and-drone-control-stack-boundaries.md` | Process-level rewrite gate for drone/RC control stack slugs |

### Quality / Test Steps Supported

- SPI → AOI → X-ray (BGA/LGA/QFN on FC, ESC, comm modules) → ICT/flying-probe → FCT → final inspection + traceability

## Stable Facts

- The Tier-2 source covers 6 platform categories: consumer, FPV/racing, industrial, agricultural, logistics/delivery, and defense/security. This card focuses on civilian/commercial contexts; defense UAV content routes to `defense-ew-surveillance-targeting-pcb-review-boundaries.md`.
- Trust-bar labels (`"Flight-Ready"`, `"Weight Optimized"`, `"Vibration Tested"`) are marketing framing — NOT airworthiness or qualification proof.
- RF frequency identity vocabulary (2.4 GHz, 900 MHz, 1.2 GHz) is architecture-level context only per `methods-remote-control-and-drone-control-stack-boundary` — no range, EIRP, or anti-interference claims.
- PX4, MAVLink, and ExpressLRS are identity-level vocabulary only — not performance, compatibility, or cross-brand interoperability proof.
- "Defense/Security UAV" platform context exists in the Tier-2 source; for defense UAV content with MIL-STD vocabulary, route to `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md`.

## Conditions And Methods

- Use this card for civilian/commercial drone PCB routing.
- For defense/military UAV contexts, route to `defense-ew-surveillance-targeting-pcb-review-boundaries.md`.
- For consumer RC/hobby (non-drone) context, also check `methods-remote-control-and-drone-control-stack-boundary`.

## Limits And Non-Claims

- FAA Part 107, EASA UAS category, or airworthiness certification claims NOT supported.
- DO-254 or aviation hardware assurance claims NOT supported.
- Flight endurance, range, payload capacity, or speed claims NOT supported.
- GNSS accuracy, fix rate, RTK precision, or anti-jamming/spoofing claims NOT supported.
- Autonomy, obstacle avoidance, BVLOS performance, or swarm-control claims NOT supported.
- RF range, EIRP, anti-interference, or link-budget claims NOT supported.
- Yield, throughput, cost, or lead-time claims NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|-----|-----------------|
| FAA Part 107 / EASA UAS regulatory boundary vocabulary | Official FAA/EASA drone regulatory source recovery |
| GNSS accuracy / RTK standard vocabulary | Official RTK/GNSS standard or chipset source |
| RF link budget / certification vocabulary (FCC, CE) | Official FCC/CE source recovery for drone comms |
| DO-254 airborne electronic hardware assurance | Official DO-254 source (also needed for civil aerospace p4-163) |
| Dedicated drone/UAV wiki page status | Reopen only if the page later regresses and requires demotion from `active` |
