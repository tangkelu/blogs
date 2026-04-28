# P4-38 2025.7 Mixed Service Official-Source Recovery Scout

Date: 2026-04-28

## Purpose And Assigned Lane

Lane `P4-38` audits the five `/code/blogs/tmps/2025.7/en` mixed-service drafts as claim inventory only, then identifies:

- existing `llm_wiki` support already usable for conservative upgrades
- official or durable source candidates worth recovering next
- exact claims that remain blocked without dated capability records or stronger primary sources

This lane does not promote draft-originated capability, numeric, quality, lead-time, MOQ, yield, equipment, certification, reliability, or supplier claims into facts.

## Input Files Inspected

- `/code/blogs/tmps/2025.7/en/Rogers PCB.md`
- `/code/blogs/tmps/2025.7/en/keyboard-pcb-types.md`
- `/code/blogs/tmps/2025.7/en/pcba-service.md`
- `/code/blogs/tmps/2025.7/en/smt-assembly.md`
- `/code/blogs/tmps/2025.7/en/through-hole-assembly.md`
- `/code/blogs/llm_wiki/logs/p4-32-2025-7-mixed-service-blog-ingestion-map.md`

## Claim Families Found In Drafts

### Rogers PCB

- Rogers family positioning for RF, microwave, mmWave, radar, aerospace, telecom, and medical uses
- exact-product material naming such as `RO4350B`, `TMM`, `RT/duroid`, `CLTE`, `AD`, and `DIALAM`
- material-property claims including `Dk`, `Df`, thermal conductivity, frequency suitability, and cost/performance tradeoffs
- processing claims around PTFE handling, drilling, routing, lamination, plating, adhesion, mixed-dielectric builds, and finish compatibility
- Highleap-specific capability and partner-selection claims

### Keyboard PCB Types

- market segmentation by gaming, enterprise, mobile, developer, and maker audiences
- feature clusters around `QMK`, `VIA`, hot-swap, RGB, wireless, split layouts, compact layouts, and `USB-C`
- keyboard layout taxonomy such as full-size, `TKL`, `75%`, `65%`, `60%`, split, and macro-pad
- manufacturing and scaling claims around BOM, stackup, DFM, ICT/FCT, fulfillment, and rapid prototyping
- unsupported market-size, growth-rate, cost, turnaround, and Highleap execution claims

### PCBA Service / SMT / Through-Hole

- turnkey PCBA flow from bare board through sourcing, assembly, inspection, test, and ramp
- SMT process chain: stencil, paste, placement, reflow, SPI, AOI, X-ray, ICT, FCT, and traceability
- THT and mixed-technology route selection: manual insertion, auto insertion, wave solder, selective solder, press-fit, and mixed SMT+THT sequencing
- quality-system and release-gate claims around FAI, IQC, FQI, traceability, burn-in, environmental stress, and inspection archives
- Highleap-specific claims for equipment brands, placement speed, accuracy, capacity, volume, lead time, MOQ, bilingual support, certifications, and quality outcomes

## Existing llm_wiki Support Found, With Paths/IDs

### Batch-Level Consumption Boundary

- `fact_id: methods-2025-7-mixed-service-draft-consumption-boundary`
  - Path: `/code/blogs/llm_wiki/facts/methods/2025-7-mixed-service-draft-consumption-boundary.md`
  - Confirms this batch routes to existing Rogers and PCBA/THT/SMT layers, while keyboard remains claim-family-only.

### Rogers / RF Material And Process Support

- `topic_id: materials-rogers-ro3000-family`
  - Path: `/code/blogs/llm_wiki/wiki/materials/rogers-ro3000-family.md`
- `source_id: rogers-ro3000-series-product-page`
  - Path: `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro3000-series-product-page.md`
- `source_id: rogers-ro3000-fabrication-guidelines`
  - Path: `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro3000-fabrication-guidelines.md`
