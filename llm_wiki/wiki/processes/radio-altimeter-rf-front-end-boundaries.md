---
topic_id: "processes-radio-altimeter-rf-front-end-boundaries"
title: "Radio Altimeter RF Front-End Boundaries"
category: "processes"
status: "draft"
last_reviewed_at: "2026-05-01"
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

> Radio-altimeter PCB writing is only safe when it stays inside subsystem review boundaries: the `radio altimeter` / `radar altimeter` identity lane, direct height-above-terrain aircraft context, `4.2-4.4 GHz` RF-band framing, and transceiver / antenna / RF-cabling / display-interface vocabulary. The current corpus does not support turning this lane into certification proof, universal stackup doctrine, or exact altitude-performance claims.

## Why This Topic Matters

- The `2026.4.27/en` `altimeter` draft mixes three different sensing families, then overreaches into aviation qualification, RF architecture, and supplier-proof language.
- Existing `llm_wiki` layers already support RF review, validation staging, first-article discipline, and regulated-application boundaries, but they previously lacked a clean public authority lane for `radio altimeter` itself.
- This page creates that route so future rewrites can keep `radio altimeter` language at RF-front-end and avionics-interface level without importing unsupported product or certification claims.

## Stable Facts

- FAA glossary and AIM sources support `radar altimeter` and `radio altimeter` as the same aircraft-system noun family.
- FAA AIM supports the role of the radio altimeter as direct height-above-terrain measurement and as an input to other safety-critical aircraft systems and displays.
- FAA Engineering Brief `107` supports the public RF-band context that commercial-aviation radio altimeters operate at `4.2-4.4 GHz`.
- FAA draft `AC 20-199` supports a system boundary that may include a transceiver, one or more antennas, RF cables / transmission lines, and indicator or display interfaces.
- The new aviation standards metadata boundary supports guarded `DO-160G`, `DO-254`, and `DO-155` document-family vocabulary only at assurance-boundary level.
- Existing RF validation, first-article, and qualification-boundary cards support separate discussion of review workflow, release discipline, and regulated-program context without pretending to prove an approved avionics product.

## Review Lanes

### 1. Identity And System Role

- Safe posture:
  describe the board as part of a `radio altimeter` or `radar altimeter` subsystem that contributes to direct aircraft height-above-terrain measurement.
- Do not drift into:
  navigation-authority generalizations, finished-product approval, or aircraft-program proof.

### 2. RF Front-End And Antenna Path

- Safe posture:
  describe the board as handling RF transceiver, antenna-path, transmission-line, and interference-aware review problems in a guarded avionics context.
- Safe companion layers:
  `standards-aviation-altimeter-standards-metadata-boundary`,
  `methods-rf-impedance-sparameter-pdn-ota-boundaries`,
  `methods-rf-validation-capability`.
- Do not drift into:
  universal material selection, layer-count rules, antenna geometry claims, or exact RF-performance numerics.

### 3. Interface And Release Boundary

- Safe posture:
  describe display/output interfaces, staged validation, first-build confirmation, and application-boundary language for radio-altimeter-adjacent electronics.
- Safe companion layers:
  `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`,
  `standards-automotive-medical-aerospace-application-qualification-boundary`.
- Do not drift into:
  `DO-160`, `DO-155`, `DO-254`, `TSO`, airworthiness, or supplier qualification claims.

## Safe Draft Routing

### `altimeter-pcb.md`

- Status:
  `partial_support_for_radio_altimeter_subset_only`
- Safe angle:
  separate the radio-altimeter subset as an RF transceiver / antenna / interface-board lane inside a larger altitude-system article.
- Keep out:
  exact altitude accuracy, universal radar-altimeter architecture, aviation qualification claims, and supplier / program proof.

## Common Overclaims

- `aviation altimeter PCB` used as if it proves a certified avionics product
- `4.3 GHz radar altimeter board` used as if it proves a universal stackup or material recipe
- `DO-160` / `DO-254` / `TSO` language used as if it proves board-shop readiness
- `radar altimeter` wording collapsed into `all altimeter technologies are equivalent`

## Must Refresh Before Publishing

- Any exact RF, delay, accuracy, altitude, or interference numeric
- Any statement about current FAA coexistence policy beyond the public EB and draft-guidance boundary
- Any claim that moves from subsystem review into certification, airworthiness, or installed-product approval

## Related Fact Cards

- `methods-radio-altimeter-rf-front-end-and-integration-boundary`
- `methods-rf-impedance-sparameter-pdn-ota-boundaries`
- `methods-rf-validation-capability`
- `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`
- `standards-aviation-altimeter-standards-metadata-boundary`
- `standards-automotive-medical-aerospace-application-qualification-boundary`

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
