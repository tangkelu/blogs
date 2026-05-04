---
fact_id: "standards-civil-aerospace-official-assurance-depth"
title: "Civil aerospace official assurance depth: AS9100, DO-160G, DO-254, FAA TSO, AS9102 narrower public metadata with explicit PCB stop lines"
topic: "Civil aerospace assurance standards official-source depth and PCB boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-190 initial build. Supplements facts/standards/civil-aerospace-assurance-boundary.md with narrower official-source public metadata framing for AS9100D/OASIS, DO-160G section structure, DO-254 DAL framework, FAA TSO category examples, and AS9102C first article inspection. Source-backed content from existing registry sources (faa-ac-21-16g-do160-acceptability-page, faa-ac-20-152a-page, rtca-do-160g-product-page, rtca-do-254-product-page, rtca-do-155-product-page, as9102c-first-article-inspection-page). AS9100/OASIS, FAA TSO detail, and ARINC remain public-knowledge-only."
source_ids:
  - "faa-ac-21-16g-do160-acceptability-page"
  - "faa-ac-20-152a-page"
  - "rtca-do-160g-product-page"
  - "rtca-do-254-product-page"
  - "rtca-do-155-product-page"
  - "as9102c-first-article-inspection-page"
notes: "AS9100/OASIS registry, FAA TSO detail pages, ITAR/EAR, and ARINC sources not yet in registry. DO-160G, DO-254, DO-155 have existing source records. AS9102C has existing source record."
tags: ["civil-aerospace", "as9100", "as9102", "do-160g", "do-254", "do-155", "faa-tso", "faa-ac", "arinc", "qualification-boundary", "assurance-depth", "official-source"]
---

# Canonical Summary

> This card provides narrower official-source public metadata framing for the five primary civil aerospace assurance standard families: AS9100D/AS9102 (QMS/FAI), DO-160G (environmental test procedures), DO-254 (airborne hardware design assurance), DO-155 (radar altimeter performance standards), and FAA TSO (device authorization). Content is deepened with source-backed framing from existing RTCA product pages, FAA Advisory Circulars, and AS9102C first-article inspection source. AS9100/OASIS, TSO index, and ITAR/EAR remain at publicly known identity level only.

---

## Assurance Standard 1: AS9100D and AS9102C

### Narrower Official-Source Framing

| Item | Source-Backed or Public Identity |
|---|---|
| **AS9100D** | SAE / IAQG "Quality Management Systems — Requirements for Aviation, Space, and Defense Organizations." Current revision: Rev D (2016), based on ISO 9001:2015 with aerospace-specific requirements (risk management, first-article inspection, counterfeit-part prevention, FOD control, configuration management). |
| **OASIS registry** | IAQG Online Aerospace Supplier Information System — the authoritative live database for AS9100D certificate holders. Certificate validity, scope, and scope exclusions must be verified at oasis.iaqg.org, not from supplier marketing materials. |
| **AS9102C** | SAE / IAQG Aerospace First Article Inspection (FAI) Requirements. Source in registry: `as9102c-first-article-inspection-page`. Defines three types of FAI: full FAI (Part 1), partial FAI (Part 2), and BALLOONED drawing (Part 3). Provides the standard documentation set: Form 1 (design documentation), Form 2 (product accountability), Form 3 (characteristic accountability). |
| **What AS9100D adds to ISO 9001** | Planning of product realization; risk-based thinking for aviation safety; special requirements for externally provided products/services; configuration management; first-article inspection (references AS9102); counterfeit-part prevention; FOD (Foreign Object Damage) prevention. |

### PCB Stop Lines (AS9100D / AS9102C)

| Vocabulary | Status |
|---|---|
| "Aerospace PCB manufactured under AS9100D-aligned QMS discipline" | ✅ SAFE — process-level vocabulary |
| "AS9102C first-article inspection with dimensional accountability and ballooned drawing" | ✅ SAFE — source-backed FAI documentation vocabulary |
| "AS9100D certified PCB" | ❌ BLOCKED — AS9100D certification applies to the organization's QMS, not to individual PCBs |
| "AS9100D certified PCB manufacturer" (without live OASIS verification) | ❌ BLOCKED — certificate validity must be verified from OASIS; marketing statement alone is insufficient |
| "AS9100 scope includes avionics PCB production" (without OASIS scope verification) | ❌ BLOCKED — certificate scope is specific; verify from OASIS |

---

## Assurance Standard 2: DO-160G — Environmental Conditions and Test Procedures

### Narrower Official-Source Framing

