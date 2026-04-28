# P4-33 Material PDF Source Recovery Round 5

Date: 2026-04-28
Status: `source_backed_fact_layer_partial`

## Purpose

Continue the P4-33 material PDF lane by upgrading one Shengyi scout row after controller official-source verification and layout-sensitive review.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/Shengyi-AeroWave+300.pdf`
- `https://www.shengyi-usa.com/rf-and-microwave/`
- `https://www.shengyi-usa.com/download/28748/`
- `logs/p4-33-shengyi-material-pdf-extraction-scout-round-4.md`

## Added Source Records

- `shengyi-aerowave-300-datasheet`

## Added Fact Cards

- `materials-shengyi-aerowave-300`

## Source-Backed Data Unlocked

- Shengyi `AeroWave 300` exact-product RF / microwave material context.
- Source-scoped process Dk, design Dk, Df, thermal coefficient of Dk, Tg, Td, CTE, resistivity, peel strength, electrical strength, flexural strength, water absorption, thermal conductivity, flammability, standard thicknesses, panel sizes, and copper-foil context.

## Verification Notes

- The official Shengyi USA RF and Microwave page links `AEROWAVE 300-TDS` at `https://www.shengyi-usa.com/download/28748/` with title `Version en-tds-1901-01-aerowave 300`.
- The official download endpoint returns a PDF with metadata creation / modification timestamp `2019-12-26`.
- The local `tmps` PDF and official download are not byte-identical, but their `EN/CN-TDS-1901-01` property table values match for the promoted rows.
- `Thermal Coefficient of Dk` remains value `50` with direction `Z`, condition `-40~+120 C`, and method `IEC 61189-2-721 (10GHz)`; the source table does not show a unit in the unit column, so no unit was invented in the fact card.

## Still Scout-Only / Blocked Items

- Shengyi `mmWaveG / mmWaveGB`: remains `extraction_scout_only` pending exact official download URL and product-layout verification.
- Shengyi `LNB33C`: remains `extraction_scout_only` pending exact official download URL and product-layout verification.
- Shengyi `S1170G / S1170GB`: remains `extraction_scout_only` pending exact official download URL and layout-level review of the prepreg-side rows.
- Taconic `RF-35`: remains `blocked_pending_official_source`.

## Blocked Claim Classes

- Finished-board PIM, antenna efficiency, base-station qualification, insertion loss, impedance, radar, RF compliance, or application performance.
- APT / HIL / other supplier material stock, process capability, certification, price, MOQ, lead time, yield, or production approval.
- Any conversion of typical material properties into universal design guarantees.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `one Shengyi AeroWave 300 material row only`
- cumulative P4-33 material PDF source-backed upgrade: `7` AGC exact-product rows plus `5` Rogers exact-product rows plus `2` Ventec exact-product rows plus `1` Shengyi exact-product row
- next lane: verify additional Shengyi official download URLs for `mmWaveG`, `LNB33C`, and `S1170G/S1170GB`, or aggregate the recovered AGC / Rogers / Ventec / Shengyi rows into selector wiki pages.
