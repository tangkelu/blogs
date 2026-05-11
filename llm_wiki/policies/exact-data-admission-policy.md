# Exact Data Admission Policy

Last updated: 2026-05-08

## Purpose

This policy defines how formulas, tables, figures, and parameter data extracted from `/code/blogs/tmps/PCB资料` may become reusable `llm_wiki` knowledge.

The policy exists to preserve a controlled path for exact data from real-case PDFs while preventing secondary-PDF rules, cookbook formulas, branded vendor article tables, and unsupported parameter claims from being promoted as universal facts.

## Scope

Applies to all exact-data candidates originating from:

- `/code/blogs/tmps/PCB资料`
- derived extraction roots such as `/code/blogs/tmps/pcb_pdf_extracted_full`
- handbook PDFs, article PDFs, and local page/image/table derivatives created from those roots

This policy works alongside:

- `policies/language-normalization-and-indexing.md`
- `policies/prompt-consumption-specification.md`

## Core Rule

Secondary-PDF formulas, tables, figures, and rules from `/code/blogs/tmps/PCB资料` are not reusable facts by default.

They may become reusable only after classification into one of the governed exact-data classes below and only if the required provenance, authority, and admission gates are satisfied.

For the `PCB资料` first slice, there are now two governed outcomes:

- `official_fact`
  - requires stronger authority than the secondary PDF itself
- `local_pdf_fact`
  - may be admitted from repo-accepted local PDF evidence when the claim stays explicitly scoped, non-numeric when necessary, and prompt-safe

If those gates are not satisfied, the content must remain `secondary_pdf_claim_inventory_only` and downstream it must be treated as `blocked_evidence`.

## Canonical Language Rule

Canonical reusable storage remains English only.

Use English for:

- `source_id`
- `fact_id`
- `topic`
- `tags`
- reusable fact-card body language
- reusable wiki-page body language

Chinese may remain in provenance-bearing contexts such as:

- original PDF filenames
- original Chinese headings or captions when needed
- logs
- source-page notes
- image/table asset metadata

Do not create parallel Chinese and English reusable records for the same exact-data concept.

## Exact Data Classes

These are the only allowed exact-data classes for admission.

### 1. `part_scoped_exact_data`

Definition:

Exact data tied to a named part, series, package, vendor family, or exact manufacturer document.

Examples:

- datasheet parameter tables
- impedance-frequency plots for a named capacitor series
- exact ESR / ESL / SRF values tied to a specific part or family
- manufacturer figure or formula scoped to that exact part family

Allowed authority shape:

- official manufacturer datasheet
- official manufacturer application note
- official manufacturer technical FAQ or article clearly scoped to the exact part or family

Safe reuse posture:

- exact values remain tied to the named part or family
- no promotion into generic universal design rules
- prompts must preserve the exact source scope

### 2. `method_scoped_exact_data`

Definition:

Exact data tied to a named method, measurement setup, reference design note, or vendor-scoped engineering method rather than a universal physical law.

Examples:

- exact curves or formulas inside a vendor application note for decoupling or antiresonance explanation
- method-specific comparison figures
- exact example tables used to explain a measurement or simulation method

Allowed authority shape:

- official semiconductor-vendor note
- official component-vendor note
- official EDA / measurement-vendor note
- standards-adjacent public method document with stable authorship

Safe reuse posture:

- data is reusable only as method-scoped exact data
- prompts must not rewrite it as a universal default or mandatory rule
- example values stay attached to the named method context

### 3. `standard_scoped_exact_data`

Definition:

Exact data tied to a named public standard, standards organization publication, or legally reusable standards-adjacent public document.

Examples:

- standard-defined terminology tables
- exact threshold or class metadata from an open/public standards source
- exact method naming or document-identity tables

Allowed authority shape:

- public official standards body page
- open/public standard text where reuse is legally and operationally acceptable
- official standards overview or conformance-reference page when the exact data is clearly stated there

Safe reuse posture:

- exact data remains scoped to the named standard and revision context
- use for identity, classification, or method framing only unless a separate governed layer permits more
- paid/private standard content must not be reconstructed from secondary PDFs

### 4. `dated_capability_exact_data`

Definition:

Exact data tied to a dated local capability record, dated internal/public supplier record, or date-sensitive operational claim that is intentionally stored as time-bounded evidence.

Examples:

- dated impedance tolerance claims
- dated fabrication windows
- dated service capability tables
- dated process or inspection capability records

Allowed authority shape:

- dated local audited record
- dated supplier capability record already accepted by repo governance
- public dated capability page with explicit date provenance

Safe reuse posture:

- must carry explicit date scope
- must carry refresh expectations
- never convert into timeless generic fact language

### 5. `secondary_pdf_claim_inventory_only`

Definition:

Any formula, table, figure, or parameter claim extracted from a secondary PDF that has not yet passed the stronger authority gates.

Examples:

- handbook formulas
- vendor article parameter tables
- branded DFM rules
- copied standards-like thresholds from secondary summaries
- unlabeled figure interpretations
- exact data whose original authority is unknown or indirect

Safe reuse posture:

- not reusable in prompts as fact evidence
- may remain in logs, claim inventory, or future source-recovery planning only
- may preserve source-page links and local image/table assets for later verification
- downstream disposition is `blocked_evidence` unless later promoted

## Required Metadata

Any admitted exact-data record must carry enough metadata to preserve scope and prevent universalization.

Any promoted record must also carry a clear disposition layer:

- `official_fact`
- `local_pdf_fact`
- `blocked_evidence`

### Required on source records

Required fields:

- `source_id`
- `title`
- `owner`
- `source_type`
- `original_source_language`
- `source_date` or `retrieved_at`
- `authority_class`
- `exact_data_class`
- `scope_type`
- `source_origin_path`
- `source_page_range` or exact source page
- `must_refresh`
- `confidence`
- `tags`
- `authority_layer`

Recommended additional provenance fields:

- `original_pdf_title`
- `original_page_label`
- `derived_asset_paths`
- `figure_ids` or `table_ids`
- `notes_on_translation`
- `notes_on_authority_limit`

### Required on fact cards

Required fields:

- `fact_id`
- `title`
- `topic`
- `category`
- `status`
- `confidence`
- `must_refresh`
- `exact_data_class`
- `scope_type`
- `canonical_unit_policy`
- `source_ids`
- `tags`
- `authority_class` or equivalent layer field
- `allowed_for`
- `not_allowed_for`

Required body sections:

- `Canonical Summary`
- `Exact Data Scope`
- `Admitted Data`
- `Conditions And Methods`
- `Limits And Non-Claims`
- `Provenance`
- `Source Links`

### Required provenance fields inside admitted exact-data body

Every admitted exact-data fact must clearly state:

- what the data is exact for
- what it is not exact for
- whether it is part-scoped, method-scoped, standard-scoped, or dated-capability-scoped
- the exact source page, figure, table, or section if available
- whether the value or figure came from text extraction, local image/table asset verification, or both

## Admission Gates

### Gate 1: Classification Gate

Every exact-data candidate must be classified into exactly one of the five allowed classes.

If classification is unclear, default to:

- `secondary_pdf_claim_inventory_only`

### Gate 2: Authority Gate

Promotion to `official_fact` requires stronger authority than the secondary PDF itself.

Allowed promotion paths:

- `secondary PDF` -> `official manufacturer source`
- `secondary PDF` -> `official semiconductor / component / EDA / measurement vendor source`
- `secondary PDF` -> `public standard / standards-body source`
- `secondary PDF` -> `dated audited capability record`

Disallowed promotion path:

- `secondary PDF` -> reusable fact card without stronger authority

Additional allowed first-slice path:

- `secondary PDF` -> `pdf_evidence/pcb_ziliao/` -> scoped `local_pdf_fact`

Requirements for that first-slice local-PDF path:

- the local batch is explicitly accepted by repo governance
- the claim stays narrow and prompt-safe
- the record carries explicit `allowed_for` and `not_allowed_for`
- the record does not pretend to be a standard, datasheet, certification, or live capability proof

### Gate 3: Scope Gate

Exact data must stay attached to its true scope:

- part
- method
- standard
- dated capability

If the source does not support that scope cleanly, do not widen it.

Example:

- exact capacitor impedance curve for one Murata series cannot become a generic capacitor-law table
- an application-note antiresonance figure cannot become a universal capacitor-pairing rule

### Gate 4: Provenance Gate

The record must preserve:

- original input PDF path
- source page reference
- original figure/table relationship where relevant
- exact stronger-authority source used for admission
- whether a local derived image/table asset was used

If provenance is incomplete, do not admit as reusable exact data.

### Gate 5: Normalization Gate

Reusable storage must be normalized into English canonical naming while preserving the original-language provenance.

Do not store reusable exact-data cards under Chinese filenames or Chinese canonical identifiers.

### Gate 6: Non-Universalization Gate

Secondary-PDF exact data cannot be promoted as a universal fact without stronger authority that actually supports universality.

If the stronger authority is still part-scoped or method-scoped, the fact must remain part-scoped or method-scoped.

### Gate 7: Consumption Gate

Admitted exact data must be usable under `prompt-consumption-specification.md` without causing blocked claim leakage.

If the data would still cause unsupported claims in downstream prompts, it must remain:

- `secondary_pdf_claim_inventory_only`
- or be admitted only as a narrower scoped card with explicit blocked language

For `local_pdf_fact`, this gate additionally requires:

- scoped wording such as `this local figure`, `this handbook example`, or equivalent
- explicit non-claims against standard, datasheet, certification, and live-capability overreach

## Blocked Promotions

The following promotions are blocked unless a stronger authority explicitly supports them.

### Always blocked from direct secondary-PDF promotion

