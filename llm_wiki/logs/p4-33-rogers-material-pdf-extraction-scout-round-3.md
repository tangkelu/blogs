# P4-33 Rogers Material PDF Extraction Scout Round 3

Date: 2026-04-28
Lane: `P4-33 Rogers material PDF extraction scout, round 3`
Status: `extraction_scout_only`
Learning State: `not_learned`

## Purpose

Extract local text from five Rogers datasheet PDFs under `/code/blogs/tmps/materias_pdf`, preserve deletion-safe scout notes, and recommend exact future `source_id` and `fact_id` names without creating source records or reusable facts.

## Scope And Guardrails

- Input files inspected:
  - `/code/blogs/tmps/materias_pdf/RO4360G2 High Frequency Laminates Data Sheet.pdf`
  - `/code/blogs/tmps/materias_pdf/RO4830 Plus Laminates Data Sheet.pdf`
  - `/code/blogs/tmps/materias_pdf/RO4835IND LoPro Laminate Data Sheet.pdf`
  - `/code/blogs/tmps/materias_pdf/RT-duroid 6002 Laminate Data Sheet.pdf`
  - `/code/blogs/tmps/materias_pdf/RT-duroid 6202 Laminate Data Sheet.pdf`
- Existing `llm_wiki` coverage checked against `facts/`, `sources/registry/`, and prior `p4-33` logs.
- Local PDFs were treated as candidate primary manufacturer datasheet sources.
- These notes remain scout-only. No source registry entries, fact cards, wiki pages, or tracker updates were created.
- Do not promote any values below into learned facts until controller review confirms source-record and fact-card intake.

## Extraction Method

- `pdftotext` unavailable in workspace.
- Local fallback used: Python `pypdf` text extraction.
- Extraction quality was sufficient to recover product names, revision/publication markers, and the main property tables from all five PDFs.

## Existing Support Check

- Prior candidate-only naming already exists in [p4-33-material-pdf-candidate-inventory-round-2.md](/code/blogs/llm_wiki/logs/p4-33-material-pdf-candidate-inventory-round-2.md).
- Nearby existing learned coverage found for:
  - [rogers-ro4835.md](/code/blogs/llm_wiki/facts/materials/rogers-ro4835.md)
  - [rogers-rt-duroid-5880.md](/code/blogs/llm_wiki/facts/materials/rogers-rt-duroid-5880.md)
- No existing source registry records or learned fact cards were found for the exact five PDFs in this lane.

## Per-PDF Scout Notes

### 1. RO4360G2 High Frequency Laminates Data Sheet

- Local file: `/code/blogs/tmps/materias_pdf/RO4360G2 High Frequency Laminates Data Sheet.pdf`
- Product identity:
  - `RO4360G2`
  - Rogers high frequency laminate
  - text describes it as a glass-reinforced, hydrocarbon ceramic-filled thermoset material in the RO4000 line context
- Visible publication / revision marker:
  - `© 2022 Rogers Corporation`
  - `Revised 1594 080322`
  - `Publication #92-143`
- Recommended future IDs:
  - `source_id: rogers-ro4360g2-datasheet`
  - `fact_id: materials-rogers-ro4360g2`
