# P4-33 Material PDF Source Recovery Round 9

Date: 2026-04-28
Status: `source_backed_fact_layer_partial`

## Purpose

Continue the P4-33 material PDF lane by upgrading four additional AGC local PDF rows after official AGC URL checks and direct PDF text extraction.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/AGC_N4000-13EPSI_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_N4000-29_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_N4000-29NF_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_N7000-2HT_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_N4000-13EPSI_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_N4000-29_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_N4000-29NF_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_N7000-2HT_TDS.pdf`

## Added Source Records

- `agc-n4000-13epsi-datasheet`
- `agc-n4000-29-datasheet`
- `agc-n4000-29nf-datasheet`
- `agc-n7000-2ht-datasheet`

## Added Fact Cards

- `materials-agc-n4000-13epsi`
- `materials-agc-n4000-29`
- `materials-agc-n4000-29nf`
- `materials-agc-n7000-2ht`

## Source-Backed Data Unlocked

- AGC `N4000-13 EP SI`: source-scoped `50% resin content` Dk / Df rows at `2.5 GHz` and `10 GHz`, Tg, Td, T-260, T-288, thermal conductivity, CTE, Z-axis expansion, moisture absorption, UL / IPC framing, and laminate thickness floor.
- AGC `N4000-29`: source-scoped Dk / Df rows at `2 GHz`, `2.5 GHz`, and `10 GHz`, Tg by DMA / DSC, Td, T-260, T-288, thermal conductivity, CTE, Z-axis expansion, moisture absorption, UL / IPC framing, Meteorwave hybrid material-positioning context, and laminate thickness floor.
- AGC `N4000-29NF`: source-scoped no-flow prepreg construction rows for glass styles `106` and `1080`, main Dk / Df rows at `2 GHz` and `10 GHz`, Tg, Td, T-260, thermal conductivity, CTE, Z-axis expansion, moisture absorption, UL / IPC framing, and rigid-flex / heat-sink bonding material-form context.
- AGC `N7000-2HT`: source-scoped `N7000-2HT laminate` plus `N7000-3 prepreg` pairing, Dk / Df rows at `2.5 GHz` and `10 GHz`, Tg, Td, T-260, thermal conductivity, CTE, Z-axis expansion, moisture absorption, UL / IPC / old GIJ / GIL framing, and laminate thickness floor.

## Still Blocked

- Finished-board high-speed, backplane, storage, telecom, automotive, RF, radar, antenna, insertion-loss, impedance, channel, BGA, direct-chip-attach, burn-in-board, or severe-condition performance claims.
- Lead-free assembly success, CAF lifetime, IST result, high-layer-count manufacturability, rigid-flex bonding success, heat-sink attachment success, reliability qualification, or released-lot acceptance for a specific stackup.
- Supplier lamination recipes, generic process windows, inspection acceptance limits, or build qualification.
- APT / HIL / other supplier material stock, process capability, certification, price, MOQ, lead time, yield, or production approval.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `four AGC material rows only`
- cumulative P4-33 material PDF source-backed upgrade: `20` AGC exact-product rows plus `5` Rogers exact-product rows plus `2` Ventec exact-product rows plus `4` Shengyi exact-product rows
- next lane: continued official-source recovery for AGC TSM / TLX / TLY / TLE / TLC / TLF / RF tails, Ventec tail, TUC tail, or selector wiki aggregation for recovered rows.
