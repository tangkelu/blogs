---
fact_id: "standards-drone-uav-official-regulatory-depth"
title: "Drone / UAV official regulatory depth: FAA Part 107, Remote ID, EASA open category, FCC equipment authorization, GNSS/RTK public identity metadata with explicit PCB stop lines"
topic: "Drone and UAV official regulatory source depth and PCB boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-189 initial build. Supplements facts/standards/drone-uav-regulatory-and-rf-boundary.md with deeper official-source public metadata framing for FAA Part 107 (14 CFR 107), FAA Remote ID (14 CFR 89), EASA UAS Open Category regulation, FCC equipment authorization (FCC Part 15), and GNSS/RTK positioning identity. All based on publicly available regulatory-organization identity pages and CFR/regulatory text identity. No new sources added to registry — official FAA, EASA, FCC, and GNSS sources not yet recovered."
source_ids:
  - "px4-basic-concepts-guide"
  - "mavlink-overview-page"
  - "expresslrs-getting-started"
  - "frontendapt-industry-drone-uav-page-en"
notes: "Official FAA, EASA, FCC, and GNSS/RTK sources not yet in registry. Content uses publicly known regulatory-identity metadata from official regulatory organization websites (faa.gov, easa.europa.eu, fcc.gov, gps.gov). Refresh source_ids when official pages are recovered."
tags: ["drone", "uav", "faa-part-107", "remote-id", "easa-uas", "fcc-part-15", "fcc-equipment-authorization", "gnss", "rtk", "rf-authorization", "regulatory-depth", "official-source"]
---

# Canonical Summary

> This card provides deeper official-source public metadata framing for the four most-referenced drone/UAV regulatory domains: FAA Part 107 + Remote ID (US UAS operations rules), EASA UAS Open Category (EU UAS operation framework), FCC Equipment Authorization (US RF device authorization for RC and telemetry links), and GNSS/RTK (satellite positioning identity and accuracy context). All operate at aircraft/device/operator level. None creates PCB-level certification, authorization, compliance, or accuracy status. PCB vocabulary must stop at board-class and RF-interface context level.

---

## Regulatory Domain 1: FAA Part 107 and Remote ID (US)

### Official-Source Public Metadata

| Item | Official Regulatory Identity |
|---|---|
| **FAA Part 107** | 14 CFR Part 107 "Small Unmanned Aircraft Systems" — established 2016, amended 2021+. Covers unmanned aircraft operations below 55 lbs (25 kg) MTOW in US NAS for civil commercial and recreational purposes. |
| **Core rules** | Must fly below 400 ft AGL in uncontrolled airspace; requires Remote Pilot Certificate or registration; waiver system for restricted operations; VLOS (visual line of sight) required by default. |
| **FAA Remote ID** | 14 CFR Part 89 "Remote Identification of Unmanned Aircraft" — mandatory Standard Remote ID broadcast using RF or network broadcast; applies to UAS ≥ 250 g from Sep 2023. Requirements are for the complete UAS and its broadcast module, not for individual PCBs. |
| **FAA Registration** | 14 CFR Part 48 — UAS registration is per-aircraft identification number, not per-component or PCB. |
| **Authorization entity** | Federal Aviation Administration (FAA), US Department of Transportation. Official source: faa.gov/uas |

### PCB Stop Lines (FAA)

| Vocabulary | Status |
|---|---|
| "Flight controller PCB for FAA Part 107 UAS operations" | ✅ SAFE — application context |
| "Remote ID module PCB with RF broadcast interface" | ✅ SAFE — board-class/interface context |
| "FAA Part 107 authorized flight controller PCB" | ❌ BLOCKED — Part 107 authorizes operations, not PCBs |
| "FAA Remote ID compliant PCB" | ❌ BLOCKED — Remote ID compliance is UAS-system level |
| "FAA-registered PCBA" | ❌ BLOCKED — FAA registration applies to the aircraft, not to the PCB |

---

## Regulatory Domain 2: EASA UAS Open Category (EU)

### Official-Source Public Metadata

| Item | Official Regulatory Identity |
|---|---|
| **EU 2019/947** | Commission Implementing Regulation (EU) 2019/947 — defines UAS operating rules in EU: Open, Specific, and Certified categories based on risk. Open category allows lower-risk operations without individual authorization. |
| **EU 2019/945** | Commission Delegated Regulation (EU) 2019/945 — defines technical requirements and CE class designations (C0–C6) for UAS placed on the EU market. C0 = lowest risk (< 250 g), C6 = highest (for Specific category). |
| **Open Category sub-categories** | A1 (fly over people, C0/C1 class), A2 (fly near people, C2 class), A3 (away from people, C3/C4 class) |
| **CE Class Marking** | CE class marking (C0–C6) on the complete UAS product — not on any individual component or PCB. |
| **Authorization entity** | European Union Aviation Safety Agency (EASA). Official source: easa.europa.eu/en/domains/civil-drones |

### PCB Stop Lines (EASA)

| Vocabulary | Status |
|---|---|
| "Autopilot PCB for EASA Open Category C2 UAS" | ✅ SAFE — application-context vocabulary |
| "ESC board for EU-market drone with CE class marking" | ✅ SAFE — application-context vocabulary |
| "EASA Open Category A2 compliant flight controller PCB" | ❌ BLOCKED — A2 sub-category is an operational authorization, not a PCB attribute |
| "CE C2 class marked PCB" | ❌ BLOCKED — CE class marking applies to the complete UAS, not the PCB |
| "EU 2019/945 compliant PCB" | ❌ BLOCKED — regulation applies to the complete UAS product placed on the EU market |

---

## Regulatory Domain 3: FCC Equipment Authorization (US RF)