- Key numeric values captured from extracted table:
  - dielectric constant, process: `6.15 ± 0.15`, direction `Z`, condition `10 GHz / 23°C`, method `IPC-TM-650 2.5.5.5`; sheet also references `2.5 GHz / 23°C` clamped stripline
  - design Dk mentioned in body text: `6.4`
  - dissipation factor: `0.0038`, direction `Z`, condition `10 GHz / 23°C`, method `IPC-TM-650 2.5.5.5`
  - thermal conductivity: `0.75 W/m/K`, condition `50°C`, method `ASTM D-5470`
  - volume resistivity: `4.0 x 10^13 ohm-cm`, condition `Elevated T`, method `IPC-TM-650 2.5.17.1`
  - surface resistivity: `9.0 x 10^12 ohm`, condition `Elevated T`, method `IPC-TM-650 2.5.17.1`
  - electrical strength: `784 V/mil`, direction `Z`, method `IPC-TM-650 2.5.6.2`
  - tensile strength: `131 MPa X`, `97 MPa Y`, condition `40 hrs 50%RH / 23°C`, method `ASTM D638`
  - flexural strength: `213 MPa X`, `145 MPa Y`, condition `40 hrs 50%RH / 23°C`, method `IPC-TM-650 2.4.4`
  - CTE: `13 ppm/°C X`, `14 ppm/°C Y`, `28 ppm/°C Z`, range `-50°C to 288°C`, after replicated heat cycle, method `IPC-TM-650 2.4.41`
  - Tg: `>280°C`, method `IPC-TM-650 2.4.24.3`
  - Td: `407°C`, method `ASTM D3850 using TGA`
  - T288: `>30 min`, condition `30 min / 125°C prebake`, method `IPC-TM-650 2.4.24.1`
  - moisture absorption: `0.08%`, condition `50°C / 48 hr`, methods `IPC-TM-650 2.6.2.1` and `ASTM D570`
  - thermal coefficient of er: `-131 ppm/°C`, direction `Z`, condition `10 GHz`, range `-50°C to 150°C`, method `IPC-TM-650 2.5.5.5`
  - density: `2.16 g/cm3`, condition `RT`, method `ASTM D792`
  - copper peel strength: `5.2 pli (0.91 N/mm)`, condition `Condition B`, method `IPC-TM-650 2.4.8`, note says results based on `1 oz` data
  - flammability: `V-0`, `UL94`
- Extraction confidence: `high`
- Extraction status: `extraction_scout_only`

### 2. RO4830 Plus Laminates Data Sheet

- Local file: `/code/blogs/tmps/materias_pdf/RO4830 Plus Laminates Data Sheet.pdf`
- Product identity:
  - `RO4830 Plus`
  - Rogers thermoset laminate / circuit material
  - body text positions it for `76-81 GHz` automotive radar and FR-4 cap-layer use
- Visible publication / revision marker:
  - `©2025 Rogers Corporation`
  - `Issued 1422 101325`
  - `Publication #92-217`
- Recommended future IDs:
  - `source_id: rogers-ro4830-plus-datasheet`
  - `fact_id: materials-rogers-ro4830-plus`
- Key numeric values captured from extracted table:
  - dielectric constant: `3.00 ± 0.04`, condition `23°C @ 50% RH`, frequency `10 GHz`, method `IPC TM-650 2.5.5.5`
  - dissipation factor: `0.0015`, condition `23°C @ 50% RH`, frequency `10 GHz`, method `IPC TM-650 2.5.5.5`
  - dielectric constant, design: `3.03`, condition `C-24/23/50`, frequency `77 GHz`, method `Microstrip Differential Phase Length`
  - body text insertion loss note: `1.5 dB/inch` for `5 mil` laminates, measured by `microstrip differential phase length method`
  - thermal coefficient of dielectric constant: `-54 ppm/°C`, range `-50°C to 150°C`, frequency `10 GHz`, method `IPC TM-650 2.5.5.5`
  - volume resistivity: `1.1 x 10^13 Mohm-cm`, condition `C-96/35/90`, method `IPC TM-650 2.5.17.1`
  - surface resistivity: `4.1 x 10^11 Mohm`, condition `C-96/35/90`, method `IPC TM-650 2.5.17.1`
  - Td: `357°C`, method `TGA`, `ASTM D3850`
  - CTE: `46 ppm/°C X`, `47 ppm/°C Y`, `56 ppm/°C Z`, range `-40°C to 140°C`, method `IPC TM-650 2.4.41`
  - thermal conductivity: `0.5 W/(m.K)`, direction `z`, method `ASTM D5470`
  - Tg: `285°C`, method `DMA`
  - copper peel strength after thermal stress: `4.5 lbs/in`, `18 μm foil`, condition `After Solder Float`, method `IPC TM-650 2.4.8`
  - tensile modulus: `540 ksi X`, `580 ksi Y`, condition `23°C`, method `ASTM D638`
  - flexural modulus: `340 ksi X`, `340 ksi Y`, condition `23°C`, method `IPC-TM-650 2.4.4`
  - dimensional stability: `-0.67 mm/m X`, `-0.68 mm/m Y`, condition `Method C`, method `IPC-TM-650 2.2.4`
  - flammability: `V-0`, `UL 94`
  - moisture absorption: `0.02%`, condition `D48/50`, method `IPC TM-650 2.6.2.1`
  - density: `1.64 g/cm³`, condition `C-24/23/50`, method `ASTM D792`
  - lead-free process compatible: `YES`
