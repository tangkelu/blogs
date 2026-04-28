---
lane: "P4-34 aluminum / flex / metal-core intake"
title: "Deletion-safe claim-family ingestion map for /code/blogs/tmps/2025.10.20/en"
status: "completed_at_claim_family_level"
reviewed_at: "2026-04-28"
input_directory: "/code/blogs/tmps/2025.10.20/en"
output_path: "/code/blogs/llm_wiki/logs/p4-34-2025-10-20-aluminum-flex-and-metal-core-blog-ingestion-map.md"
owner_scope: "only this log file"
model: "gpt-5.4"
---

# Purpose

Preserve a deletion-safe intake record for the `2025.10.20/en` aluminum, metal-core, and flexible-circuit draft batch. Drafts were treated as claim inventory only, not as authority. This log records what existing `llm_wiki` support can safely cover, which claim families remain blocked, and which official-source lanes are still required.

# Input Files Inspected

- `aluminum board.md`
- `aluminum-base-pcb.md`
- `aluminum-circuit-board.md`
- `aluminum-core-pcb.md`
- `aluminum-pcb-assembly.md`
- `aluminum-pcb-fabrication.md`
- `aluminum-pcb-factory-turnkey-service.md`
- `aluminum-pcb-factory.md`
- `aluminum-pcb-manufacturer-china.md`
- `aluminum-pcb-manufacturer.md`
- `aluminum-pcb-manufacturing-quality-control.md`
- `aluminum-pcb-manufacturing.md`
- `aluminum-pcb-production-scale-volume.md`
- `aluminum-pcb-production.md`
- `aluminum-pcb-prototype-manufacturing.md`
- `aluminum-pcb-prototyping.md`
- `aluminum-pcb-supplier.md`
- `aluminum-substrate.md`
- `bendable-pcb.md`
- `custom-aluminum-pcb-manufacturing-solutions.md`
- `double-layer-flex-pcb.md`
- `dynamic-flex-pcb.md`
- `flex-pcb-assembly.md`
- `flex-pcb-manufacturing.md`
- `flex-pcb.md`
- `flexible-circuit-board.md`
- `flexible-connector-pcb.md`
- `flexible-pcb-assembly.md`
- `flexible-pcb-manufacturer.md`
- `flexible-pcb-manufacturing.md`
- `flexible-pcb.md`
- `foldable-pcb.md`
- `fpc-board.md`
- `high-thermal-aluminum-pcb.md`
- `metal-core-pcb-manufacturing-services.md`
- `metal-core-pcb.md`
- `multilayer-flex-pcb.md`
- `polyimide-pcb.md`
- `rollable-pcb.md`
- `single-layer-flex-pcb.md`

# Heading / Topic Clusters

## Aluminum / metal-core / IMS thermal-platform framing

- Core topics seen in titles and headings:
  aluminum board design, aluminum-base PCB, aluminum circuit board, aluminum-core PCB, metal-core PCB, aluminum substrate, high-thermal aluminum PCB.
- Repeating claim families:
  thermal-management superiority, layer/construction variants, copper-weight selection, dielectric selection, substrate-thickness selection, EMI shielding, application fit for LED/power/automotive, board-level heat-spread outcomes.

## Aluminum manufacturing / factory / prototype / supplier / turnkey framing

- Core topics seen in titles and headings:
  fabrication, assembly, turnkey workflow, factory strength, manufacturer evaluation, supplier selection, quality control, production scale, prototype transition, custom solutions.
- Repeating claim families:
  shop capability depth, process control, testing coverage, quality systems, certifications, China sourcing advantage, prototype-to-volume speed, cost/lead-time/scale claims, turnkey integration proof.

## General flex / FPC / flexible-manufacturing framing

- Core topics seen in titles and headings:
  flex PCB basics, flexible circuit-board design, flexible PCB manufacturing, FPC applications, connector-flex integration, manufacturer evaluation.
- Repeating claim families:
  flex construction classes, material framing, layout guidance, application examples, process flow, quality control, cost/lead-time, supplier reliability.

## Flex assembly framing

- Core topics seen in titles and headings:
  flex PCB assembly, flexible PCB assembly.
- Repeating claim families:
  fixturing, SMT handling, double-sided assembly, inspection, reliability testing, module integration, delivery metrics.

## Flex structure variants and bend-posture framing

- Core topics seen in titles and headings:
  single-layer, double-layer, multilayer, dynamic flex, bendable, rollable, foldable.
- Repeating claim families:
  bendability by structure, copper-type choice, adhesiveless vs adhesive constructions, roll diameter, bend ratio, cycle life, transition zones, wearables/displays/automotive applications.

## Polyimide material framing

- Core topics seen in titles and headings:
  polyimide chemistry, film types, thermal performance, chemical resistance, harsh-environment applications.
- Repeating claim families:
  film properties, high-temperature use, moisture/chemical/radiation resistance, low-temperature performance, thermal cycling, finished-board suitability.

# Existing `llm_wiki` Support Found

## Strong support already present

