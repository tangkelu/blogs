# P4-20 Layer-Count Claim Ingestion Contract

Date: 2026-04-27

## Purpose

This contract defines what it means to fully absorb the data from the 10 English layer-count PCB manufacturing blogs into `llm_wiki`.

The target content set is the layer-count article family:

- `6-layer-pcb-manufacturing`
- `8-layer-pcb-manufacturing`
- `10-layer-pcb-manufacturing`
- `12-layer-pcb-manufacturing`
- `14-layer-pcb-manufacturing`
- `16-layer-pcb-manufacturing`
- `18-layer-pcb-manufacturing`
- `20-layer-pcb-manufacturing`
- `22-layer-pcb-manufacturing`
- `24-layer-pcb-manufacturing`

Path names are not the authority for this task. Content-level claim coverage is the authority.

## Ingestion Definition

`Fully absorbed` does not mean every sentence or table from the blog family becomes a reusable fact.

`Fully absorbed` means every meaningful claim family in the blog family has one of these controlled dispositions:

- `source_scoped_fact`: may be consumed as a source-backed fact with exact `source_id`, conditions, and non-generalization rules.
- `public_site_claim`: may be consumed only as a page-scoped public-site or internal-site claim, not as independent factory proof.
- `workflow_context`: may be consumed as process, planning, validation, or review posture without hard numeric reuse.
- `architecture_example`: may be consumed as an example pattern, not as a default stack recipe or capability promise.
- `audited_but_blocked`: has been inventoried and governed, but cannot be used as a reusable numeric claim yet.
- `needs_source`: needs a better official, vendor, standards, or dated capability source before reuse.
- `reject_or_delete`: should not be stored as stable knowledge, usually because it is unsupported, dynamic commercial data, or a derived board-performance promise.

## Required Fields For Any Promoted Fact

Any future fact card created from this content set must include:

- `source_id`
- `fact_id`
- source type and source scope
- exact product, page, method, or program context
- numeric condition, frequency, test method, material grade, or page context where applicable
- allowed blog usage
- non-generalization rules
- refresh rule for public-site, internal-site, commercial, or revision-sensitive data

## Claim Families

### A: Material Numeric Claims

Examples:

- FR-4, high-Tg FR-4, halogen-free FR-4
- Rogers / PTFE / hydrocarbon-ceramic RF laminates
- Panasonic MEGTRON digital laminate families
- Isola, ITEQ, Shengyi, AGC, Ventec, Arlon exact-product material rows
- polyimide, LCP, FRCC, RCC, bondply, IMS / metal-core material rows

Promotion rule:

- Exact product values may be promoted only when tied to official manufacturer pages or datasheets.
- Generic family averages stay blocked.
- Cross-vendor tables must preserve test method, frequency, grade, and condition.

### B: Fabrication Capability Numeric Claims

Examples:

- trace / space
- drill and laser microvia diameter
- blind / buried via and VIPPO geometry
- aspect ratio
- annular ring
- backdrill tolerance and residual stub
- registration tolerance
- impedance tolerance
- board thickness windows
- copper weight
- stackup and sequential lamination count
- process windows such as bake, press, dwell, ramp, resin fill, plating buildup, and etch compensation

Promotion rule:

- Reusable capability numerics require a dated capability-source record or a deliberately scoped public-site claim card.
- Public-site values must remain `public_site_claim`.
- Recipe and process-window values remain blocked unless a named process-control source is accepted.

### C: Standards / Qualification / Acceptance Claims

Examples:

- IPC Class 2 / 3 / 3A thresholds
- IPC-6012 / IPC-6013 / IPC-A-600 thresholds
- IST cycles, coupon plans, microsection counts, plating minima
- FAI, lot conformance, QPL / QML, aerospace, defense, medical, space, or automotive qualification language
- outgassing, cleanliness, screening, acceptance, and release authority claims

Promotion rule:

- Public metadata may support hierarchy and vocabulary.
- Do not reconstruct paid-standard threshold tables from blog text.
- Do not turn standard names, TOCs, FAQs, or procurement clauses into supplier approval, accepted-lot, or release proof.

### D: High-Speed / SI / RF / Channel Claims

Examples:

- DDR4 / DDR5, PCIe, USB4, Ethernet, 56G, 112G, 224G, PAM4
- insertion loss, return loss, skew, timing, eye, BER, channel budget
- glass-weave skew, copper-roughness loss, via-stub resonance, backdrill frequency thresholds
- TDR / VNA frequency, S-parameter scope, validation package promises

Promotion rule:

- Interface sources may support system-context pressure only.
- Internal validation pages may support TDR/VNA workflow vocabulary only.
- Board-level SI budgets, pass/fail outcomes, and channel reach claims stay blocked unless tied to project-specific validated evidence.

### E: Reliability / HDI / Rigid-Flex / Build-Up Claims

Examples:

- stacked microvia reliability thresholds
- ELIC / any-layer HDI process claims
- bend radius, bend cycle, transition-zone tolerances
- rigid-flex architecture counts
- build-up material stack height, RCC/FRCC thickness, copper filling, dimple, planarization

Promotion rule:

- Architecture vocabulary and examples may be retained when clearly framed.
- Reliability thresholds, life-cycle numbers, and build-up process windows require primary source support.
- Material-form sources do not prove geometry freedom or manufacturability.

### F: Commercial / Operational Claims

Examples:

- cost uplift
- yield
- scrap cost
- lead time
- quick-turn
- production cadence
- MOQ, regional availability, supplier-status marketing

Promotion rule:

- Do not store as stable facts unless an explicit refresh-controlled business source exists.
- Default disposition is `reject_or_delete`.
- Rewrite as quote-stage or DFM-review variability when needed.

## Current Corpus Interpretation

The current `llm_wiki` corpus already has strong coverage for:

- exact-product material cards and material-family boundary controls
- layer-count numeric claim inventory
- material numeric coverage matrix and closeout
- fabrication capability bucket governance
- public-site parameter-scope cards
- high-speed system-context boundaries
- TDR / VNA / validation workflow vocabulary
- standards metadata and threshold-boundary cards
- conservative generation gate for the layer-count blog family

The current corpus does not yet unlock:

- old-blog numeric tables as-is
- generic FR-4 or generic low-loss laminate averages
- reusable factory capability tables
- IPC / IST / acceptance threshold tables
- high-speed channel budgets or board-loss tables
- HIL-specific supplier proof, process-control proof, yield proof, or lead-time promises

## Execution Rules

- Do not write or rewrite blogs during `P4-20`.
- Do not promote blog-originated numbers without source classification.
- Use existing `H0-H4`, `P4-06`, `P4-12`, `P4-13`, and `P4-19` controls before creating any new fact card.
- If a claim is already governed as blocked, do not create a duplicate fact card just to preserve the old blog number.
- If a claim is safe only as an example, store it as `architecture_example` or `workflow_context`, not as a stable parameter.

## Deliverables

- `logs/p4-20-layer-count-claim-coverage-map.md`
- optional follow-on source recovery tasks only for claim families that remain high-value and genuinely sourceable
- optional fact cards only for claim families that have source-grade support and are not already covered by existing cards

## Completion Condition

`P4-20` is complete when every major claim family from the 10 layer-count blogs is mapped to:

- a supporting fact/source/log path,
- a blocked/gap reason,
- or a reject/delete rule.

This is a data-governance completion condition, not a high-density numeric reuse unlock.
