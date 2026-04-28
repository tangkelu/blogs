---
fact_id: "materials-ventec-vt-6735"
title: "Ventec VT-6735 high-thermal-conductivity RF laminate material card"
topic: "VT-6735"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["ventec-vt-6735-datasheet"]
tags: ["ventec", "vt-6735", "tec-speed-30", "rf-materials", "microwave", "high-thermal-conductivity", "laminate"]
---

# Canonical Summary

> VT-6735 is a Ventec tec-speed 30.0 laminate positioned for high-power RF and microwave amplifier, coupler, filter, and divider material contexts. Its preliminary typical values do not prove finished-board RF performance.

## Stable Facts

- Ventec identifies VT-6735 as `tec-speed 30.0` laminate with UL approval `E214381`, version `Prelim 1`.
- Ventec frames VT-6735 around high-power RF and microwave amplifiers, power amplifiers, couplers, filters, and power dividers.
- The datasheet lists Dk `3.50 +/- 0.05` at `10 GHz` by `IPC-TM-650 2.5.5.5` clamped stripline.
- The same sheet lists design Dk `3.6` from `8~40 GHz` by differential phase method.
- The same sheet lists Df `0.0015` at `10 GHz` by `IPC-TM-650 2.5.5.5`.
- The same sheet lists thermal coefficient of Dk `-65` from `-50 C to 150 C` by `IPC-TM-650 2.5.5.5`.
- The same sheet lists volume resistivity `8 x 10^7 MOhm-cm`, surface resistivity `9 x 10^7 MOhm`, Td `520 C`, thermal conductivity `1.15 W/mK`, X/Y CTE `21 / 21 ppm/C`, and Z-axis CTE `40 ppm/C`.
- The same sheet lists specific heat `0.92 J/g/K`, peel strength after thermal stress `8.0 lb/in / 1.40 N/mm`, density `2.2 gm/m3`, moisture absorption `0.06%`, flammability `V-0`, and lead-free process compatibility `YES`.
- The sheet lists standard laminate thicknesses `0.010 in`, `0.020 in`, `0.030 in`, and `0.060 in`, plus standard panel sizes `12 in x 18 in` and `24 in x 18 in`.

## Conditions And Methods

- Keep `10 GHz` clamped-stripline Dk / Df values separate from `8~40 GHz` design Dk.
- Treat the sheet's values as preliminary typical values, matching the datasheet note.
- Treat thickness and panel-size rows as Ventec product availability context, not supplier stock or build-capability proof.

## Limits And Non-Claims

- This card does not prove amplifier output power, RF efficiency, insertion loss, thermal performance, antenna performance, or finished-board RF qualification.
- It does not prove metal-base availability, stackup manufacturability, or lead-free assembly success for a specific supplier or project.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.ventec-group.com/media/114485/230622-tec-speed30-vt-6735.pdf
