# P4-33 Material PDF Source-Backed Recovery Candidate Inventory Round 2

Date: 2026-04-28
Status: `candidate_inventory_only`
Learning State: `not_learned`

## Purpose

Create a deletion-safe inventory of local material PDFs in `/code/blogs/tmps/materias_pdf`, then identify the highest-value source-backed recovery candidates for future official-source intake.

This log does not create facts, source records, or wiki pages. It does not promote draft-originated or filename-only numeric, capability, certification, price, lead-time, MOQ, yield, quality, or application-readiness claims into reusable knowledge.

## Scope And Method

- Input directory inspected: `/code/blogs/tmps/materias_pdf`
- Existing `llm_wiki` coverage checked against `facts/materials/`, `wiki/materials/`, and related logs
- Local PDFs were treated as potential primary manufacturer datasheet sources
- Current blocker: `pdftotext` is not available in this workspace, so this pass is filename-backed and family-backed rather than full text extracted

## High-Level PDF Inventory By Vendor / Family

### AGC

- `METEORWAVE` family: `1000`, `1000NF`, `2000`, `3000`, `4000`, `4000M`, `8000`, `8300`, `M1`
- `N4000` family: `N4000-13`, `N4000-13EP`, `N4000-13EPSI`, `N4000-13SI`, `N4000-29`, `N4000-29NF`
- `N7000` family: `N7000-2HT`, `N7000-3`, `N7000-3F`
- RF / PTFE / thermoset family: `RF-10`, `RF-30A`, `RF-35HTC`, `RF-35TC`, `RF-60TC`, `NF-30`, `ELL`, `TSM-DS3`, `TSM-DS3b`, `TSM-DS3M`, `TLE-95`, `TLC-32`, `TLF-35A`, `TLX-8`, `TLY-3`, `TLY-5`, `TLY-5A`, `TLY-5Z`

### Rogers And Rogers-Adjacent Legacy HF Families

- `RO3000`, `RO4000`, `RO4400`, `RO4500`, `RO4360G2`, `RO4830 Plus`, `RO4835`, `RO4835T`, `RO4835IND LoPro`, `RO3003G2`, `RO4725JXR / RO4730G3`
- `RT/duroid`: `5870`, `5880`, `5880LZ`, `6002`, `6006`, `6010LM`, `6035HTC`, `6202`, `6202PR`, `5280LZ`
- `TMM`, `RO1200`, `RO3200`
- Rogers-owned legacy / acquisition families present by filename: `CuClad`, `IsoClad`, `DiClad`, `Cu4000`, `Kappa 438`, `MAGTREX 555`, `Anteo`, `AD Series`, `IM Series`, `Radix`

### Shengyi

- Standard FR-4 / high-Tg / halogen-free families: `S1000`, `S1000-2`, `S1000-2M`, `S1141`, `S1150G`, `S1150GH`, `S1151G`, `S1170G`, `S1190`, `S1190G`, `S1600`, `S1600L`, `S2130`, `S2131`, `S2126`, `S2155G`, `S2600F`, `S3110`, `S3116`, `S7136H`
- RF / low-loss / specialty families: `LNB33`, `LNB33C`, `mmWave`, `mmWaveG`, `AeroWave 300`, `Q260`, `Q360G`, `ST210G`, `SG7350D`, `SG7350D2`, `BIF203`
- Automotive / metal-base / specialty families: `Autolad1`, `Autolad1G`, `Autolad2G`, `Autolad2GH`, `Autolad3`, `Autolad3G`, `Autolad6G`
- Specialty `SF` family files: `SF201`, `SF202`, `SF215C`, `SF280`, `SF305`, `SF305R`, `SF335C`

### Ventec

- RF / low-loss / high-speed families: `VT-870`, `VT-901`, `VT-6880`
- High-reliability / FR-4 / halogen-free / thermal families: `VT-42`, `VT-441`, `VT-441V`, `VT-462S`, `VT-463H`, `VT-464GS`, `VT-464LT`, `VT-47`, `VT-481`, `VT-6735`, `VT-770`, `VT-90H`
- IMS / thermal adjunct files: `VT-4BC`, `VT-4B3H RCF`, `VT-4B5H`
- Bondply / prepreg / RCC-adjacent files: `VT-447PP-NFLF`, `VT-901PP-NFLF-LCTE`, `VT-464LT-RCC`, `VT-870-H1000`

### Taconic / Arlon Gap-Relevant Pool

