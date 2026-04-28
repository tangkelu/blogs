# P4-34 2025.10.1 Commercial Service And Legal-Sensitive Blog Ingestion Map

Date: 2026-04-28

## Purpose

Create a deletion-safe ingestion map for `/code/blogs/tmps/2025.10.1/en`.

The drafts are treated as claim inventory only. This log preserves service taxonomy, article intent, route decisions, and source gaps after the temporary source files are removed. It does not promote draft-originated commercial numbers, supplier proof, legal conclusions, capability claims, certification claims, process windows, quality rates, lead times, MOQs, yields, or application-readiness claims into reusable `llm_wiki` facts.

## Input Directory

- `/code/blogs/tmps/2025.10.1/en`
- markdown file count: `28`

## File List

- `pcb-assembly.md`
- `pcb-cloning.md`
- `pcb-company.md`
- `pcb-consultation.md`
- `pcb-copying.md`
- `pcb-design.md`
- `pcb-development.md`
- `pcb-engineering.md`
- `pcb-fabrication.md`
- `pcb-factory.md`
- `pcb-inspection.md`
- `pcb-manufacturer.md`
- `pcb-manufacturing.md`
- `pcb-modification.md`
- `pcb-optimization.md`
- `pcb-production.md`
- `pcb-prototyping.md`
- `pcb-quote.md`
- `pcb-redesign.md`
- `pcb-repair.md`
- `pcb-replication.md`
- `pcb-reverse-engineering.md`
- `pcb-rework.md`
- `pcb-services.md`
- `pcb-solutions.md`
- `pcb-supplier.md`
- `pcb-testing.md`
- `pcb-upgrade.md`

## Topic Cluster Inventory

| Cluster | Drafts | Main intent captured | Risk level |
| --- | --- | --- | --- |
| service portfolio and routing | `pcb-services.md`, `pcb-solutions.md`, `pcb-assembly.md`, `pcb-fabrication.md`, `pcb-manufacturing.md` | describe fabrication, assembly, turnkey, prototyping, testing, and engineering-service paths | medium |
| supplier / factory / company selection | `pcb-company.md`, `pcb-factory.md`, `pcb-manufacturer.md`, `pcb-supplier.md` | buyer evaluation, technical capability, quality systems, business relationship framing | high |
| quote / cost / production scale | `pcb-quote.md`, `pcb-production.md`, `pcb-prototyping.md` | quote inputs, prototype-to-volume routing, production planning and scale-up | high |
| engineering and design support | `pcb-design.md`, `pcb-engineering.md`, `pcb-consultation.md`, `pcb-development.md`, `pcb-optimization.md` | DFM, SI, RF, thermal, PDN, NPI, review and troubleshooting article structures | medium to high |
| inspection and testing | `pcb-inspection.md`, `pcb-testing.md` | AOI, X-ray, FAI, microsection, flying probe, ICT, FCT, traceability sections | medium |
| repair / rework / change control | `pcb-repair.md`, `pcb-rework.md`, `pcb-modification.md`, `pcb-redesign.md`, `pcb-upgrade.md` | defect recovery, BGA/SMT rework, ECO, redesign, legacy upgrade, obsolescence handling | high |
| copying / cloning / replication / reverse engineering | `pcb-copying.md`, `pcb-cloning.md`, `pcb-replication.md`, `pcb-reverse-engineering.md` | spare-board, legacy, reproduction, deliverable, and reverse-engineering intent | very high |

## Existing `llm_wiki` Support Found

Existing support is strongest for process routing, PCBA quality gates, NPI flow, traceability vocabulary, prototype/quick-turn distinctions, and controlled rework boundaries.

- `wiki/processes/pcb-service-routing-from-prototype-to-special-process.md`
- `wiki/processes/prototype-vs-quick-turn-pcb-routing.md`
- `wiki/processes/pcba-npi-to-mass-production-flow.md`
- `wiki/testing/pcba-quality-gates-and-test-strategy.md`
- `facts/methods/pcb-prototype-quickturn-and-volume-routing.md`
- `facts/methods/pcba-bom-sourcing-and-traceability-posture.md`
- `facts/methods/pcba-fai-fqi-and-traceability-gates.md`
- `facts/methods/manual-solder-rework-boundary-for-mixed-technology.md`
- `facts/methods/2025-7-mixed-service-draft-consumption-boundary.md`
- `facts/standards/high-reliability-traceability-and-counterfeit-control-metadata.md`
- `facts/standards/fda-medical-device-documentation-and-traceability-metadata.md`
- `logs/p4-33-lane-f-commercial-service-taxonomy.md`
- `logs/p4-33-full-tmps-source-gap-register.md`

Coverage conclusion:

- Source-backed partial reuse exists for service-stage routing, NPI-to-production flow, PCBA inspection/test gates, BOM sourcing posture, traceability vocabulary, and controlled rework framing.
- Current `llm_wiki` does not authorize reusable quote benchmarks, cost percentages, lead-time promises, supplier rankings, factory-capacity proof, active certification claims, or legal advice about copying, cloning, replication, or reverse engineering.

