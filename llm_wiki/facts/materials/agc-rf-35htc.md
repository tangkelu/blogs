---
fact_id: "materials-agc-rf-35htc"
title: "AGC RF-35HTC baseline material card"
topic: "RF-35HTC"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids: ["agc-rf-35htc-product-page", "agc-rf-35htc-datasheet", "agc-rf-microwave-laminates-page"]
tags: ["agc", "rf-35htc", "thermal", "power-rf", "rf-materials", "low-loss"]
---

# Canonical Summary

> RF-35HTC is an AGC non-reinforced ceramic/PTFE laminate positioned for high-power RF work where very low loss and unusually high thermal conductivity need to coexist in one microwave substrate.

## Stable Facts

- AGC describes RF-35HTC as a non-reinforced, low-loss, high-thermal-conductivity laminate with very low PTFE content.
- The official product page lists `Dk 3.5 +/- 0.05` and `Df 0.0007`.
- The official TDS lists `Dk 3.50 +/- 0.05 at 10 GHz` and `Df 0.0007 at 10 GHz` by `IPC-650 2.5.36`.
- The same TDS lists unclad thermal conductivity `1.84 W/mK` and clad thermal conductivity `2.89 W/mK`.
- The same TDS lists X/Y/Z CTE values of `11 / 14 / 77 ppm/C` from `23 C to 125 C`, moisture absorption `0.07%`, dielectric breakdown `42 kV`, and arc resistance `> 400 seconds`.
- AGC states the low PTFE content facilitates plating and drilling and that RF-35HTC is compatible with AGC `1 oz` coppers, with `ULP 1 oz` recommended at high frequencies for lowest insertion loss.
- AGC frames RF-35HTC around `filters`, `couplers`, `dividers`, `power amplifiers`, `antennas`, and `satellites`.
- The AGC lineup page lists RF-35HTC under `IPC-4103A/240`.

## Conditions And Methods

- Keep the `10 GHz` Dk/Df values attached to `IPC-650 2.5.36`.
- Keep thermal-conductivity values marked as `unclad` versus `clad`.
- Treat AGC power-handling comparisons as manufacturer evidence, not as a universal ranking proof.

## Limits And Non-Claims

- This card does not prove RF-35HTC is the best material for every power amplifier or satellite build.
- It also does not remove the need to evaluate copper profile, surface finish, and structure-level thermal design.

## Open Questions

- Whether to add an `RF-35HTC vs TMM 10i vs RF-35TC` power-RF selector card

## Source Links

- https://www.agc-multimaterial.com/solutions/rf-35htc/
- https://www.agc-multimaterial.com/agc-downloads/AGC_RF-35HTC_TDS.pdf
- https://www.agc-multimaterial.com/rfmicrowave-laminates/
