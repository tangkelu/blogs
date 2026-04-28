# P4-33 Material PDF Source Recovery Round 7

Date: 2026-04-28
Status: `source_backed_fact_layer_partial`

## Purpose

Continue the P4-33 material PDF lane by upgrading additional AGC METEORWAVE local PDF rows after official AGC TDS URL checks and extraction.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/AGC_METEORWAVE_1000_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_METEORWAVE_1000NF_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_METEORWAVE_2000_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_METEORWAVE_3000_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_METEORWAVE_4000M_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_1000_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_1000NF_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_2000_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_3000_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_4000M_TDS.pdf`

## Added Source Records

- `agc-meteorwave-1000-datasheet`
- `agc-meteorwave-1000nf-datasheet`
- `agc-meteorwave-2000-datasheet`
- `agc-meteorwave-3000-datasheet`
- `agc-meteorwave-4000m-datasheet`

## Added Fact Cards

- `materials-agc-meteorwave-1000`
- `materials-agc-meteorwave-1000nf`
- `materials-agc-meteorwave-2000`
- `materials-agc-meteorwave-3000`
- `materials-agc-meteorwave-4000m`

## Source-Backed Data Unlocked

- AGC `METEORWAVE 1000`: source-scoped Dk / Df rows at `2 GHz` and `10 GHz`, Tg, Td, T-300, thermal conductivity, CTE, Z-axis expansion, moisture absorption, UL / IPC-4101 framing, and laminate thickness floor.
- AGC `METEORWAVE 1000NF`: no-flow prepreg identity, available glass-style rows, flow migration range, source-scoped Dk / Df rows, Tg, Td, T-300, thermal conductivity, CTE, Z-axis expansion, moisture absorption, and bonding / rigid-flex use-case context.
- AGC `METEORWAVE 2000`: source-scoped Dk / Df rows at `2 GHz` and `10 GHz`, Tg, Td, T-300, thermal conductivity, CTE, Z-axis expansion, moisture absorption, UL / IPC-4101 framing, and laminate thickness floor.
- AGC `METEORWAVE 3000`: source-scoped Dk / Df rows at `2 GHz` and `10 GHz`, Tg, Td, T-300, thermal conductivity, CTE, Z-axis expansion, moisture absorption, UL / IPC-4101 framing, and laminate thickness floor.
- AGC `METEORWAVE 4000M`: source-scoped `10 GHz` and `77 GHz` dielectric rows, TcDk, TMA / DMA Tg, Td, T-300, thermal conductivity, specific heat, CTE, Z-axis expansion, moisture absorption, and automotive-radar material-positioning context.

## Still Blocked

- Finished-board `25 GHz`, `77 GHz`, radar, antenna, insertion-loss, impedance, channel, router, switch, storage, supercomputer, or cloud-system performance claims.
- Automotive qualification, radar-program acceptance, CAF lifetime, IST acceptance, high-layer-count manufacturability, or lead-free assembly success for a specific stackup.
- Lamination recipes, cure-cycle defaults, pressure defaults, flow guarantees, or rigid-flex bonding outcomes for a specific supplier or stackup.
- APT / HIL / other supplier material stock, process capability, certification, price, MOQ, lead time, yield, or production approval.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `five AGC METEORWAVE material rows only`
- cumulative P4-33 material PDF source-backed upgrade: `12` AGC exact-product rows plus `5` Rogers exact-product rows plus `2` Ventec exact-product rows plus `4` Shengyi exact-product rows
- next lane: selector wiki aggregation for the recovered AGC / Rogers / Ventec / Shengyi rows, or continued official-source recovery for Taconic and the broader material PDF tail.
