# P4-125 Knowledge-Base Distance And Subagent Roadmap

Date: 2026-05-02

## Purpose

Assess how far `llm_wiki` still is from the PCB / PCBA true-data knowledge-base target, then convert the remaining work into bounded subagent lanes that continue source-backed promotion rather than rewrite expansion.

This pass does not reopen broad draft rewriting, held numerics, or readiness unlocks.

## Assessment Baseline

Current local corpus size:

- `sources/registry/`: `705` files
- `facts/`: `402` files
- `wiki/`: `90` files
- dated English `tmps/*/en` folders: `31`

Current controller posture:

- `P4-121` remains the active mainline for `P4-06` Phase 5 Batch 1 prompt handoff only
- residual `2026.4.27/en` and `2026.4.29/en` scans do not currently expose a stronger exact non-held lane
- several topic families are prompt-consumable or claim-family-complete, but not source-backed complete

## Maturity Estimate

Overall maturity: `medium`

Component view:

- materials: `high`
- standards / process governance: `medium`
- batch closure and fact-layer completeness: `medium`

Interpretation:

- the corpus is already broad and reusable
- the remaining gap is no longer basic coverage
- the remaining gap is depth, refresh discipline, and closure of partial / held lanes

## What Is Already Strong

### Materials

- strong exact-product coverage across major laminate families such as Rogers, Isola, Panasonic, Ventec, AGC, Kingboard, Arlon, UBE, and DuPont
- good class-versus-product guardrails for ABF / BT, flex PI / LCP, ceramic / AlN / IMS, and copper-foil boundary pages

### Standards And Process Governance

- strong public metadata posture for IPC hierarchy, USB taxonomy, aviation / military subsets, and guarded medical / FDA vocabulary
- good process-boundary coverage for DFM / DFT / DFA staging, NPI / FAI / inspection flow, test-method separation, and release-authority limits

### Closure And Reuse

- all current English `tmps/*/en` folders are deletion-safe at claim-family or routing level
- the `2026.4.29/en` expert batch now has broad narrow-lane reuse across smart-meter, EV charger, hearing aid, satellite, neuromorphic, LiDAR, inverter, FPGA, audio, gaming, and endoscope subsets

## Remaining Distance To Target

### 1. Materials Source-Depth Gaps

Top recoverable gaps:

- Taconic exact-product RF laminate datasheet and product-page anchors remain missing
- more Arlon RF / PTFE family coverage is still missing, especially `CLTE-XT`, `TC350`, `AD250 / AD255 / AD300`, `CuClad`, and `DiClad`
- flex-material numeric support remains uneven for generic polyimide / `Kapton` / `UPILEX` / adhesiveless-flex claims
- ceramic / AlN / IMS / LTCC / DBC / AMB product-level datasheets are still sparse
- copper-foil roughness and foil-profile exact-grade coverage is still thinner than the laminate layer

Hold boundary:

- finished-board performance, stock, lead time, qualification, and fabrication-capability claims remain blocked unless backed by stronger dated evidence

### 2. Standards And Process-Governance Gaps

Top recoverable or partially recoverable gaps:

- revision refresh is uneven across IPC / SAE / FDA / DLA / related public metadata families
- finish governance remains metadata-rich but process-thin
- end-to-end inspection, screening, qualification, and release-governance cards are still not complete enough
- supplier qualification / listing / release-authority vocabulary is bounded, but not deeply mapped by program type
- some exact clause or threshold classes remain structurally limited by paid standards rather than open official metadata

Hold boundary:

- public metadata can support hierarchy, revision, and guarded vocabulary
- it cannot substitute for paid threshold tables, acceptance criteria, or clause text

### 3. Closure And Fact-Layer Completeness Gaps

Top closure gaps:

