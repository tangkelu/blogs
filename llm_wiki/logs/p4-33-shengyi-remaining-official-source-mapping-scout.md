# P4-33 Shengyi Remaining Official-Source Mapping Scout

Date: 2026-04-28
Lane: `P4-33 remaining Shengyi official-source mapping scout for material PDFs`
Status: `partial_official_mapping_only`
Learning State: `not_learned`

## Scope

- Allowed output only:
  - `/code/blogs/llm_wiki/logs/p4-33-shengyi-remaining-official-source-mapping-scout.md`
- Inputs checked:
  - `/code/blogs/tmps/materias_pdf/Shengyi-mmWaveG-mmWaveGB.pdf`
  - `/code/blogs/tmps/materias_pdf/Shengyi-LNB33C.pdf`
  - `/code/blogs/tmps/materias_pdf/Shengyi-S1170G-S1170GB.pdf`
  - `/tmp/shengyi-rf-and-microwave.html`
  - `/code/blogs/llm_wiki/logs/p4-33-shengyi-material-pdf-extraction-scout-round-4.md`
  - `/code/blogs/llm_wiki/logs/p4-33-material-pdf-source-recovery-round-5.md`

## Method

- Treated the three local PDFs as claim inventory and identity hints only, not authority.
- Inspected the saved Shengyi USA RF and Microwave page snapshot for exact product names and official download URLs.
- Used local `fitz` extraction only to confirm product identity strings inside the three local PDFs.
- Did not create source records, fact cards, wiki pages, trackers, or reusable fact snapshots.

## Official Snapshot Results

Official Shengyi USA RF and Microwave snapshot exposed these relevant technical-datasheet links:

- `AEROWAVE 300-TDS` -> `https://www.shengyi-usa.com/download/28748/`
- `mmWAVE - TDS` -> `https://www.shengyi-usa.com/download/28752/`
- `mmWave77 TDS.pdf` -> `https://www.shengyi-usa.com/download/29400/`
- `S7136H- TDS` -> `https://www.shengyi-usa.com/download/28754/`

The snapshot did not contain exact product-name hits for:

- `LNB33C`
- `S1170G`
- `S1170GB`
- `mmWaveG`
- `mmWaveGB`

## Local PDF Identity Check

Local PDF identity markers recovered:

- `Shengyi-mmWaveG-mmWaveGB.pdf`
  - document code `CN-TDS-2307-03-mmWaveG-mmWaveGB`
  - extracted identity includes `mmWave G`
- `Shengyi-LNB33C.pdf`
  - document code `CN-TDS-2210-01-LNB33C`
  - extracted identity includes `LNB33C`
- `Shengyi-S1170G-S1170GB.pdf`
  - document code `CN-TDS-2203-03-S1170G-S1170GB`
  - extracted identity includes both `S1170G` and `S1170GB`

## Product Mapping Assessment

### 1. mmWave / mmWaveG / mmWaveGB

- Official page section exists for `mmWave`.
- Official download URL found:
  - `https://www.shengyi-usa.com/download/28752/`
- Blocker:
  - the official page names the product `mmWave`, while the local candidate PDF is `CN-TDS-2307-03-mmWaveG-mmWaveGB` and extracted product identity is `mmWave G` with filename-level `mmWaveGB`.
- Current judgment:
  - `likely promotable next` only if the official download at `28752` is fetched and verified to be the same revision family as local `mmWaveG/mmWaveGB`, or otherwise shown to be the official successor / exact product-equivalent accepted by controller rules.
- Exact verification still needed:
  - fetch `https://www.shengyi-usa.com/download/28752/`
  - confirm whether the downloaded PDF title / document code is exact `mmWaveG-mmWaveGB`, plain `mmWave`, or another revision family
  - compare first-page product identity and table structure against local `CN-TDS-2307-03-mmWaveG-mmWaveGB`
  - decide whether only `mmWave` laminate claims are promotable, while `mmWaveGB` remains blocked unless separately named in the official file

### 2. LNB33C

- No exact `LNB33C` hit on the official snapshot.
- No official Shengyi USA download URL found in the snapshot for this exact product.
- Current judgment:
  - `blocked_pending_official_url`
- Exact verification still needed:
  - find a Shengyi official page or direct official download endpoint that explicitly names `LNB33C`
  - verify the official file title / document code against local `CN-TDS-2210-01-LNB33C`

### 3. S1170G / S1170GB

- No exact `S1170G` or `S1170GB` hit on the official snapshot.
- No official Shengyi USA download URL found in the snapshot for this exact product pair.
- Current judgment:
  - `blocked_pending_official_url`
- Exact verification still needed:
  - find a Shengyi official page or direct official download endpoint that explicitly names `S1170G` and ideally `S1170GB`
  - confirm whether the official source is one combined laminate+prepreg PDF or separate files
  - if combined, verify whether the prepreg side is sufficiently explicit for any future `S1170GB` treatment; otherwise keep only laminate-side identity in scope

## Likely Next Promotable Product

- `mmWave` is the only remaining Shengyi candidate in this lane with an official Shengyi USA download URL already surfaced from the saved snapshot.
- It is not yet safe to promote `mmWaveG/mmWaveGB` from that URL without checking the downloaded PDF identity because the official page product name and the local candidate document code do not match exactly.

## Blocked Claims

Do not promote any of the following from the local PDFs or from product-marketing page copy until exact official PDF identity is verified:

- any numeric material-property rows from `mmWaveG/mmWaveGB`, `LNB33C`, or `S1170G/S1170GB`
- any `mmWaveGB` or `S1170GB` prepreg-specific rows based only on local combined PDFs
- passive intermodulation, application suitability, antenna / radar readiness, or other performance-readiness claims
- supplier capability, certification, price, MOQ, lead-time, yield, or quality-capability claims

## Residual Gaps

- No network fetch was performed for `https://www.shengyi-usa.com/download/28752/`, so the exact PDF identity behind the `mmWAVE - TDS` link remains unverified.
- The saved RF-and-microwave snapshot appears not to cover `LNB33C` or `S1170G/S1170GB`; they may require another official Shengyi page, search path, or a different regional Shengyi source.
- `mmWaveGB` remains especially sensitive because the local combined PDF exposes stronger laminate-side identity than prepreg-side separability.

## Sources Checked

- Shengyi USA RF and Microwave snapshot:
  - `/tmp/shengyi-rf-and-microwave.html`
- Existing lane logs:
  - `/code/blogs/llm_wiki/logs/p4-33-shengyi-material-pdf-extraction-scout-round-4.md`
  - `/code/blogs/llm_wiki/logs/p4-33-material-pdf-source-recovery-round-5.md`
- Local candidate PDFs:
  - `/code/blogs/tmps/materias_pdf/Shengyi-mmWaveG-mmWaveGB.pdf`
  - `/code/blogs/tmps/materias_pdf/Shengyi-LNB33C.pdf`
  - `/code/blogs/tmps/materias_pdf/Shengyi-S1170G-S1170GB.pdf`

## Changed Files

- `/code/blogs/llm_wiki/logs/p4-33-shengyi-remaining-official-source-mapping-scout.md`

## Lane Status

- status: `partial_official_mapping_only`
- promotable_next_candidate: `mmWave only after official download identity verification`
- blocked_candidates:
  - `LNB33C`
  - `S1170G/S1170GB`
  - `mmWaveGB` as a separately promotable identity
