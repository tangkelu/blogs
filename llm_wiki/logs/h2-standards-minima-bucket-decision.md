# H2 Standards Minima Bucket Decision

Date: 2026-04-25

## Purpose

This document records the governance posture for `standards_minima` under `H2 Workstream 2: Fabrication Capability Numeric Layer`.

This area exists to stop one common failure mode:

- IPC, addendum, qualification, workmanship, or other standards-linked minima being rewritten as reusable factory capability numerics

This file is:

- a governance and dependency document
- a containment decision
- a stop/go control for standards-threshold leakage

This file is not:

- a normal capability-recovery bucket
- a numeric fact card
- permission to reuse standards minima or acceptance thresholds
- a substitute for a `Tier 1 internal dated capability record`

## Current True Posture

`standards_minima` should be governed as standards-leakage containment rather than normal capability recovery.

Most claims here are standards metadata, clause-family visibility, procurement-trigger framing, or acceptance-threshold context, not stable manufacturing authority.

Current public and internal sources support posture and boundary control only. They do not authorize reusable numeric recovery in this area.

## Why This Area Is Not A Normal Capability Bucket

This cluster mixes several non-equivalent claim types:

- IPC finish-standard minima
- `IPC-6012` / addendum acceptance thresholds
- class-linked or workmanship thresholds
- procurement-trigger or qualification-program framing
- public TOC or product-page metadata
- contract/governance acceptance context

Those items are usually:

- controlled or licensed standards content
- procurement dependent
- program dependent
- acceptance-context dependent

That means one recovered number here would almost always overstate portability and misstate its source class.

## What This Containment Area Commonly Contains

Typical mixed claim shapes:

- minimum plating or finish threshold
- addendum-linked acceptance value
- class-linked threshold table
- public standards metadata mistaken for free technical criteria
- procurement or qualification wording rewritten as shop capability

## Current Corpus Support And Boundaries

The current corpus is already strong enough to support standards hierarchy, addendum framing, and non-claim boundaries around thresholds and minima.

It is not strong enough to support reusable numeric standards claims.

### Standards Metadata Support

The following standards cards are useful for guarded framing:

- [ipc-finish-standards-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-finish-standards-metadata.md)
- [ipc-6012-addendum-program-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-6012-addendum-program-metadata.md)
- [22-layer-high-reliability-rewrite-guardrail.md](/code/blogs/llm_wiki/facts/standards/22-layer-high-reliability-rewrite-guardrail.md)

These can support statements such as:

- public IPC records are useful for document identity, revision status, clause-family visibility, and program hierarchy
- public standards metadata does not expose reusable technical thresholds
- addendum or class-linked wording must not be collapsed into factory capability claims

### Standards Registry Boundary Support

The following registry records are useful because they explicitly block threshold overreach:

- `/code/blogs/llm_wiki/sources/registry/standards/ipc-6012fs-toc.md`
- `/code/blogs/llm_wiki/sources/registry/standards/ipc-6012fa-toc.md`
- `/code/blogs/llm_wiki/sources/registry/standards/ipc-6013e-toc.md`
- `/code/blogs/llm_wiki/sources/registry/standards/ipc-a-600k-toc.md`
- `/code/blogs/llm_wiki/sources/registry/standards/ipc-a-610h-toc.md`

These support guarded statements such as:

- public TOCs can show scope and clause-family identity
- public TOCs do not authorize threshold extraction or reconstructed acceptance tables

### Copper/Plating Cluster Boundary Support

[h2-copper-plating-process-windows-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-copper-plating-process-windows-bucket-decision.md), [h2-annular-ring-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-annular-ring-bucket-decision.md), and [h2-plating-thickness-build-allowance-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-plating-thickness-build-allowance-bucket-decision.md) already support these guarded statements:

- standards minima are a separate leakage class from capability recovery
- class-linked or threshold-based values must not piggyback into H2 capability facts
- standards and capability numerics must remain separate governance layers

## Containment Rule

Current rule for this area:

- keep standards hierarchy, addendum framing, and procurement-trigger vocabulary where needed
- do not promote finish minima, class thresholds, workmanship thresholds, or acceptance tables into reusable factory defaults
- do not create one `standards_minima` capability fact card
- do not bridge this area into `P4-06` as if it were a normal recovered numeric layer

## Required Claim Split

Any future work here must first split incoming claims into these families.

### 1. `finish-standard minima`

Scope:

- finish-specific minimums or thresholds tied to IPC finish standards

### 2. `IPC-6012 and addendum acceptance thresholds`

Scope:

- thresholds, sample plans, or acceptance context tied to `IPC-6012` branches or addenda

### 3. `workmanship or class-linked thresholds`

Scope:

- class-linked visual or workmanship thresholds
- `Class 2 / Class 3 / Class 3A` style table leakage

### 4. `procurement or qualification acceptance context`

Scope:

- program-triggered acceptance context
- lot-acceptance, procurement, or qualification framing

None of these should be assumed numerically recoverable unless a very narrow family later receives a legitimate standards-access and governance path that is separate from H2 capability recovery.

## Disposition Guidance For Current Mixed Claims

### public IPC metadata or TOC reused as technical threshold proof

- disposition: `delete`
- reason:
  - public metadata is not free technical criteria

### finish-standard revision metadata rewritten as plating capability

- disposition:
  - `downgrade` for revision-control framing
  - `delete` if promoted as capability authority

### addendum or class-linked threshold reused as factory capability

- disposition: `delete`
- reason:
  - standards or acceptance threshold is not shop capability evidence

### procurement or qualification wording rewritten as current supplier or lot approval

- disposition:
  - `downgrade` as governance context if kept non-numeric
  - `delete` if promoted as capability or approval proof

## Exact Next-Step Requirements

Before any standards-threshold numeric recovery could exist here, the repo still needs:

1. narrower family decisions with clean scope boundaries
2. explicit separation between standards thresholds and current shop capability
3. explicit separation between public metadata and licensed technical criteria
4. a governance path that is separate from H2 capability recovery for any future standards-threshold handling
5. proof that a cited number is legally and contextually usable rather than a reconstructed threshold from public metadata

Until those conditions are met, `standards_minima` remains a containment area, not a normal capability-recovery bucket.
