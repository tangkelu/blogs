# P4-31 APTPCB260401 2-Layer Blog Ingestion Map

Date: 2026-04-28

## Purpose

This map audits the 27 English `2-layer PCB` drafts under `/code/blogs/tmps/APTPCB260401/en` and defines how the batch may be consumed by `llm_wiki`.

The batch is useful as a topic-intent, outline-shape, and blocked-claim inventory for 2-layer PCB articles. It is not a primary source for material properties, thermal resistance, impedance geometry, surface-finish chemistry, DFM tolerances, supplier capability, price, lead time, certification, yield, or production readiness.

## Existing Coverage Check

No existing `llm_wiki` absorption record was found for `APTPCB260401`, `APTPCB260401/en`, or related `260401` naming before this pass.

## Target Drafts

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

## Baseline Finding

Current `llm_wiki` already has broad adjacent support for this batch:

- FR-4 and high-Tg FR-4 official-source coverage through Isola, ITEQ, Shengyi, and related material cards
- Rogers RO3000 / RO4000 / RT/duroid / TMM source-backed material cards and selector pages
- PTFE / RF processing posture and hybrid RF stackup boundaries
- ceramic / alumina / AlN class-level official anchors
- flex / polyimide / LCP material-class coverage with narrow exact-product exceptions
- IMS / MCPCB and thermal-platform posture with Ventec and internal source support
- surface-finish selection posture plus IPC finish-standard metadata
- PCBA assembly flow, inspection stack, NPI, FAI/FQI, and prototype / quick-turn / mass-production routing boundaries
- RF validation, controlled impedance, high-speed context, and mmWave / antenna claim boundaries

Current `llm_wiki` still does not authorize the following from this draft batch:

- 2-layer universal design-rule tables or fixed stackup defaults
- trace width, current capacity, annular ring, drill, tolerance, impedance, or return-path numeric rules copied from drafts
- thermal-resistance calculations, LED thermal outcomes, DBC / thick-film / ceramic process values, or metal-core performance claims
- surface-finish shelf-life, thickness, black-pad, HASL planarity, OSP risk, or ENIG / ENEPIG chemistry claims beyond existing sourced boundaries
- quick-turn windows, price, MOQ, quote logic, supplier audit answers, equipment proof, yield, or production-scale promises
- application qualification claims for automotive, medical, aerospace, defense, satellite, 5G, drone, or industrial sectors

## Disposition Contract

Use these dispositions for the batch:

- `already_supported_by_existing_layer`: topic can be discussed through existing `llm_wiki` source-backed cards, not through draft prose.
- `topic_inventory_only`: draft headings and reader questions are useful for rewrite prompts, query clustering, and evidence-pack planning.
- `needs_product_datasheet`: material-property, laminate, ceramic, IMS, polyimide, PTFE, or Rogers numeric claims require official product-level source support.
- `needs_dated_capability_record`: APTPCB capability, lead time, yield, inspection coverage, process limit, volume readiness, or commercial claims require a scoped dated capability record.
- `draft_only_blocked`: draft numeric tables, formulas, examples, supplier claims, DFM thresholds, price / lead-time claims, and qualification claims must not enter reusable facts.

## Per-Draft Coverage Table

