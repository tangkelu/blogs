# P4-33 Shengyi Material PDF Extraction Scout Round 4

Date: 2026-04-28
Lane: `P4-33 Shengyi material PDF extraction scout, round 4`
Status: `extraction_scout_only`
Learning State: `not_learned`

## Purpose

Extract local text from four Shengyi datasheet PDFs under `/code/blogs/tmps/materias_pdf`, preserve deletion-safe scout notes, and recommend exact future `source_id` and `fact_id` names without creating source records or reusable facts.

## Scope And Guardrails

- Input files inspected:
  - `/code/blogs/tmps/materias_pdf/Shengyi-mmWaveG-mmWaveGB.pdf`
  - `/code/blogs/tmps/materias_pdf/Shengyi-AeroWave+300.pdf`
  - `/code/blogs/tmps/materias_pdf/Shengyi-LNB33C.pdf`
  - `/code/blogs/tmps/materias_pdf/Shengyi-S1170G-S1170GB.pdf`
- Existing `llm_wiki` coverage checked against prior `p4-33` logs and nearby `facts/materials` naming.
- Local PDFs were treated as candidate primary manufacturer datasheet sources.
- These notes remain scout-only. No source registry entries, fact cards, wiki pages, or tracker updates were created.
- Do not promote any values below into learned facts until controller review confirms source-record and fact-card intake.

## Extraction Method

- `pdftotext` unavailable in workspace.
- Local fallback used: Python `pypdf` and `fitz` text extraction.
- `fitz` was required for `Shengyi-AeroWave+300.pdf` and `Shengyi-S1170G-S1170GB.pdf` because `pypdf` flattened or garbled parts of the tables.

## Existing Support Check

- Prior candidate-only naming already exists in [p4-33-material-pdf-candidate-inventory-round-2.md](/code/blogs/llm_wiki/logs/p4-33-material-pdf-candidate-inventory-round-2.md).
- Nearby existing learned coverage found for:
  - [shengyi-s1000-2.md](/code/blogs/llm_wiki/facts/materials/shengyi-s1000-2.md)
  - [shengyi-s1000-2m.md](/code/blogs/llm_wiki/facts/materials/shengyi-s1000-2m.md)
  - [shengyi-s1150g.md](/code/blogs/llm_wiki/facts/materials/shengyi-s1150g.md)
- No existing source registry records or learned fact cards were found for the exact four PDFs in this lane.

## Per-PDF Scout Notes

### 1. Shengyi-mmWaveG-mmWaveGB.pdf

- Local file: `/code/blogs/tmps/materias_pdf/Shengyi-mmWaveG-mmWaveGB.pdf`
- Product identity:
  - `mmWave G`
  - combined PDF title string: `mmWaveG-mmWaveGB`
  - body text frames it as `MMW, low loss, glass reinforced PCB base material`
  - second-page product specification explicitly lists `mmWave G`; the companion `mmWaveGB` appears in the document code / filename but not as a separately parameterized table on the extracted pages
- Visible publication / revision marker:
  - document code `CN-TDS-2307-03-mmWaveG-mmWaveGB`
  - PDF metadata creation and modification timestamp: `2023-07-27`
- Recommended future IDs:
  - primary `source_id: shengyi-mmwaveg-datasheet`
  - primary `fact_id: materials-shengyi-mmwaveg`
  - optional companion fact candidate if controller later splits the combined PDF by product role: `materials-shengyi-mmwavegb`
- Key numeric values captured from extracted table:
  - dielectric constant: `3.00`, condition `10GHz/23C`, direction `Z`, method `Balanced Type Circular Disk Resonator`
  - dielectric constant: `3.16`, condition `10GHz/23C`, direction `Z`, method `IPC-TM-650 2.5.5.15`
  - dielectric constant, design Dk: `3.18`, condition `77GHz/23C`, direction `Z`, method `Resonator Ring`
  - dissipation factor: `0.002`, condition `10GHz/23C`, direction `Z`, method `Balanced Type Circular Disk Resonator`
  - dissipation factor: `0.002`, condition `10GHz/23C`, direction `Z`, method `IPC-TM-650 2.5.5.15`
  - Tg: `200 C`, method `IPC-TM-650 2.4.24.4 DMA`
  - Td: `395 C`, method `ASTM D3850 TGA`
  - CTE: `20 ppm/C X`, `20 ppm/C Y`, `40 ppm/C Z`, range `50C-150C`, condition `25C, 50%RH`, method `IPC-TM-650 2.4.41 TMA`
  - volume resistivity: `1.32 x 10^11 MOhm-cm`, condition `A`, method `IPC-TM-650 2.5.17.1`
  - surface resistivity: `1.04 x 10^11 MOhm`, condition `A`, method `IPC-TM-650 2.5.17.1`
  - peel strength: `0.60 N/mm [3.73 lb/in]`, condition `after solder float`, foil `Hoz HVLP foil`, method `IPC-TM-650 2.4.8`
  - water absorption: `0.06%`, method `IPC-TM-650 2.6.2.1`
  - thermal conductivity: `0.40 W/m.K`, condition `50C`, direction `Z`, method `ASTM D5470`
  - density: `1.52 g/cm3`, condition `A`, method `ASTM D792`
  - flammability: `V-0`, method `UL94`
