# P4-33 Full `/code/blogs/tmps` Learning Plan

## Goal

Absorb the current `/code/blogs/tmps` corpus into `llm_wiki` so future PCB / PCBA blog-writing agents can write from durable, source-traceable engineering data even if the temporary markdown files are later deleted.

This is a learning plan, not a blog-writing plan. It must turn engineer-authored draft blogs into:

- deletion-safe inventory records
- claim-family maps
- official-source or dated-record source registrations
- reusable fact cards
- topic wiki pages
- prompt-consumption gates and blocked-claim lists

## Current Corpus Snapshot

Snapshot date: 2026-04-28.

- total files under `/code/blogs/tmps`: `1419`
- English markdown drafts under `*/en/*.md`: `715`
- dated English draft batches: `29`
- material PDFs under `/code/blogs/tmps/materias_pdf`: present; includes Rogers, AGC, Shengyi, Ventec, Taconic, Arlon / AD, TUC, and other laminate datasheets or fabrication guides

### English Draft Batch Counts

| batch | draft_count | primary theme |
|---|---:|---|
| `2025.7` | 5 | Rogers / PCBA / SMT / THT / keyboard mixed service |
| `2025.7.14` | 25 | PCB types, applications, reliability, power, RF, LED, medical |
| `2025.7.22` | 10 | Rogers, FR-4, edge plating, gold finger, stretchable / transparent / biodegradable |
| `2025.7.23` | 26 | material classes, surface finishes, copper foil, insulation, ceramic, PTFE, polyimide |
| `2025.7.28` | 10 | PCB testing and reliability testing |
| `2025.8.1` | 32 | application PCBs plus FAI and X-ray inspection |
| `2025.8.12` | 57 | high-frequency, impedance, IPC / ISO / RoHS / REACH, displays, automation |
| `2025.8.22` | 40 | LED / MCPCB, keyboard, smart home |
| `2025.8.30` | 15 | circuit board basics, RF / microwave PCB |
| `2025.10.1` | 28 | PCB service taxonomy, reverse engineering, repair, quote, supplier |
| `2025.10.13` | 38 | FR-4, circuit-board service, cost / logistics / supply chain |
| `2025.10.20` | 40 | aluminum / MCPCB and flexible PCB |
| `2025.10.25` | 49 | HDI, rigid-flex, Rogers, RF, ceramic, 4G / 5G / mmWave |
| `2025.11.3` | 18 | PTFE / low-loss, DIY electronics, USB-C, consumer electronics |
| `2025.11.10` | 16 | electronics basics, EMS, CAM, schematic, RF antenna, Taiwan electronics |
| `2025.11.17` | 16 | ceramic Al2O3 / AlN, 4-layer, BOM cost, component comparisons |
| `2025.11.27` | 14 | procurement and service: fast-turn, medical, rigid-flex, Rogers, turnkey |
| `2025.12.10` | 10 | high-frequency / RO4003C / RO4350B / ceramic materials |
| `2025.12.17` | 14 | solar, optical / transparent PCB, procurement |
| `2025.12.20` | 29 | solution pages, HDMI, high-speed, high-reliability, application solutions |
| `2025.12.29` | 48 | PCBA applications: automotive, power, solar, medical, drone, wireless, consumer |
| `2026.1.6` | 20 | high-frequency / RF / microwave service taxonomy |
| `2026.1.13` | 40 | keyboard, mouse, MIDI / audio, industrial / rugged / medical input devices |
| `2026.1.27` | 30 | LED, industrial, consumer, automotive, motor / servo / PLC applications |
| `2026.2.25` | 17 | Kingboard laminate and PI material product drafts |
| `2026.3` | 20 | Rogers RO3003 / RO3006 drafts |
| `2026.4.1` | 27 | 2-layer PCB material / finish / service variants |
| `2026.4.24` | 10 | 6-layer through 24-layer PCB manufacturing |
| `2025.07.13` | 11 | tools, CAM, impedance, vias, multilayer, flex assembly |

