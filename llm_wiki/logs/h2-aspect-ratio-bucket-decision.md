# H2 Aspect Ratio Bucket Decision

Date: 2026-04-25

## Purpose

This document defines the current governance posture for the `aspect_ratio` bucket inside `H2 Fabrication Capability Numeric Layer`.

It is a bucket-decision file, not a fact card and not a reusable capability table.

## Why `aspect_ratio` Sits In This Geometry Wave

`aspect_ratio` belongs in the same intake wave as `trace_space` and `drill_and_via_geometry` because all three are geometry-shaped capability claims that are repeatedly mixed together in layer-count blog prose and internal process pages.

This wave exists to stop one common failure mode:

- geometry wording from drilling, HDI, or stackup pages gets flattened into reusable shop-capability numbers without date, scope, or claim-splitting discipline

`aspect_ratio` is especially sensitive because it is often written as if one number could cover:

- plated through-hole capability
- blind or buried via guidance
- microvia reliability language
- standards-style design-rule tables

Those are not the same claim.

## In-Scope Claims

In scope for this bucket:

- current internal shop-capability claims about plated through-hole aspect-ratio limits
- capability-style wording where via-depth-to-diameter is presented as a manufacturable current limit for a rigid multilayer process family
- dated internal capability records, if they later exist, for mechanical-through-hole aspect-ratio capability with explicit scope

## Excluded Claims

Excluded from this bucket:

- microvia geometry defaults
- stacked or staggered microvia reliability language
- any-layer / build-up architecture examples
- IPC or military standards thresholds
- design-rule tables presented as universal doctrine
- stackup examples and blog recipe numbers
- rigid-flex transition, bend, or flex-life ratios
- SI, channel, or impedance-outcome numerics attached to via geometry

## Current Corpus Support And Non-Claim Boundaries

Current corpus support is useful but narrow.

What the corpus can support now:

- internal posture that high-layer and HDI builds are registration-sensitive, drilling-sensitive, and process-coupled
- internal posture that drilling, laser-via, VIPPO, any-layer, and backdrill claims must be treated as refresh-sensitive
- guarded wording that advanced boards require tighter process planning around drilling and interconnect structure

What the corpus does not support now:

- any reusable plated-through-hole aspect-ratio number
- any reusable microvia aspect-ratio number
- any universal rule connecting one aspect-ratio figure to all rigid, HDI, and high-layer contexts

Relevant current support files:

- `facts/methods/high-layer-count-backdrill-and-registration-posture.md`
- `facts/methods/hdi-microvia-and-vippo-process-posture.md`
- `facts/methods/high-layer-rigid-board-manufacturability-context.md`
- `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`

Relevant current internal registry posture:

- `frontendapt-pcb-drilling-page-en`
- `frontendapt-pcb-high-layer-count-pcb-page-en`
- `frontendapt-pcb-hdi-pcb-page-en`
- `frontendapt-pcb-multilayer-pcb-page-en`

These are posture and framing inputs only. They are not current authorization for reusable aspect-ratio numerics.

## Blocker Statement

Current posture: `needs_source`.

Blocker:

- there is no current `Tier 1` dated internal capability record in the corpus that cleanly states plated-through-hole aspect-ratio capability with explicit process-family scope, site or line scope, method context, and refresh discipline

Because that blocker remains open, `aspect_ratio` is not eligible for capability fact-card promotion.

## Claim-Splitting Rule

Before any future recovery attempt, split `aspect_ratio` claims into separate families:

### 1. Plated-Through-Hole Aspect-Ratio Capability

Allowed future target for `H2`, but only if supported by a dated internal capability record.

### 2. Microvia / Blind-Via / Build-Up Geometry

Not the same bucket outcome.

Handle under `drill_and_via_geometry` or later HDI-specific governance, not as plated-through-hole aspect-ratio recovery.

### 3. Reliability Or Qualification Tables

Not `H2`.

These belong to later reliability or standards governance and must not be recovered through `aspect_ratio`.

### 4. Standards Or Design-Guide Tables

Not authorizing for `H2` numeric reuse.

These may help explain vocabulary boundaries, but they must not be converted into current shop capability.

## Disposition Guidance For Common Claim Shapes

- `finished-hole aspect ratio is X:Y`
  - disposition: `needs_source`
  - note: recover only if tied to a dated internal capability record for plated-through-hole scope
- `microvia or blind-via aspect ratio is X:Y`
  - disposition: `needs_source`
  - note: do not collapse into plated-through-hole capability; route through `drill_and_via_geometry` or later HDI governance
- `IPC or class-linked aspect-ratio table`
  - disposition: `delete`
  - note: this is standards-style table content, not current capability proof
- `any-layer / 1+N+1 / stacked-via architecture examples with implicit ratios`
  - disposition: `downgrade`
  - note: keep only architecture vocabulary, not numeric defaults
- `process wording that dense boards require tighter drilling discipline`
  - disposition: `downgrade`
  - note: safe as non-numeric manufacturability framing
- `one drilling-page ratio presented as universal company capability`
  - disposition: `delete`
  - note: this is exactly the overclaim H2 is meant to block

## Per-Blog Impact Summary

- `6-layer`
  - via-rule and tolerance clusters remain `needs_source`; aspect-ratio language can only stay as softened manufacturability wording
- `8-layer`
  - HDI / via / pitch clusters remain `needs_source`; do not bridge blind-via or aspect-ratio figures into reusable capability language
- `10-layer`
  - HDI process geometry remains blocked; architecture vocabulary may stay, but no aspect-ratio number is unlocked
- `12-layer`
  - DFM-rule geometry claims remain `needs_source`; no aspect-ratio recovery from DDR or high-speed examples
- `14-layer`
  - via geometry and aspect-ratio cluster remains blocked; standards-heavy and rigid-flex-adjacent numbers must stay split
- `16-layer`
  - any aspect-ratio or hole-depth rule remains blocked pending a dated capability record
- `20-layer`
  - high risk remains; build-up, microvia, and reliability-adjacent ratio language must not be flattened into rigid-board capability

## Exact Next-Step Requirements Before Any Fact Card Could Exist

All of the following must exist first:

1. a current `Tier 1` dated internal capability record specifically for plated-through-hole aspect-ratio capability
2. explicit scope naming:
   - process family
   - site or line scope if relevant
   - whether the claim is rigid multilayer only
3. explicit method or interpretation context:
   - finished-hole basis, plating context, or other measurement basis
4. explicit separation from:
   - microvia guidance
   - standards thresholds
   - reliability tables
   - stackup recipe examples
5. a source-map pass confirming which current internal and external pages are framing-only versus candidate upstream inputs
6. control-doc wording that says the bucket is in intake or recovery review, not numerically unlocked

Until those conditions are met:

- reusable aspect-ratio numerics remain blocked
- `aspect_ratio` stays at `needs_source`
- only downgraded non-numeric manufacturability wording is safe downstream
