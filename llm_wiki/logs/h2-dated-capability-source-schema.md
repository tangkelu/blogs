# H2 Dated Capability Source Schema

Date: 2026-04-25

## Purpose

This document defines the minimum schema and usage policy for a future `dated capability source record` in `llm_wiki`.

It is a governance document for `H2 Fabrication Capability Numeric Layer`.

It is not:

- a live source record
- a fact card
- a capability promise
- a substitute for an official external source page

## Why H2 Needs Dated Capability Source Records

`H1` improved material-grade coverage, but `Class B` fabrication capability numerics remain the weakest reusable numeric layer.

The current blocker is not lack of terminology. The blocker is that fabrication numbers are often:

- date-sensitive
- site-specific
- machine-specific
- process-family-specific
- condition-bound
- easy to over-generalize into marketing-style claims

So a fabrication capability number must not be reused in future facts, tables, or evidence packs unless it is attached to a dated record that preserves source, scope, method, and refresh discipline.

The schema exists to block stale or scope-free reuse such as:

- copying a number from a support page into a generic capability table
- turning one site or one line limit into a company-wide default
- carrying forward an old capability figure after process or equipment changed
- mixing drill, laser, rigid, HDI, and build-up numerics into one undifferentiated claim

## H2 Scope Rule

This schema is for fabrication capability numerics such as:

- trace / space
- minimum mechanical drill
- minimum laser via
- aspect ratio
- annular ring
- registration tolerance
- backdrill residual stub window
- impedance tolerance
- thickness window
- lamination or build-up capability counts when they are treated as capability claims

This schema does not authorize:

- standards thresholds
- qualification acceptance numbers
- dynamic commercial numbers
- board-level SI or channel-budget claims
- material datasheet values that already belong under `H1` product-grade material sourcing

## Minimum Required Fields For A Future Dated Capability Source Record

Every future dated capability source record should contain all fields below before any capability number is reused.

### Identity

- `source_id`
  - pattern: `cap-YYYYMMDD-owner-scope-process-shortname`
  - goal: make date, owner, and scope visible in the identifier itself
- `title`
- `record_type`
  - must be `dated_capability_source_record`
- `status`
  - example classes: `active`, `watch`, `retired`, `superseded`

### Time Control

- `capture_date`
  - the date the source was checked and frozen into the record
- `validity_window`
  - explicit bounded usage window such as `review within X months` or `valid until superseded`
- `refresh_trigger`
  - events that force review, such as page revision, equipment change, plant change, process change, line migration, or wording drift

### Ownership And Authority

- `source_owner`
  - who controls the upstream source named in the record
- `authority_class`
  - required class labels:
  - `official_external_capability_page`
  - `official_external_support_or_spec_page`
  - `internal_dated_capability_record`
  - `internal_process_framing_page`
- `confidence_or_usage_rule`
  - explicit statement of what downstream use is allowed

### Scope

- `company_scope`
  - company, division, or brand if relevant
- `site_scope`
  - plant, region, or `not stated`
- `machine_or_line_scope`
  - line, drill family, laser family, plating line, lamination press family, or `not stated`
- `process_family`
  - required examples: `standard multilayer rigid`, `HDI sequential lamination`, `laser microvia`, `rigid-flex`, `build-up substrate-like`
- `scope_statement`
  - one sentence defining exactly what the number applies to

### Numeric Payload Definition

- `numeric_field_names`
  - exact claim labels, not vague summaries
- `units`
  - exact units for every numeric field
- `condition_or_test_method`
  - method, condition, measurement basis, coupon context, or process condition required to interpret the number
- `boundary_notes`
  - what the number does not mean
- `machine_site_dependency`
  - whether the value is universal, site-bound, line-bound, or condition-bound

### Lineage And Control

- `supersedes`
  - prior record ids replaced by this record
- `superseded_by`
  - later record id if replaced
- `linked_external_source_urls`
  - official upstream URLs only
- `linked_evidence_pack_ids`
  - future evidence packs allowed to consume this record
- `linked_fact_card_ids`
  - future fact cards allowed to derive numbers from this record
- `forbidden_uses`
  - explicit misuse list

## Required Interpretation Rules

No fabrication capability number is reusable unless the record makes all of these answerable:

1. Who said it?
2. When was it captured?
3. For which process family?
4. For which site, line, machine, or stated scope?
5. In what unit?
6. Under what condition or method?
7. For how long may it be reused before refresh?
8. What downstream uses are explicitly allowed?

