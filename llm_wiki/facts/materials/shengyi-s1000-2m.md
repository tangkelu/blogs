---
fact_id: "materials-shengyi-s1000-2m"
title: "Shengyi S1000-2M baseline material card"
topic: "S1000-2M"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-25"
source_ids:
  - "shengyi-s1000-2m-product-page"
tags: ["shengyi", "s1000-2m", "fr-4", "high-tg", "multilayer", "materials"]
---

# Canonical Summary

> `S1000-2M` is an exact-product Shengyi high-Tg FR-4 anchor with a full public property table suitable for mainstream multilayer numeric baselines.

## Stable Facts

- Shengyi publishes an official exact-product page for `S1000-2M`.
- The page positions `S1000-2M` as a lead-free-compatible `FR-4.0` laminate suitable for high-layer-count PCB use.
- The table lists `Tg 180 C` by `DSC` and `185 C` by `DMA`.
- The table lists `Td 355 C` by `IPC-TM-650 2.4.24.6` at `5% wt. loss`.
- The table lists `CTE (Z-axis) 41 ppm/C` before `Tg`, `208 ppm/C` after `Tg`, and `2.4%` from `50 to 260 C`.
- The table lists `T260 >60 min`, `T288 30 min`, and `T300 15 min` by `IPC-TM-650 2.4.24.1`.
- The table lists `thermal stress >100 s` at `288 C` solder dip.
- The table lists `Dk 4.6` at `1 GHz` and `4.9` at `1 MHz`.
- The table lists `Df 0.018` at `1 GHz` and `0.015` at `1 MHz`.
- The table lists `water absorption 0.08%`, `peel strength 1.3 N/mm` after thermal stress at `288 C, 10 s`, `CTI PLC 3`, and flammability `V-0`.

## Conditions And Methods

- Keep numeric values tied to the official `S1000-2M` table and its stated methods/conditions.
- Keep `Dk` and `Df` frequencies explicit; do not collapse `1 MHz` and `1 GHz` values into one invariant number.
- Treat `high-layer-count PCB` wording as product positioning context rather than fabricator-capability proof.

## Limits And Non-Claims

- This card does not make `S1000-2M` interchangeable with `S1000-2` or all Shengyi `FR-4` products.
- It does not prove a specific lamination count, drill process, or board-level SI result.
- It does not turn page-level application wording into a universal stackup recommendation.

## Source Links

- https://www.syst.com.cn/en/Product/info_257.aspx?itemid=11623
