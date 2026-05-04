---
fact_id: "materials-rf-selector-by-application"
title: "RF material selector by application and frequency band"
topic: "RF material selection by application"
category: "materials"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-05-03"
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

# Canonical Summary

> RF material selection should be organized by real application constraints, not by a generic "best high-frequency laminate" idea. In practice, the first split is usually between `FR-4-like process convenience`, `lower-loss RF routing`, `very high-Dk compactness`, and `thermally or mechanically specialized microwave builds`.

## Stable Facts

- RO4003C and RO4350B are the current registry options most explicitly aligned with epoxy/glass-style processing.
- Panasonic MEGTRON 6 and MEGTRON 7 add process-friendly low-loss multilayer options oriented more toward high-speed digital, networking, and high-layer-count builds.
- Ventec VT-870 adds a hydrocarbon-ceramic RF option positioned around antennas, power amplifiers, automotive radar, and PIM-sensitive builds.
- AGC RF-30A adds a high-volume antenna and passive-RF option with PIM-aware framing, while RF-35HTC adds a high-power thermal-performance path and RF-10 adds a compact high-Dk path.
- RO3003, RT/duroid 5880, and Astra MT77 are the current lower-loss options with materially lower published Df than RO4003C or RO4350B.
- RO3006, RO3010, VTM1000i, and RF-10 are the current higher-Dk options in the registry for compact RF structures.
- RO3035 sits between the lower-Dk low-loss materials and the higher-Dk compactness materials.
- The TMM family is the current thermoset-microwave option in the registry when dimensional stability, plated-through-hole behavior, and in some grades higher thermal conductivity matter.
- **[Tier-2 internal only]** Taconic TLY series (Dk ~2.17–2.33, Df 0.0009 @ 10 GHz) is the lowest-loss Taconic family; recovered via APTPCB internal JSON; no current official Taconic product pages confirmed.
- **[Tier-2 internal only]** Taconic RF-35A2 (Dk 3.50 ±0.05, Df 0.0018) offers ~51% lower loss than RO4350B at matched Dk and cost; requires PTFE plasma desmear (different from RO4350B's FR-4 chemistry).
- **[Tier-2 internal only]** Taconic CER-10 (Dk 10.0) and CER-20/30 (Dk 20–30) are the highest-Dk compact-structure options in the registry for dielectric resonator antennas and miniaturized cavity filters.
- **[Tier-2 internal only]** Arlon CLTE-XT (Dk ~2.94–3.00, Df 0.0012) adds a low-PIM PTFE/ceramic path for phased-array radar and cellular base station feeds; no current official Arlon product page.
- **[Tier-2 internal only]** Arlon TC350 (Dk 3.50, Df 0.0020, thermal conductivity 1.0 W/m·K) adds a thermally enhanced PTFE path for high-power amplifiers, GaN mounting, and tower-mounted amplifiers.
- **[Tier-2 internal only]** Arlon AD series (AD250 Dk 2.50, AD300 ~3.00, AD1000 Dk 10.2; Df 0.0014 across grades) adds antenna-grade PTFE across a wide Dk range; AD1000 enables 3× size reduction vs. FR-4.

## Application Mapping

- `Mixed digital + RF, sub-6 GHz, cost-sensitive`
  Most likely starting points: `RO4003C`, `RO4350B`, `Astra MT77`, `MEGTRON 6`, `VT-870`
  Also consider [Tier-2]: `Taconic RF-35A2` (lower Df than RO4350B, PTFE processing required)
  Reason: these options preserve a more production-friendly process posture than soft PTFE families while still improving RF loss behavior over generic FR-4, though `VT-870` is more explicitly RF-oriented than the Panasonic multilayer families.

- `High-speed digital + RF hybrid, server / router / data-heavy backplane context`
  Most likely starting points: `MEGTRON 6`, `MEGTRON 7`, `Astra MT77`, `RO4350B`
  Reason: Panasonic explicitly positions MEGTRON 6 and 7 around high-speed, large-data, HDI, and high-layer-count environments where mixed digital and RF constraints often coexist.

- `Sub-6 to low tens of GHz, low-loss but still manufacturable at scale`
  Most likely starting points: `RO3003`, `RO3035`, `Astra MT77`, `VT-870`, `RF-30A`
  Also consider [Tier-2]: `Taconic TLX-8` (Df 0.0019, Dk 2.55), `Arlon CLTE-XT` (Df 0.0012, low-PIM)
  Reason: these options offer lower-loss RF paths than generic FR-4-style materials, while `VT-870` stays in the hydrocarbon-ceramic manufacturing posture and `RF-30A` adds reinforced PTFE behavior for volume antenna and passive-RF builds.

- `24 GHz to 40 GHz RF front ends, insertion loss and phase control matter`
  Most likely starting points: `RO3003`, `RO3035`, `RT/duroid 5880`
  Also consider [Tier-2]: `Taconic TLY-5A` (Df 0.0009, Dk 2.17)
  Reason: low published Df and RF-oriented positioning make them stronger candidates when path loss and phase behavior start dominating.

- `77 GHz class radar and very low-loss mmWave routing`
  Most likely starting points: `RO3003`, `RT/duroid 5880`
  Also consider [Tier-2]: `Taconic TLY-5A` (Df 0.0009 matches RT/duroid 5880 class)
  Reason: the current registry positions RO3003 explicitly around 77 GHz / ADAS framing, while RT/duroid 5880 carries the lowest published loss in the current set.

- `Compact resonators, miniaturized RF structures, constrained enclosure`
  Most likely starting points: `RO3006`, `RO3010`, `VTM1000i`, `RF-10`
  Also consider [Tier-2]: `Taconic CER-10` (Dk 10.0), `Taconic CER-20/30` (Dk 20–30), `Arlon AD1000` (Dk 10.2)
  Reason: higher Dk lets physical structures shrink, but the loss, tolerance, and temperature budget still need review.

- `High-volume antennas, passive RF, and PIM-sensitive commercial builds`
  Most likely starting points: `RF-30A`, `VT-870`, `RO4350B`
  Also consider [Tier-2]: `Arlon CLTE-XT` (low-PIM posture, cellular feeds), `Taconic RF-35A2` (sub-6 GHz 5G small-cell antennas)
  Reason: these options are the current registry entries most explicitly aligned with antenna volume, passive RF, or PIM-aware commercial deployment tradeoffs.

- `Satellite communications, GPS antennas, filters, couplers`
  Most likely starting points: `VTM1000i`, `RO3010`, `RF-10`, `TMM family`
  Also consider [Tier-2]: `Taconic TLY-5A` (satellite LNA boards, Ka-band phased-array), `Taconic CER-10` (miniaturized GPS L1/L2 patches), `Arlon AD250/300` (GPS/GNSS patch antennas)
  Reason: these options are the current registry entries most explicitly aligned with compact or high-Dk microwave structures where electrical size control matters.

- `Power RF, beamforming hardware, or microwave structures where thermally stronger thermoset options matter`
  Most likely starting points: `TMM family`, especially thermally enhanced grades such as `TMM 10i`
  Also consider [Tier-2]: `Arlon TC350` (thermal conductivity 1.0 W/m·K, GaN and GaAs PA mounting), `Taconic TF-260/290` (thermally optimized PTFE for 5G base station PA)
  Reason: the family datasheet explicitly provides thermoset-microwave framing, plated-through-hole suitability, and stronger thermal-conductivity options in the `i` variants.

- `High-power RF where dielectric heat spreading is a first-order concern`
  Most likely starting points: `RF-35HTC`, `TMM family`
  Also consider [Tier-2]: `Arlon TC350` (Dk 3.50, Df 0.0020, 1.0 W/m·K, tower-mounted amplifiers), `Taconic TF-260/290` (thermally optimized PTFE)
  Reason: `RF-35HTC` is the current registry entry most explicitly centered on very high thermal conductivity for filters, couplers, dividers, and power amplifiers, while `TMM` remains the thermoset-microwave alternative when plated-through-hole and dimensional-stability tradeoffs matter.

## Conditions And Methods

- This card is an engineering selection aid inferred from official product properties and product positioning.
- It should be used to narrow options, not to finalize material selection.
- Final selection should still validate `loss budget`, `stackup`, `surface finish`, `copper profile`, `thermal path`, and `fabricator capability`.

## Limits And Non-Claims

- This card does not claim any listed material is the universal best choice for a frequency band.
- Frequency band alone is not enough; path length, phase sensitivity, enclosure size, assembly route, and cost target also matter.
- **[Tier-2 governance boundary]** All Taconic entries in this card are sourced from APTPCB internal JSON (`frontendapt-taconic-pcb-json`), not from official Taconic product pages or datasheets. Current official Taconic RF laminate product pages are not confirmed recoverable (as of 2026-05-02). Do not publish Taconic Dk/Df values externally without explicit Tier-2 source-gap pairing.
- **[Tier-2 governance boundary]** Arlon CLTE-XT, TC350, and AD series entries are sourced from APTPCB internal JSON (`frontendapt-arlon-pcb-json`); no current official Arlon product pages or datasheets confirmed for these families. Do not publish these values externally without explicit source-gap pairing. Arlon N-series and 86HP are official-backed and are not affected by this boundary.
- Taconic TLY and Arlon CLTE-XT both require PTFE plasma desmear; fabricator PTFE capability is a selection constraint, not a secondary concern.

## Open Questions

- Confirm whether official Taconic RF laminate product pages (TLY, TLX, RF-35) become accessible under new URLs
- Confirm current Arlon/AGC product-line continuity for CLTE-XT, TC350, and AD series under official domain
- Add a dedicated application card for `antenna arrays`, `high-speed + RF hybrids`, and `satcom front ends` once official source anchors improve

## Source Links

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
