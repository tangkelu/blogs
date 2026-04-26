---
fact_id: "materials-agc-rf-10"
title: "AGC RF-10 baseline material card"
topic: "RF-10"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids: ["agc-rf-10-product-page", "agc-rf-10-datasheet", "agc-rf-microwave-laminates-page"]
tags: ["agc", "rf-10", "high-dk", "ptfe", "rf-materials", "miniaturization"]
---

# Canonical Summary

> RF-10 is an AGC ceramic-filled PTFE and woven-fiberglass laminate positioned for compact RF structures where high dielectric constant, decent thermal conductivity, and dimensional stability matter more than minimizing Dk.

## Stable Facts

- AGC describes RF-10 as a ceramic-filled PTFE and woven-fiberglass laminate.
- The official product page positions RF-10 as a `low loss, high DK material`.
- The official TDS lists `Dk 10.2 +/- 0.3 at 10 GHz` and `Df 0.0025 at 10 GHz` by `IPC-650 2.5.5.5.1 Mod.`
- The same TDS lists thermal conductivity `0.85 W/mK`, X/Y/Z CTE values of `16 / 20 / 25 ppm/C`, `TcK -370 ppm/C`, moisture absorption `0.08%`, and flammability `V-0`.
- AGC states RF-10 can be sheared, drilled, milled, and plated using standard PTFE circuit-board processing techniques.
- The product page frames RF-10 around `microstrip patch antennas`, `GPS antennas`, `filters`, `couplers`, `power dividers`, `aircraft collision avoidance systems`, and `satellite components`.
- The AGC lineup page lists RF-10 under `IPC-4103A/280`.

## Conditions And Methods

- Keep the `10 GHz` Dk/Df values attached to the modified IPC method.
- Keep the high-Dk compactness framing separate from any claim of lowest insertion loss.
- Treat RF-10 as a PTFE-process material, not as a process-friendly hydrocarbon default.

## Limits And Non-Claims

- This card does not claim RF-10 is lower loss than RO3003 or RT/duroid 5880.
- It does not remove the need for tolerance and temperature-drift review in compact filters or antennas.

## Open Questions

- Whether to add an `RF-10 vs RO3010 vs VTM1000i` high-Dk selector card

## Source Links

- https://www.agc-multimaterial.com/solutions/rf-10/
- https://www.agc-multimaterial.com/agc-downloads/AGC_RF-10_TDS.pdf
- https://www.agc-multimaterial.com/rfmicrowave-laminates/
