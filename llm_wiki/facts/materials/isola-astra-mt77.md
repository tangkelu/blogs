---
fact_id: "materials-isola-astra-mt77"
title: "Astra MT77 baseline material card"
topic: "Astra MT77"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids: ["isola-astra-mt77-datasheet", "isola-astra-mt77-dk-df-table"]
tags: ["isola", "astra-mt77", "rf-materials", "mmwave", "high-frequency"]
---

# Canonical Summary

> Astra MT77 is an Isola very low-loss RF/microwave laminate family positioned for stable dielectric behavior over frequency and temperature, with published frequency-aware Dk / Df tables and FR-4-compatible processing claims.

## Stable Facts

- The Astra MT77 data sheet shows `Tg 200 C` by DSC and `Td 360 C` by TGA at 5 percent weight loss.
- The same sheet shows moisture absorption of `0.1%` and UL 94 `V-0` flammability.
- Isola identifies the material against `IPC-4103 /17`.
- The Astra MT77 Dk / Df table shows `Dk 3.00` and `Df 0.0017` across the published `2 GHz`, `5 GHz`, `10 GHz`, `15 GHz`, and `20 GHz` table entries for the listed core thicknesses.
- Isola markets Astra MT77 as lead-free assembly compatible and FR-4 process compatible.

## Conditions And Methods

- Use the 2024 Dk / Df table when frequency-specific electrical values are needed.
- Use the 2021 data sheet for broader thermal and mechanical values.

## Limits And Non-Claims

- This card does not claim Astra MT77 is a direct drop-in substitute for every PTFE or Rogers material.
- Thickness, copper style, and final stackup still matter for real insertion-loss outcomes.

## Open Questions

- Which internal applications should map to Astra MT77 versus RO4350B or Panasonic MEGTRON families

## Source Links

- https://isola-group.com/wp-content/uploads/data-sheets/astra-mt77.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/astra-mt77-laminate-and-prepreg__Dk_Df_Tables.pdf
