# P4-34 2025-10-25 Ceramic, Rogers, HDI, And IC-Substrate Blog Ingestion Map

Date: 2026-04-28

## Purpose

This map audits the claim families in the relevant English drafts under `/code/blogs/tmps/2025.10.25/en` for ceramic PCB, Rogers material, HDI, microvia, and IC-substrate-adjacent topics.

The drafts are treated as demand and claim inventory only. They are not authority for numeric material properties, process windows, impedance, thermal behavior, RF performance, supplier capability, certification, price, lead time, MOQ, yield, throughput, quality rate, or commercial proof.

## Input Files Inspected

- `ceramic-pcb-manufacturing.md`
- `ceramic-pcb-manufacturer.md`
- `ceramic-pcb-fabrication.md`
- `ceramic-pcb-assembly.md`
- `htcc-pcb.md`
- `thin-film-pcb.md`
- `rogers-pcb-production.md`
- `rogers-tmm-pcb.md`
- `rogers-pcb-fabrication.md`
- `rogers-circuit-board-manufacturing.md`
- `rogers-material-pcb.md`
- `rogers-ro3000-pcb.md`
- `rogers-ro4000-pcb.md`
- `rogers-pcb-assembly.md`
- `rogers-pcb-supplier.md`
- `rogers-board.md`
- `rogers-printed-circuit-board.md`
- `rogers-pcb-prototyping.md`
- `rogers-substrate-pcb.md`
- `rogers-pcb-manufacturer.md`
- `hdi-printed-circuit-board.md`
- `high-density-interconnect-pcb.md`
- `hdi-board.md`
- `hdi-pcb-substrate.md`
- `hdi-pcb-assembly.md`
- `hdi-pcb.md`
- `hdi-circuit-board.md`
- `microvias-pcb.md`
- `blind-via-pcb.md`
- `buried-via-pcb.md`

## Heading / Topic Clusters

| Cluster | Drafts | Observed topic intent |
| --- | --- | --- |
| Ceramic manufacturing and supplier framing | `ceramic-pcb-manufacturing.md`, `ceramic-pcb-manufacturer.md`, `ceramic-pcb-fabrication.md`, `ceramic-pcb-assembly.md` | ceramic process flow, metallization, assembly handling, QA, manufacturer selection, HILPCB partner framing |
| Ceramic specialty subfamilies | `htcc-pcb.md`, `thin-film-pcb.md` | HTCC process posture, HTCC versus LTCC/thin film, thin-film deposition/patterning, application framing |
| Rogers generic manufacturing and sourcing | `rogers-pcb-production.md`, `rogers-pcb-fabrication.md`, `rogers-circuit-board-manufacturing.md`, `rogers-pcb-supplier.md`, `rogers-board.md`, `rogers-printed-circuit-board.md`, `rogers-pcb-manufacturer.md`, `rogers-pcb-prototyping.md`, `rogers-pcb-assembly.md` | Rogers material family selection, RF fabrication and assembly, prototyping, production, sourcing, QA, cost/lead-time/commercial positioning |
| Rogers product-family and substrate selection | `rogers-material-pcb.md`, `rogers-ro3000-pcb.md`, `rogers-ro4000-pcb.md`, `rogers-tmm-pcb.md`, `rogers-substrate-pcb.md` | RO3000, RO4000, TMM, material comparison, hybrid stackup, RF application routing |
| HDI generic manufacturing and application framing | `hdi-printed-circuit-board.md`, `high-density-interconnect-pcb.md`, `hdi-board.md`, `hdi-pcb.md`, `hdi-circuit-board.md`, `hdi-pcb-assembly.md` | HDI value framing, density, microvia process, assembly, cost, thermal, RF, future-system applications |
| HDI feature and substrate variants | `microvias-pcb.md`, `blind-via-pcb.md`, `buried-via-pcb.md`, `hdi-pcb-substrate.md` | microvia types, blind/buried-via routing, laser drilling, via fill, material selection, IC-substrate adjacency |

## Existing `llm_wiki` Support Found

Reusable support already present:

- Ceramic class framing:
  - `facts/materials/ceramic-alumina-aln-class-source-coverage.md`
  - `wiki/materials/ceramic-aln-ims-thermal-platforms.md`
  - source anchors under `sources/registry/internal/` and `sources/registry/materials/` for HIL/APT ceramic pages, CeramTec, and MARUWA
