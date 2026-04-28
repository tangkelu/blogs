---
fact_id: "materials-agc-tsm-ds3m"
title: "AGC TSM-DS3M low-loss microwave laminate material card"
topic: "TSM-DS3M"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-tsm-ds3m-datasheet"]
tags: ["agc", "tsm-ds3m", "low-loss", "rf-materials", "microwave", "military", "thermal-conductivity", "laminate"]
---

# Canonical Summary

> TSM-DS3M is an AGC TSM variant with low-loss, low-fiberglass, thermal-conductivity, and military-application positioning. Its military wording is application context only, not qualification proof.

## Stable Facts

- AGC identifies TSM-DS3M as a dimensionally stable low-loss laminate and ceramic-filled reinforced material with low fiberglass content.
- AGC frames TSM-DS3M around avionics / aerospace microstrip and stripline circuitry, couplers, phased-array antennas, radar manifolds, mmWave antenna / automotive, oil drilling, and semiconductor / ATE testing contexts.
- At `10 GHz`, the TDS lists dielectric constant `2.94 +/- 0.04` by `IPC-650 2.5.5.5.1 (Modified)`.
- At `10 GHz`, the TDS lists dissipation factor `0.0014` by `IPC-650 2.5.5.5.1 (Modified)`.
- The same TDS lists thermal conductivity `0.65 W/mK` unclad by `ASTM F 433 / ASTM 1530-06`.
- The same TDS lists Td `526 C` at `2%` weight loss and `551 C` at `5%` weight loss by `IPC-650 2.4.24.6 (TGA)`.
- The same TDS lists CTE from room temperature to `125 C` as X `10 ppm/C`, Y `16 ppm/C`, and Z `23 ppm/C` by `IPC-650 2.4.41 / TMA`.
- The source shows method-dependent TcK examples: `-11 ppm/C` from `-55 C to 150 C` by `IPC-650 2.5.5.6` without pressure, `+5.4 ppm/C` from `-30 C to 120 C` by modified `IPC-650 2.5.5.5.1` with pressure, and `-6.6 ppm/C` from `-55 C to 150 C` by `IPC-650 2.5.5.5` with pressure.
- The same TDS lists specific gravity `2.11`, dielectric breakdown `47.5 kV`, dielectric strength `21575 V/mm / 548 V/mil`, arc resistance `226 s`, and moisture absorption `0.07%`.
- The sheet lists typical thicknesses from `0.0050 in / 0.13 mm` to `0.0900 in / 2.29 mm` and multiple sheet sizes.

## Conditions And Methods

- Preserve `10 GHz` and modified IPC method on Dk / Df values.
- Keep TcK values tied to their exact IPC method, temperature range, and pressure condition.
- Treat all data as typical values, matching the source note.
- Treat military / avionics / aerospace wording as application context, not qualification or supplier approval.

## Limits And Non-Claims

- This card does not prove avionics, aerospace, military, radar, mmWave, oil-drilling, ATE, high-power, or high-layer finished-board performance.
- It does not prove insertion loss, registration yield, sequential-lamination success, resistor-foil performance, qualification, or supplier build capability.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_TSM-DS3M_TDS.pdf
