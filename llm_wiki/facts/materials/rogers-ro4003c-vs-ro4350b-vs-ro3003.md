---
fact_id: "materials-rogers-ro4003c-vs-ro4350b-vs-ro3003"
title: "RO4003C vs RO4350B vs RO3003 comparison card"
topic: "RO4003C vs RO4350B vs RO3003"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids: ["rogers-ro4003c-product-page", "rogers-ro4000-datasheet", "rogers-ro4350b-product-page", "rogers-ro3003-product-page", "rogers-ro3000-datasheet"]
tags: ["rogers", "ro4003c", "ro4350b", "ro3003", "comparison", "rf-materials"]
---

# Canonical Summary

> RO4003C, RO4350B, and RO3003 occupy different points on the Rogers RF-material tradeoff map: RO4003C is the cost/process-friendly thermoset option, RO4350B adds UL 94 V-0 and similar FR-4-like processing, and RO3003 is the lower-loss PTFE-family option for more demanding low-loss and mmWave-oriented work.

## Stable Facts

- RO4003C process Dk is `3.38 +/- 0.05` and Df at `10 GHz` is `0.0027`.
- RO4350B process Dk is `3.48 +/- 0.05` and Df at `10 GHz` is `0.0037`.
- RO3003 process Dk is `3.00 +/- 0.04` and Df at `10 GHz` is `0.0010`.
- Rogers states RO4003C and RO4350B use epoxy/glass-style processing methods, while RO4003C explicitly avoids PTFE-style special through-hole treatments.
- Rogers states RO4350B is UL 94 V-0 rated, while the RO4003C page explicitly states RO4003C is not UL 94 V-0 rated.
- RO3003 belongs to the PTFE-based RO3000 family and should be treated with PTFE-family process guidance rather than FR-4 shorthand.

## Conditions And Methods

- Use this card when you need a high-level material-selection framing across thermoset and PTFE families.
- Keep the comparison anchored to the same `10 GHz` Df context.

## Limits And Non-Claims

- This card is not enough to choose a final material without path-loss, thermal, stackup, and manufacturing-fit review.
- It does not include RT/duroid, TMM, RO4835, or hybrid-build cost logic.

## Open Questions

- Whether to add RO4835 to create a broader RO4000 family comparison card
- Whether to add an application-oriented selector card for `sub-6`, `24 GHz`, `77 GHz`, and `mixed digital/RF`

## Source Links

- https://www.rogerscorp.com/advanced-electronics-solutions/ro4000-series-laminates/ro4003c-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro4000-series-laminates/ro4350b-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3003-laminates
- https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro4000-laminates-ro4003c-and-ro4350b---data-sheet.pdf
- https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro3000-laminate-data-sheet-ro3003----ro3006----ro3010----ro3035.pdf