- Rogers family and product framing:
  - `facts/materials/rogers-material-selector.md`
  - `facts/materials/rogers-ro3003.md`
  - `facts/materials/rogers-ro3006.md`
  - `facts/materials/rogers-ro3010.md`
  - `facts/materials/rogers-ro3035.md`
  - `facts/materials/rogers-ro4003c.md`
  - `facts/materials/rogers-ro4350b.md`
  - `facts/materials/rogers-ro4835.md`
  - `facts/materials/rogers-ro4830-plus.md`
  - `facts/materials/rogers-ro4360g2.md`
  - `facts/materials/rogers-ro4450f.md`
  - `facts/materials/rogers-ro3000-processing.md`
  - `facts/materials/rogers-tmm-family.md`
  - `facts/materials/rogers-tmm-10i.md`
  - `facts/materials/rogers-bondply-and-hybrid-stackup-coverage.md`
  - `facts/materials/parameter-scope-rogers-rf-laminate-values.md`
  - `wiki/materials/rogers-ro3000-family.md`
- HDI / microvia / substrate posture:
  - `facts/methods/hdi-microvia-and-vippo-process-posture.md`
  - `facts/methods/microvia-reliability-public-context.md`
  - `facts/methods/ic-substrate-fine-line-build-up-posture.md`
  - `facts/methods/any-layer-hdi-public-boundary-for-20-layer.md`
  - `facts/methods/20-layer-any-layer-hdi-rewrite-guardrail.md`
  - `facts/materials/build-up-and-hdi-material-context-for-20-layer.md`
  - `facts/standards/hdi-design-reference-status-metadata.md`
  - `facts/standards/ipc-hdi-electrical-test-and-coating-metadata.md`
  - source anchors for IPC 2226A, IPC/JPCA-2315 legacy status, IPC microvia reliability material, NASA context, internal HIL/APT HDI pages, and internal IC-substrate pages

Weak or absent support:

- HTCC-specific official datasheet coverage, co-fire metallurgy boundaries, shrinkage/process-control data, and qualified application framing
- thin-film ceramic process-source coverage for sputtering/plating/patterning numerics, line/space, film thickness, medical suitability, and reliability outcomes
- blind-via and buried-via public boundary cards distinct from generic HDI posture
- official-source-backed Rogers assembly process windows, SMT/reflow handling specifics, and RF validation workflow details
- official-source-backed Rogers and HDI supplier/commercial proof for stock, lead time, volume, price, delivery, certification, and quality-rate language
- official-source-backed public IC-substrate boundary cards for exact line/space, bump pitch, warpage, SAP geometry, or package qualification thresholds

## Per-Draft And Claim-Family Disposition

