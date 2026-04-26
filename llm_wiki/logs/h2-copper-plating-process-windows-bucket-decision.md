# H2 Copper Plating Process Windows Bucket Decision

Date: 2026-04-25

## Purpose

This document records the current governance posture for `copper_plating_process_windows` under `H2 Workstream 2: Fabrication Capability Numeric Layer`.

This file exists to stop one unsafe shortcut:

- treating copper weight, plating thickness, etch compensation, resin-balance notes, heavy-copper process claims, and standards minima as one reusable numeric bucket

This file is:

- a governance and dependency document
- a hold-state decision
- a split-before-recovery control

This file is not:

- a normal unlocked H2 bucket
- a numeric fact card
- permission to reuse plating or copper-weight numbers
- a substitute for a `Tier 1 internal dated capability record`

## Current True Posture

`copper_plating_process_windows` remains `hold-until-split`.

Current corpus support is sufficient for posture and boundary control only, not for reusable numeric recovery.

Before any fact-card work, claims in this area must be separated into narrower families:

- `copper weight capability`
- `plating thickness / build allowance`
- `etch compensation`
- `resin-fill / balance / heavy-copper process claims`
- `standards minima`
- `recipe / process-window leakage`

Until that split exists, this area should not be treated as one ordinary H2 capability bucket.

## Why This Area Cannot Be Recovered As One Bucket

This cluster is unusually unstable because it mixes claim types with different owners, different measurement bases, and different validity windows:

- copper weight options are not the same as plating thickness capability
- plating build allowance is not the same as etch compensation
- heavy-copper process notes are not the same as maintained capability tables
- standards minima are not the same as shop capability
- recipe examples are not the same as reusable production authority

That means one combined `copper_plating_process_windows` bucket would create false transferability almost immediately.

## What This Held Area Commonly Contains

Typical mixed claim shapes:

- `1 oz / 2 oz / 3 oz / 6 oz` style capability ladders
- plating thickness or build allowance wording
- compensation values attached to etch or conductor reduction
- heavy-copper resin-balance or planarization wording
- plating minima implied through standards or finish language
- process examples tied to one stackup, one copper family, or one product route

## Current Corpus Support And Boundaries

The current corpus is already strong enough to support workflow separation and boundary control around this area.

It is not strong enough to support a unified reusable numeric layer.

### Internal Posture Support

The following internal pages are useful for process-family routing and guarded framing:

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-heavy-copper-pcb-product-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-pcb-fabrication-process-page-en.md`

These can support statements such as:

- heavy-copper and advanced fabrication belong to a special-process family
- plating and process-balance concerns deserve separate routing from ordinary multilayer claims
- exact numeric process windows remain refresh-sensitive internal claims

### Boundary-Control Support

The following sources help prevent category collapse:

- [selective-multi-finish-strategy.md](/code/blogs/llm_wiki/facts/methods/selective-multi-finish-strategy.md)
- [ipc-finish-standards-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-finish-standards-metadata.md)
- [mcpcb-ims-and-reflow-source-coverage.md](/code/blogs/llm_wiki/facts/methods/mcpcb-ims-and-reflow-source-coverage.md)
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-metal-core-pcb-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-metal-core-pcb-product-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/materials/arlon-heavy-copper-layers-application-page.md`
- `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro4835t-ro4450t-multilayer-processing-guide.md`

These are useful because they show:

- finish and plating terminology carries standards and chemistry boundary risk
- metal-core, heavy-copper, and special thermal routes must not be flattened into generic rigid-board capability
- supplier process notes are context, not transferable capability proof

## Hold-State Rule

Current rule for this area:

- do not create one `copper_plating_process_windows` fact card
- do not route mixed copper/plating/process claims into reusable H2 numerics
- do not let standards minima or recipe examples piggyback into capability language
- do not promote internal process prose into transferable tables

Current allowed use:

- posture support
- boundary control
- future split planning

Current blocked use:

- reusable numeric recovery
- evidence-pack capability tables
- customer-facing capability claims based on mixed current prose

## Required Split Before Any Recovery Attempt

Any future work here must first split claims into these narrower sub-buckets.

### 1. `copper weight capability`

Scope:

- finished copper-weight capability windows when framed as maintained production authority

### 2. `plating thickness / build allowance`

Scope:

- plating-thickness capability
- hole-copper or conductor-build capability
- maintained build-allowance windows

### 3. `etch compensation`

Scope:

- compensation values or process allowances tied to conductor formation

### 4. `resin-fill / balance / heavy-copper process claims`

Scope:

- special-process balancing, planarization, resin-fill, or heavy-copper workflow claims

### 5. `standards minima`

Scope:

- standards-derived minima, finish-related thresholds, or workmanship-style lower bounds

### 6. `recipe / process-window leakage`

Scope:

- one stackup, one application note, or one manufacturing example treated as factory default

None of these should be assumed recoverable until each narrower family has its own source posture review.

## Disposition Guidance For Current Mixed Claims

### mixed copper-weight and plating ladder on an internal page

- disposition:
  - `downgrade` for family framing
  - `needs_source` for any reusable numeric capability claim

### heavy-copper application note with example build allowances

- disposition:
  - `downgrade` as process context
  - `delete` if promoted as universal factory rule

### IPC or finish-standard minimum being reused as plating capability

- disposition: `delete`
- reason:
  - standards minimum is not shop capability proof

### process note with compensation or balance figures

- disposition:
  - `downgrade` as context only
  - do not recover numerically without a narrower split plus `Tier 1` evidence

## Exact Next-Step Requirements

Before any reusable numeric recovery could exist here, the repo still needs:

1. narrower sub-bucket definitions with clean scope boundaries
2. a separate source-map decision for each narrower family that survives the split
3. a `Tier 1 internal dated capability record` for any narrower family that attempts numeric recovery
4. explicit separation between standards minima, recipe examples, and maintained capability
5. explicit separation between heavy-copper special-process context and ordinary rigid-board capability

Until those conditions are met, `copper_plating_process_windows` remains `hold-until-split`.
