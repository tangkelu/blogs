# H2 Annular Ring Source Map

Date: 2026-04-25

## Purpose

This document maps the current corpus for the `annular_ring` H2 bucket.

Its job is to show which sources can support posture, framing, and non-claim boundaries today, and which upstream inputs might later feed a dated capability record.

This file is not:

- an annular-ring fact card
- a numeric recovery memo
- permission to reuse annular-ring numbers from existing pages

## Current Source Classification

### A. Downgrade / Framing Support

These sources are useful for manufacturability framing, drill / registration interaction, and guarded internal routing. They do not authorize transferable annular-ring numbers.

- [advanced-pcb-fabrication-and-stackup-planning.md](/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md)
  - use: advanced rigid-board fabrication, drill, stackup, and geometry-risk framing
  - limit: explicitly marks exact internal capability numbers as refresh-sensitive
- [high-layer-count-backdrill-and-registration-posture.md](/code/blogs/llm_wiki/facts/methods/high-layer-count-backdrill-and-registration-posture.md)
  - use: supports registration-sensitive high-layer manufacturability wording
  - limit: does not provide annular-ring capability numerics
- [high-layer-rigid-board-manufacturability-context.md](/code/blogs/llm_wiki/facts/methods/high-layer-rigid-board-manufacturability-context.md)
  - use: supports guarded high-layer dimensional-control posture
  - limit: does not provide annular-ring limits or tables
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-multilayer-pcb-page-en.md`
  - use: multilayer fabrication-family context
  - limit: extraction notes already treat geometry-style figures as internal claims
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-multilayer-pcb-product-page-en.md`
  - use: HIL-side multilayer stackup and manufacturability framing
  - limit: process-capability numbers remain internal support only
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-high-layer-count-pcb-page-en.md`
  - use: high-layer complexity and process-discipline framing
  - limit: not a frozen annular-ring capability source
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-drilling-page-en.md`
  - use: drilling-family routing and process posture
  - limit: exact numeric claims are internal capability framing, not transferable authority

### B. Posture Support

These sources are valid for showing that the repo already has controlled posture support around annular-ring-adjacent manufacturability risk. They still do not authorize reusable annular-ring numbers.

- [ipc-6012-addendum-program-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-6012-addendum-program-metadata.md)
  - supports: clause-family visibility around annular ring, plating integrity, and related acceptance topics
  - limit: explicitly does not provide annular-ring values or acceptance thresholds
- [22-layer-high-reliability-rewrite-guardrail.md](/code/blogs/llm_wiki/facts/standards/22-layer-high-reliability-rewrite-guardrail.md)
  - supports: high-layer, high-reliability writing boundaries where class and workmanship leakage is common
  - limit: explicitly blocks numeric annular-ring, plating, and qualification thresholds
- `/code/blogs/llm_wiki/sources/registry/standards/ipc-6012fs-toc.md`
  - supports: public topic-level visibility that annular ring sits inside standards/addendum scope
  - limit: public TOC metadata only, not numeric authority

### C. Non-Claim Boundaries

These sources are important because they explicitly block overreach.

- [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md)
  - boundary: reusable capability numbers require a `Tier 1 internal dated capability record`
  - boundary: forbids standards thresholds, design-rule leakage, and stale undated internal numerics
- [h2-capability-number-inventory.md](/code/blogs/llm_wiki/logs/h2-capability-number-inventory.md)
  - boundary: `annular_ring` is already marked as mixed with standards-threshold risk
  - boundary: explicitly warns not to recover annular-ring numerics unless they are true current internal capability numbers
- [h2-registration-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-registration-bucket-decision.md)
  - boundary: registration claims need their own measurement context and must not collapse into geometry shortcuts
  - boundary: drill / alignment interaction is not automatically annular-ring authority
- [layer-count-blog-readiness.md](/code/blogs/llm_wiki/logs/layer-count-blog-readiness.md)
  - boundary: current layer-count corpus remains weak where mixed geometry, process, and standards numerics sit together
  - boundary: annular-ring clusters remain one of the blocked overclaim zones

### D. Candidate Upstream Inputs For A Future Dated Capability Record

These inputs may help identify owner, scope, and family boundaries for a future `Tier 1` record. They do not authorize annular-ring numbers by themselves.

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-drilling-page-en.md`
  - candidate role: drilling-family owner and scope routing
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-multilayer-pcb-page-en.md`
  - candidate role: rigid-multilayer scope and downstream wording alignment
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-multilayer-pcb-product-page-en.md`
  - candidate role: HIL-side cross-check for public wording consistency
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-high-layer-count-pcb-page-en.md`
  - candidate role: high-layer scope and exception routing

These are only candidate upstream inputs because they are:

- internal
- semi-stable
- undated as capability records
- mixed with other geometry and process wording

The following sources are better treated as boundary inputs than numeric feeders:

- [ipc-6012-addendum-program-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-6012-addendum-program-metadata.md)
- [22-layer-high-reliability-rewrite-guardrail.md](/code/blogs/llm_wiki/facts/standards/22-layer-high-reliability-rewrite-guardrail.md)
- `/code/blogs/llm_wiki/sources/registry/standards/ipc-6012fs-toc.md`

Their value is mainly to prevent standards or compliance language from being misread as annular-ring capability.

## Sources That Explicitly Require Refresh Or Do Not Authorize Transferable Annular-Ring Numbers

The following sources already contain explicit boundary language that blocks direct numeric reuse:

- [advanced-pcb-fabrication-and-stackup-planning.md](/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md)
  - explicitly treats exact internal capability numbers as refresh-sensitive
- [high-layer-rigid-board-manufacturability-context.md](/code/blogs/llm_wiki/facts/methods/high-layer-rigid-board-manufacturability-context.md)
  - explicitly says it does not provide geometry limits or capability tables
- [ipc-6012-addendum-program-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-6012-addendum-program-metadata.md)
  - explicitly says it does not provide annular-ring values or other acceptance thresholds
- [22-layer-high-reliability-rewrite-guardrail.md](/code/blogs/llm_wiki/facts/standards/22-layer-high-reliability-rewrite-guardrail.md)
  - explicitly blocks class-linked annular-ring tables from reuse
- all relevant internal registry records in this bucket
  - extraction notes treat geometry figures as internal, refresh-sensitive, or support-only

## What Is Still Missing

The missing item is not more annular-ring vocabulary. The missing item is a governed numeric authority.

Still missing:

- a registered `Tier 1 internal dated capability record` for annular-ring capability
- explicit separation between shop capability and class / acceptability thresholds
- explicit separation between annular-ring capability and drill / registration interaction
- explicit distinction between cookbook design rules and maintained production limits
- usable date, owner, and refresh posture for any future annular-ring record
- evidence that a cited number is a maintained capability record rather than a standards threshold, design-rule default, or example residue

Without those items, all reusable annular-ring numbers remain `needs_source`.

## Recommended Future Ingestion Order

1. Recover or register the missing `Tier 1 internal dated capability record` for annular-ring capability.
2. Verify that the record clearly separates shop capability from IPC or addendum threshold language.
3. Verify that drill / registration interaction is handled as supporting scope, not as a substitute numeric authority.
4. Use current internal drilling and multilayer pages only as wording and owner cross-checks.
5. Keep public standards metadata as boundary control only.

Current ingestion stop/go posture:

- `keep`: boundary and posture support already in corpus
- `downgrade`: manufacturability and registration framing without numeric promotion
- `needs_source`: all reusable annular-ring numerics
- `delete`: standards or cookbook values disguised as shop capability
