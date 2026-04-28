# P4-43 2026.4.1 Two-Layer Specialty PCB Official-Source Recovery Scout

Date: 2026-04-28
Lane: `P4-43 official-source recovery scout`
Input directory: `/code/blogs/tmps/2026.4.1/en`
Output file: `/code/blogs/llm_wiki/logs/p4-43-2026-4-1-two-layer-specialty-pcb-official-source-recovery-scout.md`
Status: `completed_at_claim_family_level`

## Purpose

This scout log audits the 27 English `2-layer` drafts in `/code/blogs/tmps/2026.4.1/en` as claim inventory only.

It checks whether existing `llm_wiki` support already covers the allowed baseline for:

- `APTPCB260401` 2-layer draft boundary
- 2-layer / single-double-layer baseline routing
- `FR-4`
- `high-Tg`
- aluminum / `IMS`
- ceramic
- copper-core
- `ENIG` / `HASL` / `OSP` / lead-free `HASL`
- `PTFE` / Rogers / Teflon / RF / microwave
- polyimide / flex materials
- `PCBA` assembly
- prototype / quick-turn / service / cost boundaries

This lane does not add facts, wiki pages, tracker updates, or reusable source records.

## Input File Inventory

- `2-layer-aluminum-pcb.md`
- `2-layer-ceramic-pcb.md`
- `2-layer-copper-core-pcb.md`
- `2-layer-enig-pcb.md`
- `2-layer-fr4-pcb.md`
- `2-layer-hasl-pcb.md`
- `2-layer-high-frequency-pcb.md`
- `2-layer-high-tg-pcb.md`
- `2-layer-lead-free-hasl-pcb.md`
- `2-layer-microwave-pcb.md`
- `2-layer-osp-pcb.md`
- `2-layer-pcb-assembly.md`
- `2-layer-pcb-board.md`
- `2-layer-pcb-fabrication.md`
- `2-layer-pcb-low-cost.md`
- `2-layer-pcb-manufacturer.md`
- `2-layer-pcb-manufacturing.md`
- `2-layer-pcb-prototype.md`
- `2-layer-pcb-quick-turn.md`
- `2-layer-pcb-supplier.md`
- `2-layer-pcb.md`
- `2-layer-polyimide-pcb.md`
- `2-layer-printed-circuit-board.md`
- `2-layer-ptfe-pcb.md`
- `2-layer-rf-pcb.md`
- `2-layer-rogers-pcb.md`
- `2-layer-teflon-pcb.md`

## Draft Heading Inventory

Claim families present across the batch:

- baseline 2-layer stackup, thickness, copper distribution, vias, annular ring, drilling, current capacity, routing, EMC, impedance
- `FR-4` and `high-Tg` material choice
- aluminum / `MCPCB` / `IMS`, ceramic, copper-core thermal-platform comparisons
- `ENIG`, `HASL`, lead-free `HASL`, and `OSP` finish chemistry and selection
- `PTFE`, Teflon, Rogers, RF, high-frequency, and microwave material-selection and layout claims
- polyimide, flex, and rigid-vs-flex high-temperature claims
- `PCBA`, stencil, SMT, THT, turnkey, testing, and assembly-yield claims
- prototype, quick-turn, fabrication, manufacturing, supplier, manufacturer, and low-cost service claims
- application framing for keyboard, LED, automotive, drone, aerospace, defense, satellite, industrial, telecom, and consumer contexts

## Existing `llm_wiki` Support Checked

### Existing batch-specific governance

- `facts/methods/aptpcb260401-2-layer-draft-consumption-boundary.md`
- `logs/p4-31-aptpcb260401-2-layer-blog-ingestion-map.md`
- `logs/p4-33-full-tmps-source-gap-register.md`

Disposition:

- `APTPCB260401` already has a source-backed draft-consumption boundary and ingestion-map layer.
- The current `/code/blogs/tmps/2026.4.1/en` batch matches that same 27-file 2-layer family and should inherit the same conservative handling.
- Existing support is `source_backed_fact_layer_partial` at the surrounding material/process layer, but only `completed_at_claim_family_level` for the draft batch itself.

### 2-layer baseline and routing support

