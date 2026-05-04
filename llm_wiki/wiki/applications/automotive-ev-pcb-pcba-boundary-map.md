---
topic_id: "applications-automotive-ev-pcb-pcba-boundary-map"
title: "Automotive And EV PCB PCBA Boundary Map"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
activated_at: "2026-05-03"
activation_notes: "P4-168 review pass: boundary language stable, all 7 board families have safe/blocked pairs, standards context table complete, must-refresh and cross-lane routing present. Promoted to active."
fact_ids:
  - "applications-automotive-ev-coverage-gap-map"
  - "applications-application-coverage-gap-map"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"
  - "methods-power-energy-inverter-charger-rewrite-boundary"
  - "methods-thermal-pcb-platform-selection-posture"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-conformal-coating-lane-b-rewrite-gate"
source_ids:
  - "frontendapt-industry-automotive-electronics-page-en"
  - "iso-26262-road-vehicles-functional-safety-package"
  - "iatf-16949-overview-page"
  - "aec-documents-page"
tags: ["automotive", "ev", "bms", "adas", "ecu", "obc", "inverter", "pcb", "pcba", "boundary-map", "application-boundary"]
---

# Definition

> Automotive and EV PCB/PCBA writing is safe when it stays at board-class, assembly-context, and engineering-review vocabulary. It becomes unsafe when it crosses into ASIL claims, IATF certification proof, AEC-Q qualification proof, OEM approval, thermal/vibration pass-fail outcomes, or field-reliability guarantees. Use this page to navigate which angle is supportable for each automotive/EV board family.

## Why This Topic Matters

- Automotive and EV drafts are high-risk for over-claiming because the vocabulary (`ISO 26262`, `IATF 16949`, `ASIL`, `PPAP`, `AEC-Q`, `-40 to 125 °C`) sounds like qualification proof when it is only context framing.
- The corpus (Tier-2 internal source) supports board-class and engineering-context vocabulary for 7 distinct automotive/EV board families.
- Without this boundary map, writers drift from board-level review into system safety, certification, or reliability claims that the corpus does not support.

---

## Board Family Routing

### ECU and Vehicle Control PCBs

**Safe angles:**
- High-Tg, high-reliability material and stackup context for under-dash, under-hood, in-cabin environments
- Mixed-signal routing vocabulary: analog sensor inputs, digital control, vehicle network traces (CAN, LIN, FlexRay, Automotive Ethernet)
- Power and ground design context: copper weights, plane design, filtering for 12 V / 24 V supply rails
- Connector interface and mechanical constraint vocabulary: hole/slot/pad geometry for ECU connectors, sealing/potting/enclosure integration description
- Assembly workflow: SMT + THT combination, calibration and software-flash readiness framing

**Blocked:**
- ASIL allocation, functional-safety lifecycle claims
- ECU-level OEM qualification, customer approval, or field-reliability proof
- Exact dielectric constant, loss factor, or material performance proof

---

### Inverter / Motor Control PCBs

**Safe angles:**
- High-voltage board design vocabulary: creepage/clearance design language, isolation slots, insulation strategy description
- Thick copper and thermal management context: copper weight, thermal vias, copper pours, heat-spreading structure description
- Gate driver and control integration vocabulary: isolated gate drivers, MCU/sensing circuits, isolation boundary framing
- EMC-aware layout vocabulary: grounding practices for fast switching edges, emission and susceptibility framing

**Blocked:**
- Exact creepage/clearance values or safety-standard compliance proof (IEC 60664, IEC 61800)
- Inverter efficiency, power density, or thermal-rise performance proof
- ASIL or ISO 26262 functional-safety compliance for powertrain PCBs
- High-voltage safety certification claims (UL, IEC, LVD)

---

### BMS (Battery Management System) PCBs

**Safe angles:**
- High-accuracy measurement layout vocabulary: differential routing, signal-path separation, noise/leakage framing
- Isolation and safety design description: insulation distances, slots, coating, connector design for HV/LV separation
- Balancing and power path description: copper design for balancing circuits, contactor/relay drive, thermal framing
- Communication interface vocabulary: CAN, LIN, SPI, UART, Ethernet interface integration description

