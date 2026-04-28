# P4-39 2025.07.13 Tools / CAM / Via / Multilayer / Flex-Assembly Official-Source Recovery Scout

Date: 2026-04-28

## Purpose And Assigned Lane

Lane `P4-39 2025.07.13` audits the assigned `/code/blogs/tmps/2025.07.13/en` drafts as claim inventory only, then maps:

- existing `llm_wiki` support already usable for conservative upgrades
- official or durable source candidates already checked or recommended next
- exact claim families that remain blocked without official sources or dated internal capability records

This lane does not promote draft-originated numeric, capability, certification, price, lead-time, MOQ, yield, quality, process-window, impedance, tool-accuracy, supplier, or commercial claims into facts.

## Input Files Inspected

- `/code/blogs/tmps/2025.07.13/en/3d-viewer.md`
- `/code/blogs/tmps/2025.07.13/en/Online-Gerber-Viewer.md`
- `/code/blogs/tmps/2025.07.13/en/circuit-simulator-tool.md`
- `/code/blogs/tmps/2025.07.13/en/Online Impedance Calculator.md`
- `/code/blogs/tmps/2025.07.13/en/cam-engineering.md`
- `/code/blogs/tmps/2025.07.13/en/4-Layer PCB.md`
- `/code/blogs/tmps/2025.07.13/en/Multilayer-PCB.md`
- `/code/blogs/tmps/2025.07.13/en/blind-via-pcb.md`
- `/code/blogs/tmps/2025.07.13/en/Buried-Via-PCB.md`
- `/code/blogs/tmps/2025.07.13/en/microvia-pcb.md`
- `/code/blogs/tmps/2025.07.13/en/Flexible-PCB-Assembly.md`
- `/code/blogs/llm_wiki/logs/p4-33-lane-c-fabrication-structures.md`

## Per-Draft Claim Families

### `3d-viewer.md`

- browser-based 3D model viewing for STEP, STL, IGES, OBJ, FBX, IFC, BIM, and related formats
- claims around no-login, no-installation, local in-browser processing, privacy posture, unlimited use, and cross-browser compatibility
- claims around mechanical-clearance review, PCB fit-checking, sharing, screenshots, and support for special or proprietary formats
- HilPCB commercial and engineering-support claims

### `Online-Gerber-Viewer.md`

- online PCB / Gerber viewer for Gerber and drill data
- claims around support for Cadence Allegro `GDO` and broad EDA-tool compatibility
- viewer features such as layer visualization, zoom, pan, measurement, collaboration, and browser access
- claims that HilPCB can process virtually any PCB design-file format
- manufacturing, assembly, and DFM-handoff claims

### `circuit-simulator-tool.md`

- online circuit simulation for analog, digital, and mixed-signal circuits
- claims around SPICE-like behavior, waveform output, logic analysis, component libraries, and export flow
- comparisons against LTspice, Falstad, TINA-TI, or Multisim
- claims that simulation can transition directly into PCB design / manufacturing workflow
- free-use, platform-compatibility, and engineering-accuracy claims

### `Online Impedance Calculator.md`

- impedance-calculator framing for microstrip, stripline, differential-pair, and stackup planning
- claims around formula accuracy, instant results, material models, dielectric-thickness or copper-thickness inputs, and high-speed design use
- claims around tolerance, controlled-impedance feasibility, and direct manufacturing-readiness value
- possible coupling between calculator output and quote / DFM workflow

### `cam-engineering.md`

- CAM engineering as pre-production review between design and fabrication / assembly
- file-package intake claims around Gerber, drill, stackup, BOM, pick-and-place, and fabrication notes
- DFM / DFA / DFT / manufacturability review claims, issue detection, correction, panelization, drill-table cleanup, and production-file preparation
- claims around turnaround speed, error prevention, quote-stage review depth, and engineering support completeness

### `4-Layer PCB.md`

- 4-layer PCB structure, layer roles, grounding, power-plane, routing, EMI, and controlled-impedance framing
- stackup-selection and manufacturability guidance
- claims around cost, prototype suitability, signal-integrity benefit, and fabrication capability

