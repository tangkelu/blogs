# P4-12 Long-Task Plan

Date: 2026-04-25

## Goal

Keep `P4-12 Layer-Count Blog Numeric Source Supplementation` in controlled execution until `20-layer` and `22-layer` are no longer blocked by weak public source support, while explicitly preventing premature entry into `P4-06`.

## Why This Plan Exists

`6 / 8 / 10 / 12 / 14 / 16 / 18 / 24-layer` are already at `mostly_ready` for conservative rewrite support. The remaining long-tail risk is concentrated in:

- `20-layer` any-layer / build-up / `IST` / geometry / capability claims
- `22-layer` hi-rel standards / addendum / workflow / qualification / acceptance claims

Recent batches already improved guarded rewrite support materially. The remaining work now requires a long-task structure because:

- the remaining gaps are narrower but higher-risk
- they benefit from multi-agent parallel discovery
- they must be filtered through strict non-claim boundaries before being added to `llm_wiki`

## Non-Negotiable Boundaries

- Do not edit blog source files under `/code/hileap/frontendHIL/docs/`.
- Do not start `P4-06` while `20-layer` or `22-layer` remain `needs_sources`.
- Do not use MCP.
- Do not use third-party datasheet mirrors for Taconic, unresolved Arlon, or any other weak parameter recovery.
- Do not convert public metadata pages into threshold tables, acceptance criteria, or supplier-status claims.
- Do not let sub-agents edit `logs/backlog.md`, `logs/phase-status.md`, or `logs/update-log.md`.

## Current Readiness Baseline

- `20-layer`: still blocked by `ELIC` defaults, geometry tables, `IST` thresholds, process-window claims, and factory-capability claims
- `22-layer`: still blocked by `Class 3/3A` threshold tables, qualification/acceptance flows, supplier-status claims, and program-specific acceptance numbers

## Long-Task Workstreams

### Workstream A: 22-Layer Public Hi-Rel Acceptance Hierarchy

Objective:

- strengthen guarded wording for `22-layer` by expanding official public metadata around rigid-board hi-rel program layers, audit ecosystems, verification ecosystems, and addendum boundaries

Can improve:

- `FAI` workflow phrasing
- verification / documentation / audit ecosystem phrasing
- addendum hierarchy phrasing
- contract- or procurement-triggered standards wording

Cannot improve directly:

- `Class 2 / 3 / 3A` numeric tables
- acceptance thresholds
- sample sizes
- supplier qualification status

Priority source classes:

- `IPC-6012` family/addendum product pages and TOCs
- IAQG / SAE workflow pages
- IAQG verification / certification ecosystem pages
- IPC Validation Services metadata when clearly official and process-governance oriented

### Workstream B: 22-Layer High-Layer Manufacturability Context

Objective:

- strengthen guarded wording that high-layer rigid-board work becomes more lamination-, dimensional-control-, and registration-sensitive as complexity rises

Can improve:

- manufacturability framing
- process-sensitivity framing
- material-family suitability framing

Cannot improve directly:

- board-thickness rules
- aspect-ratio numbers
- hole sizes
- registration tolerances
- capability tables

Priority source classes:

- official laminate process guides
- official family pages explicitly mentioning `HDI`, `very high layer count`, sequential lamination, dimensional stability, or multilayer process sensitivity
- official standards release pages referencing current fabrication complexity themes

### Workstream C: 20-Layer Public Build-Up / Reliability Context

Objective:

- continue strengthening guarded `20-layer` wording without rehabilitating geometry tables or `IST` thresholds

Can improve:

- `IST` method vocabulary
- build-up / material-form vocabulary
- reliability-caution framing
- current-vs-legacy HDI reference framing

Cannot improve directly:

- lamination counts
- microvia geometry
- stacked-height limits
- `200 / 300+` cycle thresholds
- cost/yield/lead-time tables

Priority source classes:

- official IPC report metadata
- official build-up/material family positioning pages
- public microvia reliability papers and method indexes

### Workstream D: Readiness Governance And Exit Control

Objective:

