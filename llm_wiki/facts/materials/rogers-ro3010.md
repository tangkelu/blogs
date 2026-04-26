---
fact_id: "materials-rogers-ro3010"
title: "RO3010 baseline material card"
topic: "RO3010"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids: ["rogers-ro3010-product-page", "rogers-ro3000-datasheet", "rogers-ro3000-series-product-page"]
tags: ["rogers", "ro3010", "ro3000", "rf-materials", "high-dk", "miniaturization"]
---

# Canonical Summary

> RO3010 is a very high-Dk member of the Rogers RO3000 family, positioned for RF circuit miniaturization where compactness matters more than lowest-possible loss.

## Stable Facts

- Rogers states RO3010 has `Dk 10.2 +/- 0.30` and `Df 0.0022 at 10 GHz`.
- Rogers also lists low X/Y/Z CTE values of `13 / 11 / 16 ppm/C` on the product page sample table.
- The family property table exposed on the product page lists thermal conductivity `0.95 W/m/K`, water absorption `0.05`, and UL 94 `V-0`.
- Rogers states the material's stability simplifies broadband component design and makes it suitable for circuit miniaturization.
- The family data table shows design Dk `11.2` and thermal coefficient of dielectric constant `-395 ppm/C`.

## Conditions And Methods

- Keep process Dk and design Dk separate.
- Keep miniaturization framing separate from any claim about overall RF efficiency.

## Limits And Non-Claims

- This card does not claim RO3010 is low loss relative to RO3003.
- High Dk does not remove the need to model tolerance, temperature drift, and stackup behavior.

## Open Questions

- Whether to add RO3010 use-case notes for compact resonators and phased-array unit cells

## Source Links

- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3010-laminates
- https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro3000-laminate-data-sheet-ro3003----ro3006----ro3010----ro3035.pdf
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates
