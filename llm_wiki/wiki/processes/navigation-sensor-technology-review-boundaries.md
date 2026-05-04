---
topic_id: "processes-navigation-sensor-technology-review-boundaries"
title: "Navigation Sensor Technology Review Boundaries"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
fact_ids:
  - "methods-navigation-sensor-technology-owner-identity-boundary"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"
source_ids:
  - "honeywell-hg1930-mems-imu-page"
  - "honeywell-hg2802-fiber-optic-gyro-imu-page"
  - "honeywell-gg1320an-digital-ring-laser-gyroscope-page"
  - "bosch-bmm350-magnetometer-product-page"
  - "bartington-mag03-fluxgate-magnetometer-page"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "faa-ac-20-152a-page"
  - "as9102c-first-article-inspection-page"
tags: ["gyroscope", "compass", "mems", "fog", "ring-laser-gyroscope", "magnetometer", "fluxgate", "imu", "navigation-sensor", "review-boundary"]
---

# Definition

> Navigation-sensor PCB writing is safe only at a narrow review-boundary level: owner-backed sensor-technology identity, guarded subsystem integration language, staged PCBA review and first-build release wording, and regulated-application boundary framing. This lane does not authorize drift proof, heading-accuracy proof, navigation-system authority, qualification proof, deployment proof, or supplier proof.

## Routing Guidance

- Use this page when `gyroscope-pcb.md`, `compass-pcb.md`, or similar drafts need exact technology-family nouns without expanding into finished-system performance or qualification claims.
- Route inertial wording through owner-backed `MEMS gyroscope`, `fiber-optic gyroscope`, `FOG`, `ring laser gyroscope`, `RLG`, and guarded `IMU` identity only.
- Route magnetic wording through owner-backed `magnetometer` and `fluxgate magnetometer` identity only.
- Route board-process wording through early `DFM`, `DFT`, `DFA`, first-build confirmation, and staged validation language.
- Route automotive, medical, aerospace, avionics, and defense-sensitive mention through application-boundary framing only.

## Stable Facts

- Honeywell owner pages support exact technology identity for `MEMS` inertial measurement units, `fiber optic gyro IMU`, and digital `ring laser gyroscope` products.
- Bosch owner material supports `magnetometer` identity with compass and dead-reckoning application framing.
- Bartington owner material supports `fluxgate magnetometer` identity.
- Internal PCBA workflow facts support `DFM`, `DFT`, and `DFA` as front-end engineering review gates that precede downstream inspection and validation.
- Existing first-article facts support `FAI` as an early-run verification and documentation gate rather than as proof of high-speed or navigation performance.
- Existing regulated-application facts support standards and regulator language only as program, device, or system boundary context rather than as PCB or supplier readiness proof.

## Engineering Boundaries

### 1. Sensor Technology Identity Boundary

- Safe wording: the board integrates or reviews `MEMS gyroscope`, `fiber-optic gyroscope`, `ring laser gyroscope`, `magnetometer`, or `fluxgate magnetometer` technology families.
- Safe extension: describe inertial-sensor, compass-sensor, or IMU signal-chain context at subsystem level.
- Keep this boundary at technology naming and guarded hardware vocabulary, not finished-system performance.

### 2. Board Review Boundary

- Safe wording: low-noise analog review, mixed-signal partitioning, magnetic-cleanliness review, packaging posture, connector or interface planning, calibration-access posture, and staged build planning.
- Safe companion fact: `methods-pcba-dfm-dft-dfa-review-gate-positioning`.
- Safe outcome framing: these are engineering review lanes that shape later inspection and validation.

### 3. First-Build Boundary

- Safe wording: `FAI` or first-build review helps confirm released-package alignment, setup readiness, and documentation discipline.
- Safe companion fact: `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`.
- Keep first-build language separate from any claim about high-speed success, navigation accuracy, or field deployment readiness.

### 4. Application Qualification Boundary