- Extraction confidence: `medium`
- Extraction status: `extraction_scout_only`
- Notes:
  - extracted text layer is clean for the main table
  - the filename and doc code include `mmWaveGB`, but the extracted pages do not expose a separate prepreg/bondply property table, so only the laminate-side `mmWave G` values are safely captured here

### 2. Shengyi-AeroWave+300.pdf

- Local file: `/code/blogs/tmps/materias_pdf/Shengyi-AeroWave+300.pdf`
- Product identity:
  - `AeroWave 300`
  - body text frames it as `High Frequency, Low Loss Material for RF PCB`
- Visible publication / revision marker:
  - document code `CN-TDS-1901-01-AeroWave 300`
  - PDF metadata creation and modification timestamp: `2019-06-26`
- Recommended future IDs:
  - `source_id: shengyi-aerowave-300-datasheet`
  - `fact_id: materials-shengyi-aerowave-300`
- Key numeric values captured from extracted table:
  - dielectric constant, process Dk: `3.0 +/- 0.05`, condition `10GHz/23C`, direction `Z`, method `IPC-TM-650 2.5.5.5 Clamped Stripline`
  - dielectric constant, design Dk: `2.98`, condition `1.5 GHz-6GHz/23C`, direction `Z`, method `Differential Phase Length Method`
  - dissipation factor: `0.0031`, condition `10GHz/23C`, direction `Z`, method `IPC-TM-650 2.5.5.5 Clamped Stripline`
  - thermal coefficient of Dk: `50`, range `-40 to +120C`, direction `Z`, method `IEC 61189-2-721 (10GHz)`
  - Tg: `200 C`, method `IPC-TM-650 2.4.24.4 DMA`
  - Td: `400 C`, method `ASTM D3850 TGA`
  - CTE: `15 ppm/C X`, `15 ppm/C Y`, `50 ppm/C Z`, method `IPC-TM-650 2.4.41 TMA`
  - volume resistivity: `2.21 x 10^8 MOhm-cm`, condition `COND A`, method `IPC-TM-650 2.5.17.1`
  - surface resistivity: `6.84 x 10^7 MOhm`, condition `COND A`, method `IPC-TM-650 2.5.17.1`
  - peel strength: `0.85 N/mm`, condition `after solder float`, foil `1 oz HVLP foil`, method `IPC-TM-650 2.4.8`
  - electrical strength: `60 kV/mm`, condition `0.508mm (0.020 inch)`, direction `Z`, method `IPC-TM-650 2.5.6.2`
  - flexural strength: `232/216 MPa`, direction `ALW/CW`, method `IPC-TM-650 2.4.4A`
  - water absorption: `0.15%`, method `IPC-TM-650 2.6.2.1`
  - thermal conductivity: `0.46 W/m.K`, condition `100C`, method `ASTM D5470`
  - flammability: `V-0`, method `UL94`
- Extraction confidence: `high`
- Extraction status: `extraction_scout_only`
- Notes:
  - `pypdf` output was too degraded for safe table capture; `fitz` recovered a usable text layer
  - the extracted thermal-coefficient row does not show a visible unit label beyond the numeric `50`, so confirm the exact unit rendering against the PDF before any fact-card intake

### 3. Shengyi-LNB33C.pdf

- Local file: `/code/blogs/tmps/materias_pdf/Shengyi-LNB33C.pdf`
- Product identity:
  - `LNB33C`
  - body text frames it as `High Frequency Antenna Grade Circuit Materials`
- Visible publication / revision marker:
  - document code `CN-TDS-2210-01-LNB33C`
  - PDF metadata creation and modification timestamp: `2022-10-11`
- Recommended future IDs:
  - `source_id: shengyi-lnb33c-datasheet`
  - `fact_id: materials-shengyi-lnb33c`