| Item | Source-Backed Identity |
|---|---|
| **DO-160G** | RTCA document "DO-160G Environmental Conditions and Test Procedures for Airborne Equipment" (2010). Source in registry: `rtca-do-160g-product-page`. |
| **FAA AC 21-16G recognition** | FAA Advisory Circular AC 21-16G (source in registry: `faa-ac-21-16g-do160-acceptability-page`) recognizes DO-160 versions D, E, F, and G as containing acceptable means of compliance with airworthiness requirements for certain environmental qualifications. DO-160G is preferred for new articles. |
| **Section structure (public knowledge)** | DO-160G contains 27 sections (approximately): Section 4 (Temperature and altitude), Section 5 (Temperature variation), Section 6 (Humidity), Section 7 (Operational shocks and crash safety), Section 8 (Vibration), Section 9 (Explosion proofness), Section 20 (Radio frequency susceptibility), Section 21 (Magnetic effect), Section 22 (Power input), Section 25 (Electrostatic discharge). |
| **Equipment classification** | For each DO-160G section, the equipment category (e.g., Category A/B for temperature, Category S for shock, Category U for vibration) is selected by the applicant based on the intended installation environment — not assigned by the PCB manufacturer. |
| **Testing responsibility** | DO-160G testing is performed by accredited test laboratories on the complete airborne equipment/article, not on the bare PCB or PCBA independently. |

### PCB Stop Lines (DO-160G)

| Vocabulary | Status |
|---|---|
| "PCB for airborne equipment subject to DO-160G environmental qualification" | ✅ SAFE — application-context vocabulary |
| "Board design review considers thermal, vibration, and humidity requirements per DO-160G equipment categories" | ✅ SAFE — design-review context vocabulary |
| "DO-160G Section 8 Vibration Category S passed" | ❌ BLOCKED — section-specific pass-status belongs to the complete equipment article after testing |
| "DO-160G qualified PCB" | ❌ BLOCKED — DO-160G qualification applies to the complete airborne equipment, not the PCB |
| Any specific DO-160G temperature range, g-force, or humidity value | ❌ BLOCKED — requires access to section-level standard text, not recoverable from RTCA product page |

---

## Assurance Standard 3: DO-254 — Design Assurance Guidance for Airborne Electronic Hardware

### Narrower Official-Source Framing

| Item | Source-Backed Identity |
|---|---|
| **DO-254** | RTCA document "DO-254 Design Assurance Guidance for Airborne Electronic Hardware" (2000). Source in registry: `rtca-do-254-product-page`. |
| **FAA AC 20-152A context** | FAA Advisory Circular AC 20-152A (source: `faa-ac-20-152a-page`) provides guidance on the use of DO-254 for airborne electronic hardware design assurance. Explicitly covers circuit-board-assembly hardware as within DO-254 scope. |
| **Design Assurance Level (DAL)** | DO-254 defines DAL A (catastrophic failure effect), B (hazardous), C (major), D (minor), E (no safety effect). DAL is assigned by the system safety assessment (per ARP4761) at the aircraft/system level, not by the PCB manufacturer. |
| **DO-254 process activities** | Planning (PHAC), hardware requirements, conceptual design, detailed design, implementation, production transition, acceptance testing, hardware configuration management, hardware process assurance, and certification liaison. These are lifecycle process activities — not PCB manufacturing steps. |
| **Circuit-board-assembly scope** | FAA AC 20-152A confirms that circuit-board-assembly (CBA) hardware is within DO-254 scope. The PCB manufacturer may manufacture CBA per customer's DO-254 program requirements; they cannot independently assert DAL or DO-254 compliance. |

### PCB Stop Lines (DO-254)

| Vocabulary | Status |
|---|---|
| "PCB assembly manufactured to customer's DO-254 program requirements" | ✅ SAFE — manufacturing-to-requirement vocabulary |
| "DO-254 circuit-board-assembly scope per FAA AC 20-152A context" | ✅ SAFE — source-backed assurance-context vocabulary |
| "DO-254 DAL-B flight controller PCB" | ❌ BLOCKED — DAL is a safety-assessment outcome, not a PCB manufacturing attribute |
| "DO-254 compliant PCBA" | ❌ BLOCKED — DO-254 compliance is a program/lifecycle declaration, not a PCB attribute |
| "DO-254 certified PCB manufacturer" | ❌ BLOCKED — DO-254 does not certify manufacturers; it guides hardware design assurance programs |

---

## Assurance Standard 4: DO-155 — Radar Altimeters

### Narrower Official-Source Framing

