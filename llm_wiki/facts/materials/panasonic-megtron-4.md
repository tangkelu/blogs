---
fact_id: "materials-panasonic-megtron-4"
title: "MEGTRON 4 R-5725 / R-5620 baseline material card"
topic: "MEGTRON 4"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-25"
source_ids:
  - "panasonic-megtron-4-r5725-r5620"
  - "panasonic-megtron-4-datasheet"
tags: ["panasonic", "megtron-4", "r-5725", "r-5620", "high-speed", "low-loss", "materials"]
---

# Canonical Summary

> `MEGTRON 4` `R-5725 / R-5620` is now an exact-grade Panasonic low-loss multilayer anchor with public model-level values, so it can serve as the lower-loss Panasonic baseline below `MEGTRON 6 / 7 / 8`.

## Stable Facts

- Panasonic publishes an official model page for `MEGTRON 4` `R-5725 / R-5620`.
- Panasonic also exposes an official `R-5725` datasheet file linked from that model page.
- The model page lists `Tg 176 C` by `DSC`, `170 C` by `TMA`, and `210 C` by `DMA`.
- The page lists `Td 360 C`.
- The page lists `T288 >120 min` without copper and `30 min` with copper.
- The page lists `CTE-Z 35 ppm/C` below `Tg` and `CTE alpha2 Z-axis 265 ppm/C`.
- The page lists in-plane `CTE` below `Tg` in the `12 to 15 ppm/C` range.
- The page lists `Dk 3.8` at `1 GHz` and `10 GHz`.
- The page lists `Df 0.005` at `1 GHz` and `0.007` at `10 GHz`.
- The page lists `thermal conductivity 0.60 W/m.K`, `water absorption 0.14%`, `peel strength 1.1 kN/m`, volume resistivity `1 x 10^9 MOhm.cm`, surface resistivity `1 x 10^8 MOhm`, and flammability `94V-0`.

## Conditions And Methods

- Keep all numeric values tied to the `R-5725 / R-5620` model page and datasheet layer rather than the broader series page.
- Keep the frequency-specific dielectric values explicit.
- Treat server/router/high-speed positioning as product context, not as board-level SI or throughput proof.

## Limits And Non-Claims

- This card does not make `MEGTRON 4` interchangeable with `MEGTRON 6`, `MEGTRON 7`, or `MEGTRON 8`.
- It does not prove a specific channel budget, insertion-loss target, or high-layer-count manufacturing outcome.
- It does not turn Panasonic family positioning into a generic supplier-capability claim.

## Source Links

- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/lineup/megtron-series/series/127607/model/131587
- https://api.pim.na.industrial.panasonic.com/file_stream/main/fileversion/180147
