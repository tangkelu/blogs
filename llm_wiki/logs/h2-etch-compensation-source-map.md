# H2 Etch Compensation Source Map

Date: 2026-04-25

## Purpose

This document maps the current corpus for the `etch_compensation` H2 child bucket.

Its job is to show which sources can support posture, framing, and non-claim boundaries today, and which upstream inputs might later feed a dated capability record.

This file is not:

- an etch-compensation fact card
- a numeric recovery memo
- permission to reuse etch-compensation numbers from existing pages

## Current Source Classification

### A. Downgrade / Framing Support

These sources are useful for heavy-copper route framing, advanced-process posture, and guarded conductor-formation context. They do not authorize transferable etch-compensation numbers.

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
  - use: heavy-copper manufacturing-family framing where conductor-formation and process-adjustment language may appear
  - limit: extraction notes already treat ounce, plating, and reliability limits as refresh-sensitive internal claims
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-heavy-copper-pcb-product-page-en.md`
  - use: HIL-side corroboration for heavy-copper special-process framing
  - limit: internal product-page posture only; not numeric authority
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
  - use: advanced-process aggregation where heavy copper appears as one special route
  - limit: numeric figures and production scope remain internal capability framing only
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-pcb-fabrication-process-page-en.md`
  - use: fabrication-process backbone and process-routing context
  - limit: process prose is not a maintained etch-compensation capability table

### B. Posture Support

These sources are valid for showing that the repo already has controlled posture support around process-adjustment language and special-process separation. They still do not authorize reusable etch-compensation numerics.

- [pcb-stackup-special-process-and-baseline-families.md](/code/blogs/llm_wiki/facts/methods/pcb-stackup-special-process-and-baseline-families.md)
  - supports: heavy-copper and special-process route separation
  - limit: explicitly says numeric capability claims must refresh before publication
- [h2-copper-plating-process-windows-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-copper-plating-process-windows-bucket-decision.md)
  - supports: the original split discipline for the copper/plating cluster
  - limit: mixed process windows still remain blocked unless narrowed
- [h2-copper-weight-capability-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-copper-weight-capability-bucket-decision.md)
  - supports: copper-weight boundary so ounce ladders do not contaminate etch claims
  - limit: copper-weight authority is separate and still blocked
- [h2-plating-thickness-build-allowance-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-plating-thickness-build-allowance-bucket-decision.md)
  - supports: plated-buildup boundary so build allowances do not contaminate etch claims
  - limit: plating-build authority is separate and still blocked

### C. Geometry And Standards Boundary Inputs

These sources are useful because they block geometry or standards leakage. They are not reusable etch-compensation proof.

- [h2-trace-space-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-trace-space-bucket-decision.md)
  - boundary value: feature-size capability must not be reconstructed from adjacent geometry language
- [h2-trace-space-source-map.md](/code/blogs/llm_wiki/logs/h2-trace-space-source-map.md)
  - boundary value: width/spacing and geometry examples are not generic process capability proof
- [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md)
  - boundary value: reusable capability numbers require a `Tier 1 internal dated capability record`
  - boundary value: forbids standards thresholds, recipe leakage, and stale process numerics from becoming H2 facts

### D. Supplier / Process-Guide Boundary Inputs

These sources are useful because they show where named process examples can be misused as factory defaults. They are not reusable capability proof.

- `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro4835t-ro4450t-multilayer-processing-guide.md`
  - boundary value: named multilayer process guidance is not a universal etch-compensation rule
- `/code/blogs/llm_wiki/sources/registry/materials/arlon-heavy-copper-layers-application-page.md`
  - boundary value: heavy-copper application context is source discovery only, not etch-compensation authority

## Sources That Explicitly Require Refresh Or Do Not Authorize Transferable Etch-Compensation Numbers

The following sources already contain explicit boundary language that blocks direct numeric reuse:

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
  - extraction notes already warn that ounce, plating, and reliability limits must be re-verified before external publication
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
  - extraction notes already warn that numeric figures and production scope are internal capability framing only
- [pcb-stackup-special-process-and-baseline-families.md](/code/blogs/llm_wiki/facts/methods/pcb-stackup-special-process-and-baseline-families.md)
  - explicitly requires refresh of copper-weight and other capability claims before publication
- [h2-trace-space-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-trace-space-bucket-decision.md)
  - explicitly blocks geometry tables and adjacent process/DFM leakage from becoming feature-size authority
- `/code/blogs/llm_wiki/sources/registry/materials/arlon-heavy-copper-layers-application-page.md`
  - explicitly says not to extract copper-processing values without current datasheets

## Candidate Upstream Inputs For A Future Dated Capability Record

These inputs may help identify owner, scope, and family boundaries for a future `Tier 1` record. They do not authorize etch-compensation numbers by themselves.

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
  - candidate role: heavy-copper product-family anchor where process-adjustment language may surface
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
  - candidate role: advanced-process family routing and owner mapping
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-pcb-fabrication-process-page-en.md`
  - candidate role: fabrication-process routing and measurement-basis hints

These are only candidate upstream inputs because they are:

- internal
- semi-stable
- undated as capability records
- mixed with copper-weight, plating, reliability, or broader process-language context

## What Is Still Missing

The missing item is not more process vocabulary. The missing item is a governed numeric authority.

Still missing:

- a registered `Tier 1 internal dated capability record` for etch-compensation capability
- explicit separation between etch-compensation and finished copper-weight capability
- explicit separation between etch-compensation and plated buildup/build allowance
- explicit separation between etch-compensation and trace/space or impedance geometry examples
- usable date, owner, process-family scope, measurement basis, and refresh posture for any future etch record
- evidence that a cited number is a maintained capability record rather than one geometry example or one process note

Without those items, all reusable etch-compensation numbers remain `needs_source`.

## Recommended Future Ingestion Order

1. Start with the internal process family:
   - `frontendapt-pcb-heavy-copper-pcb-page-en`
   - `frontendapt-pcb-advanced-pcb-manufacturing-page-en`
   - `frontendapt-pcb-pcb-fabrication-process-page-en`
2. Use the copper-weight and plating-build child-bucket docs as boundary control so adjacent child families do not collapse back together.
3. Use trace/space docs as geometry boundary control so etch-adjustment language does not become feature-size authority.
4. Keep supplier heavy-copper and process-guide pages as named-context boundaries only.
5. Only after steps `1-4`, decide whether a real dated capability record can be created.

Current ingestion stop/go posture:

- `keep`: boundary and posture support already in corpus
- `downgrade`: internal special-process framing and supplier process-guide context without numeric promotion
- `needs_source`: all reusable etch-compensation numerics
- `delete`: geometry tables, recipe examples, or supplier process notes rewritten as transferable shop capability