| Draft | Current status | Safe reuse | Blocked / rejected content |
| --- | --- | --- | --- |
| `2-layer-aluminum-pcb.md` | `partial_existing_layer` | MCPCB / IMS topic intent, LED and power-thermal context, order-spec checklist shape | thermal-resistance calculations, dielectric numeric ladders, LED thermal outcomes, aluminum material capability, assembly profile claims |
| `2-layer-ceramic-pcb.md` | `class_context_only` | ceramic, alumina, AlN, DBC, thick-film topic clustering | alumina-vs-AlN numeric comparisons, DBC / thick-film process values, RF performance, cost and lead-time claims |
| `2-layer-copper-core-pcb.md` | `topic_inventory_only` | copper-core vs aluminum-core comparison need, heavy-copper / embedded-copper topic intent | copper-core performance, defense suitability, heavy-copper values, cost / lead-time expectations, embedded-copper capability |
| `2-layer-enig-pcb.md` | `partial_existing_layer` | ENIG / fine-pitch / BGA / ENEPIG comparison topic intent | ENIG thickness, shelf life, black-pad prevention guarantees, medical suitability, universal fine-pitch claims |
| `2-layer-fr4-pcb.md` | `partial_existing_layer` | FR-4 family framing, high-Tg selection need, surface-finish and DFM section shape | universal FR-4 values, fixed thickness / stackup defaults, impedance feasibility as guarantee, DFM numeric tables |
| `2-layer-hasl-pcb.md` | `topic_inventory_only` | HASL process topic, cost-optimized / through-hole / keyboard context labels | HASL planarity, leaded-status handling, keyboard suitability, drilling claims, surface consistency proof |
| `2-layer-high-frequency-pcb.md` | `partial_existing_layer` | high-frequency material selection, return-path, RF validation, 5G / drone context inventory | FR-4 failure thresholds, link-budget claims, yield verification, frequency limits, application performance |
| `2-layer-high-tg-pcb.md` | `partial_existing_layer` | Tg selection topic, lead-free and automotive context as questions, high-Tg material examples if source-backed | Tg thresholds from draft, automotive-grade claims, reflow profiles, via reliability testing outcomes, cost claims |
| `2-layer-lead-free-hasl-pcb.md` | `compliance_context_only` | lead-free HASL, RoHS / EU-market topic intent | RoHS proof for a product, automotive mass-production suitability, volume economics, reflow windows, halogen-free proof |
| `2-layer-microwave-pcb.md` | `partial_existing_layer` | microwave / mmWave topic intent, material-selection and validation structure | Ka-band / satellite performance, cost values, thermal outcomes, 2-layer-vs-multilayer conclusions as universal rules |
| `2-layer-osp-pcb.md` | `topic_inventory_only` | OSP as surface-finish option and cost/risk topic | OSP chemistry claims, shelf life, mass-production economics, cost matrix, assembly risk ranking |
| `2-layer-pcb-assembly.md` | `partial_existing_layer` | SMT/THT/turnkey, stencil, BOM, inspection, double-sided assembly section intent | assembly yield, stencil numerics, pricing, exact inspection coverage, turnkey savings, process windows |
| `2-layer-pcb-board.md` | `topic_inventory_only` | stackup, copper distribution, via, ground pour, finish, drilling, panelization checklist shape | trace/current tables, drill/pad/annular-ring values, impedance rules, solder-mask/silkscreen constraints as universal limits |
| `2-layer-pcb-fabrication.md` | `topic_inventory_only` | fabrication sequence, DFM and application clusters such as keyboard, power, Arduino, IoT | lead-time fluctuation causes as proof, warpage solutions, isolation values, yield optimization numbers, hidden-defect promises |
| `2-layer-pcb-low-cost.md` | `draft_only_blocked` | cost-driver categories and DFC topic intent | price calculations, savings percentages, prototype/mass pricing, ultra-cheap risk claims, quote promises |
| `2-layer-pcb-manufacturer.md` | `draft_only_blocked` | manufacturer-audit question inventory | China-dominance claims, broker detection rules, equipment audit proof, supplier capability, quality/e-test standards claims |
| `2-layer-pcb-manufacturing.md` | `topic_inventory_only` | application clusters and DFM / panelization topic intent | dominance / market claims, DFM tolerances, volume cost optimization, automotive/opto qualification, manufacturing outcome claims |
| `2-layer-pcb-prototype.md` | `partial_existing_layer` | Gerber package, DFC, panelization, assembly-readiness, debug, NPI-to-volume topic intent | NRE delay rules, scrap savings, quote or schedule claims, prototype-to-scale guarantees |
| `2-layer-pcb-quick-turn.md` | `draft_only_blocked` | quick-turn blocker inventory and schedule-planning questions | 24-72 hour promises, fastest finish claims, time-zone effects as rule, rush impedance claims, quick-turn cost |
| `2-layer-pcb-supplier.md` | `draft_only_blocked` | supplier lifecycle, MOQ, VMI, PCBA alignment, counterfeit mitigation, QA agreement topic intent | MOQ / pricing optimization, VMI capability, RMA protocol claims, supplier status, lifecycle guarantees |
| `2-layer-pcb.md` | `partial_existing_layer` | 2-layer vs 4-layer decision framing, material / finish / assembly handoff topics | fixed stackup specs, EMC/SI rules, cost figures, DFM numeric rules, turnkey claims |
| `2-layer-polyimide-pcb.md` | `class_context_only` | polyimide rigid vs flex topic, Kapton / high-temperature / UAV context labels | Kapton properties from draft, bend rules, aerospace-grade claims, profiling parameters, high-temperature performance |
| `2-layer-printed-circuit-board.md` | `topic_inventory_only` | broad application taxonomy across industrial, power, robotics, medical, drone, consumer, IoT | sector qualification, medical / aerospace suitability, limit thresholds, application-performance outcomes |
| `2-layer-ptfe-pcb.md` | `partial_existing_layer` | PTFE material-family and processing-challenge topic intent | PTFE property values from draft, product-family comparisons, DFM rules, insertion-loss examples, defense and lead-time claims |
| `2-layer-rf-pcb.md` | `partial_existing_layer` | RF trace / ground / connector / shielding / validation topics | 50-ohm geometry rules, connector-launch prescriptions, shielding effectiveness, RF PCBA verification proof |
| `2-layer-rogers-pcb.md` | `already_supported_by_existing_layer` | Rogers material-selection and RF manufacturing topic intent if paired with official Rogers cards | core-thickness / 50-ohm rules, antenna / 5G constraints, Rogers processing costs, mass-production claims |
| `2-layer-teflon-pcb.md` | `partial_existing_layer` | Teflon / PTFE terminology, satellite / high-speed / supplier-qualification topic intent | Teflon dominance claims, brand comparison values, space-grade specs, supplier qualification proof, data-center performance |

