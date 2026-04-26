# H2 Recipe Process Window Leakage Bucket Decision

Date: 2026-04-25

## Purpose

This document records the governance posture for `recipe_process_window_leakage` under `H2 Workstream 2: Fabrication Capability Numeric Layer`.

This area exists to stop one common failure mode:

- stackup examples, lamination recipes, timing windows, pressure windows, bake conditions, and similar manufacturing examples being rewritten as reusable factory capability numerics

This file is:

- a governance and dependency document
- a containment decision
- a stop/go control for recipe and process-window leakage

This file is not:

- a normal capability-recovery bucket
- a numeric fact card
- permission to reuse process-window, timing, pressure, or recipe numbers
- a substitute for a `Tier 1 internal dated capability record`

## Current True Posture

`recipe_process_window_leakage` should be governed as recipe-leakage containment rather than normal capability recovery.

Most claims here are route-dependent process examples, stackup-specific construction notes, or supplier/application context, not stable manufacturing authority.

Current internal and supplier sources support posture and boundary control only. They do not authorize reusable numeric process-window claims.

## Why This Area Is Not A Normal Capability Bucket

This cluster mixes several non-equivalent claim types:

- stackup copper-allocation examples
- lamination or press recipes
- bake, cure, dwell, or timing windows
- pressure or temperature process windows
- process-sequence examples
- heavy-copper or special-process recipe notes
- supplier process-note context

Those items are usually:

- route dependent
- stackup dependent
- copper-weight dependent
- material dependent
- example dependent

That means one recovered number here would almost always overstate portability and turn a recipe example into fake factory authority.

## What This Containment Area Commonly Contains

Typical mixed claim shapes:

- one lamination or press recipe presented as a default manufacturing window
- one bake or cure schedule presented as a generic factory rule
- one pressure or dwell range copied out of process prose
- one heavy-copper build sequence rewritten as normal rigid-board capability
- one supplier process note treated as shop authority
- one stackup example with copper and process settings promoted as reusable capability

## What This Area Excludes

This containment area does not govern:

- finished `copper_weight_capability`
- `plating_thickness_build_allowance`
- `etch_compensation`
- `standards_minima`
- general stackup-count leakage already governed under `stackup_recipe_and_process_count_numbers`
- material datasheet numerics used only for material identity

Those belong to other governance layers even when they appear next to recipe or process-window wording.

## Current Corpus Support And Boundaries

The current corpus is already strong enough to support process-family vocabulary, stackup-planning posture, and non-claim boundaries around recipe leakage.

It is not strong enough to support reusable recipe or process-window numerics.

### Internal Posture Support

The following internal pages are useful for special-process framing, fabrication workflow context, and guarded route vocabulary:

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-heavy-copper-pcb-product-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-pcb-fabrication-process-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`

These can support statements such as:

- heavy copper and advanced fabrication belong to distinct process families
- process notes and route examples must remain planning or workflow context
- exact process windows remain refresh-sensitive internal claims

### Wiki And Method Boundary Support

The following existing cards are useful for controlled posture:

- [advanced-pcb-fabrication-and-stackup-planning.md](/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md)
- [pcb-stackup-special-process-and-baseline-families.md](/code/blogs/llm_wiki/facts/methods/pcb-stackup-special-process-and-baseline-families.md)
- [h2-copper-plating-process-windows-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-copper-plating-process-windows-bucket-decision.md)
- [h2-stackup-recipe-and-process-count-numbers-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-stackup-recipe-and-process-count-numbers-bucket-decision.md)

These support guarded statements such as:

- process-family selection, stackup planning, and route examples should stay separate from maintained capability claims
- count-style recipe leakage and process-window leakage are related but not identical control problems
- exact copper/plating/process numerics remain blocked unless a narrower family later receives stronger authority

### Supplier / Application Boundary Support

The following sources are useful because they show where recipe leakage often enters drafts:

- `/code/blogs/llm_wiki/sources/registry/materials/arlon-heavy-copper-layers-application-page.md`
- `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro4835t-ro4450t-multilayer-processing-guide.md`
- `/code/blogs/llm_wiki/sources/registry/materials/ventec-vt464lt-process-guide.md`

These support guarded statements such as:

- supplier process guides and application pages are context and discovery inputs
- named process examples do not authorize reusable shop windows

## Containment Rule

Current rule for this area:

- keep process-family vocabulary and non-numeric workflow framing where needed
- do not promote process recipes, bake/cure windows, pressure windows, dwell windows, or route examples into reusable factory defaults
- do not create one `recipe_process_window_leakage` capability fact card
- do not bridge this area into `P4-06` as if it were a normal recovered numeric layer

## Required Claim Split

Any future work here must first split incoming claims into these families.

### 1. `process recipe example`

Scope:

- lamination recipe
- press recipe
- heavy-copper route sequence
- build-specific process recipe

### 2. `process-window or timing example`

Scope:

- bake, cure, or dwell windows
- pressure, time, or temperature windows
- workflow timing conditions tied to one route

### 3. `supplier or application-note process context`

Scope:

- named process-guide examples
- supplier workflow notes
- application-note construction examples

### 4. `adjacent true capability family`

Scope:

- finished copper-weight capability
- plating buildup or allowance
- etch compensation
- standards minima

None of these should be assumed numerically recoverable unless a narrower true capability family later receives its own `Tier 1` dated capability source.

## Disposition Guidance For Current Mixed Claims

### one internal process page showing a bake or pressure window

- disposition:
  - `downgrade` as workflow context
  - not valid as reusable capability evidence

### one heavy-copper or special-process route sequence rewritten as default capability

- disposition: `delete`
- reason:
  - route example is not stable factory authority

### supplier processing guide reused as generic shop process-window proof

- disposition: `delete`
- reason:
  - supplier context is not maintained production authority

### mixed recipe wording sitting next to copper-weight or plating claims

- disposition:
  - split and route true capability claims to their own child buckets
  - keep recipe residue under containment only

## Exact Next-Step Requirements

Before any process-window numeric recovery could exist here, the repo still needs:

1. explicit separation between recipe examples and maintained production rules
2. explicit separation between supplier process-note context and current shop authority
3. explicit separation between process-window leakage and adjacent true capability families
4. a `Tier 1 internal dated capability record` for any very narrow future family that attempts numeric recovery
5. proof that a cited number is maintained production authority rather than stackup or route example residue

Until those conditions are met, `recipe_process_window_leakage` remains a containment area, not a normal capability-recovery bucket.