- Flex material class framing:
  `facts/materials/flex-polyimide-and-lcp-class-source-coverage.md`
- Exact-product polyimide-film examples:
  `facts/materials/dupont-kapton-hn.md`
  `facts/materials/ube-upilex-s.md`
- Bend-posture and rigid-flex guidance boundaries:
  `facts/methods/parameter-scope-rigid-flex-bend-guidance.md`
  `facts/methods/rigid-flex-stackup-and-bend-reliability-posture.md`
- IMS / MCPCB exact-product material and scope controls:
  `facts/materials/ventec-vt-4b7.md`
  `facts/materials/ventec-vt-4bc.md`
  `facts/materials/ventec-vt-4bd.md`
  `facts/materials/parameter-scope-ventec-ims-material-values.md`
- MCPCB assembly framing:
  `facts/methods/mcpcb-ims-and-reflow-source-coverage.md`
- Prior batch coverage map for this same topic family:
  `logs/p4-33-lane-c-fabrication-structures.md`

## Coverage shape

- Existing support is good for:
  class-level separation, exact-product material examples with preserved scope, bend-guidance-as-design-context, IMS material examples, and anti-overclaim boundaries.
- Existing support is weak or absent for:
  board-level thermal outcomes, dynamic/rollable/foldable life claims, supplier-specific capability proof, current commercial terms, and production/certification banners.

# Per-Draft / Per-Claim-Family Disposition

| Scope | Files | Disposition | Safe reuse from existing `llm_wiki` | Blocked claim classes |
| --- | --- | --- | --- | --- |
| Aluminum / metal-core / IMS structure and platform framing | `aluminum board.md`, `aluminum-base-pcb.md`, `aluminum-circuit-board.md`, `aluminum-core-pcb.md`, `aluminum-substrate.md`, `high-thermal-aluminum-pcb.md`, `metal-core-pcb.md` | `source_backed_fact_layer_partial` | MCPCB / IMS / metal-core as thermal-platform class framing; Ventec exact-product IMS examples when product name and test conditions remain attached; MCPCB assembly as material-plus-reflow problem | Draft-originated board-vs-FR4 multipliers, junction-temperature deltas, lifespan multipliers, generic aluminum thermal conductivity rows, dielectric-thickness defaults, current capacity tables, via-count rules, EMI guarantees, application-readiness claims |
| Aluminum assembly / fabrication / factory / supplier / prototype / turnkey | `aluminum-pcb-assembly.md`, `aluminum-pcb-fabrication.md`, `aluminum-pcb-factory-turnkey-service.md`, `aluminum-pcb-factory.md`, `aluminum-pcb-manufacturer-china.md`, `aluminum-pcb-manufacturer.md`, `aluminum-pcb-manufacturing-quality-control.md`, `aluminum-pcb-manufacturing.md`, `aluminum-pcb-production-scale-volume.md`, `aluminum-pcb-production.md`, `aluminum-pcb-prototype-manufacturing.md`, `aluminum-pcb-prototyping.md`, `aluminum-pcb-supplier.md`, `custom-aluminum-pcb-manufacturing-solutions.md`, `metal-core-pcb-manufacturing-services.md` | `completed_at_claim_family_level` | Only generic process-stage vocabulary, quality-gate categories, and conservative statements that assembly depends on material selection, profiling, inspection, and validation | Factory depth, equipment proof, yield/throughput, defect-rate claims, prototype/volume lead times, MOQ, pricing, turnkey completeness, country/manufacturer superiority, certifications, PPAP/automotive qualification, “one-stop” capability proof, test coverage as released-lot proof |
| General flex / FPC / flexible-manufacturing framing | `flex-pcb.md`, `flexible-pcb.md`, `flexible-circuit-board.md`, `flex-pcb-manufacturing.md`, `flexible-pcb-manufacturing.md`, `flexible-pcb-manufacturer.md`, `fpc-board.md`, `flexible-connector-pcb.md` | `source_backed_fact_layer_partial` | Flex vs rigid-flex class framing; conservative polyimide/LCP family wording; exact-product `Kapton HN` or `UPILEX-S` examples where scoped; bend guidance only as design-guide context | Generic polyimide/Kapton numeric ladders, default trace/space minima, default copper-type rules, connector-flex reliability claims, manufacturer ranking, quick-turn/price claims, compliance/certification banners, production proof |
| Flex assembly | `flex-pcb-assembly.md`, `flexible-pcb-assembly.md` | `source_backed_fact_layer_partial` | General assembly-risk framing: fixturing, handling, bend-zone awareness, inspection, validation, and profile matching are all relevant | Named process windows, line capability, component-size limits, endurance/yield figures, box-build completeness, lead time, quality-rate claims, supplier proof |
| Flex structure variants | `single-layer-flex-pcb.md`, `double-layer-flex-pcb.md`, `multilayer-flex-pcb.md`, `dynamic-flex-pcb.md`, `bendable-pcb.md`, `rollable-pcb.md`, `foldable-pcb.md` | `blocked_pending_official_source` | Structural vocabulary only: single/double/multilayer distinctions, static-vs-dynamic bend separation, need for thickness/copper/adhesive/neutral-axis review | Bend-radius tables treated as universal rules, cycle-life counts, roll-diameter ranges, RA-vs-ED superiority quantified as universal, adhesiveless-thickness deltas, dynamic-life guarantees, display/automotive qualification, IPC/Class banners, repeated-motion proof |
| Polyimide material | `polyimide-pcb.md` | `source_backed_fact_layer_partial` | Exact-product film examples from `Kapton HN` and `UPILEX-S`; conservative statement that film properties do not equal finished-board reliability | Generic polyimide temperature, moisture, radiation, chemical, or tensile values; finished-board harsh-environment qualification; soldering-cycle guarantees; aerospace/medical/automotive approval claims |