**Blocked:**
- Over-charge, over-discharge, over-temperature protection effectiveness proof
- State-of-charge (SOC), state-of-health (SOH) accuracy claims
- Pack-lifetime, cycle-life, or field reliability proof
- Isolation voltage, creepage, or safety standard compliance claims

---

### OBC / DC-DC / Charger PCBs

**Safe angles:**
- AC-DC and DC-DC power stage layout vocabulary: PFC stage, LLC/resonant topology description, isolated DC-DC section framing
- High-voltage clearance and creepage design description
- Thermal and mechanical integration vocabulary: component placement, copper spreading, heatsink/baseplate/enclosure integration framing
- Control and communication vocabulary: digital control MCU, CAN/PLC/Ethernet integration description

> **Route EV charger protocol claims** (IEC 61851, ISO 15118, SAE J1772, CCS, NACS, OCPP) to `wiki/applications/power-energy-pcb-pcba-review-boundaries.md` — that page owns the EV-charger control-stack boundary.

**Blocked:**
- Charging speed, cable current, or connector-protocol compliance claims
- Exact isolation, creepage, clearance, or insulation standard compliance proof
- Charging efficiency, power loss, or thermal-rise performance proof

---

### ADAS / Radar / Camera PCBs

**Safe angles:**
- Sensor front-end PCB vocabulary: RF (radar module), high-speed LVDS/MIPI (camera), power/signal conditioning on compact boards
- Domain/fusion controller PCB vocabulary: multilayer SoC/FPGA hosting, high-speed interface routing framing
- Environmental robustness description: material, coating, connector choices for exterior/roof/bumper mounting contexts
- Automotive network integration vocabulary: CAN, FlexRay, Automotive Ethernet connection framing

> **Route radar/sensor RF front-end depth** to `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md` for RF impedance, S-parameter, and OTA boundary detail.

**Blocked:**
- ADAS safety function proof (ISO 21448 / SOTIF, ISO 26262)
- Radar detection range, accuracy, or angular resolution claims
- Camera resolution, frame rate, or image-quality proof
- Autonomous driving readiness, NCAP test outcome, or OEM certification claims

---

### Infotainment / Connectivity / Telematics PCBs

**Safe angles:**
- High-speed display interface vocabulary: LVDS, MIPI DSI, HDMI routing framing
- Connectivity module integration vocabulary: cellular (4G/5G), GNSS, Wi-Fi, Bluetooth, V2X antenna interface description
- HMI electronics vocabulary: capacitive touch, button panel, backlighting, haptic feedback PCB framing
- In-vehicle network vocabulary: CAN/Ethernet gateway, security chip integration description

**Blocked:**
- Wi-Fi, Bluetooth, or cellular performance, range, or throughput proof
- V2X safety or standards compliance claims
- Display color accuracy, contrast ratio, or refresh rate claims
- Software/OS or cybersecurity claims

---

### Lighting / Body / BCM PCBs

**Safe angles:**
- LED lighting board vocabulary: MCPCB and FR-4 for LED headlamp/DRL/tail lamp/ambient lighting, thermal and optical framing
- Body control and comfort PCB vocabulary: BCM, door/seat/window/HVAC/wiper controller framing
- Environmental and mechanical description: moisture, dust, vibration, temperature variation context for door/trunk/exterior/under-dash locations

**Blocked:**
- Photometric claims (lumen output, beam pattern, FMVSS/ECE compliance)
- BCM functional safety or diagnostic coverage claims
- Lifespan or duty-cycle proof for body electronics

---

## Standards Context

| Standard | Safe Use |
|---|---|
| `ISO 26262` | Road-vehicle E/E functional-safety vocabulary: ASIL levels A–D, safety lifecycle phases, hazard analysis and risk assessment (HARA) framing — NOT compliance proof |
| `IATF 16949` | Automotive QMS vocabulary: PPAP, APQP, control plans, MSA, SPC process-description framing — NOT certification status proof |
| `AEC-Q` family | Component-qualification document-family identity (AEC-Q100, Q101, Q200) — NOT PCB or supplier qualification proof |

