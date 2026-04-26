# H2 Testing And Verification Capability Bucket Decision

Date: 2026-04-26

## Purpose

This document records the bucket-level governance decision for `testing_and_verification_capability` under `H2 Workstream 2: Fabrication Capability Numeric Layer`.

It converts current corpus findings into a controlled decision sheet before any test- or verification-related numeric recovery starts.

This file is:

- a governance and dependency document
- a bucket-level handling decision
- a stop/go control for future recovery work

This file is not:

- a numeric fact card
- permission to reuse `20GHz`, coupon-count, or coverage numbers
- a customer-facing claim source
- a substitute for a `Tier 1 internal dated capability record`

## Why `testing_and_verification_capability` Needs Its Own Bucket

`testing_and_verification_capability` is a high-risk `B` bucket because the current corpus strongly supports layered validation posture, but demand-side blog drafts repeatedly try to turn that posture into reusable numeric scope or quality-proof claims.

Current demand-side evidence already shows repeated dependence on test and verification numbers:

- `6-layer`: `100% electrical testing` style closing banners remain blocked
- `8-layer`: testing / tolerance / plating sections mix verification language with unsupported numerics
- `12-layer`: `20GHz` VNA, `>10Gbps`, and validation-scope numerics remain blocked
- `16-layer`: service and quality banners reuse validation-like numbers as capability proof
- `18-layer` and `24-layer`: validation-presence language can be misread as frequency or measurement-package promises

This bucket also sits at the intersection of four claim types that the repo must not blur together:

- verification posture
- verification scope numerics
- coverage / acceptance numerics
- SI / RF / performance-outcome numerics

Because that split is central to H2 governance, this bucket must stay tightly controlled.

## What This Bucket Includes

This bucket includes numeric claims that assert, imply, or strongly suggest what a fabricator can currently measure, cover, verify, or promise as part of an electrical-test, impedance, SI, RF, or quality-verification offering.

In scope:

- TDR / coupon / VNA frequency or scope numerics when framed as service capability
- electrical-test coverage percentages when framed as quality proof
- numeric counts of coupons, structures, or verification stages when framed as routine offering
- threshold-style language such as `above X Gbps use Y validation`
- fixed verification-package numerics or lab-scope promises

Typical claim shapes:

- `20GHz VNA`
- `>10Gbps requires VNA`
- `100% electrical testing`
- `6-8 TDR structures`
- `coupon count of X`
- `verify to X`

## What This Bucket Excludes

This bucket does not govern:

- non-numeric validation posture by itself
- material-test methods inside supplier datasheets
- standards acceptance thresholds
- SI / RF outcome numerics such as insertion loss, eye opening, skew budgets, or return loss
- dynamic commercial promises attached to advanced validation

Excluded examples:

- `PCIe 5.0`, `DDR5`, `112G` used as ecosystem context
- `Dk / Df / Tg / Td` test methods published in a datasheet
- `Class 3` or qualification-acceptance language
- channel-performance numerics derived from validation presence

Those belong to separate governance layers even when they appear next to testing language.

## Current Corpus Support Already Available

The current corpus is already strong enough to support layered validation posture and non-claim boundaries.

It is not strong enough to support reusable verification scope or coverage numerics.

### Validation-Scope Segmentation Support

[advanced-validation-scope-segmentation.md](/code/blogs/llm_wiki/facts/methods/advanced-validation-scope-segmentation.md) already supports these guarded statements:

- baseline electrical integrity, impedance verification, destructive metrology, and deeper SI checks are separate validation layers
- advanced validation scope can expand by program need
- internal pages distinguish routine manufacturing checks from deeper SI / RF review

Its non-claims already matter for this bucket:

- it does not prove every order receives the full advanced validation stack
- it does not prove all test types are standard-scope
- it does not replace current fixture, lab, or program-specific planning

### Controlled-Impedance Verification Posture Support

[controlled-impedance-tdr-verification-posture.md](/code/blogs/llm_wiki/facts/methods/controlled-impedance-tdr-verification-posture.md) supports planning-side wording:

- controlled impedance is paired with TDR, coupon, or similar verification language
- verification posture is stronger than bare design-intent language
- measurement and validation should remain tied to actual stackup and production context

Its non-claims already matter for this bucket:

- it does not authorize a universal tolerance or coverage promise
- it does not prove identical TDR scope on every build
- exact scope and percentages remain refresh-sensitive

### Validation Ladder Support

[validation-ladder-from-e-test-to-si-verification.md](/code/blogs/llm_wiki/wiki/testing/validation-ladder-from-e-test-to-si-verification.md) supports these guarded statements:

- electrical test, impedance correlation, and deeper SI / RF verification are distinct layers
- TDR is not the same thing as full-path SI validation
- customer-facing scope and frequency claims require re-checking before publication

### High-Speed Interface Context Support

[high-speed-interface-system-context.md](/code/blogs/llm_wiki/facts/methods/high-speed-interface-system-context.md) supports guarded context that public `PCIe`, `DDR`, and `112G` sources can explain why stronger validation planning may matter.

Its non-claims already matter for this bucket:

- it does not prove that a given PCB shop supports a given validation package by default
- it does not provide board-level performance proof

## Current Blocker Statement

Current blocker for this bucket:

- there is no registered `Tier 1 internal dated capability record` yet for validation scope, equipment scope, coverage percentage, or routine-vs-optional test-package boundaries

Under [h2-capability-number-policy.md](/code/blogs/llm_wiki/logs/h2-capability-number-policy.md), that means:

- reusable testing and verification numerics remain `needs_source`
- internal quality, high-speed, and impedance pages remain `downgrade` / posture-only support
- no `testing_and_verification_capability` fact card can exist yet
- no blog or evidence pack may reuse validation-scope numerics as governed capability numerics

Current corpus posture is therefore:

- validation posture: supported
- layered verification framing: supported
- reusable scope / coverage / package numerics: blocked

## Claim-Splitting Rule For This Bucket

Every testing-related claim must be split into one of the following buckets before disposition.

### 1. Verification Presence

This is a posture claim.

Examples:

- `TDR verification is part of controlled-impedance workflow`
- `VNA may be used for higher-frequency validation`
- `coupon planning belongs in impedance verification`

Handling:

- not a numeric capability claim
- may remain as non-numeric posture

### 2. Verification Scope Numeric

This is a fabrication capability claim.

Examples:

- `20GHz VNA`
- `6-8 TDR structures`
- `>10Gbps requires VNA`

Handling:

- H2 bucket item
- currently `needs_source`
- cannot be reused until a dated internal capability record exists

### 3. Coverage / Acceptance Claim

This is a fabrication capability or assurance claim when written as a reusable production promise.

Examples:

- `100% electrical testing`
- fixed coverage percentages
- wording that implies numerical coverage proves accepted-status quality

Handling:

- H2 bucket item
- currently `needs_source` or `delete`
- must not be imported through posture pages alone

### 4. SI / RF / Performance-Outcome Number

This is not a testing-capability claim even if it appears near validation language.

Examples:

- return-loss or insertion-loss outcomes
- skew budgets
- eye-opening or channel-margin numbers

Handling:

- exclude from this bucket
- do not allow performance numerics to piggyback on validation language

## Bucket Guidance For Common Claim Shapes

### `TDR / coupon verification` with no number

- disposition: `downgrade`
- reason: posture is supported; no numeric capability promise is required

### `20GHz VNA` on an internal page

- disposition: `needs_source`
- reason: this is a capability-scope promise without a dated capability record

### `100% electrical testing`

- disposition: `needs_source` or `delete`
- reason: this is a coverage / assurance claim without governed current-scope authority

### `>10Gbps requires VNA`

- disposition: `delete`
- reason: this mixes system-threshold logic with validation-scope capability and is unsafe as a reusable rule

## Recovery Gate

Before any `testing_and_verification_capability` fact card can exist, all of the following must be true:

1. A `Tier 1 internal dated capability record` is registered for validation scope.
2. The record separates baseline electrical test from impedance verification and from deeper SI / RF lab work.
3. The record separates capability presence from coverage or acceptance proof.
4. The record states refresh date and scope boundaries.
5. H0/H2 demand items are re-checked so blocked claims are split into `verification presence`, `scope numeric`, `coverage claim`, or `performance numeric` before promotion.
