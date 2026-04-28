---
fact_id: "materials-tuc-tu-872-lk"
title: "TUC TU-872 LK low-Dk / low-Df high-thermal-reliability material card"
topic: "TU-872 LK"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["tuc-tu-872-lk-datasheet-page"]
tags: ["tuc", "tu-872-lk", "low-dk", "low-df", "high-thermal-reliability", "fr4", "laminate", "prepreg"]
---

# Canonical Summary

> TU-872 LK is a TUC modified epoxy FR-4 low-Dk / low-Df laminate and TU-87P LK prepreg positioned for high-speed, low-loss, high-frequency multilayer material contexts. Its values do not prove finished-board SI or stackup reliability.

## Stable Facts

- TUC identifies TU-872 LK core and TU-87P LK prepreg as a low-Dk / low-Df and high-thermal-reliability laminate and prepreg with datasheet code `DS1801019B`.
- TUC frames TU-872 LK around backpanel, high-performance computing, line cards, storage, servers, telecom, base station, and office-router contexts.
- The sheet lists IPC-4101E type designations `/29`, `/99`, `/101`, `/126`, IPC-4101E `/126` Validation Services QPL Certified wording, UL file `E189572`, flammability `94V-0`, and maximum operating temperature `130 C`.
- The sheet lists Tg `220 C` by DMA, Tg `200 C` by DSC, Tg `190 C` by TMA, and Td `340 C` by TGA.
- The same sheet lists X-axis CTE and Y-axis CTE `12~15 ppm/C` and Z-axis expansion `2.5%`.
- The same sheet lists thermal stress solder float at `288 C` as `>60 sec`, T260 `60 min`, T288 `20 min`, and T300 `5 min`.
- At `RC50%`, the sheet lists permittivity `4.0 / 3.8` at `1 GHz` by `SPC method / 4291B`.
- At `RC50%`, the sheet lists permittivity `3.8` at `5 GHz` and `3.8` at `10 GHz` by `SPC method`.
- At `RC50%`, the sheet lists loss tangent `0.008 / 0.006` at `1 GHz` by `SPC method / 4291B`.
- At `RC50%`, the sheet lists loss tangent `0.008` at `5 GHz` and `0.009` at `10 GHz` by `SPC method`.
- The same sheet lists volume resistivity `>10^10 MOhm-cm`, surface resistivity `>10^8 MOhm`, electric strength `>40 kV/mm`, dielectric breakdown `>50 kV`, Young's modulus `26 GPa` warp / `24 GPa` fill, peel strength `4~7 lb/in` for `1.0 oz RTF Cu foil`, and water absorption `0.15%`.
- The sheet lists thickness availability from `0.002 in / 0.05 mm` to `0.062 in / 1.58 mm`, copper foil cladding from `1/3 oz` to `5 oz`, and glass styles including `106`, `1080`, `3313`, and `2116`.

## Conditions And Methods

- Preserve `RC50%`, frequency, and `SPC method / 4291B` method labels on Dk / Df values.
- Treat all values as information-only / typical, matching the source note.
- Treat QPL wording as product-source context, not a supplier qualification or finished-board approval.
- Do not turn backpanel, server, telecom, or base-station wording into board-level performance proof.

## Limits And Non-Claims

- This card does not prove backplane, HPC, storage, server, telecom, base-station, or office-router finished-board performance.
- It does not prove insertion loss, impedance tolerance, signal integrity, stackup reliability, CAF lifetime, qualification, or supplier build success.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.tuc.com.tw/en-us/products-detail/id/1