- formulas copied from handbooks or vendor articles as universal physics / design laws
- branded rule tables turned into generic engineering rules
- exact parameter ladders presented as default selection recipes
- exact placement distances or quantity rules presented as reusable defaults
- standards-equivalent acceptance thresholds reconstructed from secondary summaries
- capability, certification, or compliance claims inferred from a handbook or article
- figure-derived exact values where the original authority is not verified
- tables or charts whose units, test conditions, or part scope are ambiguous

### Still blocked even after some admission

Unless separately governed, these remain blocked:

- universal performance outcomes
- compliance outcomes
- supplier capability generalization from dated records
- generic cookbook design rules inferred from method examples
- paid-standard content reconstructed from secondary paraphrase

## Output Targets

### For `part_scoped_exact_data`

Primary targets:

- `sources/registry/`
- `facts/`

Optional aggregation target later:

- `wiki/` only if multiple exact part / family cards need routing context

### For `method_scoped_exact_data`

Primary targets:

- `sources/registry/`
- `facts/methods/`

Optional later target:

- `wiki/processes/` or `wiki/methods/` for boundary aggregation

### For `standard_scoped_exact_data`

Primary targets:

- `sources/registry/`
- `facts/standards/`

Optional later target:

- `wiki/processes/` when the standard identity needs routing guidance

### For `dated_capability_exact_data`

Primary targets:

- `sources/registry/`
- `facts/` with explicit dated scope and refresh handling

Optional later target:

- no wiki aggregation by default unless a controller explicitly approves a dated-capability review map

### For `secondary_pdf_claim_inventory_only`

Allowed targets only:

- `logs/`
- intake maps
- source-recovery plans
- deletion-safe image/table manifests
- `pdf_evidence/pcb_ziliao/`

Not allowed targets:

- `facts/`
- `wiki/`

### For `local_pdf_fact`

Primary targets:

- `pdf_evidence/pcb_ziliao/`
- `facts/local_pdf/`

Optional supporting targets later:

- `wiki/` only when a controller explicitly decides to aggregate multiple curated local-PDF facts without hiding their authority layer

## Local Image And Table Asset Preservation

A blocked or not-yet-admitted secondary PDF may still preserve local image/table assets for later authority verification.

Allowed preservation posture:

- keep local extracted image/table asset paths
- link the asset to the original source page
- store crop/mask/review notes
- mark whether the asset is:
  - `text_verified`
  - `image_verified`
  - `needs_manual_review`
  - `blocked_pending_stronger_authority`

Important:

- local image/table assets are provenance aids, not standalone authority
- a local crop of a table or figure does not by itself upgrade the claim to reusable fact status

## Admission Workflow

1. Extract exact-data candidates from the PDF into logs or intake maps.
2. Classify each candidate into one of the five exact-data classes.
3. Default all unresolved candidates to `secondary_pdf_claim_inventory_only`.
4. Recover stronger authority.
5. If stronger authority is not required for the specific first-slice use, decide whether a scoped `local_pdf_fact` path is explicitly allowed.
6. Verify scope, provenance, date sensitivity, and English normalization.
7. Create or update `sources/registry/` records first for `official_fact` lanes.
8. Create fact cards only for the narrowest safely supported scope.
9. Keep blocked and unresolved data in logs or `pdf_evidence/`, not in reusable fact layers.
10. Update downstream evidence-pack or prompt-routing artifacts only after the fact layer exists.

## Prompt-Consumption Rule

Downstream prompts must prefer admitted exact-data cards over secondary PDF summaries.

Downstream prompts must ignore:

- `secondary_pdf_claim_inventory_only`
- `blocked_evidence`
- raw PDF formulas / tables / figures that never passed admission
- image/table assets not attached to an admitted source / fact record

## Enforcement Guidance

Before creating any reusable exact-data card from `/code/blogs/tmps/PCB资料`, check:

- is the class one of the five allowed classes?
- is the stronger authority present?
- is the scope exact and narrow?
- is provenance complete?
- is canonical storage English?
- does the prompt-consumption layer know how to consume it safely?
- are blocked promotions still blocked?

If the target is `official_fact` and any answer is no, keep the content in logs or `pdf_evidence/` as `secondary_pdf_claim_inventory_only`.

If the target is `local_pdf_fact`, also check:

- does the record explicitly say it is local-PDF-scoped?
- does it explicitly ban standards, datasheet, certification, and live-capability overclaiming?

If those answers are no, keep the content in logs or `pdf_evidence/` as `blocked_evidence`.

## Related Documents

- `policies/language-normalization-and-indexing.md`
- `policies/prompt-consumption-specification.md`
- `logs/p4-207-2026-5-6-pcb-pdf-batch-ingestion-and-image-governance-map.md`
- `logs/p4-208-2026-5-6-pcb-handbook-intake-map.md`
- `logs/p4-211-2026-5-6-emc-source-first-authority-recovery-integration.md`
- `logs/p4-212-2026-5-6-via-transition-authority-recovery-integration.md`
