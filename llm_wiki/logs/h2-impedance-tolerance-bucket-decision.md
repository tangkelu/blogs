# H2 Impedance Tolerance Bucket Decision

Date: 2026-04-25

## Purpose

This document records the bucket-level governance decision for `impedance_tolerance`, the first execution bucket under `H2 Workstream 2: Fabrication Capability Numeric Layer`.

It converts current corpus findings into a controlled decision sheet before any capability-number recovery starts.

This file is:

- a governance and dependency document
- a bucket-level handling decision
- a stop/go control for future recovery work

This file is not:

- a numeric fact card
- permission to reuse impedance tolerance numbers
- a customer-facing claim source
- a substitute for a dated internal capability record

## Why `impedance_tolerance` Is First In H2

`impedance_tolerance` is the right first H2 bucket because it is one of the most repeated fabrication-capability claim shapes across the layer-count blog program, while also being one of the easiest classes to overstate.

Current demand-side evidence already shows repeated dependence on impedance-tolerance-style claims:

- `6-layer`: `±8%` impedance
- `8-layer`: `±8%` and optional `±5%` impedance
- `10-layer`: `±8%`
- `12-layer`: `±8%` impedance plus nearby TDR / VNA and skew language
- `18-layer`: exact impedance promises remain a current-draft risk
- `24-layer`: shop-specific impedance promises remain a current-draft risk

This bucket also sits at the intersection of three claim classes that the repo must not blur together:

- fabrication capability numerics
- validation posture
- SI / channel-performance interpretation

Because that split is central to the entire H2/H3/H4 boundary, `impedance_tolerance` is the best first control bucket.

## What This Bucket Includes

This bucket includes numeric claims that assert, imply, or strongly suggest a current manufacturable impedance-control tolerance as a fabrication capability.

In scope:

- controlled-impedance tolerance promises
- standard versus tighter impedance tolerance bands
- tolerance numbers attached to a shop capability summary
- tolerance numbers attached to a board family, process family, or service page
- tolerance numbers attached to coupon or TDR language when the draft is clearly turning them into a manufacturable capability promise

Typical claim shapes:

- `±X% impedance`
- `±Y ohm class targets`
- `standard tolerance` versus `tight tolerance`
- impedance tolerance presented as a routine production default

## What This Bucket Excludes

This bucket does not govern:

- target impedances such as `50Ω`, `85Ω`, `90Ω`, or `100Ω` when they are interface or stackup design targets rather than shop capability promises
- TDR, coupon, microsection, or VNA presence claims by themselves
- SI, channel, resonance, skew, insertion-loss, or return-loss numerics
- material-property numbers such as `Dk`, `Df`, `Tg`, or copper profile
- standards thresholds or acceptance criteria
- dynamic commercial promises attached to impedance support

Excluded examples:

- `DDR5 80Ω`
- `100Ω differential`
- `stub effects above 3 GHz`
- `20GHz VNA`
- `56G / 112G channel-performance claims`

Those belong to separate governance layers even if they appear next to impedance wording.

## Current Corpus Support Already Available

The current corpus is already strong enough to support impedance-control posture and validation-stage framing.

It is not strong enough to support reusable impedance tolerance numbers.

### Verification Posture

[controlled-impedance-tdr-verification-posture.md](/code/blogs/llm_wiki/facts/methods/controlled-impedance-tdr-verification-posture.md) already supports these guarded statements:

- internal pages repeatedly pair controlled impedance with verification
- impedance targets are linked to TDR, coupon-style validation, or similar measurement language
- high-speed, HDI, multilayer, and PTFE pages all connect impedance language to verification posture

Its non-claims already matter for this bucket:

- exact tolerance bands are refresh-sensitive internal claims
- exact verification percentages are refresh-sensitive internal claims
- the card does not claim a universal impedance tolerance across all structures or programs

### Planning Posture

[spread-glass-and-controlled-impedance-planning.md](/code/blogs/llm_wiki/facts/methods/spread-glass-and-controlled-impedance-planning.md) supports planning-side wording:

- spread-glass selection, stackup planning, copper profile, resin system, coupon planning, and TDR/VNA planning are linked decisions
- reference stackups are starting templates only
- final geometry must be simulated with actual material and compensation data

Its non-claims already matter for this bucket:

- it does not guarantee a specific impedance tolerance for every stackup
- it does not replace simulation or production coupon measurement

### Validation Ladder

[validation-ladder-from-e-test-to-si-verification.md](/code/blogs/llm_wiki/wiki/testing/validation-ladder-from-e-test-to-si-verification.md) already supports the evidence split this bucket needs:

- e-test, AOI, ICT, TDR, and VNA are not interchangeable
- impedance correlation is a separate layer from deeper SI verification
- TDR is not full-path insertion-loss or S-parameter validation
- listing VNA on a capability page does not mean every order gets the same scope

### Advanced Process Framing

[advanced-pcb-fabrication-and-stackup-planning.md](/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md) already supports guarded process language:

- controlled impedance is part of advanced stackup planning
- impedance evidence is usually coupon, TDR, or project-specific validation
- exact impedance tolerance, coupon requirements, and VNA scope must refresh before publication

## Current Blocker Statement

Current blocker for this bucket:

- there is no registered `Tier 1 internal dated capability record` yet for impedance tolerance

Under [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md), that means:

- impedance tolerance numbers remain `needs_source`
- internal process pages remain `downgrade` / posture-only support
- no impedance-tolerance capability fact card can exist yet
- no blog or evidence pack may reuse tolerance numbers as governed capability numerics

Current corpus posture is therefore:

- verification posture: supported
- planning posture: supported
- validation ladder separation: supported
- reusable tolerance numbers: blocked

## Claim-Splitting Rule For This Bucket

Every impedance-related claim must be split into one of the following buckets before disposition:

### 1. Impedance-Tolerance Promise

This is a fabrication capability claim.

Examples:

- `±8% impedance`
- `optional tighter tolerance`
- `standard impedance control tolerance`

Handling:

- H2 bucket item
- currently `needs_source`
- cannot be reused until a dated internal capability record exists

### 2. TDR / Coupon / VNA Presence

This is a verification-posture or validation-scope claim, not an impedance-tolerance number by default.

Examples:

- impedance coupons are used
- TDR is part of verification
- VNA may be part of advanced validation

Handling:

- may remain as posture support
- must not be rewritten into a tolerance guarantee
- exact percentages, scope, and ceilings remain refresh-sensitive

### 3. SI / Channel-Performance Number

This is not a fabrication capability claim even if it appears inside impedance sections.

Examples:

- channel budget
- insertion loss
- resonance thresholds
- skew performance
- eye-opening or return-loss outcome

Handling:

- exclude from this bucket
- do not allow these numbers to piggyback on impedance-control language

## Bucket Guidance For Common Claim Shapes

### `±X% impedance` on an internal page

- disposition: `needs_source`
- reason: this is a capability promise without a dated capability record

### `±Y ohm` target paired with TDR language

- disposition: `needs_source` for the tolerance portion
- disposition: `downgrade` for the TDR / verification-posture portion when it is being separated from the blocked numeric promise
- reason: target band and verification posture are separate claims

### `controlled impedance with TDR verification`

- disposition: `downgrade`
- reason: posture is supported; no numeric capability promise is required

### `controlled impedance with coupon verification and VNA support`

- disposition: `downgrade`
- reason: validation ladder posture is supported; this is not yet a reusable tolerance fact

### `50Ω / 90Ω / 100Ω impedance tables` presented as shop manufacturability rules

- disposition: `downgrade` or `delete`, depending on wording
- reason: these are usually stackup-design targets or interface context, not governed shop capability numerics

### `impedance tolerance tied to DDR / PCIe / 56G / 112G outcome`

- disposition: `delete`
- reason: this merges fabrication capability with unsupported SI/performance claims

### `tighter impedance tolerance because spread-glass is used`

- disposition: `downgrade`
- reason: spread-glass planning posture is supportable, but the numeric tolerance implication is not yet governed

### `100% TDR` or universal coupon coverage claims

- disposition: `needs_source`
- reason: this is a numeric verification-scope promise, not just posture

## Per-Blog Impact Summary

### `6-layer`

- directly affected by `±8%` impedance language
- current safe output: keep impedance-control posture, remove or hold numeric tolerance

### `8-layer`

- directly affected by `±8%` and optional tighter tolerance language
- current safe output: retain controlled-impedance discussion, strip unsupported tolerance bands

### `10-layer`

- directly affected by capability-bundle wording that mixes blind-via, tolerance, and impedance claims
- current safe output: keep multilayer / validation posture, hold numeric tolerance

### `12-layer`

- one of the highest-impact blogs for this bucket
- mixes `±8%` impedance, backdrill, skew matching, and `20GHz` VNA in one cluster
- current safe output: split capability promise from validation posture and from SI/performance numerics

### `18-layer`

- current readiness notes explicitly flag exact impedance promises as a draft risk
- current safe output: keep hybrid material / validation framing, block tolerance promises

### `24-layer`

- current readiness notes explicitly flag impedance promises and measurement guarantees as a draft risk
- current safe output: keep high-speed validation framing, block tolerance guarantees

### `20-layer` and `22-layer`

- not the primary impedance-tolerance blogs, but the bucket still matters because unsupported capability numerics compound their already blocked posture
- current safe output: do not let impedance-control wording reopen blocked capability claims

## Exact Next-Step Requirements Before Any Capability Fact Card Can Exist

No impedance-tolerance capability fact card may be created until all of the following exist:

1. a registered `Tier 1 internal dated capability record` for impedance tolerance
2. explicit scope for that record
   - board family
   - plant / line / region context if relevant
   - structure scope or limitation if relevant
3. clear provenance fields as required by `h2-capability-number-policy.md`
   - `capability_family`
   - `number_type`
   - `value`
   - `unit`
   - `scope`
   - `source_tier`
   - `source_id`
   - `captured_at`
   - `effective_date`
   - `review_by`
   - `owner`
   - `refresh_interval`
   - `confidence`
   - `customer_facing_allowed`
   - `notes_on_limits`
4. a bucket-specific non-claims section stating that the number does not prove:
   - universal tolerance across all stackups
   - universal coupon scope
   - SI or channel-performance outcome
   - standards acceptance or qualification status
5. a clean split between:
   - impedance tolerance promise
   - TDR / coupon / VNA presence
   - SI/performance interpretation
6. a re-check of all affected blog claim clusters against this bucket decision

If any one of those conditions is missing, the bucket remains:

- `framing supported`
- `numeric capability blocked`

## Current Bucket Decision

Decision as of `2026-04-25`:

- `impedance_tolerance` remains an active H2 bucket
- current corpus is sufficient for posture, planning, and validation-ladder support
- current corpus is not sufficient for reusable impedance tolerance numerics
- all impedance tolerance numbers remain `needs_source`
- no capability fact card should be created yet

This bucket is therefore:

- ready for governance
- not ready for numeric promotion
