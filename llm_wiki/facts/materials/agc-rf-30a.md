---
fact_id: "materials-agc-rf-30a"
title: "AGC RF-30A baseline material card"
topic: "RF-30A"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids: ["agc-rf-30a-product-page", "agc-rf-30a-datasheet", "agc-rf-microwave-laminates-page"]
tags: ["agc", "rf-30a", "antenna", "ptfe", "rf-materials", "pim"]
---

# Canonical Summary

> RF-30A is an AGC woven-glass reinforced organic-ceramic RF laminate positioned for high-volume commercial microwave and antenna builds where stable PIM behavior, PTH reliability, and cost-performance matter more than chasing the very lowest loss available from softer ultra-low-loss systems.

## Stable Facts

- AGC describes RF-30A as an organic-ceramic laminate based on woven glass reinforcement.
- The official product page positions RF-30A as a `high volume antenna material`.
- The official TDS lists `Dk 2.97 +/- 0.05 at 1.9 GHz` by `IPC-TM 650 2.5.5.5.1 mod`.
- The same TDS lists `Df 0.0013 at 1.9 GHz` and `Df 0.0020 at 10 GHz` by the same modified IPC method.
- The same TDS lists thermal conductivity `0.42 W/mK`, X/Y/Z CTE values of `8 / 11 / 60 ppm/C` from `50 C to 150 C`, and flammability `V-0`.
- AGC states RF-30A was optimized for lower Z-axis CTE for improved PTH reliability and easier multilayer fabrication.
- The TDS states RF-30A exceeded `-153 dBc` PIM requirements in the specified PCB test conditions, and the front-page framing cites PIM values measured lower than `-160 dBc` on a coupon setup.
- The AGC lineup page lists RF-30A under `IPC-4103A/230`.

## Conditions And Methods

- Keep the `1.9 GHz` and `10 GHz` values separate.
- Keep the PIM statements tied to the stated coupon and power conditions.
- Treat RF-30A as a reinforced PTFE-family RF material, not as an FR-4-process substitute.

## Limits And Non-Claims

- This card does not claim RF-30A is the universal best antenna material.
- It does not prove finished-board PIM performance without considering design, connectors, soldering, and PCB processing.

## Open Questions

- Whether to add an `RF-30A vs VT-870 vs RO4350B` commercial antenna selector card

## Source Links

- https://www.agc-multimaterial.com/solutions/rf-30a/
- https://www.agc-multimaterial.com/agc-downloads/AGC_RF-30A_TDS.pdf
- https://www.agc-multimaterial.com/rfmicrowave-laminates/
