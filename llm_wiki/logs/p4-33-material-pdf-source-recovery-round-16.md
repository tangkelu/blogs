# P4-33 Material PDF Source Recovery Round 16

Date: 2026-04-28
Status: `source_backed_fact_layer_partial`

## Purpose

Integrate the scout-only AGC tail findings for `METEORWAVE ELL` and `TLF-35A` into source-backed `llm_wiki` records after main-agent review of the official URL checks and local PDF text extraction.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/AGC_ELL_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_TLF-35A_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_ELL_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_TLF-35A_TDS.pdf`
- `logs/p4-33-agc-tail-scout-round-16.md`

## Added Source Records

- `agc-meteorwave-ell-datasheet`
- `agc-tlf-35a-datasheet`

## Added Fact Cards

- `materials-agc-meteorwave-ell`
- `materials-agc-tlf-35a`

## Source-Backed Data Unlocked

- AGC `METEORWAVE ELL`: source-scoped laminate / prepreg family values for `ELL 101`, `ELL 102`, and `ELL 103`, including variant-specific `10 GHz` Dk / Df, electric strength, Tg, Td, T-288 / T-300, thermal conductivity, peel strength, CTE, Z-axis expansion, moisture absorption, outgas, thickness, and panel-size context.
- AGC `TLF-35A`: source-scoped Dk 3.5 RF laminate values, including modified-IPC `10 GHz` Dk / Df, resistivity, thermal conductivity, CTE, peel strength, flexural strength, flammability, water absorption, thickness, panel-size, copper-cladding, and manufacturing-increment context.

## Still Blocked

- Finished-board insertion loss, RF, microwave, antenna, radar, telecom, AI, cloud, router, switching, 112 Gb, aerospace, repeater, power-amplifier, LNA, passive-component, filter, coupler, PIMD, PTH, attenuation, or thermal-cycling performance claims.
- Space qualification, automotive-radar readiness, AI server readiness, competitive equivalence, drop-in replacement, released-lot acceptance, production approval, or current compliance claims without refresh.
- Supplier process windows, build capability, stock, price, MOQ, lead time, yield, certification, or production approval.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `two AGC material rows only`
- cumulative P4-33 material PDF source-backed upgrade: `32` AGC exact-product / exact-family rows plus `5` Rogers exact-product rows plus `13` Ventec exact-product rows plus `4` Shengyi exact-product rows plus `3` TUC exact-product rows
- next lane: TUC `TU-865S` after preliminary-revision binding, Ventec product-form-specific rows, Rogers legacy HF rows after ownership / source validation, or selector wiki aggregation for recovered material rows.
