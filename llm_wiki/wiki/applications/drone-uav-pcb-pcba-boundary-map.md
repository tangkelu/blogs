---
topic_id: "applications-drone-uav-pcb-pcba-boundary-map"
title: "Drone UAV PCB PCBA Boundary Map"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
activated_at: "2026-05-03"
activation_notes: "P4-169 review pass: boundary language stable, all 5 board families have safe/blocked pairs, civilian-vs-defense routing decision table present, FAA/EASA/PX4/MAVLink standards identity table complete, must-refresh and cross-lane routing present. Promoted to active."
fact_ids:
  - "applications-drone-uav-coverage-gap-map"
  - "applications-application-coverage-gap-map"
  - "methods-remote-control-and-drone-control-stack-boundary"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-flying-probe-vs-ict-selection-posture"
  - "methods-hidden-joint-xray-inspection-boundary"
  - "methods-low-void-bga-conservative-generation-gate"
source_ids:
  - "frontendapt-industry-drone-uav-page-en"
  - "px4-basic-concepts-guide"
  - "mavlink-overview-page"
  - "expresslrs-getting-started"
  - "frontendapt-pcba-quality-system-page-en"
tags: ["drone", "uav", "flight-controller", "esc", "pdb", "fpv", "gnss", "telemetry", "gimbal", "bms", "pcb", "pcba", "boundary-map", "application-boundary"]
---

# Definition

> Drone/UAV PCB/PCBA writing is safe at board-class, control-stack architecture, and layout-context vocabulary. It is unsafe when it crosses into airworthiness certification, FAA/EASA regulatory compliance, flight endurance/range/payload performance, GNSS accuracy, RF link budget, or autonomous-flight capability claims. Use this page to navigate which angle is supportable for each drone board family.

## Why This Topic Matters

- Drone vocabulary (`"Flight-Ready"`, `"autonomous"`, `"anti-interference"`, `"precision GPS"`, `"long range"`) reads as performance or certification proof when it is only application-context framing or marketing.
- Civilian/commercial drone content previously had no dedicated routing page and relied on defense-page overlap and a single control-stack fact card.
- PX4, MAVLink, and ExpressLRS are widely cited — they are now bounded as architecture-identity vocabulary only, not performance or compatibility proof.

---

## Routing Decision: Civilian vs. Defense Drone Context

| Context | Route To |
|---|---|
| Civilian/commercial drones (hobby, FPV, industrial, agricultural, delivery) | **This page** |
| Defense/military UAV (ISR, targeting, EW payloads, MIL-STD context) | `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md` |
| Consumer RC/hobby (non-drone remote control) | `facts/methods/remote-control-and-drone-control-stack-boundary.md` |

---

## Board Family Routing

### Flight Controller / Autopilot PCBs

**Safe angles:**
- Sensor and MCU integration vocabulary: MCU/SoC, IMU (accelerometer/gyro), magnetometer, barometer, GNSS module layout integration description
- Low-noise mixed-signal design vocabulary: analog sensor area separation from digital and power sections description
- Compact/lightweight layout vocabulary: 4/6-layer and higher stackup for signal integrity and noise control in weight-constrained drones
- Standard and custom form-factor vocabulary: 20×20, 30.5×30.5 FPV form factor, proprietary industrial UAV size description
- Control-stack architecture identity vocabulary: PX4, MAVLink, Betaflight identity names — architecture context only

**Blocked:**
- Attitude control bandwidth, stabilization latency, or PID-loop performance claims
- FAA Part 107 / EASA UAS category compliance claims
- Autonomous flight capability, obstacle avoidance, or BVLOS authorization proof
- Named autopilot software (PX4, ArduPilot) performance benchmarks or reliability metrics

---

### ESC / Power Distribution (PDB) PCBs

**Safe angles:**
- High-current design vocabulary: copper weight, trace width, thermal via structure for motor-current handling description
- MOSFET and driver integration vocabulary: MOSFET array, driver IC, current sensing, protection circuit layout description
- PDB vocabulary: battery-to-ESC-to-payload power distribution board with fusing/protection
- EMI and noise vocabulary: switching noise reduction layout practices to protect flight-control and RF sections

