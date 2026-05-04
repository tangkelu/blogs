---
topic_id: "processes-navigation-sensor-technology-review-boundaries"
title: "Navigation Sensor Technology Review Boundaries"
category: "processes"
status: "draft"
last_reviewed_at: "2026-05-01"
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

> Navigation-sensor PCB writing is only safe when it stays inside owner-backed sensor-technology review boundaries: named `MEMS gyroscope`, `fiber-optic gyroscope`, `ring laser gyroscope`, `magnetometer`, and `fluxgate magnetometer` identity, plus guarded sensor-interface, magnetic-cleanliness, low-noise analog, packaging, and staged validation language. The current corpus does not support turning this lane into drift proof, heading-accuracy proof, military qualification proof, or navigation-system authority.

## Why This Topic Matters

- The `2026.4.27/en` `gyroscope` and `compass` drafts mix legitimate sensor-technology nouns with unsupported performance and qualification claims.
- Existing `llm_wiki` layers already support board-review, staged validation, and qualification-boundary language, but they previously lacked a clean owner-backed lane for exact inertial and magnetic navigation sensor technologies.
- This page creates that route so future rewrites can keep exact sensor nouns conservatively without importing unsupported navigation-system proof.

## Stable Facts

- Honeywell provides owner-backed `MEMS gyroscope`, `fiber-optic gyroscope`, and `ring laser gyroscope` product identity pages.
- Bosch provides an owner-backed magnetometer product page with compass and dead-reckoning application framing.
- Bartington provides an owner-backed fluxgate magnetometer product page.
- Existing DFM / first-article / qualification-boundary cards support separate discussion of mixed-signal review workflow, first-build confirmation, and regulated-program boundary language.

## Review Lanes

### 1. Inertial Gyroscope Technology Family

- Safe posture:
  describe the board as integrating guarded `MEMS gyroscope`, `FOG`, or `ring laser gyroscope` technology families in an IMU or inertial-sensor context.
- Safe companion layers:
  `methods-pcba-dfm-dft-dfa-review-gate-positioning`,
  `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`.
- Do not drift into:
  exact drift, bias stability, jitter, GPS-denied endurance, or navigation-grade performance claims.

### 2. Magnetic Compass Sensor Family

- Safe posture:
  describe the board as integrating a guarded `magnetometer` or `fluxgate magnetometer` signal chain in a compass or heading-reference context.
- Safe companion layers:
  `methods-pcba-dfm-dft-dfa-review-gate-positioning`,
  `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`.
- Do not drift into:
  exact heading accuracy, tilt-compensation outcome, calibration-matrix proof, or naval-system authority.

### 3. Release And Qualification Boundary

- Safe posture:
  describe staged validation, first-build confirmation, and regulated-program boundary language around navigation-sensor-bearing boards.
- Safe companion layers:
  `standards-automotive-medical-aerospace-application-qualification-boundary`.
- Do not drift into:
  `DO-160`, `MIL-STD-810`, airworthiness, naval qualification, or supplier qualification claims.

## Safe Draft Routing

### `gyroscope-pcb.md`

- Status:
  `partial_support_for_sensor_technology_subset`
- Safe angle:
  separate the article into owner-backed gyroscope-technology identity, inertial-sensor interface, low-noise analog review, packaging, and staged validation language.
- Keep out:
  exact drift, bias-stability, vibration-rejection, and military / aviation qualification claims.

### `compass-pcb.md`

- Status:
  `partial_support_for_sensor_technology_subset`
- Safe angle:
  separate the article into owner-backed magnetometer or fluxgate technology identity, magnetic-cleanliness review, signal-chain partitioning, packaging, and staged validation language.
- Keep out:
  exact heading accuracy, naval-compass authority, calibration outcomes, and supplier-proof claims.

## Common Overclaims

- `MEMS`, `FOG`, or `RLG` wording used as if the noun alone proves navigation-grade performance
- `magnetometer` or `fluxgate` wording used as if it proves sub-degree heading accuracy or marine-system compliance
- sensor-technology naming widened into aircraft, naval, or defense-program proof
- owner product identity reused as if it proves HILPCB validation, qualification, or deployment readiness

## Must Refresh Before Publishing

- Any exact drift, bias stability, heading accuracy, vibration, or temperature-compensation numeric
- Any statement about sensor-fusion outcome, calibration yield, or system-level navigation endurance
- Any claim that moves from sensor identity into qualification, deployment, or supplier proof

## Related Fact Cards

- `methods-navigation-sensor-technology-owner-identity-boundary`
- `methods-pcba-dfm-dft-dfa-review-gate-positioning`
- `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`
- `standards-automotive-medical-aerospace-application-qualification-boundary`

## Primary Sources

- https://aerospace.honeywell.com/us/en/products-and-services/product/hardware-and-systems/sensors/hg1930-inertial-measurement-unit
- https://aerospace.honeywell.com/us/en/products-and-services/product/hardware-and-systems/sensors/hg2802-fiber-optic-gyro-imu
- https://aerospace.honeywell.com/us/en/products-and-services/product/hardware-and-systems/sensors/gg1320an-digital-ring-laser-gyroscope
- https://www.bosch-sensortec.com/products/motion-sensors/magnetometers/bmm350/
- https://www.bartington.com/magnetometers/mag-03/
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1041323
- https://saemobilus.sae.org/standards/as9102c-aerospace-series-first-article-inspection-requirements
