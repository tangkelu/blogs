---
fact_id: "materials-agc-meteorwave-2000"
title: "AGC METEORWAVE 2000 baseline material card"
topic: "METEORWAVE 2000"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-meteorwave-2000-datasheet"]
tags: ["agc", "meteorwave-2000", "ultra-low-loss", "laminate", "prepreg", "high-speed", "caf"]
---

# Canonical Summary

> METEORWAVE 2000 is an AGC laminate and prepreg material positioned for high-speed, ultra-low-loss digital PCBs where low Dk/Df, CAF resistance, lead-free assembly context, and high-Tg FR-4-style processing are relevant.

## Stable Facts

- AGC describes METEORWAVE 2000 as a high-speed / ultra-low-loss laminate and prepreg material.
- The TDS frames METEORWAVE 2000 for `25 GHz and above` infrastructure, core routers, high-speed switches, cloud storage, supercomputers, and high-data-transfer-rate applications.
- The TDS lists `Dk 3.3 at 2 GHz` and `Dk 3.2 at 10 GHz` by `IPC-TM-650 2.5.5.5`.
- The same TDS lists `Df 0.0027 at 2 GHz` and `Df 0.0034 at 10 GHz`.
- The same TDS lists Tg `240 C` by DMA `Tan d Peak`.
- The same TDS lists degradation temperature `390 C` at `5%` weight loss and `T-300 >120 minutes`.
- The same TDS lists thermal conductivity `0.43 W/mK` by `ASTM E1461`.
- The same TDS lists X/Y CTE from `-40 C to +125 C` of `10-14 ppm/C`, Z-axis CTE Alpha 1 / Alpha 2 of `55 / 260 ppm/C`, and Z-axis expansion `1.5%`.
- The same TDS lists moisture absorption `0.12 wt.%`.
- The TDS states METEORWAVE 2000 meets `UL 94V-0` and `IPC-4101 /102`, with UL file number `E36295`.
- The TDS states METEORWAVE 2000 can be manufactured in laminate thickness from `2.0 mil / 0.05 mm` and up.

## Conditions And Methods

- Keep `2 GHz` and `10 GHz` Dk/Df values separate.
- Treat all listed values as typical datasheet values, not guaranteed specification limits.
- Treat CAF, IST, infrastructure, router, switch, storage, supercomputer, and high-data-rate wording as material-positioning context unless separate program, test, or capability evidence is attached.

## Limits And Non-Claims

- This card does not prove a finished board will meet any `25 GHz`, insertion-loss, impedance, channel, storage, router, switch, or supercomputer performance target.
- It does not prove CAF lifetime, high-layer-count manufacturability, lead-free assembly success, or IST performance for a specific stackup.
- It does not prove APT, HIL, or any other supplier capability, certification, yield, lead time, stock, price, or qualification status.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_2000_TDS.pdf
