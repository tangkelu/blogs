# P4-33 AGC Tail Scout Round 16

Date: 2026-04-28
Status: `scout_only_source_inventory`

## Purpose

Scout the remaining AGC tail for `METEORWAVE ELL` and `TLF-35A` using the supplied local PDFs plus current `llm_wiki` coverage, without promoting any new facts or updating registries, facts, wiki pages, trackers, or other logs.

## Scope Boundary

- Allowed edit used: `/code/blogs/llm_wiki/logs/p4-33-agc-tail-scout-round-16.md`
- No other files were edited.
- This lane is not fully learned. It is only a scout / handoff note for later main-agent integration.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/AGC_ELL_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_TLF-35A_TDS.pdf`
- Existing `llm_wiki` AGC coverage under `facts/`, `wiki/`, `sources/registry/`, and prior P4-33 logs

## Existing Coverage Check

- Existing AGC exact-product fact coverage is broad, but no current `facts/`, `wiki/`, or `sources/registry/` rows were found for:
  - `ELL`
  - `METEORWAVE ELL`
  - `TLF-35A`
- Prior round-14 tail planning explicitly left `TLX / TLY / TLE / TLC / TLF / ELL tail` open.

## Source URLs Checked

Confirmed as likely official AGC public URLs:

- `https://www.agc-multimaterial.com/agc-downloads/AGC_ELL_TDS.pdf`
  - HTTP check: `200`
  - response metadata observed: `Last-Modified: Fri, 09 Aug 2024 17:18:00 GMT`
- `https://www.agc-multimaterial.com/agc-downloads/AGC_TLF-35A_TDS.pdf`
  - HTTP check: `200`
  - response metadata observed: `Last-Modified: Thu, 29 Feb 2024 16:11:30 GMT`
- `https://www.agc-multimaterial.com/solutions/meteorwave-ell/`
  - HTTP check: `200`
- `https://www.agc-multimaterial.com/solutions/tlf-35a/`
  - HTTP check: `200`

Notes:

- Product-page body extraction was not completed in this scout note; only HTTP-level public-page confirmation was performed.
- Safe extraction below is based on the supplied local PDFs, which align with the checked official AGC PDF URLs by filename pattern and HTTP availability.

## Candidate Source IDs

Likely future source records for main-agent integration:

- `agc-meteorwave-ell-datasheet`
- `agc-meteorwave-ell-product-page`
- `agc-tlf-35a-datasheet`
- `agc-tlf-35a-product-page`

## Candidate Fact IDs

Likely future exact-product fact cards for main-agent integration:

- `materials-agc-meteorwave-ell`
- `materials-agc-tlf-35a`

## Safe Source-Scoped Values

### `METEORWAVE ELL`

Source basis:

- local file `AGC_ELL_TDS.pdf`
- matched checked URL `https://www.agc-multimaterial.com/agc-downloads/AGC_ELL_TDS.pdf`
- PDF footer shows `AGC Inc. 2024-08`

Safe values and conditions:

- Product-family naming in the TDS is `METEORWAVE ELL 101, ELL 102, ELL 103`.
- Material form is stated as `Laminate & Prepreg`.
- Dk:
  - `ELL 101 @ 10 GHz = 3.05`
  - `ELL 102/103 @ 10 GHz = 3.03`
  - method shown: `IPC-TM-650.2.5.5.5`
- Df:
  - `ELL 101 @ 10 GHz = 0.0012`
  - `ELL 102/103 @ 10 GHz = 0.0009`
- Volume resistivity:
  - `C - 96 / 35 / 90 = 8.9 x 10^7 MΩ-cm`
  - `E - 24 / 125 = 1.1 x 10^8 MΩ-cm`
  - method shown: `IPC-TM-650.2.5.17.1`
- Surface resistivity:
  - `C - 96 / 35 / 90 = 4.7 x 10^6 MΩ`
  - `E - 24 / 125 = 2.3 x 10^8 MΩ`
  - method shown: `IPC-TM-650.2.5.17.1`
- Electric strength:
  - `65 kV/mm`
  - secondary unit shown: `(1.7 x 10^3) V/mil`
  - method shown: `IPC-TM-650.2.5.6.2`
