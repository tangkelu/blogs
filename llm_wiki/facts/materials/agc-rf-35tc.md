---
fact_id: "materials-agc-rf-35tc"
title: "AGC RF-35TC baseline material card"
topic: "RF-35TC"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-rf-35tc-datasheet"]
tags: ["agc", "rf-35tc", "ptfe", "ceramic-filled", "thermal", "power-rf", "rf-materials", "low-loss"]
---

# Canonical Summary

> RF-35TC is an AGC PTFE-based, ceramic-filled fiberglass substrate positioned for power RF work where low dielectric loss and thermal conductivity matter, but it must remain distinct from AGC RF-35HTC and from finished-board power-handling claims.

## Stable Facts

- AGC describes RF-35TC as a PTFE based, ceramic filled fiberglass substrate.
- The TDS frames RF-35TC for filters, couplers, power amplifiers, antennas, and satellites.
- The TDS lists `Dk 3.5 +/- 0.05 at 10 GHz` by `IPC-650 2.5.5.5.1 (Modified)`.
- The same TDS lists `Df 0.002 at 10 GHz` by the same modified IPC method.
- The same TDS lists thermal conductivity at `125 C` of `0.60 W/mK` unclad, `0.92 W/mK` for `C1/C1`, and `0.87 W/mK` for `CH/CH`.
- The same TDS lists CTE values from `23 C to 125 C` of `X 11 ppm/C`, `Y 13 ppm/C`, and `Z 34 ppm/C`.
- The same TDS lists `Td 420 C` at `2%` weight loss and `Td 436 C` at `5%` weight loss.
- The same TDS lists peel strength `1.25 N/mm` for `1/2 oz CVH`, moisture absorption `0.05%`, density `2.35 g/cm3`, dielectric breakdown `56.7 kV`, arc resistance `304 seconds`, and flammability `V-0`.
- The same TDS lists typical thicknesses from `0.0050 in / 0.13 mm` through `0.0600 in / 1.52 mm`, with manufacturing increments of `0.005 in / 0.125 mm`.

## Conditions And Methods

- Keep `10 GHz` attached to the Dk and Df values.
- Keep thermal-conductivity values tied to `125 C` and separated by construction.
- Treat AGC's comparative thermal images and high-power framing as manufacturer demonstration context, not a board-level power rating.
- Treat the values as typical datasheet values, not guaranteed specification limits.

## Limits And Non-Claims

- This card does not claim RF-35TC is interchangeable with RF-35HTC or generic RF-35.
- It does not prove finished-board amplifier power, antenna efficiency, satellite readiness, or thermal margin.
- It does not prove APT, HIL, or any other supplier capability, yield, lead time, or qualification status.

## Open Questions

- Whether to add an `RF-35TC vs RF-35HTC` selector that separates reinforced and non-reinforced high-thermal-conductivity AGC options.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_RF-35TC_TDS.pdf
