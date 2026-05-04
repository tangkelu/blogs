---
topic_id: "processes-radio-altimeter-rf-front-end-boundaries"
title: "Radio Altimeter RF Front-End Boundaries"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
fact_ids:
  - "standards-aviation-altimeter-standards-metadata-boundary"
  - "methods-radio-altimeter-rf-front-end-and-integration-boundary"
  - "methods-rf-impedance-sparameter-pdn-ota-boundaries"
  - "methods-rf-validation-capability"
  - "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"
source_ids:
  - "faa-ac-21-16g-do160-acceptability-page"
  - "rtca-do-160g-product-page"
  - "rtca-do-254-product-page"
  - "rtca-do-155-product-page"
  - "faa-pcg-radio-altimeter-glossary-page"
  - "faa-aim-radio-radar-altimeter-anomalies-section"
  - "faa-eb-107-5g-c-band-aero-studies"
  - "faa-ac-20-199-draft-radio-altimeter-installation"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "faa-ac-20-152a-page"
  - "as9102c-first-article-inspection-page"
tags: ["radio-altimeter", "radar-altimeter", "radalt", "altimeter", "rf-front-end", "antenna", "interface-boundary", "avionics"]
---

# Definition

> Radio-altimeter PCB writing is safe only at a narrow subsystem boundary: `radio altimeter` or `radar altimeter` identity, direct height-above-terrain aircraft context, guarded `4.2-4.4 GHz` RF-band framing, and transceiver / antenna / RF-cabling / display-interface vocabulary. This lane does not authorize certification or airworthiness proof, exact altitude or RF performance numerics, universal RF stackup doctrine, or supplier or program approval claims.

## Routing Guidance

- Use this page when a draft needs safe wording for the `radio altimeter` subset of aviation or `altimeter PCB` content.
- Route `radio altimeter`, `radar altimeter`, `RADALT`, direct height-above-terrain context, and guarded aircraft-system role wording through the identity-boundary facts only.
- Route transceiver, antenna, RF cable, transmission-line, coexistence-awareness, and display or indicator interface wording through the RF front-end and installation-boundary facts only.
- Route impedance-review posture, coupons, `TDR`, `VNA`, and traceability language through the existing RF validation capability lane rather than through finished-product proof.
- Route first-build confirmation, release-stage checks, and inspection-documentation language through the first-article boundary instead of turning them into RF validation or avionics approval claims.
- Route `DO-160G`, `DO-254`, `DO-155`, aerospace, or regulated-application wording through standards metadata and application-boundary cards only.

## Why This Topic Matters

- `Altimeter` drafts can collapse barometric, radio, and other sensing families into one unsupported authority lane.
- The already-landed facts support a narrower and safer split: radio-altimeter identity, aircraft-system role, RF-front-end vocabulary, staged validation posture, and standards metadata boundaries.
- This page converts that split into a reusable active route so future rewrites can keep legitimate subsystem language without importing unsupported aviation approval, architecture, or numeric performance claims.

## Stable Facts

- FAA glossary and AIM sources support `radar altimeter`, `radio altimeter`, and `RADALT` as the same aircraft-system noun family.
- FAA public sources support radio altimeters as aircraft equipment used to determine height above terrain or the surface, and as a data source for other onboard systems and displays.
- FAA Engineering Brief `107` supports the public RF-band framing that commercial-aviation radio altimeters operate in the `4.2-4.4 GHz` band.
- FAA draft `AC 20-199` supports a subsystem boundary that may include the radio-altimeter transceiver, one or more antennas, RF cables or transmission lines, and indicator or display interfaces.
- The landed aviation standards metadata card supports guarded public vocabulary for `DO-160G`, `DO-254`, and `DO-155` only at standards-family and scope-boundary level.
- The landed RF validation capability card supports an internal review posture centered on impedance coupons, `TDR`, `VNA`, and build traceability rather than AOI-only or release-only language.
- The landed first-article boundary supports `FAI` as an early-run verification and documentation gate rather than as a substitute for RF or high-speed validation.
- The landed regulated-application boundary supports aerospace and other regulated language only as system, device, component, or program context rather than as PCB or supplier readiness proof.

## Engineering Boundaries

### 1. Identity And Aircraft-System Role Boundary

- Safe wording: the board belongs to a `radio altimeter` or `radar altimeter` subsystem used for direct height-above-terrain context.
- Safe extension: describe `RADALT` as a safety-critical aircraft-system data source for onboard displays or dependent systems.
- Keep this boundary at aircraft-system identity and role vocabulary, not certification, installation approval, or operator authorization proof.

### 2. RF Front-End And Antenna-Path Boundary

- Safe wording: the board participates in a transceiver, antenna path, transmission-line, and interference-aware RF review problem inside a guarded avionics context.
- Safe companion facts: `methods-radio-altimeter-rf-front-end-and-integration-boundary`, `methods-rf-impedance-sparameter-pdn-ota-boundaries`, `methods-rf-validation-capability`.
- Keep this boundary at front-end review posture, not exact gain, isolation, delay, range, latency, or antenna-geometry proof.