- Taconic-branded file present: `Taconic RF-35.pdf`
- Taconic / Rogers legacy PTFE family files present by line name: `TC350`, `TC350 Plus`, `TC600`, `CuClad`, `IsoClad`, `DiClad`
- Arlon-specific filenames are not present in this local PDF pool, but several legacy PTFE / antenna / thermoset lines that can overlap Arlon-adjacent comparison demand are present under Rogers-owned naming

## Round-2 Recovery Candidates

Selection rule:

- prioritize exact-product or exact-family gaps that are not already obvious from current fact cards
- bias toward AGC missing products, Rogers missing products, Shengyi missing products, and Ventec / Taconic / Arlon-adjacent gaps
- keep every row at `candidate_inventory_only`

| # | Local PDF filename | Likely product / family | Why it matters for PCB / PCBA blogs | Recommended future fact card ID | Recommended future source ID | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `AGC_METEORWAVE_4000_TDS.pdf` | AGC METEORWAVE 4000 | High-value gap for high-speed digital and low-loss laminate blogs because AGC high-speed coverage is much thinner than Rogers / Panasonic / Isola coverage today. | `materials-agc-meteorwave-4000` | `agc-meteorwave-4000-tds` | `candidate_inventory_only` |
| 2 | `AGC_METEORWAVE_8000_TDS.pdf` | AGC METEORWAVE 8000 | Useful for very-low-loss and high-data-rate laminate comparison content where current AGC branch is underrepresented. | `materials-agc-meteorwave-8000` | `agc-meteorwave-8000-tds` | `candidate_inventory_only` |
| 3 | `AGC_N4000-13SI_TDS.pdf` | AGC N4000-13SI | Likely stronger than generic N4000 family mention for server / SI / multilayer material comparison pages and could widen non-RF AGC coverage. | `materials-agc-n4000-13si` | `agc-n4000-13si-tds` | `candidate_inventory_only` |
| 4 | `AGC_N7000-3_TDS.pdf` | AGC N7000-3 | Existing coverage includes `N7000-3F`, not this adjacent product; this is a plausible missing exact-product row for high-speed laminate family mapping. | `materials-agc-n7000-3` | `agc-n7000-3-tds` | `candidate_inventory_only` |
| 5 | `AGC_NF-30_TDS.pdf` | AGC NF-30 | Already flagged in current AGC comparison notes as a future mmWave-oriented gap; strong candidate for RF / antenna / mmWave selector expansion. | `materials-agc-nf-30` | `agc-nf-30-tds` | `candidate_inventory_only` |
| 6 | `AGC_RF-35TC_TDS.pdf` | AGC RF-35TC | Natural follow-on to the existing `RF-35HTC` card and likely useful for power RF or adjacent selector comparisons without overextending current RF coverage. | `materials-agc-rf-35tc` | `agc-rf-35tc-tds` | `candidate_inventory_only` |
| 7 | `RO4360G2 High Frequency Laminates Data Sheet.pdf` | Rogers RO4360G2 | High-value gap between `RO4350B` and other Rogers RF lines for mixed RF / manufacturable hydrocarbon-ceramic content. | `materials-rogers-ro4360g2` | `rogers-ro4360g2-datasheet` | `candidate_inventory_only` |
| 8 | `RO4830 Plus Laminates Data Sheet.pdf` | Rogers RO4830 Plus | Distinct from existing `RO4835` and useful for antenna-grade and low-loss comparison coverage inside the RO4800 branch. | `materials-rogers-ro4830-plus` | `rogers-ro4830-plus-datasheet` | `candidate_inventory_only` |
| 9 | `RO4835IND LoPro Laminate Data Sheet.pdf` | Rogers RO4835IND LoPro | Attractive exact-product candidate for automotive / radar / low-profile copper discussion where the current branch mostly centers on base `RO4835`. | `materials-rogers-ro4835ind-lopro` | `rogers-ro4835ind-lopro-datasheet` | `candidate_inventory_only` |
| 10 | `RT-duroid 6002 Laminate Data Sheet.pdf` | Rogers RT/duroid 6002 | Explicitly called out by an existing `RT/duroid 5880` card as a desirable follow-on for more balanced low-loss PTFE comparison. | `materials-rogers-rt-duroid-6002` | `rogers-rt-duroid-6002-datasheet` | `candidate_inventory_only` |
| 11 | `RT-duroid 6202 Laminate Data Sheet.pdf` | Rogers RT/duroid 6202 | Valuable for high-Dk PTFE compactness and RF miniaturization comparison content beyond current `RO3010` / `RF-10` coverage. | `materials-rogers-rt-duroid-6202` | `rogers-rt-duroid-6202-datasheet` | `candidate_inventory_only` |
| 12 | `Shengyi-mmWaveG-mmWaveGB.pdf` | Shengyi mmWaveG / mmWaveGB | High-value missing Shengyi RF/mmWave row that could support cautious China-supplier-neutral mmWave material framing once source-scoped. | `materials-shengyi-mmwaveg` | `shengyi-mmwaveg-datasheet` | `candidate_inventory_only` |
| 13 | `Shengyi-AeroWave+300.pdf` | Shengyi AeroWave 300 | Another RF-focused Shengyi gap with likely payoff for antenna and microwave blog families where current Shengyi coverage is mostly FR-4 class. | `materials-shengyi-aerowave-300` | `shengyi-aerowave-300-datasheet` | `candidate_inventory_only` |
| 14 | `Shengyi-LNB33C.pdf` | Shengyi LNB33C | Likely low-loss / high-speed family candidate with stronger practical payoff than reopening already-held `S1141`; useful for digital laminate branch expansion. | `materials-shengyi-lnb33c` | `shengyi-lnb33c-datasheet` | `candidate_inventory_only` |
| 15 | `Shengyi-S1170G-S1170GB.pdf` | Shengyi S1170G / S1170GB | Missing exact-product Shengyi halogen-free FR-4 candidate that could extend the current `S1150G` and `S1000-*` coverage into another common family. | `materials-shengyi-s1170g` | `shengyi-s1170g-datasheet` | `candidate_inventory_only` |
| 16 | `Ventec-vt-901.pdf` | Ventec VT-901 | High-value Ventec RF / microwave gap because current Ventec exact-product coverage leans `VT-870`, `VTM1000i`, `VT-464G`, and IMS. | `materials-ventec-vt-901` | `ventec-vt-901-datasheet` | `candidate_inventory_only` |
| 17 | `Ventec-vt-6880.pdf` | Ventec VT-6880 | Likely useful for low-loss RF / microwave comparison and a strong complement to existing `VT-870` and `VTM1000i` anchors. | `materials-ventec-vt-6880` | `ventec-vt-6880-datasheet` | `candidate_inventory_only` |
| 18 | `Taconic RF-35.pdf` | Taconic RF-35 | Highest-value Taconic gap because current corpus only has source-gap governance for Taconic and no exact-product fact card. | `materials-taconic-rf-35` | `taconic-rf-35-datasheet` | `candidate_inventory_only` |

