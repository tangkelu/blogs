---
fact_id: "materials-rogers-ro4360g2"
title: "Rogers RO4360G2 baseline material card"
topic: "RO4360G2"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["rogers-ro4360g2-datasheet"]
tags: ["rogers", "ro4360g2", "ro4000", "hydrocarbon-ceramic", "high-dk", "rf-materials"]
---

# Canonical Summary

> RO4360G2 is a Rogers RO4000-line high-frequency laminate with a high process dielectric constant class, useful for compact RF material discussions when kept separate from board-level RF performance claims.

## Stable Facts

- Rogers identifies RO4360G2 as a high-frequency laminate in the RO4000 context.
- The datasheet lists process dielectric constant `6.15 +/- 0.15` in the Z direction at `10 GHz / 23 C` by `IPC-TM-650 2.5.5.5`.
- The datasheet body also gives a design Dk of `6.4`.
- The datasheet lists dissipation factor `0.0038` in the Z direction at `10 GHz / 23 C`.
- The datasheet lists thermal conductivity `0.75 W/m/K` at `50 C` by `ASTM D-5470`.
- The datasheet lists CTE values from `-50 C to 288 C` of `13 / 14 / 28 ppm/C` for X/Y/Z after replicated heat cycle.
- The datasheet lists Tg `>280 C`, Td `407 C`, T288 `>30 min`, moisture absorption `0.08%`, density `2.16 g/cm3`, copper peel strength `0.91 N/mm`, and flammability `V-0`.

## Conditions And Methods

- Keep process Dk, design Dk, and Df separate.
- Keep all thermal and CTE values tied to their listed methods and test ranges.
- Treat the values as datasheet material properties, not finished-board guarantees.

## Limits And Non-Claims

- This card does not prove insertion loss, antenna gain, impedance tolerance, or compact RF module performance.
- It does not prove supplier capability, certification, yield, price, MOQ, or lead time.

## Source Links

- https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro4360g2-high-frequency-laminates-data-sheet.pdf
