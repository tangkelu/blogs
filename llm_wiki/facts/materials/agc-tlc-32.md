---
fact_id: "materials-agc-tlc-32"
title: "AGC TLC-32 microwave laminate material card"
topic: "TLC-32"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-tlc-32-datasheet"]
tags: ["agc", "tlc-32", "microwave", "low-loss", "rf-materials", "laminate"]
---

# Canonical Summary

> TLC-32 is an AGC microwave laminate with Dk published at `1 MHz` and Df published at `10 GHz`. Its values are product-scoped typical material parameters only.

## Stable Facts

- At `1 MHz`, the TDS lists dielectric constant `3.20 +/- 0.05` by `IPC-650 2.5.5.3`.
- At `10 GHz`, the TDS lists dissipation factor `0.0030` by modified `IPC-650 2.5.5.5.1`.
- The same TDS lists unclad thermal conductivity `0.24 W/mK` by `ASTM F 433`.
- The same TDS lists CTE from `50 C to 150 C` as X `9 ppm/C`, Y `12 ppm/C`, and Z `70 ppm/C` by `ASTM D3386 / TMA`.
- The same TDS lists arc resistance `180 seconds` by `IPC-650 2.5.1` and UL-94 flammability `V-0`.
- The sheet lists typical thicknesses from `0.0100 in / 0.25 mm` to `0.1200 in / 3.04 mm` and multiple sheet sizes.

## Conditions And Methods

- Keep Dk tied to `1 MHz` and Df tied to `10 GHz`; do not compare directly against cards whose Dk is measured at `10 GHz` without stating the method difference.
- Treat all values as typical values and product-scoped only.
- Treat sheet-size and thickness rows as AGC product context, not supplier stock or capability proof.

## Limits And Non-Claims

- This card does not prove finished-board RF, microwave, antenna, insertion-loss, impedance, or channel performance.
- It does not prove PTH reliability, thermal cycling success, supplier process capability, or supplier stock.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_TLC-32_TDS.pdf
