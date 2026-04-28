---
fact_id: "materials-agc-meteorwave-8000"
title: "AGC METEORWAVE 8000 baseline material card"
topic: "METEORWAVE 8000"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-meteorwave-8000-datasheet"]
tags: ["agc", "meteorwave-8000", "extremely-low-loss", "laminate", "prepreg", "high-speed", "caf", "backplane"]
---

# Canonical Summary

> METEORWAVE 8000 is an AGC laminate and prepreg material positioned for high-speed, extremely-low-loss digital PCBs where low Dk/Df, CAF resistance, high-Tg FR-4-style processing, and high-layer-count reliability context are relevant.

## Stable Facts

- AGC describes METEORWAVE 8000 as a high-speed / extremely-low-loss laminate and prepreg material.
- The TDS frames METEORWAVE 8000 for telecommunications, high-speed services, storage networks, internet switching / routing systems, and wireless-communications backplanes.
- The TDS states the material is designed for high-layer-count PCBs and intended for 100 Gbps core routers, high-speed switches, supercomputers, and high-data-transfer-rate applications.
- The TDS lists `Dk 3.29 at 2 GHz` and `Dk 3.28 at 10 GHz` by `IPC-TM-650 2.5.5.5`.
- The same TDS lists `Df 0.0012 at 2 GHz` and `Df 0.0016 at 10 GHz`.
- The same TDS lists Tg `165 C` by TMA and Tg `185 C` by DMA `Tan d Peak`.
- The same TDS lists degradation temperature `376 C` at `5%` weight loss and `T-300 40 minutes`.
- The same TDS lists thermal conductivity `0.51 W/mK` by `ASTM E1461`.
- The same TDS lists X/Y CTE from `-40 C to +125 C` of `14 / 16 ppm/C`, Z-axis CTE Alpha 1 / Alpha 2 of `35 / 185 ppm/C`, and Z-axis expansion `2.5%`.
- The same TDS lists moisture absorption `0.01 wt.%`.
- The TDS states METEORWAVE 8000 meets `UL 94V-0` and `IPC4101 /102`, with UL file number `E36295`.
- The TDS states the series can be manufactured in laminate thickness from `1.2 mil / 0.031 mm` and up.

## Conditions And Methods

- Keep `2 GHz` and `10 GHz` Dk/Df values separate.
- Keep TMA and DMA Tg values separate.
- Treat `100 Gbps`, NASA outgassing, CAF, and high-layer-count language as material-positioning context unless separate program, test, or capability evidence is attached.
- Treat the values as typical datasheet values, not guaranteed specification limits.

## Limits And Non-Claims

- This card does not prove a finished board will meet a 100 Gbps, switch, router, storage, supercomputer, or backplane performance target.
- It does not prove channel loss, controlled impedance, CAF lifetime, outgassing acceptance, or high-layer-count manufacturability for a specific stackup.
- It does not prove APT, HIL, or any other supplier capability, certification, yield, lead time, or qualification status.

## Open Questions

- Whether to add a METEORWAVE family selector covering `4000`, `8000`, and later `1000NF / 3000 / 4000M` rows.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_8000_TDS.pdf
