---
topic_id: "applications-drone-uav-regulatory-routing-boundary"
title: "Drone / UAV Regulatory And RF Routing Boundary"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "standards-drone-uav-regulatory-and-rf-boundary"
  - "standards-drone-uav-official-regulatory-depth"
source_ids:
  - "px4-basic-concepts-guide"
  - "mavlink-overview-page"
  - "expresslrs-getting-started"
  - "frontendapt-industry-drone-uav-page-en"
notes: "No official FAA, EASA, FCC, CE RED, or GNSS source is currently registered locally. This page keeps all regulatory vocabulary at document-identity and routing-boundary level only."
tags: ["drone", "uav", "faa-part-107", "easa-uas", "fcc", "ce-red", "gnss", "rtk", "rf", "regulatory-boundary", "routing"]
---

# Definition

> Drone and UAV regulatory vocabulary is safe only at document-identity and routing-boundary level. FAA Part 107, EASA UAS categories, FCC RF authorization, CE RED, and GNSS / RTK all operate at aircraft, RF-device, navigation-system, or operator level. This page exists to let future agents route those terms safely without turning them into PCB certification, authorization, qualification, or performance claims.

## Why This Page Exists

This page turns scattered blocked-claim rules into a reusable routing surface. It is meant to answer one narrow question: when a draft mentions FAA, EASA, FCC, CE RED, GNSS, or RTK, what can the wiki safely say at PCB / PCBA level, and where must the claim stop?

## Routing Rule

- Safe use: document identity, regulatory-family identity, board-class vocabulary, RF-interface vocabulary, and system-context routing.
- Unsafe use: legal validity, certification validity, qualification status, authorization status, supplier proof, or commercial outcome claims.
- When a draft needs device-level conformity, authorization, or navigation-performance proof, stop here and reopen a narrower evidence lane.

## Regulatory Families

### FAA Part 107 (US)

**Document identity:**
- `FAA Part 107` is 14 CFR Part 107, the FAA's rules for Small Unmanned Aircraft Systems (UAS) in the US. It covers UAS weighing below 55 lbs MTOW operated in the US National Airspace System for civil purposes.
- `FAA Remote ID` (14 CFR Part 89) requires UAS to broadcast identity and location during flight — a system-level and UAS-firmware broadcast requirement.
- FAA registration is per-aircraft, not per-component.

**What Part 107 reaches:**
- The UAS operator and the complete aircraft as an operational unit in US airspace.

**PCB-stop line:**
- PCB board vocabulary (flight controller PCB, IMU board, barometer/GNSS module board, autopilot PCBA) is safe.
- FAA Part 107 authorization is an operational authorization for a specific UAS and operator — not a PCB attribute.
- Remote ID broadcast is a firmware and RF transmission behavior of the complete aircraft — not a PCB manufacturing attribute.

**Blocked at PCB level:**
- `"FAA Part 107 compliant PCB"`, `"FAA-authorized flight controller"`, `"Remote ID compliant PCB"` — all unsupported.

### EASA UAS Regulation (EU)

**Document identity:**
- `EU 2019/947` establishes the Open, Specific, and Certified categories for UAS operations in EU airspace.
- `Open Category` covers low-risk operations in A1/A2/A3 sub-categories based on MTOW and proximity to people.
- `Specific Category` requires SORA risk assessment or pre-approved Standard Scenario (STS) authorization.
- `Certified Category` requires aircraft type certification and operator licensing.
- `EU 2019/945` (Delegated Regulation) sets CE class markings C0–C6 for UAS placed on the EU market — applied to the complete UAS product.

**What EASA UAS reaches:**
- The complete UAS aircraft and its operator in EU airspace; the CE class marking applies to the complete UAS product placed on the EU market.

**PCB-stop line:**
- UAV PCB vocabulary (autopilot board, ESC PCBA, BMS board, RF communication module board) is safe.
- EASA Open/Specific/Certified category and CE class marking (C0–C6) apply to the complete UAS product — not to the PCB.

**Blocked at PCB level:**
- `"EASA Open Category PCB"`, `"CE C2 class flight controller"`, `"EASA Specific Category compliant ESC"` — all unsupported.