## Governing Boundary

The drafts were written by PCB / PCBA engineers, so they are valuable domain input. Treat them as expert-authored claim inventory, outline structure, terminology, and prioritization signal.

Do not treat draft prose alone as reusable fact authority for:

- numeric material properties
- design-rule limits
- process windows
- yield, throughput, quality rates, price, MOQ, lead time, stock, or logistics promises
- supplier-specific capability, certification, approval, qualification, compliance, or release authority
- application readiness for medical, automotive, aerospace, military, safety, RF/mmWave, or high-reliability programs

Promote a draft claim into reusable `facts/` only when one of these exists:

- official source record, such as standards metadata, regulator page, vendor datasheet, vendor processing guide, or certification-program metadata
- dated non-blog internal capability record with scope, date, responsible source, and applicability boundary
- existing `llm_wiki` fact card that already supports the claim

## Status Model

Use these statuses consistently:

- `not_started`: no durable `llm_wiki` intake record for the batch.
- `completed_at_claim_family_level`: title, headings, topic intent, claim families, safe reuse, blocked claims, and source gaps are logged.
- `source_recovery_in_progress`: official-source or dated-record recovery has started.
- `source_backed_fact_layer_partial`: some reusable facts are created, but important gaps remain.
- `source_backed_fact_layer_complete_for_scope`: source records, fact cards, boundaries, and wiki pages are sufficient for a clearly defined scope.
- `blocked_pending_official_source`: public official source is still missing.
- `blocked_pending_dated_capability_record`: public source cannot prove a supplier-specific claim.

## Execution Architecture

### Main-Agent Responsibilities

The main agent owns:

- global plan and priority order
- final batch status
- tracker updates
- source/fact/wiki integration
- conflict resolution between duplicate drafts
- verification before claiming completion

### `gpt-5.4` Subagent Responsibilities

Use `gpt-5.4` subagents for independent lanes only. Each subagent receives:

- exact input files or batch directory
- one assigned lane
- one output log path
- allowed edit paths
- banned edit paths
- instruction to treat drafts as claim inventory, not facts
- instruction not to update trackers unless explicitly assigned

Subagents should usually write lane logs under:

- `llm_wiki/logs/p4-33-lane-<lane-id>-<topic>.md`

The main agent then consolidates them into:

- `llm_wiki/logs/p4-33-full-tmps-master-ingestion-map.md`
- topic-specific source recovery logs
- source records, fact cards, wiki pages, and tracker entries

## Deliverables

### Required Durable Logs

- `logs/p4-33-full-tmps-learning-plan.md`
- `logs/p4-33-full-tmps-source-manifest.md`
- `logs/p4-33-full-tmps-master-ingestion-map.md`
- `logs/p4-33-full-tmps-topic-taxonomy.md`
- `logs/p4-33-full-tmps-source-gap-register.md`
- `logs/p4-33-full-tmps-completion-gate.md`

### Required Lane Logs

At minimum, create lane logs for:

- `materials-rf-high-speed`
- `materials-fr4-ims-flex-ceramic`
- `pcba-process-quality-testing`
- `fabrication-structures-hdi-vias-layer-count`
- `rf-microwave-impedance-high-speed`
- `applications-automotive-medical-industrial-consumer`
- `power-led-solar-energy`
- `input-devices-keyboard-mouse-audio`
- `commercial-procurement-cost-logistics`
- `engineering-basics-tools-cam-calculators`

### Required Fact / Wiki Outputs

Only create these when supported by sources:

- `sources/registry/` records for official sources and dated internal records
- `facts/materials/` exact-product or family-boundary cards
- `facts/methods/` process, inspection, testing, assembly, fabrication, and routing cards
- `facts/standards/` public metadata and standard-scope boundary cards
- `facts/compliance/` RoHS / REACH / ISO / IPC / automotive / medical vocabulary cards
- `wiki/materials/` selector and material-family pages
- `wiki/processes/` fabrication and PCBA flow pages
- `wiki/testing/` inspection, electrical test, environmental test, reliability-test pages
- `wiki/applications/` application-specific consumption pages with clear non-claims

