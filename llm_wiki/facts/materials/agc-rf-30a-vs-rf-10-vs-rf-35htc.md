---
fact_id: "materials-agc-rf-30a-vs-rf-10-vs-rf-35htc"
title: "AGC RF-30A vs RF-10 vs RF-35HTC comparison card"
topic: "AGC RF-30A vs RF-10 vs RF-35HTC"
category: "materials"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "agc-rf-30a-product-page"
  - "agc-rf-30a-datasheet"
  - "agc-rf-10-product-page"
  - "agc-rf-10-datasheet"
  - "agc-rf-35htc-product-page"
  - "agc-rf-35htc-datasheet"
  - "agc-rf-microwave-laminates-page"
tags: ["agc", "comparison", "rf-30a", "rf-10", "rf-35htc", "rf-materials"]
---

# Canonical Summary

> Within the current AGC RF set, RF-30A reads as the commercial-volume antenna and PIM-aware option, RF-10 reads as the compact high-Dk option, and RF-35HTC reads as the power-RF thermal-performance option.

## Stable Facts

- RF-30A lists `Dk 2.97 +/- 0.05 at 1.9 GHz`, while RF-10 lists `Dk 10.2 +/- 0.3 at 10 GHz`, and RF-35HTC lists `Dk 3.50 +/- 0.05 at 10 GHz`.
- RF-30A lists `Df 0.0020 at 10 GHz`, RF-10 lists `Df 0.0025 at 10 GHz`, and RF-35HTC lists `Df 0.0007 at 10 GHz`.
- RF-30A lists thermal conductivity `0.42 W/mK`, RF-10 lists `0.85 W/mK`, and RF-35HTC lists `1.84 W/mK` unclad.
- AGC frames RF-30A around `antenna`, `RF passive components`, and `PA`, RF-10 around `GPS antennas`, `filters`, `couplers`, and `satellite components`, and RF-35HTC around `high power` filters, couplers, dividers, and power amplifiers.
- The AGC lineup page maps the three materials to different IPC slash-sheet references: `4103A/230`, `4103A/280`, and `4103A/240`.

## Conditions And Methods

- This comparison uses current public AGC product pages and TDS files.
- RF-30A uses `1.9 GHz` as its published Dk anchor while RF-10 and RF-35HTC use `10 GHz`, so the comparison should be used as a product-selection guide rather than a perfectly normalized benchmark.

## Limits And Non-Claims

- This card does not prove one AGC material is globally superior.
- It does not cover copper choice, process yield, or fabricator-specific handling differences.

## Open Questions

- Whether to add `NF-30` later for mmWave-oriented AGC coverage

## Source Links

- https://www.agc-multimaterial.com/solutions/rf-30a/
- https://www.agc-multimaterial.com/agc-downloads/AGC_RF-30A_TDS.pdf
- https://www.agc-multimaterial.com/solutions/rf-10/
- https://www.agc-multimaterial.com/agc-downloads/AGC_RF-10_TDS.pdf
- https://www.agc-multimaterial.com/solutions/rf-35htc/
- https://www.agc-multimaterial.com/agc-downloads/AGC_RF-35HTC_TDS.pdf
- https://www.agc-multimaterial.com/rfmicrowave-laminates/
