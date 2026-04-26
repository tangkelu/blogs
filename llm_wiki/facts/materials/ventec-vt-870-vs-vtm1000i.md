---
fact_id: "materials-ventec-vt-870-vs-vtm1000i"
title: "Ventec VT-870 vs VTM1000i comparison card"
topic: "VT-870 vs VTM1000i"
category: "materials"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids: ["ventec-vt-870-datasheet", "ventec-vtm1000i-datasheet", "ventec-tec-speed-rf-family-page"]
tags: ["ventec", "comparison", "vt-870", "vtm1000i", "rf-materials"]
---

# Canonical Summary

> Inside the current Ventec RF cards, VT-870 reads as the moderate-Dk hydrocarbon option for antenna and radar-style RF builds, while VTM1000i reads as the much higher-Dk compactness-oriented option for filters, couplers, and other structures where electrical size reduction matters.

## Stable Facts

- VT-870 lists `Dk 3.48 +/- 0.05 at 10 GHz`, while VTM1000i lists `Dk 9.8 +/- 0.245 at 10 GHz`.
- VT-870 lists `Df 0.0037 at 10 GHz`, while VTM1000i lists `Df 0.0023 at 10 GHz`.
- VT-870 lists thermal conductivity `0.69 W/mK`, while VTM1000i lists `1.00 W/mK`.
- VT-870 lists `Td 392 C`, while VTM1000i lists `Td 426 C`.
- Ventec frames VT-870 around `cellular base station antenna`, `power amplifiers`, `automotive radar`, and `RFID`, while VTM1000i is framed around `satellite communication`, `GPS antennas`, `filters and couplers`, and `RF and microwave circuitry`.

## Conditions And Methods

- This comparison is based on the current public Ventec datasheets in the registry.
- Dk and Df values come from different listed methods between the two sheets, so use them as product-level comparisons, not as perfectly normalized lab benchmarks.

## Limits And Non-Claims

- This card does not prove VTM1000i is always better than VT-870.
- It does not cover fabrication yield, copper roughness, or bondply-stack interactions.

## Open Questions

- Whether to add a broader hydrocarbon-ceramic comparison card including `RO4350B`, `Astra MT77`, and `MEGTRON 6`

## Source Links

- https://www.ventec-group.com/media/1957/180720tecspeed20-vt-870.pdf
- https://www.ventec-group.com/media/114432/230320tecspeed20-vtm1000i.pdf
- https://www.ventec-group.com/products/tec-speed-rf/