### `Multilayer-PCB.md`

- multilayer PCB classification, stackup planning, layer-count growth, lamination, power / ground strategy, and high-density routing
- claims around complexity, manufacturability, high-speed suitability, and validation posture
- potential capability, thickness, tolerance, speed, and commercial claims

### `blind-via-pcb.md`

- blind-via definition, routing-density role, and HDI relationship
- claims around design benefits, fabrication complexity, reliability, and application fit
- possible geometry, fill, plating, lamination, and cost claims

### `Buried-Via-PCB.md`

- buried-via definition, multilayer routing role, and internal-layer interconnection
- claims around density, signal-routing efficiency, stackup complexity, and performance benefit
- possible lamination, drill/fill, reliability, and capability claims

### `microvia-pcb.md`

- microvia definition, HDI context, stacked/staggered architecture, sequential-build-up vocabulary, and density benefits
- claims around laser drilling, small geometry, registration, via-in-pad, reliability, and advanced-package use
- likely capability, yield, process-window, certification, and application-readiness claims

### `Flexible-PCB-Assembly.md`

- flex assembly versus rigid assembly framing
- handling, fixturing, reinforcement, placement, soldering, inspection, and bend-aware process needs
- substrate and material families such as PI, PET, PTFE composite, and LCP
- claims around component-size limits, placement accuracy, lead time, endurance, temperature range, compliance, and sector readiness

## Existing `llm_wiki` Support Found, With Paths / IDs

### Prior Batch-Level Fabrication-Structure Mapping

- `/code/blogs/llm_wiki/logs/p4-33-lane-c-fabrication-structures.md`
  - already classifies the `2025.07.13/en` structure family as partial-to-strong for multilayer, HDI / via, and flex material / process posture

### Multilayer / 4-Layer / Impedance / Advanced-Process Support

