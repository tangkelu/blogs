---
topic_id: "applications-civil-aerospace-pcb-pcba-boundary-map"
title: "Civil Aerospace PCB PCBA Boundary Map"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
activated_at: "2026-05-03"
activation_notes: "P4-169 review pass: boundary language stable, all 5 board families have safe/blocked pairs, civil-vs-defense routing decision table present, 9-entry aviation standards context table complete (DO-160G/DO-254/AS9100/TSO/ITAR all correctly bounded), must-refresh and cross-lane routing present. AS9100 trust-bar risk explicitly addressed. ITAR complete block confirmed. Promoted to active."
fact_ids:
  - "applications-civil-aerospace-coverage-gap-map"
  - "applications-application-coverage-gap-map"
  - "standards-aviation-altimeter-standards-metadata-boundary"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"
  - "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-hidden-joint-xray-inspection-boundary"
source_ids:
  - "frontendapt-industry-aerospace-defense-page-en"
  - "faa-ac-20-152a-page"
  - "faa-ac-21-16g-do160-acceptability-page"
  - "rtca-do-160g-product-page"
  - "rtca-do-254-product-page"
  - "as9102c-first-article-inspection-page"
tags: ["civil-aerospace", "avionics", "flight-control", "navigation", "do-160g", "do-254", "faa", "as9100", "as9102", "pcb", "pcba", "boundary-map", "application-boundary"]
---

# Definition

> Civil aerospace PCB/PCBA writing is safe at board-class, layout-context, and documentation-discipline vocabulary. It is unsafe when it crosses into AS9100 certification status, DO-160G qualification pass-status, DO-254 design-assurance level (DAL), airworthiness approval (TSO, STC), ITAR/export-control compliance, or mission/program outcomes. Use this page for civil commercial aviation content. Use `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md` for defense/military aviation.

## Why This Topic Matters

- Civil aerospace vocabulary (`AS9100 certified`, `DO-160G qualified`, `DO-254 DAL-B`, `airworthy`, `TSO-authorized`) reads as certification proof when it is only standards-context framing or marketing.
- The Tier-2 aerospace-defense source contains `"AS9100 Certified – Mission Assurance"` as a trust-bar label. This is marketing framing, NOT a current certificate or OASIS listing. It must not appear as certification proof in published content.
- The shared Tier-2 source covers both civil and defense aerospace. This page separates civilian aviation content (commercial aircraft, civil avionics, civil navigation) from defense-specific contexts that require the defense page.

---

## Routing Decision: Civil vs. Defense Aerospace

| Context | Route To |
|---|---|
| Civil/commercial aviation (commercial aircraft avionics, civil navigation, air traffic systems) | **This page** |
| Defense/military aviation (EW, ISR, radar, guided systems, MIL-STD) | `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md` |
| Altimeter-specific slug content (DO-155, DO-160G, radio/barometric/laser altimeter) | `wiki/processes/altimeter-aviation-standards-and-assurance-boundaries.md` |
| UAV/drone flight controller (civilian platform) | `wiki/applications/drone-uav-pcb-pcba-boundary-map.md` |

---

## Board Family Routing

### Avionics / Flight Control / Navigation PCBs

**Safe angles:**
- High-reliability digital and mixed-signal board vocabulary: multilayer processor, FPGA, memory, mixed-signal interface with controlled impedance and noise management description
- Redundant architecture vocabulary: redundant channel, voting logic, cross-monitoring, segmented power domain layout description — framed as customer-design support only, NOT safety-function certification
- Navigation and sensor interface vocabulary: air-data sensor, IMU, GPS/GNSS, altimeter sensor interface PCB description (identity-level only)
- Cockpit display and HMI vocabulary: display PCB, control panel PCBA, keypad/knob board description

> **For altimeter-specific content** (DO-155, barometric, radio altimeter, laser ToF), route to `wiki/processes/altimeter-aviation-standards-and-assurance-boundaries.md`.

**Blocked:**
- DO-254 DAL assignment (DAL-A through DAL-E) or design-assurance compliance claims
- AS9100 certification, OASIS registration, or QMS audit-status claims
- Airworthiness approval, TSO authorization, or STC claims
- Safety function proof, failure-mode coverage, or FMEA/FMECA outcome claims
- Flight computer performance (latency, accuracy, availability) or RTCA minimum-performance-standard claims