### Official-Source Public Metadata

| Item | Official Regulatory Identity |
|---|---|
| **FCC Part 15** | 47 CFR Part 15 — FCC rules for intentional, unintentional, and incidental radiators. Most RC transmitter/receiver links (2.4 GHz, 5.8 GHz) and telemetry radios require Part 15 authorization before US market placement. |
| **FCC ID** | Unique alphanumeric device identifier assigned by FCC after Certification (TCB or SDoC) testing — applies to the complete RF device/module placed on the US market. Format: FCC ID = applicant code + product code. |
| **Certification types** | Certification (TCB review), Supplier's Declaration of Conformity (SDoC), or Verification — method depends on device class. |
| **FCC Part 97** | 47 CFR Part 97 Amateur Radio Service — some long-range RC links (ExpressLRS at 433 MHz/915 MHz) operate under Part 97 when used by licensed US amateur operators. |
| **Authorization entity** | Federal Communications Commission (FCC), US. Official source: fcc.gov/equipment-authorization-overview |

### PCB Stop Lines (FCC)

| Vocabulary | Status |
|---|---|
| "2.4 GHz RC receiver PCB with antenna trace and ground plane" | ✅ SAFE — board-class/RF interface vocabulary |
| "Telemetry radio PCB with 900 MHz RF front-end" | ✅ SAFE — board-class/interface vocabulary |
| "FCC ID XXXXX RC receiver PCB" | ❌ BLOCKED — FCC ID applies to the complete RF device, not the PCB alone |
| "FCC Part 15 certified PCB" | ❌ BLOCKED — Part 15 authorization is device/module level |
| "FCC-approved RF PCB" | ❌ BLOCKED — FCC authorization applies to the complete RF device as tested |

---

## Regulatory Domain 4: GNSS / RTK Positioning Identity

### Official-Source Public Metadata

| Item | Official Regulatory / Standards Identity |
|---|---|
| **GPS (US NAVSTAR)** | Global Positioning System operated by the US Space Force / AFSPC. L1 C/A (1575.42 MHz), L2 (1227.60 MHz), L5 (1176.45 MHz) civil signals. Official GPS accuracy information: gps.gov/systems/gps/performance/accuracy/ |
| **GPS accuracy context** | GPS.gov states standard GPS ≈ 3.5 m or better horizontal accuracy for SPS (Standard Positioning Service) under open sky. Actual receiver performance depends on firmware, satellite geometry (DOP), and environmental conditions. |
| **GLONASS / BeiDou / Galileo** | Russian / Chinese / EU GNSS constellations — each maintains official performance documentation. Multi-constellation receivers can improve accuracy and availability. |
| **RTK (Real-Time Kinematic)** | Differential GNSS correction technique achieving centimeter-level accuracy; requires base station or NTRIP correction stream plus receiver firmware support. Not a certification standard — an implementation technique. |
| **SBAS** | Satellite-Based Augmentation Systems (WAAS/US, EGNOS/EU, etc.) — improve GPS accuracy for aviation and precision users. |

### PCB Stop Lines (GNSS/RTK)

| Vocabulary | Status |
|---|---|
| "GNSS multi-constellation receiver board with RF ground plane" | ✅ SAFE — board-class/RF interface vocabulary |
| "RTK positioning board with u-blox or equivalent GNSS module footprint" | ✅ SAFE — board-class/module interface vocabulary |
| "GPS accurate PCB — 3.5 m horizontal accuracy" | ❌ BLOCKED — GPS accuracy is a receiver-system + satellite-geometry outcome, not a PCB attribute |
| "RTK precision PCB — centimeter accuracy guaranteed" | ❌ BLOCKED — RTK accuracy depends on correction service + firmware + satellite geometry, not PCB manufacturing |
| "Anti-jamming GNSS PCB" | ❌ BLOCKED — anti-jamming is receiver firmware + antenna architecture capability, not PCB manufacturing |

---

## Summary: PCB Stop Lines for Drone/UAV Regulatory Standards

| Regulatory Domain | Safe Vocabulary | Blocked Vocabulary |
|---|---|---|
| **FAA Part 107 + Remote ID** | Flight controller / Remote ID module board-class identity; application context | FAA Part 107 authorization, Remote ID compliance, FAA registration at PCB level |
| **EASA UAS Open Category** | Autopilot/ESC board-class identity; EU market drone application context | EASA category authorization, CE class marking, EU 2019/945 compliance at PCB level |
| **FCC Equipment Authorization** | 2.4 GHz/5.8 GHz/900 MHz RF PCB board-class identity; RF interface vocabulary | FCC ID, FCC Part 15 certification, FCC approval at PCB level |
| **GNSS / RTK** | GNSS module footprint board-class identity; RF ground plane/antenna vocabulary | GPS accuracy, RTK centimeter accuracy, anti-jamming capability at PCB level |

---

## Remaining Gaps

| Gap | Reopen Condition |
|---|---|
| Official FAA Part 107 regulatory text page | faa.gov/uas or 14 CFR Part 107 page added to sources registry |
| Official FAA Remote ID regulatory text page | faa.gov/uas/getting_started/remote_id page added to registry |
| Official EASA EU 2019/947 / EU 2019/945 pages | EASA regulation page added to registry |
| Official FCC Part 15 / equipment authorization overview page | fcc.gov page added to registry |
| Official GPS.gov performance/accuracy page | gps.gov accuracy page added to registry |
| Official GLONASS / BeiDou / Galileo accuracy pages | Official constellation authority pages added to registry |
| BVLOS / advanced operations vocabulary | Official FAA BVLOS ARC report or rulemaking page |
| Swarm / urban air mobility vocabulary | Official FAA or EASA UAM/AAM regulatory guidance page |
