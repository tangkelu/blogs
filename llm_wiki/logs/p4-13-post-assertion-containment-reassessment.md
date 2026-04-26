# P4-13 Post-Assertion-Containment Reassessment

Date: 2026-04-26

## Purpose

This control note records the reassessment after the next two narrowed blocker-reduction passes have landed:

- `22-layer` supplier-status / compliance / acceptance-assertion containment
- `20-layer` HIL capability / process-control / lead-time containment

The goal is not to reopen broad source hunting.

The goal is:

- verify whether the remaining blocked drafts are now limited by even narrower claim families
- record whether the latest containment pass changed retrieval safety without changing readiness
- decide whether `P4-06` is still blocked after this additional assertion-control layer

## Current Verdict

The readiness verdict remains unchanged:

- `20-layer`: `needs_sources`
- `22-layer`: `needs_sources`
- `P4-06`: blocked

What changed is not readiness.

What changed is that the current blocker surface is now more explicitly split between:

- public-source boundary control
- HIL-specific unsupported marketing or assertion language

## 20-Layer Reassessment

### Draft-Level Result

`20-layer` remains blocked because the current draft still depends on unsupported:

- geometry and feature-size tables
- stack recipe and lamination-count claims
- `IST` threshold and qualification claims
- HIL-specific capability assertions
- HIL-specific process-control numerics
- HIL-specific production, yield, and lead-time claims

### Current Narrowest Blocker

The latest containment pass now makes it harder for prompt retrieval to confuse:

- public architecture vocabulary with HIL capability proof
- public process-sensitivity sources with HIL control numerics
- public workflow context with HIL production-readiness claims

The narrowest remaining blocker is still:

`HIL-specific unsupported numeric and promotional claim load inside the current 20-layer draft`

### Decision

Another blocker-reduction pass is not yet justified as a readiness unlock.

`20-layer` remains `needs_sources` until exact unsupported claim clusters are either:

- removed from future bridge targets, or
- replaced by separately governed dated supplier evidence

## 22-Layer Reassessment

### Draft-Level Result

`22-layer` remains blocked because the current draft still depends on unsupported:

- `Class 3 / 3A` threshold tables
- addendum-triggered acceptance claims
- HIL-specific supplier-status marketing
- HIL-specific compliance assertions
- HIL-specific qualification and acceptance assertions
- coupon / qualification / acceptance-plan numerics

### Current Narrowest Blocker

The latest containment pass now makes it harder for prompt retrieval to confuse:

- public governance ecosystems with supplier-status proof
- public framework metadata with compliance proof
- public workflow and lot-conformance vocabulary with accepted-status proof

The narrowest remaining blocker is still:

`HIL-specific unsupported supplier/compliance/acceptance claim load inside the current 22-layer draft`

### Decision

Another blocker-reduction pass is not yet justified as a readiness unlock.

`22-layer` remains `needs_sources` until exact unsupported assertion clusters are either:

- removed from future bridge targets, or
- replaced by separately governed supplier/lot evidence

## Cross-Branch Result

The latest assertion-containment pass improved retrieval safety again, but did not change the evidence ceiling.

That means:

- `20-layer` remains `needs_sources`
- `22-layer` remains `needs_sources`
- `P4-06` remains blocked

## Current Priority Order

After this reassessment, the next long-task order should be:

1. keep `20-layer` and `22-layer` blocked in `layer-count-blog-readiness.md`
2. use the expanded guardrail stack to prevent unsupported carryover into any future bridge drafting
3. only consider `P4-06` for other safer branches unless a separate supplier-evidence discipline is introduced

## Stop Conditions

Do not treat either branch as unlocked if the latest work only narrows unsupported HIL-specific assertions without replacing them with stronger evidence.

`P4-06` must stay blocked if any of the following remain true:

- `20-layer` or `22-layer` still show `needs_sources`
- HIL-specific capability, process-control, lead-time, supplier-status, compliance, or acceptance assertions remain unsupported
- public framework, workflow, or method vocabulary can still be rewritten into HIL-specific proof claims

## Current Decision

The next `P4-13` step is not a readiness unlock.

It is controlled persistence:

- keep the two blocked branches under containment
- continue building prompt-safe exclusion layers
- do not start `P4-06` for these two drafts
