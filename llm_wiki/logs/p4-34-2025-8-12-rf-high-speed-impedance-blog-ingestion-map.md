# P4-34 2025.8.12 RF High-Speed Impedance Blog Ingestion Map

Date: 2026-04-28

## Purpose

Create a deletion-safe ingestion map for the RF / high-speed / impedance lane inside `/code/blogs/tmps/2025.8.12/en`.

Treat all `tmps` drafts in this directory as claim inventory only, not as authority.

This log records:

- purpose and date
- file list for the assigned lane
- title and topic / heading inventory
- existing `llm_wiki` support found by targeted search
- per-draft disposition
- safe reuse classes
- blocked claim classes
- official-source gaps
- completion status using standard labels

## Input Directory

- `/code/blogs/tmps/2025.8.12/en`

## Lane Boundary

This lane covers the RF / high-speed / impedance draft family only.

Included in this log:

- `100-ohm-impedance-pcb.md`
- `50-ohm-impedance-pcb.md`
- `characteristic-impedance-pcb.md`
- `choosing-high-frequency-pcb-manufacturer.md`
- `common-issues-high-frequency-pcbs.md`
- `controlled-impedance-pcb.md`
- `differential-impedance-pcb.md`
- `hf-pcb.md`
- `high-frequency-pcb-antenna-design.md`
- `high-frequency-pcb-design.md`
- `high-frequency-pcb-impedance-control.md`
- `high-frequency-pcb-layer-stackup.md`
- `high-frequency-pcb-manufacturing.md`
- `high-frequency-pcb-materials.md`
- `high-frequency-pcb-power-design.md`
- `high-frequency-pcb-signal-integrity.md`
- `high-frequency-pcb-testing-methods.md`
- `impedance-control-pcb.md`
- `microwave-applications-high-frequency-pcbs.md`
- `tdr-testing-pcb.md`
- `what-is-hf-pcb.md`

Out of lane and not dispositioned here:

- display, HMI, automation, sensor, industrial-control, quote, compliance-only, and other non-RF topic drafts in the same directory

## File List

- `/code/blogs/tmps/2025.8.12/en/100-ohm-impedance-pcb.md`
- `/code/blogs/tmps/2025.8.12/en/50-ohm-impedance-pcb.md`
- `/code/blogs/tmps/2025.8.12/en/characteristic-impedance-pcb.md`
- `/code/blogs/tmps/2025.8.12/en/choosing-high-frequency-pcb-manufacturer.md`
- `/code/blogs/tmps/2025.8.12/en/common-issues-high-frequency-pcbs.md`
- `/code/blogs/tmps/2025.8.12/en/controlled-impedance-pcb.md`
- `/code/blogs/tmps/2025.8.12/en/differential-impedance-pcb.md`
- `/code/blogs/tmps/2025.8.12/en/hf-pcb.md`
- `/code/blogs/tmps/2025.8.12/en/high-frequency-pcb-antenna-design.md`
- `/code/blogs/tmps/2025.8.12/en/high-frequency-pcb-design.md`
- `/code/blogs/tmps/2025.8.12/en/high-frequency-pcb-impedance-control.md`
- `/code/blogs/tmps/2025.8.12/en/high-frequency-pcb-layer-stackup.md`
- `/code/blogs/tmps/2025.8.12/en/high-frequency-pcb-manufacturing.md`
- `/code/blogs/tmps/2025.8.12/en/high-frequency-pcb-materials.md`
- `/code/blogs/tmps/2025.8.12/en/high-frequency-pcb-power-design.md`
- `/code/blogs/tmps/2025.8.12/en/high-frequency-pcb-signal-integrity.md`
- `/code/blogs/tmps/2025.8.12/en/high-frequency-pcb-testing-methods.md`
- `/code/blogs/tmps/2025.8.12/en/impedance-control-pcb.md`
- `/code/blogs/tmps/2025.8.12/en/microwave-applications-high-frequency-pcbs.md`
- `/code/blogs/tmps/2025.8.12/en/tdr-testing-pcb.md`
- `/code/blogs/tmps/2025.8.12/en/what-is-hf-pcb.md`

## Title And Topic Inventory

| Draft | Title | Topic summary |
| --- | --- | --- |
| `100-ohm-impedance-pcb.md` | `100-Ohm Impedance PCB Manufacturing: The Critical Factor in High-Speed Differential Signaling` | differential-impedance framing, material selection, validation, pitfalls, supplier CTA |
| `50-ohm-impedance-pcb.md` | `50-Ohm Impedance PCB Manufacturing: Professional Solutions for RF and High-Speed Applications` | 50-ohm RF framing, signal integrity, cost / time-to-market, specialized RF applications, supplier CTA |
| `characteristic-impedance-pcb.md` | `Characteristic Impedance PCB Manufacturing and Integration for Advanced Electronic Systems` | transmission-line framing, manufacturing, signal optimization, application segments, test / validation |
| `choosing-high-frequency-pcb-manufacturer.md` | `Choosing a High-frequency PCB Manufacturer: Essential Selection Criteria and Evaluation Guide` | vendor evaluation, processing expertise, impedance precision, certifications, technical review, sourcing, lead time |
| `common-issues-high-frequency-pcbs.md` | `Common Issues in High-frequency PCBs: Troubleshooting Guide` | failure modes, attenuation, mismatch, EMI, process defects, environmental failures, crosstalk, vias, troubleshooting |
| `controlled-impedance-pcb.md` | `Controlled Impedance PCB: Manufacturing Excellence for Mission-Critical Applications` | process control, aerospace / defense, medical, telecom, data center, validation |
| `differential-impedance-pcb.md` | `Impedance Control PCB: Precision Engineering for High-Speed Electronics` | physics, manufacturing, high-speed digital, RF / microwave, test / validation |
| `hf-pcb.md` | `High-Frequency PCB (HF PCB): Complete Technical Guide` | umbrella hub draft covering materials, stackup, design, impedance, power, SI, manufacturing, testing, antenna, microwave, vendor selection, standards |
| `high-frequency-pcb-antenna-design.md` | `High-frequency PCB Antenna Design: Advanced Techniques for Wireless Applications` | antenna types, RF design method, simulation, mmWave integration, OTA / VNA / chamber testing |
| `high-frequency-pcb-design.md` | `High-frequency PCB Design: Key Principles for RF/Microwave Circuits` | transmission lines, stackup, SI, PDN, EMI, mmWave, simulation, DFM / testability |
| `high-frequency-pcb-impedance-control.md` | `High-frequency PCB Impedance Control: Essential Guide for RF and High-Speed Design` | impedance calculation, stackup, material stability, discontinuities, TDR / VNA, application-specific impedance |
| `high-frequency-pcb-layer-stackup.md` | `High-frequency PCB Layer Stackup: Optimizing Signal Integrity and Performance` | substrate selection, 4-layer / 8-layer / mmWave stackups, impedance planning, plane strategy, EMI |
| `high-frequency-pcb-manufacturing.md` | `High-frequency PCB Manufacturing: Advanced RF/Microwave Techniques` | PTFE handling, lamination, drilling, metallization, impedance control, metrology, environmental compliance |
| `high-frequency-pcb-materials.md` | `High-frequency PCB Materials: Advanced Substrate Selection for RF/Microwave Applications` | Dk / Df framing, PTFE / ceramic / thermoset / LCP, frequency-band routing, process compatibility, reliability, cost-performance |
| `high-frequency-pcb-power-design.md` | `High-frequency PCB Power Design: Advanced PDN Solutions for RF and High-Speed Systems` | PDN architecture, decoupling, noise, isolation, ground strategy, thermal considerations |
| `high-frequency-pcb-signal-integrity.md` | `High-frequency PCB Signal Integrity: Complete Design and Analysis Guide` | SI fundamentals, eye / time / frequency domain, crosstalk, reflections, jitter, stackup, vias, PI interplay, verification |
| `high-frequency-pcb-testing-methods.md` | `High-frequency PCB Testing Methods: Complete Validation Guide for RF and Microwave Circuits` | TDR, S-parameters, production testing, SPC / yield, mmWave, OTA, environmental tests, sector-specific validation |
| `impedance-control-pcb.md` | `Impedance Control PCB: Precision Engineering for High-Speed Electronics` | impedance physics, manufacturing techniques, high-speed and RF use cases, supplier capability framing |
| `microwave-applications-high-frequency-pcbs.md` | `Microwave Applications of High-frequency PCBs: From 5G to Satellite Communications` | telecom, radar, satcom, defense, 6G, transmission lines, grounding / shielding, supplier CTA |
| `tdr-testing-pcb.md` | `TDR Testing PCB: Advanced Quality Control for Mission-Critical Electronics` | TDR basics, process integration, applications, specialized testing, supplier capability framing |
| `what-is-hf-pcb.md` | `What is HF PCB: Complete Guide to High-Frequency Circuit Board Technology` | definition, key characteristics, material families, applications, design considerations, supplier CTA |

## Existing `llm_wiki` Support Found By Targeted Search

Targeted search across `/code/blogs/llm_wiki`, `/code/blogs/docs`, and `/code/blogs/prompts_template` found meaningful existing support, but mostly at boundary / method / workflow level rather than article-ready fact completeness for every draft.

Strongest support already present:

- `wiki/testing/rf-validation-and-test-coverage.md`
  - layered RF validation model separating coupons, TDR, VNA, and routine fabrication checks
- `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`
  - separates electrical screening from signal-integrity proof
- `facts/methods/rf-validation-capability.md`
  - guarded internal RF validation posture centered on coupons, TDR, VNA, and traceability
- `facts/methods/controlled-impedance-tdr-verification-posture.md`
  - controlled-impedance targets linked to measurement / verification, not just nominal design intent
- `facts/methods/parameter-scope-public-capability-impedance-and-validation.md`
  - public-site impedance / TDR / VNA claims are already fenced as capability-claim context only
- `facts/methods/parameter-scope-test-inspection-high-speed-si-measurement-dimensions.md`
  - guarded vocabulary for TDR, VNA, target-ohm families, and SI measurement scope
- `facts/methods/spread-glass-and-controlled-impedance-planning.md`
  - material / glass / copper / stackup / coupon planning linkage for high-speed work
- `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
  - reusable stackup and manufacturability governance for high-speed / RF builds
- `wiki/processes/public-capability-parameter-consumption-map.md`
  - fences public capability numbers and keeps them out of generalized fact writing
- `wiki/materials/internal-material-family-coverage-and-refresh-rules.md`
  - shows existing material-family coverage and refresh rules

Relevant internal source coverage already registered:

- `sources/registry/internal/frontendhil-high-frequency-product-page-en.md`
- `sources/registry/internal/frontendhil-high-speed-product-page-en.md`
- `sources/registry/internal/frontendhil-teflon-pcb-product-page-en.md`
- `sources/registry/internal/frontendapt-high-frequency-pcb-page-en.md`
- `sources/registry/internal/frontendapt-pcb-pcb-impedance-control-page-en.md`
- `sources/registry/internal/frontendapt-materials-controlled-impedance-stackups-page-en.md`
- `sources/registry/internal/frontendapt-microwave-pcb-page-en.md`
- `sources/registry/internal/frontendapt-pcb-quality-page-en.md`

Relevant source-backed materials layer already present:

- official RF / microwave laminate rows across Rogers, AGC, Shengyi, Ventec, Isola, Panasonic, and related families
- existing material cards already block over-promotion from laminate properties to finished-board RF, antenna, radar, or protocol performance

Coverage summary for this lane:

- strongest existing support:
  - RF validation structure
  - controlled-impedance verification posture
  - stackup / materials planning boundaries
  - public capability claim containment
  - high-frequency material-family routing
- partial existing support:
  - antenna-design workflow language
  - microwave-application context
  - high-speed SI review dimensions
  - PTFE / hybrid RF manufacturing posture
- weak or missing support:
  - authoritative general-purpose explainer pages for `50-ohm`, `100-ohm`, `characteristic impedance`, and `what is HF PCB`
  - official neutral-source anchors for OTA / chamber testing, sector-specific validation, and supplier-selection criteria
  - supplier-specific certification, lead-time, yield, capacity, and application-readiness proof for HILPCB

## Per-Draft Disposition

| Draft | Current support | Safe reuse now | Blocked claim families | Status |
| --- | --- | --- | --- | --- |
| `100-ohm-impedance-pcb.md` | partial | differential-pair topic intent, impedance-as-measured-workflow framing, validation / pitfalls outline | exact `100-ohm` geometry defaults, DDR / USB application-readiness, material rankings, tolerance numbers, HIL capability proof | `source_backed_fact_layer_partial` |
| `50-ohm-impedance-pcb.md` | partial | RF transmission-line topic intent, 50-ohm family as common RF target context, SI / validation outline | universal 50-ohm optimization claims, RF-market numbers, cost / schedule claims, HIL capability, application success claims | `source_backed_fact_layer_partial` |
| `characteristic-impedance-pcb.md` | partial | terminology, transmission-line topic routing, validation and material-selection outline | `25 to 600 ohms` range claims, broad application coverage, process-window claims, capability claims | `source_backed_fact_layer_partial` |
| `choosing-high-frequency-pcb-manufacturer.md` | weak | evaluation-question inventory only, topic clustering around materials / validation / sourcing review | certifications, qualifications, capacity, lead times, inventory, process precision, equipment, HIL superiority | `completed_at_claim_family_level` |
| `common-issues-high-frequency-pcbs.md` | partial | failure-mode taxonomy, troubleshooting topic map, mismatch / crosstalk / via / moisture issue buckets | root-cause rates, proven fixes, environment limits, failure probability, supplier troubleshooting capability | `source_backed_fact_layer_partial` |
| `controlled-impedance-pcb.md` | partial | controlled-impedance workflow positioning, application-category outline, validation separation | aerospace / defense / medical readiness, long-life stability proof, manufacturing-standard claims, HIL quality claims | `source_backed_fact_layer_partial` |
| `differential-impedance-pcb.md` | partial | high-speed differential topic intent, RF / high-speed split, validation outline | `±5 ohm` claims, compliance-pass claims, specific industry readiness, HIL capability proof | `source_backed_fact_layer_partial` |
| `hf-pcb.md` | partial | hub / taxonomy structure linking materials, stackup, SI, testing, antenna, microwave applications | frequency-range numerics, standards / certification claims, case studies, future-trend certainty, HIL capability proof | `source_backed_fact_layer_partial` |
| `high-frequency-pcb-antenna-design.md` | weak | antenna-topic taxonomy, simulation / manufacturing / validation section inventory | OTA outcomes, chamber capability, antenna gain / efficiency, AiP / SIW manufacturability, HIL antenna expertise claims | `completed_at_claim_family_level` |
| `high-frequency-pcb-design.md` | partial | design-topic taxonomy, stackup / grounding / via / EMI / simulation section structure | trace / via formulas, mmWave performance claims, compliance outcomes, DFM limits, HIL design-services proof | `source_backed_fact_layer_partial` |
| `high-frequency-pcb-impedance-control.md` | partial | impedance-planning workflow, TDR / VNA topic routing, problem / solution buckets | calculation formulas, tolerance guarantees, application-specific target tables, cost optimization claims | `source_backed_fact_layer_partial` |
| `high-frequency-pcb-layer-stackup.md` | partial | stackup-planning topic inventory, application-specific stackup buckets, impedance and plane strategy framing | 4-layer / 8-layer / mmWave default stackups, exact dimensions, layer-order prescriptions, EMI outcome claims | `source_backed_fact_layer_partial` |
| `high-frequency-pcb-manufacturing.md` | partial | PTFE / hybrid-material process-topic routing, drilling / metallization / metrology section inventory | process superiority, advanced-equipment proof, live monitoring claims, environmental-compliance proof, HIL capability proof | `source_backed_fact_layer_partial` |
| `high-frequency-pcb-materials.md` | partial | material-family routing, PTFE / ceramic / LCP / thermoset topic buckets, reliability-question inventory | draft-originated Dk / Df / moisture / thermal values, band-by-band prescriptions, cost-performance rankings, standardization claims | `source_backed_fact_layer_partial` |
| `high-frequency-pcb-power-design.md` | weak | PDN / decoupling / isolation / thermal topic inventory only | thermal-resistance calculations, noise-suppression effectiveness, power-plane prescriptions, HIL design proof | `completed_at_claim_family_level` |
| `high-frequency-pcb-signal-integrity.md` | partial | SI topic taxonomy, reflections / crosstalk / jitter / PI interplay buckets, pre/post-layout verification outline | eye-mask claims, jitter thresholds, guaranteed SI improvements, tool-correlation claims, HIL SI capability proof | `source_backed_fact_layer_partial` |
| `high-frequency-pcb-testing-methods.md` | partial | TDR / S-parameter / mmWave / environmental validation topic map, production-versus-lab test separation | OTA methods, SPC / yield claims, radar / aerospace readiness, environmental thresholds, HIL testing capability proof | `source_backed_fact_layer_partial` |
| `impedance-control-pcb.md` | partial | controlled-impedance topic routing, manufacturing / application / validation outline | tolerance numbers, manufacturing-technique effectiveness claims, HIL core capability claims | `source_backed_fact_layer_partial` |
| `microwave-applications-high-frequency-pcbs.md` | partial | application taxonomy for telecom / radar / satcom / defense, transmission-line and grounding topic routing | `77 GHz`, phased-array, EW, LEO, HTS, 6G, wireless-power readiness claims without source-specific grounding; HIL expertise claims | `source_backed_fact_layer_partial` |
| `tdr-testing-pcb.md` | partial | TDR as impedance / discontinuity / validation vocabulary, process-integration outline | defect-detection certainty, technical capability depth, mission-critical proof, HIL testing-stack claims | `source_backed_fact_layer_partial` |
| `what-is-hf-pcb.md` | partial | explainer intent, material-family routing, application taxonomy, design-question inventory | frequency-range definitions, universal HF criteria, material-performance claims, HIL-fit claims | `source_backed_fact_layer_partial` |

## Safe Reuse Classes

- terminology
  - high-frequency PCB
  - RF / microwave PCB
  - controlled impedance
  - characteristic impedance
  - differential pair
  - TDR
  - VNA
  - stackup
  - signal integrity
  - PTFE / hybrid RF material families
- topic / outline reuse
  - H2 / H3 article shape
  - explainer versus troubleshooting versus validation versus manufacturing topic grouping
  - application taxonomy for telecom, radar, satellite, backplane, and mixed-signal contexts
- workflow framing
  - impedance belongs to stackup + coupon + measurement workflow
  - TDR / VNA are distinct from AOI / e-test / generic QA
  - material choice, stackup, SI, and validation should be described as coupled decisions
- guarded material routing
  - reuse existing official material cards when discussing named laminate families
  - keep laminate properties separate from finished-board performance proof
- non-promotional reuse
  - FAQ / question inventory
  - engineering decision categories
  - problem / risk / mitigation bucket names

## Blocked Claim Classes

- draft-originated numerics
  - impedance tolerances
  - ohm-target geometry defaults
  - frequency ranges
  - Dk / Df / thermal / moisture / attenuation values
  - TDR edge times, VNA frequency ceilings, jitter figures, eye metrics, yield or SPC numbers
- supplier capability claims
  - HILPCB process precision
  - equipment stack
  - monitoring depth
  - advanced manufacturing superiority
  - antenna / SI / RF design-service competence
  - capacity, lead time, scalability, sourcing strength
- certification / compliance / qualification claims
  - aerospace, defense, medical, telecom, automotive, radar, OTA, military, IPC, ISO, customer-approval, or qualification readiness
- application-readiness claims
  - 5G, radar, satellite, mmWave, DDR, USB, AI server, or microwave success proof
  - compliance-pass, interoperability-pass, field-life, or product-level readiness claims
- commercial claims
  - price
  - MOQ
  - cost optimization
  - time-to-market acceleration
  - delivery speed
  - quality-rate or yield-rate superiority
- generalization risks
  - turning a material datasheet into board-level performance proof
  - turning public capability pages into universal process facts
  - turning draft troubleshooting advice into validated root-cause / fix certainty

## Official-Source Gaps

- neutral explainer anchors
  - authoritative or standards-adjacent sources for general `characteristic impedance`, `50-ohm`, `100-ohm`, and `HF PCB` explanatory writing
- antenna and OTA test coverage
  - neutral official sources for chamber, OTA, and antenna-validation method framing
- microwave / application-domain framing
  - stronger official sources for radar, satellite, defense, and mmWave application context before publishing application-specific advice
- vendor-selection / certifications / capability evaluation
  - neutral official sources or dated capability records for manufacturer-selection criteria, certifications, and production-capacity claims
- power-integrity and SI explainer layer
  - neutral official anchors for PDN, jitter, eye-diagram, and SI interpretation language if these topics are to move beyond inventory level
- supplier-specific capability proof
  - dated HIL capability records would be required before any actual factory claim about tolerance, TDR coverage, VNA scope, stackup precision, RF testing depth, lead time, or qualification support

## Prompt-Consumption Gate

Before writing from this lane:

1. Route impedance, TDR, VNA, and SI wording through the existing method / testing boundary cards.
2. Route RF material statements through existing official material fact cards only.
3. Keep `50-ohm`, `100-ohm`, `characteristic impedance`, and `HF PCB` drafts at explainer / intent level until stronger neutral source anchors are added.
4. Keep antenna, OTA, radar, satcom, defense, and mmWave application statements conservative unless supported by official source records.
5. Do not convert public-site capability numbers into reusable facts without explicit capability-claim fencing.
6. Stop before any HILPCB-specific capability, certification, pricing, yield, lead-time, or application-readiness claim unless backed by dated internal records.

## Completion Status

- lane scope: `/code/blogs/tmps/2025.8.12/en`
- assigned sub-lane: `rf-high-speed-impedance`
- deletion-safe map created: yes
- draft inventory completed: yes
- existing `llm_wiki` support cross-checked: yes
- new source records created: no
- new facts created: no
- new wiki pages created: no
- tracker files updated: no

Status labels:

- overall lane status: `completed_at_claim_family_level`
- existing source-backed support level across the lane: `source_backed_fact_layer_partial`
- drafts still at claim-family-only level:
  - `choosing-high-frequency-pcb-manufacturer.md`
  - `high-frequency-pcb-antenna-design.md`
  - `high-frequency-pcb-power-design.md`
- blocked topics requiring official-source recovery before stronger reuse:
  - neutral impedance explainer layer
  - antenna / OTA method layer
  - microwave application-domain layer
  - manufacturer-selection / certification / capability-evaluation layer
  - supplier-specific HIL capability proof

Boundary note:

This log preserves the batch as deletion-safe claim inventory for the assigned lane only. It does not promote draft-originated numbers, process limits, capability claims, certifications, lead times, prices, MOQs, yields, quality rates, application-readiness claims, or supplier claims into reusable facts.
