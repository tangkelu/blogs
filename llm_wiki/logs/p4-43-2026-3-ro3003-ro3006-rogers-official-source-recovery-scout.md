## P4-43 Official-Source Recovery Scout

Date: 2026-04-28
Lane: `P4-43 official-source recovery scout`
Model: `gpt-5.4`
Scope: `/code/blogs/tmps/2026.3/en`
Output: `/code/blogs/llm_wiki/logs/p4-43-2026-3-ro3003-ro3006-rogers-official-source-recovery-scout.md`
Status: `completed_at_claim_family_level`

## Workflow Notes

- Read `/root/.codex/skills/llm-wiki-workflow/SKILL.md` and followed its draft-handling and deletion-safe logging rules.
- Treated `tmps` drafts as claim inventory only, not authority.
- Did not update trackers, reusable facts, source registry, or wiki pages.
- Did not edit any file outside this assigned log path.

## Input Inventory

Input directory inventory under `/code/blogs/tmps/2026.3/en` at time of scout:

- `ro3003-pcb-cost.md`

Primary draft theme:

- RO3003 cost framing
- hybrid RO3003 + FR-4 stackup as a savings story
- supplier/process/capability assertions
- prototype / quote / volume / quick-turn / stocking framing
- impedance / RF validation / PTFE process assertions embedded as cost justifications

## Existing Support Checked

### Exact-product and family support already present

- `materials-rogers-ro3003` at `/code/blogs/llm_wiki/facts/materials/rogers-ro3003.md`
- `materials-rogers-ro3006` at `/code/blogs/llm_wiki/facts/materials/rogers-ro3006.md`
- `materials-rogers-ro3003-vs-ro3006` at `/code/blogs/llm_wiki/facts/materials/rogers-ro3003-vs-ro3006.md`
- `materials-rogers-ro3003-vs-ro3006-vs-ro3010-vs-ro3035` at `/code/blogs/llm_wiki/facts/materials/rogers-ro3003-vs-ro3006-vs-ro3010-vs-ro3035.md`
- `materials-rogers-material-selector` at `/code/blogs/llm_wiki/facts/materials/rogers-material-selector.md`
- `materials-rf-selector-by-application` at `/code/blogs/llm_wiki/facts/materials/rf-material-selector-by-application.md`
- `materials-rf-selector-by-application-band` at `/code/blogs/llm_wiki/wiki/materials/rf-material-selector-by-application-band.md`
- `materials-rogers-ro3000-family` at `/code/blogs/llm_wiki/wiki/materials/rogers-ro3000-family.md`

### Rogers official source records already present

- `rogers-ro3000-datasheet` at `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro3000-datasheet.md`
- `rogers-ro3000-series-product-page` at `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro3000-series-product-page.md`
- `rogers-ro3003-product-page` at `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro3003-product-page.md`
- `rogers-ro3006-product-page` at `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro3006-product-page.md`
- `rogers-ro3000-fabrication-guidelines` at `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro3000-fabrication-guidelines.md`

### PTFE, stackup, impedance, and RF validation support already present

- `methods-hybrid-rf-stackup-capability` at `/code/blogs/llm_wiki/facts/methods/hybrid-rf-stackup-capability.md`
- `processes-hybrid-rf-stackup-strategy` at `/code/blogs/llm_wiki/wiki/processes/hybrid-rf-stackup-strategy.md`
- `methods-ptfe-processing-capability` at `/code/blogs/llm_wiki/facts/methods/ptfe-processing-capability.md`
- `processes-ptfe-processing-and-manufacturability` at `/code/blogs/llm_wiki/wiki/processes/ptfe-processing-and-manufacturability.md`
- `methods-controlled-impedance-tdr-verification-posture` at `/code/blogs/llm_wiki/facts/methods/controlled-impedance-tdr-verification-posture.md`
- `methods-pcb-impedance-and-rf-measurement-method-boundary` at `/code/blogs/llm_wiki/facts/methods/pcb-impedance-and-rf-measurement-method-boundary.md`
- `methods-rf-validation-capability` at `/code/blogs/llm_wiki/facts/methods/rf-validation-capability.md`
- `testing-rf-validation-and-test-coverage` at `/code/blogs/llm_wiki/wiki/testing/rf-validation-and-test-coverage.md`
- `testing-validation-ladder-from-e-test-to-si-verification` at `/code/blogs/llm_wiki/wiki/testing/validation-ladder-from-e-test-to-si-verification.md`

