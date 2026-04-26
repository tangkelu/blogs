# H2 Backdrill And Stub Bucket Decision

Date: 2026-04-25

## Purpose

This document records the bucket-level governance decision for `backdrill_and_stub` under `H2 Workstream 2: Fabrication Capability Numeric Layer`.

It converts current corpus findings into a controlled decision sheet before any backdrill- or stub-related numeric recovery starts.

This file is:

- a governance and dependency document
- a bucket-level handling decision
- a stop/go control for future recovery work

This file is not:

- a numeric fact card
- permission to reuse backdrill or residual-stub numbers
- a customer-facing claim source
- a substitute for a `Tier 1 internal dated capability record`

## Why `backdrill_and_stub` Is A Top H2 Bucket

`backdrill_and_stub` is a high-risk fabrication-capability bucket because the current corpus strongly supports the engineering posture for backdrill, but demand-side blog drafts repeatedly try to turn that posture into reusable numeric capability promises.

Current demand-side evidence already shows repeated dependence on backdrill- and stub-style claims:

- `8-layer`: backdrill frequency thresholds and DFM-rule numerics remain blocked
- `12-layer`: `±8mil` back-drill depth and nearby threshold logic remain blocked
- `18-layer`: backdrill rationale is supportable, but numeric process tables remain unsafe
- `24-layer`: current draft risk still includes backdrill accuracy, residual-stub, and measurement-guarantee overreach

This bucket also sits at the intersection of four claim classes that the repo must not blur together:

- backdrill capability numerics
- residual-stub targets
- depth / oversize / verification controls
- SI / RF / channel-performance numerics

Because that split is central to H2 governance, `backdrill_and_stub` must stay tightly controlled.

## What This Bucket Includes

This bucket includes numeric claims that assert, imply, or strongly suggest what a fabricator can currently control, verify, or promise around backdrill execution and remaining via-stub geometry.

In scope:

- backdrill depth-accuracy promises
- residual-stub targets presented as manufacturing outcomes
- drill oversize or compensation numbers when framed as backdrill capability
- target-layer verification or depth-control numbers when framed as a production promise
- trigger-style numerics that say when backdrill becomes required as a shop rule

Typical claim shapes:

- `±X mil` or `±Y um` backdrill depth accuracy
- `residual stub < X`
- `oversize by X`
- `verify to target layer within X`
- `backdrill required above X GHz` or `above Y Gbps`
- `standard` versus `tight` backdrill-control windows

## What This Bucket Excludes

This bucket does not govern:

- non-numeric backdrill posture by itself
- general drilling vocabulary by itself
- stackup or connector review workflow by itself
- SI, RF, resonance, return-loss, insertion-loss, eye-opening, or channel-budget numerics
- interface-speed or SerDes-rate numerics used as ecosystem context
- standards thresholds or acceptance criteria
- dynamic commercial promises attached to high-speed support

Excluded examples:

- `112G-ready` as ecosystem positioning
- `stub resonance above 3 GHz`
- return-loss or eye-diagram outcomes
- VNA / TDR frequency ceilings when presented as validation-package scope
- press-fit or connector system numbers that are not pure backdrill capability
- layer-count examples that are clearly architecture context rather than capability proof

Those belong to separate governance layers even when they appear next to backdrill language.

## Current Corpus Support Already Available

The current corpus is already strong enough to support backdrill posture, multilayer-planning framing, and non-claim boundaries.

It is not strong enough to support reusable backdrill or residual-stub numbers.

### Backdrill Posture Support

[backdrill-control-capability.md](/code/blogs/llm_wiki/facts/methods/backdrill-control-capability.md) already supports these guarded statements:

- internal non-blog pages consistently frame backdrill as a normal engineering control for high-speed, RF, and long-through-via structures
- internal drilling posture links controlled-depth backdrill to via-stub resonance control, target-layer verification, and transition cleanup
- backplane, high-speed, and Rogers-linked pages all reinforce that backdrill belongs to transition control rather than isolated mechanical drilling

