# H2 Testing And Verification Capability Control Notes

Date: 2026-04-26

## Purpose

This note tells the main agent how to handle the `testing_and_verification_capability` bucket that already exists in `logs/h2-capability-number-inventory.md` but has not yet been promoted into a dedicated control layer.

The goal is to stop prompt-side drafting from mixing:

- verification presence
- numeric verification scope
- acceptance / quality proof

into one reusable claim cluster.

This note is governance only.

It is not:

- a fact card
- a source map
- permission to restore `20GHz`, `100% electrical testing`, coupon-count, or VNA-scope numerics

## Why This Bucket Needs Its Own Control Note

Current layer-count drafts repeatedly bundle test and verification language into one unstable numeric block:

- `6-layer` and `8-layer` use `100% electrical testing` or impedance / TDR banners as if they are transferable quality proof
- `12-layer` uses `20GHz` VNA, `>10Gbps`, and related verification numerics as if they prove current reusable capability
- `16-layer` and `18-layer` blur validation presence with numeric scope and service positioning
- `22-layer` risks pulling acceptance-style wording through verification language

Without an explicit control note, future evidence packs can accidentally treat:

- `verification posture`
- `measurement equipment presence`
- `acceptance coverage`

as interchangeable.

They are not.

## Current True Posture

What the current corpus supports:

- non-numeric validation-ladder posture
- the distinction between `e-test`, `TDR`, `coupon`, `VNA`, and broader verification stages
- the idea that higher-complexity boards often require more structured verification planning

What the current corpus does not yet support as reusable numerics:

- frequency ceilings such as `20GHz`
- exact coverage claims such as `100% electrical testing` when used as article-grade proof
- fixed coupon-count or TDR-structure numerics
- numeric guarantees tied to SI outcome, acceptance quality, or program readiness

## Bucket Split Rule

Every testing / verification claim must be split into one of the following subtypes before disposition.

### 1. Verification Presence

Examples:

- `TDR verification is part of controlled-impedance workflow`
- `VNA may be used for RF or high-speed validation`
- `coupon planning belongs in the validation ladder`

Handling:

- may remain as non-numeric posture

### 2. Verification Scope Numeric

Examples:

- `20GHz VNA`
- `6-8 TDR structures`
- `>10Gbps requires VNA`

Handling:

- `needs_source` if intended as a reusable capability numeric
- otherwise delete

### 3. Acceptance / Coverage Claim

Examples:

- `100% electrical testing`
- coverage-style quality banners
- wording that implies numerical verification scope proves acceptance status

Handling:

- do not import through this bucket unless a dedicated governed authority exists
- default to `needs_source` or `delete`

### 4. SI / Performance Outcome Claim

Examples:

- verification numerics used to imply return-loss, eye-opening, skew, or channel-margin proof

Handling:

- `delete`

## Allowed Prompt-Side Output

Safe output may say:

- controlled impedance should be treated as a plan-plus-verification workflow
- coupon and TDR correlation matter for high-speed multilayer work
- validation stages differ between ordinary electrical test, impedance verification, and broader SI / RF review

Safe output may not say:

- the shop guarantees a fixed frequency ceiling
- a fixed numeric test scope applies to all boards in a layer-count class
- `100%` testing or similar coverage language proves acceptance or qualification status
- verification equipment presence proves board-level performance or compliance

## Recommended Tracking-Doc Wording

Use wording that shows governance tightening, not numeric recovery.

Recommended wording:

- `H2 governance now also isolates testing_and_verification_capability so verification posture, numeric scope, and acceptance-style claims cannot be silently merged inside future evidence packs`

Do not word it as:

- `test capability numerics recovered`
- `VNA / TDR coverage approved`
- `quality-verification tables added`

## Immediate Consequence For P4-06

Until a dedicated source map and dated capability layer exist:

- `20GHz`, `>10Gbps`, coupon-count, and similar verification numerics remain out of usable evidence packs
- `100% electrical testing` remains out of usable evidence packs when framed as reusable proof
- only non-numeric validation posture may survive in second-wave bridge-prep and evidence-pack work

## Minimal One-Line Control Posture

- `testing_and_verification_capability` is now governed as a split bucket: verification posture may remain, but numeric scope, coverage, and acceptance-style claims stay blocked pending dedicated source control