- Extraction confidence: `high`
- Extraction status: `extraction_scout_only`

### 3. RO4835IND LoPro Laminate Data Sheet

- Local file: `/code/blogs/tmps/materias_pdf/RO4835IND LoPro Laminate Data Sheet.pdf`
- Product identity:
  - `RO4835IND LoPro`
  - Rogers high frequency circuit material
  - body text positions it for `60-81 GHz` short-range industrial radar
- Visible publication / revision marker:
  - `© 2022 Rogers Corporation`
  - `Revised 1599 080422`
  - `Publication #92-206`
- Recommended future IDs:
  - `source_id: rogers-ro4835ind-lopro-datasheet`
  - `fact_id: materials-rogers-ro4835ind-lopro`
- Key numeric values captured from extracted table:
  - dielectric constant, process: `3.48 ± 0.05`, direction `Z`, condition `10 GHz / 23°C`, method `IPC-TM-650 2.5.5.5`, note says clamped stripline
  - dissipation factor: `0.0037` at `10 GHz / 23°C`, direction `Z`, method `IPC-TM-650 2.5.5.5`
  - dissipation factor: `0.0031` at `2.5 GHz / 23°C`, direction `Z`, method `IPC-TM-650 2.5.5.5`
  - design dielectric constant: `3.49` at `77 GHz`, method `Microstrip differential phase length`
  - transmission line loss: `2.75 dB/in` at `77 GHz`, method `Microstrip differential phase length`
  - design dielectric constant: `3.48` at `60 GHz`, method `Microstrip differential phase length`
  - transmission line loss: `2.13 dB/in` at `60 GHz`, method `Microstrip differential phase length`
  - dimensional stability: `<0.5 mm/m`, direction `X,Y`, condition `after etch +E2/150°C`, method `IPC-TM-650 2.4.39A`
  - Tg: `>280°C`, method `IPC-TM-650 2.4.24.3`
  - Td: `390°C`, method `TGA`, `ASTM D3850`
  - moisture absorption: `0.05%`, condition `48 hrs immersion`, `0.060 inch sample`, `50°C`, method `ASTM D570`
  - copper peel strength: `0.88 N/mm (5.0 pli)`, condition `after solder float`, `1 oz EDC foil`, method `IPC-TM-650 2.4.8`
  - flammability: `V-0`, `UL 94`
  - lead-free process compatible: `Yes`
  - standard thickness called out in offering table: `0.0040 inch (0.102 mm) ± 0.0007 inch`
- Extraction confidence: `high`
- Extraction status: `extraction_scout_only`

### 4. RT-duroid 6002 Laminate Data Sheet

- Local file: `/code/blogs/tmps/materias_pdf/RT-duroid 6002 Laminate Data Sheet.pdf`
- Product identity:
  - `RT/duroid 6002`
  - Rogers high frequency laminate / microwave material
  - body text frames it as low-loss, low-dielectric-constant laminate for mechanically reliable and electrically stable microwave structures
- Visible publication / revision marker:
  - `©2022 Rogers Corporation`
  - `Revised 1605 080822`
  - `Publication #92-102`
- Recommended future IDs:
  - `source_id: rogers-rt-duroid-6002-datasheet`
  - `fact_id: materials-rogers-rt-duroid-6002`
