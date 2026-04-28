---
fact_id: "materials-shengyi-aerowave-300"
title: "Shengyi AeroWave 300 exact-product material card"
topic: "AeroWave 300"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids:
  - "shengyi-aerowave-300-datasheet"
tags: ["shengyi", "aerowave-300", "rf-materials", "microwave", "low-loss", "materials"]
---

# Canonical Summary

> `AeroWave 300` is an exact-product Shengyi RF / microwave material row. Its datasheet values may be used as source-scoped material parameters, not as finished antenna, base-station, PIM, insertion-loss, or supplier-capability claims.

## Stable Facts

- Shengyi Technology USA publishes an official `AeroWave 300` technical datasheet from its RF and Microwave page.
- Shengyi positions `AeroWave 300` as a high-frequency, low-loss material for RF PCB use.
- The table lists process Dk `3.0 +/- 0.05` in the Z direction at `10 GHz / 23 C` by `IPC-TM-650 2.5.5.5 Clamped Stripline`.
- The table lists design Dk `2.98` in the Z direction at `1.5 GHz - 6 GHz / 23 C` by differential phase length method.
- The table lists Df `0.0031` in the Z direction at `10 GHz / 23 C` by `IPC-TM-650 2.5.5.5 Clamped Stripline`.
- The table lists thermal coefficient of Dk value `50` in the Z direction over `-40~+120 C` by `IEC 61189-2-721 (10GHz)`; the source table does not show a unit in the unit column.
- The table lists Tg `200 C` by DMA under `IPC-TM-650 2.4.24.4`, and Td `400 C` by TGA under `ASTM D3850`.
- The table lists CTE `15 / 15 / 50 ppm/C` for X/Y/Z by TMA under `IPC-TM-650 2.4.41`.
- The table lists volume resistivity `2.21 x 10^8 MOhm-cm` and surface resistivity `6.84 x 10^7 MOhm` under `IPC-TM-650 2.5.17.1`, condition `A`.
- The table lists peel strength `0.85 N/mm` after solder float with `1 oz. HVLP foil`, electrical strength `60 kV/mm` at `0.508 mm (0.020")`, flexural strength `232 / 216 MPa` in LW/CW, water absorption `0.15%`, thermal conductivity `0.46 W/m.K` at `100 C`, and flammability `V-0`.
- The product-specification table lists standard thicknesses `0.005"`, `0.010"`, `0.020"`, `0.030"`, and `0.060"` and standard panel sizes `36" x 48"`, `40" x 48"`, and `42" x 48"` with additional panel sizes available upon request.
- The datasheet states that typical values are reference values and are not intended as specifications.

## Conditions And Methods

- Keep process Dk separate from design Dk because the conditions and methods differ.
- Preserve the Df frequency and clamped-stripline method whenever using the `0.0031` value.
- Treat product thickness, panel-size, and copper-foil notes as manufacturer catalog context, not as proof of distributor stock or fabricator availability.

## Limits And Non-Claims

- This card does not prove finished-board PIM, antenna efficiency, insertion loss, base-station qualification, power-amplifier performance, radar performance, or RF compliance.
- It does not prove APT, HIL, or any other supplier's stock, process capability, certification, procurement approval, price, MOQ, lead time, or yield.
- It does not make `AeroWave 300` interchangeable with Shengyi `mmWaveG`, `LNB33C`, `S1170G`, `S1150G`, or generic FR-4 materials.

## Source Links

- https://www.shengyi-usa.com/download/28748/