---

### Communication / RF / Data Links PCBs

**Safe angles:**
- RF and microwave section vocabulary: RF layer, matching network, front-end circuit on aerospace RF PCB description (customer material and stackup basis)
- High-speed signal processing board vocabulary: high-speed ADC/DAC, FPGA, DSP, memory for communication and data-link signal chains description
- Conduction/convection cooling vocabulary: wedge-lock, chassis-mounted, conduction-cooled layout description
- Secure/tactical communication vocabulary: encryption module footprint, frequency-hopping radio, tactical data-link interface description (customer-design basis)

> **For EW, ISR, radar front-end, or defense-specific RF content**, route to `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md`.

**Blocked:**
- Secure communication, COMSEC, TEMPEST, or signal-encryption compliance claims
- RF performance (bandwidth, sensitivity, EIRP, spurious emission) claims
- FCC/ETSI/DO-160G RF emission qualification claims
- Named data-link standard (Link 16, ARINC 429, ARINC 664/AFDX) conformance proof

---

### Power / Actuation PCBs

**Safe angles:**
- High-voltage and high-current design vocabulary: copper thickness, creepage/clearance, slots, insulation strategy description (design-intent, NOT compliance values)
- Motor and actuator driver vocabulary: MOSFET/IGBT, gate driver, current sensing, feedback interface for flap/valve/landing-gear/UAV actuator description
- EMC-aware layout vocabulary: conducted/radiated emission reduction layout practices for system-level EMC context
- Redundancy and monitoring vocabulary: status monitoring, fault reporting, redundant feed integration description (customer-design basis)

**Blocked:**
- DO-160G Section 16/17/18 (power input) or Section 21 (magnetic effect) qualification claims
- Exact creepage/clearance values as IEC 60664 or aviation wiring-standard compliance proof
- Actuator performance, force, speed, or control accuracy claims
- Power supply MIL-STD-704 compliance claims

---

### Ground Systems / Test Equipment PCBs

**Safe angles:**
- Rugged computing and control board vocabulary: industrial PC, rack-mounted server, dedicated controller with long-lifecycle and extended operating conditions description
- Control console and HMI vocabulary: operator panel, keyboard, trackball, display, status indicator board
- Test and interface PCBA vocabulary: test rack, simulator, load bank, RF/interface adapter boards
- Long-lifecycle focus vocabulary: repeatable materials and process description for extended production periods

**Blocked:**
- Defense-specific ground system vocabulary (command-and-control for weapons, fire control, JTIDS) → route to defense page
- System qualification pass-status or integration-test outcome claims
- TEMPEST or RF-shielding compliance claims

---

### Ruggedization / Materials / Stackup

**Safe angles:**
- High-Tg and thermal material vocabulary: high-Tg, thermally robust material description (customer-specified basis)
- Controlled impedance vocabulary: stackup control, impedance management for high-speed digital and RF sections
- Via and PTH integrity vocabulary: via integrity, hole-wall quality, copper distribution for thermal and mechanical stress
- Conformal coating vocabulary: conformal coating and protective finish at PCBA stage description (on request)

**Blocked:**
- MIL-PRF-31032, MIL-PRF-55110, or IPC-6012 Class 3/3A qualification claims
- Specific material qualification to named aerospace material approvals
- Environmental screening (thermal cycling, vibration, humidity) pass-status claims

---

## Aviation Standards Context

| Standard | Safe Use |
|---|---|
| `DO-160G` | RTCA environmental-conditions and test-procedures document-family identity; FAA AC 21-16G recognizes versions D–G for certain airworthiness requirements — NOT section-level qualification proof |
| `DO-254` | RTCA airborne electronic hardware design-assurance guidance identity; FAA AC 20-152A supports circuit-board-assembly context only — NOT DAL assignment or compliance proof |
| `DO-155` | RTCA minimum-performance standard for low-range radar altimeters identity only — NOT applicable to barometric or laser altimeters |
| `AS9100` | Aerospace QMS standard identity — NOT current certificate, audit, or OASIS listing proof |
| `AS9102` | Aerospace first-article inspection standard identity and documentation context — NOT process-capability or qualification proof |
| `FAA AC 20-152A` | Airborne electronic hardware design-assurance advisory circular — supports circuit-board-assembly context only, NOT airworthiness or supplier approval |
| `ARINC 429 / 664` | Avionics data bus standard identity — NOT conformance proof |
| `TSO` | FAA Technical Standard Order authorization — NOT a PCB-level claim; device-level authorization only |
| `ITAR / EAR` | US export-control regulations — completely outside current source corpus; any ITAR/EAR language requires refresh |

