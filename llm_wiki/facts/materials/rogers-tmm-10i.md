---
fact_id: "materials-rogers-tmm-10i"
title: "Rogers TMM 10i member material card"
topic: "TMM 10i"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-25"
source_ids: ["rogers-tmm-family-datasheet"]
tags: ["rogers", "tmm", "tmm-10i", "thermoset", "microwave", "materials"]
---

# Canonical Summary

> `TMM 10i` is the Rogers TMM family member with datasheet-backed electrical, thermal, moisture, and mechanical values that must stay tied to the official family table conditions.

## Stable Facts

- The Rogers TMM family datasheet explicitly includes `TMM 10i` as a named family member.
- `Dielectric constant (process)` is `9.80 ± 0.245` at `10 GHz` by `IPC-TM-650 2.5.5.5`.
- `Dielectric constant (design)` is `9.9` across `8-40 GHz` by the differential phase length method.
- `Dissipation factor` is `0.0020` at `10 GHz` by `IPC-TM-650 2.5.5.5`.
- `Thermal coefficient of dielectric constant` is `-43 ppm/°K` from `-55 to +125°C` and is marked as an estimated value in the datasheet.
- `CTE-x` is `19 ppm/K`, `CTE-y` is `19 ppm/K`, and `CTE-z` is `20 ppm/K` from `0 to 140°C` by `ASTM E831 / IPC-TM-650 2.4.41`.
- `Thermal conductivity` is `0.76 W/m/K` at `80°C` by `ASTM C518`.
- `Moisture absorption` is `0.16%` at `1.27 mm (0.050")` and `0.13%` at `3.18 mm (0.125")` by `ASTM D570`.
- `Specific gravity` is `2.77` by `ASTM D792`.
- `Flexural modulus` is `1.80 Mpsi` by `ASTM D790`.
- `Electrical strength` is `267 V/mil` by `IPC-TM-650 2.5.6.2`.
- `Copper peel strength` after thermal stress is `5.0 lb/in (0.9 N/mm)` with `1 oz EDC` by `IPC-TM-650 2.4.8`.
- `Decomposition temperature` is `425°C` by `TGA` and `ASTM D3850`.
- `Specific heat capacity` is `0.72 J/g/K` and is marked as a calculated value in the datasheet.
- `Lead-free process compatible` is listed as `YES`.

## Conditions And Methods

- Keep every value tied to its stated test condition and method.
- Keep member-level values separate from family-level TMM prose.
- Treat the card as a member-level datasheet summary, not as a cross-family selector.

## Limits And Non-Claims

- This card does not claim cross-family superiority versus PTFE, ceramic, or AGC materials.
- It does not add tensile modulus because the current official family datasheet does not list one for `TMM 10i`.
- It does not turn flexural modulus into tensile modulus.
- It does not treat family-level TMM wording as a `TMM 10i`-exclusive claim.

## Source Links

- https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/tmm-thermoset-laminate-data-sheet-tmm3----tmm4----tmm6----tmm10----tmm10i----tmm13i.pdf
