---
fact_id: "materials-isola-fr4-high-tg-product-grade-fields"
title: "Isola FR-4/high-Tg product-grade fields are safe only when product name and datasheet conditions stay attached"
topic: "Isola FR-4 high-Tg product-grade fields"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-25"
source_ids:
  - "isola-370hr-datasheet"
  - "isola-370hr-dk-df-tables"
  - "isola-fr408-datasheet"
  - "isola-fr408hr-datasheet"
  - "isola-is410-datasheet"
tags: ["isola", "fr-4", "high-tg", "370hr", "fr408", "fr408hr", "is410", "product-grade"]
---

# Canonical Summary

> Isola FR-4/high-TG materials can support exact-product numeric writing, but only when the product name, source id, and test conditions stay attached to every reused value.

## Stable Facts

- `IS410`, `370HR`, `FR408`, and `FR408HR` are separate official product anchors, not one generic FR-4 bucket.
- Safe reusable numeric fields are product-specific datasheet values only, such as `Dk`, `Df`, `Tg`, `Td`, `T288`, `CTE`, `water absorption`, `peel strength`, and other explicitly tabled properties.
- `370HR` deserves stronger-than-usual `Dk / Df` handling because the corpus also has a condition-sensitive companion construction table.
- `IS410` and `370HR` are the conservative baseline/high-TG FR-4-family examples.
- `FR408` and `FR408HR` are the better-defined higher-performance FR-4-family examples.

## Conditions And Methods

- Keep every numeric field tied to the exact product and datasheet condition.
- Use this card when a layer-count article needs a reusable exact-product FR-4/high-TG comparison row.
- Use this card as the gate before any cross-product FR-4 table is assembled.

## Limits And Non-Claims

- Do not collapse the four products into one universal FR-4 value set.
- Do not infer availability, stocking, approval, or vendor-neutral ranking.
- Do not reuse a number if the product name or test condition is missing.

## Source Links

- https://www.isola-group.com/wp-content/uploads/data-sheets/is410-fr-4-epoxy-laminate-and-prepreg.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/370hr-laminate-prepreg.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/370hr-dk-df-construction-table__dk_df_tables.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/fr408-laminate-and-prepreg.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/fr408hr-laminate-and-prepreg.pdf