**Blocked:**
- ESC current rating, burst current, continuous current proof
- Motor efficiency, throttle linearity, or thrust-to-weight performance claims
- Specific ESC protocol (DSHOT, PWM, OneShot) latency or performance claims
- Thermal rise, derating, or reliability-under-load outcome claims

---

### Communication / RF / Navigation PCBs

**Safe angles:**
- RC receiver board vocabulary: RC receiver module, telemetry radio PCB, video transmitter (VTX) PCB description
- RF frequency identity vocabulary: 2.4 GHz RC link, 900 MHz / 1.2 GHz long-range link identity — **architecture-level only**; per `methods-remote-control-and-drone-control-stack-boundary`
- Video transmission board vocabulary: analog/digital VTX PCB, RF section, modulation/demod, camera/OSD interface description
- GNSS and compass board vocabulary: GPS/GLONASS/BeiDou/Galileo module, magnetometer on compact nav PCB description
- Antenna integration vocabulary: PCB antenna, feed network, ground plane, clearance description

**Blocked:**
- RF link range, EIRP, receive sensitivity, or anti-interference claims
- GNSS fix accuracy, CEP, TTFF, or jamming-resistance claims
- RTK positioning precision claims without dedicated RTK chipset source
- FCC/CE/RED RF certification claims
- Video latency, resolution, or FPV goggle compatibility claims
- Cross-brand transmitter/receiver compatibility claims (ExpressLRS, ELRS, FrSky, Spektrum)

---

### Payload / Gimbal Control PCBs

**Safe angles:**
- Gimbal control board vocabulary: 2/3-axis gimbal motor driver, IMU, control logic description
- Camera and sensor interface vocabulary: HDMI, CSI, MIPI, analog video input, LiDAR data interface, thermal sensor interface description
- Payload power and control vocabulary: voltage regulation and switching to payloads, control interface to flight controller or companion computer description
- Modular and swappable design vocabulary: standard connector and physical format for different mission payloads

> **Overlap with sensor/navigation:** For LiDAR/radar RF front-end depth, consult `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md`.

**Blocked:**
- Camera image quality, resolution, stabilization accuracy, or optical performance claims
- LiDAR point-cloud density, range, or angular resolution claims
- Sprayer flow-rate accuracy or agricultural-application coverage claims
- AI-based object detection, classification, or tracking performance claims

---

### Battery / BMS / Charging PCBs

**Safe angles:**
- Cell monitoring and balancing vocabulary: BMS PCB for LiPo/Li-ion multi-cell monitoring, temperature measurement, passive/active balancing description
- Protection circuit vocabulary: over-current, over/under-voltage, short-circuit, over-temperature on battery PCB
- Charging and docking vocabulary: charger hub, automated docking/recharge station PCB, AC-DC/DC-DC description
- Power distribution vocabulary: voltage rail regulation and distribution to FC, payloads, RF, auxiliary systems

**Blocked:**
- Battery flight-time, cycle-life, energy density, or capacity-retention claims
- Smart battery protocol (DJI, etc.) compatibility proof
- Charging speed, full-charge time, or C-rate claims
- Swelling, fire-safety, or UN 38.3 transport qualification claims

---

### Ground Control / Remote Controller PCBs

**Safe angles:**
- UI and controls vocabulary: joystick, button, switch, dial, touchscreen, indicator PCB for controller/console description
- Communication module vocabulary: RF module, Wi-Fi, cellular integration on GCS/remote unit (identity-level only)
- Power and battery vocabulary: internal battery charging and power regulation for ground equipment
- Rugged design vocabulary: outdoor use, handling, transport, EMI shielding layout practices

**Blocked:**
- Control range, link reliability, or interference-rejection claims
- Touchscreen response time or display quality claims
- IP rating (IP54, IP65) or drop/shock resistance proof
- Named ecosystem compatibility (DJI, Autel, Skydio) claims

---

## Control-Stack Architecture: Cross-Route to Existing Fact Card

**Do not re-derive this boundary here.** The following fact card defines the safe architecture-identity posture for drone control stacks:

| Topic | Route To |
|---|---|
| RC control link / autopilot / actuator / telemetry architecture identity | `facts/methods/remote-control-and-drone-control-stack-boundary.md` |
| PX4, MAVLink, ExpressLRS identity vocabulary | `facts/methods/remote-control-and-drone-control-stack-boundary.md` |
| Drone slug-level rewrite gate | `wiki/processes/remote-control-and-drone-control-stack-boundaries.md` |

---

## Standards Context

| Standard / Protocol | Safe Use |
|---|---|
| `FAA Part 107` | US commercial drone operator rule identity — NOT airworthiness or hardware compliance proof |
| `EASA UAS Category A/B/C` | EU UAS classification identity — NOT certification proof |
| `DO-254` | Airborne electronic hardware assurance standard identity — NOT compliance proof; **not in sources registry** |
| `PX4` | Open-source autopilot platform identity — NOT performance, reliability, or compatibility proof |
| `MAVLink` | Drone communication protocol identity — NOT performance, latency, or security proof |
| `ExpressLRS` | Open-source RC link ecosystem identity — NOT range, compatibility, or certification proof |

---

## Engineering Boundaries

- Drone content is weight-conscious, vibration-exposed, and RF-dense — these are board-level engineering pressures, not performance guarantees.
- "Defense/Security UAV" platform exists in the Tier-2 source; do NOT use this page for defense ISR or EW-payload UAV content; route to the defense page.
- Trust-bar labels (`"Flight-Ready"`, `"Weight Optimized"`, `"Vibration Tested"`) are marketing framing; do not publish as specifications.
- RF frequency identities (2.4 GHz, 900 MHz) are architecture-context labels only per the control-stack fact card; no EIRP, range, or anti-interference claims.

---

## Common Misreadings

- `"Flight-Ready – Multi-Platform"` trust-bar → does NOT prove airworthiness, qualification, or FAA/EASA certification.
- `"Vibration Tested"` trust-bar → does NOT prove a specific test standard, test cycle count, or pass/fail outcome.
- PX4 or MAVLink mentioned → does NOT prove the PCB is certified, tested, or compatible with specific aircraft.
- GNSS module on navigation board → does NOT prove accuracy, CEP, TTFF, or anti-spoofing.
- `"Long-range RF link"` vocabulary → does NOT prove range, EIRP, or anti-interference performance.
- Defense/Security UAV platform listed → does NOT permit MIL-STD or EW vocabulary; route to defense page.

---

## Must Refresh Before Publishing

- Any FAA Part 107, EASA UAS category, or airworthiness compliance claims
- Any DO-254 or aviation hardware assurance claims
- Any flight endurance, range, payload capacity, or speed claims
- Any GNSS accuracy, RTK precision, fix-rate, or anti-jamming claims
- Any RF range, EIRP, anti-interference, or FCC/CE certification claims
- Any PX4/MAVLink/ExpressLRS performance, latency, or cross-brand compatibility claims
- Any battery flight-time, cycle life, or C-rate claims

---

## Cross-Lane Routing

| Content Type | Route To |
|---|---|
| Defense/military UAV, ISR payload, EW drone | `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md` |
| Consumer RC / hobby non-drone remote control | `facts/methods/remote-control-and-drone-control-stack-boundary.md` |
| LiDAR / radar RF front-end depth on payload | `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md` |
| DFM / DFT review gates | `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md` |
| Flying probe vs ICT | `facts/methods/pcba-flying-probe-vs-ict-selection-posture.md` |
| X-ray hidden-joint inspection | `facts/methods/hidden-joint-xray-inspection-boundary.md` |
| Low-void BGA on flight controller | `facts/methods/low-void-bga-conservative-generation-gate.md` |

---

## Related Pages

- `facts/applications/drone-uav-coverage-gap-map.md`
- `wiki/applications/application-routing-and-boundary-map.md`
- `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md`
- `wiki/processes/remote-control-and-drone-control-stack-boundaries.md`

## Primary Sources

- /code/hileap/frontendAPT/public/static/industries/en/drone-uav-pcb.json
- https://docs.px4.io/main/en/getting_started/px4_basic_concepts.html
- https://mavlink.io/en/about/overview.html
- https://www.expresslrs.org/quick-start/getting-started/
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