- Key numeric values captured from extracted table:
  - dielectric constant, process: `2.94 ± 0.04`, direction `Z`, condition `10 GHz / 23°C`, method `IPC-TM-650 2.5.5.5`
  - dielectric constant, design: `2.94`, range `8 GHz-40 GHz`, method `Differential Phase Length Method`
  - dissipation factor: `0.0012`, direction `Z`, condition `10 GHz / 23°C`, method `IPC-TM-650 2.5.5.5`
  - thermal coefficient of er: `+12 ppm/°C`, direction `Z`, condition `10 GHz`, range `0-100°C`, method `IPC-TM-650 2.5.5.5`
  - volume resistivity: `10^6 Mohm cm`, direction `Z`, condition `A`, method `ASTM D257`
  - surface resistivity: `10^7 Mohm`, direction `Z`, condition `A`, method `ASTM D257`
  - tensile modulus: `828 MPa (120 kpsi)`, direction `X,Y`, condition `23°C`, method `ASTM D638`
  - ultimate stress: `6.9 MPa (1.0 kpsi)`, direction `X,Y`
  - ultimate strain: `7.3%`, direction `X,Y`
  - compressive modulus: `2482 MPa (360 kpsi)`, direction `Z`, method `ASTM D638`
  - moisture absorption: `0.02%`, condition `D48/50`, methods `IPC-TM-650 2.6.2.1` and `ASTM D570`
  - thermal conductivity: `0.60 W/m/K`, condition `80°C`, method `ASTM C518`
  - CTE: `16 ppm/°C X`, `16 ppm/°C Y`, `24 ppm/°C Z`, range `-55 to 288°C`, condition `23°C / 50% RH`, method `IPC-TM-650 2.4.41`
  - Td: `500°C`, method `TGA`, `ASTM D3850`
  - density: `2.1 g/cm3`, method `ASTM D792`
  - specific heat: `0.93 J/g/K (0.22 BTU/lb/°F)`, method `Calculated`
  - copper peel: `8.9 lbs/in (1.6 N/mm)`, method `IPC-TM-650 2.4.8`
  - flammability: `V-0`, `UL94`
  - lead-free process compatible: `YES`
- Extraction confidence: `high`
- Extraction status: `extraction_scout_only`

### 5. RT-duroid 6202 Laminate Data Sheet

- Local file: `/code/blogs/tmps/materias_pdf/RT-duroid 6202 Laminate Data Sheet.pdf`
- Product identity:
  - `RT/duroid 6202`
  - Rogers high frequency laminate / circuit material
  - body text frames it as low-loss, low-dielectric-constant laminate with limited woven-glass reinforcement for dimensional stability
- Visible publication / revision marker:
  - `© 2022 Rogers Corporation`
  - `Revised 1616 090922`
  - `Publication# 92-116`
- Recommended future IDs:
  - `source_id: rogers-rt-duroid-6202-datasheet`
  - `fact_id: materials-rogers-rt-duroid-6202`
- Key numeric values captured from extracted table:
  - dielectric constant: `2.94 ± 0.04`, direction `Z`, condition `10 GHz / 23°C`, method `IPC-TM-650 2.5.5.5`
  - thickness-dependent dielectric-constant note:
    - `0.005 inch` laminates: `3.06 ± 0.04`
    - `0.010 inch` and `0.015 inch` laminates: `3.02 ± 0.04`
    - `>=0.020 inch` laminates: `2.94 ± 0.04`
  - dissipation factor: `0.0015`, direction `Z`, condition `10 GHz / 23°C`, method `IPC-TM-650 2.5.5.5`
  - thermal coefficient of er: `+5 ppm/°C`, direction `Z`, condition `10 GHz`, range `-50 to +150°C`, method `IPC-TM-650 2.5.5.5`
  - volume resistivity: `10^6 Mohm cm`, direction `Z`, condition `A`, method `ASTM D257`
  - surface resistivity: `10^9 Mohm`, direction `Z`, condition `A`, method `ASTM D257`
  - tensile modulus: `1007 MPa (146 kpsi)`, direction `X,Y`, condition `23°C`, method `ASTM D638`
  - ultimate stress: `30 MPa (4.3 kpsi)`, direction `X,Y`
  - ultimate strain: `4.9%`, direction `X,Y`
  - compressive modulus: `1035 MPa (150 kpsi)`, direction `Z`, method `ASTM D638`
  - moisture absorption: `0.04%`, conditions `D23/24` and `D48/50`, methods `IPC-TM-650 2.6.2.1` and `ASTM D570`
  - thermal conductivity: `0.68 W/m/K`, condition `80°C`, method `ASTM C518`
  - CTE: `15 ppm/°C X`, `15 ppm/°C Y`, `30 ppm/°C Z`, range `-55 to 288°C`, condition `23°C / 50% RH`, method `IPC-TM-650 2.4.41`
  - dimensional stability: `0.07 mm/m`, direction `X,Y`, condition `after etch +E/150`, method `IPC-TM-650 2.4.3.9`
  - Td: `500°C`, method `TGA`, `ASTM D3850`
  - density: `2.1 g/cm3`, method `ASTM D792`
  - specific heat: `0.93 J/g/K (0.22 BTU/lb/°F)`, method `Calculated`
  - copper peel: `9.1 lbs/in (1.6 N/mm)`, method `IPC-TM-650 2.4.8`
  - flammability: `V-0`, `UL 94`
  - lead-free process compatible: `YES`
