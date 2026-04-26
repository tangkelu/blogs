---
fact_id: "materials-isola-is410"
title: "Isola IS410 baseline material card"
topic: "IS410"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-26"
source_ids:
  - "isola-is410-datasheet"
  - "isola-is410-processing-guide"
tags: ["isola", "is410", "fr-4", "high-tg", "lead-free", "materials"]
---

# Canonical Summary

> `IS410` is an exact-product Isola laminate/prepreg anchor with official datasheet-backed baseline values; the companion processing guide is usable only for guarded handling, storage, innerlayer-preparation, and dimensional-movement context.

## Stable Facts

- Isola publishes an official exact-product datasheet for `IS410` laminate and prepreg.
- The datasheet identifies `IS410` as a lead-free epoxy laminate and prepreg system.
- The datasheet lists `Tg 180 C` by `DSC`.
- The datasheet lists `Td 350 C` by `TGA @ 5% weight loss`.
- The datasheet lists time to delaminate by `TMA` with copper removed as `T260 50 min` and `T288 10 min`.
- The datasheet lists `Z-axis CTE 55 ppm/C` before `Tg`, `250 ppm/C` after `Tg`, and `3.5%` total expansion from `50 to 260 C`.
- The datasheet lists `X/Y-axis CTE 11 ppm/C` before `Tg`.
- The datasheet lists `thermal conductivity 0.5 W/m.K`.
- The datasheet lists `Dk 3.96` at `100 MHz`, `3.90` at `1 GHz`, `3.97` at `2 GHz`, `3.87` at `5 GHz`, and `3.87` at `10 GHz`.
- The datasheet lists `Df 0.0149` at `100 MHz`, `0.0189` at `1 GHz`, `0.0200` at `2 GHz`, `0.0230` at `5 GHz`, and `0.0230` at `10 GHz`.
- The datasheet lists `moisture absorption 0.20%`, `CTI 3 (175-249)`, `flammability V-0`, and `RTI 130 C`.
- Isola also publishes an `IS410` processing guide that explicitly covers prepreg handling and storage, innerlayer preparation, dimensional stability, lamination, and drilling as fabricator-side process guidance.

## Conditions And Methods

- Keep all numeric values tied to the `IS410` datasheet and its stated methods.
- Keep the dielectric values frequency-specific and do not flatten them into one generic `FR-4` number.
- Use the processing guide only for guarded context about prepreg handling, storage discipline, innerlayer preparation, laminate/prepreg dimensional movement, and process sensitivity.
- Treat the processing guide as fabricator starting-point guidance rather than a transferable production recipe.

## Limits And Non-Claims

- This card does not make `IS410` interchangeable with generic `FR-4` or with other Isola materials such as `370HR`, `FR408`, or `FR408HR`.
- It does not prove a specific stackup, layer-count capability, via architecture, drilling result, or board-level reliability outcome.
- It does not turn the processing guide into a universal lamination schedule, registration tolerance, drill program, or shop capability claim.
- It does not make availability, stocking, procurement, or approval claims.

## Source Links

- https://www.isola-group.com/wp-content/uploads/data-sheets/is410-fr-4-epoxy-laminate-and-prepreg.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/is410-fr-4-epoxy-laminate-and-prepreg_Processing_Guide_new.pdf