- `topic_id: processes-advanced-pcb-fabrication-and-stackup-planning`
  - Path: `/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
- `fact_id: methods-high-layer-count-backdrill-and-registration-posture`
  - Path: `/code/blogs/llm_wiki/facts/methods/high-layer-count-backdrill-and-registration-posture.md`
- `fact_id: methods-controlled-impedance-tdr-verification-posture`
  - Path: `/code/blogs/llm_wiki/facts/methods/controlled-impedance-tdr-verification-posture.md`
- `topic_id: processes-public-capability-parameter-consumption-map`
  - Path: `/code/blogs/llm_wiki/wiki/processes/public-capability-parameter-consumption-map.md`
- `fact_id: methods-parameter-scope-public-capability-construction-windows`
  - Path: `/code/blogs/llm_wiki/facts/methods/parameter-scope-public-capability-construction-windows.md`
- `source_id: ipc-6012f-toc`
  - Path: `/code/blogs/llm_wiki/sources/registry/standards/ipc-6012f-toc.md`

These support conservative multilayer, stackup-planning, validation-posture, and standards-hierarchy wording, but not free numeric stackups, capability tables, or commercial claims.

### Blind Via / Buried Via / Microvia / HDI Support

- `fact_id: standards-ecss-via-hdi-microvia-definitions`
  - Path: `/code/blogs/llm_wiki/facts/standards/ecss-via-hdi-microvia-definitions.md`
- `fact_id: standards-hdi-design-reference-status-metadata`
  - Path: `/code/blogs/llm_wiki/facts/standards/hdi-design-reference-status-metadata.md`
- `fact_id: standards-ipc-rigid-flex-and-microvia-reliability-metadata`
  - Path: `/code/blogs/llm_wiki/facts/standards/ipc-rigid-flex-and-microvia-reliability-metadata.md`
- `fact_id: methods-hdi-microvia-and-vippo-process-posture`
  - Path: `/code/blogs/llm_wiki/facts/methods/hdi-microvia-and-vippo-process-posture.md`
- `fact_id: methods-microvia-reliability-public-context`
  - Path: `/code/blogs/llm_wiki/facts/methods/microvia-reliability-public-context.md`
- `source_id: ipc-2226-design-standards`
  - Path: `/code/blogs/llm_wiki/sources/registry/standards/ipc-2226-design-standards.md`
- `source_id: ipc-microvia-reliability-warning-2019`
  - Path: `/code/blogs/llm_wiki/sources/registry/standards/ipc-microvia-reliability-warning-2019.md`
- `source_id: ipc-stacked-microvia-reliability-paper`
  - Path: `/code/blogs/llm_wiki/sources/registry/methods/ipc-stacked-microvia-reliability-paper.md`
- `source_id: nasa-nepp-microvia-reliability-2006`
  - Path: `/code/blogs/llm_wiki/sources/registry/methods/nasa-nepp-microvia-reliability-2006.md`

These already support official definition language, current-vs-legacy IPC reference hierarchy, and cautionary reliability framing for blind via, buried via, and microvia topics.

### Flex Assembly / Flex Material / Bend-Aware Process Support

- `topic_id: materials-flex-material-classes-pi-lcp-and-rigid-flex-boundaries`
  - Path: `/code/blogs/llm_wiki/wiki/materials/flex-material-classes-pi-lcp-and-rigid-flex-boundaries.md`
- `fact_id: materials-flex-polyimide-and-lcp-class-source-coverage`
  - Path: `/code/blogs/llm_wiki/facts/materials/flex-polyimide-and-lcp-class-source-coverage.md`
- `fact_id: methods-rigid-flex-stackup-and-bend-reliability-posture`
  - Path: `/code/blogs/llm_wiki/facts/methods/rigid-flex-stackup-and-bend-reliability-posture.md`
- `fact_id: methods-parameter-scope-rigid-flex-bend-guidance`
  - Path: `/code/blogs/llm_wiki/facts/methods/parameter-scope-rigid-flex-bend-guidance.md`
- `source_id: minco-flex-circuits-design-guide-2019`
  - Path: `/code/blogs/llm_wiki/sources/registry/methods/minco-flex-circuits-design-guide-2019.md`

These support class-level flex-material wording, bend-guidance context, and conservative handling / reliability posture, but not draft-originated assembly capability, endurance, placement, or commercial claims.

### CAM / DFM / Internal Review-Workflow Support

- `source_id: frontendapt-pcb-pcb-fabrication-process-page-en`
  - Path: `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-pcb-fabrication-process-page-en.md`
- `source_id: frontendapt-dfm-guidelines-resource-page-en`
  - Path: `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-dfm-guidelines-resource-page-en.md`
- `topic_id: processes-apt-resource-layer-for-dfm-faq-and-download-retrieval`
  - Path: `/code/blogs/llm_wiki/wiki/processes/apt-resource-layer-for-dfm-faq-and-download-retrieval.md`

These support internal review-flow vocabulary such as DFM intake, DFM / CAM ingestion, file-package review, and process-stage framing. They do not yet supply official-source coverage for broad CAM-engineering claims.

### Tool-Side Coverage Reality

- No meaningful existing `llm_wiki` fact, wiki, or registered-source layer was found for:
  - browser 3D-viewer capability
  - online Gerber-viewer capability
  - browser circuit-simulation capability
  - online impedance-calculator capability

Current support for these drafts is therefore mostly adjacent vocabulary only:

- impedance planning and TDR posture from `methods-controlled-impedance-tdr-verification-posture`
- DFM / file-package review posture from internal process and resource pages
- occasional mentions that simulation or Gerber files are part of broader workflow context

## Official Sources Checked Or Recommended

### Already Present In Local `llm_wiki`

- `IPC` standards metadata already registered for via / HDI / rigid-board framing:
  - `ipc-6012f-toc`
  - `ipc-2226-design-standards`
  - `ipc-microvia-reliability-warning-2019`
- public government / standards-body or public-paper support already registered for microvia reliability:
  - `nasa-nepp-microvia-reliability-2006`
  - `ipc-stacked-microvia-reliability-paper`
- vendor-primary flex design guidance already registered:
  - `minco-flex-circuits-design-guide-2019`
- internal non-blog records already registered for DFM / CAM / fabrication-process posture:
  - `frontendapt-pcb-pcb-fabrication-process-page-en`
  - `frontendapt-dfm-guidelines-resource-page-en`

### Strong Candidate Official Sources To Recover Next

#### Gerber / PCB Viewer / CAM Data-Format Owners

- `Ucamco` official Gerber-format pages
  - strongest candidate for Gerber ownership, format identity, and modern Gerber / X2 / X3 vocabulary
- `IPC-2581 Consortium` official specification or overview pages
  - strongest candidate for neutral manufacturing-data-transfer vocabulary beyond Gerber
- `Siemens / ODB++` official pages
  - candidate for `ODB++` identity and CAM / manufacturing-package vocabulary

These would support data-format identity and file-package taxonomy, not HilPCB/HIL/APT tool capability proof.

#### 3D Viewer / File-Format Owners

- official format-owner pages where relevant:
  - `Khronos` for glTF
  - `STEP` / ISO family references where accessible
  - format-owner documentation for STL / OBJ / IGES only if needed for neutral format identity

These would support file-format naming only. They would not prove a specific browser viewer supports or renders those formats correctly.

#### Circuit Simulation / SPICE Owners

- official simulator or method owners for neutral vocabulary:
  - `LTspice` official Analog Devices pages
  - official SPICE / ngspice documentation if later needed

These would support simulation vocabulary and comparison framing, not HilPCB simulator feature proof.

#### Impedance Calculator / Controlled-Impedance Sources

- field-solver / simulation-tool owners such as `Polar Instruments` or `Keysight` for guarded impedance-modeling vocabulary
- official laminate-vendor data when any calculator claim depends on dielectric-property inputs

These would support modeling context, not calculator accuracy or universal trace-geometry outputs.

#### Flex Assembly / Flex Process Owners

- `IPC-6013` public metadata already partly represented; further official metadata recovery could strengthen flex-performance-spec hierarchy
- material / process vendors for assembly-compatible flex-material handling if future drafts need more than class-level flex wording

## Strongest Source-Backed Fact-Upgrade Opportunities

### `4-Layer PCB.md` and `Multilayer-PCB.md`

- upgrade to conservative stackup-planning, validation-posture, and standards-hierarchy language from:
  - `processes-advanced-pcb-fabrication-and-stackup-planning`
  - `methods-high-layer-count-backdrill-and-registration-posture`
  - `methods-controlled-impedance-tdr-verification-posture`
  - `ipc-6012f-toc`
- keep all exact stackup counts, dimensions, tolerances, and capability numerics blocked unless separately sourced

### `blind-via-pcb.md`, `Buried-Via-PCB.md`, and `microvia-pcb.md`

- upgrade term definitions and HDI relationship from:
  - `standards-ecss-via-hdi-microvia-definitions`
  - `standards-hdi-design-reference-status-metadata`
- upgrade reliability caution and advanced-interconnect review posture from:
  - `standards-ipc-rigid-flex-and-microvia-reliability-metadata`
  - `methods-microvia-reliability-public-context`
  - `ipc-microvia-reliability-warning-2019`
  - `ipc-stacked-microvia-reliability-paper`
  - `nasa-nepp-microvia-reliability-2006`

### `Flexible-PCB-Assembly.md`

- upgrade material-family and bend-aware process posture from:
  - `materials-flex-polyimide-and-lcp-class-source-coverage`
  - `materials-flex-material-classes-pi-lcp-and-rigid-flex-boundaries`
  - `methods-rigid-flex-stackup-and-bend-reliability-posture`
  - `methods-parameter-scope-rigid-flex-bend-guidance`
- keep assembly-window, endurance, component-size, line-accuracy, and sector-readiness claims blocked

### `cam-engineering.md`

- partial upgrade possible for DFM-intake and process-backbone vocabulary from:
  - `frontendapt-pcb-pcb-fabrication-process-page-en`
  - `frontendapt-dfm-guidelines-resource-page-en`
  - `processes-apt-resource-layer-for-dfm-faq-and-download-retrieval`
  - `processes-advanced-pcb-fabrication-and-stackup-planning`
- usable framing:
  CAM engineering sits between design output and production release, and file-package review is broader than raw Gerber upload
- blocked:
  quote-turnaround depth, error-prevention rates, completeness promises, or HilPCB-specific tool/process superiority

## Blocked Claims Needing Official Sources Or Dated Capability Records

### Tool-Side Drafts Blocked Almost Entirely Beyond Topic Intent

- `3d-viewer.md`
  - exact supported format count
  - proprietary-format support
  - local-only processing / privacy architecture
  - browser / mobile compatibility guarantees
  - unlimited use / no-login / no-retention claims
  - rendering speed, collaboration, screenshot, or special-format support claims
- `Online-Gerber-Viewer.md`
  - Cadence Allegro `GDO` support claim
  - broad EDA-native file compatibility claims
  - measurement-tool, collaboration-link, or browser-feature claims
  - “can handle virtually any PCB file format” claims
- `circuit-simulator-tool.md`
  - analog / digital / mixed-signal engine details
  - waveform, logic-analyzer, component-library, and export claims
  - comparisons versus LTspice, Falstad, TINA-TI, or Multisim
  - “free unlimited use” and cross-platform claims
- `Online Impedance Calculator.md`
  - calculator accuracy, formula authority, material-model fidelity, or manufacturing-readiness claims
  - direct tolerance or controlled-impedance guarantee claims

### CAM / Manufacturing-Service Claims Still Blocked

- `cam-engineering.md`
  - turnaround-time promises
  - exact file-repair, panelization, or engineering-review depth claims
  - same-day DFM / CAM response promises
  - HilPCB/HIL/APT team capability proof without dated non-blog records

### Fabrication / Via / Flex Claims Still Blocked

- all draft-originated numeric claims for:
  - layer-count ceilings
  - stackup thicknesses
  - trace / space / via / microvia dimensions
  - laser-drill, fill, plating, or lamination windows
  - impedance tolerance or calculator output authority
  - placement accuracy, component-size floors, endurance cycles, temperature ranges, lead times, MOQ, or pricing
- all supplier or commercial claims for:
  - factory breadth
  - quality rates
  - certifications
  - volume / quick-turn / response-time / cost advantage
  - sector qualification or release readiness

## Residual Gaps

- there is still no official-source-backed `llm_wiki` layer for HilPCB/HIL/APT online tool capability claims
- no registered source was found for neutral Gerber-viewer or 3D-viewer feature authority inside current local `llm_wiki`
- no registered source was found for circuit-simulator feature authority inside current local `llm_wiki`
- no official-source-backed impedance-calculator record exists yet for this lane
- CAM engineering is only partially supported through internal non-blog workflow pages, not through standards-body or format-owner sources
- multilayer / via / flex topics are comparatively well covered at boundary and metadata level, but still lack authorization for many draft numeric and commercial claims

## Completion Status Using Standard Labels

- lane status: `completed`
- evidence outcome: `existing_support_mapped`
- official-source recovery outcome: `candidate_recovery_targets_identified`
- blocked-claim outcome: `high_risk_claims_held`
- publish-readiness shape for this lane:
  - `3d-viewer.md`: `claim_inventory_only`
  - `Online-Gerber-Viewer.md`: `claim_inventory_only`
  - `circuit-simulator-tool.md`: `claim_inventory_only`
  - `Online Impedance Calculator.md`: `claim_inventory_only`
  - `cam-engineering.md`: `partial_source_backed_upgrade_possible`
  - `4-Layer PCB.md`: `partial_source_backed_upgrade_possible`
  - `Multilayer-PCB.md`: `partial_source_backed_upgrade_possible`
  - `blind-via-pcb.md`: `partial_source_backed_upgrade_possible`
  - `Buried-Via-PCB.md`: `partial_source_backed_upgrade_possible`
  - `microvia-pcb.md`: `partial_source_backed_upgrade_possible`
  - `Flexible-PCB-Assembly.md`: `partial_source_backed_upgrade_possible`
