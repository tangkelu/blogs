# H2 Etch Compensation Bucket Decision

Date: 2026-04-25

## Purpose

This document records the bucket-level governance decision for `etch_compensation` under `H2 Workstream 2: Fabrication Capability Numeric Layer`.

It converts the next narrow child split from the held `copper_plating_process_windows` area into a controlled decision sheet before any etch-compensation numeric recovery starts.

This file is:

- a governance and dependency document
- a bucket-level handling decision
- a stop/go control for future recovery work

This file is not:

- a numeric fact card
- permission to reuse etch-compensation numbers
- a customer-facing claim source
- a substitute for a `Tier 1 internal dated capability record`

## Why `etch_compensation` Is A Distinct H2 Child Bucket

`etch_compensation` is a necessary child split because conductor-width compensation or conductor-reduction allowance is not the same thing as:

- finished copper-weight capability
- plating thickness or build allowance
- resin-fill, planarization, or heavy-copper workflow notes
- standards minima or acceptance thresholds
- stackup recipes, impedance geometry tables, or generic trace/space capability

This bucket exists to stop several common collapse errors:

- trace/space capability claims being backfilled from process-adjustment numbers
- plating or copper-weight language being confused with conductor-formation adjustment
- one stackup or process example being rewritten as reusable etch-compensation authority
- impedance or DFM geometry examples being reused as shop etch practice

Current H2 demand already shows repeated dependence on compensation-style claims:

- `8-layer`: stackup tables and geometry assumptions that can over-read compensation values as generic feature-size authority
- `12-layer`: process-control and conductor-width sections that can smuggle in adjustment numbers
- `14-layer`: dense DFM rule bundles where compensation language can become unsupported capability
- `16-layer`: heavy-copper and process-window sections where conductor-formation wording can be overstated
- `20-layer`: high-risk mixed process examples where compensation values can be mistaken for maintained factory defaults

Because these claim families are even less stable than ordinary capability-result buckets, `etch_compensation` requires its own governance layer before any recovery attempt.

## What This Bucket Includes

This bucket includes numeric claims that assert, imply, or strongly suggest what conductor-width compensation or etch-driven adjustment a fabricator can currently apply as an operational capability or maintained process control.

In scope:

- etch-compensation values presented as current production authority
- conductor-reduction allowance presented as a maintained shop default
- pattern-adjustment numbers framed as routine process capability
- compensation values rewritten as maintained etch-control authority rather than one-off examples

Typical claim shapes:

- etch compensation value
- conductor reduction allowance
- trace-width compensation tied to conductor formation
- pattern adjustment presented as routine etch-control capability

## What This Bucket Excludes

This bucket does not govern:

- finished copper-weight capability
- plating thickness or build allowance
- trace/space capability ladders
- impedance geometry tables
- resin-fill, balance, planarization, or heavy-copper workflow notes
- standards minima, acceptance thresholds, or finish-stack specifications
- stackup recipes and one-project process examples
- supplier process notes used only for context

Excluded examples:

- `3/3 mil` or `2.5/2.5 mil` style feature-size capability ladders
- one impedance table with width/spacing examples
- one stackup recipe using one compensation assumption
- one heavy-copper process note with planarization or balance language
- one process guide listing handling or process sensitivity only
- standards or finish-related thresholds reused as etch authority

Those belong to other governance layers even when they appear next to conductor-width or process-adjustment wording.

## Current Corpus Support And Non-Claim Boundaries

The current corpus is already strong enough to support heavy-copper posture, special-process routing, and non-claim boundaries around etch-compensation language.

It is not strong enough to support reusable etch-compensation numbers.

### Internal Process And Heavy-Copper Support

