---
fact_id: "standards-drone-uav-regulatory-and-rf-boundary"
title: "Drone / UAV regulatory and RF standards (FAA Part 107, EASA UAS, FCC RF, CE RF, GNSS/RTK) are aircraft/device/operator authorization boundaries, not PCB qualification proof"
topic: "Drone and UAV regulatory and RF standards identity and PCB boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "px4-basic-concepts-guide"
  - "mavlink-overview-page"
  - "expresslrs-getting-started"
  - "frontendapt-industry-drone-uav-page-en"
notes: "No official FAA Part 107, EASA UAS, FCC Part 15/97, CE RE directive, or GNSS standard source is currently in the sources registry. This card uses publicly known regulatory-identity metadata to establish document-level boundary framing only. Refresh to add official sources when recovered."
tags: ["drone", "uav", "faa-part-107", "easa-uas", "fcc", "ce", "gnss", "rtk", "mavlink", "px4", "expresslrs", "rf", "regulatory-boundary", "standards-boundary"]
---

# Canonical Summary

> FAA Part 107 (US small-UAS rules), EASA UAS Regulation (EU Open/Specific/Certified categories), FCC Part 15/Part 97 RF authorizations, CE Radio Equipment Directive (RED), and GNSS/RTK accuracy standards are aircraft/device/operator-level regulatory frameworks. They authorize UAS operations, RF device marketing, or navigation-system performance for the complete aircraft or device — not for the PCB or PCBA. Mentioning these regulatory names in PCB/PCBA content is safe only as document-identity framing; it is not safe as certification, authorization, compliance, or performance proof at the PCB level.

## Regulatory Families

### FAA Part 107 — US Small Unmanned Aircraft Systems

| Item | Identity (Public Knowledge) |
|---|---|
| **FAA Part 107** | US Code of Federal Regulations 14 CFR Part 107 — Small Unmanned Aircraft Systems. Establishes rules for civilian UAS operations below 55 lbs MTOW in the US National Airspace System. |
| **FAA Registration** | Required for UAS ≥ 0.55 lbs / 250 g for outdoor operations; registration is of the aircraft, not a PCB or component. |
| **Remote ID** | FAA Remote ID rule (14 CFR Part 89) requires Standard Remote ID broadcast from the UAS — a system-level and device-level broadcast requirement, not a PCB specification. |
| **TRUST** | FAA The Recreational UAS Safety Test — operator knowledge test; not a PCB or hardware requirement. |

**PCB boundary for FAA Part 107:**
- Flight controller PCB vocabulary (MCU/SoC, IMU, barometer, GNSS module board) is safe.
- FAA Part 107 authorization, waiver, or airspace approval belong to the UAS operator and aircraft — not to the PCB manufacturer.
- Remote ID broadcast is a UAS-system firmware + RF transmission requirement — not a PCB manufacturing attribute.
- "FAA Part 107 compliant PCB" and "FAA-authorized flight controller PCB" are unsupported claims.

---

### EASA UAS Regulation — EU Drone Categories

| Item | Identity (Public Knowledge) |
|---|---|
| **EASA UAS Regulation** | EU (EU) 2019/947 and related acts — establishes Open, Specific, and Certified categories for UAS operations in EU airspace. |
| **Open Category** | Low-risk UAS operations; divided into A1/A2/A3 sub-categories based on MTOW, proximity to people, and operator registration. |
| **Specific Category** | Medium-risk operations; requires SORA (Specific Operations Risk Assessment) authorization or pre-defined scenarios (STS). |
| **Certified Category** | High-risk operations; aircraft must be type-certified, operator must be licensed. |
| **CE Marking for UAS** | UAS sold in the EU market in Open Category must carry CE class marking (C0–C6) per EU Delegated Regulation 2019/945. |

**PCB boundary for EASA UAS:**
- UAS PCB vocabulary (autopilot board, ESC, BMS, communication module board) is safe.
- EASA Open/Specific/Certified category is a UAS operation authorization — not a PCB classification.
- CE class marking (C0–C6) applies to the complete UAS product placed on the EU market — the PCB alone does not hold a CE UAS class marking.
- "EASA Open Category PCB" and "CE C2 class flight controller PCB" are unsupported claims.

---

### FCC RF Authorization — US

| Item | Identity (Public Knowledge) |
|---|---|
| **FCC Part 15** | FCC rules for unlicensed intentional, unintentional, and incidental radiators. Applies to RF devices including RC transmitters/receivers, 2.4 GHz and 5.8 GHz links, and telemetry radios at device level. |
| **FCC Part 97** | FCC Amateur Radio Service rules. Some long-range RC links (e.g., ExpressLRS on 433 MHz / 915 MHz) operate under Part 97 in the US when used by licensed amateur operators. |
| **FCC ID** | Device-level authorization number issued to RF device by FCC after TCB or laboratory testing. Applies to the complete RF module or device — not to the PCB. |

**PCB boundary for FCC RF:**
- RF module PCB vocabulary (RC receiver board, telemetry radio PCB, 2.4 GHz / 900 MHz link board, antenna feed and ground-plane layout) is safe.
- FCC ID authorization belongs to the complete RF device/module submitted for certification — not to the PCB.
- EIRP, frequency band, emission bandwidth, spurious emission, and conducted power are device-level or component-level RF parameters — not PCB manufacturing claims.
- "FCC ID PCB", "FCC Part 15 compliant PCB", or "FCC certified RC receiver PCB" are unsupported claims.

---

### CE Radio Equipment Directive (RED) — Europe