| Draft or family | Current status | Safe reuse | Blocked from draft-to-fact promotion |
| --- | --- | --- | --- |
| `ceramic-pcb-manufacturing.md` | `source_backed_fact_layer_partial` | ceramic class framing, DBC/DPC/HTCC as topic labels only, process-stage inventory, thermal-platform intent | numeric material values, metallization/process windows, DFM rules, yield, capability, quality, application-readiness, HILPCB proof |
| `ceramic-pcb-manufacturer.md` | `completed_at_claim_family_level` | manufacturer-selection topic intent, ceramic/HTCC/thin-film demand inventory | in-house equipment, capability breadth, test coverage, industry proof, certifications, scale, quality-rate, trust claims |
| `ceramic-pcb-fabrication.md` | `completed_at_claim_family_level` | ceramic fabrication stage sequence, metallization/patterning/via topic map | laser/via dimensions, plating specs, surface-finish compatibility, machining tolerances, process controls |
| `ceramic-pcb-assembly.md` | `completed_at_claim_family_level` | ceramic assembly challenge taxonomy, SMT/reflow/bonding topic intent | paste, placement, reflow, bonding, defect, inspection, reliability, zero-defect, and assembly-capability claims |
| `htcc-pcb.md` | `completed_at_claim_family_level` | HTCC as a ceramic subfamily topic, HTCC vs LTCC/thin-film comparison demand | HTCC property values, co-fire metallurgy specifics, temperature/power endurance, application proof, fabrication parameters, QA evidence |
| `thin-film-pcb.md` | `completed_at_claim_family_level` | thin-film ceramic as a topic family, deposition/patterning workflow intent | deposition thickness, pattern precision, RF/medical suitability, reliability, fabrication parameters, HILPCB capability |
| Rogers generic manufacturing / sourcing family | `source_backed_fact_layer_partial` | Rogers family names, official family-selection routing, RO3000/RO4000/TMM differentiation, hybrid-stackup caution, topic intent for RF manufacturing | generic `Rogers PCB` property tables, supplier stock, certified sourcing, lead time, cost, throughput, volume, quality proof, shipping, commercial guarantees |
| `rogers-ro3000-pcb.md` | `source_backed_fact_layer_partial` | RO3000 family routing through official product cards and family wiki, condition-bound values from existing cards | family flattening, unqualified thermal/RF outcomes, design-rule numerics, manufacturing limits, quick-turn claims |
| `rogers-ro4000-pcb.md` | `completed_at_claim_family_level` | RO4000 family demand signal, hydrocarbon/ceramic family positioning as a topic | unsupported RO4000 family-wide values, low-loss/performance guarantees, application readiness, price/delivery language |
| `rogers-tmm-pcb.md` | `source_backed_fact_layer_partial` | TMM family framing through `facts/materials/rogers-tmm-family.md` and `facts/materials/rogers-tmm-10i.md` | family-to-grade overgeneralization, thermal/rf superiority claims, HILPCB capability, application proof |
| `rogers-substrate-pcb.md` | `source_backed_fact_layer_partial` | comparison intent among RO4003C / RO4350B / RT-duroid routing, hybrid stackup topic intent | availability, lead time, cost optimization, QC proof, universal substrate-selection claims, mmWave qualification |
| `rogers-material-pcb.md` | `source_backed_fact_layer_partial` | material-selector topic intent and official family routing | generic material-property averaging, universal RF superiority, supplier/commercial proof |
| `rogers-pcb-assembly.md` | `completed_at_claim_family_level` | assembly topic demand, RF assembly handling categories, test-taxonomy demand | material handling windows, SMT/reflow methods, RF validation specifics, traceability systems, SPC, reliability proof, end-to-end capability |
| `rogers-pcb-prototyping.md` | `completed_at_claim_family_level` | prototyping demand signal, material-family selection sections as topic map | fast-turn, seamless prototype-to-volume, internal engineering capability, delivery promises |
| `rogers-pcb-production.md`, `rogers-circuit-board-manufacturing.md`, `rogers-pcb-fabrication.md`, `rogers-board.md`, `rogers-printed-circuit-board.md`, `rogers-pcb-supplier.md`, `rogers-pcb-manufacturer.md` | `completed_at_claim_family_level` | outline shape, topic intent, family segmentation, demand for commercial-proof lanes | pricing, production volume, sourcing control, certifications, QA rates, turnaround, logistics, “trusted” or “leading” supplier proof |
| HDI generic manufacturing family | `source_backed_fact_layer_partial` | HDI as build-up/microvia/VIPPO posture, any-layer and sequential-build topic framing, standards metadata, cautionary reliability context | generic cost optimization, thermal outcomes, RF performance, future-system readiness, application proof, fab limits, commercial claims |
| `microvias-pcb.md` | `source_backed_fact_layer_partial` | microvia vocabulary, blind/buried/stacked/staggered taxonomy, reliability caution framing, laser-drill topic intent | size ranges, drill parameters, copper fill requirements, spacing/density limits, test thresholds, yield/reliability outcomes |
| `blind-via-pcb.md` | `completed_at_claim_family_level` | blind-via topic demand and relation to HDI routing | exact architecture, drill/fill rules, reliability outcomes, application proof, capability claims |
| `buried-via-pcb.md` | `completed_at_claim_family_level` | buried-via topic demand and multilayer-routing intent | material/lamination windows, drill/fill specifics, cross-industry proof, QA claims, HILPCB capability |
| `hdi-pcb-substrate.md` | `source_backed_fact_layer_partial` | build-up material context, HDI material-choice taxonomy, IC-substrate adjacency topic, ABF/BT class existence | IC-substrate capability thresholds, exact HDI material rankings, certification, supply consistency, substrate suitability claims |
| `hdi-pcb-assembly.md` | `completed_at_claim_family_level` | HDI assembly-stage topic map and mixed-technology demand | precision assembly claims, x-ray/testing sufficiency, validation coverage, supplier proof |
| `hdi-pcb.md`, `hdi-board.md`, `hdi-circuit-board.md`, `hdi-printed-circuit-board.md`, `high-density-interconnect-pcb.md` | `source_backed_fact_layer_partial` | HDI posture, density/microvia topic framing, build-up material context, internal capability posture only at guarded summary level | cost, lead time, RF/mmWave performance, 5G/AI/6G/server readiness, thermal/integrity outcomes, partner-selection proof |

