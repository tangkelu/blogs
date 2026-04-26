# H2 Plating Thickness Build Allowance Source Map

Date: 2026-04-25

## Purpose

This document maps the current corpus for the `plating_thickness_build_allowance` H2 child bucket.

Its job is to show which sources can support posture, framing, and non-claim boundaries today, and which upstream inputs might later feed a dated capability record.

This file is not:

- a plating-build fact card
- a numeric recovery memo
- permission to reuse plating-thickness or build-allowance numbers from existing pages

## Current Source Classification

### A. Downgrade / Framing Support

These sources are useful for heavy-copper route framing, fabrication-process posture, and guarded internal process context. They do not authorize transferable plating-thickness/build-allowance numbers.

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
  - use: heavy-copper manufacturing-family framing where plating-related process complexity appears
  - limit: extraction notes already treat ounce, plating, and reliability limits as refresh-sensitive internal claims
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
  - use: advanced-process aggregation where heavy copper and special routes are grouped
  - limit: numeric figures and production scope remain internal capability framing only
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-pcb-fabrication-process-page-en.md`
  - use: fabrication-process backbone including plating process language
  - limit: process prose is not a maintained plating-build capability table

### B. Posture Support

These sources are valid for showing that the repo already has controlled posture support around finish/plating workflow boundaries and special-process separation. They still do not authorize reusable plating-build numerics.

- [selective-multi-finish-strategy.md](/code/blogs/llm_wiki/facts/methods/selective-multi-finish-strategy.md)
  - supports: finish zoning and process-sequence posture
  - limit: explicitly says exact plating-stack thickness by zone needs higher-trust refresh
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-surface-finishes-page-en.md`
  - supports: internal finish-selection framing and finish vocabulary
  - limit: extraction notes explicitly say finish thickness claims must be re-verified against stronger sources
- [mcpcb-ims-and-reflow-source-coverage.md](/code/blogs/llm_wiki/facts/methods/mcpcb-ims-and-reflow-source-coverage.md)
  - supports: thermal-platform and process layering boundaries
  - limit: not generic plated-copper authority

### C. Standards Boundary Support

These sources are important because they explicitly block standards leakage.

- [ipc-finish-standards-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-finish-standards-metadata.md)
  - boundary: public IPC finish metadata does not provide thickness, process limits, or acceptance tables
- [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md)
  - boundary: reusable capability numbers require a `Tier 1 internal dated capability record`
  - boundary: forbids standards minima, finish-page leakage, and stale internal process numerics from becoming H2 capability facts
- [h2-copper-plating-process-windows-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-copper-plating-process-windows-bucket-decision.md)
  - boundary: plating-thickness/build-allowance is only one child family from the previously held mixed bucket
  - boundary: copper weight, etch compensation, standards minima, and recipe leakage must remain separate

### D. Supplier / Process-Guide Boundary Inputs

These sources are useful because they show where named process examples can be misused as factory defaults. They are not reusable capability proof.

- `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro4835t-ro4450t-multilayer-processing-guide.md`
  - boundary value: named multilayer process guidance is not a universal plating-build rule
- `/code/blogs/llm_wiki/sources/registry/materials/arlon-heavy-copper-layers-application-page.md`
  - boundary value: heavy-copper application context is source discovery only, not plating-build authority

## Sources That Explicitly Require Refresh Or Do Not Authorize Transferable Plating-Build Numbers

The following sources already contain explicit boundary language that blocks direct numeric reuse:

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
  - extraction notes already warn that plating limits must be re-verified before external publication
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-surface-finishes-page-en.md`
  - extraction notes already warn that finish thickness claims need stronger source verification
- [selective-multi-finish-strategy.md](/code/blogs/llm_wiki/facts/methods/selective-multi-finish-strategy.md)
  - explicitly says exact plating-stack thickness needs higher-trust refresh
- [ipc-finish-standards-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-finish-standards-metadata.md)
  - explicitly says it does not provide finish thickness or acceptance criteria
- [mcpcb-ims-and-reflow-source-coverage.md](/code/blogs/llm_wiki/facts/methods/mcpcb-ims-and-reflow-source-coverage.md)
  - explicitly says platform/material/process windows must remain tied to the correct source layer

## Candidate Upstream Inputs For A Future Dated Capability Record

These inputs may help identify owner, scope, and family boundaries for a future `Tier 1` record. They do not authorize plating-build numbers by themselves.

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
  - candidate role: heavy-copper product-family anchor where plating-build capability may be mentioned
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
  - candidate role: advanced-process family routing and owner mapping
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-pcb-fabrication-process-page-en.md`
  - candidate role: fabrication-process routing and measurement-basis hints
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-surface-finishes-page-en.md`
  - candidate role: finish/plating boundary control so finish-stack claims do not contaminate plated-copper capability

These are only candidate upstream inputs because they are:

- internal
- semi-stable
- undated as capability records
- mixed with finish, process, heavy-copper, or application-language context

## What Is Still Missing

The missing item is not more process vocabulary. The missing item is a governed numeric authority.

Still missing:

- a registered `Tier 1 internal dated capability record` for plating-thickness/build-allowance capability
- explicit separation between plated buildup and finished copper-weight capability
- explicit separation between plated buildup and finish-stack specification
- explicit separation between plated buildup and etch-compensation allowances
- usable date, owner, scope, measurement basis, and refresh posture for any future plating-build record
- evidence that a cited number is a maintained capability record rather than finish-page residue or one process example

Without those items, all reusable plating-thickness/build-allowance numbers remain `needs_source`.

## Recommended Future Ingestion Order

1. Start with the internal fabrication/process family:
   - `frontendapt-pcb-heavy-copper-pcb-page-en`
   - `frontendapt-pcb-advanced-pcb-manufacturing-page-en`
   - `frontendapt-pcb-pcb-fabrication-process-page-en`
2. Use finish pages and finish method/standards cards only as boundary control so finish-stack wording does not leak into plated-copper capability.
3. Keep metal-core/IMS cards as thermal-platform separation only.
4. Keep supplier process guides as named-context boundaries only.
5. Only after steps `1-4`, decide whether a real dated capability record can be created.

Current ingestion stop/go posture:

- `keep`: boundary and posture support already in corpus
- `downgrade`: internal process-family framing, finish/plating workflow context, and supplier process-guide context without numeric promotion
- `needs_source`: all reusable plating-thickness/build-allowance numerics
- `delete`: finish-stack, standards-minimum, or recipe-example claims rewritten as transferable shop capability