- `facts/materials/hil-base-laminate-and-build-stage-family-map.md`
- `wiki/processes/prototype-vs-quick-turn-pcb-routing.md`
- `facts/methods/pcb-prototype-quickturn-and-volume-routing.md`
- `sources/registry/internal/frontendhil-single-double-layer-pcb-product-page-en.md`
- `sources/registry/internal/frontendhil-fr4-pcb-product-page-en.md`
- `sources/registry/internal/frontendhil-pcb-prototype-landing-en.md`
- `sources/registry/internal/frontendhil-quick-turn-pcb-landing-en.md`
- `sources/registry/internal/frontendapt-pcb-pcb-prototype-page-en.md`
- `sources/registry/internal/frontendapt-pcb-quick-turn-pcb-page-en.md`
- `sources/registry/internal/frontendapt-pcb-npi-small-batch-pcb-manufacturing-page-en.md`
- `sources/registry/internal/frontendapt-pcb-mass-production-pcb-manufacturing-page-en.md`

What this supports safely:

- `single/double-layer` as a low-complexity internal product family
- prototype vs quick-turn vs NPI vs mass-production as separate routing/service postures
- conservative wording that 1-2 layer `FR-4` is the common quick-turn baseline

What remains blocked:

- universal 2-layer stackup defaults
- 24-72 hour promises
- guaranteed finish-dependent turnarounds
- supplier-specific process windows, yields, queue priority, or rush capability

### `FR-4` and `high-Tg` support

- `facts/materials/fr4-official-source-coverage.md`
- `facts/materials/isola-fr4-high-tg-product-grade-fields.md`
- `facts/materials/iteq-it-180a-high-tg-fr4-product-coverage.md`
- `facts/materials/shengyi-s1000-2-vs-s1000-2m-high-tg-fr4-coverage.md`
- `facts/materials/non-isola-fr4-to-very-low-loss-coverage.md`
- `sources/registry/internal/frontendhil-fr4-pcb-product-page-en.md`
- `sources/registry/internal/frontendhil-high-tg-pcb-product-page-en.md`
- `sources/registry/internal/frontendapt-pcb-fr4-pcb-page-en.md`
- `sources/registry/internal/frontendapt-pcb-high-tg-pcb-page-en.md`

What this supports safely:

- `FR-4` is a family, not one universal property row
- `high-Tg` must stay product-specific when numeric values appear
- internal HIL/APT pages can frame service posture, not substitute for datasheets

What remains blocked:

- generic `FR-4` thickness, Dk, Df, Tg, CTE, or impedance tables
- draft-originated layer-stack defaults
- automotive-grade, lead-free reliability, and thermal-resilience conclusions without exact product or dated qualification evidence

### Aluminum / `IMS` / thermal-platform support

- `wiki/materials/ceramic-aln-ims-thermal-platforms.md`
- `facts/materials/parameter-scope-ventec-ims-material-values.md`
- `facts/methods/mcpcb-ims-and-reflow-source-coverage.md`
- `sources/registry/materials/ventec-ims-family-overview.md`
- `sources/registry/internal/frontendapt-pcb-metal-core-pcb-page-en.md`
- `sources/registry/internal/frontendhil-metal-core-pcb-product-page-en.md`

What this supports safely:

- `IMS` / metal-core as a separate thermal-platform family
- exact-product Ventec `IMS` values only when product identity and conditions stay attached
- MCPCB assembly as combined material-selection plus paste/profile validation context

What remains blocked:

- supplier-neutral `IMS` ranking tables
- thermal-resistance formulas or finished-board thermal outcomes copied from drafts
- base-metal, dielectric-thickness, copper-weight, and reflow success claims for unnamed products

### Ceramic support

- `wiki/materials/ceramic-aln-ims-thermal-platforms.md`
- `facts/materials/ceramic-alumina-aln-class-source-coverage.md`
- `facts/materials/thin-film-ceramic-circuit-technology-kyocera.md`
- `facts/materials/ltcc-class-definition-and-nonclaims.md`
- `sources/registry/internal/frontendhil-ceramic-pcb-product-page-en.md`
- `sources/registry/internal/frontendapt-ceramic-pcb-capability-page-en.md`
- `sources/registry/materials/ceramtec-ceramic-substrates-page.md`

What this supports safely:

- ceramic, alumina, and `AlN` as class-level thermal-platform vocabulary
- separation between ceramic substrate families and `IMS`
- guarded mention of `LTCC` or thin-film ceramic as distinct technology lanes

What remains blocked:

- alumina-vs-`AlN` numeric comparison tables
- `DBC`, thick-film, and metallization process values
- finished-board RF/thermal outcomes, cost, lead time, or capability proof

### Copper-core support

Existing support found:

- indirect thermal-platform support through `wiki/materials/ceramic-aln-ims-thermal-platforms.md`
- `IMS` / MCPCB method support through `facts/methods/mcpcb-ims-and-reflow-source-coverage.md`
- gap register note: `P1` `HDI / via / edge-feature evidence` explicitly includes `copper-core`

Disposition:

- `blocked_pending_official_source`

Reason:

- no dedicated current copper-core fact/wiki/source layer was found in `llm_wiki`
- draft comparisons between copper-core and aluminum-core remain inventory only

### Surface-finish support: `ENIG` / `HASL` / `OSP` / lead-free `HASL`

- `facts/standards/ipc-surface-finish-taxonomy-osp-hasl-extension.md`
- `facts/standards/ipc-finish-standards-metadata.md`
- `facts/methods/finish-zoning-by-assembly-sequence-and-storage-exposure.md`
- `sources/registry/internal/frontendapt-pcb-surface-finishes-page-en.md`
- `sources/registry/internal/frontendhil-pcb-surface-finish-landing-en.md`

What this supports safely:

- corrected public taxonomy for `ENIG`, immersion silver, immersion tin, `OSP`, and `ENEPIG`
- guarded `HASL` / solder-coating vocabulary through IPC public metadata
- finish selection as storage, assembly-sequence, and process-context discussion

What remains blocked:

- finish thickness tables
- shelf-life values
- black-pad prevention guarantees
- planarity, solderability, pore/corrosion, or RF-loss rankings
- leaded vs lead-free `HASL` commercial or regulatory conclusions for current supplier service

### `PTFE` / Rogers / Teflon / RF / microwave support

- `wiki/materials/rogers-ro3000-family.md`
- `wiki/materials/rf-material-selector-by-application-band.md`
- `wiki/processes/ptfe-processing-and-manufacturability.md`
- `facts/materials/ptfe-rf-material-processing-posture.md`
- `facts/materials/apt-rogers-internal-framing.md`
- `facts/materials/parameter-scope-rogers-rf-laminate-values.md`
- `facts/materials/rogers-material-selector.md`
- exact-product Rogers cards:
  - `facts/materials/rogers-ro3003.md`
  - `facts/materials/rogers-ro3006.md`
  - `facts/materials/rogers-ro3010.md`
  - `facts/materials/rogers-ro3035.md`
  - `facts/materials/rogers-ro4003c.md`
  - `facts/materials/rogers-ro4350b.md`
  - `facts/materials/rogers-rt-duroid-5880.md`
  - `facts/materials/rogers-rt-duroid-6002.md`
  - `facts/materials/rogers-rt-duroid-6202.md`
  - `facts/materials/rogers-tmm-family.md`
- `sources/registry/internal/frontendhil-teflon-pcb-product-page-en.md`
- `sources/registry/internal/frontendhil-rogers-product-page-en.md`
- `sources/registry/internal/frontendapt-materials-teflon-pcb-page-en.md`
- `sources/registry/internal/frontendapt-materials-rf-rogers-page-en.md`
- `sources/registry/internal/frontendapt-materials-rogers-pcb-manufacturing-page-en.md`

What this supports safely:

- Rogers, `PTFE`, and Teflon-family materials must stay product-specific when numeric values appear
- internal pages support process framing, hybrid-stackup posture, and RF-validation vocabulary
- RF articles may discuss return path, material selection posture, and validation sensitivity conservatively

What remains blocked:

- 50-ohm geometry rules from generic 2-layer drafts
- link-budget, antenna, Ka-band, satellite, `5G`, drone, or mmWave performance promises
- supplier capability, yield, lead time, or cost claims for Rogers / `PTFE` builds

### Polyimide / flex-material support

- `wiki/materials/flex-material-classes-pi-lcp-and-rigid-flex-boundaries.md`
- `facts/materials/flex-polyimide-and-lcp-class-source-coverage.md`
- `facts/methods/rigid-flex-stackup-and-bend-reliability-posture.md`
- `facts/methods/parameter-scope-rigid-flex-bend-guidance.md`
- `facts/standards/ipc-2223e-flex-rigid-flex-design-metadata.md`
- `sources/registry/internal/frontendhil-flex-pcb-product-page-en.md`
- `sources/registry/internal/frontendhil-rigid-flex-pcb-product-page-en.md`
- `sources/registry/internal/frontendapt-pcb-flex-pcb-page-en.md`
- `sources/registry/internal/frontendapt-pcb-rigid-flex-pcb-page-en.md`

What this supports safely:

- class-level flex / rigid-flex material framing
- narrow exact-product exceptions for non-generic flex material rows
- bend/reliability as guarded design-guidance posture, not universal numeric rules

What remains blocked:

- generic polyimide / Kapton / `UPILEX` property tables
- dynamic-flex cycle-life promises
- aerospace-grade, wearable-grade, or release-readiness conclusions

### `PCBA` assembly support

- `wiki/processes/pcba-npi-to-mass-production-flow.md`
- `wiki/testing/pcba-quality-gates-and-test-strategy.md`
- `facts/methods/pcba-mixed-technology-assembly-flow.md`
- `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`
- `facts/methods/pcba-stencil-selective-solder-and-fine-pitch-controls.md`
- `facts/methods/tht-pressfit-terminal-route-boundary.md`
- `facts/methods/pcba-test-method-selection-framework.md`
- `facts/methods/pcba-flying-probe-vs-ict-selection-posture.md`
- `facts/methods/hidden-joint-xray-inspection-boundary.md`
- `sources/registry/internal/frontendapt-pcba-smt-tht-page-en.md`
- `sources/registry/internal/frontendapt-pcba-turnkey-assembly-page-en.md`
- `sources/registry/internal/frontendhil-turnkey-assembly-product-page-en.md`
- `sources/registry/internal/frontendhil-smt-assembly-product-page-en.md`
- `sources/registry/internal/frontendhil-through-hole-assembly-product-page-en.md`
- `sources/registry/internal/frontendapt-pcba-stencil-page-en.md`
- `sources/registry/internal/frontendapt-pcba-ict-test-page-en.md`
- `sources/registry/internal/frontendapt-pcba-flying-probe-testing-page-en.md`
- `sources/registry/internal/frontendapt-pcba-x-ray-inspection-page-en.md`

What this supports safely:

- SMT/THT/turnkey/mixed-technology route framing
- stencil, inspection, and test-method vocabulary
- NPI-to-volume handoff and quality-gate structure

What remains blocked:

- assembly yield numbers
- stencil aperture rules copied from drafts
- exact test coverage percentages
- turnkey savings, price, throughput, or release-quality guarantees

### Service / supplier / manufacturer / cost boundaries

- `facts/methods/2025-10-1-commercial-service-legal-sensitive-draft-consumption-boundary.md`
- `wiki/processes/international-pcb-procurement-shipping-boundaries.md`
- `logs/p4-33-full-tmps-source-gap-register.md`

What this supports safely:

- commercial and supplier drafts are high-risk and need explicit gating
- landed-cost, logistics, procurement, and service vocabulary can be discussed at boundary level only

What remains blocked:

- pricing formulas
- savings percentages
- `MOQ`
- lead-time windows
- direct-factory proof
- equipment/audit conclusions
- quality-rate, yield, lifecycle-management, or certification claims

## Per-Claim-Family Disposition

| claim family | disposition | notes |
| --- | --- | --- |
| `APTPCB260401` 2-layer draft boundary | `source_backed_fact_layer_partial` | Existing boundary and ingestion map already govern the batch, but only as draft-consumption control |
| 2-layer baseline routing and service posture | `source_backed_fact_layer_partial` | Prototype / quick-turn / single-double-layer framing exists; design-rule numerics remain blocked |
| `FR-4` / `high-Tg` family framing | `source_backed_fact_layer_partial` | Exact-product anchors exist; generic family numerics remain blocked |
| aluminum / `IMS` | `source_backed_fact_layer_partial` | Thermal-platform and exact-product `IMS` support exist; board-level thermal claims remain blocked |
| ceramic / alumina / `AlN` | `source_backed_fact_layer_partial` | Class-level coverage exists; process and parameter comparisons remain blocked |
| copper-core | `blocked_pending_official_source` | No dedicated current copper-core source-backed layer found |
| `ENIG` / `HASL` / `OSP` / lead-free `HASL` taxonomy | `source_backed_fact_layer_partial` | Public taxonomy and finish-boundary support exist; chemistry/performance specifics remain blocked |
| `PTFE` / Rogers / Teflon / RF / microwave | `source_backed_fact_layer_partial` | Strong exact-product and process-posture support exists; board-level RF outcomes remain blocked |
| polyimide / flex materials | `source_backed_fact_layer_partial` | Class-level support exists; generic PI numeric or bend-life claims remain blocked |
| `PCBA` assembly / test / inspection | `source_backed_fact_layer_partial` | Route and test vocabulary exist; yield and capability claims remain blocked |
| prototype / quick-turn / supplier / manufacturer / cost | `blocked_pending_dated_capability_record` | public/internal boundary support exists, but supplier-specific commercial and capability claims need dated records |