# Safe Reuse Classes

- Topic intent, file titles, and heading structure as rewrite inventory.
- Class-level distinctions among flex, rigid-flex, FPC, polyimide-film examples, MCPCB, metal-core, and IMS.
- Exact-product material examples only when they stay source-scoped:
  `Ventec VT-4B7`, `VT-4BC`, `VT-4BD`, `DuPont Kapton HN`, `UBE UPILEX-S`.
- Design-review framing that depends on thickness, layer count, bend type, copper type, adhesive system, coverlay, neutral axis, and manufacturer review.
- MCPCB assembly framing that separates material selection, paste/profile selection, thermal validation, and application qualification.
- Conservative statements that internal HIL/APT pages are service-context framing, not independent proof of released capability.

# Blocked Claim Classes

- Unsupported numeric claims from drafts, including:
  material-property rows, substrate-thickness defaults, dielectric thermal conductivity ladders, copper-weight/current tables, trace/space minima, via-count formulas, board-vs-FR4 multipliers, temperature-rise or junction-temperature deltas, lifespan multipliers, bend-cycle counts, roll-diameter ranges, thermal-shock counts.
- Unsupported supplier/process/capability claims:
  blind/buried-via-for-aluminum defaults, dynamic-flex production readiness, connector-flex precision proof, line capability, equipment depth, registration accuracy, AOI/e-test/test-program completeness, thermal-simulation proof, FEM validation claims.
- Unsupported certification/compliance/qualification claims:
  IATF, IPC class, PPAP, automotive/medical/aerospace approval, biocompatibility, customer acceptance, lot release, qualification to specific markets.
- Unsupported commercial claims:
  price, cost savings, lead time, quick turn, MOQ, prototype turnaround, production scale, yield, throughput, quality rate, sourcing superiority, “trusted supplier” proof.
- Unsupported finished-board performance claims:
  actual heat-spreading outcome, EMI shielding outcome, reliability improvement, continuous-motion survival, foldable/rollable display readiness, harsh-environment product success.

# Official-Source Gaps

## Flex / polyimide side

- Official flex-laminate or flex-material vendor sources beyond current Panasonic class framing and the two exact-product film examples.
- Public official sources for dynamic flex, foldable, rollable, and connector-flex design/reliability framing.
- Public standards metadata or vendor design guides that support single-layer, double-layer, and multilayer flex construction differences without turning them into supplier capability claims.

## Aluminum / IMS / metal-core side

- Additional official IMS suppliers if supplier-neutral comparisons are needed.
- Official metal-core / IMS processing or design guides for platform-selection context beyond current Ventec material cards.
- Dated capability records if any draft needs HIL/APT-specific aluminum stackups, copper weights, base-metal options, testing depth, or production claims.

## Commercial / factory / quality side

- Dated internal capability records for any real factory, certification, prototype, volume, turnaround, or quality-rate claim.
- Official standards/regulator metadata if future pages require standards naming beyond generic category references.

# Suggested Source Recovery Lanes

1. `flex-variant-official-source-recovery`
   Recover official design guides or vendor docs for dynamic flex, rollable, foldable, and connector-flex posture.
2. `polyimide-material-anchor-expansion`
   Add at least one supplier-controlled flex-laminate/polyimide construction source so generic PI flex pages are not forced to rely only on film examples.
3. `ims-platform-expansion`
   Add more official IMS / metal-base suppliers or platform docs before any supplier-neutral aluminum/metal-core comparison writing.
4. `dated-capability-record-lane`
   Recover dated HIL/APT capability evidence before allowing factory, lead-time, scale, quality-rate, or certification claims.

# Completion Status

- Batch intake status:
  `completed_at_claim_family_level`
- Flex / polyimide knowledge state:
  `source_backed_fact_layer_partial`
- IMS / metal-core knowledge state:
  `source_backed_fact_layer_partial`
- Dynamic / rollable / foldable / connector-flex variant state:
  `blocked_pending_official_source`
- Factory / supplier / prototype / commercial claim state:
  `blocked_pending_dated_capability_record`

# Completion Notes

This batch is deletion-safe at claim-family level only. Existing `llm_wiki` support can supply guarded class framing and a few exact-product anchors, but the draft set remains far from fully learned. No fact cards, wiki pages, source registries, or global trackers were edited in this lane.
