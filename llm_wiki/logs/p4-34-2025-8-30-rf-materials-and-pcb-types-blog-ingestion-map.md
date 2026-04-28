# P4-34 2025.8.30 RF Materials And PCB Types Blog Ingestion Map

Date: 2026-04-28

## Purpose

Create a deletion-safe ingestion map for `/code/blogs/tmps/2025.8.30/en`.

Treat all `tmps` drafts in this batch as claim inventory only, not as authority.

This log records:

- purpose and date
- file inventory
- title and heading or topic-summary inventory
- existing `llm_wiki` support found by targeted search
- per-draft disposition
- safe reuse classes
- blocked claim classes
- official-source gaps
- completion status using standard labels

## Input Directory

- `/code/blogs/tmps/2025.8.30/en`

## File List

- `/code/blogs/tmps/2025.8.30/en/buying-circuit-boards.md`
- `/code/blogs/tmps/2025.8.30/en/circuit-board-assembly.md`
- `/code/blogs/tmps/2025.8.30/en/circuit-board-manufacturing.md`
- `/code/blogs/tmps/2025.8.30/en/circuit-board-testing.md`
- `/code/blogs/tmps/2025.8.30/en/circuit-board.md`
- `/code/blogs/tmps/2025.8.30/en/custom-circuit-board-design.md`
- `/code/blogs/tmps/2025.8.30/en/high-frequency-circuit-board.md`
- `/code/blogs/tmps/2025.8.30/en/microwave-pcb.md`
- `/code/blogs/tmps/2025.8.30/en/multilayer-circuit-board.md`
- `/code/blogs/tmps/2025.8.30/en/rf-pcb-assembly.md`
- `/code/blogs/tmps/2025.8.30/en/rf-pcb-design.md`
- `/code/blogs/tmps/2025.8.30/en/rf-pcb-impedance-control.md`
- `/code/blogs/tmps/2025.8.30/en/rf-pcb-manufacturing.md`
- `/code/blogs/tmps/2025.8.30/en/rf-pcb-materials.md`
- `/code/blogs/tmps/2025.8.30/en/rf-pcb-testing.md`

## Title And Heading Inventory

| Draft | Title / topic | Main section inventory |
| --- | --- | --- |
| `buying-circuit-boards.md` | buying circuit boards / PCB procurement guide | cost considerations, RFQ-to-delivery process, supplier selection, QA, compliance, sourcing strategy |
| `circuit-board-assembly.md` | general PCB assembly services guide | assembly fundamentals, SMT, through-hole and mixed technology, advanced assembly, QC/testing/DFM, supplier evaluation |
| `circuit-board-manufacturing.md` | general PCB production-process guide | quality/speed framing, substrate materials, staged fabrication flow, testing/finalization, cost-effectiveness, future technologies |
| `circuit-board-testing.md` | general PCB testing services guide | test fundamentals, bare-board electrical test, impedance test, AOI, dimensional validation, ICT/JTAG/AXI/FCT, reliability testing |
| `circuit-board.md` | general circuit-board manufacturing partner guide | quality matters, manufacturing capabilities, certifications, process flow, partner selection, cost optimization, project management |
| `custom-circuit-board-design.md` | custom PCB design guide | design process, stackup, routing, signal integrity, PDN, thermal, DRC/DFM/prototyping, optimization, supplier CTA |
| `high-frequency-circuit-board.md` | high-frequency PCB manufacturing solutions | what high-frequency boards are, characteristics, applications, manufacturer evaluation, capabilities, QA/testing, engineering support |
| `microwave-pcb.md` | microwave PCB design guide | distributed-element design, material selection, thermal design, manufacturing considerations, testing considerations |
| `multilayer-circuit-board.md` | multilayer PCB technology guide | cost factors, optimization, multilayer definition, manufacturing process, assembly/testing, manufacturer selection |
| `rf-pcb-assembly.md` | RF PCB assembly services | RF component handling, precision assembly, best practices, QC/testing, scalable production, supplier CTA |
| `rf-pcb-design.md` | RF PCB layout guide | RF fundamentals, layout techniques, material strategy, impedance control, power/EMI, testing/validation |
| `rf-pcb-impedance-control.md` | controlled impedance for RF PCB | impedance physics, transmission-line geometries, manufacturing process control, advanced testing, optimization, troubleshooting |
| `rf-pcb-manufacturing.md` | RF and microwave PCB production guide | supplier capability pitch, DFM, material handling, advanced manufacturing, testing/QC, cost optimization, scaling |
| `rf-pcb-materials.md` | RF substrate-selection guide | RF material properties, Rogers portfolio, alternative suppliers, cost optimization, manufacturing considerations |
| `rf-pcb-testing.md` | RF PCB validation guide | RF test equipment and methods, calibration, environmental/reliability testing, cost optimization, related resources |

