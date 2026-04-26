# H2 Trace Space Bucket Decision

Date: 2026-04-25

## Purpose

This document records the bucket-level governance decision for `trace_space` under `H2 Workstream 2: Fabrication Capability Numeric Layer`.

It converts current corpus findings into a controlled decision sheet before any trace/space numeric recovery starts.

This file is:

- a governance and dependency document
- a bucket-level handling decision
- a stop/go control for future recovery work

This file is not:

- a numeric fact card
- permission to reuse line/space numbers
- a customer-facing claim source
- a substitute for a `Tier 1 internal dated capability record`

## Why `trace_space` Is A Top H2 Bucket

`trace_space` is one of the highest-risk fabrication-capability buckets in the current layer-count blog program because unsupported feature-size numbers recur across multiple drafts and are easy to overstate as transferable shop defaults.

Current demand-side evidence already shows repeated dependence on trace/space-style claims:

- `6-layer`: `3/3mil`
- `12-layer`: `3.5-4.0mil` trace width, `3.5mil/5mil`
- `14-layer`: `3/3mil`, `2.5/2.5mil`
- `20-layer`: `2.5/2.5mil`
- `24-layer`: current-draft risk still includes shop-specific geometry capability statements

This bucket also sits at the center of several claim classes that the repo must not collapse together:

- shop feature-size capability
- HDI vocabulary and build-up posture
- IC-substrate fine-line posture
- standards or design-threshold numerics
- SI geometry tables and impedance-derivation tables

Because those boundaries are central to H2 governance, `trace_space` is a top-priority control bucket.

## What This Bucket Includes

This bucket includes numeric claims that assert, imply, or strongly suggest what feature geometry a fabricator can currently produce as an operational capability.

In scope:

- minimum line / space capability claims
- standard versus advanced line/space ladders
- outer-layer versus inner-layer feature-size windows
- fine-line claims when they are being turned into transferable shop capability
- trace-width or spacing numbers presented as routine production defaults

Typical claim shapes:

- `3/3mil`
- `2.5/2.5mil`
- `standard line/space` versus `advanced line/space`
- `outer layer` versus `inner layer` feature windows
- trace-width minima presented as manufacturing capability rather than stackup-specific calculation output

## What This Bucket Excludes

This bucket does not govern:

- HDI architecture vocabulary by itself
- IC-substrate packaging posture by itself
- IPC or other standards thresholds
- width/spacing tables used to derive `50 ohm`, `90 ohm`, or `100 ohm` targets
- material-property numbers such as `Dk`, `Df`, `Tg`, `Td`, `CTE`, or peel strength
- board-level SI, channel, skew, or loss numerics
- layer-stack examples that are clearly recipe illustrations rather than capability records

Excluded examples:

- `1+N+1`, `any-layer`, `VIPPO`, `SAP`, `ABF/BT`
- class-linked geometry thresholds
- impedance geometry tables
- package-pitch or interface-speed context numbers

Those belong to other governance layers even when they appear next to feature-size wording.

## Current Corpus Support And Non-Claim Boundaries

The current corpus is already strong enough to support process posture, vocabulary separation, and non-claim boundaries around trace/space.

It is not strong enough to support reusable trace/space numbers.

### Process And Planning Support

[advanced-pcb-fabrication-and-stackup-planning.md](/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md) already supports these guarded statements:

- line/space belongs to advanced stackup and route-planning decisions
- HDI, high-layer, impedance, and IC-substrate fine-line language should be kept as separate decision frames
- exact line/space limits are refresh-sensitive internal claims

### Capability-Family Boundary Support

[apt-capability-family-map-and-boundaries.md](/code/blogs/llm_wiki/wiki/processes/apt-capability-family-map-and-boundaries.md) already supports these guarded statements:

- `HDI PCB` is the density-first capability family
- capability-family pages are routing maps, not manufacturing specifications
- table limits, trust-bar figures, and line/space-like claims on capability pages are refresh-sensitive internal claims

### HDI Posture Support

[hdi-microvia-and-vippo-process-posture.md](/code/blogs/llm_wiki/facts/methods/hdi-microvia-and-vippo-process-posture.md) already supports:

- HDI pages consistently frame microvia, any-layer build-up, and VIPPO as normal HDI posture
- exact microvia and geometry figures are refresh-sensitive internal claims

### IC-Substrate Boundary Support

[ic-substrate-fine-line-build-up-posture.md](/code/blogs/llm_wiki/facts/methods/ic-substrate-fine-line-build-up-posture.md) already supports:

- substrate fine-line SAP is a distinct packaging-substrate posture
- substrate line/space language is not transferable to general PCB capability
- exact substrate line/space values remain refresh-sensitive internal claims

## Current Blocker Statement

Current blocker for this bucket:

- there is no registered `Tier 1 internal dated capability record` yet for trace/space feature-size capability

Under [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md), that means:

- reusable trace/space numbers remain `needs_source`
- internal capability and process pages remain `downgrade` / posture-only support
- no trace/space capability fact card can exist yet
- no blog or evidence pack may reuse feature-size numbers as governed capability numerics

Current corpus posture is therefore:

- process vocabulary: supported
- HDI / build-up posture: supported
- IC-substrate boundary control: supported
- reusable feature-size numbers: blocked

## Claim-Splitting Rule For This Bucket

Every trace/space-related claim must be split into one of the following buckets before disposition.

### 1. Shop Feature-Size Capability

This is a fabrication capability claim.

Examples:

- `3/3mil`
- `2.5/2.5mil`
- `outer layer 3mil, inner layer 4mil`
- `standard` versus `advanced` line/space

Handling:

- H2 bucket item
- currently `needs_source`
- cannot be reused until a dated internal capability record exists

### 2. HDI Vocabulary Or Build-Up Posture

This is process framing, not feature-size proof.

Examples:

- any-layer HDI
- sequential build-up
- microvia, VIPPO, or SBU language
- dense-routing posture without transferable minimum geometry

Handling:

- may remain as `downgrade` or posture support
- must not be rewritten into exact line/space capability

### 3. IC-Substrate Fine-Line Posture

This is packaging-substrate framing, not general PCB capability proof.

Examples:

- SAP fine-line build-up
- ABF/BT substrate language
- stacked microvia substrate posture

Handling:

- may remain as `downgrade` or posture support
- must not be transferred into rigid multilayer or generic HDI capability facts

### 4. Standards Threshold Or Design-Rule Threshold

This is not an H2 capability numeric by default.

Examples:

- class-linked geometry thresholds
- acceptability-style annular-ring or breakout numbers
- design-rule cookbook thresholds presented as universal manufacturing limits

Handling:

- usually `delete`
- do not allow standards or design heuristics to piggyback into H2 capability facts

### 5. SI Geometry Table Or Impedance-Derivation Table

This is not trace/space capability proof even if it contains widths and spacings.

Examples:

- width/spacing tables for `50 ohm`, `90 ohm`, or `100 ohm`
- geometry numbers attached to skew, loss, or channel-performance interpretation

Handling:

- `downgrade` or `delete`, depending on wording
- do not convert geometry examples into shop feature-size capability

## Disposition Guidance For Common Claim Shapes

### `3/3mil` or `2.5/2.5mil` on an internal page

- disposition: `needs_source`
- reason: this is a shop capability promise without a dated capability record

### `fine-line HDI` with no number

- disposition: `downgrade`
- reason: HDI posture is supported, but numeric capability is not

### `SAP fine-line substrate`

- disposition: `downgrade`
- reason: substrate posture is supported, but it does not authorize transferable general-PCB trace/space numbers

### `50 ohm` or `100 ohm` geometry table

- disposition: `downgrade` or `delete`
- reason: this is usually stackup interpretation, not line/space capability evidence

### standards-style geometry threshold presented as shop capability

- disposition: `delete`
- reason: unsupported standards or design-rule threshold disguised as H2 capability

### trace-width example inside a stackup recipe

- disposition: `needs_source` if written as a reusable manufacturing rule
- disposition: `downgrade` if rewritten as a project-specific geometry example without capability promise

## Per-Blog Impact Summary

The immediate effect of this bucket decision is controlled reduction, not recovery.

- `6-layer`: `3/3mil` stays `needs_source`; retain only general manufacturability framing
- `8-layer`: line/space-adjacent DFM rules stay blocked unless backed by a dated capability record
- `12-layer`: trace-width and spacing tables stay blocked; keep only high-level stackup and verification framing
- `14-layer`: `3/3mil` and `2.5/2.5mil` stay `needs_source`; standards-linked geometry thresholds stay `delete`
- `16-layer`: fine-line and current-density geometry rules stay blocked as capability numerics
- `20-layer`: HDI / build-up vocabulary may remain, but feature-size tables stay blocked
- `24-layer`: advanced-routing and high-speed framing may remain, but exact shop geometry claims stay blocked

## Exact Next-Step Requirements Before Any Fact Card Could Exist

Before any trace/space capability fact card can exist, all of the following must be true:

1. A `Tier 1 internal dated capability record` is registered for trace/space feature-size capability.
2. The record clearly states scope: plant, line family, process family, board family, or release context.
3. The record separates general rigid multilayer, HDI build-up, and IC-substrate geometry instead of collapsing them into one number.
4. The record states whether the geometry applies to outer layer, inner layer, standard production, advanced process, or special-case builds.
5. The record is stable enough for refresh and expiry handling under H2 policy.
6. H0/H2 demand items are re-checked so blocked geometry tables are split from HDI vocabulary, standards thresholds, and SI geometry tables before promotion.

Stop/go rule for this bucket today:

- `stop` for numeric recovery
- `go` only for posture framing, non-claim boundaries, and source-routing work