- keep the workstream honest by updating guardrails and readiness wording whenever a new source class lands

Deliverables:

- guardrail fact updates
- readiness-log clarifications
- explicit non-claims
- phase/backlog/update-log sync

## Multi-Agent Execution Pattern

For each batch:

1. Main agent defines `2-3` independent source-hunting tasks.
2. Each sub-agent receives one narrow source class only.
3. Sub-agent returns:
   - candidate official URLs
   - safe metadata contribution
   - non-claims
4. Main agent filters candidates.
5. Main agent writes source records and fact updates.
6. Main agent updates logs and counts.

## Planned Batches

### Batch L1: Audit / Validation Ecosystem Follow-On

Primary workstream:

- Workstream A

Target outputs:

- `1-3` official source records for aerospace audit/validation ecosystem metadata
- `0-1` fact update for `fai-and-aerospace-quality-workflow-metadata`
- optional `22-layer` guardrail update if wording range expands safely

Success criterion:

- `22-layer` can more safely mention audit/verification ecosystem context without implying certification or qualification

### Batch L2: Cross-Vendor High-Layer Process Corroboration

Primary workstream:

- Workstream B

Target outputs:

- `1-3` official supplier-side process or family-positioning source records from vendors beyond current single-source dependence
- `0-1` fact update for `high-layer-rigid-board-manufacturability-context`

Success criterion:

- high-layer manufacturability context is supported by at least two independent official supplier-side layers plus IPC release context

### Batch L3: 20-Layer Reliability Vocabulary Tightening

Primary workstream:

- Workstream C

Target outputs:

- `1-2` official method/report metadata records or fact updates that strengthen `IST` / microvia-reliability naming without unlocking thresholds
- optional update to `20-layer-any-layer-hdi-rewrite-guardrail`

Success criterion:

- `20-layer` has stronger method vocabulary and clearer non-claims, even if readiness status does not change

### Batch L4: Reassessment Gate

Primary workstream:

- Workstream D

Target outputs:

- refresh `logs/layer-count-blog-readiness.md`
- decide whether `20-layer` and/or `22-layer` remain `needs_sources`
- document why `P4-06` still stays blocked or what exact prerequisites were satisfied

Success criterion:

- readiness state is explicitly justified from the current evidence layer, not from optimism

## Batch Status Update

- `Batch L1`: executed
- `Batch L2`: executed
- `Batch L3`: executed
- `Batch L4`: executed
- Follow-on after `L4`: one additional high-value `20-layer` source landed from reassessment follow-up
  - accepted: official Isola `Sequential Lamination in PCBs` note
  - deferred at that time: `AGC fastRise` and IPC Validation Services FAQ until a later narrow-source reassessment

## Current Post-L4 Position

- `20-layer` gained stronger official sequential-lamination stress-factor / failure-mode vocabulary
- `22-layer` did not gain a materially new public hi-rel governance layer in this follow-on
- overall readiness verdict remains unchanged:
  - `20-layer`: `needs_sources`
  - `22-layer`: `needs_sources`
  - `P4-06` remains blocked

## Additional Follow-On After Post-L4 Review

- accepted:
  - official IPC Validation Services FAQ
  - official IPC Standards Gap Analysis page
  - official Panasonic `MEGTRON M` product page
- rejected for now:
  - Panasonic `MEGTRON2` page, because this round did not need two adjacent Panasonic additions with similar `high multilayer` / `IST` framing
  - IPC Validation Services Technology Solutions page, because it added less ceiling than the FAQ plus SGA pair

## Updated Position After Additional Follow-On

- `22-layer` now has a clearer public hierarchy for `qualification listing`, `site-specific scope`, and `pre-qualification assessment` wording
- `20-layer` and adjacent high-layer digital-material framing now have one more official Panasonic product-grade anchor with condition-bound values plus `high multilayer` / `IST` context
- `20-layer` reliability wording now also has a broader public `inspection` / `defect-criteria` / `interconnect-quality` governance anchor through NASA workmanship metadata
- readiness verdict still remains unchanged:
  - `20-layer`: `needs_sources`
  - `22-layer`: `needs_sources`
  - `P4-06` remains blocked