## Why These Candidates Beat Some Nearby Alternatives

- `Shengyi S1141` was already held in prior control logs, so it is not the best round-2 recovery candidate unless a future batch specifically requires it.
- `Ventec VT-4BC`, `VT-4B7`, `VT-4BD`, `VT-870`, and `VT-464G` already have usable coverage, so this pass favors less-covered Ventec products.
- `AGC RF-10`, `RF-30A`, `RF-35HTC`, and `N7000-3F` already have current fact coverage, so this pass favors adjacent missing AGC rows.
- `RO3003`, `RO3006`, `RO3010`, `RO3035`, `RO4003C`, `RO4350B`, `RO4835`, `RO4450F`, `RO4460G2`, `RT/duroid 5880`, and `TMM 10i` already anchor the main Rogers branch, so this pass favors uncovered adjacent Rogers products.

## Residual Gaps After This Inventory

- AGC still has multiple uncovered `METEORWAVE`, `N4000`, `TSM`, and PTFE-family rows beyond the short list above.
- Shengyi still has a large uncovered tail across `Autolad`, `SF`, `Q`, `SG`, and `S16xx / S21xx / S31xx` families.
- Ventec still has meaningful uncovered products in `VT-441`, `VT-463H`, `VT-481`, `VT-6735`, `VT-770`, and prepreg / RCC-adjacent files.
- Taconic remains thin because only one clearly Taconic-branded file is present and current official-source governance is still strict.
- Arlon-specific missing product recovery cannot advance from this local PDF pool because no clearly Arlon-branded local PDFs were identified in this directory.
- Rogers-owned legacy HF lines such as `CuClad`, `IsoClad`, `DiClad`, `Kappa 438`, `MAGTREX 555`, `Anteo`, and `IM Series` may matter later, but they need vendor-line validation before safe fact extraction.

## Extraction Blockers

