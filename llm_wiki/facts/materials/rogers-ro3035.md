---
fact_id: "materials-rogers-ro3035"
title: "RO3035 baseline material card"
topic: "RO3035"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids: ["rogers-ro3035-product-page", "rogers-ro3000-datasheet", "rogers-ro3000-series-product-page"]
tags: ["rogers", "ro3035", "ro3000", "rf-materials", "5g", "massive-mimo"]
---

# Canonical Summary

> RO3035 is a Rogers RO3000-series ceramic-filled PTFE laminate with a moderate dielectric constant and low loss, positioned between RO3003 and higher-Dk family members for broadband and 5G-oriented RF design tradeoffs.

## Stable Facts

- Rogers states RO3035 has `Dk 3.50 +/- 0.05` and `Df 0.0015 at 10 GHz`.
- The product page sample table lists X/Y/Z CTE values of `17 / 17 / 24 ppm/C`, thermal conductivity `0.50 W/m/K`, water absorption `0.04`, and UL 94 `V-0`.
- Rogers states RO3035 can be used in applications up to `30-40 GHz`.
- Rogers positions RO3035 for 5G, millimeter-wave sub-6 GHz, and massive MIMO applications on the public product page.
- The family data table shows design Dk `3.60` and thermal coefficient of dielectric constant `-45 ppm/C`.

## Conditions And Methods

- Use the product page for application framing and the family data sheet for stable numeric extraction.
- Keep the `30-40 GHz` positioning tied to the product-page date check.

## Limits And Non-Claims

- This card does not prove RO3035 is the right default choice for all 5G RF designs.
- It does not replace path-level loss modeling or stackup validation.

## Open Questions

- Whether to add a dedicated RO3035 vs RO3003 comparison for sub-6 GHz and 5G front-end work

## Source Links

- https://rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3035-laminates
- https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro3000-laminate-data-sheet-ro3003----ro3006----ro3010----ro3035.pdf
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates
