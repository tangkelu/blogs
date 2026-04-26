# H2 Copper Weight Capability Bucket Decision

Date: 2026-04-25

## Purpose

This document records the bucket-level governance decision for `copper_weight_capability` under `H2 Workstream 2: Fabrication Capability Numeric Layer`.

It converts the first safe child split from the held `copper_plating_process_windows` area into a controlled decision sheet before any copper-weight numeric recovery starts.

This file is:

- a governance and dependency document
- a bucket-level handling decision
- a stop/go control for future recovery work

This file is not:

- a numeric fact card
- permission to reuse copper-weight numbers
- a customer-facing claim source
- a substitute for a `Tier 1 internal dated capability record`

## Why `copper_weight_capability` Is A Distinct H2 Child Bucket

`copper_weight_capability` is the first safe child split under the previously held `copper_plating_process_windows` area because copper-weight claims can be separated more cleanly than plating thickness, etch compensation, or process-balance notes.

This bucket exists to stop several common collapse errors:

- heavy-copper product posture being rewritten as a transferable copper-weight ladder
- stackup copper examples being rewritten as maintained shop capability
- current-carrying or thermal design context being rewritten as fabrication authority
- plating or conductor-build language being confused with finished copper-weight capability

Current H2 demand already shows repeated dependence on copper-weight-style claims:

- `6-layer`: power and thermal route framing with implicit copper ladders
- `8-layer`: stackup tables that mix copper weights with dielectric examples
- `12-layer`: layer-by-layer copper assumptions drifting into generic manufacturability
- `14-layer`: current-density and power-routing clusters mixed with process claims
- `16-layer`: heavy-copper and thermal-platform wording
- `20-layer`: complex build examples where copper-weight assumptions can be over-read as factory defaults

Because those claim families are easy to flatten into one unsupported default, `copper_weight_capability` requires its own governance layer before any recovery attempt.

## What This Bucket Includes

This bucket includes numeric claims that assert, imply, or strongly suggest what finished copper-weight range a fabricator can currently produce as an operational capability.

In scope:

- finished copper-weight capability windows presented as current production authority
- standard copper-weight ladders presented as shop defaults
- copper-weight claims framed as routine manufacturing capability across ordinary or heavy-copper builds
- copper-weight values rewritten as maintained fabrication limits rather than one-off examples

Typical claim shapes:

- `1 oz / 2 oz / 3 oz / 4 oz / 6 oz` capability ladder
- standard versus heavy-copper copper-weight window
- copper-weight range presented as a routine production offering
- copper-weight capability tied to board family rather than one stackup example

## What This Bucket Excludes

This bucket does not govern:

- plating thickness or build allowance
- etch compensation or conductor-reduction allowances
- resin-fill, planarization, balance, or other heavy-copper process notes
- stackup recipe examples using one copper allocation
- current-carrying charts or electrical/thermal design rules
- IMS, ceramic, or other thermal-platform comparison by itself
- standards minima or workmanship thresholds
- supplier application notes used only for material discovery

Excluded examples:

- one stackup listing `1 oz` outer copper and `0.5 oz` inner copper
- one heavy-copper process note discussing resin balance or planarization
- current-versus-temperature guidance rewritten as a fabrication ladder
- plating or conductor-build values presented as if they were finished copper-weight authority
- official material/application pages used as copper-weight capability proof

Those belong to other governance layers even when they appear next to copper-weight wording.

## Current Corpus Support And Non-Claim Boundaries

The current corpus is already strong enough to support heavy-copper posture, special-process routing, and non-claim boundaries around copper-weight capability.

It is not strong enough to support reusable copper-weight numbers.

### Process-Family And Routing Support

[pcb-service-routing-from-prototype-to-special-process.md](/code/blogs/llm_wiki/wiki/processes/pcb-service-routing-from-prototype-to-special-process.md) and [pcb-stackup-special-process-and-baseline-families.md](/code/blogs/llm_wiki/facts/methods/pcb-stackup-special-process-and-baseline-families.md) already support these guarded statements:

- heavy copper is a distinct power and thermal route, not just thicker standard FR-4
- service routing, stackup planning, and special-process family selection should stay separate
- exact copper-weight values remain refresh-sensitive internal claims

### Thermal-Platform Boundary Support

[thermal-pcb-platform-selection-posture.md](/code/blogs/llm_wiki/facts/methods/thermal-pcb-platform-selection-posture.md) already supports these guarded statements:

