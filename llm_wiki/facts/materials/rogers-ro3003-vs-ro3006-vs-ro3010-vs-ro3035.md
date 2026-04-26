---
fact_id: "materials-rogers-ro3003-vs-ro3006-vs-ro3010-vs-ro3035"
title: "RO3003 vs RO3006 vs RO3010 vs RO3035 comparison card"
topic: "RO3000 family comparison ladder"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-25"
source_ids:
  - "rogers-ro3000-datasheet"
  - "rogers-ro3003-product-page"
  - "rogers-ro3006-product-page"
  - "rogers-ro3010-product-page"
  - "rogers-ro3035-product-page"
  - "rogers-ro3000-fabrication-guidelines"
tags: ["rogers", "ro3000", "ro3003", "ro3006", "ro3010", "ro3035", "comparison", "rf-materials", "hybrid-stackup"]
---

# Canonical Summary

> RO3003, RO3035, RO3006, and RO3010 form a practical Rogers RO3000 ladder: RO3003 is the lowest-loss low-Dk anchor, RO3035 is a slightly higher-Dk middle step, RO3006 moves into compact high-Dk territory, and RO3010 is the aggressive miniaturization option with the largest dielectric and temperature-drift tradeoff.

## Stable Facts

- Process Dk at `23 C / 10 GHz` is `3.00 +/- 0.04` for RO3003, `3.50 +/- 0.05` for RO3035, `6.15 +/- 0.15` for RO3006, and `10.2 +/- 0.30` for RO3010.
- Design Dk over `8 GHz to 40 GHz` is `3.00` for RO3003, `3.60` for RO3035, `6.50` for RO3006, and `11.2` for RO3010.
- Df at `23 C / 10 GHz` is `0.0010` for RO3003, `0.0015` for RO3035, `0.0020` for RO3006, and `0.0022` for RO3010.
- Thermal coefficient of dielectric constant is `-3 ppm/C` for RO3003, `-45 ppm/C` for RO3035, `-262 ppm/C` for RO3006, and `-395 ppm/C` for RO3010.
- Thermal conductivity is `0.50 W/(m.K)` for RO3003, `0.50 W/(m.K)` for RO3035, `0.79 W/(m.K)` for RO3006, and `0.95 W/(m.K)` for RO3010.
- Moisture absorption is `0.04%` for RO3003, `0.04%` for RO3035, `0.02%` for RO3006, and `0.05%` for RO3010.
- X/Y/Z CTE is `17 / 16 / 25 ppm/C` for RO3003, `17 / 17 / 24 ppm/C` for RO3035, `17 / 17 / 24 ppm/C` for RO3006, and `13 / 11 / 16 ppm/C` for RO3010.
- Rogers positions RO3003 for use cases up to `77 GHz`; RO3035 for roughly `30-40 GHz`; RO3006 for reduced circuit size; and RO3010 for circuit miniaturization and broadband component stability.
- Rogers fabrication guidance states RO3000 materials use standard PTFE circuit-board processing techniques with minor modifications, not generic FR-4 handling assumptions.

## Practical Selector

- Choose RO3003 when the main requirement is the lowest loss and the most stable dielectric behavior in this four-material set.
- Choose RO3035 when you need a modest Dk increase over RO3003 without jumping into the much larger TcDk and loss penalty of RO3006.
- Choose RO3006 when RF structure size reduction materially matters and the design can tolerate roughly double the `10 GHz` Df of RO3003.
- Choose RO3010 only when very high Dk is needed for aggressive miniaturization and the larger dielectric drift must be modeled explicitly.
- Treat all four as PTFE-family materials in fabrication planning, including hybrid multilayer discussions.

## Conditions And Methods

- Keep process Dk and design Dk separate in every downstream use.
- Keep all numeric comparisons tied to the stated method and frequency context from the RO3000 family data sheet.
- Use this card as a Rogers-family ladder inside layer-count and hybrid-stackup blogs, then add bondply or adhesive evidence separately if the draft discusses actual multilayer bonding.

## Limits And Non-Claims

- This card does not say any RO3000 option processes like RO4000 or generic FR-4.
- It does not provide RO4400 bondply, adhesive-system, lamination-cycle, or hybrid build recipe values.
- It does not prove which material is optimal for a full `10-layer` stackup without trace geometry, copper, bonding, and fabrication-fit review.
- It does not introduce Taconic, Arlon, or other non-Rogers alternatives.

## Open Questions

- Whether a second card is needed later for `RO3000 family ladder` vs `RO4000 family hybrid-friendly ladder`
- Whether internal 10-layer blogs want a short mapping from `sub-6`, `24 GHz`, `39 GHz`, and `77 GHz` examples to this ladder

## Source Links

- https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro3000-laminate-data-sheet-ro3003----ro3006----ro3010----ro3035.pdf
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3003-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3006-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3010-laminates
- https://rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3035-laminates
- https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/fabrication-information/fabrication-guidelines-ro3000-and-ro3200-series-high-frequency-circuit-materials.pdf
