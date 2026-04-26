---
fact_id: "materials-agc-vs-ventec-commercial-antenna-rf-compactness"
title: "AGC vs Ventec commercial antenna / RF compactness comparison card"
topic: "AGC vs Ventec commercial antenna / RF compactness"
category: "materials"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-25"
source_ids:
  - "agc-rf-30a-product-page"
  - "agc-rf-30a-datasheet"
  - "agc-rf-10-product-page"
  - "agc-rf-10-datasheet"
  - "ventec-vt-870-datasheet"
  - "ventec-vtm1000i-datasheet"
  - "ventec-tec-speed-rf-family-page"
tags: ["agc", "ventec", "comparison", "antenna", "pim", "compact-rf", "rf-materials"]
---

# Canonical Summary

> For a conservative cross-vendor selector built only from the current AGC and Ventec records, RF-30A reads as the AGC choice when commercial antenna volume and published PIM-aware framing are central, VT-870 reads as the process-friendlier hydrocarbon commercial antenna option with an explicit HVLP foil note for PIM-sensitive work, and RF-10 plus VTM1000i read as the high-Dk compactness branch when electrical size reduction matters more than staying near Dk 3.

## Stable Facts

- AGC positions RF-30A as a `high volume antenna material`, and the RF-30A TDS includes coupon-based PIM framing tied to stated test conditions.
- Ventec frames VT-870 around `cellular base station antenna and power amplifiers`, and its datasheet explicitly notes `HVLP` foil for `PIM-sensitive applications`.
- RF-30A lists `Dk 2.97 +/- 0.05 at 1.9 GHz` and `Df 0.0020 at 10 GHz`, while VT-870 lists `Dk 3.48 +/- 0.05 at 10 GHz` and `Df 0.0037 at 10 GHz`.
- RF-30A lists thermal conductivity `0.42 W/mK`, while VT-870 lists `0.69 W/mK`.
- For compact RF structures, RF-10 lists `Dk 10.2 +/- 0.3 at 10 GHz` and VTM1000i lists `Dk 9.8 +/- 0.245 at 10 GHz`.
- RF-10 lists `Df 0.0025 at 10 GHz`, while VTM1000i lists `Df 0.0023 at 10 GHz`.
- RF-10 lists thermal conductivity `0.85 W/mK`, while VTM1000i lists `1.00 W/mK`.
- AGC frames RF-10 around `microstrip patch antennas`, `GPS antennas`, `filters`, and `couplers`, while Ventec frames VTM1000i around `GPS antennas`, `filters and couplers`, `satellite communication systems`, and `RF and microwave circuitry`.

## Conditions And Methods

- This card is a source-bound selector built from the current AGC product pages and datasheets plus the current Ventec RF family page and datasheets already in the registry.
- RF-30A publishes its anchor Dk at `1.9 GHz`, while VT-870, RF-10, and VTM1000i publish their main Dk values at `10 GHz`, so use this as directional product selection guidance rather than a normalized benchmark.
- RF-30A PIM statements stay attached to AGC's stated coupon and power conditions.
- VT-870's PIM-sensitive note is a foil-availability statement, not a published finished-board PIM result.
- RF-10 and VTM1000i belong to the compact high-Dk branch; RF-30A and VT-870 belong to the lower-Dk commercial antenna branch, so they should not be treated as direct substitutes without geometry rework.

## Limits And Non-Claims

- This card does not claim one vendor is globally better across all antenna or microwave builds.
- It does not prove finished-board PIM, insertion loss, or yield without stackup, copper, finish, connector, and fabrication details.
- It does not extend to Taconic, Arlon, or any other vendor family not already covered by the linked registry records.

## Open Questions

- Whether to add RF-35HTC later as a separate thermal and power-RF branch instead of broadening this compact commercial selector.

## Source Links

- https://www.agc-multimaterial.com/solutions/rf-30a/
- https://www.agc-multimaterial.com/agc-downloads/AGC_RF-30A_TDS.pdf
- https://www.agc-multimaterial.com/solutions/rf-10/
- https://www.agc-multimaterial.com/agc-downloads/AGC_RF-10_TDS.pdf
- https://www.ventec-group.com/media/1957/180720tecspeed20-vt-870.pdf
- https://www.ventec-group.com/media/114432/230320tecspeed20-vtm1000i.pdf
- https://www.ventec-group.com/products/tec-speed-rf/
