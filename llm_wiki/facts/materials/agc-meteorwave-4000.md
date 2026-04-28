---
fact_id: "materials-agc-meteorwave-4000"
title: "AGC METEORWAVE 4000 baseline material card"
topic: "METEORWAVE 4000"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-meteorwave-4000-datasheet"]
tags: ["agc", "meteorwave-4000", "ultra-low-loss", "laminate", "prepreg", "high-speed", "caf", "high-layer-count"]
---

# Canonical Summary

> METEORWAVE 4000 is an AGC laminate and prepreg material positioned for ultra-low-loss high-speed PCB work where low Dk/Df, high Tg, CAF resistance, lead-free assembly compatibility, and high-layer-count construction context are relevant.

## Stable Facts

- AGC describes METEORWAVE 4000 as an ultra-low-loss material available as laminate and prepreg.
- The TDS frames METEORWAVE 4000 for `25 GHz and above` infrastructure, automotive radar, high-speed switches, core routers, supercomputers, and high-data-rate applications.
- The TDS states the material is designed for high-temperature lead-free assemblies and high-layer-count PCB designs that require high reliability, CAF resistance, and low Z-axis expansion.
- The TDS lists `Dk 3.4 at 2 GHz` and `Dk 3.3 at 10 GHz` by `IPC-TM-650 2.5.5.5`.
- The same TDS lists `Df 0.0019 at 2 GHz` and `Df 0.0024 at 10 GHz`.
- The same TDS lists Tg `200 C` by DMA `Tan d Peak`, degradation temperature `390 C` at `5%` weight loss, and `T-300 >120 minutes`.
- The same TDS lists thermal conductivity `0.45 W/mK` by `ASTM E1461`.
- The same TDS lists X/Y CTE from `-40 C to +125 C` of `10 / 14 ppm/C`, Z-axis CTE Alpha 1 / Alpha 2 of `55 / 260 ppm/C`, and Z-axis expansion `2.1%`.
- The same TDS lists moisture absorption `0.08 wt.%`.
- The TDS states METEORWAVE 4000 meets `UL 94V-0` and `IPC4101 /102`, with UL file number `E36295`.
- The TDS states the series can be manufactured in laminate thickness from `2 mil / 0.050 mm` and up.

## Conditions And Methods

- Keep `2 GHz` and `10 GHz` Dk/Df values separate.
- Keep Tg tied to DMA `Tan d Peak`.
- Treat CAF resistance, IST performance, high-layer-count, and lead-free assembly wording as AGC material-positioning context unless a specific test report or capability record is attached.
- Treat the values as typical datasheet values, not guaranteed specification limits.

## Limits And Non-Claims

- This card does not prove a finished board will meet a `25 GHz+`, radar, switch, router, or supercomputer performance target.
- It does not prove controlled impedance, insertion loss, CAF lifetime, IST survival, or high-layer-count manufacturability for any specific stackup.
- It does not prove APT, HIL, or any other supplier capability, certification, yield, lead time, or qualification status.

## Open Questions

- Whether to add METEORWAVE 4000 to the high-speed material-family selector alongside Isola, Panasonic, ITEQ, Rogers, and Ventec rows.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_4000_TDS.pdf