### FCC RF Authorization (US)

**Document identity:**
- `FCC Part 15` governs unlicensed intentional radiators including 2.4 GHz, 5.8 GHz, and 900 MHz RC links, telemetry radios, and FPV video transmitters. Authorization is per complete RF device.
- `FCC Part 97` governs Amateur Radio Service; some long-range links (ExpressLRS at 433 MHz / 915 MHz) operate under Part 97 when used by licensed amateur operators.
- `FCC ID` is a device-level authorization number assigned after TCB/laboratory testing of the complete RF module or device.

**What FCC authorization reaches:**
- The complete RF device (RC transmitter/receiver module, telemetry radio, FPV VTX) as a unit — not the PCB inside it.

**PCB-stop line:**
- RF PCB vocabulary (RC receiver PCB, telemetry radio board, 2.4 GHz / 900 MHz module PCB, RF ground plane, antenna feed trace, impedance-controlled trace) is safe.
- FCC ID authorization belongs to the complete RF module or device — not to the PCB substrate or assembly.
- EIRP, frequency band, spurious emissions, and conducted power are device-level parameters — not PCB manufacturing parameters.

**Blocked at PCB level:**
- `"FCC ID PCB"`, `"FCC Part 15 compliant PCB"`, `"FCC certified RC receiver PCB"` — all unsupported.

### CE Radio Equipment Directive / RED (EU)

**Document identity:**
- `CE RED (2014/53/EU)` is the EU Radio Equipment Directive; mandatory for radio equipment placed on the EU market. Requires conformity assessment covering health/safety, EMC, and radio spectrum requirements.
- `EN 300 328` (2.4 GHz) and `EN 301 893` (5 GHz) are harmonized ETSI standards under the RED for the respective bands.
- CE marking is placed on the complete radio device after conformity assessment and DoC (Declaration of Conformity).

**What CE RED reaches:**
- The complete radio device placed on the EU market — firmware, RF performance, and safety as a unit.

**PCB-stop line:**
- RF PCB manufacturing vocabulary (RF layer, controlled impedance, matching network, shielding pad) is safe.
- CE RED conformity applies to the complete device — not to the bare PCB or PCBA.

**Blocked at PCB level:**
- `"CE RED compliant PCB"`, `"CE marked RF PCB"`, `"EN 300 328 PCB"` — all unsupported.

### GNSS / RTK Navigation

**Document identity:**
- `GPS` (L1 C/A at 1575.42 MHz, L2, L5): US NAVSTAR constellation. Accuracy depends on receiver quality, firmware, satellite geometry, and correction methods.
- `GLONASS`, `BeiDou (BDS)`, `Galileo`: Russian, Chinese, EU GNSS constellations. Multi-constellation receivers use signals from 2–4 constellations.
- `RTK (Real-Time Kinematic)`: Differential correction technique achieving centimeter-level accuracy. Requires a compatible receiver, base station or NTRIP correction service, and firmware support.
- `NTRIP`: Internet protocol for streaming RTCM correction data to RTK receivers.

**What GNSS/RTK accuracy reaches:**
- The complete GNSS receiver, its firmware, the satellite signals available, and the correction data source together determine accuracy — not the PCB.

**PCB-stop line:**
- GNSS module PCB vocabulary (GNSS module footprint, GPS/GLONASS/BeiDou/Galileo multi-constellation receiver board, RF ground plane, u.FL/IPEX antenna connector, RTK positioning board hardware description) is safe.
- Accuracy (CEP, RMS), fix rate, TTFF, anti-jamming, anti-spoofing, and RTK precision are receiver firmware and system-level attributes.

**Blocked at PCB level:**
- `"GPS accurate PCB"`, `"RTK precision GNSS PCB"`, `"anti-jamming GNSS board"`, `"centimeter-level PCB"` — all unsupported.

## RC Protocol Identity (Existing Fact Card Extension)

Per `facts/methods/remote-control-and-drone-control-stack-boundary.md`:

