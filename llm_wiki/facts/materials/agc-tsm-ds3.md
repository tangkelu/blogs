---
fact_id: "materials-agc-tsm-ds3"
title: "AGC TSM-DS3 low-loss microwave laminate material card"
topic: "TSM-DS3"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-tsm-ds3-datasheet"]
tags: ["agc", "tsm-ds3", "low-loss", "rf-materials", "microwave", "thermal-conductivity", "laminate"]
---

# Canonical Summary

> TSM-DS3 is an AGC ceramic-filled reinforced low-loss microwave laminate with low fiberglass content and high thermal-conductivity positioning. Its source contains board-level insertion-loss examples, but this card uses only material-parameter rows.

## Stable Facts

- AGC identifies TSM-DS3 as a dimensionally stable low-loss laminate and ceramic-filled reinforced material with low fiberglass content.
- AGC frames TSM-DS3 around couplers, phased-array antennas, radar manifolds, mmWave antenna / automotive, oil drilling, and semiconductor / ATE testing contexts.
- The TDS lists dielectric constant `3.00 +/- 0.05` by `IPC-650 2.5.5.3`.
- The same TDS lists dissipation factor `0.0014` by `IPC-650 2.5.5.5.1 (Modified)`.
- The same TDS lists thermal conductivity `0.65 W/mK` unclad by `ASTM F 433 / ASTM 1530-06`.
- The same TDS lists Td `526 C` at `2%` weight loss and `551 C` at `5%` weight loss by `IPC-650 2.4.24.6 (TGA)`.
- The same TDS lists CTE from room temperature to `125 C` as X `10 ppm/C`, Y `16 ppm/C`, and Z `23 ppm/C` by `IPC-650 2.4.41 / TMA`.
- The same TDS lists specific gravity `2.11`, dielectric breakdown `47.5 kV`, dielectric strength `21575 V/mm / 548 V/mil`, arc resistance `226 s`, and moisture absorption `0.07%`.
- The sheet lists typical thicknesses from `0.0050 in / 0.13 mm` to `0.0900 in / 2.29 mm` and multiple sheet sizes.

## Conditions And Methods

- Keep Dk / Df tied to their stated IPC methods.
- Treat the source's insertion-loss examples as blocked finished-board / test-vehicle context, not reusable material facts.
- Treat all data as typical values, matching the source note.
- Treat thickness and sheet-size rows as AGC product availability context, not supplier stock or build-capability proof.

## Limits And Non-Claims

- This card does not prove coupler, antenna, radar, mmWave, oil-drilling, ATE, high-power, or high-layer finished-board performance.
- It does not prove insertion loss, registration yield, sequential-lamination success, fastRise stackup success, resistor-foil performance, or supplier build capability.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_TSM-DS3_TDS.pdf
