---
lane: "P4-48c HDI/BOM cost-driver evidence scout"
title: "Scout log for BOM cost, HDI cost, and PCB cost-reduction evidence lanes"
status: "completed_at_claim_family_level"
reviewed_at: "2026-04-29"
owner_scope: "/code/blogs/llm_wiki/logs/p4-48c-hdi-bom-cost-driver-evidence-scout.md"
model: "gpt-5"
---

# Purpose And Scope

- Inspect the assigned BOM / HDI / cost-reduction drafts as claim inventory only.
- Cross-check existing `llm_wiki` coverage for BOM/sourcing posture, HDI vocabulary, and any reusable public cost-driver evidence.
- Identify only primary-source / official-source recovery lanes worth doing next.
- Do not create facts, wiki pages, source records, or tracker updates.
- Keep the lane conservative around price, savings, lead time, MOQ, yield, and supplier capability claims.

# Exact Files Reviewed

## Claim Inventory Inputs

- `/code/blogs/tmps/2025.11.17/en/bom-cost.md`
- `/code/blogs/tmps/2025.11.27/en/hdi-pcb-cost.md`
- `/code/blogs/tmps/2025.11.27/en/pcb-cost-reduction.md`
- `/code/blogs/llm_wiki/logs/p4-40-2025-11-17-ceramic-power-basics-official-source-recovery-scout.md`
- `/code/blogs/llm_wiki/logs/p4-40-2025-11-27-service-cost-medical-rf-quickturn-official-source-recovery-scout.md`

## Existing `llm_wiki` Support Files Opened

- `/code/blogs/llm_wiki/facts/methods/pcba-bom-sourcing-and-traceability-posture.md`
- `/code/blogs/llm_wiki/wiki/processes/pcba-npi-to-mass-production-flow.md`
- `/code/blogs/llm_wiki/facts/methods/hdi-microvia-and-vippo-process-posture.md`
- `/code/blogs/llm_wiki/facts/methods/microvia-reliability-public-context.md`
- `/code/blogs/llm_wiki/facts/standards/ecss-via-hdi-microvia-definitions.md`
- `/code/blogs/llm_wiki/facts/standards/hdi-design-reference-status-metadata.md`
- `/code/blogs/llm_wiki/facts/standards/ipc-surface-finish-taxonomy-osp-hasl-extension.md`
- `/code/blogs/llm_wiki/facts/methods/surface-finish-selection-for-rf.md`
- `/code/blogs/llm_wiki/wiki/processes/rf-surface-finish-selection.md`
- `/code/blogs/llm_wiki/logs/p4-44-blog-learning-continuation-handoff.md`
- `/code/blogs/llm_wiki/logs/h4-shared-b-capability-parameters-first-wave-queue.md`
- `/code/blogs/llm_wiki/logs/p4-20-layer-count-claim-coverage-map.md`

## Tree-Wide Coverage Sweeps

- Keyword sweeps across `/code/blogs/llm_wiki` for `BOM`, `sourcing`, `traceability`, `HDI`, `microvia`, `sequential lamination`, `panelization`, `surface finish`, `ENIG`, `OSP`, `HASL`, `cost`, `savings`, `lead time`, and related blockers.

# Existing `llm_wiki` Support Worth Reusing

## BOM / Sourcing Posture

- `facts/methods/pcba-bom-sourcing-and-traceability-posture.md`
  - strongest current reuse for BOM review, AVL / authorized sourcing posture, authenticity checks, lifecycle review, and lot-traceability framing
- `wiki/processes/pcba-npi-to-mass-production-flow.md`
  - strongest current reuse for where BOM review, sourcing, stencil, inspection, test, and traceability sit in the NPI-to-volume flow

## HDI Vocabulary And Boundary Support

- `facts/methods/hdi-microvia-and-vippo-process-posture.md`
  - usable for high-level HDI process vocabulary only: microvias, any-layer / build-up, VIPPO, sequential lamination posture
- `facts/standards/ecss-via-hdi-microvia-definitions.md`
  - usable for official definitions of blind via, buried via, HDI, and microvia
- `facts/standards/hdi-design-reference-status-metadata.md`
  - usable for current-vs-legacy IPC HDI reference hierarchy
- `facts/methods/microvia-reliability-public-context.md`
  - usable for cautionary reliability context, not for geometry, threshold, or cost tables

