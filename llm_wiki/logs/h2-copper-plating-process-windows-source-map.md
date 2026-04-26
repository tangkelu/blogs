# H2 Copper Plating Process Windows Source Map

Date: 2026-04-25

## Purpose

This document maps the current corpus for the held `copper_plating_process_windows` area.

Its job is to show which sources can support posture, framing, and non-claim boundaries today, and why this area still cannot be treated as one reusable numeric bucket.

This file is not:

- a copper/plating fact card
- a numeric recovery memo
- permission to reuse copper-weight, plating, or compensation values from existing pages

## Current Source Classification

### A. Downgrade / Framing Support

These sources are useful for process-family routing, heavy-copper posture, and guarded fabrication framing. They do not authorize transferable mixed copper/plating numerics.

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
  - use: heavy-copper manufacturing-family framing
  - limit: process-capability claims remain internal support only
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-heavy-copper-pcb-product-page-en.md`
  - use: HIL-side heavy-copper and special-process framing
  - limit: internal product-page posture only; not a numeric authority
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
  - use: advanced-process aggregation across heavy copper, sequential lamination, VIPPO, and related special routes
  - limit: numeric figures and production scope remain internal capability framing only
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-pcb-fabrication-process-page-en.md`
  - use: fabrication-process backbone including plating process language
  - limit: process prose is not a maintained capability table

### B. Posture Support

These sources are valid for showing that the repo already has controlled posture support around copper/plating-adjacent process families. They still do not authorize reusable numerics.

- [selective-multi-finish-strategy.md](/code/blogs/llm_wiki/facts/methods/selective-multi-finish-strategy.md)
  - supports: finish/plating workflow separation and chemistry-sensitive review posture
  - limit: explicitly does not authorize exact process or thickness windows
- [mcpcb-ims-and-reflow-source-coverage.md](/code/blogs/llm_wiki/facts/methods/mcpcb-ims-and-reflow-source-coverage.md)
  - supports: thermal-platform and metal-core source coverage boundaries
  - limit: does not prove generic rigid-board copper/plating capability
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-metal-core-pcb-page-en.md`
  - supports: IMS / thermal-platform process posture
  - limit: platform-specific context only; not generic plating authority
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-metal-core-pcb-product-page-en.md`
  - supports: HIL-side metal-core posture
  - limit: internal support only; not transferable numeric authority

### C. Supplier Or Process-Note Boundary Inputs

These sources are useful because they show where recipe or application-note leakage can happen. They are not reusable capability proof.

- `/code/blogs/llm_wiki/sources/registry/materials/arlon-heavy-copper-layers-application-page.md`
  - boundary value: heavy-copper application context must not be rewritten as factory default capability
- `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro4835t-ro4450t-multilayer-processing-guide.md`
  - boundary value: process-guide context must not be converted into generic plating or build-window claims

### D. Standards Boundary Support

These sources are important because they explicitly block standards leakage.

- [ipc-finish-standards-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-finish-standards-metadata.md)
  - boundary: public finish-standard metadata does not provide transferable thickness or minima tables
- [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md)
  - boundary: forbids standards minima, recipe leakage, and stale internal process numbers from becoming H2 capability facts
- [h2-capability-number-inventory.md](/code/blogs/llm_wiki/logs/h2-capability-number-inventory.md)
  - boundary: explicitly marks `copper_plating_process_windows` as `hold_until_bucket_split`

## Why Current Sources Do Not Authorize One Unified Numeric Bucket

Current sources are mixed across:

- heavy-copper product posture
- fabrication-process prose
- finish/plating workflow context
- thermal-platform product framing
- supplier application-note context
- standards metadata

That means the current corpus can support:

- posture and boundary control
- future split planning

It cannot support:

- one combined capability ladder for copper weight and plating
- one reusable process-window table
- one transferable build-allowance or compensation layer

## Candidate Split Families For Future Work

If later work continues here, claims must first be split into:

1. `copper weight capability`
2. `plating thickness / build allowance`
3. `etch compensation`
4. `resin-fill / balance / heavy-copper process claims`
5. `standards minima`
6. `recipe / process-window leakage`

Each future family would need its own:

- bucket-decision file
- source-map file
- `Tier 1 internal dated capability record` if numeric recovery is attempted

## Sources That Explicitly Require Refresh Or Do Not Authorize Transferable Mixed Copper/Plating Numerics

The following sources already contain explicit boundary language that blocks direct numeric reuse:

- [selective-multi-finish-strategy.md](/code/blogs/llm_wiki/facts/methods/selective-multi-finish-strategy.md)
  - explicitly says chemistry limits and exact plating-stack thickness need higher-trust refresh
- [ipc-finish-standards-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-finish-standards-metadata.md)
  - explicitly does not provide finish thickness or acceptance thresholds
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-pcb-fabrication-process-page-en.md`
  - process framing only; not a maintained capability source
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
  - internal product-family posture only; not a unified numeric authority
- `/code/blogs/llm_wiki/sources/registry/materials/arlon-heavy-copper-layers-application-page.md`
  - application-page context only; not shop capability evidence
- `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro4835t-ro4450t-multilayer-processing-guide.md`
  - process-guide context only; not transferable production authority

## What Is Still Missing

The missing item is not more process vocabulary. The missing item is a safe split plus governed numeric authority.

Still missing:

- a clean split into narrower sub-buckets
- a registered `Tier 1 internal dated capability record` for any narrower sub-bucket that attempts numeric recovery
- explicit separation between standards minima and shop capability
- explicit separation between process examples and maintained capability windows
- explicit separation between heavy-copper special-process context and generic rigid-board capability
- usable date, owner, scope, and refresh posture for any future narrow record

Without those items, `copper_plating_process_windows` remains `hold-until-split`.

## Current Ingestion Stop/Go Posture

- `keep`: boundary and posture support already in corpus
- `downgrade`: internal process-family framing, heavy-copper posture, and supplier process-note context without numeric promotion
- `hold-until-split`: the overall mixed copper/plating area
- `delete`: standards minima or recipe examples disguised as transferable capability
