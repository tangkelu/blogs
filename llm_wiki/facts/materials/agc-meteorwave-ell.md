---
fact_id: "materials-agc-meteorwave-ell"
title: "AGC METEORWAVE ELL laminate and prepreg material card"
topic: "METEORWAVE ELL"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-meteorwave-ell-datasheet"]
tags: ["agc", "meteorwave-ell", "ell", "high-speed", "low-loss", "laminate", "prepreg"]
---

# Canonical Summary

> METEORWAVE ELL is an AGC laminate and prepreg family with ELL 101 / 102 / 103 variant rows. Its high-speed, 112 Gb, telecom, AI, automotive-radar, and aerospace wording is manufacturer positioning, not finished-board proof.

## Stable Facts

- AGC identifies the product family as `METEORWAVE ELL 101`, `ELL 102`, and `ELL 103`, with laminate and prepreg material forms.
- AGC maps ELL 101 to the resin system on NE fabric, ELL 102 to the resin system on NER fabric, and ELL 103 to the resin system on L2 fabric.
- At `10 GHz`, the TDS lists Dk `3.05` for `ELL 101` and Dk `3.03` for `ELL 102 / 103` by `IPC-TM-650.2.5.5.5`.
- At `10 GHz`, the TDS lists Df `0.0012` for `ELL 101` and Df `0.0009` for `ELL 102 / 103`.
- The same TDS lists electric strength `65 kV/mm` by `IPC-TM-650.2.5.6.2`.
- The same TDS lists Tg `190 C` by DMA tan-delta peak and `IPC-TM-650.2.4.24.3`, and Td `376 C` at `5%` weight loss by `IPC-TM-650.2.3.40`.
- The same TDS lists `T-288 >120 min` and `T-300 >60 min` by `IPC-TM-650.2.4.24.1`.
- The same TDS lists thermal conductivity `0.475 W/mK` by `ASTM E1461`.
- The same TDS lists X / Y CTE `12 / 12 ppm/C` from `-40 C to +125 C` by `IPC-TM-650.2.4.41`.
- The same TDS lists Z-axis CTE alpha 1 / alpha 2 as `65 / 156 ppm/C` from `50 C to Tg / Tg to 260 C` at `55% RC`, and Z-axis expansion `1.8%` from `50 C to 260 C` at `43% RC`.
- The same TDS lists moisture absorption `0.036 wt.%` and outgas TML / CVCM / WVR as `0.34 / <0.01 / <0.01 wt.%`.
- The sheet states laminate thickness from `1.2 mil / 0.031 mm` and up, with availability in common panel sizes.

## Conditions And Methods

- Preserve the ELL 101 vs ELL 102 / 103 split; do not flatten values into one generic ELL Dk / Df row.
- Keep Dk / Df tied to `10 GHz` and `IPC-TM-650.2.5.5.5`.
- Treat all values as typical values, matching the source note.
- Treat compliance and UL wording as direct source wording only when needed and refresh before evidence-pack use.

## Limits And Non-Claims

- This card does not prove 112 Gb channel performance, SI margin, insertion loss, telecom system readiness, AI server readiness, automotive-radar performance, aerospace qualification, or cloud / router deployment suitability.
- It does not prove supplier lamination recipes, process windows, stackup defaults, production yield, or supplier build capability.
- It does not prove APT, HIL, or any other supplier certification, price, MOQ, stock, lead time, or production approval.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_ELL_TDS.pdf
