---
topic_id: "materials-rf-selector-by-application-band"
title: "RF Material Selector by Application Band"
category: "materials"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "materials-rf-selector-by-application"
  - "materials-rogers-ro3003"
  - "materials-rogers-ro3006"
  - "materials-rogers-ro3035"
  - "materials-isola-astra-mt77"
  - "materials-panasonic-megtron-6"
  - "materials-panasonic-megtron-7"
  - "materials-ventec-vt-870"
  - "materials-ventec-vtm1000i"
  - "materials-agc-rf-30a"
  - "materials-agc-rf-10"
  - "materials-agc-rf-35htc"
  - "materials-taconic-tly-series-rf-laminate"
  - "materials-taconic-rf35-ceramic-ptfe"
  - "materials-taconic-cer-series-high-dk"
  - "materials-taconic-tlx-moderate-loss-ptfe"
  - "materials-taconic-tlc-economy-ptfe"
  - "materials-taconic-bonding-materials"
  - "taconic_ptfe_laminate_family_parameters"
  - "materials-taconic-official-source-coverage-gap"
  - "materials-arlon-clte-xt-microwave"
  - "materials-arlon-tc350-thermal-rf"
  - "materials-arlon-ad-series-antenna"
  - "materials-arlon-official-source-coverage"
source_ids:
  - "rogers-ro4003c-product-page"
  - "rogers-ro4350b-product-page"
  - "rogers-ro3003-product-page"
  - "rogers-ro3006-product-page"
  - "rogers-ro3010-product-page"
  - "rogers-ro3035-product-page"
  - "rogers-rt-duroid-5880-product-page"
  - "rogers-tmm-family-datasheet"
  - "isola-astra-mt77-datasheet"
  - "isola-astra-mt77-dk-df-table"
  - "panasonic-megtron-6-r5775n"
  - "panasonic-megtron-7-r5785n"
  - "ventec-vt-870-datasheet"
  - "ventec-vtm1000i-datasheet"
  - "ventec-tec-speed-rf-family-page"
  - "agc-rf-30a-datasheet"
  - "agc-rf-10-datasheet"
  - "agc-rf-35htc-datasheet"
  - "agc-rf-microwave-laminates-page"
  - "frontendapt-taconic-pcb-json"
  - "frontendapt-arlon-pcb-json"
tags: ["rf-materials", "selector", "application", "frequency-band", "materials", "taconic", "arlon"]
---

# Definition

> RF material selection should be organized by application and path constraints, not by frequency band alone. The first-pass question is whether the build wants `process convenience`, `lower-loss RF routing`, `compact high-Dk structures`, or `thermally specialized microwave performance`.

## Why This Topic Matters

- Engineers often ask for a band-first answer when the real decision is driven by path length, phase sensitivity, enclosure size, and assembly constraints.
- The selector card gives a stable way to narrow candidate laminates without pretending one band maps to one universal substrate.
- This page is intended as a quick extraction point for internal wiki use, not as a full vendor comparison article.

## Stable Facts

### Official-Source-Backed Entries (Tier 1)

- `Mixed digital + RF, sub-6 GHz, cost-sensitive` usually starts with `RO4003C`, `RO4350B`, `Astra MT77`, `MEGTRON 6`, or `VT-870`.
- `High-speed digital + RF hybrid` usually starts with `MEGTRON 6`, `MEGTRON 7`, `Astra MT77`, or `RO4350B`.
- `Sub-6 to low tens of GHz, low-loss but still manufacturable at scale` usually starts with `RO3003`, `RO3035`, `Astra MT77`, `VT-870`, or `RF-30A`.
- `24 GHz to 40 GHz RF front ends` usually starts with `RO3003`, `RO3035`, or `RT/duroid 5880`.
- `77 GHz class radar and very low-loss mmWave routing` usually starts with `RO3003` or `RT/duroid 5880`.
- `Compact resonators and miniaturized RF structures` usually starts with `RO3006`, `RO3010`, `VTM1000i`, or `RF-10`.
- `High-volume antennas, passive RF, and PIM-sensitive commercial builds` usually starts with `RF-30A`, `VT-870`, or `RO4350B`.
- `Satellite communications, GPS antennas, filters, and couplers` usually starts with `VTM1000i`, `RO3010`, `RF-10`, or the `TMM` family.
- `High-power RF where heat spreading matters` usually starts with `RF-35HTC` or the `TMM` family.

