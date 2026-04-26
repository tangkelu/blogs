# H2 Annular Ring Bucket Decision

Date: 2026-04-25

## Purpose

This document records the bucket-level governance decision for `annular_ring` under `H2 Workstream 2: Fabrication Capability Numeric Layer`.

It converts current corpus findings into a controlled decision sheet before any annular-ring numeric recovery starts.

This file is:

- a governance and dependency document
- a bucket-level handling decision
- a stop/go control for future recovery work

This file is not:

- a numeric fact card
- permission to reuse annular-ring numbers
- a customer-facing claim source
- a substitute for a `Tier 1 internal dated capability record`

## Why `annular_ring` Is A Distinct H2 Bucket

`annular_ring` is a high-risk fabrication-capability bucket because annular-ring wording is repeatedly collapsed across claim classes that are not equivalent:

- shop annular-ring capability
- standards or acceptability thresholds
- design-rule cookbook guidance
- drill / registration interaction
- stackup or example leakage

This is one of the easiest places for class-based language to be rewritten as factory capability.

Current H2 demand already shows repeated dependence on annular-ring-style claims:

- `6-layer`: via and manufacturability rule summaries
- `10-layer`: drill-to-pad and breakout-style wording
- `14-layer`: dense DFM rule bundles
- `20-layer`: high-risk geometry clusters mixed with standards leakage
- `22-layer`: compliance and high-reliability overlap risk

Because those claim families are easy to flatten into one unsupported number, `annular_ring` needs its own governance split before any recovery attempt.

## What This Bucket Includes

This bucket includes numeric claims that assert, imply, or strongly suggest what annular ring a fabricator can currently produce as an operational capability.

In scope:

- minimum annular-ring capability claims
- breakout-margin claims rewritten as capability
- annular-ring targets presented as standard production defaults
- annular-ring values treated as routine manufacturing limits

Typical claim shapes:

- minimum annular ring
- breakout margin
- manufacturable pad-to-hole margin
- standard annular-ring target presented as a shop default

## What This Bucket Excludes

This bucket does not govern:

- IPC class or acceptability thresholds
- addendum or qualification-program thresholds
- generic PCB design-rule cookbook values
- drill-to-pad registration posture by itself
- stackup examples or one-off via examples
- rigid-flex or high-reliability language when it is really compliance framing

Excluded examples:

- `IPC Class 2 / Class 3` annular-ring tables
- addendum-style annular-ring or breakout thresholds
- one layout-rule table presented as a universal manufacturing rule
- stackup illustrations with one annular-ring example
- drill registration discussion without a true capability record

Those belong to other governance layers even when they appear next to annular-ring wording.

## Current Corpus Support And Non-Claim Boundaries

The current corpus is already strong enough to support manufacturability posture, standards-boundary control, and drill / registration interaction framing around annular ring.

It is not strong enough to support reusable annular-ring numbers.

### Process And Manufacturability Support

[advanced-pcb-fabrication-and-stackup-planning.md](/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md) already supports these guarded statements:

- high-layer and advanced rigid boards need tighter drill, lamination, and registration discipline
- geometry-style claims should not be harvested directly from process pages
- exact capability figures remain refresh-sensitive internal claims

### Registration And Interaction Support

[high-layer-count-backdrill-and-registration-posture.md](/code/blogs/llm_wiki/facts/methods/high-layer-count-backdrill-and-registration-posture.md) already supports these guarded statements:

- high-layer manufacturability depends on registration and drill-control discipline
- interaction language may be kept as guarded posture
- registration-sensitive wording does not authorize annular-ring numerics

### Standards Boundary Support

[ipc-6012-addendum-program-metadata.md](/code/blogs/llm_wiki/facts/standards/ipc-6012-addendum-program-metadata.md) and [22-layer-high-reliability-rewrite-guardrail.md](/code/blogs/llm_wiki/facts/standards/22-layer-high-reliability-rewrite-guardrail.md) already support these guarded statements:

