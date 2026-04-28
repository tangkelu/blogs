# P4-33 Material PDF Source Recovery Round 6

Date: 2026-04-28
Status: `source_backed_fact_layer_partial`

## Purpose

Continue the P4-33 material PDF lane by upgrading the remaining source-verifiable Shengyi scout rows after official SYTECH English product-page checks.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/Shengyi-mmWaveG-mmWaveGB.pdf`
- `/code/blogs/tmps/materias_pdf/Shengyi-LNB33C.pdf`
- `/code/blogs/tmps/materias_pdf/Shengyi-S1170G-S1170GB.pdf`
- `https://www.syst.com.cn/en/Product/info_257.aspx?itemid=11661`
- `https://www.syst.com.cn/en/Product/info_257.aspx?itemid=11655`
- `https://www.syst.com.cn/en/Product/info_257.aspx?itemid=11617`
- `logs/p4-33-shengyi-material-pdf-extraction-scout-round-4.md`
- `logs/p4-33-shengyi-remaining-official-source-mapping-scout.md`

## Added Source Records

- `shengyi-mmwaveg-product-page`
- `shengyi-lnb33c-product-page`
- `shengyi-s1170g-product-page`

## Added Fact Cards

- `materials-shengyi-mmwaveg`
- `materials-shengyi-lnb33c`
- `materials-shengyi-s1170g`

## Source-Backed Data Unlocked

- Shengyi `mmWave G`: source-scoped Dk / Df rows, `77 GHz` design Dk, CTE, Tg, Td, resistivity, peel strength, water absorption, thermal conductivity, density, and flammability.
- Shengyi `LNB33C`: source-scoped Dk / Df / TCDk rows, PIM test-context row, resistivity, flexural strength, CTE, Tg, Td, thermal conductivity, water absorption, peel strength, and flammability.
- Shengyi `S1170G`: source-scoped Tg, Td, CTE, T260, T288, thermal stress, resistivity, arc resistance, dielectric breakdown, Dk / loss row, peel strength, flexural strength, water absorption, and flammability.

## Still Blocked

- `mmWaveGB`: not promoted as a separate prepreg / bondply fact because the verified product page and fact card are scoped to `mmWave G`.
- `S1170GB`: not promoted as a separate prepreg fact because the verified product page and fact card are scoped to `S1170G`; the local combined PDF's prepreg-side rows still need layout-level source verification before reuse.
- Shengyi processing guidelines, line-up PDFs, SGS, and MSDS links were noted but not absorbed in this round.
- Taconic `RF-35` remains `blocked_pending_official_source`.

## Blocked Claim Classes

- Finished-board PIM, antenna efficiency, base-station, WiMAX, automotive radar, satellite, insertion-loss, impedance, or qualification claims.
- APT / HIL / other supplier material stock, process capability, certification, price, MOQ, lead time, yield, or production approval.
- Any conversion of typical material properties into universal design guarantees or generic family averages.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `three Shengyi product-page-backed material rows only`
- cumulative P4-33 material PDF source-backed upgrade: `7` AGC exact-product rows plus `5` Rogers exact-product rows plus `2` Ventec exact-product rows plus `4` Shengyi exact-product rows
- next lane: selector wiki aggregation for the recovered AGC / Rogers / Ventec / Shengyi rows, or continued official-source recovery for Taconic and the broader material PDF tail.
