---
fact_id: "materials-ventec-vt-4b5h"
title: "Ventec VT-4B5H IMS metal-base laminate material card"
topic: "VT-4B5H"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["ventec-vt-4b5h-datasheet-page"]
tags: ["ventec", "vt-4b5h", "ims", "metal-base-laminate", "thermal-management", "ceramic-filled", "halogen-free"]
---

# Canonical Summary

> VT-4B5H is a Ventec ceramic-filled, halogen-free IMS / metal-base laminate with `4.2 W/mK` dielectric thermal conductivity. Thickness-dependent rows must remain tied to dielectric thickness and test method.

## Stable Facts

- Ventec identifies VT-4B5H as a metal-base laminate with UL approval `E214381`, version `23/08/2023`.
- Ventec frames VT-4B5H around high beam / low beam, power conversion, power modules, motor drives and controllers, rectifiers, power supplies, and other high-temperature or high-voltage applications.
- The sheet lists thermal conductivity `4.2 W/mK` by `ISO22007-2`.
- The same sheet lists thermal impedance by `ISO22007-2` as `0.019`, `0.029`, `0.038`, `0.057`, and `0.076 C*in2/W` for dielectric thicknesses `50 um`, `75 um`, `100 um`, `150 um`, and `200 um`.
- The same sheet lists Tg `180 C` by DSC / IPC-TM-650 `2.4.25` and `210 C` by DMA / IPC-TM-650 `2.4.24.4`.
- The same sheet lists Td `400 C` by TGA / `ASTM D3850` and thermal stress solder dip at `288 C` as `>=5 min`.
- The same sheet lists Hi-Pot proof test `>600 V` DC by IPC-TM-650 `2.5.7.2`.
- The same sheet lists AC breakdown voltage by IPC-TM-650 `2.5.6.3` as `4000 V`, `7000 V`, `8000 V`, `10000 V`, and `12000 V` for dielectric thicknesses `50 um`, `75 um`, `100 um`, `150 um`, and `200 um`.
- The same sheet lists Dk `4.8` and Df `0.016` at `1 MHz`, condition `C-24 / 23 / 50`, by IPC-TM-650 `2.5.5.3`.
- The same sheet lists CTI `600 V`, flammability `V-0`, RTI electrical `155 C`, and RTI mechanical `155 C`.
- The sheet lists available dielectric thicknesses from `50 um` to `200 um`, copper foil weights from half-ounce to `6 oz`, aluminum and copper metal-plate options, and standard panel sizes.

## Conditions And Methods

- Keep thermal impedance and AC breakdown voltage tied to dielectric thickness.
- Keep Dk / Df tied to `1 MHz`, `C-24 / 23 / 50`, and IPC-TM-650 `2.5.5.3`.
- Treat metal-plate, copper weight, panel size, finish, and protective-film rows as Ventec product availability context only.
- Treat all data as typical values, matching the source note.

## Limits And Non-Claims

- This card does not prove finished-board thermal resistance, LED lifetime, junction temperature, power-module reliability, motor-drive qualification, or high-voltage safety compliance.
- It does not prove that a supplier stocks or can build every listed metal plate, thickness, copper, surface-finish, or protective-film option.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.ventec-group.com/products/tec-thermal-thermal-management-ims/vt-4b5h/datasheet/
