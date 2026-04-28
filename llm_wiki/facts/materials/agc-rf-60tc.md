---
fact_id: "materials-agc-rf-60tc"
title: "AGC RF-60TC baseline material card"
topic: "RF-60TC"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-rf-60tc-datasheet"]
tags: ["agc", "rf-60tc", "ptfe", "ceramic-filled", "high-dk", "thermal", "power-rf", "rf-materials"]
---

# Canonical Summary

> RF-60TC is an AGC PTFE-based, ceramic-filled fiberglass substrate positioned for high-power RF and microwave designs where a `6.15` Dk class, low loss, thermal conductivity, low Z-axis CTE, and dimensional stability need to be balanced.

## Stable Facts

- AGC describes RF-60TC as a PTFE based, ceramic filled fiberglass substrate for high power RF and microwave applications.
- The TDS lists applications including high-power amplifiers, miniaturized antennas, GPS / patch / RFID reader antennas, filters, couplers, dividers, and satellites.
- The TDS lists `Dk 6.15 +/- 0.15 at 10 GHz` by `IPC-650 2.5.5.5.1 (Modified)`.
- The same TDS lists `Df 0.0020 at 10 GHz` by the same modified IPC method.
- The same TDS lists thermal conductivity values of `0.90 W/mK` unclad, `1.00 W/mK` for `CH/CH`, and `1.05 W/mK` for `C1/C1`.
- The same TDS lists CTE values from `RT to 150 C` of `X 9.9 ppm/C`, `Y 9.9 ppm/C`, and `Z 40 ppm/C`.
- The same TDS lists `TCK -3.581 ppm/C`, `Td 500 C` at `2%` weight loss, and `Td 515 C` at `5%` weight loss.
- The same TDS lists moisture absorption `0.03%`, density `2.84 g/cm3`, specific heat `0.94 J/gK`, and flammability rating `V-0`.
- The same TDS lists typical thicknesses from `0.0050 in / 0.13 mm` through `0.0600 in / 1.52 mm`, with manufacturing increments of `0.005 in / 0.125 mm`.

## Conditions And Methods

- Keep `10 GHz` attached to the Dk and Df values.
- Keep thermal-conductivity construction labels separate; do not collapse unclad and copper-clad values into one number.
- Treat the values as typical datasheet values, not guaranteed specification limits.

## Limits And Non-Claims

- This card does not prove any finished-board antenna gain, amplifier lifetime, satellite qualification, or high-power operating temperature.
- It does not prove APT, HIL, or any other supplier can fabricate RF-60TC boards to a specific stackup, tolerance, lead time, or yield.
- Heavy metal backed laminate availability should be checked with AGC or a dated sourcing record before reuse in a customer-specific claim.

## Open Questions

- Whether to add an `RF-60TC vs RF-10 vs TMM 10i` high-Dk / compact RF selector card.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_RF-60TC_TDS.pdf
