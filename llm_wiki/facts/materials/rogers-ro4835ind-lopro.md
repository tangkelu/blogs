---
fact_id: "materials-rogers-ro4835ind-lopro"
title: "Rogers RO4835IND LoPro baseline material card"
topic: "RO4835IND LoPro"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["rogers-ro4835ind-lopro-datasheet"]
tags: ["rogers", "ro4835ind-lopro", "ro4835", "industrial-radar", "lopro", "rf-materials"]
---

# Canonical Summary

> RO4835IND LoPro is a Rogers high-frequency circuit material positioned for `60-81 GHz` short-range industrial radar, distinct from base RO4835 and requiring frequency-specific value handling.

## Stable Facts

- Rogers identifies RO4835IND LoPro as a high-frequency circuit material for `60-81 GHz` short-range industrial radar.
- The datasheet lists process dielectric constant `3.48 +/- 0.05` in the Z direction at `10 GHz / 23 C` by `IPC-TM-650 2.5.5.5`.
- The datasheet lists dissipation factor `0.0037` at `10 GHz / 23 C` and `0.0031` at `2.5 GHz / 23 C`.
- The datasheet lists design Dk `3.49` at `77 GHz` and `3.48` at `60 GHz`, both by microstrip differential phase length.
- The datasheet lists transmission-line loss `2.75 dB/in` at `77 GHz` and `2.13 dB/in` at `60 GHz` by microstrip differential phase length.
- The datasheet lists dimensional stability `<0.5 mm/m`, Tg `>280 C`, Td `390 C`, moisture absorption `0.05%`, copper peel strength `0.88 N/mm`, flammability `V-0`, and lead-free process compatible `Yes`.
- The offering table calls out standard thickness `0.0040 in / 0.102 mm +/- 0.0007 in`.

## Conditions And Methods

- Keep `2.5 GHz`, `10 GHz`, `60 GHz`, and `77 GHz` values separate.
- Treat transmission-line loss values as Rogers method-specific measurement context, not a finished-board prediction.
- Keep LoPro and IND product identity intact.

## Limits And Non-Claims

- This card does not prove industrial-radar performance, range, sensitivity, insertion loss, antenna behavior, or production qualification.
- It does not prove supplier capability, certification, yield, price, MOQ, or lead time.

## Source Links

- https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro4835ind-lopro-laminate-data-sheet.pdf
