---
fact_id: "materials-agc-meteorwave-m1"
title: "AGC METEORWAVE M1 mmWave material card"
topic: "METEORWAVE M1"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-meteorwave-m1-datasheet"]
tags: ["agc", "meteorwave-m1", "ultra-low-loss", "laminate", "prepreg", "automotive-radar", "mmwave"]
---

# Canonical Summary

> METEORWAVE M1 is an AGC high-frequency / ultra-low-loss laminate and prepreg positioned for automotive radar and mmWave material context, including `77 GHz` wording, while finished-board radar and antenna performance remain outside the datasheet proof scope.

## Stable Facts

- AGC describes METEORWAVE M1 as a high-frequency / ultra-low-loss laminate and prepreg for automotive radar and mmWave applications.
- The TDS states METEORWAVE M1 is positioned for automotive radar programs up to `77 GHz`.
- The TDS lists dielectric constant `3.1 at 10 GHz` by `IPC-TM-650 2.5.5.5`.
- The same TDS lists dielectric constant `3.10 at 77 GHz` with `RTF2 copper` by ring resonator method.
- The same TDS lists dissipation factor `0.0018 at 10 GHz` by split-post dielectric resonator.
- The same TDS lists `TcDk 12 ppm/C` from `-50 C to 140 C` for Dk versus temperature at `10 GHz`.
- The same TDS lists volume resistivity `2.8 x 10^8 MOhm` at `C-96 / 35 / 90` and `1.9 x 10^8 MOhm` at `E-24 / 125`.
- The same TDS lists surface resistivity `4.0 x 10^7 MOhm` at `C-96 / 35 / 90` and `7.7 x 10^7 MOhm` at `E-24 / 125`.
- The same TDS lists electric strength `69 kV/mm`, dielectric breakdown `>50 kV`, and arc resistance `>180 seconds`.
- The same TDS lists Tg `230 C` by DMA `Tan d Peak`.
- The same TDS lists degradation temperature `391 C` at `5%` weight loss and `T-300 >120 minutes`.
- The same TDS lists thermal conductivity `0.54 W/mK` at room temperature and specific heat `0.95 J/gK` at `20 C`.
- The same TDS lists X/Y CTE from `-40 C to +125 C` of `18 / 18 ppm/C` for a `5 mil 1x1078 construction`, Z-axis CTE Alpha 1 / Alpha 2 of `47 / 178 ppm/C`, and Z-axis expansion `2.4%`.
- The same TDS lists moisture absorption `0.088 wt.%` and flammability `V-0`.
- The TDS states METEORWAVE M1 meets `UL 94V-0`, `IPC-4101 /102`, `IPC-4103 /240` laminate, and `IPC-4103 /540` prepreg specifications, with UL file number `E36295`.

## Conditions And Methods

- Keep `10 GHz` and `77 GHz` dielectric rows separate.
- Preserve the `RTF2 copper` and ring-resonator condition for the `77 GHz` Dk row.
- Treat all listed values as typical datasheet values, not guaranteed specification limits.

## Limits And Non-Claims

- This card does not prove finished-board automotive radar range, resolution, antenna efficiency, insertion loss, phase stability, EIRP, calibration, chamber / OTA result, or automotive qualification.
- It does not prove aerospace, defense, satellite, or mmWave application readiness for a supplier or design.
- It does not prove APT, HIL, or any other supplier capability, certification, yield, lead time, stock, price, or qualification status.
- It does not provide a reusable lamination recipe for suppliers or designs.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_M1_TDS.pdf