### Taconic Additions — Tier-2 Internal Only

> All Taconic entries below are sourced from APTPCB internal JSON (`frontendapt-taconic-pcb-json`). Official Taconic RF laminate product pages are not currently confirmed recoverable. Do not publish these values externally without explicit source-gap pairing.

- `Ultra-low-loss: satellite LNA, Ka-band phased array, EW receivers, VNA calibration substrates` — `Taconic TLY-5A` (Dk 2.17, Df 0.0009) or `TLY-3` (Dk 2.33, Df 0.0009).
- `Lower-loss PTFE with compact trace geometry: base station duplexers, GPS patch arrays, T/R modules` — `Taconic TLX-8` (Dk 2.55, Df 0.0019).
- `Cost-entry PTFE for Wi-Fi 6/7, Bluetooth, ISM band, automotive V2X` — `Taconic TLC` (Dk 2.95–3.20, Df 0.0020).
- `Sub-6 GHz 5G antennas, PA pallets, WLAN enterprise AP, general commercial RF` — `Taconic RF-35A2` (Dk 3.50 ±0.05, Df 0.0018; ~51% lower loss than RO4350B; PTFE plasma required).
- `Miniaturized antennas, cavity filters, DRA` — `Taconic CER-10` (Dk 10.0) or `CER-20/30` (Dk 20–30).
- `High-power 5G base station PA, GaN amplifiers` — `Taconic TF-260` (Dk 2.60) or `TF-290` (Dk 2.90); thermally optimized PTFE.
- `Hybrid Taconic/FR-4 multilayer bonding` — `fastRise 27` (Dk 2.72, Df 0.0014); also compatible with Rogers RO4350B cores.
- `All-PTFE stripline for satellite transponders, defense radar panels` — `TacLam` (Dk 2.10–2.35, Df 0.0008).

### Arlon Additions — Tier-2 Internal Only (RF/PTFE Families)

> Arlon CLTE-XT, TC350/600, AD250/300/1000 are sourced from APTPCB internal JSON (`frontendapt-arlon-pcb-json`). No current official Arlon product pages confirmed for these families. Do not publish externally without source-gap pairing. Arlon N-series (33N–85N) and 86HP are official-backed; see `arlon-material-family-source-governance.md`.

- `Low-PIM phased-array radar and cellular base station feeds` — `Arlon CLTE-XT` (Dk 2.94–3.00, Df 0.0012; Z-axis CTE copper-matched for PTH reliability).
- `High-power amplifiers, GaN/GaAs device mounting, tower-mounted amplifiers` — `Arlon TC350` (Dk 3.50, Df 0.0020, thermal conductivity 1.0 W/m·K) or `TC600` (Dk 6.15).
- `GPS/GNSS patch antennas, DRA, broadband base station antennas` — `Arlon AD250` (Dk 2.50) or `AD300` (~3.00); Df 0.0014.
- `Extreme miniaturization: GPS L1/L2 patches, miniaturized filters, compact cavity` — `Arlon AD1000` (Dk 10.2, Df 0.0014; ~3× size reduction vs FR-4).

## Source Tier Governance

| Tier | Entries | External Publishable? |
|------|---------|-----------------------|
| **Tier 1 — Official** | Rogers, Isola, Panasonic, Ventec, AGC | ✅ With standard citation |
| **Tier 2 — Internal only** | Taconic (APTPCB JSON), Arlon RF/PTFE families (APTPCB JSON) | ⚠️ Internal use only; must pair source-gap note if published |
| **Tier 1 — Official (Arlon non-RF)** | Arlon N-series (33N–85N), 86HP | ✅ With standard citation |

## Engineering Boundaries

