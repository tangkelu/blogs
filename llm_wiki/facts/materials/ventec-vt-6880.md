---
fact_id: "materials-ventec-vt-6880"
title: "Ventec VT-6880 baseline material card"
topic: "VT-6880"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["ventec-vt-6880-datasheet"]
tags: ["ventec", "vt-6880", "tec-speed-30", "ptfe", "mmwave", "radar", "rf-materials"]
---

# Canonical Summary

> VT-6880 is a Ventec tec-speed 30.0 non-woven-glass-reinforced PTFE high-frequency laminate positioned for extremely-low-loss RF and mmWave contexts, including radar applications, but its preliminary typical values must stay separate from finished-board radar performance.

## Stable Facts

- Ventec identifies VT-6880 as `tec-speed 30.0` high-frequency laminate with UL approval `E214381`, version `A1`.
- The datasheet frames VT-6880 around military / defense radar, airborne radar, mmWave radar, and radio-frequency applications.
- The datasheet lists Dk `2.20 +/- 0.02` at `10 GHz` by `IPC-TM-650 2.5.5.5`.
- The same sheet lists design Dk `2.20` from `8~40 GHz` by differential phase method.
- The same sheet lists Df `0.0009` at `10 GHz` by `IPC-TM-650 2.5.5.5`.
- The same sheet lists thermal coefficient of Dk `-140 ppm/C` from `-50 C to 150 C`.
- The same sheet lists Td `500 C` at `5%` weight loss, thermal conductivity `0.20 W/mK`, X/Y CTE `40 / 40 ppm/C` from `0 C to 100 C`, Z-axis CTE `75 ppm/C` from `0 C to 100 C`, and thermal stress at `288 C` as `>300 s`.
- The same sheet lists peel strength `3.51 N/mm`, tensile modulus `900 / 800 MPa`, density `2.1 g/cm3`, moisture absorption `0.02%`, flammability `V-0`, and lead-free process compatibility `YES`.
- The sheet lists dielectric thickness availability at `0.010 in`, `0.020 in`, and `0.030 in`, plus Hoz / 1 oz copper options and aluminum / copper metal-base options.
- The sheet lists `IPC-4103 /210`.

## Conditions And Methods

- Keep `10 GHz` IPC Dk/Df values separate from `8~40 GHz` design Dk.
- Treat the sheet's values as preliminary typical values, matching the datasheet note.
- Treat radar application wording as material-positioning context only.

## Limits And Non-Claims

- This card does not prove mmWave radar range, airborne radar qualification, defense qualification, insertion loss, antenna efficiency, or finished-board RF performance.
- It does not prove metal-base availability for a specific supplier or project without a dated sourcing / capability record.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.ventec-group.com/media/114454/230601-tec-speed30-vt-6880.pdf