- Tg:
  - `190 °C`
  - condition shown: `DMA (Tan d Peak)`
  - method shown: `IPC-TM-650.2.4.24.3`
- Td:
  - `376 °C`
  - condition shown: `5% wt. loss`
  - method shown: `IPC-TM-650.2.3.40`
- Time to delamination:
  - `T-288 >120 minutes`
  - `T-300 >60 minutes`
  - method shown: `IPC-TM-650.2.4.24.1`
- Thermal conductivity:
  - `0.475 W/mK`
  - method shown: `ASTM E1461`
- Peel strength:
  - `1 oz (35 µm) Cu = 0.49 N/mm (2.8 lb/inch)`
  - `After Solder Float = 0.54 N/mm (3.1 lb/inch)`
  - method shown: `IPC-TM-650.2.4.8`
- X / Y CTE:
  - `12 / 12 ppm/°C`
  - condition shown: `-40°C to +125°C`
  - method shown: `IPC-TM-650.2.4.41`
- Z-axis CTE:
  - `Alpha 1 / Alpha 2 = 65 / 156 ppm/°C`
  - condition shown: `50°C to Tg / Tg to 260°C (55% RC)`
  - method shown: `IPC-TM-650.2.4.24`
- Z-axis expansion:
  - `1.8 %`
  - condition shown: `50°C to 260°C (43% RC)`
  - method shown: `IPC-TM-650.2.4.24`
- Young's modulus:
  - `X / Y = 15.2 / 1.65 GN/m2`
  - secondary unit shown: `(2.2 / 2.4) psi x 10^6`
  - method shown: `ASTM D3039`
- Poisson's ratios:
  - `X / Y = 0.149 / 0.159`
- Moisture absorption:
  - `0.036 wt.%`
  - method shown: `IPC-TM-650.2.6.2.1`
- Outgas:
  - `TML / CVCM / WVR = 0.34 / <0.01 / <0.01 wt.%`
  - methods shown: `IPC-TM650 2.6.4B; ASTM E595`
- Availability / form notes from the TDS:
  - laminate thickness `from 1.2 mil (0.031 mm) and up`
  - available in `most common panel sizes`
  - contact AGC for other constructions, copper weights, glass styles, ultra-low-profile copper, and `RTFOIL`

Context that is safe only as manufacturer framing, not finished-system proof:

- application list includes `Telecommunications`, `Core Routers`, `High Speed Switching / Routing Systems`, `Cloud Storage`, `Aerospace`, `Automotive radar`, and `AI`
- the TDS states `Meets UL 94-V0 and IPC-4103/540 specifications`
- the TDS states compliance with `ROHS`, `REACH`, `California Prop 65`, and the `Conflict Minerals Act`
- the TDS names:
  - `ELL 101 = resin system on NE fabric`
  - `ELL 102 = resin system on NER fabric`
  - `ELL 103 = resin system on L2 fabric`

Treat with care:

- the statement that `ELL101 has demonstrated the SI performance suitable for 112 Gb designs` is manufacturer framing and should not be promoted as generalized finished-board proof without tighter context and scope controls.

### `TLF-35A`

Source basis:

- local file `AGC_TLF-35A_TDS.pdf`
- matched checked URL `https://www.agc-multimaterial.com/agc-downloads/AGC_TLF-35A_TDS.pdf`
- PDF footer shows `AGC Inc. 2024-02`

Safe values and conditions:

- Product name in the TDS is `TLF-35A`.
- Electrical:
  - dielectric constant `@ 10 GHz = 3.50 ± 0.05`
  - dissipation factor `@ 10 GHz = 0.0026`
  - method shown for both: `IPC-TM 650 2.5.5.5.1 Mod`
- Surface resistivity:
  - `3.0 x 10^9 Mohms`
  - method shown: `IPC-TM 650 2.5.17.1`
- Volume resistivity:
  - `2.0 x 10^8 Mohms/cm`
  - method shown: `IPC-TM 650 2.5.17.1`
- Thermal conductivity:
  - `0.37 W/m/K`
  - method shown: `IPC-TM-650 2.4.50`
- CTE:
  - `X = 9 ppm/°C`
  - `Y = 12 ppm/°C`
  - `Z = 80 ppm/°C`
  - condition shown: `50 to 150 °C`
  - method shown: `IPC-650 2.4.41`
