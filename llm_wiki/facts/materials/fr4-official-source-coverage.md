---
fact_id: "materials-fr4-official-source-coverage"
title: "FR-4 writing now has official Isola FR408 and FR408HR anchors, but FR-4 must remain a family-level topic"
topic: "FR-4 official source coverage"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "isola-fr408-datasheet"
  - "isola-fr408hr-datasheet"
  - "frontendapt-materials-spread-glass-fr4-page-en"
  - "frontendapt-materials-isola-pcb-page-en"
tags: ["fr-4", "isola", "fr408", "fr408hr", "laminate", "prepreg", "source-coverage"]
---

# Canonical Summary

> FR-4 should be treated as a broad laminate family, not a single material with one Dk, Df, Tg, CTE, or loss value. Isola `IS410`, `370HR`, `FR408`, and `FR408HR` give official product-level anchors, while internal pages provide application framing.

## Stable Facts

- IS410, 370HR, FR408, and FR408HR are official Isola laminate/prepreg product sources that can anchor FR-4-family product examples.
- IS410, 370HR, FR408, and FR408HR values are product-specific and condition-specific; they must not be generalized to all FR-4.
- Internal APT pages provide useful FR-4, Isola, and spread-glass application framing, but product-level numbers should come from manufacturer datasheets.
- Any numeric FR-4 comparison should preserve the product name, test condition, and datasheet context.

## Conditions And Methods

- Use this card when drafting FR-4 material explainers, FR-4 versus high-speed material comparisons, and spread-glass stackup discussions.
- Treat product datasheets as the source for material-property values.
- Treat internal pages as application and service-context support.

## Limits And Non-Claims

- This card does not provide a universal FR-4 property table.
- It does not claim FR408 or FR408HR are stocked, recommended, or suitable for all designs.
- It does not replace project-specific stackup review, impedance modeling, or thermal/reliability review.

## Open Questions

- Add more official FR-4 anchors from Ventec, Shengyi, Kingboard, ITEQ, or other manufacturers before publishing broad supplier-comparison tables.
- Add UL source handling if flame-rating or recognition claims appear in blog drafts.

## Source Links

- https://www.isola-group.com/wp-content/uploads/data-sheets/fr408-laminate-and-prepreg.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/fr408hr-laminate-and-prepreg.pdf
- /code/hileap/frontendAPT/public/static/materials/en/spread-glass-fr4.json
- /code/hileap/frontendAPT/public/static/materials/en/isola-pcb.json