## Workstream 0: Freeze And Baseline Inventory

- [ ] Create `logs/p4-33-full-tmps-source-manifest.md`.
- [ ] Record total file counts, English markdown counts, PDF counts, image folder counts, and each batch directory.
- [ ] Record every `*/en/*.md` path, title if detectable, and first-level heading inventory.
- [ ] Record material PDF filenames and likely vendor / product family from filenames.
- [ ] Compute whether any already-learned batch has moved or disappeared.
- [ ] Search existing `llm_wiki` for each batch name and major slug stem.
- [ ] Mark already-covered current batches:
  - `2025.7`: covered through `P4-32` at existing-layer routing level.
  - `2026.4.1`: analogous to previously ingested APTPCB260401 2-layer scope if the current directory is the same content; verify before marking.
  - `2026.3`: analogous to previously ingested APTPCB RO3003 / RO3006 scope if the current directory is the same content; verify before marking.
  - `2026.1.13`: analogous to previously ingested HILPCB input-device scope if the current directory is the same content; verify before marking.
  - `2026.2.25`: analogous to Kingboard material scope if the current directory matches P4-25 / P4-28; verify before marking.
  - `2026.4.24`: related to P4-20 layer-count coverage; verify exact file set and remaining status.

Completion condition: every current batch has a baseline status of `not_started`, `already_absorbed_verified`, or `needs_delta_ingestion`.

## Workstream 1: Deletion-Safe Batch Intake

- [ ] For each `not_started` batch, create a batch-level ingestion map or include it in the master ingestion map.
- [ ] Preserve file list, title, H2/H3 inventory, primary topic, claim families, and high-risk claims.
- [ ] Do not extract unsupported numeric values into facts in this pass.
- [ ] Record safe reuse classes:
  - terminology
  - outline structure
  - engineering topic clustering
  - problem / decision framing
  - source-gap discovery
- [ ] Record blocked classes:
  - material-property numbers without official datasheet
  - process-window numbers without source or dated record
  - supplier capability without dated capability record
  - certification / compliance / qualification without official metadata
  - price / lead-time / MOQ / stock / yield / quality rate without dated commercial record
- [ ] Update master ingestion map after each batch group.

Completion condition: all 715 markdown drafts are represented in deletion-safe logs.

## Workstream 2: Topic Taxonomy And Deduplication

- [ ] Create `logs/p4-33-full-tmps-topic-taxonomy.md`.
- [ ] Normalize duplicate topic families across batches:
  - Rogers / RO3003 / RO3006 / RO4003C / RO4350B
  - high-frequency / RF / microwave / mmWave
  - FR-4 / high-Tg / epoxy / copper foil / insulation
  - aluminum / MCPCB / IMS / LED thermal
  - ceramic / alumina / AlN / LTCC / HTCC
  - flex / rigid-flex / polyimide / Kapton / LCP
  - surface finish: HASL, lead-free HASL, ENIG, ENEPIG, OSP, immersion silver, immersion gold
  - HDI / microvia / blind via / buried via / via-in-pad / castellated / edge plating / gold finger
  - controlled impedance / TDR / 50 ohm / 100 ohm / differential impedance
  - PCBA / SMT / THT / turnkey / BOM / sourcing / box-build / cable harness
  - testing: flying probe, ICT, FCT, burn-in, vibration, thermal shock, thermal cycling, solderability, X-ray, FAI
  - applications: automotive, medical, industrial, consumer, smart home, solar, power, drone, HDMI, keyboard / mouse / MIDI
  - commercial: cost, quote, lead time, procurement, logistics, supplier, factory, company
- [ ] For each topic family, choose one canonical wiki destination and one blocked-claim list.
- [ ] Mark thin SEO duplicates as outline inputs only, not separate fact targets.