- Frequency band alone is insufficient for selection.
- Path length, phase error, and insertion-loss budget can change the right answer even within the same band.
- Dk tolerance and Df must be kept with their measurement method and frequency.
- Copper choice and copper profile matter, especially for low-loss and mmWave routing.
- Finish choice can move loss, solderability, and launch behavior enough to change the material shortlist.
- Thermal path and heat spreading can dominate the decision in power RF, compact enclosures, and antenna arrays.
- Fabricator capability is a selection constraint, not a back-end detail.
- A material that looks right on paper may still be the wrong answer if the shop cannot process the stackup reliably.

## Common Misreadings

- `Higher Dk` does not automatically mean `better for mmWave`.
- `Lower loss` does not remove the need to check tuning, transition design, and real assembly conditions.
- `FR-4-compatible processing` does not mean all RF laminates are interchangeable in fabrication.
- `Commercial antenna material` does not mean the same laminate is the best choice for every antenna geometry or power level.
- `Taconic RF-35A2 and Rogers RO4350B have matched Dk` does not mean they are drop-in substitutes; RF-35A2 requires PTFE plasma desmear while RO4350B uses FR-4 chemistry — fabrication routes differ.
- `Tier-2 Taconic/Arlon entries appear in selector` does not mean they are officially validated; they require source-gap pairing before external publication.

## Must Refresh Before Publishing

- Any change to the underlying selector card or supplier fact cards
- Any new vendor card that should alter the application buckets

## Related Fact Cards

- `materials-rf-selector-by-application`
- `materials-rogers-ro3003`
- `materials-rogers-ro3006`
- `materials-rogers-ro3035`
- `materials-isola-astra-mt77`
- `materials-panasonic-megtron-6`
- `materials-panasonic-megtron-7`
- `materials-ventec-vt-870`
- `materials-ventec-vtm1000i`
- `materials-agc-rf-30a`
- `materials-agc-rf-10`
- `materials-agc-rf-35htc`
- `materials-taconic-tly-series-rf-laminate` [Tier-2]
- `materials-taconic-rf35-ceramic-ptfe` [Tier-2]
- `materials-taconic-cer-series-high-dk` [Tier-2]
- `materials-taconic-tlx-moderate-loss-ptfe` [Tier-2]
- `materials-taconic-tlc-economy-ptfe` [Tier-2]
- `materials-taconic-bonding-materials` [Tier-2]
- `materials-arlon-clte-xt-microwave` [Tier-2]
- `materials-arlon-tc350-thermal-rf` [Tier-2]
- `materials-arlon-ad-series-antenna` [Tier-2]
- `wiki/materials/taconic-material-family-source-governance.md` (Taconic tier map)
- `wiki/materials/arlon-material-family-source-governance.md` (Arlon tier map)

## Primary Sources

- https://www.rogerscorp.com/advanced-electronics-solutions/ro4000-series-laminates/ro4003c-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro4000-series-laminates/ro4350b-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3003-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3006-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3010-laminates
- https://rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3035-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/rt-duroid-laminates/rt-duroid-5880-laminates
- https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/tmm-thermoset-laminate-data-sheet-tmm3----tmm4----tmm6----tmm10----tmm10i----tmm13i.pdf
- https://isola-group.com/wp-content/uploads/data-sheets/astra-mt77.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/astra-mt77-laminate-and-prepreg__Dk_Df_Tables.pdf
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/megtron-series/series/127603/model/131590
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/lineup/megtron-series/series/127604/model/131596
- https://www.ventec-group.com/media/1957/180720tecspeed20-vt-870.pdf
- https://www.ventec-group.com/media/114432/230320tecspeed20-vtm1000i.pdf
- https://www.ventec-group.com/products/tec-speed-rf/
- https://www.agc-multimaterial.com/agc-downloads/AGC_RF-30A_TDS.pdf
- https://www.agc-multimaterial.com/agc-downloads/AGC_RF-10_TDS.pdf
- https://www.agc-multimaterial.com/agc-downloads/AGC_RF-35HTC_TDS.pdf
- https://www.agc-multimaterial.com/rfmicrowave-laminates/