- Key numeric values captured from extracted table:
  - dielectric constant, Dk: `3.30 +/- 0.05`, condition `C-24/23/50, 10GHz`, direction `Z`, method `IPC-TM-650 2.5.5.5`
  - dielectric constant, Dk: `3.56 +/- 0.05`, condition `C-24/23/50, 10GHz`, direction `X/Y`, method `IPC-TM-650 2.5.5.15`
  - dissipation factor, Df: `0.0030`, condition `C-24/23/50, 10GHz`, direction `X/Y`, method `IPC-TM-650 2.5.5.15`
  - thermal coefficient of Dk: `+50 ppm/C`, range `-55C to 85C`, direction `Z`, method `IPC-TM-650 2.5.5.5`
  - PIM: `-158 dBc`, condition `43dBm, 1900MHz, 50 ohm, 0.0307 inch`
  - volume resistivity: `6.8 x 10^8 MOhm-cm`, condition `COND A`, method `IPC-TM-650 2.5.17.1`
  - surface resistivity: `5.3 x 10^7 MOhm`, condition `COND A`, method `IPC-TM-650 2.5.17.1`
  - flexural strength: `200/160 MPa`, direction `X/Y`, condition `R.T.`, method `IPC-TM-650 2.4.4`
  - CTE: `30 ppm/C Z`, range `50-260C`, method `IPC-TM-650 2.4.24`
  - CTE: `12/12 ppm/C X/Y`, range `50-260C`, method `IPC-TM-650 2.4.41`
  - Tg: `>280 C`, method `IPC-TM-650 2.4.25 DSC`
  - Td: `400 C`, condition `TGA (5% wt. loss)`, method `IPC-TM-650 2.4.24.6`
  - thermal conductivity: `0.65 W/(m.K)`, condition `50C`, direction `Z`, method `ASTM D5470`
  - water absorption: `0.05%`, condition `D-24/23`, method `IPC-TM-650 2.6.2.1`
  - peel strength: `1.05 N/mm [6.0 lb/in]`, condition `1 oz HVLP, 288C/10s`, method `IPC-TM-650 2.4.8`
  - flammability: `V-0`, condition `C-48/23/50`, method `UL94`
- Extraction confidence: `high`
- Extraction status: `extraction_scout_only`
- Notes:
  - remarks state typical values are based on `0.780mm (0.0307 inch)` thickness specimen
  - application bullets were present but remain non-learned scout context only

### 4. Shengyi-S1170G-S1170GB.pdf

- Local file: `/code/blogs/tmps/materias_pdf/Shengyi-S1170G-S1170GB.pdf`
- Product identity:
  - `S1170G`
  - `S1170GB`
  - page 1 is the laminate `S1170G` property sheet
  - page 2 is `S1170GB` prepreg purchasing / storage / prepreg-parameter information rather than a full mirrored laminate property table
- Visible publication / revision marker:
  - document code `CN-TDS-2203-03-S1170G-S1170GB`
  - PDF metadata creation and modification timestamp: `2022-03-10`
- Recommended future IDs:
  - primary `source_id: shengyi-s1170g-datasheet`
  - primary `fact_id: materials-shengyi-s1170g`
  - companion fact candidate if controller later splits the prepreg side into its own source-scoped card: `materials-shengyi-s1170gb`