| Item | Identity (Public Knowledge) |
|---|---|
| **CE RED (2014/53/EU)** | EU Radio Equipment Directive — mandatory before placing radio equipment on the EU market. Requires conformity assessment covering health/safety, EMC, and radio spectrum requirements. |
| **CE Marking** | Device/product-level conformity declaration; placed on the complete radio device after testing and technical documentation. |
| **EN 300 328** | ETSI standard for 2.4 GHz wideband transmission — harmonized standard under RED; applies to the device. |
| **EN 301 893** | ETSI standard for 5 GHz wideband transmission — harmonized standard under RED; applies to the device. |

**PCB boundary for CE RED:**
- RF PCB manufacturing vocabulary (RF layer, matching network, antenna pad, impedance-controlled trace, shielding pad) is safe.
- CE RED conformity applies to the complete radio device placed on the EU market — not to the bare PCB or PCBA.
- "CE RED compliant PCB" and "CE marked RF PCB" are unsupported claims.

---

### GNSS / RTK Navigation Standards

| Item | Identity (Public Knowledge) |
|---|---|
| **GPS (US NAVSTAR)** | US Global Positioning System; L1 C/A (1575.42 MHz), L2, L5 frequency bands; accuracy depends on receiver quality, firmware, and satellite geometry. |
| **GLONASS** | Russian GNSS constellation; compatible with multi-constellation receivers. |
| **BeiDou (BDS)** | Chinese GNSS constellation; multi-frequency. |
| **Galileo** | EU GNSS constellation; E1/E5 bands. |
| **RTK (Real-Time Kinematic)** | Post-processing / real-time differential correction technique achieving centimeter-level accuracy; requires a base station or NTRIP correction service plus compatible receiver firmware. |
| **NTRIP** | Networked Transport of RTCM via Internet Protocol — correction data streaming protocol for RTK. |

**PCB boundary for GNSS/RTK:**
- GNSS module board vocabulary (GNSS/GPS module footprint, RF ground plane, antenna trace, multi-constellation receiver board, RTK positioning board hardware description) is safe.
- Accuracy (CEP, RMS, horizontal/vertical), fix rate, TTFF, anti-jamming performance, and anti-spoofing capability are GNSS receiver firmware and system-level attributes — not PCB manufacturing attributes.
- RTK centimeter-level accuracy is achieved by the combined receiver firmware + correction service system — not by the PCB.
- "GPS accurate PCB", "RTK precision PCB", "anti-jamming GNSS PCB" are unsupported claims.

---

### RC / Telemetry Protocol Identity (Existing Fact Card Extension)

Per `facts/methods/remote-control-and-drone-control-stack-boundary.md` (already in corpus):

| Protocol/Platform | Identity Level Safe Use | Blocked |
|---|---|---|
| **PX4** | Open-source autopilot platform identity | Performance benchmarks, reliability statistics, compatibility guarantees |
| **MAVLink** | Communication protocol identity; used in drone and vehicle ecosystems | Telemetry latency, link quality, throughput claims |
| **ExpressLRS** | Open-source RC control-link ecosystem identity (transmitter + receiver setup vocabulary) | Range, latency, anti-interference, penetration claims |
| **ArduPilot** | Open-source autopilot software identity | Stability, accuracy, or compatibility guarantees |

---

## Stable Facts

- FAA Part 107, EASA UAS, FCC Part 15/97, CE RED, and GNSS standards all operate at aircraft, device, or operator level — none creates PCB-level certification, authorization, or qualification status.
- RF frequency identity vocabulary (2.4 GHz, 900 MHz, 1.2 GHz, 5.8 GHz, GPS L1) is safe as architecture-level context — it is not safe as compliance, EIRP, range, or interference characteristic.
- No official FAA, EASA, FCC, ETSI/CE RED, or GNSS standard source is currently in the sources registry. This card uses publicly known regulatory-identity metadata.
- The existing `methods-remote-control-and-drone-control-stack-boundary` fact card already establishes PX4, MAVLink, and ExpressLRS identity. This card adds the regulatory and RF authorization layer.

## Conditions And Methods

- Use this card for any drone/UAV draft that mentions FAA Part 107, EASA UAS categories, FCC authorization, CE RED, or GNSS/RTK accuracy by name.
- Pair with `wiki/applications/drone-uav-pcb-pcba-boundary-map.md` for full application routing.
- Pair with `wiki/applications/drone-uav-regulatory-routing-boundary.md` for the prompt-consumable companion.
- For defense/military UAV (MIL-STD, airworthiness, DO-254), route to `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md`.
- When official FAA, EASA, FCC, or GNSS sources are added to the registry, refresh this card.

## Limits And Non-Claims

- FAA Part 107 waiver, airspace authorization, or registration claims NOT supported.
- EASA Open/Specific/Certified category authorization NOT supported.
- Remote ID broadcast compliance NOT supported.
- FCC ID, FCC Part 15/97 authorization, or CE RED conformity for any device NOT supported.
- GNSS/RTK accuracy, fix rate, TTFF, anti-jamming, anti-spoofing claims NOT supported.
- RF range, EIRP, link budget, spectral mask claims NOT supported.
- Autonomy, BVLOS, swarm performance claims NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|-----|-----------------|
| Official FAA Part 107 / Remote ID source | FAA regulatory page added to registry |
| Official EASA UAS regulation source | EASA regulation page added to registry |
| Official FCC Part 15 / FCC ID source | FCC page added to registry |
| Official CE RED / ETSI harmonized standard source | EU RED or ETSI page added to registry |
| Official GNSS constellation / RTK standard source | ITU, GPS.gov, or ESA page added to registry |
| Promote wiki page draft → active | Content review pass |
