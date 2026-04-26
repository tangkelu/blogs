# H2 Registration Bucket Decision

Date: 2026-04-25

## Purpose

This document records the bucket-level governance decision for `registration` inside `H2 Workstream 2: Fabrication Capability Numeric Layer`.

It converts current corpus findings into a controlled decision sheet before any capability-number recovery starts.

This file is:

- a governance and dependency document
- a bucket-level handling decision
- a stop/go control for future recovery work

This file is not:

- a numeric fact card
- permission to reuse registration numbers
- a customer-facing claim source
- a substitute for a dated internal capability record

## Why `registration` Is A Priority H2 Bucket

`registration` is one of the core fabrication-capability claim families in the layer-count blog program because it appears wherever multilayer density, sequential lamination, backdrill, hybrid stackups, or rigid-flex transitions are discussed.

Current demand-side evidence already shows that registration-style claims are repeatedly entangled with other categories the repo must not blur together:

- high-layer manufacturability posture
- backdrill and sequential-lamination process posture
- standards or class-language claims
- warpage / flatness / dimensional-control language
- SI or hybrid-transition claims

This bucket is therefore high value for H2 because weak handling creates a predictable failure mode:

- internal high-layer or rigid-flex pages are read as if they authorize a reusable alignment-tolerance number
- standards or class wording gets flattened into shop capability
- warpage, flatness, skew, or transition-control language gets smuggled in as registration proof

## What This Bucket Includes

This bucket includes numeric claims that assert, imply, or strongly suggest a current manufacturable registration capability as a fabrication capability.

In scope:

- layer-to-layer registration capability claims
- drill-to-pad or interlayer alignment claims when written as shop capability
- registration-tolerance numbers attached to multilayer or high-layer build summaries
- registration numbers attached to sequential lamination or advanced-process capability banners
- rigid-flex registration claims when written as transferable fabrication capability rather than project-specific posture

Typical claim shapes:

- registration tolerance in a capability summary
- alignment tolerance in a multilayer or high-layer service page
- tolerance wording attached to backdrill, stackup, or transition-control sections
- registration numbers embedded in DFM or manufacturability rule lists

## What This Bucket Excludes

This bucket does not govern:

- generic process posture saying high-layer boards are more alignment-sensitive
- standards or class thresholds presented as inspection or acceptance requirements
- warpage, flatness, bow/twist, or dimensional-stability numerics
- skew, SI, RF-transition, or channel-performance numerics
- stackup recipe or lamination-count examples
- dynamic commercial promises attached to advanced registration capability
- pure architecture vocabulary such as hybrid stackup, sequential lamination, or rigid-flex transition wording when no numeric capability is asserted

Excluded examples:

- class-linked registration or workmanship claims
- bow / twist / flatness thresholds
- skew or transition-quality numerics
- hybrid RF transition claims used as SI evidence
- lamination examples rewritten as registration guarantees

Those belong to separate governance layers even if they appear next to registration wording.

## Current Corpus Support Already Available

The current corpus is already strong enough to support registration posture, coupled-process framing, and boundary control.

It is not strong enough to support reusable registration numbers.

### Coupled High-Layer Posture

[high-layer-count-backdrill-and-registration-posture.md](/code/blogs/llm_wiki/facts/methods/high-layer-count-backdrill-and-registration-posture.md) already supports these guarded statements:

- dense multilayer fabrication is treated as a coupled control problem
- registration, sequential lamination, and backdrill are repeatedly presented together
- high-layer growth raises alignment risk and via-stub sensitivity together

Its non-claims already matter for this bucket:

- layer-count, feature-size, and tolerance numbers are refresh-sensitive internal claims
- it does not state universal tolerance or layer-count limits

### High-Layer Manufacturability Context

[high-layer-rigid-board-manufacturability-context.md](/code/blogs/llm_wiki/facts/methods/high-layer-rigid-board-manufacturability-context.md) supports guarded manufacturability wording:

- high-layer rigid boards require tighter handling discipline, dimensional-movement control, artwork compensation, and lamination planning
- supplier process guides can support a cautious statement that higher-layer rigid boards become more registration-sensitive and fabrication-sensitive

Its non-claims already matter for this bucket:

- it does not provide registration tolerances
- it does not turn supplier process guides into capability tables
- it does not provide transferable recipes or process-window numerics

### Advanced Process Framing

[advanced-pcb-fabrication-and-stackup-planning.md](/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md) already supports process-side wording:

- high-layer registration belongs inside advanced stackup planning
- registration must be kept separate from impedance, HDI, rigid-flex, substrate, and thermal decisions
- exact registration limits must refresh before publication

### Hybrid RF Boundary

[hybrid-rf-stackup-strategy.md](/code/blogs/llm_wiki/wiki/processes/hybrid-rf-stackup-strategy.md) supports one important boundary for this bucket:

- hybrid RF builds should describe lamination, transition review, registration, and validation as separate decisions
- registration language in hybrid stackups is manufacturability posture, not proof of universal tolerance or RF outcome

## Current Blocker Statement

Current blocker for this bucket:

- there is no registered `Tier 1 internal dated capability record` yet for registration capability