---

## Test / Inspection Vocabulary

The following test and inspection vocabulary is supported at process-description level only:

- `SPI → AOI → X-ray → ICT/flying-probe → FCT → final QC + traceability` workflow
- Thermal cycling: `-40 to 125 °C` cycle range vocabulary (NOT lot-level pass/fail proof)
- Vibration testing: `5 Grms / 10 h` vocabulary (NOT qualification proof)
- Cleanliness: `ROSE ≤1.5 µg/cm²` vocabulary (NOT specification compliance proof)
- VIN-to-board traceability framing (NOT OEM-specific traceability system proof)

---

## Engineering Boundaries

- Treat all automotive/EV board content as board-class and review-workflow stories, not as system-safety or certification stories.
- Separate board-level PCB/PCBA engineering vocabulary from vehicle-level functional safety lifecycle, OEM approval, and lot-level qualification.
- When a draft covers both the PCB and the vehicle system (e.g., "this BMS PCB prevents over-charge"), stop at the board-level design description; do not advance to system protection effectiveness.
- EV high-voltage content (OBC, DC-DC, inverter) requires extra care: creepage, clearance, and insulation values must not be given as compliance claims.

---

## Common Misreadings

- `IATF 16949 compliance` in page vocabulary → does NOT mean the supplier is currently certified or that any specific lot has PPAP approval.
- `-40 to 125 °C thermal cycling` in vocabulary → does NOT mean every board lot passes that cycle; it is capability-context framing.
- `ASIL-ready PCB` or `ISO 26262 PCB` → NOT supported; ISO 26262 is a vehicle E/E lifecycle standard, not a PCB manufacturing standard.
- `AEC-Q PCB` → NOT supported; AEC-Q qualifies electronic components, not PCB manufacturing.
- `ADAS PCB supports autonomous driving` → does NOT imply functional safety compliance or OEM approval for any autonomy level.
- `Automotive Ethernet on ECU PCB` → does NOT prove IEEE 100BASE-T1 / 1000BASE-T1 compliance or interoperability.

---

## Must Refresh Before Publishing

- Any IATF 16949 certification status or PPAP completion claim
- Any ASIL allocation, functional safety lifecycle, or ISO 26262 clause-level claim
- Any thermal cycling, vibration, or cleanliness test lot-level pass/fail statement
- Any creepage, clearance, or high-voltage insulation compliance value
- Any OEM approval, customer qualification, or field-deployment claim
- Any automotive network (CAN FD, Automotive Ethernet, FlexRay) interoperability or compliance claim

---

## Cross-Lane Routing

| Content Type | Route To |
|---|---|
| EV charger protocol claims (IEC 61851, ISO 15118, J1772, OCPP) | `wiki/applications/power-energy-pcb-pcba-review-boundaries.md` |
| Radar/sensor RF front-end depth | `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md` |
| Automotive aerospace/medical standards context | `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md` |
| Thermal platform selection (MCPCB, heavy copper, metal core) | `facts/methods/thermal-pcb-platform-selection-posture.md` |
| Conformal coating in EV/automotive context | `facts/methods/conformal-coating-lane-b-rewrite-gate.md` |
| DFM/DFT/DFA review gate positioning | `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md` |

---

## Related Pages

- `facts/applications/automotive-ev-coverage-gap-map.md`
- `wiki/applications/application-routing-and-boundary-map.md`
- `wiki/applications/power-energy-pcb-pcba-review-boundaries.md`
- `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md`
- `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md`

## Primary Sources

- /code/hileap/frontendAPT/public/static/industries/en/automotive-electronics-pcb.json
- https://www.iso.org/publication/PUB200262.html
- https://www.iatfglobaloversight.org/iatf-16949/
- https://www.aecouncil.com/AECDocuments.html