Completion condition: future agents can route any draft slug to a topic family and know whether to reuse, source-recover, or block.

## Workstream 3: Material PDF Source Recovery

- [ ] Register official or locally preserved datasheet source records for PDFs that are usable as source anchors.
- [ ] Separate vendor families:
  - Rogers
  - AGC / Nelco
  - Shengyi
  - Ventec
  - Taconic
  - Arlon / AD / IsoClad / DiClad / CuClad
  - TUC
  - other laminate vendors
- [ ] For each PDF, extract only stable datasheet fields with conditions:
  - Dk and test frequency
  - Df and test frequency
  - Tg / Td / CTE where given
  - thermal conductivity where given
  - copper options / laminate thickness only when source-scoped
  - UL / RoHS / halogen-free only if stated in source and not generalized
- [ ] Create exact-product fact cards only when the PDF source identity is clear.
- [ ] Create family-boundary cards when the PDF is a family datasheet and product-specific extraction would overgeneralize.
- [ ] Cross-link material facts to drafts that requested the data.

Completion condition: high-value local PDFs are either converted into source-backed facts or explicitly marked unusable / needs official URL / needs PDF provenance.

## Workstream 4: Fabrication Structures And Layer-Count Knowledge

- [ ] Audit layer-count, multilayer, 2-layer, 4-layer, 6-to-24-layer, HDI, microvia, blind/buried via, rigid-flex, flex, castellated, cavity, backplane, thick copper, ultra-thin, and high-density drafts.
- [ ] Reuse existing P4-20 / P4-06 / P4-12 layer-count governance where applicable.
- [ ] Add missing deletion-safe maps for batches not already represented.
- [ ] Source-recover only public metadata and official vendor/process guides that can support stable engineering statements.
- [ ] Keep fabricator-specific geometry capability, registration, aspect ratio, min trace/space, drill limits, lead-time, yield, and quality claims blocked unless dated capability records exist.

Completion condition: fabrication-structure topic wiki pages can support conservative blogs without inventing process limits.

## Workstream 5: PCBA Process, Quality, And Testing

- [ ] Audit PCBA, SMT, THT, turnkey, BOM, component sourcing, box-build, electronics assembly, EMS, NPI, mass production, and quality-gate drafts.
- [ ] Audit testing drafts:
  - flying probe
  - ICT
  - FCT
  - burn-in
  - impedance testing
  - solderability testing
  - thermal cycling
  - thermal shock
  - vibration testing
  - X-ray inspection
  - FAI
- [ ] Reuse existing PCBA and testing wiki layers.
- [ ] Add official-source supplement only where current wiki lacks method boundaries or standards metadata.
- [ ] Create fact cards for process flow and test-method boundaries, not universal pass/fail thresholds unless sourced.

Completion condition: PCBA blogs can be generated from process and quality-gate facts with explicit boundaries for thresholds and supplier claims.

## Workstream 6: RF / Microwave / High-Speed / Impedance

- [ ] Audit Rogers, PTFE, low-loss, high-frequency, RF, microwave, antenna, mmWave, 4G, 5G, satellite, radar, telecom, HDMI, high-speed, impedance, and controlled-impedance drafts.
- [ ] Reuse existing Rogers / RO3000 / RO4000 / PTFE / RF validation / impedance / material-selector pages.
- [ ] Fill source gaps from official datasheets and standards metadata only.
- [ ] Keep board-level RF performance, insertion loss, antenna performance, channel budget, mmWave readiness, and supplier measurement capability blocked unless source-backed and scoped.

Completion condition: RF / high-speed topic families have source-backed material selectors and prompt gates for unsupported performance claims.

## Workstream 7: Applications And Industry Pages