- Extraction confidence: `high`
- Extraction status: `extraction_scout_only`

## Recommended Future ID Set

| PDF | Recommended `source_id` | Recommended `fact_id` | Notes |
| --- | --- | --- | --- |
| `RO4360G2 High Frequency Laminates Data Sheet.pdf` | `rogers-ro4360g2-datasheet` | `materials-rogers-ro4360g2` | Matches prior round-2 candidate naming and existing materials-card style |
| `RO4830 Plus Laminates Data Sheet.pdf` | `rogers-ro4830-plus-datasheet` | `materials-rogers-ro4830-plus` | Keep `plus` in slug to separate from base `RO4830` naming if it appears later |
| `RO4835IND LoPro Laminate Data Sheet.pdf` | `rogers-ro4835ind-lopro-datasheet` | `materials-rogers-ro4835ind-lopro` | Keep exact `IND` and `LoPro` product identity |
| `RT-duroid 6002 Laminate Data Sheet.pdf` | `rogers-rt-duroid-6002-datasheet` | `materials-rogers-rt-duroid-6002` | Aligns with existing `rt-duroid` materials naming |
| `RT-duroid 6202 Laminate Data Sheet.pdf` | `rogers-rt-duroid-6202-datasheet` | `materials-rogers-rt-duroid-6202` | Aligns with existing `rt-duroid` materials naming |

## Confidence Summary

| PDF | Extraction confidence | Reason |
| --- | --- | --- |
| `RO4360G2 High Frequency Laminates Data Sheet.pdf` | `high` | full property table and revision marker extracted cleanly |
| `RO4830 Plus Laminates Data Sheet.pdf` | `high` | full standard properties table and issue marker extracted cleanly |
| `RO4835IND LoPro Laminate Data Sheet.pdf` | `high` | full property table and revision marker extracted cleanly |
| `RT-duroid 6002 Laminate Data Sheet.pdf` | `high` | full property table and revision marker extracted cleanly |
| `RT-duroid 6202 Laminate Data Sheet.pdf` | `high` | full property table and revision marker extracted cleanly |

## Blockers And Cautions

- `pdftotext` is unavailable in this workspace, so extraction used `pypdf` rather than the preferred CLI path.
- Some extracted formatting is flattened, so unit strings and nearby conditions should be rechecked against the original PDF layout before any fact-card publication.
- Several application statements appear in body copy, but this scout deliberately does not elevate them into learned application-readiness claims.
- No official URL verification was performed in this lane because the task was limited to local PDF extraction scout notes.

## Disposition

- All five PDFs: `extraction_scout_only`
- Learned status: `not_learned`
- Controller action still required before any source record or fact-card creation

## Controller Integration Note

After this extraction scout, the controller verified official Rogers PDF URLs for all five rows and upgraded them into source-backed records and fact cards:

- `RO4360G2 High Frequency Laminates Data Sheet.pdf` -> `rogers-ro4360g2-datasheet` / `materials-rogers-ro4360g2`
- `RO4830 Plus Laminates Data Sheet.pdf` -> `rogers-ro4830-plus-datasheet` / `materials-rogers-ro4830-plus`
- `RO4835IND LoPro Laminate Data Sheet.pdf` -> `rogers-ro4835ind-lopro-datasheet` / `materials-rogers-ro4835ind-lopro`
- `RT-duroid 6002 Laminate Data Sheet.pdf` -> `rogers-rt-duroid-6002-datasheet` / `materials-rogers-rt-duroid-6002`
- `RT-duroid 6202 Laminate Data Sheet.pdf` -> `rogers-rt-duroid-6202-datasheet` / `materials-rogers-rt-duroid-6202`

Those five rows are no longer merely extraction-scout notes. See `logs/p4-33-material-pdf-source-recovery-round-3.md` for the source-backed upgrade scope and remaining blocked claim classes.
