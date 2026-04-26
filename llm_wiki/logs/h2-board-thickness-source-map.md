# H2 Board Thickness Source Map

Date: 2026-04-25

## Purpose

This document maps the current corpus for the `board_thickness` H2 bucket.

Its job is to show which sources can support posture, framing, and non-claim boundaries today, and which upstream inputs might later feed a dated capability record.

This file is not:

- a board-thickness fact card
- a numeric recovery memo
- permission to reuse thickness numbers from existing pages

## Current Source Classification

### A. Downgrade / Framing Support

These sources are useful for vocabulary, process-family routing, and guarded framing. They do not authorize transferable board-thickness numbers.

- [advanced-pcb-fabrication-and-stackup-planning.md](/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md)
  - use: separates rigid, HDI, rigid-flex, thermal-platform, and substrate planning frames
  - limit: explicitly marks internal numeric capabilities and related process numbers as refresh-sensitive
- [prototype-vs-quick-turn-pcb-routing.md](/code/blogs/llm_wiki/wiki/processes/prototype-vs-quick-turn-pcb-routing.md)
  - use: separates schedule posture from build-complexity posture
  - limit: does not authorize finished-board thickness defaults for quick-turn or prototype lanes
- [high-layer-rigid-board-manufacturability-context.md](/code/blogs/llm_wiki/facts/methods/high-layer-rigid-board-manufacturability-context.md)
  - use: supports guarded high-layer manufacturability and dimensional-control wording
  - limit: explicitly does not provide board-thickness limits or capability tables
- [frontendapt-pcb-multi-layer-laminated-structure-page-en.md](/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-multi-layer-laminated-structure-page-en.md)
  - use: lamination-process and stackup-construction vocabulary
  - limit: stackup complexity framing only; not a finished-board capability source
- [frontendapt-pcb-multilayer-pcb-page-en.md](/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-multilayer-pcb-page-en.md)
  - use: multilayer build framing and process-family context
  - limit: extraction notes already treat thickness figures as internal claims
- [frontendhil-multilayer-pcb-product-page-en.md](/code/blogs/llm_wiki/sources/registry/internal/frontendhil-multilayer-pcb-product-page-en.md)
  - use: HIL-side multilayer stackup and build-complexity framing
  - limit: process-capability numbers remain internal support only

### B. Posture Support

These sources are valid for showing that the repo already has controlled posture support around thickness-sensitive manufacturing decisions. They still do not authorize reusable board-thickness numbers.

- [frontendapt-pcb-rigid-flex-pcb-page-en.md](/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-rigid-flex-pcb-page-en.md)
  - supports: rigid-flex stackup and bend-related posture
  - limit: total-thickness and bend claims are refresh-sensitive internal claims
- [frontendhil-rigid-flex-pcb-product-page-en.md](/code/blogs/llm_wiki/sources/registry/internal/frontendhil-rigid-flex-pcb-product-page-en.md)
  - supports: rigid-flex integration and dynamic-bend posture
  - limit: registration and class-linked wording remain internal support only
- [frontendapt-pcb-metal-core-pcb-page-en.md](/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-metal-core-pcb-page-en.md)
  - supports: thermal-platform and IMS manufacturing posture
  - limit: base-thickness or conductivity-like values are internal claims, not generic rigid-board authority
- [frontendapt-pcb-fr4-pcb-page-en.md](/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-fr4-pcb-page-en.md)
  - supports: mainstream FR-4 manufacturing posture
  - limit: marketing framing and capability claims remain refresh-sensitive
- [frontendapt-pcb-high-tg-pcb-page-en.md](/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-high-tg-pcb-page-en.md)
  - supports: higher-thermal-demand rigid-board posture
  - limit: temperature, layer-count, and tolerance-like claims remain refresh-sensitive

### C. Non-Claim Boundaries

These sources are important because they explicitly block overreach.

- [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md)
  - boundary: reusable capability numbers require a `Tier 1 internal dated capability record`
  - boundary: forbids marketing-page leakage, stale undated shop numbers, and recipe tables disguised as generic capability
- [h2-capability-number-inventory.md](/code/blogs/llm_wiki/logs/h2-capability-number-inventory.md)
  - boundary: `board_thickness` is already recognized as a mixed capability-versus-recipe risk bucket
  - boundary: stackup examples and common commercial builds must not be promoted into reusable numerics
- [layer-count-blog-readiness.md](/code/blogs/llm_wiki/logs/layer-count-blog-readiness.md)
  - boundary: current corpus is weak for numeric process capability tables
  - boundary: high-layer drafts still overreach when they depend on unsupported process windows and factory-specific capability statements
- [advanced-pcb-fabrication-and-stackup-planning.md](/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md)
  - boundary: rigid, rigid-flex, thermal, and substrate decisions must stay separated
  - boundary: internal numeric capabilities are refresh-sensitive
- [prototype-vs-quick-turn-pcb-routing.md](/code/blogs/llm_wiki/wiki/processes/prototype-vs-quick-turn-pcb-routing.md)
  - boundary: quick-turn posture must not be mistaken for generalized capability proof
- [high-layer-rigid-board-manufacturability-context.md](/code/blogs/llm_wiki/facts/methods/high-layer-rigid-board-manufacturability-context.md)
  - boundary: public process guides do not authorize board-thickness limits or capability tables