- `pdftotext` is not installed in the current workspace, so filenames could be inventoried but the internal datasheet tables, revision markers, and exact product naming could not be text-verified here.
- Some filenames may represent legacy Rogers-owned or distributor-preserved product lines; future recovery should confirm current manufacturer ownership and official publication status before any fact intake.
- Duplicate or near-duplicate Shengyi and Rogers files exist in the pool, so future source intake should normalize exact revision / variant identity before creating product cards.

## Disposition

- This file is a `candidate_inventory_only` log.
- Nothing in this log should be treated as `learned`.
- Future work should convert only selected rows into official-source-backed source records and fact cards after direct document verification.

## Controller Integration Note

After this candidate inventory was produced, the controller completed direct PDF extraction and official URL checks for three AGC rows:

- `AGC_RF-60TC_TDS.pdf` -> `agc-rf-60tc-datasheet` / `materials-agc-rf-60tc`
- `AGC_RF-35TC_TDS.pdf` -> `agc-rf-35tc-datasheet` / `materials-agc-rf-35tc`
- `AGC_METEORWAVE_4000_TDS.pdf` -> `agc-meteorwave-4000-datasheet` / `materials-agc-meteorwave-4000`

Those three rows are no longer merely candidate inventory. See `logs/p4-33-material-pdf-source-recovery-round-1.md` for the source-backed upgrade scope and remaining blocked claim classes.

The controller then completed direct PDF extraction and official URL checks for four more AGC rows:

- `AGC_METEORWAVE_8000_TDS.pdf` -> `agc-meteorwave-8000-datasheet` / `materials-agc-meteorwave-8000`
- `AGC_N4000-13SI_TDS.pdf` -> `agc-n4000-13si-datasheet` / `materials-agc-n4000-13si`
- `AGC_N7000-3_TDS.pdf` -> `agc-n7000-3-datasheet` / `materials-agc-n7000-3`
- `AGC_NF-30_TDS.pdf` -> `agc-nf-30-datasheet` / `materials-agc-nf-30`

Those four rows are also no longer merely candidate inventory. See `logs/p4-33-material-pdf-source-recovery-round-2.md` for the source-backed upgrade scope and remaining blocked claim classes.

The controller later completed direct extraction and official URL checks for five Rogers rows, two Ventec rows, and four Shengyi rows:

- `RO4360G2 High Frequency Laminates Data Sheet.pdf` -> `rogers-ro4360g2-datasheet` / `materials-rogers-ro4360g2`
- `RO4830 Plus Laminates Data Sheet.pdf` -> `rogers-ro4830-plus-datasheet` / `materials-rogers-ro4830-plus`
- `RO4835IND LoPro Laminate Data Sheet.pdf` -> `rogers-ro4835ind-lopro-datasheet` / `materials-rogers-ro4835ind-lopro`
- `RT-duroid 6002 Laminate Data Sheet.pdf` -> `rogers-rt-duroid-6002-datasheet` / `materials-rogers-rt-duroid-6002`
- `RT-duroid 6202 Laminate Data Sheet.pdf` -> `rogers-rt-duroid-6202-datasheet` / `materials-rogers-rt-duroid-6202`
- `Ventec-vt-901.pdf` -> `ventec-vt-901-datasheet-page` / `materials-ventec-vt-901`
- `Ventec-vt-6880.pdf` -> `ventec-vt-6880-datasheet` / `materials-ventec-vt-6880`
- `Shengyi-AeroWave+300.pdf` -> `shengyi-aerowave-300-datasheet` / `materials-shengyi-aerowave-300`
- `Shengyi-mmWaveG-mmWaveGB.pdf` -> `shengyi-mmwaveg-product-page` / `materials-shengyi-mmwaveg`
- `Shengyi-LNB33C.pdf` -> `shengyi-lnb33c-product-page` / `materials-shengyi-lnb33c`
- `Shengyi-S1170G-S1170GB.pdf` -> `shengyi-s1170g-product-page` / `materials-shengyi-s1170g`

Those rows are no longer merely candidate inventory. See `logs/p4-33-material-pdf-source-recovery-round-3.md`, `logs/p4-33-material-pdf-source-recovery-round-4.md`, `logs/p4-33-material-pdf-source-recovery-round-5.md`, and `logs/p4-33-material-pdf-source-recovery-round-6.md` for the source-backed upgrade scopes and remaining blocked claim classes. Companion / prepreg identities `mmWaveGB` and `S1170GB` remain blocked unless separately verified.