- Peel strength:
  - `1 oz. copper = 1.8 N/mm (10 Lbs./linear in)`
  - method shown: `IPC-TM 650 2.4.8`
- Flexural strength:
  - `Lengthwise = 90 N/mm2 (13,000 psi)`
  - `Crosswise = 90 N/mm2 (13,000 psi)`
  - method shown: `IPC-TM 650 2.4.4`
- Flammability:
  - `V-0`
  - method shown: `UL-94`
- Water absorption:
  - `0.03 %`
  - method shown: `IPC-TM 650 2.6.2.1`
- Typical thicknesses:
  - `0.030 in / 0.76 mm`
  - `0.060 in / 1.52 mm`
- Typical panel sizes:
  - `12 x 18 in / 305 x 457 mm`
  - `16 x 18 in / 406 x 457 mm`
  - `18 x 24 in / 457 x 610 mm`
  - `36 x 48 in / 914 x 1220 mm`
- Available copper cladding table is present with named designations:
  - `CVH (CH)`
  - `CV1 (C1)`
  - `CLH`
  - `CL1`
  - `C2`
- Availability / manufacturing note from the TDS:
  - can be manufactured in increments of `0.030 in (0.76 mm)`
  - standard panel size stated as `18 x 24 in (457 x 610 mm)`
  - contact AGC for additional thicknesses, sizes, and cladding

Context that is safe only as manufacturer framing, not finished-system proof:

- benefits include `Improved PIMD with DK3.5`, `Improved PTH Quality`, `Stable at high frequency`, `Stable at high temp.`, `Low moisture absorption`, `Excellent Peel Strength`, and `Excellent price/performance Ratio`
- application list includes `Size effective Antenna`, `Power Amplifiers`, `LNA`, `Repeater PA`, `Passive Components`, and `Filters / Couplers`
- the text frames attenuation measurement using a `microstrip ring resonator` with `20 mil dielectric thickness and 1 oz. copper`

Treat with care:

- the body text says `TLF-35A is an organic-ceramic laminate in Taconic's family of product`; that lineage statement should be carried forward only as a directly attributed text observation if needed, not normalized into unsupported ownership or equivalence claims.

## Blocked Claims

Do not promote from this scout note into reusable facts without tighter source handling or extra evidence:

- Any price, `low cost`, `price/performance`, MOQ, stock, lead-time, yield, or volume-supply claim.
- Any generalized `improved PIMD`, `similar PIMD levels`, `improved PTH quality`, or attenuation-outperformance claim beyond the exact source conditions stated.
- Any finished-board or system-level RF, microwave, telecom, antenna, repeater, radar, aerospace, AI, cloud, router, switching, or 112G performance claim.
- Any supplier capability, production approval, qualification, reliability-at-scale, or build-success claim.
- Any compliance or certification claim beyond direct source wording and exact scope.
- Any equivalence, competitive replacement, or drop-in-substitution claim.

## Residual Gaps

- No source registry entries were created in this scout lane.
- No exact-product fact cards were created in this scout lane.
- No product-page body extraction was completed, so current public AGC positioning text remains only HTTP-confirmed, not content-extracted here.
- `METEORWAVE ELL` is a family row with `ELL 101 / 102 / 103` variants; the main agent should decide whether to model it as one family card or one umbrella card with explicit variant subrows.
- The `112 Gb` wording for `ELL101` needs especially strict handling if later integrated.
- `TLF-35A` includes method-conditioned attenuation / PIMD framing but this scout note does not normalize any graph-derived values or comparative performance conclusions.

## Handoff Summary

- Changed files:
  - `/code/blogs/llm_wiki/logs/p4-33-agc-tail-scout-round-16.md`
- Safe next integration targets:
  - source records: `agc-meteorwave-ell-datasheet`, `agc-meteorwave-ell-product-page`, `agc-tlf-35a-datasheet`, `agc-tlf-35a-product-page`
  - fact cards: `materials-agc-meteorwave-ell`, `materials-agc-tlf-35a`
- Current lane verdict:
  - `scout only`
  - not fully learned
  - suitable as evidence inventory for a later main-agent source-registration and fact-card pass