| Item | Source-Backed Identity |
|---|---|
| **DO-155** | RTCA "DO-155 Minimum Performance Standards — Airborne Low Range Radar Altimeters." Source in registry: `rtca-do-155-product-page`. |
| **Scope restriction** | DO-155 applies specifically to low-range radar altimeters — the radio altimeter system used for ground proximity sensing in aircraft. It does NOT apply to barometric pressure altimeters, GPS/GNSS altimeters, or laser altimeters. |
| **5G C-band interference context** | FAA studies (EB 107 / FAA-AC-20-199 draft) address interference between 5G C-band ground stations and radio altimeters operating at 4.2–4.4 GHz — relevant to 5G telecom PCB/antenna context. Sources in registry: `faa-eb-107-5g-c-band-aero-studies`, `faa-ac-20-199-draft-radio-altimeter-installation`. |

### PCB Stop Lines (DO-155)

| Vocabulary | Status |
|---|---|
| "Radio altimeter RF front-end board per DO-155 radar altimeter equipment context" | ✅ SAFE — source-backed application-context vocabulary |
| "5G C-band interference risk for radio altimeter PCB front-end" | ✅ SAFE — source-backed interference-context vocabulary (FAA EB 107) |
| "DO-155 compliant radio altimeter PCB" | ❌ BLOCKED — DO-155 qualification applies to the complete radar altimeter equipment |
| Any exact DO-155 altitude range, accuracy, or interference immunity value | ❌ BLOCKED — requires access to standard clause-level text |

---

## Assurance Standard 5: FAA TSO — Technical Standard Order

### Narrower Public Knowledge Framing

| Item | Public Identity |
|---|---|
| **TSO system** | FAA Technical Standard Orders (TSOs) are minimum performance standards issued by the FAA Administrator for specified avionics and aircraft articles. Compliance enables TSO authorization for the named article. |
| **Examples of TSO-C** | TSO-C119 (TCAS II), TSO-C145/C146 (GNSS/GPS receiving equipment), TSO-C151 (TAWS), TSO-C179 (rechargeable lithium batteries), TSO-C206 (traffic awareness beacon system). |
| **Authorization structure** | TSO authorization is granted by FAA to a specific design and manufacturer — not to a generic product class. Each TSO authorization has a defined article name, manufacturer name, and design description. |
| **PCB relevance** | PCBs manufactured for TSO-authorized articles (avionics units) must meet the design requirements established by the TSO holder's approved design. The PCB manufacturer does not hold TSO authorization. |

### PCB Stop Lines (FAA TSO)

| Vocabulary | Status |
|---|---|
| "GNSS receiver PCB for TSO-C145/C146 navigation equipment" | ✅ SAFE — application-context vocabulary |
| "TCAS II processing board for TSO-C119 avionic unit" | ✅ SAFE — application-context vocabulary |
| "TSO-authorized PCB" | ❌ BLOCKED — TSO authorization is granted to the complete avionics article, not to the PCB |
| "TSO-C145 compliant GNSS PCB" | ❌ BLOCKED — compliance with TSO-C145 belongs to the complete avionics unit, not the PCB |

---

## Summary: PCB Stop Lines for Civil Aerospace Assurance Standards

| Standard | PCB-Safe Vocabulary | Blocked Vocabulary |
|---|---|---|
| **AS9100D / AS9102C** | QMS-discipline vocabulary; AS9102C FAI documentation context | AS9100D certification claims, OASIS registration claims, DAL/scope claims without live verification |
| **DO-160G** | Airborne equipment environmental qualification context; section-category framing | Section-specific pass-status, specific test values, "DO-160G qualified PCB" |
| **DO-254** | Circuit-board-assembly scope per FAA AC 20-152A; manufacturing-to-requirement vocabulary | DAL assignment, compliance declaration, "DO-254 certified PCB" |
| **DO-155** | Radio altimeter RF front-end context; 5G C-band interference context | Compliance, exact altitude accuracy, interference immunity values |
| **FAA TSO** | Avionics unit application context (TSO-C number as context) | TSO authorization at PCB level, compliance claims without complete avionics unit |

---

## Remaining Gaps

| Gap | Reopen Condition |
|---|---|
| Official AS9100D SAE/IAQG product page | SAE International AS9100D page added to registry |
| Official OASIS registry access page | IAQG OASIS page added to registry |
| Official FAA TSO index page | FAA TSO index page (faa.gov/aircraft/air_cert/design_approvals/tso/) added to registry |
| DO-160G section-level environmental test vocabulary | Full DO-160G standard text or clause-level FAA AC source |
| DO-254 DAL-level process vocabulary | Full DO-254 standard or clause-level DO-254 planning guidance source |
| Official ARINC 429 / ARINC 664 public standard pages | Aerospace Industries Association (AIA) or ARINC standard page added to registry |
| ITAR USML classification vocabulary | DDTC/State Dept USML page added to registry (currently completely blocked) |
| EAR CCL classification vocabulary | BIS/Commerce Dept CCL page added to registry (currently completely blocked) |
