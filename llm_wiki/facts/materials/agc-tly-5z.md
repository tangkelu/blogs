---
fact_id: "materials-agc-tly-5z"
title: "AGC TLY-5Z PTFE laminate material card"
topic: "TLY-5Z"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-tly-5z-datasheet"]
tags: ["agc", "tly-5z", "ptfe", "low-dk", "low-loss", "rf-materials", "laminate"]
---

# Canonical Summary

> TLY-5Z is an AGC low-Dk PTFE laminate with Dk / Df values published at `10 GHz` by a modified IPC method. It must stay separate from TLY-5 and TLY-5A.

## Stable Facts

- At `10 GHz`, the TDS lists dielectric constant `2.20 +/- 0.04` by modified `IPC-650 2.5.5.5.1`.
- At `10 GHz`, the TDS lists dissipation factor `0.0015` by modified `IPC-650 2.5.5.5.1`.
- The same TDS lists thermal conductivity `0.2 W/mK` by `IPC-650 2.4.50`.
- The same TDS lists CTE from `25 C to 260 C` as X `30 ppm/C`, Y `40 ppm/C`, and Z `130 ppm/C` by `IPC-650 2.4.41`.
- The same TDS lists specific gravity `1.92` by `IPC-650 2.3.5`.
- The same TDS lists moisture absorption `0.03%` by `IPC-650 2.6.2.1` and UL-94 flammability `V-0`.
- The same TDS lists dimensional-stability rows for `10 mil` and `30 mil` material after bake and stress.
- The sheet lists typical thicknesses from `0.0100 in / 0.25 mm` to `0.0600 in / 1.52 mm` and multiple sheet sizes.

## Conditions And Methods

- Preserve `10 GHz` and modified IPC-650 `2.5.5.5.1` on Dk / Df values.
- Preserve the separate thermal-conductivity method `IPC-650 2.4.50`.
- Do not merge TLY-5Z values into TLY-5, TLY-5A, or generic TLY family defaults.
- Treat all data as typical values, matching the source note.

## Limits And Non-Claims

- This card does not prove finished-board RF, radar, antenna, insertion-loss, impedance, or mmWave performance.
- It does not prove manufacturing yield, layer-stack success, supplier process capability, or supplier stock.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_TLY-5Z_TDS.pdf