## Existing `llm_wiki` Support Found By Targeted Search

Targeted search across `/code/blogs/llm_wiki` found meaningful support for RF material selection, PTFE and hybrid-stackup process framing, controlled-impedance verification posture, multilayer and advanced fabrication routing, and PCBA test-method boundaries.

Most relevant existing support:

- RF materials and product-family selection
  - `facts/materials/rf-material-selector-by-application.md`
  - `wiki/materials/rf-material-selector-by-application-band.md`
  - `facts/materials/parameter-scope-rogers-rf-laminate-values.md`
  - many exact-product cards already exist for Rogers, AGC, Isola, Ventec, Panasonic, Shengyi, and others
- FR-4 and baseline laminate-family boundaries
  - `facts/materials/fr4-official-source-coverage.md`
  - `facts/materials/hil-base-laminate-and-build-stage-family-map.md`
- RF process and manufacturing posture
  - `facts/methods/hybrid-rf-stackup-capability.md`
  - `facts/methods/ptfe-processing-capability.md`
  - `wiki/processes/hybrid-rf-stackup-strategy.md`
  - `wiki/processes/ptfe-processing-and-manufacturability.md`
  - `wiki/processes/rf-drilling-and-transition-control.md`
  - `wiki/processes/rf-surface-finish-selection.md`
