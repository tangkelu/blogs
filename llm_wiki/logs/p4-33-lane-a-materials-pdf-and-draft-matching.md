# P4-33 Lane A Audit: TMPS Materials PDF And Draft Matching

Date: 2026-04-28

## Purpose

Inspect the TMPS materials-PDF pool and the material-heavy English draft batches, then record how far the current `llm_wiki` already supports them.

This pass treats drafts as claim inventory only. It does not promote draft-originated material values, capability claims, cost, lead time, MOQ, yield, quality-rate, certification, or supplier-proof language into facts.

## Input Files Inspected

Input roots:

- `/code/blogs/tmps/materias_pdf`
- `/code/blogs/tmps/2025.7.22/en`
- `/code/blogs/tmps/2025.7.23/en`
- `/code/blogs/tmps/2025.12.10/en`
- `/code/blogs/tmps/2026.2.25/en`
- `/code/blogs/tmps/2026.3/en`

Draft files inspected by batch:

- `2025.7.22/en`
  - `fr4-materia.md`
  - `edge-plated-pcb.md`
  - `rogers-4003c-pcb.md`
  - `stretchable-pcb.md`
  - `rogers-pcb.md`
  - `gold-finger-pcb.md`
  - `rogers-4350b-pcb.md`
  - `rogers-4350b.md`
  - `transparent-pcb.md`
  - `biodegradable-pcb.md`
- `2025.7.23/en`
  - `alumina-pcb.md`
  - `isola-pcb.md`
  - `waterproof-pcb.md`
  - `thermally-conductive-pcb.md`
  - `pcb_surface_finish_guide.md`
  - `teflon-pcb.md`
  - `immersion-gold-pcb.md`
  - `enig-pcb.md`
  - `hasl-pcb.md`
  - `kapton-pcb.md`
  - `enepig-pcb.md`
  - `lead-free-hasl-pcb.md`
  - `high-tg-pcb.md`
  - `ptfe-pcb.md`
  - `pcb-insulation.md`
  - `peelable-mask-pcb.md`
  - `epoxy-pcb.md`
  - `hybrid-circuit-board.md`
  - `ltcc-pcb.md`
  - `aluminum-nitride-pcb.md`
  - `pcb-copper-foil.md`
  - `taconic-pcb.md`
  - `osp-pcb.md`
  - `polyimide-pcb.md`
  - `ceramic-circuit-board-manufacturing.md`
  - `immersion-silver-pcb.md`
- `2025.12.10/en`
  - `ro4003c-pcb-china.md`
  - `high-frequency-pcb-lifecycle.md`
  - `rogers-ro4350b-pcb.md`
  - `ro4003c-pcb-fabrication.md`
  - `high-frequency-pcb-for-radar.md`
  - `high-frequency-pcb-manufacturing.md`
  - `ceramic-pcb-materials.md`
  - `ro4003c-pcb-manufacturer.md`
  - `ro4350b-pcb.md`
  - `china-high-frequency pcb-manufacturer.md`
- `2026.2.25/en`
  - `kb-6160f-kb-6160lc-pcb.md`
  - `kb-6165-pcb.md`
  - `kb-6169gt-pcb.md`
  - `kb-6150-pcb.md`
  - `kb-3200g-pcb.md`
  - `kb-6167gmd-pcb.md`
  - `hf-140-hf-170-pcb.md`
  - `kb-6165c-kb-6165le-pcb.md`
  - `kb-6167f-pcb.md`
  - `kb-6168le-pcb.md`
  - `kb-6164-pcb.md`
  - `kb-6160a-pcb.md`
  - `kb-6160-pcb.md`
  - `pi-515g-pi-520g-pcb.md`
  - `kingboard-pcb-laminate.md`
  - `kb-6167gld-pcb.md`
  - `kb-6165f-pcb.md`