---

## Engineering Boundaries

- Civil aerospace content is board-class and documentation-discipline vocabulary only — not system qualification, program approval, or airworthiness proof.
- `"AS9100 Certified – Mission Assurance"` trust-bar from the Tier-2 source is marketing framing; do NOT publish as current certificate or OASIS listing.
- DO-160G and DO-254 are standards-identity vocabulary only; qualification pass-status, section-specific test conditions, DAL, and design-assurance level are blocked.
- Defense, MIL-STD, EW, ISR, or weapons-system vocabulary must route to the defense page even when the application uses the same Tier-2 source.
- ITAR/EAR are completely blocked; do not use export-control compliance language under any circumstance.

---

## Common Misreadings

- `"AS9100 Certified"` trust-bar → does NOT prove current AS9100 certificate, scope, or OASIS registration.
- `"Mission Assurance"` trust-bar → does NOT prove DO-254 DAL, airworthiness, or program qualification.
- `"Thermal Cycling -55 to 125°C"` trust-bar → does NOT prove DO-160G Section 4 temperature qualification.
- DO-254 mentioned in a draft → does NOT prove DAL-A, B, C, D, or E assignment or compliance.
- FAA AC 20-152A referenced → does NOT prove airworthiness, TSO, or installation approval.
- Aerospace PCB manufactured → does NOT prove ITAR compliance, export-control authorization, or US government program eligibility.
- Redundant architecture described → does NOT prove safety function, fail-safe behavior, or DO-178C software assurance.

---

## Must Refresh Before Publishing

- Any AS9100 certification status, certificate scope, or OASIS registration claims
- Any DO-160G section-level test or pass-status claims
- Any DO-254 DAL assignment or design-assurance compliance claims
- Any airworthiness, TSO, STC, or FAA approval claims
- Any ITAR, EAR, or export-control compliance claims
- Any MIL-STD, defense-program, or weapons-system qualification claims
- Any RF performance, data-link conformance, or RTCA minimum-performance-standard claims
- Any mission reliability, MTBF, or program-history claims

---

## Cross-Lane Routing

| Content Type | Route To |
|---|---|
| Defense/military aviation (EW, ISR, radar, guided systems) | `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md` |
| Altimeter-specific slugs (DO-155, radio/barometric/laser altimeter) | `wiki/processes/altimeter-aviation-standards-and-assurance-boundaries.md` |
| Civilian UAV/drone flight controller | `wiki/applications/drone-uav-pcb-pcba-boundary-map.md` |
| First-article inspection documentation | `facts/methods/pcba-first-article-inspection-vs-high-speed-validation-boundary.md` |
| DFM / DFT review gates | `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md` |
| X-ray hidden-joint inspection | `facts/methods/hidden-joint-xray-inspection-boundary.md` |
| Qualification boundary (AS9100, DO-254, FAA AC context) | `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md` |
| Aviation standards metadata (DO-160G, DO-254, DO-155) | `facts/standards/aviation-altimeter-standards-metadata-boundary.md` |

---

## Related Pages

- `facts/applications/civil-aerospace-coverage-gap-map.md`
- `wiki/applications/application-routing-and-boundary-map.md`
- `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md`
- `wiki/processes/altimeter-aviation-standards-and-assurance-boundaries.md`
- `facts/standards/aviation-altimeter-standards-metadata-boundary.md`
- `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md`

## Primary Sources

- /code/hileap/frontendAPT/public/static/industries/en/aerospace-defense-pcb.json
- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1041323
- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1019280
- https://my.rtca.org/productdetails?id=a1B36000001IcnSEAS
- https://my.rtca.org/productdetails?id=a1B36000001IcjTEAS
- https://saemobilus.sae.org/standards/as9102c-aerospace-series-first-article-inspection-requirements