- additional exact-product and process support already present in local search:
  - `rogers-ro3010-product-page`
  - `rogers-ro3035-product-page`
  - `rogers-rt-duroid-6202-datasheet`
  - `rogers-ro4835ind-lopro-datasheet`
  - `/code/blogs/llm_wiki/wiki/processes/ptfe-processing-and-manufacturability.md`
  - `/code/blogs/llm_wiki/wiki/processes/hybrid-rf-stackup-strategy.md`
  - `/code/blogs/llm_wiki/wiki/processes/rf-drilling-and-transition-control.md`

### PCBA / SMT / THT Existing Support

- `topic_id: processes-pcba-npi-to-mass-production-flow`
  - Path: `/code/blogs/llm_wiki/wiki/processes/pcba-npi-to-mass-production-flow.md`
- `topic_id: processes-mixed-technology-solder-route-selection`
  - Path: `/code/blogs/llm_wiki/wiki/processes/mixed-technology-solder-route-selection.md`
- useful internal source records already registered:
  - `frontendapt-pcba-smt-tht-page-en`
  - `frontendhil-smt-assembly-product-page-en`
  - `frontendhil-through-hole-assembly-product-page-en`
  - `frontendhil-turnkey-assembly-product-page-en`
  - `frontendapt-pcba-spi-inspection-page-en`
  - `frontendapt-pcba-aoi-inspection-page-en`
  - `frontendapt-pcba-xray-inspection-page-en`
  - `frontendapt-pcba-ict-test-page-en`
  - `frontendapt-pcba-fct-test-page-en`
  - `frontendapt-pcba-pcb-stencil-page-en`
  - `frontendapt-pcba-pcb-selective-soldering-page-en`
  - `frontendapt-pcba-quality-system-page-en`

### Keyboard Boundary Support

- `fact_id: methods-hilpcb-blog1-13-input-device-draft-consumption-boundary`
  - Path: `/code/blogs/llm_wiki/facts/methods/hilpcb-blog1-13-input-device-draft-consumption-boundary.md`
- `logs/p4-30-hilpcb-blog1-13-ingestion-map.md`
  - points to official-source gap families for `QMK`, `VIA`, hot-swap vendors, Bluetooth SIG, USB-IF, FCC, and EU RED / CE

## Official Sources Checked Or Candidate Official Sources To Recover

### Checked In Existing Local Support

- Rogers official family and product sources already present locally for conservative Rogers upgrades:
  - `rogers-ro3000-series-product-page`
  - `rogers-ro3000-fabrication-guidelines`
  - exact-product Rogers records already registered in `llm_wiki`
- IPC public metadata anchors already present locally for guarded assembly vocabulary:
  - `ipc-j-std-001j-toc`
  - `ipc-a-610h-toc`
- method/vendor-primary sources already present locally for inspection/test framing:
  - `koh-young-spi-technology`
  - `koh-young-aoi-technology`
  - `keysight-ict-systems`
- broader test/inspection scout already available:
  - `/code/blogs/llm_wiki/logs/p4-36-2025-7-28-testing-quality-official-source-recovery-scout.md`

### Strong Candidate Official Sources To Recover Next

- Rogers official product pages or datasheets for draft-named families not yet explicitly mapped in this lane log:
  - `RO4350B`
  - `TMM` family
  - `RT/duroid 5880`
  - `CLTE`
  - `AD / DIALAM`
- keyboard-specific official or standards-owner sources if that draft is ever promoted beyond claim inventory:
  - official `QMK` documentation
  - official `VIA` documentation
  - official hot-swap socket vendor pages such as `Kailh` or other named socket manufacturers
  - official `USB-IF` language / connector / functional-test pages for guarded `USB-C` vocabulary only
  - official `Bluetooth SIG` specification / qualification context for wireless keyboard vocabulary
  - official `FCC` and EU `RED / CE` entry-point pages for compliance-program context only
- assembly/test official or vendor-primary sources for more neutral process framing where internal pages are too capability-heavy:
  - IPC `TM-650 2.6.8E` plated-through-hole thermal-stress method identity
  - official ICT / flying-probe vendor pages already flagged in `P4-36` for ICT-vs-FCT boundary recovery

