# H2 Resin Fill Balance Heavy Copper Process Claims Bucket Decision

Date: 2026-04-25

## Purpose

This document records the governance posture for `resin_fill_balance_heavy_copper_process_claims` under `H2 Workstream 2: Fabrication Capability Numeric Layer`.

This area exists to stop one common failure mode:

- special-process heavy-copper notes about resin fill, balance, planarization, copper coin, or workflow sequencing being rewritten as reusable factory capability numerics

This file is:

- a governance and dependency document
- a containment decision
- a stop/go control for process-note leakage

This file is not:

- a normal capability-recovery bucket
- a numeric fact card
- permission to reuse resin-fill, balance, or planarization numbers
- a substitute for a `Tier 1 internal dated capability record`

## Current True Posture

`resin_fill_balance_heavy_copper_process_claims` should be governed as process-leakage containment rather than normal capability recovery.

Most claims here are stackup-, copper-weight-, route-, and product-dependent process notes, not stable manufacturing authority.

Current internal and supplier sources support posture and boundary control only. They do not authorize reusable numeric process claims in this area.

## Why This Area Is Not A Normal Capability Bucket

This cluster mixes several non-equivalent claim types:

- resin-fill process notes
- balance or planarization workflow claims
- copper-coin and special thermal-path process notes
- heavy-copper route sequencing
- application-note context
- one-project or one-family process examples

Those items are usually:

- route dependent
- copper-weight dependent
- stackup dependent
- material dependent

That means one recovered number here would almost always overstate portability.

## What This Containment Area Commonly Contains

Typical mixed claim shapes:

- resin-fill or fill-balance wording
- planarization or copper-balance workflow notes
- copper coin process examples
- heavy-copper route sequencing
- build balancing or special thermal-path statements
- named process examples tied to one construction family

## Current Corpus Support And Boundaries

The current corpus is already strong enough to support special-process vocabulary, heavy-copper posture, and process-leakage boundaries.

It is not strong enough to support reusable numeric process claims.

### Internal Posture Support

The following internal pages are useful for heavy-copper and advanced-process framing:

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-heavy-copper-pcb-product-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`

These can support statements such as:

- heavy copper belongs to a special-process manufacturing family
- copper coin, balance, and related workflow notes belong to project-specific process framing
- exact numeric process notes remain internal, refresh-sensitive claims

### Special-Process Boundary Support

[pcb-stackup-special-process-and-baseline-families.md](/code/blogs/llm_wiki/facts/methods/pcb-stackup-special-process-and-baseline-families.md) and [thermal-pcb-platform-selection-posture.md](/code/blogs/llm_wiki/facts/methods/thermal-pcb-platform-selection-posture.md) already support these guarded statements:

- heavy copper is a distinct power and thermal route
- thermal platform selection and special-process routing should stay separate from generalized capability claims
- exact capability-style numbers remain refresh-sensitive internal claims

### Supplier / Application Boundary Support

`/code/blogs/llm_wiki/sources/registry/materials/arlon-heavy-copper-layers-application-page.md` already supports these guarded statements:

- official heavy-copper application context is useful for discovery and framing
- application pages do not authorize reusable processing values without current datasheets

## Containment Rule

Current rule for this area:

- keep heavy-copper process vocabulary and non-numeric route framing where needed
- do not promote resin-fill, balance, planarization, copper coin, or route-sequence notes into reusable factory defaults
- do not create one `resin_fill_balance_heavy_copper_process_claims` capability fact card
- do not bridge this area into `P4-06` as if it were a normal recovered numeric layer

## Required Claim Split

Any future work here must first split incoming claims into these families.

### 1. `resin-fill or fill-balance notes`

Scope:

- fill-related or balance-related process notes tied to special heavy-copper or stackup routes

### 2. `planarization or copper-balance workflow`

Scope:

- planarization steps
- copper-balance process notes
- route-specific flattening or balancing workflow

### 3. `copper coin or special thermal-path process notes`

Scope:

- copper coin workflow
- special thermal-path process notes
- route-specific embedded thermal feature process claims

### 4. `heavy-copper route sequence examples`

Scope:

- named process examples
- route sequencing tied to one board family
- one-project or one-family workflow examples

None of these should be assumed numerically recoverable unless a very narrow family later receives its own `Tier 1` dated capability source.

## Disposition Guidance For Current Mixed Claims

### heavy-copper page with balance or planarization wording

- disposition:
  - `downgrade` as special-process posture
  - not valid as reusable capability evidence

### advanced-process page mentioning copper coin or related route notes

- disposition:
  - `downgrade` as route framing
  - `delete` if promoted as transferable numeric authority

### supplier application page used as process-capability proof

- disposition: `delete`
- reason:
  - application context is not shop capability evidence

### one stackup or route example rewritten as general special-process rule

- disposition:
  - `downgrade` as context if the number is removed
  - `delete` if promoted as reusable factory default

## Exact Next-Step Requirements

Before any process-claim numeric recovery could exist here, the repo still needs:

1. narrower child-family decisions with clean scope boundaries
2. explicit separation between special-process notes and maintained production rules
3. explicit separation between application-note context and current shop authority
4. a `Tier 1 internal dated capability record` for any very narrow process claim that attempts numeric recovery
5. proof that a cited number is maintained production authority rather than one route example or one product-family note

Until those conditions are met, `resin_fill_balance_heavy_copper_process_claims` remains a containment area, not a normal capability-recovery bucket.
