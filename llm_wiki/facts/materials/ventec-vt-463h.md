---
fact_id: "materials-ventec-vt-463h"
title: "Ventec VT-463H halogen-free ultra-low-loss material card"
topic: "VT-463H"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["ventec-vt-463h-datasheet-page"]
tags: ["ventec", "vt-463h", "tec-speed-7h", "halogen-free", "high-tg", "ultra-low-loss", "laminate", "prepreg"]
---

# Canonical Summary

> VT-463H is a Ventec tec-speed 7.0H halogen-free high-Tg laminate / prepreg positioned for very-low-Dk and ultra-low-loss signal-integrity contexts. Its values must remain method, frequency, and resin-content scoped.

## Stable Facts

- Ventec identifies VT-463H as `tec-speed 7.0H` laminate / prepreg with UL approval `E214381`, version `Preliminary 1`.
- Ventec frames VT-463H around high-speed network equipment, IC tester, and high-frequency measuring instruments / devices.
- The sheet lists Tg `220 C` by DMA / `IPC-TM-650 2.4.24.4` and Tg `175 C` by TMA / `IPC-TM-650 2.4.24`.
- The same sheet lists Td `430 C` by `ASTM D3850`, T288 `>120 min`, thermal stress at `288 C` as `>600 s`, and total expansion from `50 C to 260 C` as `2.2%`.
- The same sheet lists Z-axis CTE before Tg `45 ppm/C` and after Tg `200 ppm/C`.
- The same sheet lists Dk at `RC 55%` of `3.7 at 1 GHz` by `IPC-TM-650 2.5.5.9` and `3.6 at 10 GHz` by cavity resonator.
- The same sheet lists Df at `RC 55%` of `0.0018 at 1 GHz` by `IPC-TM-650 2.5.5.9` and `0.0028 at 10 GHz` by cavity resonator.
- The same sheet lists moisture absorption `0.10%`, CTI `Grade 3 (175~250)`, arc resistance `195 s`, and flammability `V-0`.
- The sheet lists core thickness availability from `0.002 in / 0.05 mm` to `0.030 in / 0.762 mm`, copper foil availability from `1/3 oz` to `3 oz`, and prepregs in roll or panel form.

## Conditions And Methods

- Keep `1 GHz` IPC rows separate from `10 GHz` cavity-resonator rows.
- Preserve `RC 55%` on Dk / Df values.
- Treat availability ranges as Ventec product availability context, not a supplier stock or build-capability claim.
- Treat all data as typical values, matching the source note.

## Limits And Non-Claims

- This card does not prove high-speed network, IC tester, or high-frequency instrument finished-board performance.
- It does not prove insertion loss, impedance tolerance, channel budget, protocol compliance, or supplier build success.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.ventec-group.com/products/tec-speed-signal-integrity/tec-speed-70h-vt-463h/datasheet/