- Safe wording: automotive, medical, aerospace, or airborne programs impose separate system, device, component, and documentation boundaries.
- Safe companion fact: `standards-automotive-medical-aerospace-application-qualification-boundary`.
- Keep standards, regulatory, and aerospace references at context level unless program-specific evidence is added elsewhere.

## Blocked Claims To Preserve

- Drift and heading-accuracy claims remain blocked, including bias stability, angle random walk, sub-degree heading, calibration outcome, tilt-compensation outcome, vibration rejection, and similar numeric or performance proof.
- Navigation-system authority claims remain blocked, including inertial-navigation authority, dead-reckoning outcome proof, GPS-denied endurance, naval-compass authority, and finished-system control claims.
- Qualification or deployment claims remain blocked, including `DO-160`, `MIL-STD-810`, airworthiness, naval qualification, medical-device readiness, ASIL-ready, flight-certified, deployment-ready, or field-proven wording.
- Supplier-proof claims remain blocked, including any statement that sensor naming or standards references prove HILPCB validation, customer approval, completed compliance packages, or program-qualified supply status.

## Common Misreadings

- Naming `MEMS`, `FOG`, or `RLG` is sometimes misread as proof of navigation-grade drift or bias performance; it is only owner-backed technology identity here.
- Naming `magnetometer` or `fluxgate magnetometer` is sometimes misread as proof of compass accuracy or calibration success; it is only sensor-family identity here.
- Combining sensor nouns with `FAI` can be misread as proof of validated navigation behavior; first-article language here only supports launch-control and documentation posture.
- Referencing aerospace or regulated-application standards can be misread as proof that a board, assembly, or supplier is qualified; those sources only support application-boundary context here.

## Safe Draft Routing

### `gyroscope-pcb.md`

- Supported route: owner-backed gyroscope technology identity, inertial-sensor integration posture, low-noise or mixed-signal review language, and staged build validation wording.
- Keep blocked: drift, bias stability, jitter, GPS-denied navigation, military readiness, or deployment claims.

### `compass-pcb.md`

- Supported route: owner-backed magnetometer or fluxgate identity, magnetic-cleanliness review, signal-chain partitioning, packaging posture, and staged validation wording.
- Keep blocked: heading-accuracy, tilt-compensation, marine authority, calibration yield, or supplier-proof claims.

## Must Refresh Before Publishing

- Any exact numeric tied to drift, heading accuracy, bias stability, noise, temperature behavior, vibration behavior, or sensor-fusion performance.
- Any statement that turns subsystem identity into system-level navigation authority or deployment readiness.
- Any statement that names qualification, certification, approval, customer acceptance, or supplier capability for a specific program.
- Any direct standards naming that needs current metadata or program-specific interpretation beyond the existing fact cards.

## Related Facts

- `methods-navigation-sensor-technology-owner-identity-boundary`
- `methods-pcba-dfm-dft-dfa-review-gate-positioning`
- `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`
- `standards-automotive-medical-aerospace-application-qualification-boundary`

## Source Scope

- Owner-backed navigation-sensor identity sources: Honeywell inertial products, Bosch magnetometer product material, and Bartington fluxgate product material.
- Internal process sources: local PCBA review and first-article workflow records already landed in `llm_wiki`.
- Application-boundary sources: existing standards and regulator records already landed in `llm_wiki`.
- Outside current scope: fresh numeric performance validation, program qualification evidence, deployment evidence, and supplier proof.

## Primary Sources

- https://aerospace.honeywell.com/us/en/products-and-services/product/hardware-and-systems/sensors/hg1930-inertial-measurement-unit
- https://aerospace.honeywell.com/us/en/products-and-services/product/hardware-and-systems/sensors/hg2802-fiber-optic-gyro-imu
- https://aerospace.honeywell.com/us/en/products-and-services/product/hardware-and-systems/sensors/gg1320an-digital-ring-laser-gyroscope
- https://www.bosch-sensortec.com/products/motion-sensors/magnetometers/bmm350/
- https://www.bartington.com/magnetometers/mag-03/
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1041323
- https://saemobilus.sae.org/standards/as9102c-aerospace-series-first-article-inspection-requirements
