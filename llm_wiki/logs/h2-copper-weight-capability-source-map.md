# H2 Copper Weight Capability Source Map

Date: 2026-04-25

## Purpose

This document maps the current corpus for the `copper_weight_capability` H2 child bucket.

Its job is to show which sources can support posture, framing, and non-claim boundaries today, and which upstream inputs might later feed a dated capability record.

This file is not:

- a copper-weight fact card
- a numeric recovery memo
- permission to reuse copper-weight numbers from existing pages

## Current Source Classification

### A. Downgrade / Framing Support

These sources are useful for heavy-copper route framing, special-process routing, and guarded internal posture. They do not authorize transferable copper-weight numbers.

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
  - use: heavy-copper manufacturing-family framing for power and thermal builds
  - limit: extraction notes already treat ounce and reliability limits as refresh-sensitive internal claims
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-heavy-copper-pcb-product-page-en.md`
  - use: HIL-side corroboration for heavy-copper route framing
  - limit: extraction notes already treat copper-weight and load-test numbers as refresh-sensitive internal claims
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
  - use: advanced-process aggregation point where heavy copper appears as one special route
  - limit: numeric figures and production scope remain internal capability framing only
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-pcb-fabrication-process-page-en.md`
  - use: fabrication-process backbone and plating/process routing context
  - limit: process prose is not a maintained copper-weight capability table

### B. Posture Support

These sources are valid for showing that the repo already has controlled posture support around heavy-copper manufacturing decisions. They still do not authorize reusable copper-weight numbers.

- [pcb-service-routing-from-prototype-to-special-process.md](/code/blogs/llm_wiki/wiki/processes/pcb-service-routing-from-prototype-to-special-process.md)
  - supports: heavy copper as a separate power and thermal route instead of a generic default
  - limit: explicitly says exact copper-weight values must refresh before publication
- [pcb-stackup-special-process-and-baseline-families.md](/code/blogs/llm_wiki/facts/methods/pcb-stackup-special-process-and-baseline-families.md)
  - supports: baseline laminate families, stackup planning, and heavy-copper route separation
  - limit: explicitly says copper-weight claims must refresh before publication
- [thermal-pcb-platform-selection-posture.md](/code/blogs/llm_wiki/facts/methods/thermal-pcb-platform-selection-posture.md)
  - supports: heavy copper, MCPCB, and ceramic as distinct thermal platforms
  - limit: explicitly says conductivity, temperature, and load figures are refresh-sensitive internal claims

### C. Supplier / Application-Note Boundary Inputs

These sources are useful because they show where material or application framing can be over-read as factory capability. They are not reusable capability proof.

- `/code/blogs/llm_wiki/sources/registry/materials/arlon-heavy-copper-layers-application-page.md`
  - boundary value: heavy-copper application context and source discovery only, not fabrication authority
- `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro4835t-ro4450t-multilayer-processing-guide.md`
  - boundary value: process-guide workflow must not be rewritten as generic copper-weight capability

### D. Governance Boundaries

These sources are important because they explicitly block overreach.

- [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md)
  - boundary: reusable capability numbers require a `Tier 1 internal dated capability record`
  - boundary: forbids recipe leakage, stale internal numerics, and process prose from becoming H2 capability facts
- [h2-capability-number-inventory.md](/code/blogs/llm_wiki/logs/h2-capability-number-inventory.md)
  - boundary: mixed copper/plating claims were already flagged as `hold_until_bucket_split`
  - boundary: copper-weight windows were one of the original mixed claim shapes
- [h2-copper-plating-process-windows-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-copper-plating-process-windows-bucket-decision.md)
  - boundary: `copper_weight_capability` is only one child family from the previously held mixed bucket
  - boundary: plating thickness, etch compensation, standards minima, and recipe leakage must remain separate

## Sources That Explicitly Require Refresh Or Do Not Authorize Transferable Copper-Weight Numbers

The following sources already contain explicit boundary language that blocks direct numeric reuse:

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
  - extraction notes already warn that ounce, plating, and reliability limits must be re-verified before external publication
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-heavy-copper-pcb-product-page-en.md`
  - extraction notes already warn that copper-weight and load-test numbers are refresh-sensitive internal claims
- [pcb-service-routing-from-prototype-to-special-process.md](/code/blogs/llm_wiki/wiki/processes/pcb-service-routing-from-prototype-to-special-process.md)
  - explicitly requires refresh of exact copper-weight values before publication
- [pcb-stackup-special-process-and-baseline-families.md](/code/blogs/llm_wiki/facts/methods/pcb-stackup-special-process-and-baseline-families.md)
  - explicitly requires refresh of copper-weight and other capability claims before publication
- [thermal-pcb-platform-selection-posture.md](/code/blogs/llm_wiki/facts/methods/thermal-pcb-platform-selection-posture.md)
  - explicitly requires refresh of conductivity, temperature, and load figures
- `/code/blogs/llm_wiki/sources/registry/materials/arlon-heavy-copper-layers-application-page.md`
  - explicitly says not to extract copper-processing values without current datasheets

## Candidate Upstream Inputs For A Future Dated Capability Record

These inputs may help identify owner, scope, and family boundaries for a future `Tier 1` record. They do not authorize copper-weight numbers by themselves.

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
  - candidate role: primary heavy-copper product-family anchor for scope and owner mapping
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-heavy-copper-pcb-product-page-en.md`
  - candidate role: HIL-side public wording cross-check and route consistency
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
  - candidate role: special-process family routing and exception handling
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-pcb-fabrication-process-page-en.md`
  - candidate role: process-family routing and ownership hints for where maintained records may live

These are only candidate upstream inputs because they are:

- internal
- semi-stable
- undated as capability records
- mixed with power, thermal, plating, or process-language context

## What Is Still Missing

The missing item is not more heavy-copper vocabulary. The missing item is a governed numeric authority.

Still missing:

- a registered `Tier 1 internal dated capability record` for finished copper-weight capability
- explicit separation between finished copper weight and plating/build allowance
- explicit separation between copper-weight capability and current/thermal application context
- explicit distinction between stackup copper examples and maintained capability windows
- usable date, owner, and refresh posture for any future copper-weight record
- evidence that a cited number is a maintained capability record rather than internal product-page residue or one application example

Without those items, all reusable copper-weight numbers remain `needs_source`.

## Recommended Future Ingestion Order

1. Start with the internal heavy-copper product family:
   - `frontendapt-pcb-heavy-copper-pcb-page-en`
   - `frontendhil-heavy-copper-pcb-product-page-en`
2. Use `advanced-pcb-manufacturing` and `pcb-fabrication-process` only as routing and owner cross-checks, not numeric authorities.
3. Use the current wiki and method pages as posture support so heavy-copper framing stays separate from baseline FR-4, MCPCB, and ceramic routes.
4. Keep supplier heavy-copper application pages as boundary control only.
5. Only after steps `1-4`, decide whether a real dated capability record can be created.

Current ingestion stop/go posture:

- `keep`: boundary and posture support already in corpus
- `downgrade`: internal heavy-copper route framing, special-process routing, and supplier application context without numeric promotion
- `needs_source`: all reusable copper-weight numerics
- `delete`: stackup examples or supplier application context rewritten as transferable shop capability
