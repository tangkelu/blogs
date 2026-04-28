# P4-33 Material PDF Source Recovery Round 11

Date: 2026-04-28
Status: `source_backed_fact_layer_partial`

## Purpose

Continue the P4-33 material PDF lane by upgrading four additional Ventec local PDF rows after official Ventec page checks and direct PDF text extraction.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/Ventec-vt-462s.pdf`
- `/code/blogs/tmps/materias_pdf/Ventec-vt-464gs.pdf`
- `/code/blogs/tmps/materias_pdf/Ventec-vt-90h.pdf`
- `/code/blogs/tmps/materias_pdf/Ventec-vt-4b5h.pdf`
- `https://www.ventec-group.com/zh/products/tec-speed-signal-integrity/tec-speed-60-vt-462s/datasheet/`
- `https://www.ventec-group.com/cht/products/tec-pack-ic-packaging/vt-464gs/datasheet/`
- `https://www.ventec-group.com/products/polyimide/vt-90h/datasheet/`
- `https://www.ventec-group.com/products/tec-thermal-thermal-management-ims/vt-4b5h/datasheet/`

## Added Source Records

- `ventec-vt-462s-datasheet-page`
- `ventec-vt-464gs-datasheet-page`
- `ventec-vt-90h-datasheet-page`
- `ventec-vt-4b5h-datasheet-page`

## Added Fact Cards

- `materials-ventec-vt-462s`
- `materials-ventec-vt-464gs`
- `materials-ventec-vt-90h`
- `materials-ventec-vt-4b5h`

## Source-Backed Data Unlocked

- Ventec `VT-462S`: source-scoped very-low-Dk / very-low-loss laminate-prepreg values, including Tg, Td, T260, T288, thermal stress, CTE, expansion, Dk / Df at `1 GHz` and `10 GHz`, and guarded availability context.
- Ventec `VT-464GS`: source-scoped halogen-free high-Tg IC-packaging laminate-prepreg values, including low-CTE rows, `RC 70%` Dk / Df at `2 GHz` by cavity resonator, and guarded preliminary-version context.
- Ventec `VT-90H`: source-scoped high-Tg polyimide laminate-prepreg values, including Tg, Td, T260, T288, thermal stress, CTE, expansion, `RC 40%` Dk / Df at `1 GHz`, and guarded severe-service application context.
- Ventec `VT-4B5H`: source-scoped IMS metal-base laminate values, including `4.2 W/mK` dielectric thermal conductivity, dielectric-thickness-dependent thermal impedance and breakdown-voltage rows, Tg, Td, Hi-Pot, Dk / Df at `1 MHz`, and guarded availability context.

## Still Blocked

- Finished-board high-speed, RF, satellite, navigation, GPS, LTE, IC-packaging, BGA, CSP, SIP, flip-chip, backplane, military, aerospace, flight-control, downhole, LED, motor-drive, power-module, insertion-loss, impedance, channel, thermal-resistance, junction-temperature, or reliability claims.
- Lead-free assembly success, CAF lifetime, IST result, high-layer-count manufacturability, package reliability, IMS thermal performance, qualification, or released-lot acceptance for a specific stackup.
- Supplier press cycles, desmear process windows, storage / bake schedules, generic lamination recipes, inspection acceptance limits, or build qualification.
- APT / HIL / other supplier material stock, process capability, certification, price, MOQ, lead time, yield, or production approval.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `four Ventec material rows only`
- cumulative P4-33 material PDF source-backed upgrade: `20` AGC exact-product rows plus `5` Rogers exact-product rows plus `10` Ventec exact-product rows plus `4` Shengyi exact-product rows
- next lane: continued official-source recovery for Ventec second-tier rows, TUC official URL binding, AGC TSM / TLX / TLY / TLE / TLC / TLF / RF tails, or selector wiki aggregation for recovered rows.
