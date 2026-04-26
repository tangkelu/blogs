# H2 Plating Thickness Build Allowance Bucket Decision

Date: 2026-04-25

## Purpose

This document records the bucket-level governance decision for `plating_thickness_build_allowance` under `H2 Workstream 2: Fabrication Capability Numeric Layer`.

It converts the next narrow child split from the held `copper_plating_process_windows` area into a controlled decision sheet before any plating-thickness or build-allowance numeric recovery starts.

This file is:

- a governance and dependency document
- a bucket-level handling decision
- a stop/go control for future recovery work

This file is not:

- a numeric fact card
- permission to reuse plating-thickness or build-allowance numbers
- a customer-facing claim source
- a substitute for a `Tier 1 internal dated capability record`

## Why `plating_thickness_build_allowance` Is A Distinct H2 Child Bucket

`plating_thickness_build_allowance` is a necessary child split because plating buildup or finished build allowance is not the same thing as:

- finished copper-weight capability
- etch compensation
- resin-fill or planarization workflow
- surface-finish thickness or finish-stack specification
- standards minima or acceptance thresholds

This bucket exists to stop several common collapse errors:

- finish-page or finish-standard wording being rewritten as plated-copper capability
- heavy-copper process posture being rewritten as a reusable build-allowance ladder
- metal-core or thermal-platform wording being reused as plating authority
- one process-guide example being rewritten as universal plating buildup capability

Current H2 demand already shows repeated dependence on plating-thickness-style claims:

- `6-layer`: plating and process-window wording mixed with copper-weight assumptions
- `8-layer`: stackup and via-process sections that can over-read conductor-build language
- `12-layer`: process-control clusters mixed with fabrication capability phrasing
- `14-layer`: high-density and reliability-adjacent sections that can smuggle plating allowances into DFM rules
- `16-layer`: heavy-copper and power-route wording that can overstate buildup capability
- `20-layer`: complex build examples where plating-growth language can be misread as maintained shop authority

Because these claim families are easy to flatten into one unsupported default, `plating_thickness_build_allowance` requires its own governance layer before any recovery attempt.

## What This Bucket Includes

This bucket includes numeric claims that assert, imply, or strongly suggest what plating buildup or finished plated allowance a fabricator can currently produce as an operational capability.

In scope:

- plating-thickness capability presented as current production authority
- conductor-build or hole-build allowance presented as a maintained shop default
- plating-growth numbers framed as routine fabrication capability
- build-allowance windows rewritten as maintained process control rather than one-off examples

Typical claim shapes:

- plating thickness capability window
- build allowance added by plating
- hole-copper or conductor-build capability
- plating-growth value presented as routine process authority

## What This Bucket Excludes

This bucket does not govern:

- finished copper-weight capability
- etch compensation or conductor-reduction allowance
- resin-fill, balance, planarization, or heavy-copper workflow notes
- surface-finish thickness or finish-stack specification
- standards minima, class-based thresholds, or acceptance criteria
- current-carrying, thermal, or reliability outcome claims
- stackup recipes and one-project process examples
- supplier process-guide examples used only as context

Excluded examples:

- ENIG or ENEPIG finish thickness wording
- IPC finish-standard references used as plating capability proof
- one heavy-copper note with planarization or resin-balance language
- one stackup recipe that implies plating growth by layer
- one supplier process guide with example buildup sequence
- one reliability or thermal claim inferred from plated thickness

Those belong to other governance layers even when they appear next to plating wording.

## Current Corpus Support And Non-Claim Boundaries

The current corpus is already strong enough to support finish/plating workflow boundaries, heavy-copper posture, and non-claim boundaries around plating-thickness/build-allowance capability.

It is not strong enough to support reusable plating-thickness or build-allowance numbers.

### Internal Process And Heavy-Copper Support

