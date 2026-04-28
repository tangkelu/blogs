---
fact_id: "materials-rogers-rt-duroid-6202"
title: "Rogers RT/duroid 6202 baseline material card"
topic: "RT/duroid 6202"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["rogers-rt-duroid-6202-datasheet"]
tags: ["rogers", "rt-duroid-6202", "ptfe", "woven-glass", "low-dk", "microwave", "rf-materials"]
---

# Canonical Summary

> RT/duroid 6202 is a Rogers low-Dk microwave laminate with limited woven-glass reinforcement where thickness-dependent dielectric-constant handling is part of safe reuse.

## Stable Facts

- Rogers identifies RT/duroid 6202 as a high-frequency laminate / circuit material with limited woven-glass reinforcement for dimensional stability.
- The datasheet lists dielectric constant `2.94 +/- 0.04` in the Z direction at `10 GHz / 23 C` by `IPC-TM-650 2.5.5.5`.
- The datasheet includes a thickness-dependent Dk note: `0.005 in` laminates use `3.06 +/- 0.04`, `0.010 in` and `0.015 in` laminates use `3.02 +/- 0.04`, and `>=0.020 in` laminates use `2.94 +/- 0.04`.
- The datasheet lists dissipation factor `0.0015` in the Z direction at `10 GHz / 23 C`.
- The datasheet lists TCDk `+5 ppm/C` from `-50 C to +150 C` at `10 GHz`.
- The datasheet lists moisture absorption `0.04%`, thermal conductivity `0.68 W/m/K` at `80 C`, CTE `15 / 15 / 30 ppm/C` from `-55 C to 288 C`, dimensional stability `0.07 mm/m`, Td `500 C`, density `2.1 g/cm3`, copper peel `1.6 N/mm`, flammability `V-0`, and lead-free process compatible `YES`.

## Conditions And Methods

- Preserve the thickness-dependent Dk note; do not flatten all thicknesses into one universal value.
- Keep TCDk range, CTE range, and thermal-conductivity temperature with the values.
- Treat the values as material properties, not finished-board microwave performance.

## Limits And Non-Claims

- This card does not prove insertion loss, antenna behavior, microwave package performance, or fabrication capability.
- It does not prove supplier capability, certification, yield, price, MOQ, or lead time.

## Source Links

- https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/rt-duroid-6202-laminate-data-sheet.pdf
