---
fact_id: "materials-agc-tlx-8"
title: "AGC TLX-8 fiberglass-reinforced PTFE microwave substrate material card"
topic: "TLX-8"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-tlx-8-datasheet"]
tags: ["agc", "tlx-8", "ptfe", "fiberglass-reinforced", "microwave", "rf-materials", "low-dk", "laminate"]
---

# Canonical Summary

> TLX-8 is an AGC fiberglass-reinforced PTFE microwave substrate with low-Dk, low-Df, and low-layer-count RF design positioning. Space / severe-environment wording is not qualification proof.

## Stable Facts

- AGC identifies TLX-8 as a high-volume fiberglass-reinforced microwave substrate.
- AGC frames TLX-8 around antennas, mixers, splitters, filters, combiners, passive components, radar systems, mobile communications, microwave test equipment, microwave transmission devices, and RF components.
- The TDS lists dielectric constant `2.55 +/- 0.04` at `1 MHz` by `IPC-650 2.5.5.3`.
- The same TDS lists dissipation factor `0.0018` at `10 GHz` by modified `IPC-650 2.5.5.5.1`.
- The same TDS lists outgassing values TML `0.03%`, CVCM `0.00%`, and WVR `0.01%` under `4 h 257 F` at `<= 5 x 10^-5 Torr` by `ASTM E 595`.
- The same TDS lists thermal conductivity `0.19 W/mK` unclad by `ASTM F 433 / ASTM 1530-06`.
- The same TDS lists CTE from `25 C to 260 C` as X `21 ppm/C`, Y `23 ppm/C`, and Z `215 ppm/C` by `IPC-650 2.4.41 / TMA`.
- The same TDS lists Td `535 C` at `2%` weight loss and `553 C` at `5%` weight loss by `IPC-650 2.4.24.6 (TGA)`.
- The same TDS lists moisture absorption `0.02%`, dielectric breakdown `45 kV`, and UL-94 flammability `V-0`.
- The sheet lists typical thicknesses from `0.0050 in / 0.13 mm` to `0.1100 in / 2.79 mm`, copper cladding options, and multiple sheet sizes.

## Conditions And Methods

- Keep Dk tied to `1 MHz` and Df tied to `10 GHz`.
- Treat ASTM E 595 outgassing rows as source-scoped material test values, not space qualification.
- Treat all data as typical values, matching the source note.
- Treat copper-cladding, thickness, and sheet-size rows as AGC product availability context, not supplier stock or build-capability proof.

## Limits And Non-Claims

- This card does not prove antenna, radar, mobile-communication, microwave-test, space, warship, engine-module, altimeter, or severe-environment finished-board performance.
- It does not prove space qualification, radiation resistance, insertion loss, passive-component performance, or supplier build capability.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_TLX-8_TDS.pdf