- [ ] Audit automotive, ADAS, ECU, EV, BMS, inverter, motor driver, solar, power supply, medical, drone, industrial, smart home, consumer, keyboard, mouse, MIDI / audio, HDMI, LED, optical, transparent, and wearable application drafts.
- [ ] Extract application-specific board requirements as claim families.
- [ ] Route application claims to material, process, compliance, quality, and test layers.
- [ ] Do not create application readiness claims without official regulatory / standards metadata or dated capability records.
- [ ] For supplier-specific application claims, create a dated-record request list instead of fact cards.

Completion condition: application pages become consumption layers over facts, not sources of unsupported capability claims.

## Workstream 8: Commercial, Procurement, Supplier, And Service Claims

- [ ] Audit quote, cost, pricing, lead time, delivery, logistics, supply chain, sourcing, procurement, supplier, manufacturer, factory, company, services, solutions, repair, rework, redesign, cloning, copying, and reverse-engineering drafts.
- [ ] Split reusable content into:
  - stable process explanation
  - RFQ input checklist
  - buyer decision criteria
  - blocked commercial claims
  - supplier-specific dated-record requirements
- [ ] Do not create evergreen price, lead-time, MOQ, stock, yield, throughput, or quality-rate facts.
- [ ] Create prompt-consumption gates that force fresh official / internal commercial records for dynamic claims.

Completion condition: commercial drafts are safe for structure and buyer guidance, but dynamic claims cannot leak into generated blogs.

## Workstream 9: Topic Wiki Aggregation

- [ ] Create or update topic wiki pages only after fact cards exist.
- [ ] Prefer fewer, stronger wiki pages over one wiki page per SEO slug.
- [ ] Candidate wiki pages:
  - `wiki/materials/fr4-and-high-tg-source-boundaries.md`
  - `wiki/materials/ims-mcpcb-and-led-thermal-materials.md`
  - `wiki/materials/ceramic-alumina-aln-and-hybrid-substrates.md`
  - `wiki/materials/flex-polyimide-kapton-and-lcp-materials.md`
  - `wiki/processes/surface-finish-selection-and-limitations.md`
  - `wiki/processes/hdi-via-and-edge-feature-planning.md`
  - `wiki/processes/pcba-assembly-flow-and-quality-gates.md`
  - `wiki/testing/pcb-reliability-and-environmental-test-boundaries.md`
  - `wiki/applications/power-solar-and-inverter-pcba-boundaries.md`
  - `wiki/applications/automotive-medical-and-high-reliability-pcb-boundaries.md`
  - `wiki/applications/input-device-and-consumer-electronics-pcb-boundaries.md`
- [ ] Each wiki page must link `fact_ids` and `source_ids`, list safe claims, and list blocked claims.

Completion condition: blog-writing agents can consume wiki pages instead of searching hundreds of draft maps.

## Workstream 10: Prompt Consumption Gates

- [ ] For every major topic family, create a rewrite / generation gate that states:
  - required facts
  - allowed claims
  - banned claims
  - refresh-required claims
  - fallback wording when data is missing
- [ ] Do not rewrite blogs in this workstream unless separately requested.
- [ ] Record whether each batch is:
  - ready for conservative blog generation
  - mostly ready but needs source supplement
  - claim-family-only
  - blocked pending dated capability record

Completion condition: `llm_wiki` can tell a blog-writing AI what data can be used and what must be searched or refreshed.

## Recommended Execution Order

### Stage A: Corpus Safety

1. Create full source manifest.
2. Create master ingestion map.
3. Verify already-learned and delta batches.
4. Mark every draft as covered by at least claim-family inventory.

### Stage B: Highest Reuse Engineering Layers

1. Materials PDFs and material draft families.
2. RF / high-speed / impedance families.
3. PCBA / testing / quality families.
4. Fabrication structures and layer-count families.

### Stage C: Application And Commercial Layers

1. Power / solar / inverter / LED.
2. Automotive / medical / high-reliability.
3. Industrial / consumer / smart home / input devices.
4. Commercial / procurement / supplier / service pages.

### Stage D: Wiki And Gate Consolidation

