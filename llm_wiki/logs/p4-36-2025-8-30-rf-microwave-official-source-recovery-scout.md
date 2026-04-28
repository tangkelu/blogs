# P4-36 2025-8-30 RF / Microwave Official-Source Recovery Scout

Date: 2026-04-28
Model: `gpt-5.4`
Input inventory: `/code/blogs/tmps/2025.8.30/en`
Lane: official-source recovery scout for RF / microwave / impedance / materials drafts
Output ownership: only this file

## Scope

This scout treats the `tmps/2025.8.30/en` drafts as claim inventory only, not as authority.

It does not update registries, facts, wiki pages, or trackers.

It identifies official-source candidates for later upgrades across:

- RF material parameters
- impedance-control definitions and standards anchors
- RF / microwave fabrication and process controls
- RF testing and validation
- procurement / commercial claims

## Drafts Inspected

- `microwave-pcb.md`
- `rf-pcb-assembly.md`
- `rf-pcb-design.md`
- `rf-pcb-impedance-control.md`
- `rf-pcb-manufacturing.md`
- `rf-pcb-materials.md`
- `rf-pcb-testing.md`

## High-Value Claim Families Needing Real Data

### Recoverable with official sources

- exact laminate identity and vendor-scoped material values for:
  - Rogers `RO4350B`
  - Rogers `RO3003`
  - Rogers `RT/duroid 5880`
  - AGC / Taconic-line `TLY-5` and `TLY-5A`
  - Isola `I-Tera MT40`
- vendor-scoped processing posture such as:
  - `RO4350B` processing like standard epoxy / glass materials
  - `RO4350B` not requiring PTFE-style special through-hole treatment
  - PTFE-family laminates needing distinct fabrication guidance
- standards metadata for:
  - controlled impedance design
  - RF / microwave printed-board design
  - flexible printed-board design
  - IPC test-method families for Dk / Df and TDR-based characteristic impedance
- instrument-vendor validation basics for:
  - S-parameter naming and meaning
  - VNA usage for reflection / transmission characterization
  - TDR as impedance-discontinuity localization and profile measurement

### Not recoverable in this lane from official sources found

- generic, supplier-neutral frequency ceilings like `FR4 works to X GHz` or `RO4350B handles 77 GHz` as a universal finished-board claim
- fab capability claims for Highleap / HIL such as `±3% impedance`, `up to 77 GHz`, `±0.025 mm registration`, `24-48 hour reports`, `3-5 day assembly`, `100% inspection coverage`, or `full testing suite`
- universal RF process windows such as etch uniformity, copper-thickness tolerance, press-parameter tolerance, or layer-registration tolerance
- generic bend / via / backdrill / quarter-wave rules presented as standards-backed thresholds
- cost-reduction percentages, yield improvements, lead-time improvements, stock availability, MOQ, volume discounts, or procurement guarantees
- application-readiness claims for aerospace, defense, automotive radar, 5G, mmWave, or satellite unless tied to a specific source and kept source-scoped

## Official Sources Found

### 1. Rogers RO4350B laminates page

- URL: `https://www.rogerscorp.com/advanced-electronics-solutions/ro4000-series-laminates/ro4350b-laminates`
- Owner: Rogers Corporation
- Source type: official manufacturer product page
- Candidate source ID: `src_rogers_ro4350b_laminates`
- Supported claims:
  - official `RO4350B` product identity
  - vendor-scoped values including `Dk 3.48 +/- 0.05` and `Df 0.0037 at 10 GHz`
  - product positioning that it uses the same processing method as standard epoxy / glass
  - explicit claim that it does not require the special through-hole treatments or handling procedures of PTFE-based materials
  - UL 94 V-0 product-level rating context
- Exact limits / non-claims:
  - not proof that any finished PCB meets a given impedance tolerance
  - not proof of universal `77 GHz` finished-board suitability
  - not proof of a fab's yield, lead time, registration, trace tolerance, or cost
  - source-scoped to `RO4350B`, not all RF laminates or all Rogers products
- Candidate fact IDs:
  - `materials-rogers-ro4350b-product-identity`
  - `materials-rogers-ro4350b-dk-df`
  - `methods-ro4350b-fr4-like-processing-scope`
  - `methods-ro4350b-no-ptfe-through-hole-treatment-scope`