If any answer is missing, the number stays non-reusable.

## Record-Type Distinctions

### 1. Internal Dated Capability Record

This is the `H2` object governed by this schema.

Allowed use:

- reusable intermediate layer for future capability fact cards
- controlled bridge between an upstream source and downstream evidence packs

Not enough by itself unless it points to a real upstream source or clearly states why the record is a controlled internal capture with a bounded validity window.

### 2. Official External Capability Or Support Page

This is a manufacturer- or fabricator-controlled public page, support page, capability page, or published spec page.

Allowed use:

- primary upstream evidence for a dated capability record

Not enough by itself for reuse if it lacks capture date, validity handling, scope normalization, or condition notes.

### 3. Internal Process Framing Page

This is an internal explanatory page about process logic, workflow, or manufacturability framing.

Allowed use:

- vocabulary
- planning posture
- non-numeric context

Not allowed as sole support for transferable fabrication capability numerics.

## Authority And Usage Posture

- `official_external_capability_page`
  - strongest public anchor for capability-style numbers
  - still requires dated capture and scope normalization before reuse
- `official_external_support_or_spec_page`
  - acceptable when it clearly publishes a capability-like numeric with method and scope
  - must not be stretched beyond the stated process family
- `internal_dated_capability_record`
  - governance object for reuse
  - may enable downstream fact-card writing only when all mandatory fields are complete
- `internal_process_framing_page`
  - posture-only
  - cannot unlock numeric reuse

## Forbidden Uses

Every future dated capability source record should explicitly block at least the following:

- using one record as proof of company-wide universal capability when site or line is unstated
- converting one process-family number into a neighboring process-family number
- converting prototype capability into production-default capability
- converting one test condition into all-condition performance
- using a dated capability record as standards compliance proof
- using a dated capability record as customer-program approval proof
- using a dated capability record as a commercial SLA or quotation promise
- reusing the number after the validity window or after a refresh trigger fired

## Example-Safe Record Pattern

Safe pattern, described abstractly:

- a record id includes date, owner, site or scope token, and process-family token
- the upstream source is an official external capability or support page
- the record lists one or more named numeric fields with exact units
- each field is tied to a stated condition, method, or measurement context
- the record says whether the number is site-bound or line-bound
- the record states when review is required
- the record says it may feed only a guarded capability fact card and a named evidence pack

This pattern is safe because the number remains attached to date, scope, and interpretation limits.

## Example-Unsafe Record Pattern

Unsafe pattern, described abstractly:

- a record id has no date or scope
- the upstream page is a generic process explainer
- numeric fields are summarized loosely as `advanced capability` or `fine feature support`
- no unit, method, or condition is preserved
- no site, line, or machine boundary is stated
- the record is then used to populate multiple generic manufacturing tables

This pattern is unsafe because it turns a context-bound statement into a scope-free reusable fact.

## Linkage Rules To Future Fact Cards And Evidence Packs

Future capability fact cards should not pull a fabrication number directly from a raw page if a dated capability record is required for that class of claim.

The expected linkage order is:

1. official external capability or support page
2. internal dated capability source record
3. guarded capability fact card
4. evidence pack or prompt-ready downstream asset

Rules:

- a fact card must cite the dated capability record id, not only the raw upstream URL
- an evidence pack should cite both the fact card and the dated capability record for higher-risk capability numerics
- one dated capability record may feed multiple fact cards only if scope, process family, and validity window remain identical
- if a fact card broadens the scope beyond the dated record, that fact card is invalid

## Recommended Control-Doc References For H2 Start

When `H2` begins, control docs should reference this schema in short form:

- `high-numeric-density-program-plan.md`
  - state that `Class B` numerics are reusable only through a dated capability source record that satisfies this schema
- `phase-status.md`
  - describe `H2` progress in terms of record count, process-family coverage, and refresh discipline rather than raw number count
- `backlog.md`
  - queue governance and inventory tasks before speculative capability fact cards
- future H2 tracking docs
  - separate `record created`, `record refreshed`, `record superseded`, and `fact-card unlocked`

## Operational Recommendation

At H2 kickoff, start with inventory and schema compliance, not with number harvesting.

The first question for each candidate capability number should be:

`Can this be preserved as a dated, scoped, method-bound record?`

If the answer is no, the number should remain under `gap_control`, even if the source looks plausible.
