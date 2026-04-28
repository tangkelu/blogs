# P4-33 Material PDF Source Recovery Round 3

## Purpose

Upgrade the Rogers extraction scout from candidate notes into source-backed exact-product material facts after official Rogers PDF URL verification.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/RO4360G2 High Frequency Laminates Data Sheet.pdf`
- `/code/blogs/tmps/materias_pdf/RO4830 Plus Laminates Data Sheet.pdf`
- `/code/blogs/tmps/materias_pdf/RO4835IND LoPro Laminate Data Sheet.pdf`
- `/code/blogs/tmps/materias_pdf/RT-duroid 6002 Laminate Data Sheet.pdf`
- `/code/blogs/tmps/materias_pdf/RT-duroid 6202 Laminate Data Sheet.pdf`
- `logs/p4-33-rogers-material-pdf-extraction-scout-round-3.md`

## Added Source Records

- `rogers-ro4360g2-datasheet`
- `rogers-ro4830-plus-datasheet`
- `rogers-ro4835ind-lopro-datasheet`
- `rogers-rt-duroid-6002-datasheet`
- `rogers-rt-duroid-6202-datasheet`

## Added Fact Cards

- `materials-rogers-ro4360g2`
- `materials-rogers-ro4830-plus`
- `materials-rogers-ro4835ind-lopro`
- `materials-rogers-rt-duroid-6002`
- `materials-rogers-rt-duroid-6202`

## Source-Backed Data Unlocked

- Rogers `RO4360G2`: high-Dk RO4000-family material parameters with process Dk, design Dk, Df, thermal conductivity, CTE, Tg, Td, T288, moisture absorption, peel strength, and flammability.
- Rogers `RO4830 Plus`: radar-oriented material parameters with `10 GHz` IPC Dk/Df, `77 GHz` design Dk, method-specific insertion-loss context, thermal / mechanical values, and lead-free compatibility.
- Rogers `RO4835IND LoPro`: industrial-radar material parameters with `2.5 GHz`, `10 GHz`, `60 GHz`, and `77 GHz` values kept separate.
- Rogers `RT/duroid 6002`: low-Dk microwave laminate parameters with process Dk, design Dk over `8-40 GHz`, Df, TCDk, thermal / mechanical values, and lead-free compatibility.
- Rogers `RT/duroid 6202`: low-Dk microwave laminate parameters with thickness-dependent Dk handling and core thermal / mechanical values.

## Blocked Claim Classes

- Finished-board insertion loss, antenna behavior, radar performance, channel budget, impedance tolerance, qualification, or product compliance.
- APT / HIL / other supplier capability, material stock, process window, price, MOQ, lead time, yield, or certification claims.
- Any conversion of datasheet material properties into universal design guarantees.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `five Rogers material PDFs only`
- cumulative P4-33 material PDF source-backed upgrade: `7` AGC exact-product rows plus `5` Rogers exact-product rows
- next lane: continue source-backed extraction for Shengyi / Ventec / Taconic candidates or aggregate AGC / Rogers additions into selector wiki pages.