### 2. Rogers RO3003 laminates page

- URL: `https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3003-laminates`
- Owner: Rogers Corporation
- Source type: official manufacturer product page
- Candidate source ID: `src_rogers_ro3003_laminates`
- Supported claims:
  - official `RO3003` product identity
  - vendor-scoped values including `Dk 3.00 +/- 0.04` and `Df 0.0010 at 10 GHz`
  - source-scoped stability positioning over temperature / frequency
  - product page names application contexts including automotive radar and 5G infrastructure
- Exact limits / non-claims:
  - application mentions are not the same as qualification for any end-product program
  - not proof that every `RO3003` board is low loss in-system without stackup and copper context
  - not proof of impedance tolerance, manufacturability at a given fab, or cost savings
- Candidate fact IDs:
  - `materials-rogers-ro3003-product-identity`
  - `materials-rogers-ro3003-dk-df`
  - `materials-ro3003-application-context-source-scoped`

### 3. Rogers RT/duroid 5880 laminates page

- URL: `https://www.rogerscorp.com/advanced-electronics-solutions/rt-duroid-laminates/rt-duroid-5880-laminates`
- Owner: Rogers Corporation
- Source type: official manufacturer product page
- Candidate source ID: `src_rogers_rtduroid_5880_laminates`
- Supported claims:
  - official `RT/duroid 5880` product identity
  - vendor-scoped values including `Dk 2.20 +/- 0.02`, `Df 0.0009 at 10 GHz`, and low moisture absorption
  - source-scoped thermal-conductivity and CTE context
  - product-family positioning as low-loss PTFE composite material for high-frequency / broadband use
- Exact limits / non-claims:
  - not proof of universal superiority for all microwave designs
  - not proof of board-level power handling, reliability, or qualification
  - not proof of universal trace-width or impedance advantages without stackup details
- Candidate fact IDs:
  - `materials-rogers-rtduroid-5880-product-identity`
  - `materials-rogers-rtduroid-5880-dk-df-moisture`

### 4. AGC woven-glass reinforced PTFE base materials page

- URL: `https://www.agc-multimaterial.com/woven-glass-reinforced-ptfe-base-materials/`
- Owner: AGC Multi Material America, Inc.
- Source type: official manufacturer family page
- Candidate source ID: `src_agc_woven_glass_ptfe_family`
- Supported claims:
  - official family lineup including `TLY-5` and `TLY-5A`
  - family table lists vendor-scoped `Dk` and `Df` values for `TLY-5` and `TLY-5A`
  - official product-family context for woven-glass reinforced PTFE laminates
- Exact limits / non-claims:
  - family table is not a substitute for exact-product datasheets
  - not proof of generic Taconic market ranking or interchangeability with Rogers materials
  - not proof of supply continuity, qualification, or fab stock
- Candidate fact IDs:
  - `materials-agc-tly5-family-context`
  - `materials-agc-tly5-tly5a-dk-df-table`

### 5. Isola I-Tera MT40 datasheet

- URL: `https://www.isola-group.com/wp-content/uploads/data-sheets/i-tera-mt40.pdf?t=311556509`
- Owner: Isola Group
- Source type: official manufacturer datasheet PDF
- Candidate source ID: `src_isola_itera_mt40_datasheet`
- Supported claims:
  - official `I-Tera MT40` product identity
  - vendor-scoped values including `Dk 3.45` and `Df 0.0031`
  - datasheet states suitability for high-speed digital and RF / microwave printed circuit designs
  - datasheet states FR-4 process compatibility and says it does not require special through-hole treatments commonly needed for PTFE-based materials
- Exact limits / non-claims:
  - not a neutral comparison proving superiority over PTFE or Rogers
  - not proof of any specific fab capability or cost outcome
  - not proof of system-level RF loss without construction context
- Candidate fact IDs:
  - `materials-isola-itera-mt40-product-identity`
  - `materials-isola-itera-mt40-dk-df`
  - `methods-itera-mt40-fr4-process-compatibility-scope`

### 6. IPC design standards page