- Key numeric values captured from extracted table:
  - Tg: `175 C`, method `IPC-TM-650 2.4.25D DSC`
  - Tg: `180 C`, method `IPC-TM-650 2.4.24.4 DMA`
  - Td: `390 C`, condition `TGA (5% W.L)`, method `IPC-TM-650 2.4.24.6`
  - T288: `60 min`, method `IPC-TM-650 2.4.24.1 TMA`
  - T260: `>60 min`, method `IPC-TM-650 2.4.24.1 TMA`
  - thermal stress: `>100 s`, condition `288C, solder dips`, method `IPC-TM-650 2.4.13.1`
  - CTE, Z-axis: `45 ppm/C before Tg`, method `IPC-TM-650 2.4.24`
  - CTE, Z-axis: `210 ppm/C after Tg`, method `IPC-TM-650 2.4.24`
  - CTE, Z-axis expansion: `2.3%`, range `50-260C`, method `IPC-TM-650 2.4.24`
  - permittivity: `4.4`, condition `C-24/23/50`, frequency `1GHz`, method `IPC-TM-650 2.5.5.9`
  - loss tangent: `0.010`, condition `C-24/23/50`, frequency `1GHz`, method `IPC-TM-650 2.5.5.9`
  - volume resistivity: `5.65 x 10^7 MOhm-cm`, condition `C-96/35/90`, method `IPC-TM-650 2.5.17.1`
  - surface resistivity: `5.99 x 10^6 MOhm`, condition `C-96/35/90`, method `IPC-TM-650 2.5.17.1`
  - arc resistance: `180 s`, condition `D-48/50 + D-0.5/23`, method `IPC-TM-650 2.5.1`
  - dielectric breakdown: `>45 kV`, condition `D-48/50 + D-0.5/23`, method `IPC-TM-650 2.5.6`
  - peel strength: `1.3 N/mm [7.43 lb/in]`, condition `1 oz, 288C/10s`, method `IPC-TM-650 2.4.8`
  - flexural strength: `550/450 MPa`, direction `LW/CW`, method `IPC-TM-650 2.4.4A`
  - water absorption: `0.12%`, condition `D-24/23`, method `IPC-TM-650 2.6.2.1`
  - flammability: `V-0`, condition `C-48/23/50`, method `UL94`
  - halogen content: `Br <= 900 ppm`, `Cl <= 900 ppm`, `Br + Cl <= 1500 ppm`, method `EN 14582`
  - prepreg cured-thickness rows present on page 2:
    - `1067`, resin content `72%`, cured thickness `0.053 mm`
    - `7628`, resin content `43%`, cured thickness `0.193 mm`
    - additional intermediate glass-style rows are present in extraction but should be rechecked against PDF layout before any structured fact intake
  - prepreg storage conditions present on page 2:
    - `3 months` when stored at `<23C` and `<50% RH`
    - `6 months` when stored at `<5C`
- Extraction confidence: `medium`
- Extraction status: `extraction_scout_only`
- Notes:
  - `fitz` recovered the laminate table cleanly enough for scouting, but page-2 prepreg rows are densely flattened
  - safe scout capture exists for a subset of `S1170GB` prepreg data, but any reusable prepreg parameter card would require layout-level verification against the original PDF

## Recommended Future ID Set

| PDF | Recommended `source_id` | Recommended `fact_id` | Notes |
| --- | --- | --- | --- |
| `Shengyi-mmWaveG-mmWaveGB.pdf` | `shengyi-mmwaveg-datasheet` | `materials-shengyi-mmwaveg` | Matches prior round-2 candidate naming; combined filename suggests optional future companion `materials-shengyi-mmwavegb` if the controller splits laminate vs GB role |
| `Shengyi-AeroWave+300.pdf` | `shengyi-aerowave-300-datasheet` | `materials-shengyi-aerowave-300` | Matches prior round-2 candidate naming |
| `Shengyi-LNB33C.pdf` | `shengyi-lnb33c-datasheet` | `materials-shengyi-lnb33c` | Matches prior round-2 candidate naming |
| `Shengyi-S1170G-S1170GB.pdf` | `shengyi-s1170g-datasheet` | `materials-shengyi-s1170g` | Matches prior round-2 candidate naming; combined PDF also suggests optional future companion `materials-shengyi-s1170gb` for prepreg-specific intake |

## Confidence Summary

| PDF | Extraction confidence | Reason |
| --- | --- | --- |
| `Shengyi-mmWaveG-mmWaveGB.pdf` | `medium` | main table extracted cleanly, but the `mmWaveGB` companion identity is not separately parameterized in extracted pages |
| `Shengyi-AeroWave+300.pdf` | `high` | `fitz` recovered a usable full table and product specification page |
| `Shengyi-LNB33C.pdf` | `high` | full property table and product specification page extracted cleanly |
| `Shengyi-S1170G-S1170GB.pdf` | `medium` | laminate table extracted well, but prepreg page is flattened and only partially safe for structured capture |

## Blockers And Cautions

- `pdftotext` is unavailable in this workspace, so extraction used Python PDF libraries rather than the preferred CLI path.
- `Shengyi-AeroWave+300.pdf` and `Shengyi-S1170G-S1170GB.pdf` needed `fitz` because `pypdf` text extraction was incomplete or garbled.
- Combined-product PDFs (`mmWaveG/mmWaveGB`, `S1170G/S1170GB`) do not expose equally structured data for both product identities in the extracted text, so companion `GB` recommendations remain tentative scout notes only.
- Some units and row boundaries are flattened by extraction, especially on the `S1170GB` prepreg page; verify against the original PDF layout before any source record or fact-card publication.
- Application bullets, anti-CAF wording, lead-free compatibility wording, and similar qualitative claims were not promoted into learned facts in this lane.

## Disposition

- All four PDFs: `extraction_scout_only`
- Learned status: `not_learned`
- Controller action still required before any source record or fact-card creation