## Additional Reliability-And-Governance Follow-On

- accepted:
  - official NASA `NEPP` 2019 program-overview page
  - official Mitsui engineered-materials `RCC` page
  - official `AS9100D` `QMS` requirements page
  - official `AS9101G` audit-requirements page
  - official `AS9131D` nonconformity-reporting page
- rejected for now:
  - ECSS glossary pages for `inspection` and `qualification test`, because they add less usable rewrite ceiling than the NASA and `AS9101G` governance layers and are easier to overread as generic definitions
  - additional adjacent product pages that repeat build-up or hi-rel marketing posture without adding a new governance boundary

## Updated Position After Reliability-And-Governance Follow-On

- `20-layer` now has a clearer public assurance hierarchy for `screening`, `qualification`, `test`, and `reliable use`, but this remains vocabulary-safe rather than qualification-flow-safe
- `20-layer` material framing now has a direct official `RCC` material-form anchor from Mitsui, but this remains vocabulary-safe rather than process-window-safe
- `22-layer` now has a clearer public baseline-`QMS` and customer/regulatory-precedence layer through `AS9100D`, but this remains governance-safe rather than certification- or approval-safe
- `22-layer` now has a clearer public audit-process layer through `AS9101G`, but this remains governance-safe rather than supplier-status-safe
- `22-layer` now has a clearer public contract-driven nonconformity-reporting layer through `AS9131D`, but this remains governance-safe rather than waiver-, disposition-, or release-authority-safe
- readiness verdict still remains unchanged:
  - `20-layer`: `needs_sources`
  - `22-layer`: `needs_sources`
  - `P4-06` remains blocked

## Batch L5

- accepted:
  - official IPC `TM-650 2.6.26A` method page
  - official IPC `TM-650 2.6.27B` method page
  - official IPC `TM-650 2.6.7.2C` method page
  - official AGC `fastRise` family page
  - official AGC `Bond Plies / Prepregs` page
  - official IPC `6012` addendum taxonomy page
- effect:
  - `20-layer` now has stronger named official method vocabulary for `D.C. current induced thermal cycling`, `convection reflow assembly simulation`, `thermal shock`, `continuity`, and representative-coupon context
  - `20-layer` now has stronger named official material-form vocabulary for `bond ply`, `prepreg`, `nonreinforced` bonding layers, `sequential lamination`, and `stacked or staggered microvias`
  - `22-layer` now has a cleaner public hierarchy for base rigid-board framing versus current `medical`, `space/military`, and `automotive` addendum branches
- verdict:
  - `20-layer`: still `needs_sources`
  - `22-layer`: still `needs_sources`
  - `P4-06` remains blocked

## L11 Long-Task Batch

- accepted:
  - official `MIL-PRF-31032/1E` rigid-multilayer specification-sheet detail page
  - official `IPC-6012FA` product page
  - official `IPC-6012FA` TOC
  - official Shengyi `S7439 / S7439B` processing guide
- effect:
  - `22-layer` now has a cleaner public sheet-level military hierarchy for the rigid multilayer thermosetting-resin branch under `MIL-PRF-31032`
  - `22-layer` now has a cleaner current automotive addendum hierarchy with procurement-trigger and clause-family visibility through `IPC-6012FA`
  - `20-layer` now has one more mainstream supplier-side handling / lay-up / drilling / desmear-sensitivity anchor through Shengyi process guidance
- guardrail:
  - do not turn `MIL-PRF-31032/1E` sheet identity into qualification flow, current listing status, or acceptance authority
  - do not turn `IPC-6012FA` product or TOC wording into automotive thresholds, supplier compliance, or program acceptance
  - do not turn Shengyi process guidance into bake schedules, press cycles, drill tables, or capability claims
- verdict:
  - `20-layer`: still `needs_sources`
  - `22-layer`: still `needs_sources`
  - `P4-06` remains blocked

## L12 Long-Task Batch

