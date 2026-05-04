---
topic_id: "processes-altimeter-aviation-standards-and-assurance-boundaries"
title: "Altimeter Aviation Standards And Assurance Boundaries"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "standards-aviation-altimeter-standards-metadata-boundary"
  - "methods-barometric-pressure-sensor-owner-identity-and-interface-boundary"
  - "methods-radio-altimeter-rf-front-end-and-integration-boundary"
  - "methods-laser-time-of-flight-pulsed-driver-and-safety-boundary"
  - "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"
source_ids:
  - "faa-ac-21-16g-do160-acceptability-page"
  - "faa-ac-20-152a-page"
  - "rtca-do-160g-product-page"
  - "rtca-do-254-product-page"
  - "rtca-do-155-product-page"
  - "bosch-bmp390-product-page"
  - "te-ms5611-product-page"
  - "infineon-dps310-datasheet"
  - "faa-pcg-radio-altimeter-glossary-page"
  - "faa-aim-radio-radar-altimeter-anomalies-section"
  - "faa-eb-107-5g-c-band-aero-studies"
  - "faa-ac-20-199-draft-radio-altimeter-installation"
  - "ti-tdc7200-product-page"
  - "ti-lmh13000-product-page"
tags: ["altimeter", "do-160g", "do-254", "do-155", "faa", "rtca", "assurance-boundary", "avionics"]
---

# Definition

> Altimeter aviation standards wording is safe only when it stays inside document-identity and assurance-boundary lanes: named RTCA document families, FAA recognition context, sensing-family scope separation, staged validation framing, and explicit PCB stop lines. This page is not a universal altimeter qualification page and must not collapse barometric, radio, and laser subsets into one avionics-readiness conclusion.

## Why This Topic Matters

- The `2026.4.27/en` `altimeter` draft mixes barometric, radar, and laser subsets, then uses `DO-160G`, `DO-254`, and `DO-155` as if they prove universal architecture or production readiness.
- Public FAA and RTCA pages are strong enough to recover exact document identity and scope boundaries without pretending to hold the underlying full standard text.
- This page creates a safer route so future rewrites can retain exact aviation standard names conservatively while still blocking direct qualification and compliance overclaims.

## Stable Facts

- `DO-160G` is the RTCA environmental-conditions and test-procedures document family for airborne equipment, and FAA `AC 21-16G` publicly recognizes `DO-160` versions `D` through `G` as acceptable environmental qualifications for certain airworthiness requirements while strongly encouraging `DO-160G` for new articles.
- `DO-254` is the RTCA design-assurance guidance document for airborne electronic hardware, and public RTCA metadata plus FAA `AC 20-152A` support circuit-board-assembly context only.
- `DO-155` is the RTCA minimum-performance-standard document for airborne low-range radar altimeters only.
- Existing barometric, radio-altimeter, and laser-time-of-flight lanes already support separate sensing-family context, so the standards metadata lane should not collapse them back into one universal `altimeter PCB` authority claim.

## Standards Identity And Assurance Framing

### `DO-160G`

- Safe use: named RTCA environmental-conditions and test-procedures document-family identity for airborne equipment.
- Safe FAA framing: FAA `AC 21-16G` recognition context for acceptable environmental qualification document families.
- PCB stop line: do not convert this into exact test category coverage, section ownership, or PCB qualification conclusion.

### `DO-254`

- Safe use: named RTCA airborne electronic hardware design-assurance document-family identity.
- Safe FAA framing: FAA `AC 20-152A` supports airborne electronic hardware assurance context and guarded circuit-board-assembly scope language.
- PCB stop line: do not convert this into DAL closure, verification-completeness, fabricator-control mandates, or supplier readiness proof.

### `DO-155`

- Safe use: named RTCA minimum-performance-standard identity for airborne low-range radar altimeters only.
- Safe assurance framing: keep this document inside the radio-altimeter subset and do not reuse it as if it governed all `altimeter` boards.
- PCB stop line: do not treat radar-altimeter MPS identity as proof for barometric or laser altimeter hardware.

## Sensing-Family Separation

### Barometric Altimeter Subset

- Route to `methods-barometric-pressure-sensor-owner-identity-and-interface-boundary`.
- Safe language stays at pressure-sensor owner identity, interface vocabulary, pressure-plus-temperature measurement context, and conservative subsystem integration wording.
- Do not convert pressure-sensor identity into aviation-altimeter qualification, aircraft-bus authority, or exact altitude-performance proof.

### Radio Altimeter Subset

- Route to `methods-radio-altimeter-rf-front-end-and-integration-boundary`.
- Safe language stays at aircraft-system identity, `4.2-4.4 GHz` public RF-band context, transceiver/antenna/transmission-line/interface boundaries, and low-range radar-altimeter standards identity.
- Do not convert this subset into universal `altimeter PCB` architecture, installation approval, or compliance proof.