The controller also completed direct extraction and official URL checks for five additional AGC METEORWAVE tail rows:

- `AGC_METEORWAVE_1000_TDS.pdf` -> `agc-meteorwave-1000-datasheet` / `materials-agc-meteorwave-1000`
- `AGC_METEORWAVE_1000NF_TDS.pdf` -> `agc-meteorwave-1000nf-datasheet` / `materials-agc-meteorwave-1000nf`
- `AGC_METEORWAVE_2000_TDS.pdf` -> `agc-meteorwave-2000-datasheet` / `materials-agc-meteorwave-2000`
- `AGC_METEORWAVE_3000_TDS.pdf` -> `agc-meteorwave-3000-datasheet` / `materials-agc-meteorwave-3000`
- `AGC_METEORWAVE_4000M_TDS.pdf` -> `agc-meteorwave-4000m-datasheet` / `materials-agc-meteorwave-4000m`

Those rows are no longer merely filename inventory. See `logs/p4-33-material-pdf-source-recovery-round-7.md` for the source-backed upgrade scope and remaining blocked claim classes.

The controller then completed direct extraction and official URL checks for four additional AGC tail rows:

- `AGC_METEORWAVE_8300_TDS.pdf` -> `agc-meteorwave-8300-datasheet` / `materials-agc-meteorwave-8300`
- `AGC_METEORWAVE_M1_TDS.pdf` -> `agc-meteorwave-m1-datasheet` / `materials-agc-meteorwave-m1`
- `AGC_N4000-13_TDS.pdf` -> `agc-n4000-13-datasheet` / `materials-agc-n4000-13`
- `AGC_N4000-13EP_TDS.pdf` -> `agc-n4000-13ep-datasheet` / `materials-agc-n4000-13ep`

Those rows are no longer merely filename inventory. See `logs/p4-33-material-pdf-source-recovery-round-8.md` for the source-backed upgrade scope and remaining blocked claim classes.

The controller then completed direct extraction and official URL checks for four additional AGC tail rows:

- `AGC_N4000-13EPSI_TDS.pdf` -> `agc-n4000-13epsi-datasheet` / `materials-agc-n4000-13epsi`
- `AGC_N4000-29_TDS.pdf` -> `agc-n4000-29-datasheet` / `materials-agc-n4000-29`
- `AGC_N4000-29NF_TDS.pdf` -> `agc-n4000-29nf-datasheet` / `materials-agc-n4000-29nf`
- `AGC_N7000-2HT_TDS.pdf` -> `agc-n7000-2ht-datasheet` / `materials-agc-n7000-2ht`

Those rows are no longer merely filename inventory. See `logs/p4-33-material-pdf-source-recovery-round-9.md` for the source-backed upgrade scope and remaining blocked claim classes.

The controller then completed direct extraction and official Ventec page / PDF checks for four additional Ventec rows:

- `Ventec-vt-481.pdf` -> `ventec-vt-481-datasheet-page` / `materials-ventec-vt-481`
- `Ventec-vt-463h.pdf` -> `ventec-vt-463h-datasheet-page` / `materials-ventec-vt-463h`
- `Ventec-vt-6735.pdf` -> `ventec-vt-6735-datasheet` / `materials-ventec-vt-6735`
- `Ventec-vt-770-vt-770lk.pdf` -> `ventec-vt-770-vt-770lk-datasheet-page` / `materials-ventec-vt-770-vt-770lk`

Those rows are no longer merely filename inventory. See `logs/p4-33-material-pdf-source-recovery-round-10.md` for the source-backed upgrade scope and remaining blocked claim classes. Ventec process / storage / handling guidance remains product-scoped only and does not become generic process-window or supplier-capability evidence.

The controller then completed direct extraction and official Ventec page checks for four additional Ventec rows:

- `Ventec-vt-462s.pdf` -> `ventec-vt-462s-datasheet-page` / `materials-ventec-vt-462s`
- `Ventec-vt-464gs.pdf` -> `ventec-vt-464gs-datasheet-page` / `materials-ventec-vt-464gs`
- `Ventec-vt-90h.pdf` -> `ventec-vt-90h-datasheet-page` / `materials-ventec-vt-90h`
- `Ventec-vt-4b5h.pdf` -> `ventec-vt-4b5h-datasheet-page` / `materials-ventec-vt-4b5h`

