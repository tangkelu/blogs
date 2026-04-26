# H2 Resin Fill Balance Heavy Copper Process Claims Source Map

Date: 2026-04-25

## Purpose

This document maps the current corpus for the `resin_fill_balance_heavy_copper_process_claims` containment area.

Its job is to show which sources can support special-process vocabulary, route framing, and non-claim boundaries today, and why process-note claims in this area still cannot be treated as reusable capability numerics.

This file is not:

- a process-claim fact card
- a numeric recovery memo
- permission to reuse resin-fill, balance, planarization, or copper-coin numbers from existing pages

## Current Source Classification

### A. Downgrade / Framing Support

These sources are useful for heavy-copper route framing and advanced special-process posture. They do not authorize transferable numeric process claims.

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
  - use: heavy-copper manufacturing-family framing
  - limit: process-capability claims remain internal support only
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-heavy-copper-pcb-product-page-en.md`
  - use: HIL-side corroboration for heavy-copper route framing
  - limit: internal product-page posture only; not numeric authority
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
  - use: advanced-process aggregation across heavy copper, copper coin, and other special routes
  - limit: numeric figures and production scope remain internal capability framing only

### B. Posture Support

These sources are valid for showing that the repo already has controlled posture support around special-process heavy-copper routing. They still do not authorize reusable numerics.

- [pcb-stackup-special-process-and-baseline-families.md](/code/blogs/llm_wiki/facts/methods/pcb-stackup-special-process-and-baseline-families.md)
  - supports: heavy-copper and special-process route separation
  - limit: explicitly says numeric capability claims must refresh before publication
- [thermal-pcb-platform-selection-posture.md](/code/blogs/llm_wiki/facts/methods/thermal-pcb-platform-selection-posture.md)
  - supports: heavy copper as one distinct thermal platform
  - limit: explicitly says load and performance figures are refresh-sensitive internal claims
- [h2-copper-plating-process-windows-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-copper-plating-process-windows-bucket-decision.md)
  - supports: the original split discipline for the copper/plating cluster
  - limit: mixed process windows remain blocked unless narrowed

### C. Supplier / Application Boundary Inputs

These sources are useful because they show where special-process application notes can be misused as factory defaults. They are not reusable capability proof.

- `/code/blogs/llm_wiki/sources/registry/materials/arlon-heavy-copper-layers-application-page.md`
  - boundary value: heavy-copper application context and source discovery only, not shop capability evidence

### D. Governance Boundaries

These sources explicitly explain why this area stays contained.

- [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md)
  - boundary: reusable capability numbers require a `Tier 1 internal dated capability record`
  - boundary: forbids process-note leakage and stale internal process numerics from becoming H2 capability facts
- [h2-copper-weight-capability-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-copper-weight-capability-bucket-decision.md)
  - boundary: copper-weight claims are a separate child family
- [h2-plating-thickness-build-allowance-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-plating-thickness-build-allowance-bucket-decision.md)
  - boundary: plated-buildup claims are a separate child family
- [h2-etch-compensation-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-etch-compensation-bucket-decision.md)
  - boundary: etch-adjustment claims are a separate child family

## Why Current Sources Do Not Authorize Reusable Numeric Process Claims

Current sources are mixed across:

- internal heavy-copper product posture
- advanced-process summaries
- application-note discovery pages
- special-process and thermal-platform method cards

That means the current corpus can support:

- special-process vocabulary
- route framing
- process-leakage control

It cannot support:

- reusable resin-fill numerics
- reusable balance or planarization rules
- reusable copper-coin process windows
- transferable heavy-copper special-process tables

## Candidate Split Families For Future Work

If later work continues here, claims must first be split into:

1. `resin-fill or fill-balance notes`
2. `planarization or copper-balance workflow`
3. `copper coin or special thermal-path process notes`
4. `heavy-copper route sequence examples`

Only a very narrow future family with a real `Tier 1 internal dated capability record` could ever attempt numeric recovery.

## Sources That Explicitly Require Refresh Or Do Not Authorize Transferable Numeric Process Claims

The following sources already contain explicit boundary language that blocks direct numeric reuse:

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
  - extraction notes already warn that ounce, plating, and reliability limits must be re-verified before external publication
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-heavy-copper-pcb-product-page-en.md`
  - extraction notes already warn that copper-weight and load-test numbers are refresh-sensitive internal claims
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
  - extraction notes already warn that numeric figures and production scope are internal capability framing only
- [pcb-stackup-special-process-and-baseline-families.md](/code/blogs/llm_wiki/facts/methods/pcb-stackup-special-process-and-baseline-families.md)
  - explicitly requires refresh of copper-weight and other capability claims before publication
- `/code/blogs/llm_wiki/sources/registry/materials/arlon-heavy-copper-layers-application-page.md`
  - explicitly says not to extract resin, press, or copper-processing values without current datasheets

## What Is Still Missing

The missing item is not more heavy-copper vocabulary. The missing item is clean containment plus governed numeric authority for any very narrow future process claim.

Still missing:

- narrower child-family decisions with clean scope boundaries
- explicit separation between special-process notes and maintained production rules
- explicit separation between application-note context and shop authority
- a registered `Tier 1 internal dated capability record` for any future narrow process claim
- usable date, owner, scope, and refresh posture for any future narrow record
- evidence that a cited number is maintained capability rather than route or application-note residue

Without those items, `resin_fill_balance_heavy_copper_process_claims` remains a containment area, not a reusable H2 numeric bucket.

## Current Ingestion Stop/Go Posture

- `keep`: special-process vocabulary and route framing in the correct layer
- `downgrade`: internal heavy-copper posture and application context without numeric promotion
- `hold`: process-leakage containment for special-process numerics
- `delete`: application-note or route-example claims rewritten as reusable factory defaults
