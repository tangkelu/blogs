---
fact_id: "materials-ventec-vt-462s"
title: "Ventec VT-462S very-low-Dk / very-low-loss material card"
topic: "VT-462S"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["ventec-vt-462s-datasheet-page"]
tags: ["ventec", "vt-462s", "tec-speed-6", "very-low-dk", "very-low-loss", "high-tg", "laminate", "prepreg"]
---

# Canonical Summary

> VT-462S is a Ventec tec-speed 6.0 laminate / prepreg positioned as a very-low-Dk and very-low-loss material for high-speed and high-frequency equipment contexts. Its Dk / Df values must remain resin-content and frequency scoped.

## Stable Facts

- Ventec identifies VT-462S as `tec-speed 6.0` laminate / prepreg with UL approval `E214381`, version `23/10/2024`, IPC-4101E `/91 /102`.
- Ventec frames VT-462S around high-speed networking equipment, IC testers, and high-frequency measuring instruments / devices.
- The sheet lists Tg `210 C` by DMA / `IPC-TM-650 2.4.24.4` and Tg `170 C` by TMA / `IPC-TM-650 2.4.24`.
- The same sheet lists Td `400 C` by `ASTM D3850`, T260 `>60 min`, T288 `>30 min`, and thermal stress at `288 C` as `>600 s`.
- The same sheet lists Z-axis CTE before Tg `48 ppm/C`, after Tg `260 ppm/C`, total expansion from `50 C to 260 C` as `2.8%`, X-Y CTE `11~13 ppm/C`, and MOT `130 C`.
- At `RC 50%`, the sheet lists Dk `3.6` at `1 GHz` by `IPC-TM-650 2.5.5.9` and Dk `3.5` at `10 GHz` by `IPC-TM-650 2.5.5.13`.
- At `RC 50%`, the sheet lists Df `0.003` at `1 GHz` by `IPC-TM-650 2.5.5.9` and Df `0.005` at `10 GHz` by `IPC-TM-650 2.5.5.13`.
- The same sheet lists moisture absorption `0.10%`, CTI `Grade 3 (175~250)`, arc resistance `124 s`, and flammability `V-0`.
- The sheet lists core thickness availability from `0.002 in / 0.05 mm` to `0.200 in / 5 mm`, copper foil availability from `1/3 oz` to `3 oz`, and E-glass styles including `2116`, `2113`, `1078`, and `106`.

## Conditions And Methods

- Preserve `RC 50%` on Dk / Df values.
- Keep `1 GHz` IPC-TM-650 `2.5.5.9` rows separate from `10 GHz` IPC-TM-650 `2.5.5.13` rows.
- Treat all data as typical values, matching the source note.
- Treat availability ranges as Ventec product availability context, not supplier stock or build-capability proof.

## Limits And Non-Claims

- This card does not prove high-speed network, IC tester, or high-frequency instrument finished-board performance.
- It does not prove insertion loss, impedance tolerance, channel budget, protocol compliance, or supplier build success.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.ventec-group.com/zh/products/tec-speed-signal-integrity/tec-speed-60-vt-462s/datasheet/