Its non-claims already matter for this bucket:

- it does not prove every board should be backdrilled
- it does not prove every quoted build includes the same backdrill depth, tolerance, or verification scope
- it explicitly says exact residual-stub limits, oversize rules, and verification criteria need current engineering confirmation

### High-Layer Posture Support

[high-layer-count-backdrill-and-registration-posture.md](/code/blogs/llm_wiki/facts/methods/high-layer-count-backdrill-and-registration-posture.md) supports planning-side wording:

- internal high-layer sources repeatedly combine registration, sequential lamination, and backdrill stub mitigation
- backdrill is treated as part of dense multilayer control, not as an isolated add-on
- layer-count growth is framed as raising both alignment risk and via-stub sensitivity

Its non-claims already matter for this bucket:

- it does not claim all multilayer boards require backdrill
- it does not state universal tolerance or layer-count limits
- exact residual-stub limits and registration tolerances must refresh before publication

### RF / Transition-Control Support

[rf-drilling-and-transition-control.md](/code/blogs/llm_wiki/wiki/processes/rf-drilling-and-transition-control.md) supports these guarded statements:

- RF and high-speed failures are often transition problems, not just laminate-choice problems
- controlled-depth backdrill, launch review, via-stub management, and adjacent cavity features belong to one transition-control frame
- backdrill capability does not mean every RF or high-speed board should automatically be backdrilled

Its non-claims already matter for this bucket:

- exact residual-stub or depth-control targets must refresh before publishing
- exact oversize or verification rules must refresh before publishing
- hard customer-facing default-scope claims are blocked

### Advanced Process Framing

[advanced-pcb-fabrication-and-stackup-planning.md](/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md) already supports guarded process language:

- backdrill is one of several separate but connected advanced-PCB planning decisions
- backdrill becomes relevant when via stubs interact with signal speed and channel length
- exact backdrill and residual-stub limits must refresh before publication

### Official External Manufacturability Context

[high-layer-rigid-board-manufacturability-context.md](/code/blogs/llm_wiki/facts/methods/high-layer-rigid-board-manufacturability-context.md) supports guarded context that high-layer rigid boards become more process-sensitive and should not be framed as commodity fabrication.

Its non-claims already matter for this bucket:

- it does not provide backdrill depth windows
- it does not provide residual-stub limits
- it does not convert supplier process guides into transferable shop capability tables

## Current Blocker Statement

Current blocker for this bucket:

- there is no registered `Tier 1 internal dated capability record` yet for backdrill depth control, residual-stub windows, or related oversize / verification controls

Under [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md), that means:

- reusable backdrill and residual-stub numbers remain `needs_source`
- internal drilling, high-speed, multilayer, and backplane pages remain `downgrade` / posture-only support
- no `backdrill_and_stub` capability fact card can exist yet
- no blog or evidence pack may reuse backdrill-control numbers as governed capability numerics

Current corpus posture is therefore:

- backdrill posture: supported
- high-layer / transition-control framing: supported
- guarded manufacturability context: supported
- reusable backdrill and stub numbers: blocked

## Claim-Splitting Rule For This Bucket

Every backdrill-related claim must be split into one of the following buckets before disposition.

### 1. Backdrill Capability Promise

This is a fabrication capability claim.

Examples:

- `±8mil backdrill depth`
- `controlled-depth backdrill within X`
- `standard` versus `tight` backdrill window

Handling:

- H2 bucket item
- currently `needs_source`
- cannot be reused until a dated internal capability record exists

### 2. Residual Stub Target

This is a fabrication-outcome claim when presented as what the shop can routinely leave after backdrill.

Examples:

- `remaining stub below X`
- `residual barrel length under Y`
- `stub-free` or near-zero stub language when turned into a numeric promise

Handling:

- H2 bucket item
- currently `needs_source`
- must not be imported from SI tables or marketing prose

