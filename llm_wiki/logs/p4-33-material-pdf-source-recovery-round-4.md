# P4-33 Material PDF Source Recovery Round 4

## Purpose

Continue the P4-33 material PDF lane with Ventec rows that could be tied to official Ventec datasheet URLs or pages.

Taconic `RF-35` was inspected locally in this workstream but was not upgraded because a current official source URL was not verified.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/Ventec-vt-901.pdf`
- `/code/blogs/tmps/materias_pdf/Ventec-vt-6880.pdf`
- `/code/blogs/tmps/materias_pdf/Taconic RF-35.pdf`
- `logs/p4-33-shengyi-material-pdf-extraction-scout-round-4.md`

## Added Source Records

- `ventec-vt-901-datasheet-page`
- `ventec-vt-6880-datasheet`

## Added Fact Cards

- `materials-ventec-vt-901`
- `materials-ventec-vt-6880`

## Source-Backed Data Unlocked

- Ventec `VT-901`: high-temperature laminate / prepreg material context with Tg, Td, T260/T288, CTE, expansion, Dk/Df, electrical strength, moisture absorption, flammability, and availability ranges.
- Ventec `VT-6880`: tec-speed 30.0 PTFE / mmWave laminate context with `10 GHz` Dk/Df, `8~40 GHz` design Dk, TCDk, Td, thermal conductivity, CTE, peel strength, density, moisture absorption, flammability, lead-free compatibility, and IPC-4103 slash-sheet framing.

## Scout-Only / Blocked Items

- `Taconic RF-35.pdf`: local old Taconic PDF text is extractable, but no current official Taconic URL was verified in this round; remains `blocked_pending_official_source`.
- Shengyi scout round 4 produced extraction notes for `mmWaveG`, `AeroWave 300`, `LNB33C`, and `S1170G/S1170GB`; at the end of round 4 those rows remained `extraction_scout_only` pending controller official-source verification and layout review. Round 5 later upgraded `AeroWave 300` only.

## Blocked Claim Classes

- Finished-board radar, aerospace, military, flight-control, downhole, burn-in, antenna, insertion-loss, impedance, or qualification claims.
- APT / HIL / other supplier fabrication capability, stock, process window, certification, price, MOQ, lead time, or yield claims.
- Any conversion of typical material properties into universal design guarantees.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `two Ventec material rows only`
- cumulative P4-33 material PDF source-backed upgrade: `7` AGC exact-product rows plus `5` Rogers exact-product rows plus `2` Ventec exact-product rows
- next lane: controller review of Shengyi official-source availability and layout-sensitive values, or selector wiki aggregation for the newly recovered AGC / Rogers / Ventec rows.
