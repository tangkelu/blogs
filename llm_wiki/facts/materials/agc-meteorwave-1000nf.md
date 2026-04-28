---
fact_id: "materials-agc-meteorwave-1000nf"
title: "AGC METEORWAVE 1000NF no-flow prepreg material card"
topic: "METEORWAVE 1000NF"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-meteorwave-1000nf-datasheet"]
tags: ["agc", "meteorwave-1000nf", "no-flow-prepreg", "very-low-loss", "bonding", "rigid-flex", "caf"]
---

# Canonical Summary

> METEORWAVE 1000NF is an AGC high-speed / very-low-loss no-flow prepreg based on the METEORWAVE 1000 resin system, positioned for bonding, flex circuitry, heat-sink attachment, and high-layer-count PCB designs that require controlled resin flow.

## Stable Facts

- AGC describes METEORWAVE 1000NF as a no-flow prepreg based on the METEORWAVE 1000 resin system.
- The TDS frames it for high-speed switches and networks, wireless communication, rigid-flex bonding, heat-sink attachment, and use cases requiring minimal and uniform resin flow.
- The TDS lists typical flow migration `50-120 mils` by `IPC-TM-650 2.3.17.2` and available glass styles `106` and `1080`.
- The available-prepreg table lists glass style `106`, `65%` RC, `0.0016 inch` thickness, `Dk 3.41 at 10 GHz`, and `Df 0.0047 at 10 GHz`.
- The same table lists glass style `1080`, `61%` RC, `0.0027 inch` thickness, `Dk 3.49 at 10 GHz`, and `Df 0.0049 at 10 GHz`.
- The bulk-property table lists `Dk 3.45 at 2 GHz` and `Dk 3.50 at 10 GHz` by `IPC-TM-650 2.5.5.5`.
- The same bulk-property table lists `Df 0.0038 at 2 GHz` and `Df 0.0048 at 10 GHz`.
- The same TDS lists Tg `240 C` by DMA `Tan d Peak`.
- The same TDS lists degradation temperature `390 C` at `5%` weight loss and `T-300 >120 minutes`.
- The same TDS lists thermal conductivity `0.46 W/mK`, X/Y CTE from `-40 C to +125 C` of `10 / 14 ppm/C`, Z-axis CTE Alpha 1 / Alpha 2 of `55 / 260 ppm/C`, Z-axis expansion `1.5%`, and moisture absorption `0.12 wt.%`.
- The TDS states METEORWAVE 1000NF meets `UL 94V-0` and `IPC-4101 /102`, with UL file number `E36295`.

## Conditions And Methods

- Keep available-prepreg construction rows separate from the bulk-property Dk/Df rows.
- Keep `2 GHz` and `10 GHz` Dk/Df values separate.
- Treat flow, bonding, and heat-sink attachment language as material-positioning context, not a supplier lamination recipe.
- Treat all listed values as typical datasheet values, not guaranteed specification limits.

## Limits And Non-Claims

- This card does not prove a finished rigid-flex or heat-sink-bonded board will pass reliability, thermal, or mechanical requirements.
- It does not prove lamination pressure, cycle, registration, voiding, adhesive, or delamination outcomes for any specific stackup.
- It does not prove APT, HIL, or any other supplier capability, certification, yield, lead time, stock, price, or qualification status.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_1000NF_TDS.pdf