## Strongest Source-Backed Fact-Upgrade Opportunities

- `Rogers PCB.md`
  - upgrade generic `Rogers is used in RF/microwave/mmWave` language from existing Rogers family pages and local RF process wiki pages
  - replace vague PTFE-processing prose with source-backed Rogers fabrication-guideline language around handling, bonding, drilling, and multilayer process context
  - recover only exact-product properties already registered in `llm_wiki`; do not reuse family-wide or unsourced draft numerics

- `pcba-service.md`
  - rewrite the service-flow skeleton from `processes-pcba-npi-to-mass-production-flow`
  - keep sourcing, traceability, inspection, ICT, FCT, and box-build as staged workflow vocabulary rather than proof of current Highleap capacity

- `smt-assembly.md`
  - rewrite SPI/AOI/X-ray/ICT/FCT layering from existing internal source-backed process cards
  - use `Koh Young` and `Keysight` method pages only to clarify what SPI, AOI, and ICT are for, not to prove Highleap owns specific tools or achieves draft-stated throughput

- `through-hole-assembly.md`
  - safely upgrade THT definition, mixed-technology route selection, and wave/selective/manual solder distinctions from existing mixed-technology topic pages
  - use IPC public metadata only for standards identity, not class-specific acceptability or hole-fill thresholds

- `keyboard-pcb-types.md`
  - only reusable now: keyboard layout/type taxonomy and generic PCB/PCBA workflow context
  - future upgrade path exists only after separate official-source lanes for firmware, hot-swap, wireless, and compliance topics

## Blocked Claims Needing Dated Capability Records Or Official Sources

- all Highleap-specific claims for:
  - in-house Rogers breadth
  - turnkey completeness
  - equipment brands
  - placement speed and accuracy
  - line capacity and monthly volume
  - prototype and production lead times
  - MOQ
  - response-time promises
  - certifications or operator training claims
  - quality outcomes, yield, reliability, or archive/report availability

- draft-originated numeric or threshold claims, including:
  - Rogers material values not already tied to exact official product records
  - keyboard market size, market growth, user percentages, layer-count defaults, unit-volume thresholds, turnaround days, and stackup requirements
  - SMT/THT process windows, placement accuracy, throughput, inspection coverage rates, and environmental-test claims
  - THT hole-clearance and solder-process parameter claims

- keyboard-specific claims blocked pending separate official-source recovery:
  - `QMK` / `VIA` compatibility
  - hot-swap durability or vendor interchangeability
  - RGB electrical/current/thermal implications
  - Bluetooth or other wireless behavior
  - `USB-C` implementation details
  - FCC / CE / RED / Bluetooth qualification claims

## Residual Gaps

- no dated non-blog capability record was recovered in this lane for current Highleap SMT, THT, turnkey PCBA, sourcing, inspection, scale, delivery, or certification assertions
- keyboard article remains mostly blocked beyond layout taxonomy and generic process context
- Rogers family coverage is usable, but draft-named families beyond already-registered exact products still need explicit source mapping if future rewrites want broader portfolio detail
- IPC public metadata anchors remain insufficient for detailed acceptability criteria, hole-fill rules, solder-joint classes, or process windows
- vendor-primary SPI/AOI/ICT pages help define methods, but they do not convert into supplier-specific equipment or quality proof

## Completion Status Using Standard Labels

- lane status: `completed`
- evidence outcome: `existing_support_mapped`
- official-source recovery outcome: `candidate_recovery_targets_identified`
- blocked-claim outcome: `high_risk_claims_held`
- publish readiness for this batch:
  - `Rogers PCB.md`: `partial_source_backed_upgrade_possible`
  - `pcba-service.md`: `partial_source_backed_upgrade_possible`
  - `smt-assembly.md`: `partial_source_backed_upgrade_possible`
  - `through-hole-assembly.md`: `partial_source_backed_upgrade_possible`
  - `keyboard-pcb-types.md`: `claim_inventory_only`