- `2026.3/en`
  - `rogers-ro3006-rf-pcb.md`
  - `ro3003-pcb-fabrication.md`
  - `rogers-ro3003-high-frequency-pcb.md`
  - `rogers-ro3006-pcb-fabrication.md`
  - `ro3003-pcb-cost.md`
  - `ro3003-pcb.md`
  - `ro3003-quick-turn-pcb.md`
  - `rogers-ro3006-microwave-pcb.md`
  - `rogers-ro3003-mmwave-pcb.md`
  - `rogers-ro3003-rf-pcb.md`
  - `ro3003-pcb-manufacturing.md`
  - `rogers-ro3006-pcb.md`
  - `rogers-ro3006-pcb-manufacturer.md`
  - `ro3003-custom-pcb.md`
  - `rogers-ro3003-low-loss-pcb.md`
  - `rogers-circuit-board-design.md`
  - `ro3003-pcb-manufacturer.md`
  - `rogers-ro3003-microwave-pcb.md`
  - `ro3003-pcb-supplier.md`
  - `ro3003-pcb-assembly.md`

PDF pool inspected at filename-family level:

- Rogers: `RO3000`, `RO4000`, `RO4360G2`, `RO4835`, `RO3003G2`, `RT-duroid`, `TMM`, `RO4500`, `RO4400`
- Taconic / Arlon-adjacent: `Taconic RF-35`, `CuClad`, `DiClad`, `IsoClad`, `TC350`, `TC350 Plus`, `TC600`, `TLY`, `TLX`, `TLE`, `TLC`, `TLF`, `RF-*`
- AGC: `METEORWAVE`, `N4000`, `N7000`, `RF-*`, `TLY`, `TLX`, `TSM`, `ELL`, `NF-30`
- Ventec: `VT-4BC`, `VT-464LT`, `VT-47`, `VT-42`, `VT-441`, `VT-463H`, `VT-481`, `VT-6735`, `VT-6880`, `VT-770`, `VT-870`, `VT-901`
- Shengyi: large pool covering `S1141`, `S1150G`, `S1600`, `Autolad`, `LNB33`, `mmWave`, and related families
- TU / Taiwan Union and other families: `tu-668`, `tu-768`, `tu-787`, `tu-865`, `tu-872`, `tu-901`, `thunderclad`, `SCGA`

Inspection limit:

- `pdftotext` is not available in this workspace, so PDFs were matched by filename and family only during this lane.

## Existing `llm_wiki` Support Found

Strong existing support already exists for these material families and boundary layers:

- Rogers RF materials:
  `facts/materials/rogers-ro3003.md`
  `facts/materials/rogers-ro3006.md`
  `facts/materials/rogers-ro4003c.md`
  `facts/materials/rogers-ro4350b.md`
  `facts/materials/rogers-ro3003-vs-ro3006.md`
  `facts/materials/rogers-material-selector.md`
  `wiki/materials/rogers-ro3000-family.md`
  `wiki/materials/rf-material-selector-by-application-band.md`
- Kingboard laminate family:
  `facts/materials/kingboard-material-selection-boundaries.md`
  `facts/materials/kingboard-kb-6150.md`
  `facts/materials/kingboard-kb-6160a.md`
  `facts/materials/kingboard-kb-6165.md`
  `facts/materials/kingboard-kb-6165c.md`
  `facts/materials/kingboard-kb-6167gld.md`
  `facts/materials/kingboard-hf-170.md`
  `facts/materials/kingboard-pi-520g.md`
  `wiki/materials/kingboard-laminate-selection-and-boundaries.md`
- Flex / PTFE / ceramic / thermal-platform posture:
  `facts/materials/dupont-kapton-hn.md`
  `facts/materials/site-material-baseline-gap-map.md`
  `facts/materials/site-material-baseline-follow-on-gap-control.md`
  `wiki/materials/flex-material-classes-pi-lcp-and-rigid-flex-boundaries.md`
  `wiki/materials/ceramic-aln-ims-thermal-platforms.md`