## Claim-Family Rules

### Can Be Consumed Now

- 2-layer topic clustering: FR-4, high-Tg, aluminum, copper core, ceramic, polyimide, PTFE, Rogers, RF, microwave, surface finish, assembly, prototype, quick-turn, supplier, and low-cost themes
- outline structures and reader questions for future evidence-pack planning
- conservative process or material-family language only when it is pulled from existing source-backed `llm_wiki` cards
- blocked-claim inventories for future source recovery or dated capability-record planning

### Needs Official Source Or Dated Capability Record

- any numeric value from the drafts
- material properties for FR-4, high-Tg FR-4, Rogers, PTFE, Teflon, polyimide, Kapton, ceramic, alumina, AlN, aluminum IMS, copper core, OSP, HASL, lead-free HASL, ENIG, or ENEPIG
- design-rule, impedance, current-capacity, drill, annular-ring, tolerance, copper, dielectric, thickness, thermal-resistance, DBC, thick-film, or reflow-profile claims
- cost, price, savings, MOQ, lead time, quick-turn window, quote, inventory, VMI, yield, throughput, quality-rate, or production-scale claims
- supplier, audit, equipment, direct-factory, material-authenticity, stocking, or lifecycle-management claims
- automotive, medical, aerospace, defense, satellite, 5G, drone, industrial, RoHS, halogen-free, or other qualification / compliance claims

### Reject From Draft-To-Data Promotion

- universal `2-layer` design rules or stackup defaults
- formulas and worked examples that imply guaranteed impedance, thermal, cost, or RF outcomes
- APTPCB capability statements without bounded source and date
- application qualification statements based only on target market language
- surface-finish shelf-life, black-pad, planarity, solderability, and risk-ranking claims copied from draft prose

## Prompt-Consumption Gate

Before rewriting or generating from this batch:

1. Use this ingestion map to remove draft-originated numbers, price / lead-time language, and supplier proof.
2. Pull FR-4, Rogers, PTFE, ceramic, flex / polyimide, IMS / MCPCB, finish, PCBA, quick-turn, and RF-validation support from existing `llm_wiki` cards.
3. Keep `2-layer` articles qualitative unless exact product datasheets, official standards metadata, or dated APT capability records are attached.
4. If a target article needs cost, lead time, process limits, impedance geometry, thermal calculations, qualification, or supplier audit claims, stop and require a separate source lane.

## Candidate Future Source Needs

- official HASL / lead-free HASL / OSP / ENIG / ENEPIG chemistry or IPC finish-source supplementation if surface-finish articles need more than selection posture
- product-level ceramic, alumina, AlN, IMS, copper-core, aluminum-core, and polyimide datasheets if thermal or material-property comparisons are needed
- dated APT capability records for 2-layer quick-turn, low-cost, production, supplier, audit, and process-limit claims
- a 2-layer-specific evidence-pack bridge only after the claim boundary here is connected to `prompts_template`

## Completion Status

This batch is absorbed at claim-family disposition level.

No material numeric, 2-layer design-rule, surface-finish chemistry, thermal-performance, RF-performance, quick-turn, cost, supplier, qualification, or APT capability fact was created from temporary draft prose.
