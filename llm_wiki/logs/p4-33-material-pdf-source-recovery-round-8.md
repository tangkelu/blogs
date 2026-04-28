# P4-33 Material PDF Source Recovery Round 8

Date: 2026-04-28
Status: `source_backed_fact_layer_partial`

## Purpose

Continue the P4-33 material PDF lane by upgrading four additional AGC local PDF rows after official AGC URL checks and direct PDF text extraction.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/AGC_METEORWAVE_8300_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_METEORWAVE_M1_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_N4000-13_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_N4000-13EP_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_8300_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_M1_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_N4000-13_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_N4000-13EP_TDS.pdf`

## Added Source Records

- `agc-meteorwave-8300-datasheet`
- `agc-meteorwave-m1-datasheet`
- `agc-n4000-13-datasheet`
- `agc-n4000-13ep-datasheet`

## Added Fact Cards

- `materials-agc-meteorwave-8300`
- `materials-agc-meteorwave-m1`
- `materials-agc-n4000-13`
- `materials-agc-n4000-13ep`

## Source-Backed Data Unlocked

- AGC `METEORWAVE 8300`: source-scoped Dk / Df rows at `2 GHz` and `10 GHz`, Tg, Td, T-300, thermal conductivity, specific heat, CTE, Z-axis expansion, moisture absorption, UL / IPC framing, and laminate thickness floor.
- AGC `METEORWAVE M1`: source-scoped `10 GHz` and `77 GHz` dielectric rows, TcDk, Tg, Td, T-300, thermal conductivity, specific heat, CTE, Z-axis expansion, moisture absorption, UL / IPC framing, and guarded automotive-radar / mmWave material-positioning context.
- AGC `N4000-13`: source-scoped `50% resin content` Dk / Df rows at `2.5 GHz` and `10 GHz`, Tg, Td, T-260, T-288, thermal conductivity, CTE, Z-axis expansion, moisture absorption, UL / IPC framing, and laminate thickness floor.
- AGC `N4000-13 EP`: source-scoped `50% resin content` Dk / Df rows at `2.5 GHz` and `10 GHz`, Tg, Td, T-260, T-288, thermal conductivity, CTE, Z-axis expansion, moisture absorption, UL / IPC framing, lead-free material-positioning context, and laminate thickness floor.

## Still Blocked

- Finished-board high-speed, backplane, switch, router, storage, RF, satellite, radar, antenna, mmWave, impedance, insertion-loss, channel, GPS, guidance, EIRP, OTA, or system performance claims.
- Lead-free assembly success, CAF lifetime, high-layer-count manufacturability, reliability qualification, or released-lot acceptance for a specific stackup.
- Supplier lamination recipes, cure cycles, process windows, inspection acceptance limits, or build qualification.
- APT / HIL / other supplier material stock, process capability, certification, price, MOQ, lead time, yield, or production approval.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `four AGC material rows only`
- cumulative P4-33 material PDF source-backed upgrade: `16` AGC exact-product rows plus `5` Rogers exact-product rows plus `2` Ventec exact-product rows plus `4` Shengyi exact-product rows
- next lane: continued official-source recovery for AGC `N4000-29`, `N4000-29NF`, `N7000-2HT`, TSM/TLX/TLY/TLE/TLC/TLF tails, Ventec tail, TUC tail, or selector wiki aggregation for recovered rows.