- accepted:
  - official TUC `ThunderClad 5Q` product page
- deferred:
  - Nan Ya `NPG-199K`, because the current environment still does not provide a clean certificate-valid download path for stable primary extraction
- effect:
  - `20-layer` now has one more official non-Isola very-low-loss product-grade anchor with explicit `high layer count circuit board design` positioning and condition-bound values
- guardrail:
  - do not turn TUC `high layer count` wording or page-backed values into stack recipes, qualification evidence, or factory-capability claims
- verdict:
  - `20-layer`: still `needs_sources`
  - `22-layer`: still `needs_sources`
  - `P4-06` remains blocked

## L6 Scouting Result

- `20-layer` branch:
  - no new source landed
  - best remaining public candidates were mostly overlapping method/governance pages or unstable vendor/government endpoints
  - current blockers remain unsupported `IST` thresholds, geometry/process tables, coupon/qualification plans, and factory-capability claims
- `22-layer` branch:
  - no new source landed
  - exploratory candidates such as additional certification-governance or procurement-surveillance pages may still improve wording precision, but none were strong and stable enough in this pass to justify a new accepted batch
  - current blockers remain unsupported `Class 3/3A` thresholds, addendum acceptance details, qualification-flow reconstruction, and supplier-status/capability claims

## L6b Narrow Follow-On

- accepted:
  - official IPC `QPL IPC-4101` page
  - official `FAR 44.303 Extent of review` page
- effect:
  - `20-layer` now has a clearer public boundary that qualification-listing vocabulary can apply to certified base materials and listed products/sites without qualifying a finished board
  - `22-layer` now has a clearer public procurement-governance layer for `purchasing-system review`, `subcontractor responsibility`, `postaward management`, and `higher-level quality-standards review`
- verdict:
  - `20-layer`: still `needs_sources`
  - `22-layer`: still `needs_sources`
  - `P4-06` remains blocked

## L6c Narrow Follow-On

- accepted:
  - official IPC `QPL IPC-4103` page
  - official IPC `QML IPC-1791` page
- rejected for now:
  - official `J-STD-001S` Space/Military Addendum `QML` page, because this round did not need one more assembly-process listing page with lower marginal ceiling than the organization-level `IPC-1791` boundary
- effect:
  - `20-layer` now has a clearer public boundary that qualification-listing vocabulary can also attach to high-speed/high-frequency base materials and bonding-layer products/sites without qualifying a finished board
  - `22-layer` now has a clearer public boundary that `QML` can sit at the organization and role level for trusted designers, fabricators, and assemblers without granting supplier approval or release authority
- verdict:
  - `20-layer`: still `needs_sources`
  - `22-layer`: still `needs_sources`
  - `P4-06` remains blocked

## L6d Narrow Follow-On

- accepted:
  - official `J-STD-001S` Space/Military Addendum `QML` page
- effect:
  - `22-layer` now has a clearer public boundary that some IPC `QML` listings can sit at the `EMS/OEM assembly-process` layer under `J-STD-001S`, which should stay separate from organization-level trusted-source `QML` and from bare-board qualification framing
- verdict:
  - `20-layer`: still `needs_sources`
  - `22-layer`: still `needs_sources`
  - `P4-06` remains blocked

## L6e Narrow Follow-On

- accepted:
  - official `IPC-A-600K` TOC
  - official `IPC-6011A` TOC
- deferred:
  - official `MIL-PRF-55110` page, because this round did not need to land a network-unstable legacy military-spec page without clean direct verification
- effect:
  - `22-layer` now has a clearer public bare-board acceptability boundary through `IPC-A-600K`, distinct from assembly acceptability
  - `22-layer` now has a clearer public `IPC-601X` generic printed-board hierarchy through `IPC-6011A`, distinct from sectional/addendum rigid-board claims
- verdict:
  - `20-layer`: still `needs_sources`
  - `22-layer`: still `needs_sources`
  - `P4-06` remains blocked

## L6f Narrow Reassessment