- Process and consumption boundaries:
  `wiki/processes/ptfe-processing-and-manufacturability.md`
  `wiki/processes/hybrid-rf-stackup-strategy.md`
  `wiki/processes/rf-surface-finish-selection.md`
  `wiki/processes/finish-zoning-and-selective-multi-finish.md`
  `wiki/processes/prototype-vs-quick-turn-pcb-routing.md`
  `facts/methods/pcb-prototype-quickturn-and-volume-routing.md`
  `facts/methods/controlled-impedance-tdr-verification-posture.md`
  `facts/methods/hidden-joint-xray-inspection-boundary.md`
  `facts/methods/2025-7-mixed-service-draft-consumption-boundary.md`

Current support is still weak or absent for several draft families in this lane:

- edge-plating, gold-finger, waterproof, peelable-mask, transparent, stretchable, biodegradable, and generic insulation narratives
- exact finish chemistry cards for `HASL`, `lead-free HASL`, `OSP`, `immersion silver`, `immersion gold`, and `ENEPIG` beyond current posture-level selection logic
- exact product cards for many `Shengyi`, `Ventec`, `AGC`, `Taconic`, `TU`, and ceramic product families that appear in the PDF pool
- supplier / China-manufacturer / quick-turn / cost / stock / certification / lead-time / authenticity / audit narratives at reusable-fact level

## Per-Batch Disposition

### `2025.7.22/en`

Disposition: `completed_at_claim_family_level`

Usable now:

- FR-4 topic intent and baseline-material framing
- Rogers family topic intent tied to existing RO4003C / RO4350B / Rogers selector cards
- general special-process labels such as edge plating and gold finger as topic clusters only

Blocked or downgraded:

- Highleap capability, quality, equipment, and supplier-proof language
- unsupported special-board narratives such as transparent, stretchable, and biodegradable PCB as fact claims
- numeric FR-4 or Rogers values copied from draft prose when not pulled from existing fact cards

Batch verdict:

- `rogers-4003c-pcb.md`, `rogers-4350b-pcb.md`, `rogers-4350b.md`, and `rogers-pcb.md` are partially covered by current Rogers facts and process wiki
- `fr4-materia.md` is only safe at generic material-family level
- `edge-plated-pcb.md`, `gold-finger-pcb.md`, `transparent-pcb.md`, `stretchable-pcb.md`, and `biodegradable-pcb.md` remain mostly `topic_inventory_only`

### `2025.7.23/en`

Disposition: `completed_at_claim_family_level`

Usable now:

- ceramic / alumina / AlN / thermal-platform class framing
- PTFE / Teflon / Taconic / Kapton / polyimide topic clustering with existing boundary support
- surface-finish choice as qualitative workflow language

Blocked or downgraded:

- finish thickness, shelf life, black-pad, solderability ranking, pore/corrosion, and chemistry-outcome claims
- exact dielectric, thermal, insulation, copper-foil, LTCC, or waterproof numeric/property claims without official class or product anchor
- HIL / factory capability, certification, lead-time, and volume-readiness language

Batch verdict:

- `alumina-pcb.md`, `aluminum-nitride-pcb.md`, `ceramic-circuit-board-manufacturing.md`, and `thermally-conductive-pcb.md` are usable only through existing ceramic / thermal-platform posture
- `teflon-pcb.md`, `ptfe-pcb.md`, `taconic-pcb.md`, `kapton-pcb.md`, and `polyimide-pcb.md` are partially supported at material-family boundary level
- `enig-pcb.md`, `immersion-gold-pcb.md`, `immersion-silver-pcb.md`, `enepig-pcb.md`, `hasl-pcb.md`, `lead-free-hasl-pcb.md`, `osp-pcb.md`, and `pcb_surface_finish_guide.md` remain guarded by finish-selection posture and do not unlock exact finish numerics
- `waterproof-pcb.md`, `pcb-insulation.md`, `peelable-mask-pcb.md`, `epoxy-pcb.md`, `hybrid-circuit-board.md`, `ltcc-pcb.md`, and `pcb-copper-foil.md` still need source recovery before factual reuse

### `2025.12.10/en`

Disposition: `completed_at_claim_family_level`

Usable now:

- RO4003C / RO4350B material-family framing from existing Rogers cards
- high-frequency manufacturing, radar, and lifecycle narratives as topic intent only
- ceramic material-family mention at class level

