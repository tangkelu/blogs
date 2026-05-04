---
topic_id: "processes-eo-ir-detector-owner-identity-review-boundaries"
title: "EO/IR Detector Owner Identity Review Boundaries"
category: "processes"
status: "draft"
last_reviewed_at: "2026-04-30"
fact_ids:
  - "methods-eo-ir-detector-owner-identity-and-interface-boundary"
  - "methods-fire-control-platform-interface-boundary"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"
source_ids:
  - "exosens-image-intensifier-tube-page"
  - "sony-starvis-technology-page"
  - "sony-security-camera-image-sensor-products-page"
  - "lynred-about-our-technologies-page"
  - "mil-std-1553-data-bus-page"
  - "mil-hdbk-1553-multiplex-application-handbook-page"
  - "bosch-can-protocols-page"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "faa-ac-20-152a-page"
  - "as9102c-first-article-inspection-page"
tags: ["eo-ir", "night-vision", "thermal-imaging", "surveillance", "targeting", "image-intensifier-tube", "cmos-image-sensor", "infrared-detector", "review-boundary"]
---

# Definition

> EO/IR-adjacent PCB writing is only safe when it stays inside owner-backed detector-review boundaries: named detector-family identity, guarded detector-chain and optical-sensor-interface vocabulary, compact packaging and isolation pressure, processing-board context, and staged validation plus release gates. The current corpus does not support turning this lane into detector-performance proof, optics authority, video-chain proof, or military-program claims.

## Why This Topic Matters

- The `2026.4.27/en` imaging and defense drafts repeatedly mix real detector nouns with unsupported performance, military, surveillance, and supplier-proof claims.
- Existing `llm_wiki` layers already support board-review workflow, release gates, qualification boundaries, and targeting platform-interface posture, but they previously lacked a clean owner-backed lane for exact EO/IR detector-family naming.
- This page creates that route so future rewrites can retain exact detector nouns conservatively without importing unsupported optics, mission-system, or qualification proof.

## Stable Facts

- Exosens provides an owner-backed route for `image intensifier tube` detector-chain vocabulary including `photocathode`, `microchannel plate`, and `phosphor screen`.
- Sony provides an owner-backed route for `STARVIS` CMOS image-sensor technology and security-image-sensor family naming in low-light imaging contexts.
- Lynred provides an owner-backed route for `cooled infrared detector`, `uncooled infrared detector`, `infrared detector array`, and `microbolometer` vocabulary in thermal-imaging contexts.
- Existing DFM, first-article, and qualification-boundary cards separately support discussion of review workflow, first-build confirmation, and regulated-program boundary language.

## Review Lanes

### 1. Image Intensifier Detector Chain Identity

- Safe posture:
  describe the board as interfacing with an image-intensifier detector chain using owner-backed `photocathode`, `microchannel plate`, and `phosphor screen` vocabulary.
- Safe companion layers:
  `methods-pcba-dfm-dft-dfa-review-gate-positioning`,
  `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`.
- Do not drift into:
  generation-class proof, exact high-voltage numerics, auto-gating outcomes, military deployment, or optics-performance proof.

### 2. Low-Light CMOS Sensor Identity

- Safe posture:
  describe the board as integrating a low-light CMOS image-sensor lane using owner-backed `STARVIS`, security-image-sensor, and detector-interface vocabulary.
- Safe companion layers:
  `methods-pcba-dfm-dft-dfa-review-gate-positioning`.
- Do not drift into:
  `CCD`, exact sensitivity, `QE`, lux, frame-rate, resolution, or finished-camera claims.

### 3. Thermal IR Detector Family Identity

- Safe posture:
  describe the board as supporting a thermal-detector readout and processing path using owner-backed cooled / uncooled infrared-detector family vocabulary.
- Safe companion layers:
  `methods-pcba-dfm-dft-dfa-review-gate-positioning`,
  `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`.
- Do not drift into:
  detector materials, exact microbolometer architecture, `NETD`, cryocooler behavior, optics-performance, or universal thermal-camera doctrine.

### 4. Board Review And Release Boundary

- Safe posture:
  describe detector-bearing boards through compact packaging, isolation, power and thermal review, staged validation, first-build confirmation, and regulated-program boundary language.
- Safe companion layers:
  `methods-fire-control-platform-interface-boundary`,
  `standards-automotive-medical-aerospace-application-qualification-boundary`.
- Do not drift into:
  supplier readiness, military qualification, program approval, or deployment proof.

## Safe Draft Routing

### `night-vision-pcb.md`

- Status:
  `go_now_conservative`
- Safe angle:
  owner-backed image-intensifier or low-light CMOS detector-family naming, detector-chain and processing-board context, compact packaging, isolation review, and staged validation workflow.
- Keep out:
  `ENVG-B`, exact detector generation or voltage numerics, military qualification, optics-performance, and HIL capability claims.

### `thermal-imaging-pcb.md`

- Status:
  `go_now_conservative`
- Safe angle:
  owner-backed cooled / uncooled infrared-detector family naming, detector readout and processing-board context, power / thermal segregation, and staged validation workflow.
- Keep out:
  `FLIR` brand proof, detector materials, `NETD`, cryocooler performance, optics claims, and military-program language.

### `surveillance-pcb.md`, `targeting-pcb.md`

- Status:
  `partial_support_for_optical_sensor_subset_only`
- Safe angle:
  owner-backed EO/IR detector-family naming, optical-sensor-interface posture, detector-processing context, and pairing with existing platform-interface or release-governance layers.
- Keep out:
  surveillance mission proof, target-tracking outcomes, fire-control authority, program history, and qualification claims used as supplier proof.

## Common Overclaims

- `EO/IR` or `night vision` used as if exact detector-family naming proves optics or system performance
- `image intensifier` or `microbolometer` mention widened into voltage, gain, `NETD`, or detector-material proof
- Sony or Lynred owner naming widened into surveillance, targeting, or military-program authority
- detector-family vocabulary reused as if it proves HILPCB manufacturing readiness or deployment history

## Must Refresh Before Publishing

- Any exact detector sensitivity, `QE`, lux, `NETD`, range, resolution, or frame-rate numeric
- Any statement about cryocoolers, detector materials, optical stack, image registration, or video-output standards
- Any claim that moves from detector-family identity into military qualification, mission-system performance, or supplier proof

## Related Fact Cards

- `methods-eo-ir-detector-owner-identity-and-interface-boundary`
- `methods-fire-control-platform-interface-boundary`
- `methods-pcba-dfm-dft-dfa-review-gate-positioning`
- `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`
- `standards-automotive-medical-aerospace-application-qualification-boundary`

## Primary Sources

- https://www.exosens.com/products/image-intensifier-tube
- https://www.sony-semicon.com/en/technology/security/index.html
- https://www.sony-semicon.com/en/products/is/security/index.html
- https://www.lynred.com/about-our-technologies
- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=36973
- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=54141
- https://www.bosch-semiconductors.com/products/ip-modules/can-protocols/
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1041323
- https://saemobilus.sae.org/standards/as9102c-aerospace-series-first-article-inspection-requirements
