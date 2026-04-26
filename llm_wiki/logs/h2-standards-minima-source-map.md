# H2 Standards Minima Source Map

Date: 2026-04-25

## Purpose

This document maps the current corpus for the `standards_minima` containment area.

Its job is to show which sources can support standards hierarchy, addendum framing, and non-claim boundaries today, and why threshold/minimum claims in this area still cannot be treated as reusable capability numerics.

This file is not:

- a standards-threshold fact card
- a numeric recovery memo
- permission to reuse minima, thresholds, or acceptance values from existing pages

## Current Source Classification

### A. Downgrade / Framing Support

These sources are useful for standards hierarchy, revision control, and guarded addendum framing. They do not authorize transferable numeric threshold claims.

- [ipc-finish-standards-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-finish-standards-metadata.md)
  - use: finish-standard identity, revision status, and source discovery
  - limit: explicitly does not provide finish thickness, acceptance criteria, sampling rules, or process limits
- [ipc-6012-addendum-program-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-6012-addendum-program-metadata.md)
  - use: rigid-board base-vs-addendum hierarchy and program-trigger framing
  - limit: explicitly does not provide annular-ring values, plating minima, bow/twist limits, or other acceptance thresholds
- [22-layer-high-reliability-rewrite-guardrail.md](/code/blogs/llm_wiki/facts/standards/22-layer-high-reliability-rewrite-guardrail.md)
  - use: high-reliability rewrite boundary control around class-linked, qualification, and acceptance leakage
  - limit: explicitly blocks unsupported threshold tables and supplier-status overreach

### B. Standards Registry Boundary Support

These sources are valid for showing what public standards records can and cannot support. They still do not authorize reusable numerics.

- `/code/blogs/llm_wiki/sources/registry/standards/ipc-6012fs-toc.md`
  - supports: clause-family visibility for space/military addendum scope
  - limit: explicitly does not authorize acceptance values or full requirements
- `/code/blogs/llm_wiki/sources/registry/standards/ipc-6012fa-toc.md`
  - supports: clause-family visibility for automotive addendum scope
  - limit: explicitly does not authorize technical criteria or full automotive requirements
- `/code/blogs/llm_wiki/sources/registry/standards/ipc-6013e-toc.md`
  - supports: rigid-flex/flex performance-spec metadata
  - limit: explicitly does not authorize thresholds or class-specific requirements
- `/code/blogs/llm_wiki/sources/registry/standards/ipc-a-600k-toc.md`
  - supports: workmanship-document identity
  - limit: explicitly does not authorize reusable class thresholds
- `/code/blogs/llm_wiki/sources/registry/standards/ipc-a-610h-toc.md`
  - supports: workmanship-document identity
  - limit: explicitly does not authorize accept/fail thresholds

### C. Governance Boundaries

These sources explicitly explain why this area stays contained.

- [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md)
  - boundary: reusable capability numbers require a `Tier 1 internal dated capability record`
  - boundary: standards thresholds and acceptance criteria are excluded from H2 capability recovery
- [h2-annular-ring-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-annular-ring-bucket-decision.md)
  - boundary: class-linked threshold tables are not capability proof
- [h2-plating-thickness-build-allowance-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-plating-thickness-build-allowance-bucket-decision.md)
  - boundary: finish-standard and threshold wording must not contaminate plated-copper capability
- [h2-copper-plating-process-windows-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-copper-plating-process-windows-bucket-decision.md)
  - boundary: standards minima were always a separate child leakage class from the mixed copper/plating cluster

## Why Current Sources Do Not Authorize Reusable Numeric Threshold Claims

Current sources are mixed across:

- revision metadata
- TOC or product-page standards identity
- addendum hierarchy and program framing
- rewrite guardrails
- contract or acceptance-context metadata

That means the current corpus can support:

- standards vocabulary
- program hierarchy
- threshold-leakage control

It cannot support:

- reusable finish minima
- reusable class thresholds
- reusable acceptance tables
- transferable procurement or qualification thresholds

## Candidate Split Families For Future Work

If later work continues here, claims must first be split into:

1. `finish-standard minima`
2. `IPC-6012 and addendum acceptance thresholds`
3. `workmanship or class-linked thresholds`
4. `procurement or qualification acceptance context`

These families should be handled under a standards-governance path, not ordinary H2 capability recovery.

## Sources That Explicitly Require Refresh Or Do Not Authorize Transferable Numeric Threshold Claims

The following sources already contain explicit boundary language that blocks direct numeric reuse:

- [ipc-finish-standards-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-finish-standards-metadata.md)
  - explicitly says it does not provide finish thickness, acceptance criteria, sampling rules, or process limits
- [ipc-6012-addendum-program-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-6012-addendum-program-metadata.md)
  - explicitly says it does not provide plating-thickness minima or other acceptance thresholds
- [22-layer-high-reliability-rewrite-guardrail.md](/code/blogs/llm_wiki/facts/standards/22-layer-high-reliability-rewrite-guardrail.md)
  - explicitly blocks unsupported `Class 3/3A` tables, qualification tables, and threshold leakage
- `/code/blogs/llm_wiki/sources/registry/standards/ipc-6012fs-toc.md`
  - explicitly says not to quote or reconstruct acceptance values from the TOC
- `/code/blogs/llm_wiki/sources/registry/standards/ipc-6013e-toc.md`
  - explicitly says not to extract thresholds or class-specific requirements from the public record

## What Is Still Missing

The missing item is not more standards vocabulary. The missing item is lawful, scoped, and context-correct threshold governance.

Still missing:

- narrower family decisions with clean scope boundaries
- explicit separation between standards thresholds and current shop capability
- explicit separation between public metadata and licensed technical criteria
- a governance path outside ordinary H2 capability recovery for any future threshold handling
- proof that a cited threshold is legally and contextually usable rather than reconstructed from public metadata

Without those items, `standards_minima` remains a containment area, not a reusable H2 numeric bucket.

## Current Ingestion Stop/Go Posture

- `keep`: standards hierarchy, addendum framing, and revision metadata in the correct layer
- `downgrade`: procurement and program-governance context without numeric promotion
- `hold`: standards-threshold containment for minima and acceptance values
- `delete`: metadata, TOCs, or public standards pages rewritten as reusable technical threshold tables
