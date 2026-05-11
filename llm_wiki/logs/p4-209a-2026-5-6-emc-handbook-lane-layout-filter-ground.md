# P4-209A EMC Handbook Lane: Layout / Filtering / Grounding Intake

Date: 2026-05-06
Lane: `85页 PCB设计EMC设计指导书` layout / filtering / grounding intake
Model requested: `gpt-5.4`

## Purpose

Capture a claim-family intake for the `【PCB必备】85页-PCB设计EMC设计指导书` handbook slice covering layout posture, device placement, filter components, filter topologies, capacitor selection, and grounding families.

This handbook is treated as `claim inventory`, not authority. No handbook-originated numeric, certification, acceptance, capability, or universal performance claim is promoted here.

## Exact Pages Inspected

Inspected text pages: `9-31` from:

- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0009.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0010.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0011.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0012.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0013.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0014.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0015.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0016.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0017.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0018.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0019.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0020.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0021.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0022.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0023.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0024.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0025.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0026.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0027.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0028.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0029.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0030.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/page-0031.txt`

Topic map by page cluster:

- `9-14`: layer setting, plane adjacency, relative layer placement, stackup examples
- `15-18`: module partition, power/clock/coil/bus-driver/filter-component placement
- `19-23`: filter role, passive/filter component families, low-pass topologies, EMI filter framing
- `24-28`: capacitor self-resonance, antiresonance, ESR/ESL, capacitor selection, decoupling / bypass / bulk / storage framing
- `29-31`: grounding meaning, purpose, single-point / multi-point / floating / hybrid grounding

## Existing `llm_wiki` Support Found

Current support already exists, but only for narrow reuse classes:

- `logs/p4-208-2026-5-6-pcb-handbook-intake-map.md`
  - confirms this handbook as the highest-priority next lane and already classifies it as claim-family intake only
- `policies/prompt-consumption-specification.md`
  - blocks handbook-originated board-level SI / EMC numerics under class `D`
- `facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`
  - supports continuous low-impedance reference-plane language, partition-before-routing posture, avoid split/slot crossings, and preserve return continuity on layer changes
- `logs/p4-116-2026-5-2-grounding-return-path-source-recovery.md`
  - documents that current grounded reuse is intentionally narrow and does not support EMC / field / telecom outcome claims
- `wiki/processes/emi-noise-suppression-component-boundaries.md`
  - supports routing EMI-suppression prompts conservatively and keeps ferrite beads, common-mode chokes, LC filters, feedthrough capacitors, shields, and grounding schemes as separate method families
- `facts/methods/ferrite-bead-vendor-guidance-boundary.md`
  - supports vendor-scoped ferrite-bead vocabulary only, not universal placement, selection, or compliance claims
- `wiki/applications/industrial-control-pcb-pcba-boundary-map.md`
  - already allows conservative `EMC-aware layout vocabulary` and `routing / grounding / filtering` framing at board-class level
- `wiki/applications/automotive-ev-pcb-pcba-boundary-map.md`
  - already allows conservative `EMC-aware layout vocabulary` for power-stage boards while blocking compliance and performance proof

What is not yet present as a reusable fact/wiki layer:

- source-backed capacitor self-resonance / parallel antiresonance / ESR / ESL execution boundary
- source-backed decoupling / bypass / bulk capacitor role boundary
- source-backed common-mode choke execution boundary
- source-backed low-pass topology selection boundary
- source-backed grounding-family selection boundary for single-point vs multi-point vs floating vs hybrid without inheriting old frequency cutoffs

## Claim Families

### 1. Layout posture and plane adjacency

- layer-count decision framing
- ground-plane priority as reference plane
- power/ground adjacency posture
- signal-layer adjacency to ground
- avoid signal routing across plane splits
- no direct reuse of handbook stackup recipes as defaults

### 2. Module partition and device placement

- partition by function, frequency, and signal type
- keep signal-flow-oriented placement
- power-entry clustering
- keep noisy blocks isolated from sensitive blocks
- clock placement away from board edge / connectors
- local placement rules for coils, bus drivers, and filter parts

### 3. Filter component families

- resistor + capacitor RC network framing
- inductor behavior family
- capacitor as filter component family
- ferrite bead as EMI-suppression component family
- common-mode choke as separate family

### 4. Filter topologies

- low-pass framing
- `L`, `C`, `Gamma`, `Pi`, `T`, and power-EMI-filter topologies
- source / load impedance suitability claims appear, but remain handbook inventory only

### 5. Capacitor behavior and selection

- decoupling / bypass / storage / bulk role naming
- self-resonance and parasitic model framing
- antiresonance risk when capacitors are combined
- ESR / ESL as boundary vocabulary
- capacitor selection and placement posture near IC power pins and local load clusters

### 6. Grounding families

- safety earth vs system reference ground
- grounding purpose: safety, reference, shielding
- single-point, multi-point, floating, and hybrid grounding families
- ground-loop and public-impedance-coupling risk framing
- board-level local ground joining and split-ground claim inventory

## Safe Reuse Classes

Safe reuse in the current corpus is limited to the following classes:

- `reference-plane / return-path continuity vocabulary`
  - continuous ground-reference language, partitioning, slot/split avoidance, and layer-transition return continuity
- `EMC-aware board-review posture`
  - conservative layout-review wording about noisy vs sensitive region separation, return-path preservation, and interface-entry filtering posture
- `component-family identity vocabulary`
  - ferrite bead as a vendor-scoped EMI-suppression component family, without implying equivalence to common-mode chokes or LC filters
- `topic routing and taxonomy`
  - layout, placement, filter-family, topology-family, capacitor-role, and grounding-family claim inventory for later official-source recovery

## Blocked Claim Classes

Blocked from reuse or promotion from this handbook slice:

- handbook-originated board-level SI / EMC numerics
- exact frequency thresholds and cutovers
- exact capacitor values, ratios, value ladders, or placement recipes
- exact ESR / ESL / self-resonance / antiresonance numbers
- exact layer-count or stackup schemes presented as universal defaults
- exact source/load-impedance suitability rules for topology selection
- universal statements that a filter topology or component `works`, `must be used`, or `guarantees` suppression
- common-mode choke, ferrite bead, LC filter, feedthrough capacitor, and grounding scheme treated as interchangeable
- company-specific or dated examples
  - supplier price table
  - internal product cases
  - owner-specific device examples
  - dated ESD pass/fail anecdotes
- certification, compliance, or acceptance claims
  - `CISPR16 Class B`
  - ESD pass statements
  - any implication that handbook guidance proves compliance
- universal grounding-family rules based on old frequency breakpoints or wavelength heuristics

## Image / Table Pages For Later Selective Vision Pass

Use later selective vision only where figure structure matters more than extracted text:

- `19-20`
  - current-path and filter-capacitor role diagrams
- `21-22`
  - ferrite-bead and common-mode-choke frequency-characteristic figures, low-pass topology figure set
- `23`
  - power EMI filter structure figure
- `24-28`
  - capacitor self-resonance / antiresonance / ESR / ESL figures, `表3-1`, insertion-loss comparison figures, decoupling-layout examples
- `29-30`
  - grounding-family and public-ground-impedance coupling figures

Do not spend vision effort on `9-18` or `31` for this lane; text extraction already captures the useful claim inventory there.

## Official-Source Gaps

High-value official-source recovery gaps revealed by this lane:

- current official source for capacitor role boundaries:
  - decoupling vs bypass vs bulk / storage
- current official source for capacitor parasitic / resonance boundaries:
  - self-resonance, ESR, ESL, parallel antiresonance
- current official source for low-pass topology selection posture:
  - when `L`, `C`, `Gamma`, `Pi`, and `T` topologies are described safely without cookbook numerics
- current official source for common-mode choke execution boundary
  - especially separation from ferrite beads and generic inductors
- current official source for grounding-family selection boundary
  - single-point vs multi-point vs floating vs hybrid without carrying old threshold rules into `llm_wiki`
- current official source for board-entry filter placement and power-entry clustering posture
  - especially clock, power module, coil, and interface-filter placement guidance at execution-boundary level
- current official source for multi-layer plane-adjacency / stackup tradeoff language
  - enough to explain posture, not enough to authorize handbook stackup tables

## Lane Status

Final status label: `completed_at_claim_family_level`

Meaning:

- handbook pages `9-31` are absorbed as demand / claim inventory
- strongest existing reuse is narrow and already bounded
- no new fact-layer or wiki-layer promotion is justified from this handbook slice alone
- next valid move is selective official-source recovery for capacitor, filter-topology, common-mode-choke, and grounding-family gaps