- public standards metadata can identify clause families and risk zones
- public standards metadata does not provide reusable annular-ring values
- class-based thresholds must not be rewritten as factory capability

This is useful for boundary control, not annular-ring numeric authorization.

## Current Blocker Statement

Current blocker for this bucket:

- there is no registered `Tier 1 internal dated capability record` yet for annular-ring capability

Under [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md), that means:

- reusable annular-ring numbers remain `needs_source`
- class-linked or standards-derived annular-ring tables remain `delete`
- internal product and process pages remain `downgrade` / posture-only support
- no annular-ring capability fact card can exist yet
- no blog or evidence pack may reuse annular-ring numbers as governed capability numerics

Current corpus posture is therefore:

- manufacturability and registration interaction framing: supported
- standards / acceptability boundary control: supported
- reusable annular-ring numbers: blocked

## Claim-Splitting Rule For This Bucket

Every annular-ring-related claim must be split into one of the following buckets before disposition.

### 1. Shop Annular-Ring Capability

This is the actual H2 bucket target.

Examples:

- minimum annular-ring capability
- annular-ring target presented as current shop default
- breakout allowance presented as maintained factory capability

Handling:

- H2 bucket item
- currently `needs_source`
- cannot be reused until a dated internal capability record exists

### 2. Standards Or Acceptability Threshold

This is not shop capability.

Examples:

- `IPC Class 2 / 3 / 3A` thresholds
- addendum or high-reliability thresholds
- class-linked breakout limits

Handling:

- `delete`
- do not allow standards thresholds to piggyback into H2 capability facts

### 3. Design-Rule Cookbook Threshold

This is not automatically capability proof.

Examples:

- generic PCB layout-rule table
- default drill-to-pad margin recommendation
- cookbook breakout allowance presented as universal

Handling:

- usually `delete`
- may remain only as non-numeric planning caution
- must not be promoted into factory capability

### 4. Registration / Drill Interaction

This is interaction posture, not standalone annular-ring capability.

Examples:

- drill-to-pad interaction wording
- breakout risk driven by registration sensitivity
- high-layer registration caution

Handling:

- usually `downgrade` when kept as guarded process posture
- not valid as annular-ring numeric authority

### 5. Stackup Or Example Leakage

This is not a maintained capability claim.

Examples:

- one stackup or via example showing one annular-ring value
- one article recipe using one pad / hole margin
- one rigid-flex or hi-rel example treated as shop default

Handling:

- `downgrade` if kept as non-numeric planning context
- `delete` if promoted as universal numeric rule

## Disposition Guidance For Common Claim Shapes

### exact annular-ring number presented as current shop capability from internal page only

- disposition: `needs_source`
- reason:
  - internal support page without a `Tier 1` dated capability record

### `IPC Class 2` or `Class 3` annular-ring number presented as manufacturing capability

- disposition: `delete`
- reason:
  - standards or acceptability threshold, not H2 capability evidence

### breakout rule or drill-to-pad margin from a cookbook-style article

- disposition: `delete`
- reason:
  - design-rule guidance is not factory capability proof

### high-layer or drill-registration wording without a specific capability number

- disposition: `downgrade`
- reason:
  - safe as manufacturability posture only

### stackup or via example that includes one annular-ring value

- disposition:
  - `downgrade` as planning context if the number is removed
  - `delete` if promoted as a transferable rule

## Exact Next-Step Requirements Before Any Fact Card Could Exist

Before any `annular_ring` fact card could exist, the repo still needs:

1. a registered `Tier 1 internal dated capability record` for annular-ring capability
2. explicit separation between shop capability and class / acceptability thresholds
3. explicit separation between annular-ring capability and registration-interaction posture
4. explicit separation between cookbook guidance and maintained production limits
5. usable date, owner, scope, and refresh posture for any future annular-ring record

Until those conditions are met, `annular_ring` remains a governed but blocked H2 numeric bucket.