Blocked or downgraded:

- China-manufacturer proof, direct-factory claims, stock and sourcing claims
- radar-performance, RF performance, frequency-band success, and application qualification language
- fabrication-control numerics, supplier audit standards, and factory certification bundles unless separately sourced

Batch verdict:

- `rogers-ro4350b-pcb.md`, `ro4350b-pcb.md`, `ro4003c-pcb-fabrication.md`, and `ro4003c-pcb-china.md` have partial support through Rogers facts, but their supplier and country-specific claims remain blocked
- `high-frequency-pcb-lifecycle.md`, `high-frequency-pcb-for-radar.md`, `high-frequency-pcb-manufacturing.md`, and `china-high-frequency pcb-manufacturer.md` are mostly claim-family inventory only
- `ceramic-pcb-materials.md` can reuse ceramic-class framing but not property tables or qualification claims

### `2026.2.25/en`

Disposition: `completed_at_claim_family_level`

Usable now:

- Kingboard family grouping and selector posture
- exact baseline reuse for already-covered products such as `KB-6150`, `KB-6160A`, `KB-6165`, `KB-6165C`, `KB-6167GLD`, `HF-170`, and `PI-520G`
- laminate-selection boundaries instead of blanket application claims

Blocked or downgraded:

- unsupported exact-product values for uncovered SKUs
- automotive, server, high-speed, halogen-free, low-loss, or application-readiness claims beyond what named cards already support
- draft-originated supplier qualification, price, stock, MOQ, lead time, and quality-rate language

Batch verdict:

- `kb-6150-pcb.md`, `kb-6160a-pcb.md`, `kb-6165-pcb.md`, `kb-6165c-kb-6165le-pcb.md`, `kb-6167gld-pcb.md`, `hf-140-hf-170-pcb.md`, `pi-515g-pi-520g-pcb.md`, and `kingboard-pcb-laminate.md` have the strongest current match
- `kb-6160f-kb-6160lc-pcb.md`, `kb-6169gt-pcb.md`, `kb-3200g-pcb.md`, `kb-6167gmd-pcb.md`, `kb-6167f-pcb.md`, `kb-6168le-pcb.md`, `kb-6164-pcb.md`, `kb-6160-pcb.md`, and `kb-6165f-pcb.md` still need exact-product source cards before values or positioning can be reused safely

### `2026.3/en`

Disposition: `completed_at_claim_family_level`

Usable now:

- strong RO3003 / RO3006 material-family framing from existing Rogers cards
- PTFE processing posture, hybrid stackup, RF finish selection, quick-turn routing boundary, and RF validation posture
- broad application-band and RF / microwave / mmWave topic intent

Blocked or downgraded:

- quick-turn windows, stock, prototype turnaround, supplier shortlist, and sourcing-authenticity claims
- cost percentages, savings percentages, quote logic, and procurement strategy claims
- exact impedance geometry, insertion-loss examples, thermal outcomes, antenna / filter / array performance, and production qualification claims
- supplier certification, Class 3 proof, ESS / NDI proof, and automotive / defense readiness claims unless backed by separate authority

Batch verdict:

- `ro3003-pcb.md`, `rogers-ro3003-rf-pcb.md`, `rogers-ro3003-high-frequency-pcb.md`, `rogers-ro3003-microwave-pcb.md`, `rogers-ro3003-mmwave-pcb.md`, `rogers-ro3003-low-loss-pcb.md`, `rogers-ro3006-pcb.md`, `rogers-ro3006-rf-pcb.md`, and `rogers-ro3006-microwave-pcb.md` have the strongest current material-level support
- `ro3003-pcb-fabrication.md`, `rogers-ro3006-pcb-fabrication.md`, `rogers-circuit-board-design.md`, and `ro3003-pcb-assembly.md` can reuse process posture only, not draft numerics
- `ro3003-pcb-cost.md`, `ro3003-quick-turn-pcb.md`, `ro3003-pcb-supplier.md`, `ro3003-pcb-manufacturer.md`, and `rogers-ro3006-pcb-manufacturer.md` remain heavily blocked on commercial and supplier-proof claim families