### D. Candidate Upstream Inputs For A Future Dated Capability Record

These inputs may help identify owner, scope, and family boundaries for a future `Tier 1` record. They do not authorize finished-board thickness numbers by themselves.

- `frontendapt-pcb-multilayer-pcb-page-en`
  - candidate role: feeder for rigid-multilayer scope and internal owner mapping
- `frontendhil-multilayer-pcb-product-page-en`
  - candidate role: feeder for cross-site multilayer wording and stackup-family alignment
- `frontendapt-pcb-multi-layer-laminated-structure-page-en`
  - candidate role: feeder for stackup-construction vocabulary and lamination-family routing

These are only candidate upstream inputs because they are:

- internal
- semi-stable
- undated as capability records
- not normalized by site, line, or finished-board interpretation basis

The following sources are better treated as boundary inputs than numeric feeders:

- `frontendapt-pcb-rigid-flex-pcb-page-en`
- `frontendhil-rigid-flex-pcb-product-page-en`
- `frontendapt-pcb-metal-core-pcb-page-en`
- `frontendapt-pcb-fr4-pcb-page-en`
- `frontendapt-pcb-high-tg-pcb-page-en`

Their value is mainly to prevent rigid-board finished thickness from being collapsed into other thickness concepts.

## Sources That Explicitly Require Refresh Or Do Not Authorize Transferable Thickness Numbers

The following sources already contain explicit boundary language that blocks direct numeric reuse:

- [advanced-pcb-fabrication-and-stackup-planning.md](/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md)
  - explicitly treats internal numeric capabilities and related process claims as refresh-sensitive
- [prototype-vs-quick-turn-pcb-routing.md](/code/blogs/llm_wiki/wiki/processes/prototype-vs-quick-turn-pcb-routing.md)
  - explicitly treats lead-time and accelerated-lane scope as refresh-required internal commitments
- [high-layer-rigid-board-manufacturability-context.md](/code/blogs/llm_wiki/facts/methods/high-layer-rigid-board-manufacturability-context.md)
  - explicitly says it does not provide board-thickness limits or capability tables
- [frontendapt-pcb-multilayer-pcb-page-en.md](/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-multilayer-pcb-page-en.md)
  - extraction notes already warn that thickness figures are internal claims
- [frontendhil-multilayer-pcb-product-page-en.md](/code/blogs/llm_wiki/sources/registry/internal/frontendhil-multilayer-pcb-product-page-en.md)
  - extraction notes already say process-capability numbers are internal support only
- [frontendapt-pcb-rigid-flex-pcb-page-en.md](/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-rigid-flex-pcb-page-en.md)
  - extraction notes already warn that bend and layer-window claims are internal capability claims
- [frontendapt-pcb-metal-core-pcb-page-en.md](/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-metal-core-pcb-page-en.md)
  - extraction notes already warn that conductivity and test thresholds are internal capability claims
- [frontendapt-pcb-fr4-pcb-page-en.md](/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-fr4-pcb-page-en.md)
  - extraction notes already warn that impedance and class-level claims are refresh-sensitive
- [frontendapt-pcb-high-tg-pcb-page-en.md](/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-high-tg-pcb-page-en.md)
  - extraction notes already warn that temperature, layer-count, and tolerance-like claims are refresh-sensitive

## What Is Still Missing

The missing item is not more thickness vocabulary. The missing item is a governed numeric authority.

Still missing:

- a registered `Tier 1 internal dated capability record` for finished-board thickness capability
- explicit scope separating rigid multilayer, rigid-flex, and special thermal-platform thickness claims
- explicit separation between finished board thickness and material-thickness availability
- explicit distinction between stackup examples and maintained capability windows
- usable date, owner, and refresh posture for any future finished-board thickness record
- evidence that a cited number is a maintained capability record rather than a stackup example, marketing residue, or platform-specific product option

Without those items, all reusable board-thickness numbers remain `needs_source`.

## Recommended Future Ingestion Order

1. Start with rigid-multilayer internal inputs:
   - `frontendapt-pcb-multilayer-pcb-page-en`
   - `frontendhil-multilayer-pcb-product-page-en`
   - `frontendapt-pcb-multi-layer-laminated-structure-page-en`
2. Use `high-layer-rigid-board-manufacturability-context.md` as the main non-numeric cross-check for dimensional-control and lamination-planning posture.
3. Use rigid-flex and metal-core pages as boundary-control inputs so finished rigid-board thickness does not collapse into flex, bend, or IMS thickness claims.
4. Use FR-4 and high-Tg pages only as mainstream-family context, not as finished-board capability authority.
5. Use `prototype-vs-quick-turn-pcb-routing.md` to block accelerated-lane assumptions from becoming thickness defaults.
6. Only after steps `1-5`, decide whether a real dated capability record can be created.

If step `6` fails, the bucket remains:

- `needs_source` for reusable finished-board thickness numerics
- `downgrade` for non-numeric planning and manufacturability wording

## Current Ingestion Stop/Go Posture

- `keep`: material-thickness availability only when it stays in the correct material or product layer
- `downgrade`: stackup examples, planning posture, rigid-flex/mechanical posture, and complexity framing without numeric promotion
- `needs_source`: all reusable finished-board thickness numerics
- `delete`: warped or special-platform thickness claims rewritten as generic finished-board capability