Under `h2-capability-number-policy.md`, that means:

- registration numbers remain `needs_source`
- internal process and product pages remain `downgrade` / posture-only support
- no registration capability fact card can exist yet
- no blog or evidence pack may reuse registration numbers as governed capability numerics

Current corpus posture is therefore:

- process posture: supported
- boundary control: supported
- reusable registration numbers: blocked

## Claim-Splitting Rule For This Bucket

Every registration-related claim must be split into one of the following claim families before disposition.

### 1. Registration Capability

This is the H2 capability claim.

Examples:

- layer-to-layer registration tolerance
- drill-to-pad alignment tolerance
- registration tolerance presented as a routine production default

Handling:

- H2 bucket item
- currently `needs_source`
- cannot be reused until a dated internal capability record exists

### 2. Process Posture

This is not a reusable registration number by default.

Examples:

- high-layer boards need tighter alignment control
- sequential lamination increases registration sensitivity
- hybrid builds need transition and lamination review

Handling:

- may remain as posture support
- normally `downgrade`
- must not be rewritten into a numeric capability promise

### 3. Standards / Class Claims

This is not H2 capability evidence.

Examples:

- class-linked workmanship or acceptance language
- standards-derived alignment or inspection thresholds
- class framing attached to rigid-flex or advanced-board sections

Handling:

- normally `delete`
- do not allow standards or class wording to piggyback on registration capability

### 4. Warpage / Flatness / SI Claims

These are not registration capability numbers even if they appear nearby.

Examples:

- warpage or flatness thresholds
- skew or SI-related transition numerics
- RF transition-quality numerics in hybrid builds

Handling:

- exclude from this bucket
- `delete` when they are being used as capability proof
- `downgrade` only if reduced to guarded non-numeric context elsewhere

## Bucket Guidance For Common Claim Shapes

### registration tolerance on an internal high-layer or multilayer page

- disposition: `needs_source`
- reason: this is a capability promise without a dated capability record

### optical registration or alignment-control wording without a number

- disposition: `downgrade`
- reason: posture is supported; numeric capability is not

### registration language tied to sequential lamination or backdrill posture

- disposition: `downgrade`
- reason: coupled-process framing is supported; reusable tolerance is not

### rigid-flex registration wording tied to class or workmanship language

- disposition: `delete`
- reason: this merges capability with standards/class claims

### warpage, flatness, or skew number presented as proof of registration quality

- disposition: `delete`
- reason: this collapses separate claim families into unsupported capability proof

### hybrid RF transition-control wording with implied registration guarantee

- disposition: `downgrade`
- reason: hybrid stackup posture is supportable, but not as a numeric capability promise

### one internal registration number presented as universal company capability

- disposition: `delete`
- reason: this is exactly the marketing-page leakage H2 is meant to block

## Per-Blog Impact Summary

### `10-layer`

- directly affected because registration and annular-ring language already sit inside blocked capability clusters
- current safe output: keep high-layer control posture, hold numeric registration claims at `needs_source`

### `12-layer`

- directly affected where fabrication and test workflow sections blend registration-sensitive execution with other advanced capability language
- current safe output: keep coupled-process framing, do not recover registration numerics

### `14-layer`

- directly affected because current-draft risk includes standards-heavy registration and annular-ring threshold leakage
- current safe output: `delete` standards-style registration tables, `downgrade` non-numeric manufacturability wording, keep capability numerics at `needs_source`

### `18-layer`

- affected where high-layer and hybrid-build posture could be misread as registration-capability proof
- current safe output: keep process-sensitivity and validation posture only

### `20-layer`

- affected where any-layer, build-up, and reliability-sensitive language could be flattened into alignment-capability claims
- current safe output: keep registration-sensitive build complexity as guarded posture, not as numeric capability

### `22-layer`

- affected where standards, hi-rel, or acceptance framing could be mistaken for registration capability evidence
- current safe output: keep standards/class language out of H2 registration recovery

### `24-layer`

- affected where high-speed and high-layer build complexity could pull registration claims into SI or verification overreach
- current safe output: keep registration as process posture only, not as a transferable tolerance claim

## Exact Next-Step Requirements Before Any Fact Card Could Exist

All of the following must exist first:

1. a current `Tier 1` dated internal capability record specifically for registration capability
2. explicit scope naming:
   - process family
   - site or line scope if relevant
   - whether the claim is rigid multilayer only, high-layer only, or rigid-flex-inclusive
3. explicit method or interpretation context:
   - what kind of registration is being claimed
   - whether the claim is layer-to-layer, drill-to-pad, or another controlled alignment measure
4. explicit separation from:
   - standards or class claims
   - warpage / flatness / bow-twist numerics
   - SI / skew / transition-quality numerics
   - stackup recipe examples
5. a source-map pass confirming which current internal and external pages are framing-only versus candidate upstream inputs
6. control-doc wording that says the bucket remains in intake or recovery review, not numerically unlocked

Until those conditions are met:

- reusable registration numerics remain blocked
- `registration` stays at `needs_source`
- only downgraded non-numeric manufacturability wording is safe downstream
