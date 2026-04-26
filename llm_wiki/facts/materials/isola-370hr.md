---
fact_id: "materials-isola-370hr"
title: "Isola 370HR baseline material card"
topic: "370HR"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-26"
source_ids:
  - "isola-370hr-datasheet"
  - "isola-370hr-processing-guide"
  - "isola-370hr-dk-df-tables"
tags: ["isola", "370hr", "high-tg", "fr-4", "epoxy", "laminate", "prepreg", "materials"]
---

# Canonical Summary

> `370HR` is an exact-product Isola high-Tg epoxy laminate/prepreg anchor with public datasheet-backed baseline values, but its `Dk / Df` handling must stay condition-sensitive because Isola also publishes a companion `370HR` construction table rather than one universal dielectric row for every use case.

## Stable Facts

- Isola publishes an official exact-product datasheet for `370HR` laminate and prepreg.
- The datasheet identifies `370HR` as a `180 C Tg` epoxy laminate and prepreg system and lists `Td 340 C`.
- The datasheet lists `T260 60 min` and `T288 30 min` with copper removed by `TMA`.
- The datasheet lists `Z-axis CTE` as `45 ppm/C` pre-`Tg`, `230 ppm/C` post-`Tg`, and `2.8%` total expansion from `50 to 260 C`.
- The datasheet lists `X/Y-axis CTE pre-Tg 13/14 ppm/C`.
- The datasheet lists `thermal conductivity 0.4 W/m.K`.
- The datasheet lists baseline dielectric values as `Dk 4.24 @ 100 MHz` by `IPC-TM-650 2.5.5.3`, `Dk 4.17 @ 1 GHz` by `IPC-TM-650 2.5.5.9`, and `Dk 4.04 @ 2 GHz`, `3.92 @ 5 GHz`, `3.92 @ 10 GHz` by `Bereskin Stripline`.
- The datasheet lists baseline loss values as `Df 0.0150 @ 100 MHz`, `0.0161 @ 1 GHz`, `0.0210 @ 2 GHz`, `0.0250 @ 5 GHz`, and `0.0250 @ 10 GHz`, with the same method split between `IPC-TM-650` and `Bereskin Stripline`.
- The datasheet also lists `moisture absorption 0.15%`, `flammability V-0`, `RTI 130 C`, and `CTI 3 (175-249)`.
- Isola separately publishes a `370HR` `Dk / Df` construction table for core and prepreg data, so dielectric values are explicitly construction-sensitive companion data rather than a license to flatten `370HR` into one invariant `Dk / Df`.

## Conditions And Methods

- Keep all numeric values tied to the official `370HR` datasheet and its stated test methods.
- Keep the frequency-specific dielectric rows explicit; the datasheet itself changes across `100 MHz`, `1 GHz`, `2 GHz`, `5 GHz`, and `10 GHz`.
- Treat the datasheet dielectric rows as baseline product values, and treat the separate `370HR` construction table as the stronger source when a draft needs construction-aware `Dk / Df`.
- Keep any use of the processing guide limited to guarded process-sensitivity context such as moisture handling, dimensional characterization, lamination-window sensitivity, and thicker-multilayer cure-time dependence.

## Limits And Non-Claims

- This card does not make `370HR` interchangeable with generic high-Tg `FR-4`, `IS410`, `FR408`, `FR408HR`, or any other Isola system.
- It does not collapse the `370HR` construction table into one universal `Dk / Df` value for all resin contents, glass styles, or stack constructions.
- It does not turn the processing guide into a guaranteed fabrication recipe, stackup recommendation, sequential-lamination claim, or board-level reliability outcome.
- It does not make availability, stocking, procurement, or fabricator-capability claims.

## Source Links

- https://www.isola-group.com/wp-content/uploads/data-sheets/370hr-laminate-prepreg.pdf
- https://www.isola-group.com/wp-content/uploads/370HR-Laminate-and-Prepreg-Processing-Guide052020.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/370HR_Dk_Df_Construction_Table__Dk_Df_Tables.pdf