## Surface Finish Support Relevant To Cost-Driver Drafts

- `facts/standards/ipc-surface-finish-taxonomy-osp-hasl-extension.md`
  - usable for finish identity and taxonomy only
- `facts/methods/surface-finish-selection-for-rf.md`
- `wiki/processes/rf-surface-finish-selection.md`
  - usable for finish-selection logic and tradeoff framing, not for cost ranking or universal finish recommendations

## Prior Scout / Handoff Constraints Worth Preserving

- `logs/p4-40-2025-11-17-ceramic-power-basics-official-source-recovery-scout.md`
  - already marked `bom-cost.md` as blocked for percentages, savings, and sourcing-advantage claims
- `logs/p4-40-2025-11-27-service-cost-medical-rf-quickturn-official-source-recovery-scout.md`
  - already marked `hdi-pcb-cost.md` and `pcb-cost-reduction.md` as blocked for cost ordering, savings, and supplier optimization outcomes
- `logs/p4-44-blog-learning-continuation-handoff.md`
  - explicitly queued this lane as `official source evidence for cost drivers, not supplier quotes or current prices`

# Claim-Family Disposition

| Claim family | Status | Reusable now | Still blocked |
| --- | --- | --- | --- |
| `BOM cost` | `source_backed_fact_layer_partial_for_workflow_only` | BOM review, sourcing, lifecycle, authenticity, traceability, NPI-to-volume workflow context | component pricing posture, quote spread explanations, sourcing-power claims, panelization efficiency, overhead models, periodic savings, lead-time compression |
| `HDI cost` | `source_backed_fact_layer_partial_for_vocabulary_only` | official HDI / microvia terminology, sequential-build-up vocabulary, cautionary reliability context, finish taxonomy | cost hierarchy, via-cost ordering, lamination-cost multipliers, yield loss framing, supplier optimization claims, case-study savings, automotive radar proof |
| `PCB cost-reduction strategy` | `mostly_blocked_pending_official_or_dated_capability_evidence` | conservative DFM / DFA / stackup simplification vocabulary, avoid over-specifying material or HDI only when framed as general decision logic | panelization savings, finish cost ranking as universal truth, laminate substitution benefit claims, yield-driven savings, CAM optimization outcomes, sourcing leverage claims, stable production economics |

## BOM Cost

- The draft is strongest as buyer-question inventory: what belongs in a BOM, what part of the workflow touches sourcing, how NRE and assembly fit into fully loaded cost thinking.
- Existing `llm_wiki` support does not currently justify public claims about component-market dynamics, quote variance, sourcing leverage, or cost-reduction outcomes.
- Formula language such as `unit price x quantity` is generic arithmetic, but the draft's surrounding commercial claims are still unsupported unless tied to live pricing or dated internal quoting records.

## HDI Cost

- Existing support can explain what HDI is and why microvias, fine features, build-up, and inspection belong in a different process family from baseline multilayer work.
- Existing support does not establish a publishable public ranking of which HDI driver costs more, by how much, or when one stackup change reduces total cost.
- The draft's supplier-specific optimization story, `22%` case result, `FPY` posture, and scale-economy claims remain blocked.

## Cost-Reduction Strategy Language

- Existing support can back conservative language such as `review stackup early`, `reserve HDI or premium materials for real need`, `separate sourcing, assembly, and test planning`, and `keep finish choice tied to use case`.
- Existing support does not back the stronger article posture that these steps reliably reduce cost, increase yield, or improve production economics.
- `Panelization` appears in the corpus mainly as manufacturing-package or downstream process vocabulary, not as a source-backed savings lane.

# Safe Reuse Classes

- BOM / sourcing / traceability posture:
  BOM review, AVL review, authenticity, lifecycle review, lot traceability, staged release gates
- HDI term definitions:
  blind via, buried via, HDI, microvia, build-up, any-layer, VIPPO, sequential lamination
- Conservative engineering tradeoff language:
  higher density and extra process steps generally increase complexity; advanced builds need review; finish choice depends on assembly and use case
- Workflow framing:
  NPI, pilot, small-batch, mass production, inspection, test, and traceability as separate gates
- Finish taxonomy only:
  ENIG, ENEPIG, OSP, immersion silver, immersion tin, HASL identities
- Draft consumption only:
  heading inventory, claim-family mapping, source-gap discovery

