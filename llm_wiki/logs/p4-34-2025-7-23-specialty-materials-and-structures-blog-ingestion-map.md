# P4-34 2025.7.23 Specialty Materials And Structures Blog Ingestion Map

Date: 2026-04-28
Status: `source_backed_fact_layer_partial`
Input root: `/code/blogs/tmps/2025.7.23/en`
Allowed edit scope: this log only

## Purpose

Create a deletion-safe intake map for the English specialty-materials and surface-finish drafts under `/code/blogs/tmps/2025.7.23/en`.

This pass treats `tmps` drafts as claim inventory only. It does not promote draft-originated numbers, process limits, capability claims, certifications, lead times, prices, MOQs, yields, quality rates, application-readiness claims, or supplier claims into reusable facts.

## File List

- `alumina-pcb.md`
- `aluminum-nitride-pcb.md`
- `ceramic-circuit-board-manufacturing.md`
- `enepig-pcb.md`
- `enig-pcb.md`
- `epoxy-pcb.md`
- `hasl-pcb.md`
- `high-tg-pcb.md`
- `hybrid-circuit-board.md`
- `immersion-gold-pcb.md`
- `immersion-silver-pcb.md`
- `isola-pcb.md`
- `kapton-pcb.md`
- `lead-free-hasl-pcb.md`
- `ltcc-pcb.md`
- `osp-pcb.md`
- `pcb-copper-foil.md`
- `pcb-insulation.md`
- `pcb_surface_finish_guide.md`
- `peelable-mask-pcb.md`
- `polyimide-pcb.md`
- `ptfe-pcb.md`
- `taconic-pcb.md`
- `teflon-pcb.md`
- `thermally-conductive-pcb.md`
- `waterproof-pcb.md`

## Title And Topic Inventory

### Ceramic / thermal platform cluster

- `alumina-pcb.md`: alumina substrate properties, metallization, quality control, applications, ceramic assembly
- `aluminum-nitride-pcb.md`: AlN thermal/electrical properties, substrate prep, metallization, high-power applications, assembly
- `ceramic-circuit-board-manufacturing.md`: ceramic materials, metallization, thermal management, production, assembly
- `ltcc-pcb.md`: LTCC material systems, 3D integration, manufacturing flow, RF/packaging applications
- `thermally-conductive-pcb.md`: thermal material selection, heat-dissipation design rules, manufacturing, application stories

### Flex / polyimide / PTFE / RF material cluster

- `kapton-pcb.md`: Kapton material properties, flex manufacturing, design rules, applications, QA
- `polyimide-pcb.md`: polyimide material characteristics, processing, polyimide vs FR-4, applications, testing
- `ptfe-pcb.md`: PTFE services, specialized processing, design considerations, application demand, testing
- `teflon-pcb.md`: Teflon/PTFE framing, specialized processing, application fit, QA
- `taconic-pcb.md`: Taconic materials, PTFE manufacturing, RF/microwave positioning, QA
- `isola-pcb.md`: Isola material family framing, high-speed use, manufacturing, QA, assembly
- `high-tg-pcb.md`: high-Tg material properties, applications, prototyping/volume, QA, FAQ
- `hybrid-circuit-board.md`: mixed-material integration, dissimilar-bonding control, RF/microwave performance, reliability validation

### Surface finish cluster

- `enig-pcb.md`: ENIG chemistry, design guidance, process control, reliability, use-case framing
- `enepig-pcb.md`: ENEPIG advantages, treatment technology, applications, comparisons, design guidelines, testing
- `hasl-pcb.md`: HASL fundamentals, leaded vs lead-free comparison, design optimization, quality control
- `lead-free-hasl-pcb.md`: lead-free HASL selection, process optimization, comparison, design considerations, QA
- `osp-pcb.md`: OSP definition, process, advantages, applications, OSP vs HASL/ENIG
- `immersion-gold-pcb.md`: immersion-gold benefits, applications, finish comparisons
- `immersion-silver-pcb.md`: immersion-silver benefits, applications, finish comparisons
- `pcb_surface_finish_guide.md`: finish families, finish-selection criteria, QA, cost/economic framing

### Specialty construction / protection / materials adjunct cluster

- `pcb-copper-foil.md`: foil types, manufacturing, high-frequency behavior, heavy-copper use, surface treatments
- `pcb-insulation.md`: insulation properties, material selection, design strategy, testing, manufacturing
- `peelable-mask-pcb.md`: peelable-mask applications, material compatibility, design guidelines, process integration
- `epoxy-pcb.md`: epoxy technology, manufacturing, assembly, QA/certifications, logistics/support
- `waterproof-pcb.md`: waterproofing technologies, conformal coating/potting, process flow, applications, design support, assembly

## Existing `llm_wiki` Support Found By Targeted Search

### Strongest existing support

- Ceramic / alumina / AlN class framing:
  `facts/materials/ceramic-alumina-aln-class-source-coverage.md`
  `wiki/materials/ceramic-aln-ims-thermal-platforms.md`
- Flex / polyimide / rigid-flex class framing:
  `facts/materials/dupont-kapton-hn.md`
  `facts/materials/flex-polyimide-and-lcp-class-source-coverage.md`
  `wiki/materials/flex-material-classes-pi-lcp-and-rigid-flex-boundaries.md`
- PTFE / Teflon / hybrid RF processing posture:
  `facts/materials/ptfe-rf-material-processing-posture.md`
  `facts/methods/ptfe-processing-capability.md`
  `facts/methods/hybrid-rf-stackup-capability.md`
  `wiki/processes/ptfe-processing-and-manufacturability.md`
  `wiki/processes/hybrid-rf-stackup-strategy.md`
- Surface-finish selection posture and standards metadata:
  `facts/methods/surface-finish-selection-for-rf.md`
  `facts/methods/selective-multi-finish-strategy.md`
  `facts/methods/finish-zoning-by-assembly-sequence-and-storage-exposure.md`
  `facts/standards/ipc-finish-standards-metadata.md`
  `wiki/processes/rf-surface-finish-selection.md`
  `wiki/processes/finish-zoning-and-selective-multi-finish.md`
- Isola / Taconic / Teflon / high-Tg family coverage posture:
  `facts/materials/internal-material-family-coverage-map.md`
  `facts/materials/isola-site-mentioned-family-coverage.md`
  `facts/materials/taconic-official-source-coverage-gap.md`
  `wiki/materials/internal-material-family-coverage-and-refresh-rules.md`
- Thermal / coating / protection boundary support:
  `facts/methods/thermal-pcb-platform-selection-posture.md`
  `facts/methods/conformal-coating-source-coverage.md`
  `facts/methods/conformal-coating-automotive-ev-power-boundary.md`
  `wiki/processes/conformal-coating-protection-workflow-and-application-boundaries.md`
  `wiki/processes/conformal-coating-application-readiness-map.md`

### Coverage shape

- Current support is good for class-level framing, process-boundary language, and finish-selection posture.
- Current support is weak for exact finish chemistry, exact product-grade material parameters across most of this batch, waterproof/protective outcome claims, peelable-mask specifics, insulation numerics, copper-foil parameter tables, LTCC process/property claims, and supplier capability narratives.

## Safe Reuse Classes

- Topic clustering, file intent, and heading structure
- Class-level ceramic/alumina/AlN thermal-platform framing
- Class-level flex/polyimide/Kapton boundary framing, with `Kapton HN` usable only as an exact-product example rather than a generic substitute
- PTFE/Teflon processing difficulty and mixed-material / hybrid-stackup posture
- Qualitative Isola / Taconic / high-Tg family positioning where already supported by existing `llm_wiki` boundary cards
- Surface-finish selection logic at a conservative level: ENIG vs ENEPIG vs immersion silver vs OSP vs HASL as use-case posture, not as numeric finish tables
- Waterproof/coating topics only as protection-workflow intent and source-gap discovery
- FAQ and application sections only as reader-question inventory, not as proof

## Blocked Claim Classes

- Material-property numbers: dielectric, loss, thermal conductivity, Tg, Td, CTE, breakdown, insulation resistance, copper roughness, foil thickness, peel strength
- Process limits and recipes: lamination windows, drilling/plasma conditions, metallization recipes, finish thickness, storage windows, shelf life, cure schedules, reflow handling, peelable-mask dimensions
- Capability and readiness claims: factory qualification, assembly readiness, RF or high-power readiness, volume readiness, quick-turn posture, test coverage, yield, quality rate
- Supplier and commercial claims: manufacturer superiority, direct-factory proof, certifications, global logistics proof, cost, lead time, MOQ, stock, pricing
- Comparative ranking claims copied from drafts: “best”, “ideal”, “superior”, “more reliable”, “better solderability”, “cost-effective”, “long-term durability”
- Application qualification claims: automotive, aerospace, medical, military, RF power, laser diode, waterproof IP level, harsh-environment lifetime, wire-bond readiness unless separately sourced

## Per-Draft Disposition

| Draft | Disposition | Safe reuse now | Blocked or still missing |
| --- | --- | --- | --- |
| `alumina-pcb.md` | `source_backed_fact_layer_partial` | alumina as ceramic-substrate class, metallization/application topic shape | numeric property tables, assembly capability, quality outcomes |
| `aluminum-nitride-pcb.md` | `source_backed_fact_layer_partial` | AlN as ceramic thermal-platform class, high-power topic intent | exact AlN thermal/electrical values, RF-power readiness, assembly capability |
| `ceramic-circuit-board-manufacturing.md` | `source_backed_fact_layer_partial` | ceramic substrate family framing, metallization/manufacturing section shape | process values, ceramic-vs-other-platform rankings, supplier proof |
| `ltcc-pcb.md` | `completed_at_claim_family_level` | LTCC topic inventory and RF/packaging section shape | LTCC material systems, shrinkage/process values, 3D integration capability claims |
| `thermally-conductive-pcb.md` | `completed_at_claim_family_level` | thermal-management topic shape and material-selection questions | heat-dissipation rules, thermal-outcome claims, success-story proof |
| `kapton-pcb.md` | `source_backed_fact_layer_partial` | Kapton/polyimide family topic framing with exact-product boundary awareness | generic Kapton values, flex capability, bend/reliability metrics |
| `polyimide-pcb.md` | `source_backed_fact_layer_partial` | polyimide class framing and polyimide-vs-FR-4 topic shape | generic PI property tables, process windows, application qualification |
| `ptfe-pcb.md` | `source_backed_fact_layer_partial` | PTFE process-challenge framing, application topic intent | property numbers, DFM rules, production/logistics claims |
| `teflon-pcb.md` | `source_backed_fact_layer_partial` | Teflon/PTFE terminology and process-boundary framing | generic Teflon values, performance proof, supplier claims |
| `taconic-pcb.md` | `completed_at_claim_family_level` | Taconic family topic clustering and RF-material intent | product-grade Taconic values, broad capability claims, QA proof |
| `isola-pcb.md` | `source_backed_fact_layer_partial` | Isola family-positioning topic intent and high-speed material-family framing | unsupported exact Isola family substitutions, capability claims, logistics/support proof |
| `high-tg-pcb.md` | `source_backed_fact_layer_partial` | high-Tg family framing and application-question inventory | exact Tg thresholds as universal rules, cost deltas, MOQ/certification claims |
| `hybrid-circuit-board.md` | `source_backed_fact_layer_partial` | hybrid stackup strategy and mixed-material integration posture | exact bonding controls, RF-performance outcomes, validation proof |
| `enig-pcb.md` | `source_backed_fact_layer_partial` | ENIG use-case framing, reliability-risk topic inventory, design-guidance structure | chemistry-outcome claims, thickness, black-pad control proof, universal finish claims |
| `enepig-pcb.md` | `source_backed_fact_layer_partial` | ENEPIG as mixed-assembly / wire-bond-adjacent finish option | process details, finish-property tables, factory capability proof |
| `hasl-pcb.md` | `completed_at_claim_family_level` | HASL topic intent and comparison structure | technical parameters, planarity claims, leaded-vs-lead-free ranking |
| `lead-free-hasl-pcb.md` | `completed_at_claim_family_level` | lead-free HASL topic intent and design-question inventory | process optimization claims, comparative outcome claims, QA/test proof |
| `osp-pcb.md` | `completed_at_claim_family_level` | OSP as finish family and comparison topic | chemistry, shelf life, application ranking, finish-economics claims |
| `immersion-gold-pcb.md` | `completed_at_claim_family_level` | finish-comparison and benefit-category headings | exact finish identity/chemistry claims, durability/speed advantages, supplier proof |
| `immersion-silver-pcb.md` | `source_backed_fact_layer_partial` | immersion-silver low-loss selection posture at qualitative level | exact shelf life, tarnish/solderability behavior, cost/performance rankings |
| `pcb_surface_finish_guide.md` | `source_backed_fact_layer_partial` | finish-selection workflow and comparison taxonomy | cost matrices, finish numerics, lifecycle economics, supplier superiority |
| `pcb-copper-foil.md` | `completed_at_claim_family_level` | copper-foil topic taxonomy and high-frequency/heavy-copper question inventory | foil-type values, roughness/performance data, treatment claims |
| `pcb-insulation.md` | `completed_at_claim_family_level` | insulation topic taxonomy and testing/design section shape | insulation-property values, safety margins, validation criteria |
| `peelable-mask-pcb.md` | `completed_at_claim_family_level` | peelable-mask use-case and process-integration topic intent | material compatibility specifics, design-rule values, QC criteria |
| `epoxy-pcb.md` | `completed_at_claim_family_level` | epoxy-family topic intent and manufacturing/assembly section shape | generic epoxy property claims, certifications, logistics/support proof |
| `waterproof-pcb.md` | `source_backed_fact_layer_partial` | coating/potting workflow framing and waterproofing topic taxonomy | IP-rating claims, lifespan claims, rework impact claims, test-standard claims |

