# PCB资料 Unified Knowledge Layer Plan

> **For agentic workers:** Use subagents for bounded independent lanes, but keep final schema, promotion judgment, and tracker integration under the main agent.

**Goal:** Convert `/code/blogs/tmps/PCB资料` from a governed learning program that still depends on `tmps/` into the first fully usable local PDF knowledge slice inside `llm_wiki`, using the long-term unified authority model.

**Architecture:** Use a two-surface implementation cut. Surface A adds a persistent raw-evidence layer under `llm_wiki/pdf_evidence/pcb_ziliao/` for page-, figure-, table-, and formula-level provenance that survives `tmps` deletion. Surface B adds a directly consumable `llm_wiki/facts/local_pdf/` layer for curated local-PDF facts that may appear in blog body text, while preserving explicit scope boundaries and not overclaiming them as official standards, original datasheets, or supplier capability proof.

**Tech Stack:** Existing `llm_wiki` Markdown corpus, `tmps/pcb_pdf_extracted_full` manifests and extracted text while still available, current `PCB资料` logs from `P4-207` through `P4-291`, existing `facts/`, `wiki/`, and `policies/`, plus bounded subagents for evidence extraction and inventory lanes.

---

## Scope

### In Scope

- `/code/blogs/tmps/PCB资料`
- `llm_wiki/pdf_evidence/pcb_ziliao/`
- `llm_wiki/facts/local_pdf/`
- Policy updates needed to make `official_fact` and `local_pdf_fact` both consumable downstream
- Tracker updates needed to make this model discoverable by future agents

### Out Of Scope

- `/code/blogs/tmps/materias_pdf`
- Full historic backfill of the entire `llm_wiki` corpus
- One-shot migration of every legacy `fact` into the new authority model
- Rewriting blogs in this plan

## Long-Term Model

The long-term repo model is:

1. `official_fact`
   - official standards, regulator, manufacturer, or owner-backed facts
2. `local_pdf_fact`
   - curated facts from accepted local PDF batches
   - allowed in blog body with scoped wording
3. `blocked_evidence`
   - preserved provenance and candidate material only
   - not directly consumable as body facts

This plan implements that model only for the `PCB资料` batch as the first production slice.

## Directory And File Targets

### New or expanded directories

- `llm_wiki/pdf_evidence/pcb_ziliao/`
- `llm_wiki/facts/local_pdf/`

### Existing files expected to change

- `llm_wiki/README.md`
- `llm_wiki/policies/prompt-consumption-specification.md`
- `llm_wiki/policies/exact-data-admission-policy.md`
- `llm_wiki/logs/update-log.md`
- `llm_wiki/logs/backlog.md`
- `llm_wiki/logs/phase-status.md`

### Existing inputs that define current `PCB资料` status

- `llm_wiki/logs/p4-207-2026-5-6-pcb-pdf-batch-ingestion-and-image-governance-map.md`
- `llm_wiki/logs/p4-208-2026-5-6-pcb-handbook-intake-map.md`
- `llm_wiki/logs/p4-213-2026-5-6-pcb-pdf-exact-data-learning-map.md`
- `llm_wiki/logs/p4-214-2026-5-6-pcb-pdf-figure-table-learning-contract.md`
- `llm_wiki/logs/p4-216a-2026-5-6-pcb-pdf-round-1-a1-b1-c1-controller-integration.md`
- `llm_wiki/logs/p4-216b-2026-5-6-pcb-pdf-round-2-a2-b2-c2-controller-integration.md`
- `llm_wiki/logs/p4-216c-2026-5-6-pcb-pdf-round-3-a3-b3-c3-controller-integration.md`
- `llm_wiki/logs/p4-219-2026-5-7-pcb-pdf-post-round-3-promotion-review-resume-entry.md`
- `llm_wiki/logs/p4-291-2026-5-7-pcb-pdf-strong-completion-closeout.md`

## Required Schemas

### `pdf_evidence` record

Every evidence record under `pdf_evidence/pcb_ziliao/` must include at least:

- `evidence_id`
- `batch_id: pcb_ziliao`
- `original_pdf_title`
- `source_origin_path`
- `page`
- `evidence_type`
- `claim_summary`
- `authority_class`
- `allowed_use`
- `blocked_use`
- `promotion_status`
- `deletion_safe: true`

Recommended supporting fields:

- `local_asset_path`
- `page_excerpt_ref`
- `related_fact_ids`
- `related_source_ids`
- `notes_on_branding`
- `notes_on_translation`

### `facts/local_pdf` record

Every curated local-PDF fact must include at least:

- `fact_id`
- `title`
- `authority_class: local_pdf_curated`
- `allowed_for: blog_body`
- `not_allowed_for`
- `evidence_ids`
- `scope_type`
- `confidence`
- `limits_and_non_claims`

Recommended additional fields:

- `topic`
- `conditions_and_methods`
- `canonical_summary`
- `related_official_fact_ids`
- `must_refresh`

## Promotion Rules

### Allowed promotion path

`pcb_ziliao raw page/asset -> pdf_evidence -> local_pdf_fact -> optional future official_fact`

### Promotion intent

- `pdf_evidence` preserves provenance and retrieval
- `local_pdf_fact` makes selected content directly reusable for blog body
- `official_fact` remains the stronger layer when later official authority exists

### Hard blocks

Do not promote the following into `local_pdf_fact` unless the repo explicitly changes policy later:

- current certification status
- lead time, price, MOQ, yield, stock, or other dynamic commercial values
- supplier capability promises framed as current operational commitments
- branded UI workflows or brand-specific persuasion copy
- exact standards thresholds when the PDF is only a secondary summary

## Downstream Consumption Contract

After this plan lands:

- downstream prompts may consume `official_fact`
- downstream prompts may also consume `local_pdf_fact`
- prompts must preserve wording scope for `local_pdf_fact`
- prompts must not rewrite `local_pdf_fact` as:
  - official standard mandates
  - original manufacturer datasheet values
  - supplier certification proof
  - live capability or live commercial promises

Raw `pdf_evidence` is not body-ready by default. It is allowed for:

- structure planning
- terminology recovery
- figure discovery
- candidate table lookup
- future fact promotion

It is not allowed as direct blog-body fact support unless promoted into `facts/local_pdf/` or stronger.

## Execution Phases

### Phase A: Model And Policy Cut-In

- Add README documentation for the unified authority model
- Update policy language so `local_pdf_fact` is a first-class consumable layer
- Clarify that `deletion_safe` is a state, not a directory-layer name

### Phase B: `pcb_ziliao` Evidence Inventory

- Create `pdf_evidence/pcb_ziliao/`
- Inventory page-, figure-, table-, and formula-level evidence that must survive `tmps` deletion
- Prefer bounded evidence families over whole-PDF dumps

### Phase C: Curated Local-PDF Fact Landing

- Create `facts/local_pdf/`
- Promote only user-accepted, blog-usable `PCB资料` numerics / formulas / figure conclusions
- Keep scope and non-claims explicit

Priority order:

1. already semi-landed handbook families with clear blog value
2. package / footprint examples
3. PCBA visual and process guidance numerics or semi-structured conclusions
4. EMC method/example numerics that remain useful even without official-owner replacement

### Phase D: Consumption And Tracker Integration

- Update prompt-consumption rules
- Update tracker entry points so future `/goal` agents restart from this plan rather than older `tmps`-dependent assumptions
- Record what is now directly blog-consumable and what remains blocked

## Suggested Subagent Lanes

Subagents are appropriate only for bounded, disjoint lanes.

Recommended lane split:

1. `evidence inventory lane`
   - own only `pdf_evidence/pcb_ziliao/<family>/...`
2. `local_pdf_fact drafting lane`
   - own only `facts/local_pdf/...`
3. `policy and prompt lane`
   - own only policy file drafts or proposal notes
4. `tracker integration lane`
   - collect status suggestions only; main agent lands trackers

Main agent retains:

- final schema decisions
- promotion approval
- policy merge
- tracker updates
- final verification

## Acceptance Criteria

This plan is complete only when all of the following are true:

- `llm_wiki/README.md` documents the unified authority model and the `PCB资料` implementation slice
- `pdf_evidence/pcb_ziliao/` exists with stable schema and initial landed records
- `facts/local_pdf/` exists with initial landed facts that are allowed in blog body
- prompt-consumption policy explicitly supports `local_pdf_fact`
- trackers explicitly mention the new model and current `PCB资料` cut-in state
- future agents can continue from `llm_wiki/` alone without requiring `tmps/` survival for basic retrieval

## Verification Checklist

- `rg -n "pdf_evidence|local_pdf_curated|pcb_ziliao" /code/blogs/llm_wiki`
- verify every new `evidence_id` is unique
- verify every `local_pdf_fact` references valid `evidence_ids`
- `git diff --check -- /code/blogs/llm_wiki`
- ensure no `materias_pdf` paths were introduced into this implementation slice

## `/goal` Execution Intent

If a long-running `/goal` agent resumes from this plan, its default interpretation should be:

- do not redesign the model again
- implement the unified authority model only for `PCB资料`
- persist evidence and curated facts inside `llm_wiki`
- use subagents for bounded extraction and drafting lanes
- keep final authority decisions and tracker integration centralized