### 3. Depth / Oversize / Verification Control

This is still a fabrication capability claim when written as a reusable production control number.

Examples:

- oversize allowance
- target-layer hit window
- depth-control accuracy
- X-ray or target-layer verification thresholds
- fixed verification-scope promises tied to backdrill

Handling:

- H2 bucket item
- currently `needs_source`
- may not be recovered from internal process pages alone

### 4. SI / RF / Channel-Performance Number

This is not a fabrication capability claim even if it appears inside backdrill sections.

Examples:

- stub resonance thresholds
- insertion-loss improvement claims
- return-loss improvement claims
- eye-opening or channel-budget outcomes
- interface-speed thresholds used as if they prove a backdrill requirement

Handling:

- exclude from this bucket
- do not allow SI numerics to piggyback on backdrill-control language

## Bucket Guidance For Common Claim Shapes

### `controlled-depth backdrill` with no number

- disposition: `downgrade`
- reason: posture is supported; no numeric capability promise is required

### `±X mil backdrill depth` on an internal page

- disposition: `needs_source`
- reason: this is a capability promise without a dated capability record

### `residual stub < X` on a service or product page

- disposition: `needs_source`
- reason: this is a manufacturing-outcome promise without Tier 1 dated capability support

### `backdrill used to remove via stubs in high-speed backplanes`

- disposition: `downgrade`
- reason: posture and use-case framing are supported; no numeric capability claim is required

### `backdrill required above X GHz` or `above Y Gbps`

- disposition: `delete`
- reason: this merges shop capability with unsupported SI / performance threshold language

### `oversize by X` or `hit target layer within Y`

- disposition: `needs_source`
- reason: this is a machine-control or process-control promise, not just vocabulary

### `backdrill improves return loss / eye opening / 112G channel margin`

- disposition: `delete`
- reason: this is a performance-outcome claim, not an H2 capability numeric

### `backdrill with TDR / VNA / validation support`

- disposition: `downgrade`
- reason: validation posture may remain, but it must not be rewritten into a numeric capability guarantee

## Per-Blog Impact Summary

The immediate effect of this bucket decision is controlled reduction, not numeric recovery.

### `8-layer`

- backdrill-related DFM thresholds stay blocked
- safe output keeps general high-speed stackup and drilling-planning language only

### `12-layer`

- exact backdrill depth-control numbers stay `needs_source`
- SI-threshold logic tied to backdrill stays `delete`
- safe output keeps backdrill as a possible high-speed control, not a numeric promise

### `14-layer`

- transition-control and via-strategy wording may remain as posture
- any explicit backdrill-control numeric remains governed and blocked

### `18-layer`

- high-speed and hybrid-stackup rationale may keep backdrill posture
- any accuracy, residual-stub, or verification-scope number remains blocked

### `24-layer`

- current draft language around backdrill accuracy, residual-stub promises, and shop-specific measurement guarantees remains unsafe
- safe output keeps only guarded high-speed / multilayer transition-control wording

## Exact Next-Step Requirements Before Any Fact Card Could Exist

Before any `backdrill_and_stub` capability fact card can exist, all of the following must be true:

1. A `Tier 1 internal dated capability record` is registered for backdrill control.
2. The record clearly states scope: plant, line family, board family, or release context.
3. The record separates backdrill capability from SI outcome claims.
4. The record separates residual-stub targets from depth-control and oversize-control numbers.
5. The record states measurement or verification context clearly enough to avoid mixing target-layer control with marketing prose.
6. The record is stable enough for refresh and expiry handling under H2 policy.
7. H0/H2 demand items are re-checked so blocked claims are split into `backdrill capability`, `residual stub target`, `depth / oversize control`, or `SI / performance numeric` before promotion.

Stop/go rule for this bucket today:

- `stop` for numeric recovery
- `go` only for posture framing, non-claim boundaries, and source-routing work
