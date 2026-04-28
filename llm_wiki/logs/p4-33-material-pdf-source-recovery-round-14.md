# P4-33 Material PDF Source Recovery Round 14

Date: 2026-04-28
Status: `source_backed_fact_layer_partial`

## Purpose

Continue the AGC tail recovery by upgrading five additional local AGC RF / microwave laminate PDFs after official AGC PDF URL checks and direct PDF text extraction.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/AGC_TSM-DS3_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_TSM-DS3b_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_TSM-DS3M_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_TLX-8_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_TLY-5_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_TSM-DS3_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_TSM-DS3b_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_TSM-DS3M_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_TLX-8_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_TLY-5_TDS.pdf`

## Added Source Records

- `agc-tsm-ds3-datasheet`
- `agc-tsm-ds3b-datasheet`
- `agc-tsm-ds3m-datasheet`
- `agc-tlx-8-datasheet`
- `agc-tly-5-datasheet`

## Added Fact Cards

- `materials-agc-tsm-ds3`
- `materials-agc-tsm-ds3b`
- `materials-agc-tsm-ds3m`
- `materials-agc-tlx-8`
- `materials-agc-tly-5`

## Source-Backed Data Unlocked

- AGC `TSM-DS3`: source-scoped low-loss microwave laminate values, including Dk / Df rows, thermal conductivity, Td, CTE, dielectric breakdown, dielectric strength, arc resistance, moisture absorption, thicknesses, and sheet-size context.
- AGC `TSM-DS3b`: source-scoped `10 GHz` low-loss microwave laminate values, including Dk / Df rows, thermal conductivity, Td, CTE, dielectric breakdown, dielectric strength, arc resistance, moisture absorption, thicknesses, and sheet-size context.
- AGC `TSM-DS3M`: source-scoped military-application-positioned low-loss laminate values, including `10 GHz` Dk / Df, method-dependent TcK rows, thermal conductivity, Td, CTE, dielectric breakdown, dielectric strength, arc resistance, moisture absorption, thicknesses, and sheet-size context.
- AGC `TLX-8`: source-scoped fiberglass-reinforced PTFE microwave-substrate values, including `1 MHz` Dk, `10 GHz` Df, ASTM E 595 outgassing rows, thermal conductivity, Td, CTE, moisture absorption, flammability, copper-cladding, thickness, and sheet-size context.
- AGC `TLY-5`: source-scoped very-low-Dk PTFE laminate values, including `10 GHz` Dk / Df, thermal conductivity, CTE, moisture absorption, NASA outgassing rows, flammability, dimensional stability, thickness, and sheet-size context.

## Still Blocked

- Finished-board insertion loss, RF, mmWave, antenna, radar, phased-array, automotive-radar, satellite, cellular, aerospace, military, avionics, oil-drilling, ATE, passive-component, power-amplifier, LNB / LNA / LNC, Ka / E / W band, or severe-environment performance claims.
- Space qualification, military qualification, OEM drop-in equivalence, registration yield, sequential-lamination success, resistor-foil performance, fastRise stackup success, fusion-bonding comparison claims, or released-lot acceptance.
- Supplier process windows, build capability, stock, price, MOQ, lead time, yield, certification, or production approval.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `five AGC material rows only`
- cumulative P4-33 material PDF source-backed upgrade: `25` AGC exact-product rows plus `5` Rogers exact-product rows plus `13` Ventec exact-product rows plus `4` Shengyi exact-product rows plus `3` TUC exact-product rows
- next lane: remaining AGC TLX / TLY / TLE / TLC / TLF / ELL tail, TUC `TU-865S` after preliminary-revision binding, Ventec product-form-specific rows, or selector wiki aggregation for recovered rows.
