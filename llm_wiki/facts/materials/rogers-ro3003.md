---
fact_id: "materials-rogers-ro3003"
title: "RO3003 baseline material card"
topic: "RO3003"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids: ["rogers-ro3003-product-page", "rogers-ro3000-datasheet", "rogers-ro3000-series-product-page"]
tags: ["rogers", "ro3003", "ro3000", "rf-materials", "77ghz", "mmwave"]
---

# Canonical Summary

> RO3003 is a Rogers RO3000-series ceramic-filled PTFE laminate positioned for low-loss RF and microwave use where stable dielectric behavior over frequency and temperature matters more than FR-4-style processing convenience.

## Stable Facts

- Rogers describes RO3003 as a ceramic-filled PTFE composite for commercial microwave and RF printed circuit boards.
- The official RO3003 product page states `Dk 3.00 +/- 0.04`, `Df 0.0010 at 10 GHz`, and X/Y/Z CTE values of `17 / 16 / 25 ppm/C`.
- The 2024 RO3000 family data sheet lists `Dk 3.00 +/- 0.04` at `23 C / 10 GHz` by `IPC TM-650 2.5.5.5`.
- The same data sheet lists a design dielectric constant of `3.00` over `8 GHz to 40 GHz` by differential phase length.
- The same data sheet lists `Df 0.0010` at `23 C / 10 GHz`, `TcDk -3 ppm/C` from `-50 C to 150 C`, thermal conductivity `0.50 W/(m.K)`, moisture absorption `0.04%`, UL 94 `V-0`, and lead-free process compatibility `Yes`.
- Rogers positions RO3003 as appropriate for applications up to `77 GHz` and explicitly mentions automotive radar, ADAS, and mmWave-oriented use cases on the product page.

## Conditions And Methods

- Keep process Dk and design Dk separate.
- Keep the measurement method with every dielectric value.
- When using RO3003 as a 77 GHz material reference, attach the product page or family page date check.

## Limits And Non-Claims

- This card does not prove a complete RF design will meet 77 GHz performance targets by material choice alone.
- This card does not cover copper roughness, foil choice, stackup, transition design, or final insertion-loss performance in a manufactured board.

## Open Questions

- Whether you want separate cards for RO3003 and RO3003G2
- Which internal standard stackups should be linked as preferred RO3003 implementations

## Source Links

- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3003-laminates
- https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro3000-laminate-data-sheet-ro3003----ro3006----ro3010----ro3035.pdf
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates
