# P4-34 2025.7.22 Specialty Materials And Rogers Blog Ingestion Map

Date: 2026-04-28

## Purpose

This map audits the 10 English drafts under `/code/blogs/tmps/2025.7.22/en` and converts the batch into deletion-safe `llm_wiki` knowledge.

The batch is useful as a topic-intent inventory for Rogers / FR-4 material writing, edge plating, gold fingers, and specialty board concepts such as transparent, stretchable, and biodegradable PCBs. The drafts themselves are not authority for material values, fabrication windows, application readiness, supplier capability, Highleap capability, cost, lead time, quality, or sustainability claims.

## Target Drafts

- `biodegradable-pcb.md`
- `edge-plated-pcb.md`
- `fr4-materia.md`
- `gold-finger-pcb.md`
- `rogers-4003c-pcb.md`
- `rogers-4350b-pcb.md`
- `rogers-4350b.md`
- `rogers-pcb.md`
- `stretchable-pcb.md`
- `transparent-pcb.md`

## Heading Inventory

| Draft | Title / topic | Main section inventory |
| --- | --- | --- |
| `biodegradable-pcb.md` | biodegradable PCB design for sustainable electronics | definition, why biodegradable PCBs matter, applications, Highleap expertise, why choose |
| `edge-plated-pcb.md` | edge plated PCB design and manufacturing | edge plating definition, applications, Highleap expertise, why choose |
| `fr4-materia.md` | FR4 material application in PCB manufacturing | why FR4 is popular, specialized applications, Highleap high-performance solutions, why choose |
| `gold-finger-pcb.md` | gold finger PCB design and manufacturing | definition, manufacturing process, applications, why choose |
| `rogers-4003c-pcb.md` | Rogers 4003C PCB manufacturing | material characteristics, fabrication, impedance, stackup / vias, assembly, thermal, QC/testing, applications, cost strategy |
| `rogers-4350b-pcb.md` | Rogers 4350B PCB manufacturing for mmWave | material engineering, fabrication controls, impedance, stackup / vias, thermal / assembly, QA/testing, applications, supply chain / cost |
| `rogers-4350b.md` | Rogers 4350B PCB manufacturing | advantages, applications, specialized materials, design considerations, why choose |
| `rogers-pcb.md` | Rogers PCB manufacturing | difference versus other materials, applications, specialized materials, design considerations, why choose |
| `stretchable-pcb.md` | stretchable PCB design | definition, applications, why essential, Highleap expertise, why choose |
| `transparent-pcb.md` | transparent PCB design | definition, applications, Highleap expertise, why choose |

## Existing Coverage Check

This batch previously had only lane-level coverage in `logs/p4-33-lane-a-materials-pdf-and-draft-matching.md`, where `2025.7.22/en` was marked `completed_at_claim_family_level`.

Reusable `llm_wiki` support now available:

- Rogers material values and boundaries:
  - `facts/materials/rogers-ro4003c.md`
  - `facts/materials/rogers-ro4350b.md`
  - `facts/materials/rogers-ro4003c-vs-ro4350b-vs-ro3003.md`
  - `facts/materials/rogers-material-selector.md`
  - `facts/materials/parameter-scope-rogers-rf-laminate-values.md`
  - `wiki/materials/rf-material-selector-by-application-band.md`
- FR-4 family boundaries:
  - `facts/materials/fr4-official-source-coverage.md`
  - exact-product anchors such as Isola `FR408`, `FR408HR`, `370HR`, `IS410`, plus Ventec / Shengyi / Kingboard / ITEQ rows where product-specific facts exist
- RF / high-frequency process context:
  - `wiki/processes/hybrid-rf-stackup-strategy.md`
  - `wiki/processes/ptfe-processing-and-manufacturability.md`
  - `wiki/testing/rf-validation-and-test-coverage.md`
- Gold finger and finish zoning context:
  - `facts/methods/selective-multi-finish-strategy.md`
  - `facts/methods/surface-finish-selection-for-rf.md`
  - `wiki/processes/finish-zoning-and-selective-multi-finish.md`
- Edge-feature context:
  - internal PCB profiling / special PCB manufacturing source records mention edge plating, castellation, and gold fingers as manufacturing-route topics, but not as reusable numeric capability evidence.

Weak or absent support:

- transparent PCB material-property facts, optical clarity values, conductor transparency values, and process limits
- stretchable PCB substrate / conductor stack facts, stretch-cycle claims, bend / elongation limits, reliability data, and medical / wearable suitability
- biodegradable PCB material identity, degradation conditions, environmental claims, end-of-life handling, electrical reliability, soldering compatibility, and commercialization readiness
- edge-plating thickness, wrap geometry, continuity, sidewall quality, acceptance criteria, RF shielding effect, and fabricator capability
- hard-gold finger thickness, wear-cycle life, bevel angle, insertion durability, connector qualification, and plated-contact acceptance

## Per-Draft Disposition

| Draft | Current status | Safe reuse | Blocked / rejected from draft-to-data promotion |
| --- | --- | --- | --- |
| `rogers-4003c-pcb.md` | `source_backed_fact_layer_partial` | topic intent, Rogers RO4003C material discussion, FR-4-like processing contrast, hybrid stackup planning when rewritten from official Rogers cards | draft impedance formulas, stackup defaults, via rules, thermal management outcomes, SMT profile values, QC protocol claims, application success, cost optimization, Highleap capability |
| `rogers-4350b-pcb.md` | `source_backed_fact_layer_partial` | topic intent, Rogers RO4350B product positioning, process Dk / Df values with official conditions, RO4000 comparison language | mmWave readiness, impedance tolerance, layer stackup values, via architecture guarantees, thermal / power outcomes, QA/testing protocols, supply-chain or cost claims |
| `rogers-4350b.md` | `source_backed_fact_layer_partial` | outline shape, RO4350B advantages only where routed through official product / datasheet cards | broad application fit, Highleap manufacturing proof, design-rule numerics, comparative superiority, cost / lead-time claims |
| `rogers-pcb.md` | `source_backed_fact_layer_partial` | Rogers family topic map, material-selection questions, official Rogers selector routing | generic `Rogers PCB` values, universal RF performance, application qualification, supplier proof, process-control promises |
| `fr4-materia.md` | `source_backed_fact_layer_partial` | FR-4 as a material-family explainer, exact-product examples from existing official fact cards | universal FR-4 property tables, stock / suitability claims, Highleap high-performance capability, low-cost / fast-delivery / quality claims |
| `gold-finger-pcb.md` | `topic_inventory_with_partial_finish_routing` | definition-level topic intent, selective-finish / hard-gold finger zone framing, connector-contact planning questions | plating thickness, wear cycles, bevel geometry, contact resistance, durability guarantee, IPC acceptance, Highleap capability |
| `edge-plated-pcb.md` | `topic_inventory_only` | edge plating as a special edge-feature / interconnect / shielding topic label | edge metallization dimensions, wrap plating quality, continuity, RF shielding performance, sidewall acceptance, reliability, Highleap capability |
| `transparent-pcb.md` | `topic_inventory_only` | article topic demand, application taxonomy, source-gap signal | optical transparency, transparent conductor values, material availability, process compatibility, touch / display / optical readiness, Highleap capability |
| `stretchable-pcb.md` | `topic_inventory_only` | article topic demand, wearable / flexible-electronics taxonomy, source-gap signal | elongation, stretch cycles, fatigue life, medical suitability, substrate/conductor claims, reliability, Highleap capability |
| `biodegradable-pcb.md` | `topic_inventory_only` | article topic demand, sustainability vocabulary as a gap signal only | biodegradation time, compostability, environmental benefit, substrate identity, regulatory / medical / IoT suitability, production availability, Highleap capability |

## Safe Reuse Classes

- titles, H2/H3 outline shape, and article intent
- material family names when routed through existing source-backed cards
- Rogers `RO4003C` and `RO4350B` values only from official Rogers fact cards, preserving product, frequency, temperature, and method
- FR-4 family framing only with exact-product anchors for numeric values
- gold finger and finish-zone discussion only through the existing selective-finish / finish-zoning layer
- specialty topic taxonomy for future source recovery: transparent, stretchable, biodegradable, edge plating, and gold fingers

## Blocked Claim Classes

- any draft-originated material parameter, Dk / Df value, Tg, CTE, thermal conductivity, transparency, elongation, degradation, plating thickness, or wear-cycle value
- impedance geometry, stackup defaults, via rules, thermal models, SMT profiles, RF / mmWave / antenna / radar performance, and insertion-loss outcomes
- edge plating / gold finger manufacturing capability, acceptance criteria, plated-contact durability, sidewall quality, continuity, and connector qualification
- transparent / stretchable / biodegradable PCB manufacturability, application readiness, medical / wearable / sustainability proof, and material availability
- Highleap capability, equipment, quality system, inspection coverage, production scale, certification, supplier proof, cost, lead time, MOQ, yield, and delivery claims

## Source Gaps

- official edge-plating and gold-finger process / standards metadata, plus dated capability records if supplier-specific limits are needed
- official finish chemistry and hard-gold / edge-contact guidance before thickness or durability claims are reused
- transparent PCB material / conductor official sources, including optical and electrical properties under named conditions
- stretchable PCB substrate / conductor official sources and reliability data before wearable / medical claims are written
- biodegradable PCB material identity, degradation conditions, regulatory / environmental framing, and reliability sources
- dated Highleap capability records for any shop-specific execution, quality, cost, lead-time, or production-scale claim

## Prompt-Consumption Gate

Before writing from this batch:

1. For Rogers articles, use official Rogers fact cards and RF / stackup process wiki pages. Do not copy draft formulas or application-performance claims.
2. For FR-4 articles, treat FR-4 as a family and attach hard values only to exact product cards.
3. For gold finger content, route through finish-zoning / selective-finish cards and block thickness, wear, or acceptance claims unless a source lane is added.
4. For edge-plated PCB content, use only topic framing until official process evidence or dated capability records exist.
5. For transparent, stretchable, and biodegradable PCB content, treat the drafts as demand signals only. Recover official material / process sources before writing technical claims.
6. Stop before any Highleap-specific capability, commercial, certification, or quality claim unless a dated internal record exists.

## Completion Status

This batch is absorbed at `source_backed_fact_layer_partial` for Rogers / FR-4 routing and `completed_at_claim_family_level` for edge plating, gold finger, transparent, stretchable, and biodegradable PCB topics.

No new material values, process windows, plating values, sustainability claims, application-readiness claims, supplier capability claims, cost, lead time, yield, quality outcomes, or Highleap capability statements were created from temporary draft prose.
