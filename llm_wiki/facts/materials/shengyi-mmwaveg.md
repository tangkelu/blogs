---
fact_id: "materials-shengyi-mmwaveg"
title: "Shengyi mmWave G exact-product material card"
topic: "mmWave G"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids:
  - "shengyi-mmwaveg-product-page"
tags: ["shengyi", "mmwaveg", "rf-materials", "mmwave", "low-loss", "materials"]
---

# Canonical Summary

> `mmWave G` is an exact-product Shengyi RF / mmWave material row. Its product-page values may be used as source-scoped material parameters, not as finished radar, antenna, satellite, or supplier-capability claims.

## Stable Facts

- Shengyi publishes an official English product page for `mmWave G`.
- The page lists process Dk `3.00` at `10 GHz / 23 C` by balanced type circular disk resonator.
- The page lists process Dk `3.16` at `10 GHz / 23 C` by `IPC-TM-650 2.5.5.15`.
- The page lists design Dk `3.18` at `77 GHz / 23 C` by resonator ring.
- The page lists Df `0.002` at `10 GHz / 23 C` by balanced type circular disk resonator.
- The page lists Df `0.002` at `10 GHz / 23 C` by `IEC 61189-2-721 (SPDR)`.
- The page lists CTE `20 / 20 / 40 ppm/C` for X/Y/Z by `IPC-TM-650 2.4.41`, TMA `-55 to 288 C`.
- The page lists Tg `200 C` by `IPC-TM-650 2.4.24.4` DMA and Td `395 C` by `ASTM D3850` TGA.
- The page lists volume resistivity `1.32 x 10^11 MOhm-cm`, surface resistivity `1.04 x 10^11 MOhm`, peel strength `0.60 N/mm [3.73 lb/in]` after `288 C / 10 s`, water absorption `0.06%`, thermal conductivity `0.40 W/(m.K)` at `100 C`, density `1.52 g/cm3`, and flammability `V-0`.
- The page states typical values are reference values and are not intended as specifications.

## Conditions And Methods

- Keep the two process-Dk methods separate.
- Keep `77 GHz` design Dk separate from `10 GHz` process-Dk and Df values.
- Treat application bullets as material positioning context only.

## Limits And Non-Claims

- This card does not prove finished-board insertion loss, antenna efficiency, radar detection, satellite performance, PIM, RF compliance, or mmWave qualification.
- It does not create a separate `mmWaveGB` prepreg fact card.
- It does not prove APT, HIL, or any supplier's material stock, process capability, certification, procurement approval, price, MOQ, lead time, or yield.

## Source Links

- https://www.syst.com.cn/en/Product/info_257.aspx?itemid=11661