- URL: `https://www.ipc.org/ipc-design-standards`
- Owner: IPC
- Source type: official standards index page
- Candidate source ID: `src_ipc_design_standards_index`
- Supported claims:
  - IPC maintains standards including `IPC-2141`, `IPC-2223`, and `IPC-2228`
  - these standards exist as official IPC design references for controlled impedance, flex design, and RF / microwave board design
- Exact limits / non-claims:
  - does not provide reusable thresholds or formulas by itself
  - not proof that a blog claim complies with IPC
  - not sufficient for numeric design advice
- Candidate fact IDs:
  - `standards-ipc-controlled-impedance-rf-flex-family-index`

### 7. IPC-2141A product page

- URL: `https://shop.electronics.org/IPC-2141A-English-D`
- Owner: IPC / electronics.org
- Source type: official standards product page
- Candidate source ID: `src_ipc_2141a_product_page`
- Supported claims:
  - official identity for `IPC-2141A`
  - IPC defines controlled impedance on the page as maintenance of a specified tolerance in characteristic impedance of an interconnect line used to connect devices on a circuit
  - standard scope is controlled-impedance circuit boards and high-speed logic design
- Exact limits / non-claims:
  - product page is not a free license to reproduce formulas or tables
  - not proof of any single impedance target such as `50 ohm` or `100 ohm`
  - not proof that a fabricator can achieve a given tolerance
- Candidate fact IDs:
  - `standards-ipc-2141a-identity`
  - `methods-controlled-impedance-definition-ipc-product-page`

### 8. IPC-2228 TOC and product page

- URL: `https://www.ipc.org/TOC/IPC-2228_TOC.pdf`
- Companion URL: `https://shop.electronics.org/ipc-2228/ipc-2228-standard-only/Revision-0/english`
- Owner: IPC / electronics.org
- Source type: official public TOC plus official standards product page
- Candidate source ID: `src_ipc_2228_toc_and_product_page`
- Supported claims:
  - official identity for `IPC-2228`
  - standard scope covers design of rigid, flexible, and rigid-flex printed boards using RF / microwave circuitry and high-frequency laminates
  - TOC text supports the draft family distinction that RF / microwave structures are treated as distributed rather than conventional lumped elements
  - TOC text says the standard supports products typically requiring materials meeting `IPC-4103` and fabrication to `IPC-6018`
- Exact limits / non-claims:
  - not a source for copying detailed design rules, spacing tables, or stackup thresholds
  - not proof of generic board frequency limits
  - not proof that a named material or fab is compliant
- Candidate fact IDs:
  - `standards-ipc-2228-identity`
  - `methods-rf-microwave-distributed-circuit-scope`

### 9. IPC TM-650 test methods index

- URL: `https://www.ipc.org/test-methods`
- Owner: IPC
- Source type: official test-method index
- Candidate source ID: `src_ipc_tm650_test_methods_index`
- Supported claims:
  - IPC maintains official methods including:
    - `2.5.5.5C` stripline test for permittivity and loss tangent at X-band
    - `2.5.5.7A` characteristic impedance lines on printed boards by TDR
    - `2.5.5.11` propagation delay of lines on printed boards by TDR
    - `2.5.5.14` measuring high-frequency signal loss and propagation on printed boards with frequency-domain methods
    - `2.5.5.15` determination of Dk and Df by SPDR
- Exact limits / non-claims:
  - index entries are metadata only
  - not enough to claim exact measurement setup, pass/fail criteria, or acceptance thresholds
  - not proof that a specific test lab follows these methods
- Candidate fact IDs:
  - `standards-ipc-tm650-rf-test-method-family`

### 10. IPC-TM-650 2.5.5.5 PDF

- URL: `https://www.ipc.org/sites/default/files/test_methods_docs/2-5_2-5-5-5.pdf`
- Owner: IPC
- Source type: official test-method PDF
- Candidate source ID: `src_ipc_tm650_2555_stripline_xband`
- Supported claims:
  - official identity for `TM 2.5.5.5`
  - method scope is stripline testing for permittivity and loss tangent at X-band
  - supports the existence of an official IPC method for high-frequency laminate characterization
- Exact limits / non-claims:
  - one material-test method does not justify using a draft number without matching test conditions
  - not a source for generic RF PCB performance claims
  - not proof of finished-board insertion loss or impedance
