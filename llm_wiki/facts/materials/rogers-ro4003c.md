---
fact_id: "materials-rogers-ro4003c"
title: "RO4003C baseline material card"
topic: "RO4003C"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids: ["rogers-ro4003c-product-page", "rogers-ro4000-datasheet"]
tags: ["rogers", "ro4003c", "ro4000", "rf-materials", "hydrocarbon-ceramic"]
---

# Canonical Summary

> RO4003C is a Rogers RO4000-series hydrocarbon/ceramic laminate positioned as a lower-cost, FR-4-process-compatible RF material for performance-sensitive volume applications without PTFE-style fabrication handling.

## Stable Facts

- Rogers states RO4003C provides tight Dk control and low loss while using the same processing method as standard epoxy/glass.
- The RO4003C page explicitly states that, unlike PTFE-based microwave materials, no special through-hole treatments or handling procedures are required.
- The same page states RO4003C is non-brominated and is not UL 94 V-0 rated.
- Rogers lists `Dk 3.38 +/- 0.05`, `Df 0.0027 at 10 GHz`, and low Z-axis CTE `46 ppm/C` on the public product page.
- The Rogers property tool and RO4000 datasheet family values align with thermal conductivity around `0.71 W/m/K`, moisture absorption `0.04`, and lead-free compatibility `Yes`.

## Conditions And Methods

- Use RO4003C for process-positioning claims when the distinction versus PTFE matters.
- Use the RO4000 datasheet when attaching numeric values to evidence packs.

## Limits And Non-Claims

- This card does not mean RO4003C is suitable for every mmWave or phased-array use case.
- The absence of PTFE-style handling complexity does not remove the need for proper impedance and stackup control.

## Open Questions

- Whether to add a separate fact card for RO4835 as the UL 94 V-0 sister option inside the RO4000 family

## Source Links

- https://www.rogerscorp.com/advanced-electronics-solutions/ro4000-series-laminates/ro4003c-laminates
- https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro4000-laminates-ro4003c-and-ro4350b---data-sheet.pdf