1. Create topic wiki pages.
2. Create generation gates.
3. Update tracker statuses.
4. Run final verification.

## Suggested `gpt-5.4` Subagent Lanes

Use subagents only when executing, not while merely maintaining this plan.

### Lane A: Materials PDF And Material Draft Matching

- input:
  - `/code/blogs/tmps/materias_pdf`
  - material-heavy draft batches: `2025.7.22`, `2025.7.23`, `2025.12.10`, `2026.2.25`, `2026.3`
- output:
  - `logs/p4-33-lane-a-materials-pdf-and-draft-matching.md`
- allowed edits:
  - lane log only unless explicitly authorized
- focus:
  - map draft material requests to official/local PDFs and existing source-backed facts

### Lane B: PCBA, Assembly, Testing, And Quality

- input:
  - `2025.7`, `2025.7.28`, `2025.8.1`, `2025.11.10`, `2025.12.29`
- output:
  - `logs/p4-33-lane-b-pcba-testing-quality.md`
- allowed edits:
  - lane log only unless explicitly authorized
- focus:
  - PCBA flow, inspection gates, test methods, reliability tests, FAI / X-ray / ICT / FCT

### Lane C: Fabrication Structures

- input:
  - `2025.07.13`, `2025.7.14`, `2025.10.20`, `2025.10.25`, `2026.4.1`, `2026.4.24`
- output:
  - `logs/p4-33-lane-c-fabrication-structures.md`
- allowed edits:
  - lane log only unless explicitly authorized
- focus:
  - HDI, vias, layer count, flex, rigid-flex, aluminum, ceramic, multilayer, special features

### Lane D: RF, Microwave, High-Speed, And Impedance

- input:
  - `2025.8.12`, `2025.8.30`, `2026.1.6`, `2026.3`, RF files from `2025.10.25`
- output:
  - `logs/p4-33-lane-d-rf-high-speed-impedance.md`
- allowed edits:
  - lane log only unless explicitly authorized
- focus:
  - RF materials, impedance, antenna, microwave, mmWave, HDMI, high-speed boundaries

### Lane E: Applications

- input:
  - `2025.8.22`, `2025.12.17`, `2025.12.20`, `2025.12.29`, `2026.1.13`, `2026.1.27`
- output:
  - `logs/p4-33-lane-e-applications.md`
- allowed edits:
  - lane log only unless explicitly authorized
- focus:
  - LED, solar, power, automotive, medical, industrial, smart home, consumer, keyboard / mouse / MIDI

### Lane F: Commercial And Service Taxonomy

- input:
  - `2025.10.1`, `2025.10.13`, `2025.11.27`, service-heavy files across all batches
- output:
  - `logs/p4-33-lane-f-commercial-service-taxonomy.md`
- allowed edits:
  - lane log only unless explicitly authorized
- focus:
  - quote, cost, lead time, supplier, manufacturer, logistics, sourcing, reverse engineering, repair, rework, solution pages

## Verification Requirements

Before claiming P4-33 complete:

- [ ] `rg -n "p4-33|P4-33" /code/blogs/llm_wiki`
- [ ] every current `/code/blogs/tmps/*/en/*.md` file appears in a P4-33 manifest or earlier verified ingestion log
- [ ] every new fact card `source_id` resolves in `sources/registry`
- [ ] every new wiki `fact_id` resolves in `facts`
- [ ] every dynamic claim class is marked refresh-required or blocked
- [ ] `git diff --check -- /code/blogs/llm_wiki`
- [ ] `git status --short -- /code/blogs/llm_wiki`

## Final Completion Definition

P4-33 is complete only when:

- all current `tmps` English drafts are deletion-safe at claim-family level
- all high-value source-backed facts from drafts and PDFs are extracted or explicitly blocked
- all major topic families have wiki or gate coverage
- trackers distinguish claim-family learning from source-backed fact learning
- no temporary draft is required to write a conservative PCB / PCBA blog on covered topics
- missing data routes to official websites or dated internal records before use