The following internal registry records are useful for guarded framing:

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-heavy-copper-pcb-product-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-pcb-fabrication-process-page-en.md`

These support posture such as:

- heavy-copper and advanced fabrication belong to a special-process family
- conductor-formation and process-adjustment language deserves separate routing from ordinary geometry claims
- exact process-adjustment values remain internal, refresh-sensitive claims

### Special-Process Boundary Support

[pcb-stackup-special-process-and-baseline-families.md](/code/blogs/llm_wiki/facts/methods/pcb-stackup-special-process-and-baseline-families.md) already supports these guarded statements:

- heavy-copper and stackup-driven special routes should stay separate from baseline manufacturing labels
- exact numeric capability claims remain refresh-sensitive and must not be promoted from process posture

### Copper/Plating Cluster Boundary Support

[h2-copper-plating-process-windows-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-copper-plating-process-windows-bucket-decision.md), [h2-copper-weight-capability-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-copper-weight-capability-bucket-decision.md), and [h2-plating-thickness-build-allowance-bucket-decision.md](/code/blogs/llm_wiki/logs/h2-plating-thickness-build-allowance-bucket-decision.md) already support these guarded statements:

- copper weight, plated buildup, and etch adjustment must remain separate claim families
- mixed process windows should not be flattened into one reusable authority
- process-adjustment values are not automatically capability-result proof

## Current Blocker Statement

Current blocker for this bucket:

- there is no registered `Tier 1 internal dated capability record` yet for etch-compensation values with explicit process-family scope, copper-weight context, line/site scope, measurement basis, and refresh discipline

Under [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md), that means:

- reusable etch-compensation numbers remain `needs_source`
- internal heavy-copper, advanced-process, and fabrication-process pages remain `downgrade` / posture-only support
- no etch-compensation capability fact card can exist yet
- no blog or evidence pack may reuse etch-compensation numbers as governed capability numerics

Current corpus posture is therefore:

- special-process and heavy-copper route framing: supported
- cross-bucket boundary control: supported
- reusable etch-compensation numbers: blocked

## Claim-Splitting Rule For This Bucket

Every etch-compensation-related claim must be split into one of the following buckets before disposition.

### 1. Etch Compensation Capability

This is the actual H2 bucket target.

Examples:

- etch-compensation value presented as current production authority
- conductor-reduction allowance presented as a maintained shop default
- pattern-adjustment value framed as routine process capability

Handling:

- H2 bucket item
- currently `needs_source`
- cannot be reused until a dated internal capability record exists

### 2. Finished Copper-Weight Capability

This is not etch-compensation capability.

Examples:

- copper-weight ladder
- ounce-based production window
- heavy-copper range presented as board capability

Handling:

- route to `copper_weight_capability`
- do not mix into etch-compensation capability

### 3. Plating Thickness / Build Allowance

This is not etch-compensation capability.

Examples:

- plating thickness capability
- conductor-build allowance
- hole-copper growth value

Handling:

- route to `plating_thickness_build_allowance`
- do not mix into etch-compensation capability

### 4. Trace / Space Or Impedance Geometry Table

This is not etch-compensation capability.

Examples:

- line/space capability ladder
- width/spacing impedance table
- geometry examples used for SI targets

Handling:

- route to `trace_space` or keep as non-capability geometry context
- `delete` if reused as etch-capability proof

### 5. Standards Minimum Or Finish/Threshold Language

This is not shop capability.

Examples:

- IPC minimum or threshold wording
- finish-related thickness or threshold wording
- class-linked criteria

Handling:

- `delete`
- do not allow standards or finish thresholds to piggyback into H2 capability facts

### 6. Stackup Recipe Or Named Process Example

This is not automatically capability proof.

Examples:

- one stackup recipe with one compensation assumption
- one supplier process guide with one process example
- one article example using one adjustment value

Handling:

- `downgrade` when kept as non-numeric context
- `delete` if promoted as a transferable manufacturing rule

## Disposition Guidance For Common Claim Shapes

### exact etch-compensation or conductor-reduction value on an internal page only

- disposition: `needs_source`
- reason:
  - internal support page without a `Tier 1` dated capability record

### impedance or geometry table reused as etch-compensation proof

- disposition: `delete`
- reason:
  - geometry example is not etch-compensation capability evidence

### heavy-copper process page using adjustment language next to copper-weight or plating values

- disposition:
  - split claim first
  - etch portion: `needs_source`
  - copper-weight or plating portion: route to its own child bucket

### supplier process-guide example used as universal etch rule

- disposition: `delete`
- reason:
  - named process guide is context only, not shop capability evidence

### stackup recipe with one compensation assumption

- disposition:
  - `downgrade` as planning context if the number is removed
  - `delete` if promoted as transferable capability

## Exact Next-Step Requirements Before Any Fact Card Could Exist

Before any `etch_compensation` fact card could exist, the repo still needs:

1. a registered `Tier 1 internal dated capability record` for etch-compensation capability
2. explicit separation between etch-compensation and finished copper-weight capability
3. explicit separation between etch-compensation and plated buildup/build allowance
4. explicit separation between etch-compensation and trace/space or impedance geometry examples
5. usable date, owner, process-family scope, measurement basis, and refresh posture for any future etch record

Until those conditions are met, `etch_compensation` remains a governed but blocked H2 numeric bucket.