- `2026.4.27/en` still contains many partial lanes where identity and context are landed but numerics, performance, mission proof, and supplier-proof claims remain blocked
- `2026.4.29/en` is deletion-safe and widely reusable, but not source-backed complete; `biological-computing` remains explicit hold-only, and `dna-computing` remains strip-first rather than fact-complete
- `HILPCB Blog1-13` input-device drafts are still governed mostly at claim-family level, with keyboard / mouse / MIDI / rugged / wireless / compliance / HIL-capability claims unresolved
- `APTPCB260401` `2-layer` drafts still lack source-backed closure for numerics, material values, impedance / thermal calculations, finish chemistry, cost, lead time, supplier proof, and APT capability proof
- `20-layer`, `22-layer`, `quantum-computing`, and `biological-computing` remain important but hold-only unless exact new authority appears

## Long-Task Roadmap

### Mainline Still Active

Keep `P4-121` active and unchanged:

- finish `P4-06` Phase 5 Batch 1 prompt handoff for `6-layer`, `8-layer`, and `10-layer`
- do not reopen `20-layer` / `22-layer`
- do not treat prompt handoff as source-backed completion

### Next Source-Backed Queue After P4-121

#### Lane A: Taconic And Arlon RF / PTFE Recovery

Goal:

- recover current official product pages and datasheets for missing Taconic and Arlon RF laminate families

Subagent split:

- lane A1: Taconic source-registry scout and exact-product candidate list
- lane A2: Arlon RF / PTFE family gap map and exact-product candidate list
- main agent: final source acceptance, fact-card integration, and tracker updates

Expected promotion targets:

- `sources/registry/materials/`
- material exact-product fact cards
- possibly one material aggregation update if enough exact-product anchors land

#### Lane B: Flex / Copper-Foil / Ceramic-Platform Recovery

Goal:

- deepen fabrication-material coverage where class-level anchors already exist but exact-grade or exact-product depth is thin

Subagent split:

- lane B1: flex PI / LCP / adhesiveless-flex source-gap narrowing
- lane B2: copper-foil roughness / profile exact-grade recovery map
- lane B3: ceramic / IMS / LTCC / DBC / AMB product-source shortlist
- main agent: decide which branches merit source promotion versus continued hold

#### Lane C: Standards Metadata Refresh Sweep

Goal:

- tighten refresh-sensitive public metadata across standards and regulatory source families

Subagent split:

- lane C1: IPC / finish / addendum refresh sweep
- lane C2: SAE / FAA / FDA / DLA / military metadata refresh sweep
- main agent: accept refreshed source records and update dependent fact cards only where current status changes

#### Lane D: Process-Governance Gap Map

Goal:

- close the remaining process-governance gaps around inspection, screening, qualification boundaries, traceability, and release staging

Subagent split:

- lane D1: inspection / test / screening boundary map
- lane D2: qualification / listing / release-authority boundary map
- main agent: consolidate into reusable fact cards and one or more process wiki updates

#### Lane E: Closure Controller Pass

Goal:

- convert the most valuable `claim-family` or `partial` batches into an explicit source-recovery queue instead of leaving them mixed together

Priority closure families:

- `HILPCB Blog1-13` input-device subset
- `APTPCB260401` `2-layer` subset
- residual `2026.4.27/en` partial lanes that still lack their own reusable fact/wiki layer

Main-agent-only decisions:

- whether a family should move into source recovery now
- whether it should stay tracker-only
- whether it belongs in explicit hold maintenance

## Recommended Batch Order

1. finish `P4-121`
2. `Lane A` Taconic / Arlon RF-PTFE recovery
3. `Lane C` standards metadata refresh
4. `Lane D` process-governance gap map
5. `Lane B` flex / copper-foil / ceramic-platform recovery
6. `Lane E` closure controller pass for claim-family-only families

## Stop Conditions

Stop and record `distance unchanged` if a lane:

- only improves rewrite readiness without adding `sources/`, `facts/`, or `wiki/`
- tries to recover paid-standard thresholds from metadata-only pages
- turns public marketing copy into qualification, supplier-proof, or readiness proof
- reopens explicit hold lanes without exact new authority

## Status

- controller status: `long_task_ranked`
- overall maturity: `medium`
- current mainline unchanged: `P4-121`
- next source-backed queue:
  - `Taconic / Arlon RF-PTFE recovery`
  - `standards metadata refresh`
  - `process-governance gap map`
  - `flex / copper-foil / ceramic-platform recovery`
  - `closure controller pass`