## Official-Source Gaps

- LTCC official class/source layer sufficient for reusable fact work
- Surface-finish chemistry anchors beyond current selection posture for `HASL`, `lead-free HASL`, `OSP`, `ENIG`, `ENEPIG`, `immersion silver`, and generic `immersion gold`
- Product-level Taconic official datasheets for any exact-grade claims
- Product-level or class-level support for generic `epoxy PCB` claims that are currently too broad to reuse safely
- Official or dated internal anchors for copper-foil parameter claims
- Official or standards-backed anchors for generic insulation property and test-threshold claims
- Official process/material anchors for peelable-mask specifics
- Official waterproof/coating sources sufficient for IP-rating, lifetime, or test-standard language tied to finished boards
- Stronger class-level or product-level support if `thermally-conductive PCB` or `LTCC` articles need more than topic-intent inventory

## Completion Status

- Lane status: `source_backed_fact_layer_partial`
- Batch status for `/code/blogs/tmps/2025.7.23/en`: `source_backed_fact_layer_partial`
- Intake status by weaker sub-branches:
  - `ltcc-pcb.md`: `completed_at_claim_family_level`
  - `thermally-conductive-pcb.md`: `completed_at_claim_family_level`
  - `taconic-pcb.md`: `completed_at_claim_family_level`
  - `hasl-pcb.md`: `completed_at_claim_family_level`
  - `lead-free-hasl-pcb.md`: `completed_at_claim_family_level`
  - `osp-pcb.md`: `completed_at_claim_family_level`
  - `immersion-gold-pcb.md`: `completed_at_claim_family_level`
  - `pcb-copper-foil.md`: `completed_at_claim_family_level`
  - `pcb-insulation.md`: `completed_at_claim_family_level`
  - `peelable-mask-pcb.md`: `completed_at_claim_family_level`
  - `epoxy-pcb.md`: `completed_at_claim_family_level`

No tracker, registry, fact, or wiki updates were made in this lane.