- Candidate fact IDs:
  - `standards-ipc-tm650-2555-identity`
  - `methods-ipc-xband-dk-df-test-scope`

### 11. Keysight network analyzer basics

- URL: `https://www.keysight.com/blogs/en/tech/rfmw/2019/03/08/network-analyzer-basics-you-need-to-know`
- Owner: Keysight Technologies
- Source type: official instrument-vendor technical article
- Candidate source ID: `src_keysight_network_analyzer_basics`
- Supported claims:
  - VNA measures both magnitude and phase
  - S-parameters characterize RF behavior
  - `S11` and `S22` are reflection-related terms
  - `S21` and `S12` are transmission-related terms
  - return loss and insertion loss vocabulary can be anchored here
- Exact limits / non-claims:
  - educational source, not a standards document
  - not a source for production test coverage, accuracy guarantees, or specific pass/fail limits
  - not proof that a PCB shop has VNA capability
- Candidate fact IDs:
  - `methods-vna-sparameter-basics-keysight`
  - `methods-s11-s21-return-loss-insertion-loss-basics`

### 12. Keysight user manual S-parameter section

- URL: `https://www.keysight.com/us/en/assets/9018-40023/user-manuals/9018-40023.pdf`
- Owner: Keysight Technologies
- Source type: official instrument user manual
- Candidate source ID: `src_keysight_vna_user_manual_sparams`
- Supported claims:
  - official explanation that for a two-port device the first number is the port where energy emerges and the second where energy enters
  - supports precise S-parameter naming if later fact extraction needs a stricter primary anchor than the blog article
- Exact limits / non-claims:
  - manual context is instrument usage, not PCB qualification standards
  - not a source for board-level test workflows beyond general measurement semantics
- Candidate fact IDs:
  - `methods-sparameter-port-numbering-keysight`

### 13. Tektronix TDR impedance measurements fact sheet

- URL: `https://www.tek.com/document/fact-sheet/tdr-impedance-measurements-foundation-signal-integrity`
- Owner: Tektronix
- Source type: official instrument-vendor technical fact sheet
- Candidate source ID: `src_tektronix_tdr_impedance_foundation`
- Supported claims:
  - TDR measures reflections caused by impedance variations in traces, cables, connectors, and similar structures
  - TDR is used to verify impedance with hardware measurements after modeling / design
  - differential-impedance measurement context is explicitly discussed
- Exact limits / non-claims:
  - not a standards document for coupon construction or acceptance limits
  - not proof that TDR alone validates full RF performance across frequency
  - not proof of any fab's production test practice
- Candidate fact IDs:
  - `methods-tdr-impedance-verification-basics`
  - `methods-tdr-differential-impedance-context`

### 14. Tektronix TDR test primer

- URL: `https://www.tek.com/en/documents/primer/tdr-test`
- Owner: Tektronix
- Source type: official instrument-vendor primer
- Candidate source ID: `src_tektronix_tdr_test_primer`
- Supported claims:
  - supports the caution that real boards with multiple impedance segments create multiple-reflection effects
  - useful guardrail against oversimplified draft language implying TDR always yields a direct single true impedance reading on complex interconnects
- Exact limits / non-claims:
  - not a standard acceptance method
  - not a source for coupon coverage or fab capability claims
- Candidate fact IDs:
  - `methods-tdr-multiple-reflection-limit`

## Unsupported Or Still-Blocked Claim Families

### Material and electrical performance

- `FR4 works adequately` or `works up to about 1 GHz` as a universal threshold
- `RO4350B`, `RO3003`, `RT5880`, `TLY-5A`, or `I-Tera MT40` as ranked best choices without application-specific constraints
- generic claims about `premium RF materials achieve Df below ...` unless rewritten as source-scoped product examples
- universal moisture, TCDk, or power-handling claims detached from exact product and test method

### Impedance control

- `±3% impedance tolerance` or `±5% impedance tolerance` as a factual shop capability
- universal process-control numbers such as:
  - trace width `±0.025 mm`
  - dielectric thickness `±0.025 mm`
  - layer registration `±0.025 mm`
  - etch uniformity `±5%`
  - copper thickness `±10%`
  - press parameters `±2%`