- evaluated:
  - official `MIL-PRF-55110` page
  - official IPC shop pages for `IPC-9691`, `IPC-4121`, and `IPC-9241`
- accepted:
  - none
- deferred:
  - official `MIL-PRF-55110` page, because this round still did not produce clean direct public text extraction beyond unstable network access
  - official IPC shop pages for `IPC-9691`, `IPC-4121`, and `IPC-9241`, because current public access returned `403` and did not support clean primary verification
- effect:
  - current candidate set reinforced the next-search direction toward equally official but more publicly retrievable `20-layer` method/material-boundary pages and `22-layer` military-program hierarchy pages
- verdict:
  - `20-layer`: still `needs_sources`
  - `22-layer`: still `needs_sources`
  - `P4-06` remains blocked

## L7 Long-Task Batch

- accepted:
  - official NASA `PCB Inspection and Quality Control` NTRS record
  - official NASA `A Physics of Failure Approach to Evaluate Printed Circuit Board Reliability` NTRS record
  - official Isola `IS410` processing guide
  - official DLA `QML/QPL/QBL` listing page
- effect:
  - `20-layer` now has stronger public inspection / specimen-preparation / failure-analysis / physics-of-failure vocabulary plus a clearer mainstream rigid `laminate / prepreg` process boundary
  - `22-layer` now has a clearer public government-side qualification-listing hierarchy separating governing specifications, pre-acquisition qualification, and listing visibility
- verdict:
  - `20-layer`: still `needs_sources`
  - `22-layer`: still `needs_sources`
  - `P4-06` remains blocked

## L8 Long-Task Reassessment

- evaluated:
  - official `MIL-PRF-55110` ASSIST detail page
  - official `MIL-PRF-31032` specification-sheet detail page for rigid multilayer thermosetting-resin boards
- accepted:
  - none
- deferred:
  - official `MIL-PRF-55110` ASSIST detail page, because this round still did not yield clean primary text extraction from the current network path
  - official `MIL-PRF-31032` specification-sheet detail page, because this round still did not yield clean primary text extraction from the current network path
- effect:
  - current candidate review confirms these are still high-value targets for `22-layer`, but they remain outside the corpus until clean direct verification is available
- verdict:
  - `20-layer`: still `needs_sources`
  - `22-layer`: still `needs_sources`
  - `P4-06` remains blocked

## L9 Long-Task Batch

- accepted:
  - official AGC `Meteorwave 1000NF` page
  - official Rogers `2929 Bondply` datasheet
- reused and extended:
  - official AGC `Bond Plies / Prepregs` page
- effect:
  - `20-layer` now has a clearer public material-form boundary for `bond ply`, `no-flow prepreg`, and `unreinforced bondply` in high-layer constructions
- verdict:
  - `20-layer`: still `needs_sources`
  - `22-layer`: still `needs_sources`
  - `P4-06` remains blocked

## L10 Long-Task Batch

- accepted:
  - official Ventec `VT-47LT` datasheet page
- deferred:
  - official `MIL-PRF-55110` page, because this round still did not produce clean direct public text extraction from the current network path
  - official `MIL-PRF-31032/1E` rigid-multilayer specification-sheet PDF, because this round still did not produce clean direct public text extraction from the current network path
- effect:
  - `20-layer` now has a cleaner official prepreg-side boundary that `Any-layer HDI Designs`, `Sequential Laminations`, and `High Reliability for HDI Designs` can appear together on one material page without making those phrases reusable stack recipes, qualification proof, or capability claims
- verdict:
  - `20-layer`: still `needs_sources`
  - `22-layer`: still `needs_sources`
  - `P4-06` remains blocked

## L11 Long-Task Batch

- accepted:
  - official `DFARS 252.246-7008` clause page
  - official `DLAD 46.291` page
  - official `FAR 52.246-11` clause page
- effect:
  - `22-layer` now has a clearer public procurement-governance layer for preferred source hierarchy, risk-based traceability, record availability, contract-listed higher-level quality standards, subcontract flowdown, and production-lot-testing wording
  - these additions strengthen guarded contract/governance phrasing only; they still do not unlock supplier approval, contract invocation proof, acceptance authority, or PCB-specific threshold evidence