# Blocked Claim Classes

- Prices, savings percentages, cost uplifts, margin language, or ROI claims
- Lead-time, MOQ, stock, supplier-availability, or sourcing-power claims
- Yield, FPY, scrap, rework, stable-mass-production, or quality-rate claims
- Supplier-specific capability marketing:
  `automated HDI lines`, `broad material database`, `global supply chain leverage`, `quality management that prevents hidden cost`
- Case-study outcomes:
  `22%` savings, `stable yield`, launch-deadline success, or customer competitiveness improvements
- Universal cost ordering:
  one finish always cheaper than another, one HDI topology always most cost-efficient, one material family always lowest-cost for the requirement
- Panelization savings or CAM-optimization outcomes without dated internal evidence
- Any claim that BOM hygiene, DFM, or HDI simplification by itself guarantees lower quote, lower total cost, or better yield

# Best Official-Source Or Dated Capability-Record Candidates Worth Recovering Next

## Highest-Value Official-Source Lanes

1. Official HDI standards-and-method lane
   - Purpose: strengthen public HDI cost-driver vocabulary without drifting into unsupported numbers
   - Best source classes:
     - IPC HDI design-standard metadata
     - IPC TM-650 method metadata for thermal / interconnect evaluation naming
     - NASA / IPC public microvia reliability and failure-mode records
   - Expected unlock:
     - better wording for why HDI carries extra process and reliability review burden
   - Still will not unlock:
     - pricing, yield, case-study savings, or supplier proof

2. Official build-up / sequential-lamination material-process lane
   - Purpose: recover primary-source support for HDI build-up material and sequential-lamination context
   - Best source classes:
     - official laminate-vendor technical notes and datasheets for build-up / sequential-lamination material systems
     - official material-owner notes that distinguish standard multilayer from HDI build-up handling
   - Expected unlock:
     - safer explanations of why repeated build-up and material choice add complexity
   - Still will not unlock:
     - public cost hierarchy or supplier optimization claims

3. Official finish taxonomy / finish-selection lane
   - Purpose: support cost-driver drafts where finish choice is mentioned, while keeping chemistry and use-case language correct
   - Best source classes:
     - IPC finish-standard metadata and official TOC identity records
     - finish-owner datasheets or process notes where use-case positioning is explicit
   - Expected unlock:
     - better finish identity and guarded use-case tradeoff language
   - Still will not unlock:
     - universal finish cost ranking, shelf-life tables, or yield outcomes

4. Official sourcing-governance lane for BOM posture
   - Purpose: strengthen BOM/sourcing language with primary-source traceability and counterfeit-control anchors rather than supplier prose
   - Best source classes:
     - IPC traceability metadata
     - official counterfeit-control / sourcing-governance standards metadata
     - official regulatory documentation-traceability anchors where relevant
   - Expected unlock:
     - stronger BOM review / sourcing-risk / traceability posture
   - Still will not unlock:
     - component price, availability, authorized-channel breadth, or lead-time claims

## Highest-Value Dated Capability-Record Lanes

5. Dated internal quoting / capability lane for BOM and PCB cost language
   - Needed if the business wants to publish:
     - quote-spread explanations
     - panelization efficiency claims
     - sourcing leverage claims
     - lead-time or MOQ statements
   - Required record shape:
     - dated owner, scope, board family, geography / factory scope, and refresh rule

6. Dated internal HDI capability-and-economics lane
   - Needed if the business wants to publish:
     - HDI topology cost comparisons
     - current microvia / lamination capability claims
     - FPY / yield posture
     - case-study savings or optimization stories
   - Required record shape:
     - dated process family, exact stackup scope, plant / line scope, and expiration rule

# Recommendation

- This lane is **not strong enough for immediate source-backed integration** as a cost article lane.
- It is strong enough only for narrow, conservative reuse of:
  - BOM sourcing / traceability posture
  - HDI definitions and process vocabulary
  - finish taxonomy and guarded tradeoff language
- It should remain **scout-only** until one of the two following things exists:
  - stronger official-source support for cost-driver mechanics beyond vocabulary, or
  - dated internal capability records for any supplier-specific cost, savings, yield, lead-time, or optimization claims

# Changed File

- `/code/blogs/llm_wiki/logs/p4-48c-hdi-bom-cost-driver-evidence-scout.md`