- `50 ohm`, `100 ohm`, and impedance-range defaults presented as universally correct targets without design context

### RF / microwave fabrication and design practice

- `every trace becomes a transmission line above 1 GHz` as a hard threshold
- quarter-wave and one-tenth-wavelength heuristics presented as exact standard rules
- `ground vias every quarter wavelength` as an IPC-backed prescription
- `back-drilling required at X-band` as a universal statement
- `coplanar waveguide excels at millimeter-wave frequencies` as a general truth without narrower source support

### RF testing and validation

- draft frequency-range capability bands such as `DC-6 GHz`, `6-40 GHz`, `40-77 GHz` as service capability claims
- `manufacturing coupons enable 100% impedance testing` as a universal production claim
- environmental and reliability test availability as a vendor capability claim
- measurement-uncertainty numbers or turnaround-time promises

### Procurement and commercial

- material availability claims
- long-term supply-agreement savings claims
- `40-60%` cost reduction from hybrid stackups
- panel-utilization savings claims with percentages
- prototype / assembly rush lead times
- stock, MOQ, or quote promise language

## Best Upgrade Candidates

These are the strongest source-backed upgrades available from this lane.

1. Replace draft material-value tables with exact-product vendor-scoped cards for `RO4350B`, `RO3003`, `RT/duroid 5880`, `TLY-5/TLY-5A`, and `I-Tera MT40`.
2. Rewrite impedance-control definition using `IPC-2141A` product-page wording plus IPC standards anchors instead of draft marketing prose.
3. Anchor RF / microwave board-design framing to `IPC-2228` scope language, especially the distributed-circuit distinction.
4. Upgrade testing sections so `VNA`, `S11/S21`, and `TDR` claims use Keysight / Tektronix official explanations instead of unsupported service claims.
5. Rewrite `RO4350B` and `I-Tera MT40` manufacturability statements around vendor-scoped `FR-4-like` or `FR-4-process-compatible` language, while removing fab-specific performance leaps.

## Residual Gaps

- No official source recovered here for neutral, reusable numeric stackup rules or impedance geometry formulas that can be quoted freely.
- No official source recovered here for generic microwave band boundaries suitable for unqualified public reuse.
- No official source recovered here for Highleap / HIL production capability, tolerances, test coverage, or turnaround claims.
- No official source recovered here for universal RF assembly placement accuracy, component-size capability, or `100%` inspection assertions.
- No official source recovered here for procurement and commercial percentages, lead times, or availability claims.

## Candidate Fact Targets

- `materials-rogers-ro4350b-product-identity`
- `materials-rogers-ro4350b-dk-df`
- `methods-ro4350b-fr4-like-processing-scope`
- `methods-ro4350b-no-ptfe-through-hole-treatment-scope`
- `materials-rogers-ro3003-product-identity`
- `materials-rogers-ro3003-dk-df`
- `materials-rogers-rtduroid-5880-product-identity`
- `materials-rogers-rtduroid-5880-dk-df-moisture`
- `materials-agc-tly5-family-context`
- `materials-agc-tly5-tly5a-dk-df-table`
- `materials-isola-itera-mt40-product-identity`
- `materials-isola-itera-mt40-dk-df`
- `methods-itera-mt40-fr4-process-compatibility-scope`
- `standards-ipc-controlled-impedance-rf-flex-family-index`
- `standards-ipc-2141a-identity`
- `methods-controlled-impedance-definition-ipc-product-page`
- `standards-ipc-2228-identity`
- `methods-rf-microwave-distributed-circuit-scope`
- `standards-ipc-tm650-rf-test-method-family`
- `standards-ipc-tm650-2555-identity`
- `methods-ipc-xband-dk-df-test-scope`
- `methods-vna-sparameter-basics-keysight`
- `methods-s11-s21-return-loss-insertion-loss-basics`
- `methods-sparameter-port-numbering-keysight`
- `methods-tdr-impedance-verification-basics`
- `methods-tdr-differential-impedance-context`
- `methods-tdr-multiple-reflection-limit`

## Status

Completed as an official-source recovery scout only.

No registries, facts, wiki pages, trackers, or unrelated logs were edited.