Those rows are no longer merely filename inventory. See `logs/p4-33-material-pdf-source-recovery-round-11.md` for the source-backed upgrade scope and remaining blocked claim classes. Ventec PGL / storage / handling / process guidance remains product-scoped only and does not become generic process-window or supplier-capability evidence.

The controller then completed direct extraction and official Ventec page checks for three additional Ventec FR-4-family rows:

- `Ventec-vt-441v.pdf` -> `ventec-vt-441v-datasheet-page` / `materials-ventec-vt-441v`
- `Ventec-vt-441.pdf` -> `ventec-vt-441-datasheet-page` / `materials-ventec-vt-441`
- `Ventec-vt-42.pdf` -> `ventec-vt-42-datasheet-page` / `materials-ventec-vt-42`

Those rows are no longer merely filename inventory. See `logs/p4-33-material-pdf-source-recovery-round-12.md` for the source-backed upgrade scope and remaining blocked claim classes. Their FR-4 values remain product-scoped and do not become generic FR-4 defaults, process windows, supplier capability, or finished-board performance proof.

The controller then completed official TUC product-page checks and direct extraction for three high-confidence TUC rows:

- `tu-901_datasheet.pdf` -> `tuc-tu-901-datasheet-page` / `materials-tuc-tu-901`
- `tu-787 lk_datasheet.pdf` -> `tuc-tu-787-lk-datasheet-page` / `materials-tuc-tu-787-lk`
- `tu-872 lk_datasheet.pdf` -> `tuc-tu-872-lk-datasheet-page` / `materials-tuc-tu-872-lk`

Those rows are no longer merely filename inventory. See `logs/p4-33-material-pdf-source-recovery-round-13.md` for the source-backed upgrade scope and remaining blocked claim classes. TUC dynamic download endpoints should be refreshed before evidence-pack use; `TU-865S` remains pending preliminary-revision binding, and `SCGA-500 GF220` remains blocked pending exact live official TUC source recovery.

The controller then completed official AGC PDF URL checks and direct extraction for five additional AGC TSM / TLX / TLY rows:

- `AGC_TSM-DS3_TDS.pdf` -> `agc-tsm-ds3-datasheet` / `materials-agc-tsm-ds3`
- `AGC_TSM-DS3b_TDS.pdf` -> `agc-tsm-ds3b-datasheet` / `materials-agc-tsm-ds3b`
- `AGC_TSM-DS3M_TDS.pdf` -> `agc-tsm-ds3m-datasheet` / `materials-agc-tsm-ds3m`
- `AGC_TLX-8_TDS.pdf` -> `agc-tlx-8-datasheet` / `materials-agc-tlx-8`
- `AGC_TLY-5_TDS.pdf` -> `agc-tly-5-datasheet` / `materials-agc-tly-5`

Those rows are no longer merely filename inventory. See `logs/p4-33-material-pdf-source-recovery-round-14.md` for the source-backed upgrade scope and remaining blocked claim classes.

The controller then completed official AGC PDF URL checks and `pypdf` extraction for five additional AGC TLY / TLE / TLC rows:

- `AGC_TLY-3_TDS.pdf` -> `agc-tly-3-datasheet` / `materials-agc-tly-3`
- `AGC_TLY-5A_TDS.pdf` -> `agc-tly-5a-datasheet` / `materials-agc-tly-5a`
- `AGC_TLY-5Z_TDS.pdf` -> `agc-tly-5z-datasheet` / `materials-agc-tly-5z`
- `AGC_TLE-95_TDS.pdf` -> `agc-tle-95-datasheet` / `materials-agc-tle-95`
- `AGC_TLC-32_TDS.pdf` -> `agc-tlc-32-datasheet` / `materials-agc-tlc-32`

Those rows are no longer merely filename inventory. See `logs/p4-33-material-pdf-source-recovery-round-15.md` for the source-backed upgrade scope and remaining blocked claim classes.

The controller then integrated a `gpt-5.4` scout-only AGC tail handoff after main-agent review and direct `pypdf` extraction:

- `AGC_ELL_TDS.pdf` -> `agc-meteorwave-ell-datasheet` / `materials-agc-meteorwave-ell`
- `AGC_TLF-35A_TDS.pdf` -> `agc-tlf-35a-datasheet` / `materials-agc-tlf-35a`

Those rows are no longer merely filename inventory. See `logs/p4-33-agc-tail-scout-round-16.md` and `logs/p4-33-material-pdf-source-recovery-round-16.md` for the scout handoff, source-backed upgrade scope, and remaining blocked claim classes.
