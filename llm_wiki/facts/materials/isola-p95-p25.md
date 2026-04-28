---
fact_id: "materials-isola-p95-p25"
title: "Isola P95/P25 exact-product polyimide material card"
topic: "P95/P25"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-27"
source_ids:
  - "isola-p95-p25-datasheet"
  - "isola-p95-p25-dk-df-tables"
tags: ["isola", "p95", "p25", "polyimide", "high-temperature", "laminate", "prepreg", "materials"]
---

# Canonical Summary

> `P95/P25` is an exact-product Isola polyimide laminate/prepreg system for high-temperature printed circuit applications. Use it as a source-scoped high-temperature material anchor, not as a blanket hi-rel, aerospace, military, or acceptance-proof claim.

## Stable Facts

- Isola publishes an official `P95/P25` datasheet.
- The datasheet identifies `P95` as core material and `P25` as prepreg in one polyimide-based product system.
- The datasheet positions the product line for high-temperature printed circuit applications.
- The datasheet lists `Tg 260 C` by `DSC`.
- The datasheet lists `Td 416 C` by `TGA` at `5% weight loss`.
- The datasheet lists `T260 60 min` by `TMA` with copper removed.
- The datasheet lists `Z-axis CTE 55 ppm/C` pre-`Tg`, `1.5%` total expansion from `50 to 260 C`, and `X/Y-axis CTE 13/14 ppm/C` pre-`Tg`.
- The datasheet lists thermal conductivity `0.4 W/m.K`.
- The datasheet baseline dielectric rows include `Dk 3.83 @ 100 MHz`, `3.80 @ 500 MHz`, `3.78 @ 1 GHz`, `3.76 @ 2 GHz`, `3.73 @ 5 GHz`, and `3.73 @ 10 GHz`.
- The datasheet baseline loss rows include `Df 0.0135 @ 100 MHz`, `0.0151 @ 500 MHz`, `0.0172 @ 1 GHz`, `0.0179 @ 2 GHz`, `0.0188 @ 5 GHz`, and `0.021 @ 10 GHz`.
- Isola also publishes a separate `P95/P25` `Dk / Df` table, so dielectric use should remain construction- and frequency-sensitive where a draft needs more than the datasheet baseline row.

## Conditions And Methods

- Keep all numeric values tied to the official datasheet and stated test methods.
- Keep `P95` and `P25` together as a published laminate/prepreg system unless a source specifically separates them.
- Use the `Dk / Df` construction table when a draft needs construction-aware dielectric values.
- Treat `IPC-4101 /40 /41`, UL file, RoHS, reflow, via-fill, multiple-reflow, and multiple-lamination wording as product context only.

## Limits And Non-Claims

- This card does not make `P95/P25` interchangeable with `370HR`, `I-Speed`, `I-Tera MT40`, `Tachyon 100G`, `Astra MT77`, or generic polyimide.
- It does not prove Class 3, Class 3A, aerospace, military, defense, medical, space, outgassing, supplier approval, lot acceptance, or release authority.
- It does not prove HIL or APT stocking, procurement approval, lead time, cost, yield, stackup capability, or sequential-lamination capability.
- It does not turn high-temperature material values into board-level reliability thresholds or acceptance criteria.

## Source Links

- https://www.isola-group.com/wp-content/uploads/data-sheets/p95-p25.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/P95_P25__Dk_Df_Tables.pdf