- verdict:
  - `20-layer`: still `needs_sources`
  - `22-layer`: still `needs_sources`
  - `P4-06` remains blocked

## Exit Conditions For P4-12

`P4-12` may be considered complete only when all of the following are true:

1. `20-layer` and `22-layer` no longer rely on unsupported threshold tables or capability tables for their conservative rewrite support verdict.
2. Their guardrail cards clearly separate safe wording from excluded claim classes.
3. `logs/layer-count-blog-readiness.md` explicitly records a new verdict that can survive evidence-pack consumption.
4. Main logs are synchronized:
   - `logs/backlog.md`
   - `logs/phase-status.md`
   - `logs/update-log.md`

## Hard Stop Conditions

Stop and do not advance to `P4-06` if any of the following remains true:

- `20-layer` still depends on geometry/process/capability tables for article structure
- `22-layer` still depends on public-threshold reconstruction for hi-rel authority
- new sources are only marketing claims without official standards/process context
- the only way to preserve a draft section would be to infer supplier qualification or capability

## Current Execution State

- `Batch L1` executed: official IAQG certification-governance and IPC validation-services ecosystem anchors selected to strengthen guarded `22-layer` audit/verification wording without implying supplier status.
- `Batch L2` executed: official Ventec process-guide corroboration selected to strengthen cross-vendor high-layer manufacturability context beyond current Isola and Panasonic anchors.
- `Batch L3` executed: `IST` / `TM-650` wording is now more explicitly tied to named public method/report context, method-development governance, and representative coupon-evaluation context rather than thresholds.
- Latest `20-layer` follow-on tightened material-form intake boundaries across `FRCC`, `RCC`, `bond ply`, `controlled-flow prepreg`, `no-flow prepreg`, ultrathin build-up, and prepreg-side `any-layer HDI` wording; this is prompt-safety tightening at the vocabulary boundary only, not a readiness upgrade.
- Latest follow-on also accepted the historical `IPC/JPCA-4104` TOC, official Ventec `VT-464LT RCC`, and official `AT&S` `Anylayer` page; these additions tighten taxonomy, `RCC/bondply`, and architecture vocabulary boundaries only, not readiness.
- Latest material-branch follow-on also accepted AGC `N7000-3F`, ITEQ `IT-602G`, and Rogers `RO4835T / RO4450T` anchors; these improve product-grade material numerics and named-construction process context, but still do not change readiness.
- Latest hi-rel follow-on also accepted the official `MIL-PRF-55110` ASSIST detail page as a legacy rigid-board military-spec identity / scope / inactive-status anchor only; this tightens legacy-vs-current specification framing, not qualification or readiness.
- Latest high-speed follow-on also accepted official JEDEC `DDR5` release-chronology anchors via `Business Wire` plus official `OIF CEI-112G` and `TE 112G` ecosystem pages; these broaden system-context and interconnect vocabulary only, not channel-budget or capability evidence.
- Latest hierarchy/process follow-on also accepted official `MIL-PRF-31032/1E`, official `IPC-6012FA` product-page / TOC metadata, and official Shengyi `S7439 / S7439B` processing guidance; these tighten military sheet hierarchy, automotive addendum hierarchy, and mainstream supplier-side process sensitivity only, not readiness.
- Latest material follow-on also accepted official TUC `ThunderClad 5Q` product-page coverage; this tightens the product-grade very-low-loss / high-layer-count material ladder only, not readiness.
- Latest procurement-governance follow-on also accepted official `DFARS 252.246-7008`, `DLAD 46.291`, and `FAR 52.246-11`; these tighten source-hierarchy, contract-quality-flowdown, and `production lot testing` vocabulary only, not readiness.

## Immediate Next Move

Continue narrow official-source hunting in long-task mode. Prioritize only source classes that could materially change blocked verdicts for `20-layer` or `22-layer`; keep `P4-06` blocked unless readiness evidence materially changes.