## Per-Draft Disposition

| Draft | Safe reuse now | Blocked claim classes | Status |
| --- | --- | --- | --- |
| `pcb-assembly.md` | SMT/THT/BGA assembly topic structure; turnkey vs consignment decision framing; testing gate placement | fine-pitch limits, BGA yield, X-ray completeness, automotive/medical qualification, quick-turn timelines, supplier proof | `source_backed_fact_layer_partial` |
| `pcb-cloning.md` | deliverable taxonomy and legal-review-needed topic intent only | legality claims, IP-safe duplication, complexity timelines, component reverse-analysis capability, cloning success rate | `blocked_pending_official_source` |
| `pcb-company.md` | service-model taxonomy and non-ranking evaluation-question shape | quality metrics, performance rates, partnership proof, certifications, factory superiority, current business claims | `completed_at_claim_family_level` |
| `pcb-consultation.md` | design-review, troubleshooting, RF/SI/thermal consultation topic clusters | case-study outcomes, certification support proof, solution guarantees, daily-problem capability claims | `completed_at_claim_family_level` |
| `pcb-copying.md` | spare-board and legacy-maintenance demand inventory only | copying legality, remanufacturing permissibility, IP-safe inventory programs, quality equivalence, supplier trust proof | `blocked_pending_official_source` |
| `pcb-design.md` | design-service outline; SI/RF/DFM/thermal section ordering | layout-rule numbers, RF performance guarantees, DFM cost savings, design-excellence proof | `source_backed_fact_layer_partial` |
| `pcb-development.md` | NPI, risk-management, sourcing, validation workflow shape | record-time development, parallel schedule promises, supply-chain superiority, validation completeness | `source_backed_fact_layer_partial` |
| `pcb-engineering.md` | DFM, high-speed, thermal, deliverable taxonomy | prevented-failure guarantees, hidden issue detection promises, engineering capability proof | `source_backed_fact_layer_partial` |
| `pcb-fabrication.md` | HDI/RF/rigid-flex/metal-core topic routing into existing fabrication and material layers | smartphone/5G/mmWave readiness, LDI/backdrill process limits, certifications, HILPCB fabrication proof | `source_backed_fact_layer_partial` |
| `pcb-factory.md` | factory-evaluation section structure | equipment lists, clean-room class, workforce capability, capacity, efficiency, HILPCB factory excellence | `completed_at_claim_family_level` |
| `pcb-inspection.md` | AOI/X-ray/FAI/microsection topic taxonomy and release-gate placement | inspection coverage percentages, microsection acceptance rules, complete QA claims, equipment capability proof | `source_backed_fact_layer_partial` |
| `pcb-manufacturer.md` | manufacturer-tier topic shape and process-category inventory | capability tiers as factual rankings, quality-system proof, specialty-material expertise proof, certifications | `completed_at_claim_family_level` |
| `pcb-manufacturing.md` | China-manufacturing risk questions, material substitution topic demand, QC stage outline | speed promises, material availability claims, certification status, advanced capability proof, why-choose-us proof | `completed_at_claim_family_level` |
| `pcb-modification.md` | ECO/modification topic taxonomy and modify-vs-redesign decision shape | 24-48 hour promises, cost structure, yield fixes, emergency response capability, no-hidden-fee claims | `completed_at_claim_family_level` |
| `pcb-optimization.md` | SI/thermal/DFM/PDN optimization topic clusters | cost reduction percentages, panel math as reusable rule, thermal outcome guarantees, PDN improvement proof | `completed_at_claim_family_level` |
| `pcb-production.md` | prototype-to-production transition, SPC, planning, supply-chain topic demand | volume capability, scalability, SPC metrics, cost optimization, production excellence, supply-chain performance | `completed_at_claim_family_level` |
| `pcb-prototyping.md` | prototype/quick-turn/turnkey/prototype-to-production routing | fast-turn lead times, advanced-prototype capability, supplier excellence, scale-up guarantees | `source_backed_fact_layer_partial` |
| `pcb-quote.md` | quote-input and comparison-framework categories only | 300% price variation, cost percentages, 2025 benchmark pricing, negotiation tactics, fast quote promises | `blocked_pending_official_source` |
| `pcb-redesign.md` | redesign-vs-modify decision framing and architecture/topic inventory | quantified decision matrix, component rules, timeline/cost claims, optimization guarantees | `completed_at_claim_family_level` |
| `pcb-repair.md` | repair-feasibility, BGA repair, ECO, test-after-repair topic structure | repairability guarantees, manufacturer-as-better-partner proof, quality-equivalence, remanufacturing claims | `source_backed_fact_layer_partial` |
| `pcb-replication.md` | prototype-to-production-gap and DFM/test/quality topic demand | legal-safe replication, direct scale failure claims, production volume readiness, supplier CTA proof | `blocked_pending_official_source` |
| `pcb-reverse-engineering.md` | reverse-engineering deliverables and complexity-factor inventory only | legality, ethical permission, recreation accuracy, cost/timeline factors, from-RE-to-production readiness | `blocked_pending_official_source` |
| `pcb-rework.md` | rework-vs-rebuild decision shape; BGA/SMT/ECO topic routing through rework boundary card | BGA rework capability proof, quality-standard compliance, integrated-factory advantage, complete-service proof | `source_backed_fact_layer_partial` |
| `pcb-services.md` | service-spectrum taxonomy; turnkey/consignment/prototyping/production stage routing | complete-service proof, production scaling, supplier excellence, volume service claims, commercial promises | `source_backed_fact_layer_partial` |
| `pcb-solutions.md` | application/material/environment/design solution taxonomy | application readiness, specialty material capability, environmental reliability, HILPCB approach proof | `completed_at_claim_family_level` |
| `pcb-supplier.md` | supplier-evaluation checklist intent and quality-verification questions | China-region comparison, pricing models, partnership advantages, supplier reliability proof, current rankings | `completed_at_claim_family_level` |
| `pcb-testing.md` | flying probe / ICT / AOI / functional-test strategy topic routing | test coverage claims, volume thresholds, documentation completeness, equipment proof, quality guarantees | `source_backed_fact_layer_partial` |
| `pcb-upgrade.md` | legacy upgrade, obsolescence, modernization, migration topic demand | 10+ year migration proof, week-by-week timelines, ROI, industry-specific upgrade claims, outcome guarantees | `completed_at_claim_family_level` |

