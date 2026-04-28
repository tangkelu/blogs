# P4-33 Material PDF Source Recovery Round 15

Date: 2026-04-28
Status: `source_backed_fact_layer_partial`

## Purpose

Continue the AGC tail recovery by upgrading five additional local AGC TLY / TLE / TLC PDFs after official AGC PDF URL checks and direct PDF text extraction with `pypdf`.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/AGC_TLY-3_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_TLY-5A_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_TLY-5Z_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_TLE-95_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_TLC-32_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_TLY-3_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_TLY-5A_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_TLY-5Z_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_TLE-95_TDS.pdf`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_TLC-32_TDS.pdf`

## Added Source Records

- `agc-tly-3-datasheet`
- `agc-tly-5a-datasheet`
- `agc-tly-5z-datasheet`
- `agc-tle-95-datasheet`
- `agc-tlc-32-datasheet`

## Added Fact Cards

- `materials-agc-tly-3`
- `materials-agc-tly-5a`
- `materials-agc-tly-5z`
- `materials-agc-tle-95`
- `materials-agc-tlc-32`

## Source-Backed Data Unlocked

- AGC `TLY-3`: source-scoped very-low-Dk PTFE laminate values, including `10 GHz` Dk / Df, thermal conductivity, CTE, moisture absorption, NASA outgassing rows, flammability, dimensional stability, thickness, and sheet-size context.
- AGC `TLY-5A`: source-scoped very-low-Dk PTFE laminate values, including `10 GHz` Dk / Df, thermal conductivity, CTE, moisture absorption, NASA outgassing rows, dimensional stability, thickness, and sheet-size context.
- AGC `TLY-5Z`: source-scoped PTFE laminate values, including modified-IPC `10 GHz` Dk / Df, thermal conductivity, CTE, specific gravity, moisture absorption, flammability, dimensional-stability rows, thickness, and sheet-size context.
- AGC `TLE-95`: source-scoped microwave / high-speed digital laminate values, including `1 MHz` Dk, modified-IPC `10 GHz` Df, thermal conductivity, CTE, moisture absorption, dielectric breakdown, arc resistance, flammability, thickness, and sheet-size context.
- AGC `TLC-32`: source-scoped microwave laminate values, including `1 MHz` Dk, modified-IPC `10 GHz` Df, thermal conductivity, CTE, arc resistance, flammability, thickness, and sheet-size context.

## Still Blocked

- Finished-board insertion loss, RF, mmWave, antenna, radar, satellite, cellular, aerospace, microwave-radio, passive-component, high-speed-digital, PTH-reliability, SMT-reliability, thermal-cycling, or severe-environment performance claims.
- 77 GHz drop-in equivalence, OEM comparison claims, space qualification, military qualification, released-lot acceptance, or supplier-specific application readiness.
- Supplier process windows, build capability, stock, price, MOQ, lead time, yield, certification, or production approval.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `five AGC material rows only`
- cumulative P4-33 material PDF source-backed upgrade: `30` AGC exact-product rows plus `5` Rogers exact-product rows plus `13` Ventec exact-product rows plus `4` Shengyi exact-product rows plus `3` TUC exact-product rows
- next lane: remaining AGC `ELL` / `TLF-35A` tail, TUC `TU-865S` after preliminary-revision binding, Ventec product-form-specific rows, or selector wiki aggregation for recovered rows.
