---
fact_id: "materials-ventec-vt-4b7"
title: "Ventec VT-4B7 IMS baseline material card"
topic: "VT-4B7"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-25"
source_ids: ["ventec-vt-4b7-datasheet"]
tags: ["ventec", "vt-4b7", "ims", "mcpcb", "thermal-management", "exact-product", "materials"]
---

# Canonical Summary

> `VT-4B7` is an official Ventec exact-product IMS material with product-level dielectric and thermal constants that are usable for `llm_wiki` as an MCPCB / IMS material anchor when kept at the material-property layer.

## Stable Facts

- Ventec publishes an official `VT-4B7 Metal Base Laminate` datasheet page.
- The datasheet page identifies `VT-4B7` as a `tec-thermal / Thermal Management & IMS` metal-base laminate.
- The general-information block states `thermal conductivity 7.0 W/mK`.
- The general-information block states `ceramic filled`.
- The general-information block states `halogen free`.
- The general-information block states `flammability UL94 V-0`.
- The general-information block states `MOT 130 C`.
- The laminate-properties table provides dielectric-thickness columns for `75 um`, `100 um`, and `150 um`.
- `Thermal conductivity` is `7.0 W/m.K` by `ISO 22007-2`.
- `Thermal impedance` is `0.017`, `0.022`, and `0.034 C*in2/W` for `75 um`, `100 um`, and `150 um` dielectric thicknesses by `ISO 22007-2`.
- `Tg` is `100 C` by `DSC` and `145 C` by `DMA`.
- `Td` is `380 C` by `TGA` and `ASTM D3850`.
- `Thermal stress` is `>=5 min` by `Solder Dip @ 288 C` and `IPC-TM-650 2.4.13.1`.
- `Hi-Pot withstand` is `>600 V` by `DC` and `IPC-TM-650 2.5.7.2`.
- `Breakdown voltage` is `7000 V`, `8000 V`, and `10000 V` for `75 um`, `100 um`, and `150 um` dielectric thicknesses by `AC` and `IPC-TM-650 2.5.6.3`.
- `Dk` is `4.8` at `1 MHz` under `C-24/23/50` by `IPC-TM-650 2.5.5.3`.
- `Df` is `0.016` at `1 MHz` under `C-24/23/50` by `IPC-TM-650 2.5.5.3`.
- `Volume resistance` is `5.0E+8 MOhm-cm` after moisture and `3.0E+7 MOhm-cm` under `E-24/125` by `IPC-TM-650 2.5.17.1`.
- `Surface resistance` is `2.0E+7 MOhm` after moisture and `5.0E+6 MOhm` under `E-24/125` by `IPC-TM-650 2.5.17.1`.
- `Peel strength (1 oz)` is `4.5 lb/in` as received by `IPC-TM-650 2.4.8`.
- `CTI` is `600 V` as received by `ASTM D3638`.
- `RTI` is `130 C` for both electric and mechanical by `UL 746E`.

## Conditions And Methods

- Keep all values tied to the official `VT-4B7` datasheet page and its stated thickness, method, and unit.
- Use this card for IMS / MCPCB material selection language, not for finished-board thermal-performance guarantees.
- Treat published values as datasheet values for the material system, not as guaranteed junction-temperature results in a specific board or LED module.
- Treat all listed values as typical values because Ventec explicitly says the table is not intended to be specification values.

## Limits And Non-Claims

- This card does not prove board-level heat-spread outcome, LED lifetime, junction-temperature reduction, or thermal-resistance performance in a final assembly.
- It does not turn dielectric-thickness options into a universal MCPCB stack rule.
- It does not prove copper weight, base-metal selection, assembly endurance, or certification status beyond the cited page.
- It does not turn metal-plate options such as aluminum and copper into a default stack prescription.
- It does not replace thermal simulation, reflow validation, or application-specific qualification.

## Source Links

- https://www.ventec-group.com/products/tec-thermal-thermal-management-ims/vt-4b7/datasheet/
