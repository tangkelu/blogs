# P4-33 Material PDF Source Recovery Round 10

Date: 2026-04-28
Status: `source_backed_fact_layer_partial`

## Purpose

Continue the P4-33 material PDF lane by upgrading four additional Ventec local PDF rows after official Ventec page / PDF checks and direct PDF text extraction.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/Ventec-vt-481.pdf`
- `/code/blogs/tmps/materias_pdf/Ventec-vt-463h.pdf`
- `/code/blogs/tmps/materias_pdf/Ventec-vt-6735.pdf`
- `/code/blogs/tmps/materias_pdf/Ventec-vt-770-vt-770lk.pdf`
- `https://www.ventec-group.com/products/lead-free-assembly/vt-481/datasheet/`
- `https://www.ventec-group.com/products/tec-speed-signal-integrity/tec-speed-70h-vt-463h/datasheet/`
- `https://www.ventec-group.com/zh/products/tec-speed-rf/tec-speed-300-vt-6735/datasheet/`
- `https://www.ventec-group.com/media/114485/230622-tec-speed30-vt-6735.pdf`
- `https://www.ventec-group.com/products/tec-pack-ic-packaging/tec-speed-60-h-pk-vt-770-vt-770lk/datasheet/`

## Added Source Records

- `ventec-vt-481-datasheet-page`
- `ventec-vt-463h-datasheet-page`
- `ventec-vt-6735-datasheet`
- `ventec-vt-770-vt-770lk-datasheet-page`

## Added Fact Cards

- `materials-ventec-vt-481`
- `materials-ventec-vt-463h`
- `materials-ventec-vt-6735`
- `materials-ventec-vt-770-vt-770lk`

## Source-Backed Data Unlocked

- Ventec `VT-481`: source-scoped mid-Tg FR-4 / lead-free laminate-prepreg values, including Tg, Td, T260, T288, thermal stress, CTE, expansion, Dk / Df at `1 GHz`, electrical / physical properties, IPC framing, and guarded availability context.
- Ventec `VT-463H`: source-scoped halogen-free high-Tg ultra-low-loss laminate-prepreg values, including Tg by DMA / TMA, Td, T288, thermal stress, CTE, expansion, `RC 55%` Dk / Df rows at `1 GHz` and `10 GHz`, and guarded availability context.
- Ventec `VT-6735`: source-scoped RF / microwave laminate values, including `10 GHz` Dk / Df, `8~40 GHz` design Dk, TCDk, Td, thermal conductivity, CTE, specific heat, peel strength, density, moisture absorption, flammability, and guarded availability context.
- Ventec `VT-770 / VT-770(LK)`: source-scoped paired-product values, including separate `VT-770` and `VT-770(LK)` Dk / Df rows at `1 GHz` and `10 GHz`, Tg, Td, T260 / T288, CTE, moisture absorption, flammability, and guarded availability context.

## Still Blocked

- Finished-board high-speed, satellite, navigation, GPS, LTE, IC-packaging, RF amplifier, coupler, filter, power-divider, telecom, automotive, radar, antenna, insertion-loss, impedance, channel, or protocol-performance claims.
- Lead-free assembly success, CAF lifetime, high-layer reliability, RF thermal performance, qualification, or released-lot acceptance for a specific stackup.
- Supplier press cycles, desmear process windows, packaging / bake schedules, generic lamination recipes, inspection acceptance limits, or build qualification.
- APT / HIL / other supplier material stock, process capability, certification, price, MOQ, lead time, yield, or production approval.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `four Ventec material rows only`
- cumulative P4-33 material PDF source-backed upgrade: `20` AGC exact-product rows plus `5` Rogers exact-product rows plus `6` Ventec exact-product rows plus `4` Shengyi exact-product rows
- next lane: continued official-source recovery for Ventec `VT-464LT`, `VT-464LT RCC`, TUC `TU-872 LK` / `TU-901` / `ThunderClad 4HZ`, AGC TSM / TLX / TLY / TLE / TLC / TLF / RF tails, or selector wiki aggregation for recovered rows.
