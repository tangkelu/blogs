# H2 Trace Space Source Map

Date: 2026-04-25

## Purpose

This document maps the current corpus for the `trace_space` H2 bucket.

Its job is to show which sources can support posture, framing, and non-claim boundaries today, and which upstream inputs might later feed a dated capability record.

This file is not:

- a trace/space fact card
- a numeric recovery memo
- permission to reuse line/space numbers from existing pages

## Current Source Classification

### A. Downgrade / Framing Support

These sources are useful for vocabulary, process-family routing, and guarded framing. They do not authorize transferable trace/space numbers.

- [advanced-pcb-fabrication-and-stackup-planning.md](/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md)
  - use: separates HDI, impedance, high-layer, thermal, rigid-flex, and IC-substrate planning frames
  - limit: explicitly marks exact `line/space` and related internal capabilities as refresh-sensitive
- [apt-capability-family-map-and-boundaries.md](/code/blogs/llm_wiki/wiki/processes/apt-capability-family-map-and-boundaries.md)
  - use: distinguishes `Rigid PCB`, `HDI PCB`, and other capability families
  - limit: explicitly says capability pages are routing maps, not manufacturing specifications
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-capabilities-index-page-en.md`
  - use: capability-family overview and routing context
  - limit: family-index style source only; not a numeric authority
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-rigid-pcb-capability-page-en.md`
  - use: general rigid multilayer capability framing
  - limit: extraction notes already treat drill and other limits as refresh-sensitive internal claims
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-hdi-pcb-capability-page-en.md`
  - use: HDI, fine-line, microvia, and build-up wording
  - limit: extraction notes already treat line/space details as refresh-sensitive internal claims
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-hdi-pcb-page-en.md`
  - use: HDI product-page posture and TDR-linked wording
  - limit: extraction notes already say numeric capability claims are refresh-required before publication
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
  - use: advanced-manufacturing vocabulary and route framing
  - limit: process framing only unless backed by a dated capability record
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-multilayer-pcb-page-en.md`
  - use: multilayer fabrication-family context
  - limit: not a frozen feature-size capability source
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-high-layer-count-pcb-page-en.md`
  - use: high-layer routing and complexity framing
  - limit: not a transferable geometry authority
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-hdi-pcb-product-page-en.md`
  - use: HIL-side HDI posture and product framing
  - limit: internal product-page source; geometry claims remain refresh-sensitive

### B. Posture Support

These sources are valid for showing that the repo already has controlled posture support around density-oriented manufacturing. They still do not authorize reusable trace/space numbers.

- [hdi-microvia-and-vippo-process-posture.md](/code/blogs/llm_wiki/facts/methods/hdi-microvia-and-vippo-process-posture.md)
  - supports: HDI build-up, microvia, any-layer, VIPPO as normal process posture
  - limit: exact microvia or geometry figures must refresh
- [ic-substrate-fine-line-build-up-posture.md](/code/blogs/llm_wiki/facts/methods/ic-substrate-fine-line-build-up-posture.md)
  - supports: SAP fine-line substrate posture as a distinct capability class
  - limit: exact substrate line/space values must refresh and are not transferable to general PCB
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-ic-substrate-pcb-product-page-en.md`
  - supports: substrate fine-line, SAP, ABF/BT, stacked-microvia wording
  - limit: internal support only; not a substitute for a dated trace/space capability record

### C. Non-Claim Boundaries

These sources are important because they explicitly block overreach.

- [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md)
  - boundary: reusable capability numbers require a `Tier 1 internal dated capability record`
  - boundary: forbids marketing-page leakage, stale undated shop numbers, standards thresholds disguised as capability, and SI numerics disguised as manufacturability
- [h2-capability-number-inventory.md](/code/blogs/llm_wiki/logs/h2-capability-number-inventory.md)
  - boundary: `trace_space` is already marked `needs_dated_internal_capability_source`
  - boundary: forbids inference from marketing prose, laminate datasheets, or HDI vocabulary pages
- [layer-count-blog-readiness.md](/code/blogs/llm_wiki/logs/layer-count-blog-readiness.md)
  - boundary: current corpus is weak for numeric process capability tables
  - boundary: `20-layer` and related drafts remain blocked partly because of unsupported geometry tables and factory-specific promises
