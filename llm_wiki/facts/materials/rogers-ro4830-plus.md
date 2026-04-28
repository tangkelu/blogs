---
fact_id: "materials-rogers-ro4830-plus"
title: "Rogers RO4830 Plus baseline material card"
topic: "RO4830 Plus"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["rogers-ro4830-plus-datasheet"]
tags: ["rogers", "ro4830-plus", "ro4000", "automotive-radar", "rf-materials"]
---

# Canonical Summary

> RO4830 Plus is a Rogers thermoset circuit material positioned for radar-frequency applications, including `76-81 GHz` automotive radar context, but datasheet values must not be converted into finished-radar performance claims.

## Stable Facts

- Rogers identifies RO4830 Plus as a laminate / circuit material and positions it for `76-81 GHz` automotive radar and FR-4 cap-layer use.
- The datasheet lists dielectric constant `3.00 +/- 0.04` at `10 GHz`, `23 C / 50% RH`, by `IPC TM-650 2.5.5.5`.
- The datasheet lists dissipation factor `0.0015` at `10 GHz`, `23 C / 50% RH`, by the same IPC method.
- The datasheet lists design Dk `3.03` at `77 GHz` by microstrip differential phase length.
- The datasheet body notes `1.5 dB/inch` insertion loss for `5 mil` laminates measured by microstrip differential phase length.
- The datasheet lists TCDk `-54 ppm/C` from `-50 C to 150 C`, Td `357 C`, Tg `285 C` by DMA, thermal conductivity `0.5 W/(m.K)`, CTE `46 / 47 / 56 ppm/C` for X/Y/Z, moisture absorption `0.02%`, density `1.64 g/cm3`, and flammability `V-0`.
- The datasheet states lead-free process compatible: `YES`.

## Conditions And Methods

- Keep `10 GHz` IPC values separate from `77 GHz` design Dk and insertion-loss context.
- Treat the insertion-loss note as Rogers measurement context, not a universal design promise.
- Treat the values as material datasheet properties.

## Limits And Non-Claims

- This card does not prove automotive radar compliance, antenna efficiency, EIRP, detection range, insertion loss for a finished board, or production qualification.
- It does not prove supplier capability, certification, yield, price, MOQ, or lead time.

## Source Links

- https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro4830-plus-laminates-data-sheet.pdf