### 3. Validation And Release Boundary

- Safe wording: first builds need staged validation, documentation discipline, and release-gate review before broader downstream claims.
- Safe companion facts: `methods-rf-validation-capability`, `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`.
- Keep first-article and validation language separate from exact RF performance proof or universal test-scope claims.

### 4. Standards And Qualification Boundary

- Safe wording: `DO-160G`, `DO-254`, `DO-155`, and aerospace-program language may be referenced only as standards metadata or application-boundary context.
- Safe companion facts: `standards-aviation-altimeter-standards-metadata-boundary`, `standards-automotive-medical-aerospace-application-qualification-boundary`.
- Keep this boundary separate from certification, airworthiness, supplier qualification, or program approval claims unless program-specific evidence is added elsewhere.

## Blocked Claims To Preserve

- Certification or airworthiness claims remain blocked, including `TSO`, installation approval, airworthiness approval, compliance proof, or any wording that treats a board, assembly, or supplier as a certified avionics product.
- Exact altitude or RF performance numerics remain blocked, including accuracy, resolution, latency, range, gain, loss, isolation, delay, interference margin, or other RF or avionics figures.
- Universal RF stackup doctrine remains blocked, including fixed material choices, layer counts, antenna structures, heavy-copper rules, or one-size-fits-all radio-altimeter layout recipes.
- Supplier or program approval claims remain blocked, including approved vendor, flight-ready supplier, customer-program acceptance, qualified source, deployed platform, or field-proven wording.

## Common Misreadings

- `Radio altimeter` is sometimes misread as authority for all `altimeter` technologies; here it only supports the radio-altimeter aircraft-system lane.
- Mentioning the `4.2-4.4 GHz` band is sometimes misread as proof of exact board architecture or RF performance; here it only supports guarded band context.
- Naming `DO-160G`, `DO-254`, or `DO-155` is sometimes misread as proof that a PCB, PCBA, or supplier is qualified; here those sources only support standards metadata and scope boundaries.
- Mentioning `FAI`, `TDR`, or `VNA` is sometimes misread as proof that downstream RF validation is complete; here those facts only support staged review and validation posture.
- Aircraft-system role wording is sometimes misread as proof of installation approval or airworthiness; here it only supports subsystem identity and interface context.

## Safe Draft Routing

### `altimeter-pcb.md`

- Supported route: isolate the radio-altimeter subset as an RF transceiver, antenna-path, transmission-line, and display-interface lane within a broader altitude-system discussion.
- Keep blocked: certification or airworthiness claims, exact altitude or RF performance numerics, universal RF stackup doctrine, and supplier or program approval claims.

## Must Refresh Before Publishing

- Any exact numeric tied to altitude accuracy, range, latency, interference tolerance, gain, loss, isolation, delay, or other RF-performance outcomes.
- Any statement that turns public FAA or RTCA standards metadata into certification, airworthiness, or installed-product approval proof.
- Any statement that turns internal RF validation posture into a universal test package, fixed frequency ceiling, or guaranteed scope for every program.
- Any statement that turns subsystem review language into approved supplier, qualified source, or program-acceptance proof.

## Related Facts And Source Scope

- `methods-radio-altimeter-rf-front-end-and-integration-boundary`
- `methods-rf-impedance-sparameter-pdn-ota-boundaries`
- `methods-rf-validation-capability`
- `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`
- `standards-aviation-altimeter-standards-metadata-boundary`
- `standards-automotive-medical-aerospace-application-qualification-boundary`

## Source Scope

- Radio-altimeter identity, aircraft-system role, RF-band framing, and installation-boundary wording come from already-landed FAA source records referenced by the linked fact cards.
- Standards-family and assurance-boundary wording comes from already-landed FAA and RTCA source records referenced by the linked fact cards.
- RF validation and first-article workflow wording comes from already-landed internal capability and method source records referenced by the linked fact cards.
- Outside current scope: certification proof, airworthiness proof, exact RF or altitude numerics, universal board architecture doctrine, and supplier or program approval evidence.

## Primary Sources

- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1019280
- https://my.rtca.org/productdetails?id=a1B36000001IcnSEAS
- https://my.rtca.org/productdetails?id=a1B36000001IcjTEAS
- https://my.rtca.org/productdetails?id=a1B36000001IcnqEAC
- https://www.faa.gov/air_traffic/publications/atpubs/pcg_html/glossary-r.html
- https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap7_section_6.html
- https://www.faa.gov/airports/engineering/engineering_briefs/eb_107_5G_Aero_Studies
- https://www.faa.gov/aircraft/draft_docs/ac_20_199
- /code/hileap/frontendAPT/public/static/pcb/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/microwave-pcb.json
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1041323
- https://saemobilus.sae.org/standards/as9102c-aerospace-series-first-article-inspection-requirements
