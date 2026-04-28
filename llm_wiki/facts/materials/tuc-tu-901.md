---
fact_id: "materials-tuc-tu-901"
title: "TUC TU-901 Tg260 halogen-free laminate / prepreg material card"
topic: "TU-901"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["tuc-tu-901-datasheet-page"]
tags: ["tuc", "tu-901", "tg260", "halogen-free", "low-dk", "low-df", "ultra-low-insertion-loss", "laminate", "prepreg"]
---

# Canonical Summary

> TU-901 is a TUC Tg 260 C halogen-free laminate / TU-901P prepreg positioned for low-Dk / low-Df, low-CTE, high-modulus, and ultra-low-insertion-loss material contexts. Its values do not prove finished-board insertion loss or reliability.

## Stable Facts

- TUC identifies TU-901 core and TU-901P prepreg as a Tg 260 C halogen-free laminate and prepreg with datasheet code `DS2407002A`.
- TUC frames TU-901 around substrate, HDI / ELIC design, high-speed / high-frequency applications, and aerospace / military harsh-environment contexts.
- The sheet lists IPC-4101E specification number `/134`, IPC-4101E `/134` Validation Services QPL Certified wording, UL file `E189572`, flammability `94V-0`, and maximum operating temperature `160 C`.
- The sheet lists Tg `260 C` by DMA, Tg `230 C` by TMA, and Td `430 C` by TGA, with conditioning `E-2/105`.
- The same sheet lists X/Y-axis CTE `8/10 ppm/C`, Z-axis CTE `25-35 ppm/C` from ambient to Tg, Z-axis CTE `140-150 ppm/C` from Tg to `260 C`, and Z-axis expansion `1.0%` from `50 C to 260 C`.
- The same sheet lists thermal stress solder float at `288 C` as `>60 sec`, T260 `>60 min`, T288 `>60 min`, and T300 `>60 min`.
- At `RC70%`, the sheet lists permittivity `3.59` at `10 GHz` by `SPC method`.
- The sheet separately lists `impedance simulation DK` as `3.10`.
- At `RC70%`, the sheet lists loss tangent `0.0036` at `10 GHz` by `SPC method`.
- The same sheet lists volume resistivity `>10^10 MOhm-cm`, surface resistivity `>10^8 MOhm`, electric strength `>40 kV/mm`, dielectric breakdown voltage `>50 kV`, and peel strength `4 lb/in` for `1 oz RTF Cu foil`.
- The sheet lists thickness availability from `0.0012 in / 0.03 mm` to `0.062 in / 1.58 mm`, copper foil cladding from `1/3 oz` to `3 oz`, and glass styles including `1017`, `1027`, `1037`, `1067`, `1078`, `3313`, and `2116`.

## Conditions And Methods

- Preserve `RC70%`, `10 GHz`, and `SPC method` on Dk / Df values.
- Keep `impedance simulation DK` separate from measured Dk rows.
- Treat all values as information-only / typical, matching the source note.
- Treat availability and QPL wording as TUC product-page context, not supplier build approval or finished-board qualification.

## Limits And Non-Claims

- This card does not prove substrate, HDI, ELIC, aerospace, military, RF, or harsh-environment finished-board performance.
- It does not prove board-level insertion loss, signal integrity, CAF lifetime, stackup reliability, qualification, or supplier build success.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.tuc.com.tw/zh-tw/products-detail/id/40
