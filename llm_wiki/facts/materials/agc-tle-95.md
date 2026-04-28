---
fact_id: "materials-agc-tle-95"
title: "AGC TLE-95 microwave laminate material card"
topic: "TLE-95"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-tle-95-datasheet"]
tags: ["agc", "tle-95", "microwave", "low-loss", "high-speed-digital", "rf-materials", "laminate"]
---

# Canonical Summary

> TLE-95 is an AGC microwave / high-speed digital laminate with Dk published at `1 MHz` and Df published at `10 GHz`. PTH and SMT reliability wording is product positioning, not board-level reliability proof.

## Stable Facts

- AGC describes TLE-95 laminates as engineered for complex microwave and high-speed digital applications.
- AGC frames TLE-95 around microwave radios, satellite antenna systems, and passive components.
- At `1 MHz`, the TDS lists dielectric constant `2.95 +/- 0.05` by `IPC-650 2.5.5.3`.
- At `10 GHz`, the TDS lists dissipation factor `0.0026` by modified `IPC-650 2.5.5.5.1`.
- The same TDS lists unclad thermal conductivity `0.20 W/mK` by `ASTM F 433`.
- The same TDS lists CTE from `50 C to 150 C` as X `9 ppm/C`, Y `12 ppm/C`, and Z `70 ppm/C` by `ASTM D3386 (TMA)` / `IPC-650 2.4.41`.
- The same TDS lists moisture absorption `0.02%`, dielectric breakdown `60 kV`, arc resistance `180 seconds`, and UL-94 flammability `V-0`.
- The sheet lists typical thicknesses including `0.0052 in / 0.13 mm`, `0.0200 in / 0.51 mm`, `0.0300 in / 0.76 mm`, and `0.0620 in / 1.57 mm`, plus multiple sheet sizes.

## Conditions And Methods

- Keep Dk tied to `1 MHz` and Df tied to `10 GHz`; do not compare directly against cards whose Dk is measured at `10 GHz` without stating the method difference.
- Treat low Z-axis CTE / PTH reliability and X/Y expansion / SMT reliability language as material positioning only.
- Treat all data as typical values, matching the source note.

## Limits And Non-Claims

- This card does not prove microwave-radio, satellite-antenna, passive-component, high-speed-digital, PTH, or SMT finished-board performance.
- It does not prove plated-through-hole lifetime, thermal cycling success, insertion loss, antenna performance, or supplier build capability.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_TLE-95_TDS.pdf