## Safe Reuse Classes

- article titles, section clusters, reader questions, FAQ intent, and outline shape
- service taxonomy labels such as `fabrication`, `assembly`, `turnkey`, `consignment`, `prototype`, `quick-turn`, `production`, `engineering review`, `testing`, `inspection`, `repair`, `rework`, `ECO`, `redesign`, and `upgrade`
- process-stage routing already supported by `llm_wiki`: prototype vs quick-turn, NPI to mass production, BOM sourcing posture, FAI/FQI gates, AOI/X-ray/ICT/FCT positioning, and controlled rework boundaries
- non-numeric supplier-evaluation questions about process fit, documentation, traceability, communication, review gates, and escalation path
- legal-sensitive service topics only as demand inventory and source gaps, not as advice

## Blocked Claim Classes

- commercial numerics: price, cost percentages, benchmark tables, negotiation outcomes, MOQ, savings, hidden-fee claims
- schedule claims: 24-hour, 48-hour, same-day, fast-turn windows, quote turnaround, delivery promises, production ramp timing
- supplier proof: factory scale, equipment lists, certifications, qualification, approved status, region superiority, partnership advantages, customer trust proof
- capability proof: HDI / RF / BGA / X-ray / microsection / rework / reverse-engineering / specialty-material readiness unless tied to dated records
- quality outcomes: yield, defect rate, DPPM, reliability improvement, complete inspection, quality excellence, process-control maturity
- legal conclusions: legality, ethical permission, IP-safe cloning/copying/replication/reverse-engineering, spare-board program permissibility
- application readiness: automotive, medical, aerospace, defense, 5G, mmWave, industrial, or regulated-market readiness from draft prose alone

## Official-Source Gaps

- commercial governance source lane for quote structure, price language, lead-time language, MOQ language, and dynamic commercial refresh rules
- dated supplier-capability records for any HILPCB / Highleap / APT capability, equipment, certification, capacity, delivery, or quality claims
- official legal-source lane for copying, cloning, replication, reverse engineering, IP ownership, repair rights, and customer authorization boundaries
- stronger inspection / test standards metadata if future posts need acceptance criteria, coverage limits, or microsection thresholds
- application-specific regulated sources for automotive, medical, aerospace, or defense service-readiness language
- obsolescence / redesign / upgrade source lane if future posts need lifecycle, ROI, replacement, or modernization proof

## Prompt-Consumption Gate

1. Use this batch for service-topic demand, article structure, and claim-gap discovery only.
2. Route fabrication, assembly, prototype, production, inspection, testing, sourcing, and rework language through existing `llm_wiki` facts and wiki pages.
3. Do not use draft text for values, thresholds, cost, lead time, supplier status, certifications, quality outcomes, capability proof, or legal advice.
4. For copying, cloning, replication, and reverse engineering, write only with explicit customer-authorization and legal-review boundaries unless official legal sources are later registered.
5. For quote and supplier articles, use non-numeric decision frameworks only until commercial-source governance and dated capability records exist.

## Completion Status

Batch status: `source_backed_fact_layer_partial`

Reason:

- The batch is deletion-safe at dedicated ingestion-map level.
- Existing `llm_wiki` can support some process routing, inspection/test, NPI, sourcing, traceability, and rework boundaries.
- The commercial, supplier-proof, quote, legal-sensitive, factory-capability, certification, speed, quality, and application-readiness portions remain blocked or claim-family-only.

No source records or technical parameter facts were created from the drafts. A separate boundary fact card controls future prompt consumption for this batch.