### APT/service/cost/quick-turn boundary support already present

- `methods-pcb-prototype-quickturn-and-volume-routing` at `/code/blogs/llm_wiki/facts/methods/pcb-prototype-quickturn-and-volume-routing.md`
- `processes-pcb-service-routing-from-prototype-to-special-process` at `/code/blogs/llm_wiki/wiki/processes/pcb-service-routing-from-prototype-to-special-process.md`
- `processes-prototype-vs-quick-turn-pcb-routing` at `/code/blogs/llm_wiki/wiki/processes/prototype-vs-quick-turn-pcb-routing.md`
- `frontendapt-pcb-quick-turn-pcb-page-en` at `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-quick-turn-pcb-page-en.md`
- `frontendhil-service-landings-index-en` at `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-service-landings-index-en.md`
- `frontendapt-pcba-support-services-page-en` at `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcba-support-services-page-en.md`

### Prior lane support checked

- `/code/blogs/llm_wiki/logs/p4-29-aptpcb-ro3003-ro3006-blog-ingestion-map.md`

## Draft Disposition

Draft: `ro3003-pcb-cost.md`

Overall draft status:

- `source_backed_fact_layer_partial` for product-family selection framing, Rogers family context, hybrid-stackup as a general strategy, PTFE process sensitivity, impedance-validation posture, and prototype/quick-turn routing separation.
- `blocked_pending_official_source` for exact cost claims, savings percentages, material price multipliers, process consumable economics, supplier capability proof, and RF-performance-preserving commercial promises.
- `blocked_pending_dated_capability_record` for current APT-specific service, quick-turn, stock, quote, validation-scope, and volume-pricing posture.

### Claim family: exact RO3003 / RO3006 material facts

Disposition: `completed_at_claim_family_level`

Safe reuse class:

- Pull only from existing Rogers-backed fact layer for RO3003 / RO3006 exact product facts and family comparison.

Blocked class:

- Do not reuse any draft-originated material values, availability wording, comparative rounding, or application cutoffs if they are only present in draft prose.

### Claim family: RO3000 family / RF material selector framing

Disposition: `source_backed_fact_layer_partial`

Safe reuse class:

- General selection framing for lower-loss RO3003 versus higher-Dk compactness-oriented RO3006 already exists.
- Application-band routing can reuse existing selector pages and cards.

Blocked class:

- Do not promote draft claims that turn selector framing into guaranteed mmWave, microwave, antenna-range, or ADAS performance proof.

### Claim family: hybrid RO3003 + FR-4 stackup cost reduction story

Disposition: `source_backed_fact_layer_partial`

Safe reuse class:

- Hybrid RF stackup exists as a supported strategy and process posture in current llm_wiki support.
- Safe wording is limited to mixed-material stackup planning and cost/performance/manufacturability tradeoff framing.

Blocked class:

- `30-45%` cost reduction
- any baseline-versus-hybrid percentage table
- inner-layer material substitution savings percentages
- copper-density thresholds
- via aspect-ratio or plating-limit claims
- any statement that hybrid construction preserves RF performance without project-specific validation

Reason:

- Existing support proves strategy class, not numeric savings or universal no-compromise performance outcome.

### Claim family: PTFE / ceramic process and yield cost drivers

Disposition: `source_backed_fact_layer_partial`

Safe reuse class:

- PTFE processing is a distinct manufacturing discipline.
- Plasma preparation, lamination control, copper handling, and transition management belong in process framing.

Blocked class:

- drill-hit counts
- gas/consumable cost assertions
- specific yield consequences
- lamination-cycle or plasma-process economics
- any claim tying exact process maturity to a price delta

Reason:

- Current support is process-boundary and capability-posture support, not dated plant economics.

### Claim family: controlled impedance and RF validation as cost/quote drivers

Disposition: `source_backed_fact_layer_partial`

Safe reuse class:

- Controlled impedance is paired with verification.
- RF validation can be described as a layered stack including coupons, TDR, and project-based VNA work.

Blocked class:

- exact quote-cost impact of additional impedance structures
- exact test-time economics
- guaranteed validation scope on every order
- numeric acceptance thresholds pulled from draft prose

### Claim family: supplier capability, qualification, and equipment proof

Disposition: `blocked_pending_dated_capability_record`

Blocked class:

- vacuum plasma chamber ownership proof
- LDI ownership proof
- programmed cooling / lamination-control proof
- recent RO3003 production proof
- microsection report availability as a standing promise
- qualification checklist converted into current APT capability evidence

Reason:

- This lane found only general internal capability-posture support, not dated capability records that would justify present-tense operational proof.

### Claim family: commercial service / quote / stocking / volume economics

Disposition: `blocked_pending_dated_capability_record`

Blocked class:

- raw-material cost multipliers
- supplier discount structure
- stocked-material advantage claims
- `8-12 weeks` material lead time
- prototype quantity or volume thresholds
- VMI availability
- price-break logic
- panel utilization savings claims
- quote completeness savings percentages

Reason:

- These are temporally unstable and not backed by current dated capability or procurement records in the checked support layer.

### Claim family: legal / authenticity / sole-source / audit-pass conclusions

Disposition: `blocked_pending_official_source`

Blocked class:

- sole-manufacturer or sole-source supply-chain conclusions unless explicitly tied to official manufacturer/distributor evidence
- authenticity / authorized-distributor / audit-pass conclusions
- automotive-use material-authenticity requirements as legal or procurement requirements

Reason:

- Draft-originated supply-chain and audit language must not be promoted without direct official sourcing and scope review.

## Safe Reuse Classes

These classes are reusable now if phrased conservatively and sourced from existing llm_wiki support rather than the draft:

- RO3003 / RO3006 exact-product selection from existing Rogers fact cards
- RO3000 family comparison framing
- RF material selector by application-band framing
- hybrid RF stackup as a mixed-material planning strategy
- PTFE processing as a distinct manufacturability discipline
- controlled-impedance planning paired with verification posture
- RF validation ladder framing
- separation of prototype, quick-turn, NPI/small-batch, and mass-production routing

## Blocked Claim Classes

Do not promote from this draft into facts, wiki, or customer-facing evidence without new sources:

- all exact cost numbers, ratios, or savings percentages
- all lead-time, stocking, MOQ, panel-volume, or VMI claims
- all yield, scrap, drill-life, consumable, or throughput economics
- all current APT capability proofs and equipment proofs
- all RF/microwave/mmWave performance preservation claims
- all process-limit, geometry, threshold, and acceptance-limit numbers
- all qualification, certification, audit, and legal/procurement conclusions

## Official-Source Gaps

No new official-source recovery was added in this lane. Remaining gaps for this draft family:

- official manufacturer or distributor support for any supplier-channel or authenticity claim
- official or dated source for cost, pricing, lead time, stocking, and volume-economics claims
- dated internal capability records for current APT quick-turn, prototype, validation-scope, and equipment-proof assertions
- official or project-backed evidence for any performance-preserving claim attached to hybrid stackups
- official or licensed-method support for any exact process limit or acceptance-threshold claim the future article wants to publish

## Recommended Next Recovery Lanes

1. `official manufacturer / distributor lane`
   Recover only if future content truly needs authenticity, authorized-channel, or sole-source procurement framing.

2. `dated internal capability record lane`
   Check whether current APT records exist for quick-turn posture, stocked-material posture, validation scope, and named RF/PTFE equipment proof.

3. `commercial boundary lane`
   Build or refresh a dedicated boundary card for unstable cost, lead-time, MOQ, and price-break claims if the draft family will continue to generate cost-themed articles.

4. `project-evidence lane`
   Use only if future RO3003/RO3006 content needs case-specific hybrid-stackup outcome claims, measured RF results, or validation-depth claims.

## Lane Result

- Lane status: `completed_at_claim_family_level`
- Recovery result: `source_backed_fact_layer_partial`
- New official sources recovered: none
- Main outcome: deletion-safe disposition log for a cost-focused RO3003 draft with explicit safe reuse versus blocked claim classes

## Verification

Touched files:

- `/code/blogs/llm_wiki/logs/p4-43-2026-3-ro3003-ro3006-rogers-official-source-recovery-scout.md`

Verification required after write:

- run `git diff --check` scoped to touched file
