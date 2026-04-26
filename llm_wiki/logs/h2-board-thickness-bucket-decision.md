# H2 Board Thickness Bucket Decision

Date: 2026-04-25

## Purpose

This document records the bucket-level governance decision for `board_thickness` under `H2 Workstream 2: Fabrication Capability Numeric Layer`.

It converts current corpus findings into a controlled decision sheet before any board-thickness numeric recovery starts.

This file is:

- a governance and dependency document
- a bucket-level handling decision
- a stop/go control for future recovery work

This file is not:

- a numeric fact card
- permission to reuse board-thickness numbers
- a customer-facing claim source
- a substitute for a `Tier 1 internal dated capability record`

## Why `board_thickness` Is A Distinct H2 Bucket

`board_thickness` is a high-risk fabrication-capability bucket because board-thickness wording is repeatedly flattened across several different claim types that are not equivalent:

- finished board thickness capability
- material thickness availability
- stackup examples or common commercial builds
- rigid-flex, bend, warpage, or other process-behavior claims
- special-platform thickness language such as IMS or metal-core constructions

This bucket therefore exists to stop one common failure mode:

- a thickness number from a stackup example, material page, or special-process page gets rewritten as a transferable finished-board capability claim

Current H2 demand already shows repeated dependence on board-thickness-style numerics:

- `8-layer`: board-thickness assumptions and manufacturing defaults
- `10-layer`: stackup-planning thickness assumptions
- `12-layer`: `1.6-2.4mm` style planning windows and `common` thickness wording
- `14-layer`: rigid stackup thickness examples
- `16-layer`: process-window and power/thermal-adjacent thickness wording
- `18-layer`: high-complexity rigid-board thickness assumptions
- `24-layer`: current-draft risk still includes shop-specific stackup and capability statements

Because those claim families are easy to collapse together, `board_thickness` requires its own governance split before any recovery attempt.

## What This Bucket Includes

This bucket includes numeric claims that assert, imply, or strongly suggest what finished-board thickness range a fabricator can currently produce as an operational capability.

In scope:

- finished board thickness windows presented as current manufacturing capability
- finished thickness numbers presented as standard production defaults
- thickness tolerance promises when they are framed as finished-board capability
- rigid multilayer thickness claims that are being treated as transferable operational limits

Typical claim shapes:

- finished board thickness range
- standard finished-board thickness ladder
- common thickness presented as a routine manufacturing default
- thickness tolerance or control wording presented as a current capability promise

## What This Bucket Excludes

This bucket does not govern:

- laminate, prepreg, core, bond ply, or coverlay thickness availability by itself
- datasheet-side material thickness options
- stackup examples used as design or routing illustrations
- rigid-flex total-thickness and bend-related claims
- warpage, bend-life, or mechanical-behavior claims
- IMS / metal-core base-thickness product examples
- thermal-platform thickness examples
- lead-time or quick-turn assumptions tied to thinner or simpler builds
- standards thresholds or acceptance-style thickness criteria

Excluded examples:

- prepreg or laminate thickness options from official material sources
- `common 1.6 mm` style commercial build examples when they are only stackup shorthand
- rigid-flex thickness combined with bend radius or cycle claims
- metal-core base thickness lists used as platform selection context
- warpage or deformation claims inferred from thickness alone

Those belong to other governance layers even when they appear next to finished-board thickness wording.

## Current Corpus Support And Non-Claim Boundaries

The current corpus is already strong enough to support process posture, planning separation, and non-claim boundaries around board thickness.

It is not strong enough to support reusable board-thickness numbers.

### Process And Planning Support

[advanced-pcb-fabrication-and-stackup-planning.md](/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md) already supports these guarded statements:

- stackup architecture, material family, fabrication route, and validation plan should be kept as separate decisions
- rigid, HDI, rigid-flex, thermal, and substrate frames should not be collapsed together
- internal numeric capabilities such as warpage and other process-linked numbers are refresh-sensitive

This is useful for boundary control, not numeric thickness authorization.

### Schedule And Complexity Boundary Support

[prototype-vs-quick-turn-pcb-routing.md](/code/blogs/llm_wiki/wiki/processes/prototype-vs-quick-turn-pcb-routing.md) already supports these guarded statements:

- low-complexity builds are the natural quick-turn baseline
- multilayer urgency becomes more conditional as stackup and review complexity rise
- schedule posture is not the same thing as manufacturing capability

This helps block thickness numbers from being smuggled in as quick-turn or prototype defaults.

### High-Layer Manufacturability Support

[high-layer-rigid-board-manufacturability-context.md](/code/blogs/llm_wiki/facts/methods/high-layer-rigid-board-manufacturability-context.md) already supports these guarded statements:

- higher-layer rigid boards become more fabrication-sensitive
- dimensional control, lamination planning, and material-form handling matter
- public process guides do not justify board-thickness capability tables

This is directly relevant because it shows the current corpus can support manufacturability wording without unlocking thickness numbers.

## Current Blocker Statement

Current blocker for this bucket:

- there is no registered `Tier 1 internal dated capability record` yet for finished-board thickness capability