## Safe Reuse Classes

- title, H2, and H3 outline shape as topic-intent inventory
- ceramic/alumina/AlN thermal-platform framing only through existing ceramic class cards and wiki pages
- Rogers family names and member routing only through existing official-source-backed cards and family wiki pages
- TMM family framing only through existing TMM cards, keeping family-level and grade-level claims separate
- HDI, microvia, any-layer, sequential build-up, VIPPO, and IC-substrate posture only through existing methods cards and standards metadata
- microvia reliability discussion only at cautionary public-context level, without thresholds or approval language
- ABF and BT substrate class existence only through existing source-backed substrate material coverage
- draft topic demand for future standalone lanes: HTCC, thin film, blind via, buried via, Rogers assembly, HDI assembly, and IC-substrate public-boundary work

## Blocked Claim Classes

- any draft-originated numeric material parameter, including dielectric, loss, thermal conductivity, CTE, Tg, thickness, shrinkage, or metallization values
- any process-window, drill, via, copper-fill, lamination, plating, reflow, assembly, or inspection threshold claim
- any impedance, signal-integrity, RF, mmWave, antenna, radar, 5G, 6G, AI-edge, server, thermal, or power-performance outcome claim
- any HDI capability, IC-substrate capability, fine-line, SAP, warpage, bump, package, or qualification threshold claim not already supported by current guarded internal cards
- any certification, compliance, qualification, quality-rate, zero-defect, reliability-rate, or “proven” manufacturing claim
- any supplier-proof, manufacturer-ranking, factory-scale, equipment-proof, throughput, yield, delivery, MOQ, stock, price, or lead-time claim
- any broad application-readiness claim for aerospace, defense, automotive, medical, satellite, wearable, or telecom use without direct official-source support

## Official-Source Gaps

- HTCC official manufacturer or standards anchors for process posture, metallization systems, temperature/use boundaries, and application framing
- thin-film ceramic official sources for deposition methods, substrate compatibility, line/space, film systems, and medical/reliability boundaries
- blind-via and buried-via source cards separated from generic microvia/HDI posture
- public-source-backed Rogers assembly and RF validation workflow coverage
- stronger official RO4000 family coverage beyond current member-level anchors if family-wide writing is needed
- official-source-backed ceramic assembly guidance and hybrid bonding coverage
- public-source-backed IC-substrate boundary sources for what can be said safely outside internal capability posture
- dated internal records if any supplier-specific capability, quote speed, certification, quality, or delivery language is ever required

## Suggested Source Recovery Lanes

1. `ceramic-htcc-thin-film-lane`
   Recover official HTCC and thin-film manufacturer or standards sources before allowing technical or application claims.
2. `ceramic-assembly-lane`
   Recover official or dated internal ceramic-assembly handling and inspection sources before reusing assembly-process language.
3. `rogers-family-gap-lane`
   Add stronger family-wide RO4000 and Rogers assembly/test sources so generic Rogers manufacturing drafts can be rewritten safely.
4. `blind-buried-via-lane`
   Create dedicated blind-via and buried-via boundary cards instead of relying only on generic HDI posture.
5. `ic-substrate-public-boundary-lane`
   Recover public substrate-class and package-substrate boundary sources to separate rigid HDI from IC-substrate claims more clearly.
6. `commercial-proof-lane`
   Only if needed, attach dated internal records for certifications, turnaround, production scale, quality systems, and sourcing claims.

## Completion Status

This lane is `completed_at_claim_family_level` overall.

More specific status:

- Ceramic generic framing: `source_backed_fact_layer_partial`
- Rogers material-family routing: `source_backed_fact_layer_partial`
- HDI / microvia posture: `source_backed_fact_layer_partial`
- HTCC, thin-film, blind-via, buried-via, Rogers assembly, HDI assembly, and commercial-proof branches: `completed_at_claim_family_level`
- IC-substrate exact-capability reuse from this batch: still blocked beyond existing guarded internal posture

No new fact cards, wiki pages, source records, or tracker edits were created in this lane. No unsupported numeric, process, RF, HDI/IC-substrate capability, certification, commercial, or supplier-proof claims were promoted from temporary drafts into reusable facts.