## Safe Reuse Classes

- topic intent, file titles, section clustering, and reader-question inventory
- material-family framing when it already maps to source-backed `llm_wiki` facts
- class-level process posture:
  PTFE handling, hybrid stackup, RF finish selection, prototype vs quick-turn routing, validation-ladder separation, ceramic-vs-IMS thermal-platform framing
- exact-product reuse only where a named fact card already exists
- claim-gap planning for future source recovery

## Blocked Claim Classes

- draft-originated numeric values:
  dielectric, dissipation, Tg, Td, CTE, thermal conductivity, peel strength, foil profile, impedance geometry, plating thickness, finish thickness, shelf life, frequency limits, insertion loss, thermal resistance
- supplier and factory proof:
  in-house process proof, equipment proof, direct-factory claims, authenticity guarantees, stock guarantees, certification bundles, quality-rate claims
- commercial claims:
  price, savings percentages, MOQ, lead time, quick-turn windows, quote outcomes, supply-chain ranking, logistics promises
- qualification and compliance claims:
  automotive, defense, medical, radar, mmWave, space, telecom, military, regulated or customer-program readiness unless separately sourced
- finished-board or application performance claims:
  antenna behavior, filter performance, array performance, RF link success, thermal outcome, lifecycle outcome, yield, reliability pass claims

## Official-Source / PDF Gaps

Gaps despite the PDF pool being present:

- PDFs were not text-extracted in this lane, so no new source records or exact-product facts were landed from the local PDFs
- many PDF families in `/tmps/materias_pdf` have no visible one-to-one `llm_wiki` fact yet even though filenames suggest useful coverage:
  AGC `METEORWAVE`, many `Ventec` exact products, many `Shengyi` exact products, `Taconic RF-35`, `TU` materials, and several Rogers adjacent lines such as `RO4835`, `RO4360G2`, `RT-duroid 6002/6202/6035HTC`, `TMM`
- finish-family drafts still lack authoritative finish chemistry / thickness / life cards
- specialty-topic drafts such as waterproof, stretchable, transparent, biodegradable, peelable-mask, LTCC, insulation, and copper-foil still lack class-level official-source bridges
- several Kingboard draft SKUs in the 2026.2.25 batch still need exact-product coverage even though the family selector exists

## Suggested Source Recovery Lanes

- Lane B:
  local PDF extraction and source-record intake for high-value exact products already demanded by drafts, starting with `RO3000`, `RO4000`, `RO4835`, `Taconic RF-35`, `Ventec VT-4BC / VT-464LT`, and Kingboard residual SKUs
- Lane C:
  finish-source lane for `ENIG`, `ENEPIG`, `HASL`, `lead-free HASL`, `OSP`, `immersion silver`, and `immersion gold` using official standards metadata plus manufacturer chemistry pages
- Lane D:
  specialty-material class lane for `waterproof`, `stretchable`, `transparent`, `biodegradable`, `LTCC`, `peelable mask`, `insulation`, and `copper foil`
- Lane E:
  commercial/supplier boundary lane for quick-turn, price, MOQ, stock, manufacturer, supplier, and certification-claim containment in the 2025.12 and 2026.3 drafts
- Lane F:
  Kingboard residual exact-product recovery for uncovered 2026.2.25 SKUs

## Completion Status

- lane scope completed: inspected the required TMPS PDF pool and all listed material-heavy draft batches
- lane output completed: matching and governance log written at lane-owned path only
- `llm_wiki` learning status: `completed_at_claim_family_level`
- not completed in this lane:
  no PDF text extraction
  no new `sources/registry/`, `facts/`, or `wiki/` additions
  no exact-product fact recovery from the local PDF pool

End-state rule:

- this lane is deletion-safe for claim-family matching and source-gap planning
- it is not a numeric unlock or supplier-proof unlock
- future writing should reuse only the already-supported classes listed above and stop on the blocked classes until a recovery lane lands source-backed coverage
