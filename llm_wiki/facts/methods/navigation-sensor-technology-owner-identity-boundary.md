---
fact_id: "methods-navigation-sensor-technology-owner-identity-boundary"
title: "Gyroscope and compass writing is source-backed only at navigation-sensor owner identity level"
topic: "navigation sensor technology owner identity boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-01"
source_ids:
  - "honeywell-hg1930-mems-imu-page"
  - "honeywell-hg2802-fiber-optic-gyro-imu-page"
  - "honeywell-gg1320an-digital-ring-laser-gyroscope-page"
  - "bosch-bmm350-magnetometer-product-page"
  - "bartington-mag03-fluxgate-magnetometer-page"
tags: ["gyroscope", "compass", "mems", "fog", "fiber-optic-gyroscope", "ring-laser-gyroscope", "magnetometer", "fluxgate", "imu", "owner-identity"]
---

# Canonical Summary

> Current Honeywell, Bosch, and Bartington owner sources support one narrow navigation-sensor technology lane only: `gyroscope` and `compass` drafts may name exact technology families such as `MEMS gyroscope`, `fiber-optic gyroscope`, `ring laser gyroscope`, `magnetometer`, and `fluxgate magnetometer`, and may use guarded inertial or magnetic-sensing hardware vocabulary at subsystem level. The current evidence layer does not support turning those nouns into heading-accuracy proof, drift proof, military qualification proof, or supplier-readiness claims.

## Stable Facts

- Honeywell publicly identifies `HG1930` as a `MEMS` inertial measurement unit with gyroscope and accelerometer vocabulary, making `MEMS gyroscope` and `IMU` safe owner-backed nouns.
- Honeywell publicly identifies `HG2802` as a `fiber optic gyro IMU`, making `fiber-optic gyroscope` and guarded `FOG` wording safe owner-backed nouns.
- Honeywell publicly identifies `GG1320AN` as a digital `ring laser gyroscope`, making guarded `ring laser gyroscope` and `RLG` wording safe owner-backed nouns.
- Bosch Sensortec publicly identifies `BMM350` as a geomagnetic sensor and frames compass and dead-reckoning applications, making `magnetometer` a safe owner-backed noun in compass-board context.
- Bartington publicly identifies `Mag-03` as a three-axis `fluxgate magnetometer`, making `fluxgate magnetometer` a safe owner-backed noun in compass-board context.

## Conditions And Methods

- Use this card when `gyroscope-pcb.md` or `compass-pcb.md` needs a safer route than generic military-navigation marketing for exact sensor-technology nouns.
- Safe posture: keep the board role at sensor interface, low-noise or magnetic-cleanliness review, mixed-signal partitioning, packaging, calibration-access posture, and staged validation language.
- Pair this lane with existing sensor/navigation review, DFM, first-article, and qualification-boundary cards when the draft also discusses mixed-signal integration or regulated-program context.
- Keep `MEMS`, `FOG`, `RLG`, `magnetometer`, and `fluxgate magnetometer` as technology-identity lanes rather than as proof of finished-system performance.

## Limits And Non-Claims

- This card does not authorize exact drift, bias stability, heading accuracy, angle random walk, tilt-compensation, vibration-rejection, or magnetic-cleanliness outcome claims.
- It does not authorize exact loop-area, jitter, ripple, sensor-fusion, Kalman-filter, or ADC-performance claims at finished-board or finished-system level.
- It does not authorize `DO-160`, `MIL-STD-810`, naval qualification, airworthiness, or military-program claims for a PCB, assembly, or supplier.
- It does not authorize HILPCB deployment, customer, inertial-navigation-program, or defense-readiness proof.

## Open Questions

- Add narrower owner or standards sources later if future rewrites must retain exact marine-compass, airworthiness, or survey-grade authority beyond the current sensor-identity lane.
- Add stronger owner or institutional sources later if future rewrites must retain exact drift, heading-accuracy, or calibration-performance language.

## Source Links

- https://aerospace.honeywell.com/us/en/products-and-services/product/hardware-and-systems/sensors/hg1930-inertial-measurement-unit
- https://aerospace.honeywell.com/us/en/products-and-services/product/hardware-and-systems/sensors/hg2802-fiber-optic-gyro-imu
- https://aerospace.honeywell.com/us/en/products-and-services/product/hardware-and-systems/sensors/gg1320an-digital-ring-laser-gyroscope
- https://www.bosch-sensortec.com/products/motion-sensors/magnetometers/bmm350/
- https://www.bartington.com/magnetometers/mag-03/
