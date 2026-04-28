---
fact_id: "materials-agc-meteorwave-4000m"
title: "AGC METEORWAVE 4000M automotive-radar material card"
topic: "METEORWAVE 4000M"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-meteorwave-4000m-datasheet"]
tags: ["agc", "meteorwave-4000m", "ultra-low-loss", "laminate", "automotive-radar", "caf"]
---

# Canonical Summary

> METEORWAVE 4000M is an AGC high-frequency / ultra-low-loss laminate positioned for automotive radar material context, including 24 GHz and 77 GHz wording, while finished-board radar performance remains outside the datasheet's proof scope.

## Stable Facts

- AGC describes METEORWAVE 4000M as a high-frequency / ultra-low-loss laminate for automotive radar applications.
- The TDS frames applications as short-range `24 GHz` automotive radar and long-range `77 GHz` automotive radar, and states the material is positioned for automotive radar programs up to `77 GHz`.
- The TDS lists `Dk 3.2 at 10 GHz` by `IPC-TM-650 2.5.5.5`.
- The same TDS lists `Dk 3.18 at 77 GHz` for `RTF-2` and `Dk 3.20 at 77 GHz` for `HVLP2`, using a ring resonator method.
- The same TDS lists `Df 0.0020 at 10 GHz` by split-post dielectric resonator.
- The same TDS lists `TcDk 15 ppm/C` from `-50 C to 140 C` at `10 GHz`.
- The same TDS lists Tg `170 C` by TMA and Tg `200 C` by DMA `Tan d Peak`.
- The same TDS lists degradation temperature `390 C` at `5%` weight loss and `T-300 >120 minutes`.
- The same TDS lists thermal conductivity `0.46 W/mK` and specific heat `0.84 J/gK` by `ASTM E1461`.
- The same TDS lists X/Y CTE from `-40 C to +125 C` of `24 / 25 ppm/C` for a `5 mil 1x1078 construction`, Z-axis CTE Alpha 1 / Alpha 2 of `55 ppm/C`, and Z-axis expansion `2.6%`.
- The same TDS lists moisture absorption `0.12 wt.%`.
- The TDS states METEORWAVE 4000M meets `UL 94V-0` and `IPC-4101 /102`, with UL file number `E36295`.

## Conditions And Methods

- Keep `10 GHz` and `77 GHz` dielectric rows separate.
- Preserve copper and method notes for `77 GHz` Dk; do not average the `RTF-2` and `HVLP2` rows.
- Keep TMA and DMA Tg values separate.
- Treat all listed values as typical datasheet values, not guaranteed specification limits.

## Limits And Non-Claims

- This card does not prove finished-board radar range, resolution, antenna efficiency, insertion loss, phase stability, calibration performance, automotive qualification, or compliance.
- It does not prove a supplier can build or qualify an automotive radar PCB with this material.
- It does not prove APT, HIL, or any other supplier capability, certification, yield, lead time, stock, price, or qualification status.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_4000M_TDS.pdf