- controlled impedance, multilayer, and fabrication planning
  - `facts/methods/controlled-impedance-tdr-verification-posture.md`
  - `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
  - `wiki/processes/pcb-service-routing-from-prototype-to-special-process.md`
  - `facts/methods/parameter-scope-public-capability-construction-windows.md`
- RF and general test coverage boundaries
  - `facts/methods/rf-validation-capability.md`
  - `wiki/testing/rf-validation-and-test-coverage.md`
  - `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`
- assembly and PCBA test-method routing
  - `facts/methods/pcba-mixed-technology-assembly-flow.md`
  - `facts/methods/pcba-test-method-selection-framework.md`
  - `facts/methods/pcba-ict-vs-fct-boundary.md`
  - `facts/methods/pcba-flying-probe-vs-ict-selection-posture.md`
  - `wiki/testing/pcba-quality-gates-and-test-strategy.md`

Coverage summary:

- strongest current support
  - RF material-family framing
  - exact-product RF laminate cards
  - PTFE and hybrid-stackup process posture
  - multilayer and advanced-fabrication routing
  - controlled-impedance verification posture
  - RF validation and layered test-method vocabulary
  - mixed-technology assembly-flow framing
- partial current support
  - general `circuit board` buying, manufacturing, and supplier-selection topics only as routing or governance language, not as reusable proof
  - high-frequency and microwave application framing, but not blanket finished-board readiness claims
- weak or absent current support
  - supplier-selection scorecards with current commercial claims
  - broad `complete service` or `one-stop factory` claims
  - cost optimization numbers, lead times, MOQ, yield, delivery, and quality-rate assertions
  - current certification, qualification, or supplier-status proof
  - generalized hard numbers for `all RF boards`, `all high-frequency boards`, or `all multilayer boards`

## Per-Draft Disposition

| Draft | Current support | Safe reuse now | Blocked claim families | Status |
| --- | --- | --- | --- | --- |
| `buying-circuit-boards.md` | weak | procurement topic shape, RFQ-to-delivery workflow questions, supplier-evaluation checklist intent | pricing, lead times, MOQ, quality-rate claims, supplier advantage claims, compliance proof, sourcing superiority | `completed_at_claim_family_level` |
| `circuit-board-assembly.md` | partial | SMT/THT/mixed-technology flow framing, DFM and QC topic inventory, assembly-evaluation questions | assembly capability windows, equipment proof, defect/yield claims, testing coverage completeness, service superiority | `source_backed_fact_layer_partial` |
| `circuit-board-manufacturing.md` | partial | staged fabrication-flow outline, substrate-selection topic intent, testing/finalization vocabulary | speed, cost-effectiveness, throughput, process limits, quality outcomes, future-tech readiness, supplier capability | `source_backed_fact_layer_partial` |
| `circuit-board-testing.md` | partial | layered test taxonomy, distinction among e-test, ICT, JTAG, AXI, FCT, reliability framing | `complete testing` claims, coverage percentages, qualification proof, impedance tolerance promises, factory testing superiority | `source_backed_fact_layer_partial` |
| `circuit-board.md` | weak | general manufacturing-partner article structure, process-stage outline, partner-selection checklist intent | certifications, advanced capability, cost optimization numbers, supplier proof, delivery/quality promises | `completed_at_claim_family_level` |
| `custom-circuit-board-design.md` | partial | design-process outline, stackup/routing/signal-integrity/thermal topic clustering, DRC/DFM/prototyping posture | layout-rule numbers, performance outcomes, manufacturability guarantees, prototype speed, supplier expertise claims | `source_backed_fact_layer_partial` |
| `high-frequency-circuit-board.md` | partial | high-frequency board topic framing, manufacturer-evaluation dimensions, RF process and QA topic clustering | board characteristics as fixed numbers, application readiness, capability proof, turnaround, delivery, cost, supplier claims | `source_backed_fact_layer_partial` |
| `microwave-pcb.md` | partial | microwave design-intent outline, distributed-element framing, material-selection and thermal topic inventory, manufacturing/test topic demand | frequency-band performance proof, material numerics from draft prose, thermal outcomes, fabrication recipes, application guarantees | `source_backed_fact_layer_partial` |
| `multilayer-circuit-board.md` | partial | multilayer definition/topic inventory, stackup/manufacturing/test-routing questions, cost-driver categories only | pricing claims, layer-capability claims, process windows, reliability proof, supplier selection proof | `source_backed_fact_layer_partial` |
| `rf-pcb-assembly.md` | partial | RF component-handling and RF assembly topic demand, QC/testing placement, mixed-technology flow alignment | RF assembly capability proof, cleanliness/process limits, yield, scale, production-readiness, supplier superiority | `source_backed_fact_layer_partial` |
| `rf-pcb-design.md` | partial | RF design checklist structure, layout/material/impedance/power/EMI/testing topic inventory | geometry numbers, universal RF rules, impedance success claims, EMI-performance guarantees, validation outcomes | `source_backed_fact_layer_partial` |
| `rf-pcb-impedance-control.md` | partial | impedance topic clustering, transmission-line vocabulary, manufacturing-control and test-planning posture | impedance formulas as reusable facts, tolerance numbers, geometry defaults, yield/capability claims, troubleshooting guarantees | `source_backed_fact_layer_partial` |
| `rf-pcb-manufacturing.md` | partial | DFM/material-handling/testing topic inventory for RF production articles | Highleap-style capability proof, advanced-tech claims, scaling claims, cost optimization, delivery, quality-rate promises | `source_backed_fact_layer_partial` |
| `rf-pcb-materials.md` | strong | RF material-property topic inventory, named supplier families as source-recovery targets, material-selection framing routed through existing exact-product cards | draft-originated property values, portfolio rankings, cost/performance claims, supplier availability, manufacturing readiness claims | `source_backed_fact_layer_partial` |
| `rf-pcb-testing.md` | partial | RF test-method taxonomy, calibration and validation topic demand, environmental/reliability test vocabulary | equipment-range claims, measurement accuracy numbers, pass/fail thresholds, environmental qualification proof, cost optimization claims | `source_backed_fact_layer_partial` |

## Safe Reuse Classes

- titles, outline shape, H2/H3 topic clustering, and reader-intent inventory
- RF material-family names and exact-product references only when routed through existing source-backed cards
- FR-4 and multilayer family framing only with family-level boundaries or exact-product anchors
- PTFE, hybrid-stackup, drilling, transition-control, finish-selection, and validation topics where existing `llm_wiki` method or wiki pages already support guarded reuse
- mixed-technology assembly-flow and layered test-method vocabulary
- cost-driver categories and sourcing-question categories only as non-numeric planning prompts

## Blocked Claim Classes

- any draft-originated material parameters
  - Dk, Df, Tg, CTE, thermal conductivity, moisture, impedance values, insertion loss, frequency suitability numbers
- any draft-originated process limits or fabrication windows
  - layer counts, thickness, copper weights, geometry minima, lamination cycles, drilling rules, reflow profiles, cleanliness thresholds
- any draft-originated supplier or capability claims
  - equipment proof, quality systems, process maturity, scalability, engineering support depth, `one-stop` or `advanced` factory assertions
- any draft-originated commercial claims
  - price, cost savings, lead time, MOQ, stock, delivery, procurement advantage
- any draft-originated quality, yield, readiness, or qualification claims
  - yield rates, defect reduction, reliability improvement, application readiness, certification, compliance, qualification, pass-rate proof
- any generalized finished-board performance claims inferred from laminate or process vocabulary alone
  - RF success, microwave success, EMI control success, signal-integrity success, ruggedness, telecom/radar/antenna readiness

## Official-Source Gaps

- general PCB procurement lane
  - official or dated internal support is still needed for buyer checklists, supplier-selection claims, RFQ workflow evidence, and commercial framing
- general manufacturing and assembly lane
  - stronger authoritative sources are needed if future work wants reusable non-promotional process-stage explanations outside existing internal route pages
- RF impedance lane
  - if future writing needs formulas, tolerances, or geometry examples, separate official source recovery is required
- RF testing lane
  - stronger official method anchors are needed for equipment categories, calibration boundaries, environmental test scope, and acceptance-language control
- supplier-specific capability lane
  - any shop-specific process windows, current certifications, current capacity, delivery posture, or quality metrics require dated capability records
- general circuit-board and multilayer commercial lane
  - current source layer does not authorize procurement, pricing, speed, availability, or supplier-ranking content

## Prompt-Consumption Gate

1. Use these drafts for article intent, section ordering, and question inventory only.
2. Pull RF laminate facts only from existing exact-product cards and selector pages.
3. Pull RF and microwave process framing only from the current PTFE, hybrid-stackup, drilling, finish, impedance, and validation pages.
4. Keep FR-4, multilayer, and `circuit board` topics at family or workflow level unless exact-product or official standards anchors are attached.
5. Stop before any supplier-specific capability, quality, certification, commercial, delivery, or readiness claim unless a dated record exists.
6. Do not promote draft formulas, process windows, cost numbers, or test thresholds into reusable facts.

## Completion Status

Batch status: `source_backed_fact_layer_partial`

Claim-family-only subareas remain:

- `buying-circuit-boards.md`
- `circuit-board.md`

These are currently `completed_at_claim_family_level` because the existing source layer is not strong enough to unlock commercial or supplier-selection content safely.

The rest of the batch is `source_backed_fact_layer_partial` because relevant `llm_wiki` support already exists for RF materials, RF process posture, multilayer routing, assembly flow, and test-method boundaries, but not for draft-originated numbers or supplier claims.

No new facts, source records, tracker updates, or wiki expansions were created from this draft batch in this lane.
