# P4-33 Material PDF Source Recovery Round 12

Date: 2026-04-28
Status: `source_backed_fact_layer_partial`

## Purpose

Continue the P4-33 material PDF lane by upgrading three additional Ventec FR-4-family local PDF rows after official Ventec page checks and direct PDF text extraction.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/Ventec-vt-441v.pdf`
- `/code/blogs/tmps/materias_pdf/Ventec-vt-441.pdf`
- `/code/blogs/tmps/materias_pdf/Ventec-vt-42.pdf`
- `https://www.ventec-group.com/products/halogen-free/vt-441v/datasheet/`
- `https://www.ventec-group.com/zh/products/halogen-free/vt-441/datasheet/`
- `https://www.ventec-group.com/products/standard-fr4/vt-42/datasheet/`

## Added Source Records

- `ventec-vt-441v-datasheet-page`
- `ventec-vt-441-datasheet-page`
- `ventec-vt-42-datasheet-page`

## Added Fact Cards

- `materials-ventec-vt-441v`
- `materials-ventec-vt-441`
- `materials-ventec-vt-42`

## Source-Backed Data Unlocked

- Ventec `VT-441V`: source-scoped halogen-free mid-Tg FR-4-family values, including Tg, Td, T260, T288, thermal stress, CTE, expansion, `RC 50%` Dk / Df at `1 GHz`, MOT `150 C`, and guarded application / availability context.
- Ventec `VT-441`: source-scoped halogen-free mid-Tg FR4.1 values, including Tg, Td, T260, T288, thermal stress, CTE, expansion, `RC 50%` Dk / Df at `1 GHz`, MOT `130 C`, and guarded application / availability context.
- Ventec `VT-42`: source-scoped dicy-cured standard FR4.0 values, including Tg, Td, T260, T288, thermal stress, CTE, expansion, Dk / Df at `1 GHz`, and guarded application / availability context.

## Still Blocked

- Finished-board automotive, LED, high-power, phone, communication-equipment, LCD, TV, instrumentation, reliability, thermal, SI, impedance, or acceptance claims.
- CAF lifetime, lead-free assembly success, high-layer-count manufacturability, FR-4 default substitution, or released-lot acceptance for a specific stackup.
- Supplier process windows, reverse-treated-copper handling as a generic rule, prepreg storage / retest windows as shop process requirements, or build qualification.
- APT / HIL / other supplier material stock, process capability, certification, price, MOQ, lead time, yield, or production approval.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `three Ventec FR-4-family material rows only`
- cumulative P4-33 material PDF source-backed upgrade: `20` AGC exact-product rows plus `5` Rogers exact-product rows plus `13` Ventec exact-product rows plus `4` Shengyi exact-product rows
- next lane: TUC official URL binding, Ventec product-form-specific rows, AGC TSM / TLX / TLY / TLE / TLC / TLF / RF tails, or selector wiki aggregation for recovered rows.
