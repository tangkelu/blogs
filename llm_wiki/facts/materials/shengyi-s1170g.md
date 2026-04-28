---
fact_id: "materials-shengyi-s1170g"
title: "Shengyi S1170G exact-product material card"
topic: "S1170G"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids:
  - "shengyi-s1170g-product-page"
tags: ["shengyi", "s1170g", "halogen-free", "fr-4", "high-tg", "materials"]
---

# Canonical Summary

> `S1170G` is an exact-product Shengyi high-Tg halogen-free rigid-material row. Its product-page values may be used as source-scoped laminate parameters, not as generic halogen-free FR-4 averages, S1170GB prepreg data, or supplier-capability claims.

## Stable Facts

- Shengyi publishes an official English product page for `S1170G`.
- The page positions S1170G as lead-free compatible, halogen-free, UV-blocking / AOI compatible, lower Z-axis CTE material with `Tg 180 C` by DMA.
- The page lists Tg `180 C` by `IPC-TM-650 2.4.24.4` DMA and Td `390 C` at `5% wt. loss` by `IPC-TM-650 2.4.24.6`.
- The page lists Z-axis CTE `45 ppm/C` before Tg, `210 ppm/C` after Tg, and Z-axis expansion `2.3%` from `50 to 260 C` by `IPC-TM-650 2.4.24`.
- The page lists T260 `60 min` and T288 `60 min` by `IPC-TM-650 2.4.24.1` TMA.
- The page lists thermal stress at `288 C` solder dip as `pass` by `IPC-TM-650 2.4.13.1`.
- The page lists volume resistivity `5.65 x 10^7 MOhm.cm` after moisture resistance and `2.71 x 10^7 MOhm.cm` after `E-24/125`.
- The page lists surface resistivity `5.99 x 10^6 MOhm` after moisture resistance and `4.44 x 10^6 MOhm` after `E-24/125`.
- The page lists arc resistance `180 s`, dielectric breakdown `45+ kV NB`, Dk `4.4` at `1 GHz` for `RC52%`, and loss row value `0.010` at `1 GHz` for `RC52%`.
- The page lists peel strength after thermal stress `288 C / 10 s` as `1.3 N/mm`, peel strength at `125 C` as `1.1 N/mm`, flexural strength `550 / 450 MPa` in LW/CW, water absorption `0.12%`, and flammability `V-0`.
- The page states `IPC-4101/130` as reference, typical values are based on a `1.6 mm` specimen while Tg is for specimen `>=0.50 mm`, and typical values are not intended as specifications.

## Conditions And Methods

- Keep all values tied to the official S1170G page, its specimen notes, and its conditions.
- Preserve moisture-resistance and `E-24/125` conditions for resistivity values.
- Treat the page's `Dissipation Factor (Dk) RC52%` label cautiously as the page's loss row; do not generalize it into a universal Df table without source context.

## Limits And Non-Claims

- This card does not create a separate `S1170GB` prepreg fact card.
- It does not make S1170G interchangeable with S1150G, S1000-2, S1000-2M, S1170GB, or all halogen-free FR-4 materials.
- It does not prove finished-board reliability, lead-free assembly qualification, automotive qualification, AOI performance, procurement approval, HIL/APT capability, stock, price, MOQ, lead time, or yield.

## Source Links

- https://www.syst.com.cn/en/Product/info_257.aspx?itemid=11617
