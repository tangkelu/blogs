---
fact_id: "materials-agc-meteorwave-8300"
title: "AGC METEORWAVE 8300 material card"
topic: "METEORWAVE 8300"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-meteorwave-8300-datasheet"]
tags: ["agc", "meteorwave-8300", "ultra-low-loss", "low-dk", "laminate", "prepreg"]
---

# Canonical Summary

> METEORWAVE 8300 is an AGC high-speed / ultra-low-loss laminate and prepreg system with source-scoped `Dk <= 3.0` positioning, but the datasheet does not prove finished-board RF, radar, satellite, or high-speed-channel performance.

## Stable Facts

- AGC describes METEORWAVE 8300 as a high-speed / ultra-low-loss `Dk <= 3.0` laminate and prepreg system based on METEORWAVE 8000 and tailored for RF and microwave markets.
- The TDS lists dielectric constant `3.03 at 2 GHz` and `3.00 at 10 GHz` by `IPC-TM-650 2.5.5.5`.
- The same TDS lists dissipation factor `0.0022 at 2 GHz` and `0.0025 at 10 GHz`.
- The same TDS lists volume resistivity `4.2 x 10^6 MOhm-cm` at `C-96 / 35 / 90` and `8.8 x 10^7 MOhm-cm` at `E-24 / 125`.
- The same TDS lists surface resistivity `3.1 x 10^5 MOhm` at `C-96 / 35 / 90` and `3.6 x 10^7 MOhm` at `E-24 / 125`.
- The same TDS lists electric strength `5.9 x 10^4 V/mm` / `1500 V/mil`.
- The same TDS lists Tg `190 C` by DMA `Tan d Peak`.
- The same TDS lists degradation temperature `376 C` at `5%` weight loss and `T-300 40 minutes`.
- The same TDS lists thermal conductivity `0.51 W/mK` and specific heat `0.943 J/gK`.
- The same TDS lists X/Y CTE from `-40 C to +125 C` of `14 / 16 ppm/C`, Z-axis CTE Alpha 1 / Alpha 2 of `33 / 180 ppm/C`, and Z-axis expansion `2.5%`.
- The same TDS lists moisture absorption `0.01 wt.%`.
- The TDS states METEORWAVE 8300 meets `UL 94V-0`, `IPC-4101 /102`, `IPC-4103 /230` laminate, and `IPC-4103 /530` prepreg specifications, with UL file number `E36295`.
- The TDS states METEORWAVE 8300 can be manufactured in laminate thickness from `1.2 mil / 0.031 mm` and up.

## Conditions And Methods

- Keep `2 GHz` and `10 GHz` dielectric rows separate.
- Treat the listed values as typical datasheet values, not guaranteed specification limits.
- Treat `Dk <= 3.0 +/- 0.05` wording as material-positioning context unless exact construction and review conditions are available.

## Limits And Non-Claims

- This card does not prove finished-board radar, satellite, base-station, antenna, insertion-loss, impedance, channel, GPS, guidance, or RF performance.
- It does not prove CAF lifetime, high-layer-count manufacturability, lead-free assembly success, or reliability for a specific stackup.
- It does not prove APT, HIL, or any other supplier capability, certification, yield, lead time, stock, price, or qualification status.
- It does not provide a reusable lamination recipe for suppliers or designs.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_8300_TDS.pdf