## Safe Reuse Classes

Safe reuse from this batch is limited to:

- topic labels and article-intent clustering
- section shape and reader-question discovery
- conservative material-family framing already supported by source-backed `llm_wiki` cards
- conservative process and routing posture language for prototype, quick-turn, `PCBA`, RF-validation, and thermal-platform selection
- explicit blocker inventory for unsupported numeric, capability, and commercial claims

## Blocked Claim Classes

Do not promote from these drafts into facts:

- 2-layer thickness, copper, trace-width, spacing, via, drill, annular-ring, current-capacity, impedance, EMC, thermal-resistance, or stackup-default values
- material parameters for unnamed `FR-4`, `high-Tg`, aluminum-core, copper-core, ceramic, alumina, `AlN`, polyimide, Kapton, `PTFE`, Teflon, or Rogers families
- finish chemistry, finish thickness, shelf life, planarity, black-pad, solderability, or reflow claims
- RF, microwave, satellite, antenna, telecom, or mmWave board-performance claims
- process limits, yield, quality-rate, throughput, equipment, direct-factory, or supplier-audit claims
- certification, compliance, qualification, automotive-grade, aerospace-grade, defense-grade, medical-grade, or legal/IP conclusions
- price, low-cost rankings, `MOQ`, quote logic, lead time, inventory, VMI, or lifecycle claims

## Official-Source Gaps

### Gaps already partially covered but still open

- finish chemistry and finish-limit lane:
  - public IPC metadata gives taxonomy only
  - still needs official chemistry/vendor guides or dated process records for stronger finish-specific articles

- `IMS` / thermal lane:
  - exact-product Ventec anchors exist
  - still thin for supplier-neutral aluminum-vs-copper-vs-ceramic thermal comparison

- RF / microwave lane:
  - Rogers exact-product support is strong
  - still blocked for finished-board RF outcomes and supplier-specific manufacturing promises

- flex / polyimide lane:
  - class-level coverage exists
  - still missing broader official PI supplier coverage for generic polyimide discussion

### Gaps with no sufficient current support found for this lane

- copper-core official-source layer
- current official-source support that cleanly separates leaded vs lead-free `HASL` process/capability claims for conservative supplier writing
- dated APT/HIL capability records for 2-layer quick-turn, low-cost, supplier, manufacturer, and commercial claims

## Recommended Next Recovery Lanes

1. `copper-core-material-and-process-source-recovery`
   Status target: `blocked_pending_official_source` -> `source_backed_fact_layer_partial`
   Need: official copper-core material/process vendor pages or datasheets plus strict non-generalization rules.

2. `finish-chemistry-and-selection-boundaries`
   Status target: keep as `source_backed_fact_layer_partial`
   Need: official finish chemistry/process guides for `HASL`, lead-free `HASL`, `OSP`, and `ENIG` beyond IPC identity metadata.

3. `two-layer-commercial-and-capability-record-lane`
   Status target: `blocked_pending_dated_capability_record`
   Need: dated internal capability/commercial records for quick-turn windows, cost posture, supplier/manufacturer proof, inspection scope, and production readiness.

4. `ims-vs-ceramic-vs-copper-core-thermal-platform-separation`
   Status target: `source_backed_fact_layer_partial`
   Need: additional official thermal-platform sources so comparison pages stop flattening `IMS`, ceramic, and copper-core into one category.

5. `polyimide-exact-product-follow-on`
   Status target: `source_backed_fact_layer_partial`
   Need: official polyimide exact-product anchors if future 2-layer polyimide articles require more than class-level posture.

## Lane Verdict

The `/code/blogs/tmps/2026.4.1/en` batch is governed and deletion-safe at claim-family level.

Existing `llm_wiki` support is broad enough to prevent unsupported promotion of most material-family, surface-finish, RF, thermal-platform, `PCBA`, and prototype/quick-turn draft prose. It is not broad enough to authorize copper-core claims, supplier/manufacturer/commercial assertions, or draft-originated 2-layer numeric rules.

Recommended status language for this lane:

- `completed_at_claim_family_level`
- `source_backed_fact_layer_partial`
- `blocked_pending_official_source`
- `blocked_pending_dated_capability_record`

No tracker, fact, wiki, or source-registry updates were made in this lane.
