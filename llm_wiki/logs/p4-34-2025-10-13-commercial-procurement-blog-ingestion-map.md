# P4-34 2025.10.13 Commercial Procurement Blog Ingestion Map

Date: 2026-04-28
Purpose: Create a deletion-safe ingestion map for `/code/blogs/tmps/2025.10.13/en` as claim-family inventory only. Temporary drafts are treated as demand input, not authority. This log does not promote draft-originated numeric, capability, certification, price, lead-time, MOQ, yield, throughput, stock, shipping, logistics, quality-rate, supplier-proof, or commercial claims into reusable facts.

## Input Files Inspected

Directory: `/code/blogs/tmps/2025.10.13/en`

- `black-fr4-pcb.md`
- `blue-fr4-pcb.md`
- `circuit-board-company.md`
- `circuit-board-design.md`
- `circuit-board-fabrication.md`
- `circuit-board-factory.md`
- `circuit-board-manufacture.md`
- `circuit-board-production.md`
- `circuit-board-prototyping.md`
- `circuit-board-supplier.md`
- `double-layer-fr4-pcb.md`
- `fr4-assembly.md`
- `fr4-board.md`
- `fr4-fabrication.md`
- `fr4-manufacturing.md`
- `fr4-pcb.md`
- `fr4-production.md`
- `fr4-prototyping.md`
- `fr4-substrate.md`
- `green-fr4-pcb.md`
- `multilayer-fr4-pcb.md`
- `pcb-circuit-board-assembly.md`
- `pcb-circuit-board-manufacturing.md`
- `pcb-cost.md`
- `pcb-delivery.md`
- `pcb-inventory.md`
- `pcb-lead-time.md`
- `pcb-logistics.md`
- `pcb-pricing.md`
- `pcb-procurement.md`
- `pcb-shipping.md`
- `pcb-sourcing.md`
- `pcb-supply-chain.md`
- `premium-fr4-pcb.md`
- `red-fr4-pcb.md`
- `single-layer-fr4-pcb.md`
- `white-fr4-pcb.md`
- `yellow-fr4-pcb.md`

## Heading And Topic Clusters

### Cluster A: Commercial / procurement / logistics / supplier selection

- `pcb-procurement.md`: supplier evaluation, negotiation, QC in procurement, strategic partnerships
- `pcb-sourcing.md`: sourcing role, supplier identification, capability evaluation, global sourcing risk
- `pcb-supply-chain.md`: supply-chain structure, demand planning, resilience, collaboration, visibility, cost/lead-time balance
- `pcb-pricing.md`: cost factors, quote inputs, cost-minimization framing
- `pcb-cost.md`: cost structure, cost drivers, cost-reduction strategy, total cost of ownership
- `pcb-lead-time.md`: production timeline, lead-time drivers, rush-service decisions, shortening timelines
- `pcb-delivery.md`: delivery timelines, carrier options, packaging, customs, receiving issues
- `pcb-shipping.md`: carrier choice, packaging, international shipping cost, documentation/compliance
- `pcb-logistics.md`: logistics system design, international logistics challenges, logistics cost reduction, technology
- `pcb-inventory.md`: stock level planning, storage/handling, tracking, obsolescence, lean/JIT, warehouse workflow
- `circuit-board-company.md`, `circuit-board-factory.md`, `circuit-board-supplier.md`: supplier/company/factory evaluation, certification framing, support, scalability

### Cluster B: General fabrication / production / service-route taxonomy

- `circuit-board-fabrication.md`: design-to-production framing, materials/layers, process flow, testing, prototype-to-production
- `circuit-board-manufacture.md`, `pcb-circuit-board-manufacturing.md`: manufacturing quality, service scope, application support, order flow, materials/finishes
- `circuit-board-production.md`: scale-up, automation, QC, SPC, traceability, scheduling, sustainability
- `circuit-board-prototyping.md`: prototyping role, service contents, turnaround, prototype-to-production transition
- `pcb-circuit-board-assembly.md`: quote inputs, cost drivers, BOM sourcing, testing/QA, logistics/support, quote comparison
- `circuit-board-design.md`: DFM, SI/PI, thermal/mechanical reliability, workflow/tooling

### Cluster C: FR-4 family / layer-count / substrate / assembly / fabrication

- `fr4-pcb.md`, `fr4-board.md`, `fr4-substrate.md`: FR-4 buying guide, material selection, stackup, product-fit framing
- `fr4-fabrication.md`, `fr4-manufacturing.md`, `fr4-production.md`: FR-4 fabrication/manufacturing capabilities, QA, quote/lead-time framing, factory-selection posture
- `fr4-assembly.md`, `fr4-prototyping.md`: assembly quote inputs, lead time, prototype routing, turnkey vs consigned, rapid service framing
- `single-layer-fr4-pcb.md`, `double-layer-fr4-pcb.md`, `multilayer-fr4-pcb.md`: layer-count architecture, DFM, stackup, cost/performance tradeoffs, HDI/backplane posture
- `premium-fr4-pcb.md`: premium/high-performance FR-4 positioning, process control, thermal/reliability, cost efficiency

### Cluster D: Colored solder-mask / visual-positioning FR-4 variants

- `black-fr4-pcb.md`, `blue-fr4-pcb.md`, `green-fr4-pcb.md`, `red-fr4-pcb.md`, `white-fr4-pcb.md`, `yellow-fr4-pcb.md`
- Common themes: color-based visual positioning, inspection contrast, application labels, process/QA framing, cost comparison, HILPCB capability positioning

## Existing `llm_wiki` Support Found

### Strongest support already present

- Commercial/service taxonomy and routing:
  - `logs/p4-33-lane-f-commercial-service-taxonomy.md`
  - `wiki/processes/pcb-service-routing-from-prototype-to-special-process.md`
  - `wiki/processes/prototype-vs-quick-turn-pcb-routing.md`
  - `facts/methods/pcb-prototype-quickturn-and-volume-routing.md`
  - `facts/methods/pcba-bom-sourcing-and-traceability-posture.md`
  - `facts/methods/pcba-fai-fqi-and-traceability-gates.md`
  - `facts/methods/pcba-mixed-technology-assembly-flow.md`
- FR-4 material-family boundaries and supported exact-product anchors:
  - `facts/materials/fr4-official-source-coverage.md`
  - `facts/materials/non-isola-fr4-to-very-low-loss-coverage.md`
  - `facts/materials/isola-fr408.md`
  - `facts/materials/isola-fr408hr.md`
  - `facts/materials/isola-fr4-high-tg-product-grade-fields.md`
  - `facts/materials/isola-fr4-to-low-loss-family-ladder.md`
  - `facts/materials/shengyi-s1000-2-vs-s1000-2m-high-tg-fr4-coverage.md`
  - `facts/materials/iteq-it-180a-high-tg-fr4-product-coverage.md`
- Fabrication / stackup / finish framing:
  - `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
  - `facts/methods/pcb-stackup-special-process-and-baseline-families.md`
  - `wiki/processes/finish-zoning-and-selective-multi-finish.md`
  - `facts/methods/selective-multi-finish-strategy.md`
  - `facts/methods/finish-zoning-by-assembly-sequence-and-storage-exposure.md`
  - `facts/standards/ipc-finish-standards-metadata.md`

### Coverage conclusion

Current `llm_wiki` support is adequate for:

- conservative buyer/service taxonomy
- prototype vs quick-turn vs volume route framing
- BOM sourcing and traceability posture
- generic mixed-technology assembly-flow vocabulary
- FR-4 as a family-level explainer with exact-product anchors for some named grades
- generic fabrication / stackup / finish-selection context

Current `llm_wiki` support is not adequate as reusable authority for:

- current commercial terms, price tables, quote benchmarks, MOQ, stock, lead-time windows, shipping timing, or logistics promises
- supplier/company/factory proof, rankings, qualification, active certification, scale, throughput, yield, or defect-rate claims
- color-specific solder-mask optical, thermal, LED, medical, industrial, safety, or performance claims
- draft-originated FR-4 stackup defaults, layer recipes, current-carry tables, tolerances, capability windows, or HDI readiness claims

## Per-Draft And Claim-Family Disposition

| Draft or family | Disposition | Safe reuse class | Blocked claim class |
| --- | --- | --- | --- |
| `pcb-procurement.md` | `completed_at_claim_family_level` | procurement workflow vocabulary, supplier-evaluation question framing | negotiated terms, best-price outcomes, supplier quality proof |
| `pcb-sourcing.md` | `completed_at_claim_family_level` | sourcing role, risk categories, supplier-review posture | supplier reliability rankings, production-capacity proof, global-sourcing advantage claims |
| `pcb-supply-chain.md` | `completed_at_claim_family_level` | resilience, planning, visibility, collaboration taxonomy | inventory optimization results, lead-time reduction claims, future-trend certainty |
| `pcb-pricing.md`, `pcb-cost.md` | `completed_at_claim_family_level` | cost-driver taxonomy, quote-input checklist, total-cost framing | price ranges, savings claims, benchmark tables, hidden-fee certainty |
| `pcb-lead-time.md` | `completed_at_claim_family_level` | timeline-stage vocabulary, rush-vs-standard decision framing | specific lead-time windows, rush-service promises, schedule certainty |
| `pcb-delivery.md`, `pcb-shipping.md`, `pcb-logistics.md` | `blocked_pending_official_source` | packaging and delivery topic taxonomy only | carrier recommendations as facts, customs/compliance specifics, transit-time claims, logistics cost claims |
| `pcb-inventory.md` | `completed_at_claim_family_level` | inventory-control terminology, storage/handling topic demand | stock strategy outcomes, JIT effectiveness claims, warehouse-performance metrics |
| `circuit-board-company.md`, `circuit-board-factory.md`, `circuit-board-supplier.md` | `completed_at_claim_family_level` | company/factory/supplier selection questions, documentation and communication framing | certifications-as-proof, scalable-capacity proof, support-quality proof, trusted-partner claims |
| `circuit-board-fabrication.md`, `circuit-board-manufacture.md`, `pcb-circuit-board-manufacturing.md` | `source_backed_fact_layer_partial` | generic fabrication flow, materials/layers framing, prototype-to-production route taxonomy | factory capability proof, multilayer/HDI/high-frequency readiness, testing coverage promises |
| `circuit-board-production.md` | `completed_at_claim_family_level` | scale-up and production-governance topic shape, SPC/traceability vocabulary | automation precision proof, consistency outcomes, sustainability claims, customer-choice proof |
| `circuit-board-prototyping.md` | `source_backed_fact_layer_partial` | prototype routing and transition-to-volume framing | rapid-turnaround promises, seamless transfer claims, service differentiators as proof |
| `pcb-circuit-board-assembly.md` | `source_backed_fact_layer_partial` | BOM sourcing, QA/test taxonomy, quote-comparison framing | cost-reduction outcomes, after-sales proof, component-loss/yield claims |
| `circuit-board-design.md` | `completed_at_claim_family_level` | DFM, SI/PI, thermal/reliability topic inventory | design-rule numbers, yield optimization outcomes, HILPCB design superiority claims |
| `fr4-pcb.md`, `fr4-board.md`, `fr4-substrate.md` | `source_backed_fact_layer_partial` | FR-4 family explainer, material-selection questions, exact-product-anchor routing | family-level property tables, stock claims, low-loss/high-performance promises, procurement claims |
| `fr4-fabrication.md`, `fr4-manufacturing.md`, `fr4-production.md` | `completed_at_claim_family_level` | FR-4 manufacturing/fabrication topic clustering, QA and process-control vocabulary | certifications-as-proof, China-manufacturer ranking, capability windows, stable-yield claims |
| `fr4-assembly.md`, `fr4-prototyping.md` | `completed_at_claim_family_level` | assembly quote-input taxonomy, turnkey-vs-consigned framing, prototype-route inventory | 48-hour or similar promises, current lead-time/service windows, component availability claims |
| `single-layer-fr4-pcb.md` | `completed_at_claim_family_level` | single-layer topology and manufacturing topic demand | typical capability tables, copper/thickness defaults, EMI/current/thermal performance claims |
| `double-layer-fr4-pcb.md` | `completed_at_claim_family_level` | double-layer design/manufacturing topic demand | trace width/spacing, via, ground-plane, and DFM rules as reusable defaults |
| `multilayer-fr4-pcb.md` | `completed_at_claim_family_level` | multilayer architecture, stackup-planning, HDI/backplane topic demand | stackup recipes, HDI necessity rules, RF/high-speed suitability, interconnect capability proof |
| `premium-fr4-pcb.md` | `completed_at_claim_family_level` | premium-FR4 positioning as demand signal, process-control vocabulary | premium-material superiority, thermal stability outcomes, reliability proof, HILPCB capability claims |
| `black-fr4-pcb.md`, `blue-fr4-pcb.md`, `green-fr4-pcb.md`, `red-fr4-pcb.md`, `white-fr4-pcb.md`, `yellow-fr4-pcb.md` | `blocked_pending_official_source` | color-variant demand inventory, visual/inspection/branding taxonomy only | color-specific optical, thermal, LED, medical, industrial, safety, process, or cost claims |

## Safe Reuse Classes

- buyer-intent taxonomy:
  `procurement`, `sourcing`, `quote`, `pricing inputs`, `cost drivers`, `lead-time planning`, `delivery`, `shipping`, `logistics`, `inventory`
- service-route taxonomy:
  `prototype`, `quick-turn`, `small batch`, `volume production`, `turnkey`, `consigned`, `fabrication`, `assembly`, `integration`
- supplier-evaluation framing without proof:
  documentation scope, traceability, communication flow, review discipline, escalation path
- FR-4 family framing with boundaries:
  FR-4 is a family, exact values must stay attached to exact product-grade sources
- fabrication and stackup topic framing:
  process flow, material/layer decision context, DFM vocabulary, finish-selection vocabulary
- color-variant articles as demand inventory only:
  visual identification, inspection-contrast topic demand, branding/application labels without technical proof

## Blocked Claim Classes

- dynamic commercial numerics:
  price, unit cost, total cost, savings percentages, MOQ, stock, lead-time windows, turnaround promises, shipping time
- supplier proof:
  trusted partner, stable capacity, factory scale, throughput, yield, quality rate, accepted-lot or approved-supplier implications
- certification and compliance proof:
  ISO/IATF/medical/industrial claims presented as active transferable evidence without source-backed records
- logistics and customs specifics:
  carrier performance, customs predictability, compliance completeness, delivery reliability, landed-cost certainty
- FR-4 technical defaults from draft prose:
  substrate values, stackup recipes, copper/current tables, tolerances, trace/space, drill/via, HDI, impedance, thermal, reliability outcomes
- color-specific technical and application claims:
  reflectivity, optical stability, thermal advantage, LED efficiency, medical suitability, safety recognition, inspection superiority
- HILPCB-specific capability and commercial claims:
  manufacturing capability, quote speed, support quality, cost advantage, rapid service, quality outcomes

## Official-Source Gaps

- no official commercial-governance layer for admissible price, quote, MOQ, stock, and lead-time language
- no official logistics / customs / carrier / packaging-compliance source pack for PCB-specific shipping and delivery pages
- no dated supplier-capability records for company/factory/supplier/manufacturer proof claims
- no official color-solder-mask source layer for color-specific optical, inspection, thermal, LED, or application-performance claims
- no exact-product official source pack for most draft FR-4 material claims beyond the current supported anchors
- no admissible source layer for stable single-layer, double-layer, or multilayer capability defaults tied to the supplier

## Suggested Source Recovery Lanes

- `lane-commercial-numerics-governance`
  define what current commercial language is allowed only with dated internal records
- `lane-logistics-delivery-compliance`
  gather official carrier, customs, trade, and packaging-compliance sources for shipping/delivery/logistics drafts
- `lane-supplier-dated-capability-records`
  recover dated non-blog evidence if supplier/company/factory/manufacturer proof is required
- `lane-fr4-exact-product-expansion`
  extend official FR-4 product-grade coverage before any new FR-4 property tables are written
- `lane-colored-solder-mask-official-sources`
  recover official solder-mask vendor materials or standards metadata before color-specific technical claims are reused
- `lane-layer-count-boundary-maps`
  create explicit boundary cards for single-, double-, and generic multilayer-FR4 drafts if future rewrite demand persists

## Completion Status

- batch status: `completed_at_claim_family_level`
- commercial/procurement/service family: `completed_at_claim_family_level`
- fabrication/prototyping/assembly route family: `source_backed_fact_layer_partial`
- FR-4 family routing: `source_backed_fact_layer_partial`
- logistics/shipping/delivery family: `blocked_pending_official_source`
- color-FR4 family: `blocked_pending_official_source`

This batch is deletion-safe as claim-family intake only. It is not fully learned. No reusable facts, source registry entries, wiki pages, or global trackers were updated because this lane was limited to the single output log path.

## Verification

- existing support checked with targeted `rg` across `/code/blogs/llm_wiki`, `/code/blogs/docs`, and `/code/blogs/prompts_template`
- standard status labels matched against `llm-wiki-workflow` reference
- scoped verification to run after write:
  - `rg -n "2025.10.13|completed_at_claim_family_level|blocked_pending_official_source|source_backed_fact_layer_partial" /code/blogs/llm_wiki/logs/p4-34-2025-10-13-commercial-procurement-blog-ingestion-map.md`
  - `git diff --check -- /code/blogs/llm_wiki/logs/p4-34-2025-10-13-commercial-procurement-blog-ingestion-map.md`
  - `git status --short -- /code/blogs/llm_wiki/logs/p4-34-2025-10-13-commercial-procurement-blog-ingestion-map.md`