The following internal registry records are useful for guarded framing:

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-pcb-fabrication-process-page-en.md`

These support posture such as:

- heavy-copper and advanced fabrication belong to a special-process family
- plating-related process complexity deserves separate routing from ordinary multilayer claims
- exact process or build-window values remain internal, refresh-sensitive claims

### Finish And Standards Boundary Support

[selective-multi-finish-strategy.md](/code/blogs/llm_wiki/facts/methods/selective-multi-finish-strategy.md), [ipc-finish-standards-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-finish-standards-metadata.md), and `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-surface-finishes-page-en.md` already support these guarded statements:

- finish selection and finish-stack framing should stay separate from plated-copper capability claims
- public IPC finish metadata is revision control, not clause-level thickness authority
- finish-page wording cannot substitute for maintained plating-build capability

### Thermal-Platform Boundary Support

[mcpcb-ims-and-reflow-source-coverage.md](/code/blogs/llm_wiki/facts/methods/mcpcb-ims-and-reflow-source-coverage.md) already supports these guarded statements:

- metal-core and thermal-platform context must stay tied to the correct material and process layer
- thermal-platform process context is not generic plated-copper authority

## Current Blocker Statement

Current blocker for this bucket:

- there is no registered `Tier 1 internal dated capability record` yet for plating-thickness or build-allowance capability with explicit scope, owner, measurement basis, and refresh discipline

Under [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md), that means:

- reusable plating-thickness/build-allowance numbers remain `needs_source`
- internal heavy-copper, fabrication-process, and finish pages remain `downgrade` / posture-only support
- no plating-thickness/build-allowance capability fact card can exist yet
- no blog or evidence pack may reuse plating-thickness/build-allowance numbers as governed capability numerics

Current corpus posture is therefore:

- finish/plating workflow boundary control: supported
- heavy-copper and special-process posture: supported
- reusable plating-thickness/build-allowance numbers: blocked

## Claim-Splitting Rule For This Bucket

Every plating-thickness/build-allowance-related claim must be split into one of the following buckets before disposition.

### 1. Plating Thickness / Build Allowance Capability

This is the actual H2 bucket target.

Examples:

- plating-thickness capability presented as current production authority
- conductor-build or hole-build allowance presented as a maintained shop default
- plating-growth value framed as routine process capability

Handling:

- H2 bucket item
- currently `needs_source`
- cannot be reused until a dated internal capability record exists

### 2. Finished Copper-Weight Capability

This is not plating-thickness/build-allowance capability.

Examples:

- copper-weight ladder
- heavy-copper range presented as board capability
- ounce-based production window

Handling:

- route to `copper_weight_capability`
- do not mix into plating-thickness/build-allowance capability

### 3. Etch Compensation Or Conductor-Reduction Allowance

This is not plating-thickness/build-allowance capability.

Examples:

- trace-width compensation
- conductor reduction allowance
- etch adjustment value

Handling:

- route to the future `etch_compensation` child bucket
- do not mix into plating-thickness/build-allowance capability

### 4. Finish Thickness Or Finish-Stack Specification

This is not plated-copper capability.

Examples:

- ENIG thickness stack
- ENEPIG finish-stack wording
- hard-gold thickness or finish specification

Handling:

- `downgrade` for finish-selection posture if kept non-numeric
- `delete` when reused as plated-copper capability proof

### 5. Standards Minimum Or Acceptance Threshold

This is not shop capability.

Examples:

- IPC minimum or threshold wording
- class-linked acceptance criteria
- finish-standard references reused as process authority

Handling:

- `delete`
- do not allow standards minima to piggyback into H2 capability facts

### 6. Stackup Recipe Or Named Process Example

This is not automatically capability proof.

Examples:

- one process guide with one buildup sequence
- one stackup or via example implying plating growth
- one article recipe with a named plating allowance

Handling:

- `downgrade` when kept as non-numeric context
- `delete` if promoted as a transferable manufacturing rule

## Disposition Guidance For Common Claim Shapes

### exact plating-thickness or buildup value on an internal page only

- disposition: `needs_source`
- reason:
  - internal support page without a `Tier 1` dated capability record

### finish-page or finish-standard wording reused as plated-copper capability

- disposition: `delete`
- reason:
  - finish guidance and revision metadata are not plated-copper capability proof

### heavy-copper page using plating-related process language next to build values

- disposition:
  - `downgrade` for process-family posture
  - `needs_source` for any reusable plating/build capability number

### supplier process-guide example used as universal buildup rule

- disposition: `delete`
- reason:
  - named process guide is context only, not shop capability evidence

### plating/build value mixed into copper-weight or etch claim

- disposition:
  - split claim first
  - plating/build portion: `needs_source`
  - copper-weight or etch portion: route to its own child bucket

## Exact Next-Step Requirements Before Any Fact Card Could Exist

Before any `plating_thickness_build_allowance` fact card could exist, the repo still needs:

1. a registered `Tier 1 internal dated capability record` for plating-thickness/build-allowance capability
2. explicit separation between plated buildup and finished copper-weight capability
3. explicit separation between plated buildup and finish-stack specification
4. explicit separation between plated buildup and etch-compensation allowances
5. usable date, owner, scope, measurement basis, and refresh posture for any future plating/build record

Until those conditions are met, `plating_thickness_build_allowance` remains a governed but blocked H2 numeric bucket.
