# H2 Stackup Recipe And Process Count Numbers Bucket Decision

Date: 2026-04-25

## Purpose

This document records the governance posture for `stackup_recipe_and_process_count_numbers` under `H2 Workstream 2: Fabrication Capability Numeric Layer`.

This area exists to stop one common failure mode:

- example stackups, lamination counts, drill-program counts, build-up cycle counts, and similar planning shorthand being rewritten as reusable factory rules

This file is:

- a governance and dependency document
- a containment decision
- a stop/go control for recipe leakage

This file is not:

- a normal capability-recovery bucket
- a numeric fact card
- permission to reuse lamination, drill-program, or stackup-count numbers
- a substitute for a `Tier 1 internal dated capability record`

## Current True Posture

`stackup_recipe_and_process_count_numbers` should be governed as recipe-leakage containment rather than normal capability recovery.

Most count-style claims here are design- and material-dependent process examples, not stable manufacturing authority.

Current internal and supplier sources support posture and boundary control only. They do not authorize reusable numeric recipe claims.

## Why This Area Is Not A Normal Capability Bucket

This cluster mixes several non-equivalent claim types:

- example stackups
- lamination counts
- drill-program or process-step counts
- build-up route illustrations
- material-form vocabulary
- supplier process-note context

Those items are usually:

- design dependent
- material dependent
- route dependent
- article-example dependent

That means one recovered number here would almost always overstate portability.

## What This Containment Area Commonly Contains

Typical mixed claim shapes:

- sequential lamination count
- build-up cycle count
- drill-program count
- press count
- hole-family-count target
- signal / plane-count recipes framed as defaults
- `1+N+1` or `2+N+2` route examples rewritten as universal capability

## Current Corpus Support And Boundaries

The current corpus is already strong enough to support architecture vocabulary, planning posture, and recipe-leakage boundaries.

It is not strong enough to support reusable count-style numerics.

### Internal Posture Support

The following internal pages are useful for stackup, lamination, and route framing:

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-multi-layer-laminated-structure-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-multilayer-pcb-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-multilayer-pcb-product-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`

These can support statements such as:

- multilayer, sequential lamination, and advanced routes belong to planning and process vocabulary
- exact count-style examples are not stable reusable factory defaults
- route and process examples remain refresh-sensitive and design dependent

### Supplier And Material-Form Boundary Support

The following sources help prevent material-form or process-guide language from being rewritten as recipe authority:

- `/code/blogs/llm_wiki/sources/registry/materials/isola-sequential-lamination-in-pcbs-note.md`
- `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro4835t-ro4450t-multilayer-processing-guide.md`
- `/code/blogs/llm_wiki/sources/registry/materials/ventec-vt464lt-process-guide.md`
- `/code/blogs/llm_wiki/sources/registry/materials/agc-bond-plies-prepregs-page.md`

These are useful because they show:

- sequential lamination and bonding-layer language often appears in process-note or material-form context
- material-form vocabulary is not equivalent to a reusable stackup recipe
- supplier process guidance is not transferable shop capability authority

## Containment Rule

Current rule for this area:

- keep architecture vocabulary, material-form vocabulary, and non-numeric process context where needed
- do not promote example stackups, lamination counts, drill-program counts, or build-up route counts into reusable factory defaults
- do not create one `stackup_recipe_and_process_count_numbers` capability fact card
- do not bridge this area into `P4-06` as if it were a normal recovered numeric layer

## Required Claim Split

Any future work here must first split incoming claims into these families.

### 1. `stackup examples`

Scope:

- signal / plane allocation
- layer-role splits
- reference constructions used as illustration

### 2. `lamination count`

Scope:

- lamination count
- sequential lamination count
- buildup cycle count

### 3. `press / process count`

Scope:

- drill-program count
- press count
- process-step count
- hole-family-count target

### 4. `build-up recipe illustrations`

Scope:

- `1+N+1` style route examples
- named route sequences
- architecture examples with implied default counts

### 5. `material-form vocabulary`

Scope:

- `bond ply`
- `RCC`
- `FRCC`
- `no-flow prepreg`
- `controlled-flow prepreg`

### 6. `supplier process-note context`

Scope:

- sequential-lamination context
- handling discipline
- bonding-layer workflow
- stress-factor wording

None of these should be assumed numerically recoverable unless a very narrow family later receives its own `Tier 1` dated capability source.

## Disposition Guidance For Current Mixed Claims

### example stackup with one overall route count

- disposition:
  - `downgrade` as planning context if the number is removed
  - `delete` if promoted as reusable factory rule

### sequential-lamination count from an internal advanced-process page

- disposition:
  - `downgrade` as architecture or planning posture
  - not valid as capability evidence

### process guide listing bonding layers or lamination sequence examples

- disposition:
  - `keep` only for material-form or process vocabulary
  - `delete` if rewritten as generic count authority

### `1+N+1` or route-count language used as default capability promise

- disposition: `delete`
- reason:
  - architecture example is not stable numeric manufacturing authority

## Exact Next-Step Requirements

Before any count-style numeric recovery could exist here, the repo still needs:

1. narrower child-family decisions with clean scope boundaries
2. explicit separation between example stackups and maintained factory rules
3. explicit separation between material-form vocabulary and route-count authority
4. a `Tier 1 internal dated capability record` for any very narrow count claim that attempts numeric recovery
5. proof that a cited count is maintained production authority rather than one article recipe or supplier example

Until those conditions are met, `stackup_recipe_and_process_count_numbers` remains a containment bucket, not a normal capability-recovery bucket.