- [h0-numeric-claim-inventory.md](/code/blogs/llm_wiki/logs/h0-numeric-claim-inventory.md)
  - boundary: identifies the demand-side trace/space claims currently sitting in `needs_source`, `downgrade`, or `delete`
  - boundary: clarifies where geometry claims are really standards leakage or SI-table leakage instead of pure capability numerics

### D. Candidate Upstream Inputs For A Future Dated Capability Record

These inputs may help identify owner, scope, and family boundaries for a future `Tier 1` record. They do not authorize feature-size numbers by themselves.

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-rigid-pcb-capability-page-en.md`
  - candidate role: feeder for general rigid-multilayer scope and owner mapping
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-hdi-pcb-capability-page-en.md`
  - candidate role: feeder for HDI-specific scope and fine-line family separation
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-hdi-pcb-page-en.md`
  - candidate role: feeder for HDI product-language alignment and scope vocabulary
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
  - candidate role: feeder for advanced-manufacturing process-family routing
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-multilayer-pcb-page-en.md`
  - candidate role: feeder for multilayer family mapping
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-high-layer-count-pcb-page-en.md`
  - candidate role: feeder for high-layer-count scope and exception handling
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-hdi-pcb-product-page-en.md`
  - candidate role: feeder for HIL-side public wording and cross-site consistency checks
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-ic-substrate-pcb-product-page-en.md`
  - candidate role: feeder for explicit separation between substrate fine-line posture and ordinary PCB capability

## Sources That Explicitly Require Refresh Or Do Not Authorize Transferable Feature-Size Numbers

The following sources already contain explicit boundary language that blocks direct numeric reuse:

- [advanced-pcb-fabrication-and-stackup-planning.md](/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md)
  - explicitly says exact `line/space` must refresh before publishing
- [apt-capability-family-map-and-boundaries.md](/code/blogs/llm_wiki/wiki/processes/apt-capability-family-map-and-boundaries.md)
  - explicitly says trust-bar figures, FAQ windows, and table limits on capability pages are refresh-sensitive internal claims
- [hdi-microvia-and-vippo-process-posture.md](/code/blogs/llm_wiki/facts/methods/hdi-microvia-and-vippo-process-posture.md)
  - explicitly says microvia size and related figures are refresh-sensitive internal claims
- [ic-substrate-fine-line-build-up-posture.md](/code/blogs/llm_wiki/facts/methods/ic-substrate-fine-line-build-up-posture.md)
  - explicitly says line/space values are refresh-sensitive and not transferable to general PCB
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-hdi-pcb-capability-page-en.md`
  - extraction notes already warn that line/space details are refresh-sensitive internal claims
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-hdi-pcb-page-en.md`
  - extraction notes already warn that all numeric capability claims are refresh-required before publication
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-ic-substrate-pcb-product-page-en.md`
  - extraction notes already warn that line/space values are refresh-sensitive and internal-support-only

## What Is Still Missing

The missing item is not more vocabulary. The missing item is a governed numeric authority.

Still missing:

- a registered `Tier 1 internal dated capability record` for trace/space
- explicit scope separating rigid multilayer, HDI, and IC-substrate geometry
- explicit distinction between outer-layer, inner-layer, standard-production, and advanced-process windows
- usable date, owner, and refresh posture for any future feature-size record
- evidence that a cited number is a maintained capability record rather than a marketing or routing-page residue

Without those items, all reusable trace/space numbers remain `needs_source`.

## Recommended Future Ingestion Order

1. Recover or register the missing `Tier 1 internal dated capability record` for trace/space.
2. Verify that the record cleanly splits rigid multilayer, HDI, and IC-substrate geometry rather than collapsing them into one ladder.
3. Only after that, use the current internal registry pages as framing cross-checks for family names, scope wording, and downstream blog routing.
4. Re-run the H0/H2 demand split so each blocked claim is sorted into `shop feature-size capability`, `HDI posture`, `IC-substrate posture`, `standards threshold`, or `SI geometry table`.
5. Only after steps `1-4` should any trace/space fact card be considered.

Current ingestion stop/go posture:

- `keep`: boundary and posture support already in corpus
- `downgrade`: internal capability-family wording without numeric promotion
- `needs_source`: all reusable trace/space numerics
- `delete`: standards or SI geometry claims disguised as shop feature-size capability