- heavy copper, MCPCB, and ceramic are separate thermal platforms
- heavy-copper framing should not be collapsed into other thermal routes
- conductivity, temperature, and load figures are refresh-sensitive internal claims

### Internal Heavy-Copper Posture Support

The following internal registry records are useful for guarded framing:

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-heavy-copper-pcb-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-heavy-copper-pcb-product-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-advanced-pcb-manufacturing-page-en.md`

These support posture such as:

- heavy copper belongs to a special-process manufacturing family
- power, thermal, and bus-bar language can remain as route framing
- exact ounce-style windows remain internal, refresh-sensitive claims

## Current Blocker Statement

Current blocker for this bucket:

- there is no registered `Tier 1 internal dated capability record` yet for finished copper-weight capability

Under [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md), that means:

- reusable copper-weight numbers remain `needs_source`
- internal heavy-copper and fabrication pages remain `downgrade` / posture-only support
- no copper-weight capability fact card can exist yet
- no blog or evidence pack may reuse copper-weight numbers as governed capability numerics

Current corpus posture is therefore:

- heavy-copper route framing: supported
- thermal-platform and special-process boundary control: supported
- reusable copper-weight numbers: blocked

## Claim-Splitting Rule For This Bucket

Every copper-weight-related claim must be split into one of the following buckets before disposition.

### 1. Finished Copper-Weight Capability

This is the actual H2 bucket target.

Examples:

- finished copper-weight range presented as current production capability
- standard copper-weight ladder presented as a maintained shop default
- heavy-copper range presented as routine fabrication authority

Handling:

- H2 bucket item
- currently `needs_source`
- cannot be reused until a dated internal capability record exists

### 2. Plating Thickness / Build Allowance

This is not finished copper-weight capability.

Examples:

- hole-copper plating thickness
- conductor-build allowance
- plating-growth wording

Handling:

- route to the future `plating_thickness_build_allowance` child bucket
- do not mix into copper-weight capability

### 3. Etch Compensation Or Conductor-Reduction Allowance

This is not finished copper-weight capability.

Examples:

- etch compensation value
- conductor reduction allowance
- trace-width compensation tied to copper thickness

Handling:

- route to the future `etch_compensation` child bucket
- do not mix into copper-weight capability

### 4. Stackup Example Or Layer Recipe

This is not automatically capability proof.

Examples:

- outer copper and inner copper values in one reference stackup
- one layer-by-layer copper allocation table
- one article example using one copper family

Handling:

- `downgrade` when kept as non-numeric planning shorthand
- `delete` if promoted as a transferable manufacturing rule

### 5. Current-Carrying / Thermal Design Context

This is not fabrication capability by itself.

Examples:

- current-carrying chart
- thermal load design guidance
- power-electronics context numbers

Handling:

- `downgrade` when kept as application context
- not valid as copper-weight capability proof

## Disposition Guidance For Common Claim Shapes

### exact copper-weight ladder on an internal heavy-copper page only

- disposition: `needs_source`
- reason:
  - internal support page without a `Tier 1` dated capability record

### stackup recipe showing one copper allocation per layer

- disposition:
  - `downgrade` as planning context if the numbers are removed
  - `delete` if promoted as a transferable capability rule

### heavy-copper product page using current or thermal performance language next to ounce values

- disposition:
  - `downgrade` for process-family and application posture
  - `needs_source` for any reusable copper-weight capability number

### plating or compensation value mixed into a copper-weight claim

- disposition:
  - split claim first
  - copper-weight portion: `needs_source`
  - plating / compensation portion: route to its own child bucket

### supplier heavy-copper application page used as capability proof

- disposition: `delete` for numeric recovery
- reason:
  - supplier application context is not shop capability evidence

## Exact Next-Step Requirements Before Any Fact Card Could Exist

Before any `copper_weight_capability` fact card could exist, the repo still needs:

1. a registered `Tier 1 internal dated capability record` for finished copper-weight capability
2. explicit separation between finished copper weight and plating/build allowance
3. explicit separation between copper-weight capability and current-carrying or thermal design context
4. explicit separation between stackup examples and maintained production windows
5. usable date, owner, scope, and refresh posture for any future copper-weight record

Until those conditions are met, `copper_weight_capability` remains a governed but blocked H2 numeric bucket.