| Protocol | Safe Vocabulary | Blocked |
|---|---|---|
| **PX4** | Open-source autopilot platform identity, vehicle/sensor/actuator architecture vocabulary | Performance benchmarks, reliability stats, compatibility guarantees |
| **MAVLink** | Communication protocol identity for drone/vehicle ecosystems | Latency, throughput, link-quality claims |
| **ExpressLRS** | Open-source RC control-link ecosystem identity | Range, latency, anti-interference, penetration claims |
| **ArduPilot** | Open-source autopilot software identity | Stability, accuracy, compatibility claims |

## Explicit Non-Claims

- This page does not support legal or certification-validity claims.
- It does not support qualification pass-status claims.
- It does not support supplier-proof claims.
- It does not support cost, lead-time, or yield claims.
- It does not support device-level FAA, EASA, FCC, CE RED, GNSS, or RTK certification conclusions.

## Routing Summary

| Content Type | Route To |
|---|---|
| Drone/UAV PCB board vocabulary (FC, ESC, BMS, GCS, payload) | `wiki/applications/drone-uav-pcb-pcba-boundary-map.md` |
| FAA Part 107 / Remote ID regulatory identity | This page + `facts/standards/drone-uav-regulatory-and-rf-boundary.md` |
| EASA UAS category / CE class marking identity | This page + `facts/standards/drone-uav-regulatory-and-rf-boundary.md` |
| FCC Part 15/97 RF authorization identity | This page + `facts/standards/drone-uav-regulatory-and-rf-boundary.md` |
| CE RED / ETSI harmonized standard identity | This page + `facts/standards/drone-uav-regulatory-and-rf-boundary.md` |
| GNSS/RTK accuracy and protocol identity | This page + `facts/standards/drone-uav-regulatory-and-rf-boundary.md` |
| RC/autopilot control-stack identity (PX4, MAVLink, ExpressLRS) | `facts/methods/remote-control-and-drone-control-stack-boundary.md` |
| Defense/military UAV (MIL-STD, airworthiness, DO-254) | `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md` |
| Civil avionics / DO-254 hardware assurance (non-drone) | `wiki/applications/civil-aerospace-pcb-pcba-boundary-map.md` |

## Must Refresh Before Publishing

- Any FAA Part 107 waiver, authorization, or airspace approval claims
- Any EASA Open/Specific/Certified category authorization or CE class marking (C0–C6) claims
- Any FCC ID, Part 15, or Part 97 authorization claims for any RF device
- Any CE RED conformity or ETSI harmonized standard compliance claims
- Any GNSS accuracy (CEP, RMS), RTK precision, TTFF, anti-jamming, or anti-spoofing claims
- Any RF range, EIRP, link budget, conducted power, or spectral mask claims
- No official FAA, EASA, FCC, CE RED, or GNSS source currently in registry — all regulatory-identity framing is from publicly known metadata only

## Common Misreadings

- `"FAA Part 107 compliant flight controller PCB"` → Part 107 is an operational authorization for a UAS in US airspace; the PCB does not receive Part 107 authorization.
- `"EASA C2 class drone PCB"` → CE class C0–C6 marks the complete UAS product placed on the EU market; the PCB alone cannot have CE class marking.
- `"FCC certified RC receiver PCB"` → FCC ID authorizes the complete RF device/module, not the PCB substrate.
- `"RTK precision GNSS PCB"` → RTK accuracy is a receiver firmware + correction-service outcome; the PCB provides the hardware substrate but does not determine accuracy.
- `"anti-jamming GNSS board"` → anti-jamming is a receiver firmware/hardware feature at chipset level, not a PCB manufacturing attribute.
- `"2.4 GHz long-range PCB"` → range is a system-level RF outcome (EIRP, receiver sensitivity, link budget, environment); not a PCB attribute.

## Related Pages

- `facts/standards/drone-uav-regulatory-and-rf-boundary.md`
- `facts/standards/drone-uav-official-regulatory-depth.md`
- `wiki/applications/drone-uav-pcb-pcba-boundary-map.md`
- `facts/applications/drone-uav-coverage-gap-map.md`
- `facts/methods/remote-control-and-drone-control-stack-boundary.md`
- `wiki/processes/remote-control-and-drone-control-stack-boundaries.md`
- `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md`
- `wiki/applications/civil-aerospace-pcb-pcba-boundary-map.md`