Under `h2-capability-number-policy.md`, that means:

- reusable board-thickness numbers remain `needs_source`
- internal product and process pages remain `downgrade` / posture-only support
- no board-thickness capability fact card can exist yet
- no blog or evidence pack may reuse finished-board thickness numbers as governed capability numerics

Current corpus posture is therefore:

- stackup and manufacturability framing: supported
- rigid versus rigid-flex versus thermal-platform boundary control: supported
- reusable finished-board thickness numbers: blocked

## Claim-Splitting Rule For This Bucket

Every thickness-related claim must be split into one of the following buckets before disposition.

### 1. Finished Board Thickness Capability

This is the actual H2 bucket target.

Examples:

- finished board thickness range presented as current production capability
- standard finished thickness ladder presented as a shop default
- thickness tolerance promise tied to finished-board output

Handling:

- H2 bucket item
- currently `needs_source`
- cannot be reused until a dated internal capability record exists

### 2. Material Thickness Availability

This is not finished-board capability.

Examples:

- laminate thickness options
- prepreg or bond-ply thickness availability
- metal-core base thickness options
- coverlay or flex-core thickness options

Handling:

- `keep` only when tied to the correct material or product-grade source layer
- not an H2 board-thickness capability claim by itself
- must not be rewritten into finished-board capability

### 3. Stackup Example Or Common Commercial Build

This is not automatically capability proof.

Examples:

- one reference stackup showing an overall finished thickness
- a `common` rigid-board thickness used as a design example
- one blog table or recipe block listing thickness assumptions

Handling:

- `downgrade` when kept as non-numeric planning shorthand
- `needs_source` if rewritten as a transferable manufacturing rule
- do not promote examples into capability windows

### 4. Warpage / Flex / Bend / Process-Behavior Claim

This is not a pure board-thickness capability claim.

Examples:

- rigid-flex total thickness combined with bend radius
- thickness paired with warpage or bow/twist-style behavior
- process claims where thickness is tied to drilling, lamination, or deformation outcomes

Handling:

- usually `downgrade` when kept as guarded process posture
- `delete` when phrased as universal numeric behavior without the right governance layer
- do not route through H2 finished-board capability by default

## Disposition Guidance For Common Claim Shapes

### finished board thickness range presented as a current shop capability

- disposition: `needs_source`
- reason: this is the actual H2 target, but it requires a `Tier 1` dated capability record

### one `common` thickness presented as the default for multilayer production

- disposition: `downgrade`
- reason: safe only as softened planning context, not as a universal manufacturing default

### stackup recipe showing an overall thickness

- disposition: `downgrade`
- reason: a stackup example is not a finished-board capability record

### material or laminate thickness availability from the correct material source layer

- disposition: `keep`
- reason: this may be valid in the material layer, but it must not be rewritten as finished-board capability

### rigid-flex thickness paired with bend radius, flex life, or dynamic-bend posture

- disposition: `downgrade`
- reason: this is a mechanical/process framing problem, not finished-board capability proof

### warpage or process-behavior claim inferred from thickness alone

- disposition: `delete`
- reason: this overstates a context-bound process effect as a transferable numeric rule

### IMS or metal-core base thickness list rewritten as ordinary rigid-board capability

- disposition: `delete`
- reason: special-platform product options are not proof of generic finished-board capability

## Per-Blog Impact Summary

The immediate effect of this bucket decision is controlled reduction, not recovery.

- `8-layer`
  - board-thickness assumptions may remain only as softened planning context; reusable thickness numbers remain `needs_source`
- `10-layer`
  - stackup-planning thickness examples must stay split from finished-board capability claims
- `12-layer`
  - common-thickness and thickness-window wording remains blocked as reusable capability unless a dated record exists
- `14-layer`
  - rigid-stackup thickness examples may remain only as downgraded examples, not capability proof
- `16-layer`
  - process-window or thermal-adjacent thickness wording remains blocked as transferable manufacturing capability
- `18-layer`
  - high-complexity stackup thickness assumptions may remain only as guarded manufacturability framing
- `24-layer`
  - any shop-style thickness statement remains blocked until finished-board capability is governed through a dated record

## Exact Next-Step Requirements Before Any Fact Card Could Exist

All of the following must exist first:

1. a current `Tier 1 internal dated capability record` specifically for finished-board thickness capability
2. explicit scope naming:
   - rigid multilayer versus rigid-flex versus special thermal platform
   - process family
   - site or line scope if relevant
3. explicit interpretation context:
   - finished board basis rather than laminate or stackup component basis
   - whether thickness tolerance is included
4. explicit separation from:
   - material thickness availability
   - stackup examples
   - warpage / bend / flex-process claims
   - IMS / metal-core platform examples
5. a source-map pass confirming which current internal and external pages are framing-only versus candidate upstream inputs
6. control-doc wording that says the bucket is in intake or recovery review, not numerically unlocked

Until those conditions are met:

- reusable board-thickness numerics remain blocked
- `board_thickness` stays at `needs_source`
- only downgraded non-numeric planning or manufacturability wording is safe downstream