### Laser Altimeter / ToF Subset

- Route to `methods-laser-time-of-flight-pulsed-driver-and-safety-boundary`.
- Safe language stays at timing path, pulsed-driver, subsystem-control, and laser-safety boundary vocabulary.
- Do not convert time-of-flight subsystem identity into eye-safe product claims, exact range/altitude claims, or aviation qualification proof.

## Review Lanes

### 1. `DO-160G` As Environmental Qualification Document Context

- Safe posture:
  use `DO-160G` only as named RTCA environmental-test document-family vocabulary for airborne equipment, with FAA recognition context.
- Safe companion layers:
  `standards-automotive-medical-aerospace-application-qualification-boundary`,
  `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`.
- Do not drift into:
  exact section or category coverage, exact environmental numerics, or actual board qualification claims.

### 2. `DO-254` As Airborne Electronic Hardware Design-Assurance Context

- Safe posture:
  use `DO-254` only as named RTCA airborne electronic hardware design-assurance vocabulary with guarded circuit-board-assembly context.
- Safe companion layers:
  `standards-aviation-altimeter-standards-metadata-boundary`,
  `standards-automotive-medical-aerospace-application-qualification-boundary`.
- Do not drift into:
  DAL chains, exact verification obligations, manufacturing-control requirements, or supplier-readiness claims.

### 3. `DO-155` As Radar-Altimeter-Specific Scope

- Safe posture:
  use `DO-155` only when the article is clearly in the low-range radar-altimeter subset.
- Safe companion layers:
  `methods-radio-altimeter-rf-front-end-and-integration-boundary`.
- Do not drift into:
  barometric or laser altimeter claims, universal `altimeter` claims, or compliance claims for a PCB or supplier.

## PCB Stop Lines

- A standards-family name is not a PCB qualification result.
- A sensing-family identity is not a supplier-readiness result.
- A subsystem boundary is not a compliance or installation approval result.
- A first-article or validation lane is not a final airworthiness conclusion.

## Explicit Non-Claims

- This page does not support qualification and compliance claims.
- It does not support supplier-readiness claims.
- It does not support exact environmental or performance numerics.
- It does not support cost, lead-time, or yield claims.
- It does not support collapsing barometric, radio, and laser altimeter subsets into one finished-board aviation conclusion.

## Safe Draft Routing

### `altimeter-pcb.md`

- Status:
  `partial_support_for_aviation_standards_subset_only`
- Safe angle:
  separate barometric, radio-altimeter, and laser subsets; keep `DO-160G`, `DO-254`, and `DO-155` at document-family and assurance-boundary level only.
- Keep out:
  `with DO-160 qualification`, `must comply`, exact section numerics, `DAL-A/B` process claims, `TSO`, airworthiness, and supplier/program proof.

## Common Overclaims

- `with DO-160 qualification`
- `must comply with DO-160G Section 21`
- `DO-254 requires our PCB fabricator controls`
- `RTCA/DO-155` applied to all altimeter architectures rather than the radar-altimeter subset
- `all altimeter PCBs follow one aviation qualification path`
- `pressure sensor + RF front end + laser driver equals a qualified avionics altimeter platform`

## Must Refresh Before Publishing

- Any exact section, category, or numeric under `DO-160G`
- Any exact assurance-duty statement under `DO-254`
- Any claim about approval, airworthiness, installation, `TSO`, or supplier qualification

## Related Fact Cards

- `standards-aviation-altimeter-standards-metadata-boundary`
- `methods-barometric-pressure-sensor-owner-identity-and-interface-boundary`
- `methods-radio-altimeter-rf-front-end-and-integration-boundary`
- `methods-laser-time-of-flight-pulsed-driver-and-safety-boundary`
- `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`
- `standards-automotive-medical-aerospace-application-qualification-boundary`

## Primary Sources

- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1019280
- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1041323
- https://my.rtca.org/productdetails?id=a1B36000001IcnSEAS
- https://my.rtca.org/productdetails?id=a1B36000001IcjTEAS
- https://my.rtca.org/productdetails?id=a1B36000001IcnqEAC
- https://www.bosch-sensortec.com/en/products/environmental-sensors/pressure-sensors/bmp390/
- https://www.te.com/en/product-MS561101BA03-50.html
- https://www.infineon.com/assets/row/public/documents/24/49/infineon-dps310-datasheet-en.pdf
- https://www.faa.gov/air_traffic/publications/atpubs/pcg_html/glossary-r.html
- https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap7_section_6.html
- https://www.faa.gov/airports/engineering/engineering_briefs/eb_107_5G_Aero_Studies
- https://www.faa.gov/aircraft/draft_docs/ac_20_199
- https://www.ti.com/product/TDC7200
- https://www.ti.com/product/LMH13000
