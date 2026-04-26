# P4-13 Post-Split Reassessment And Next Sequence

Date: 2026-04-26

## Purpose

This control note records the first reassessment after the current `22-layer` and `20-layer` blocker-reduction batches have landed:

- `22-layer hi-rel acceptance-governance boundary batch`
- `20-layer interconnect-reliability and process-window boundary batch`
- `22-layer Class-3 / addendum threshold-boundary batch`
- `20-layer geometry-and-capability containment batch`

The purpose is not to reopen broad source hunting.

The purpose is:

- identify the highest-leverage unresolved blocker class on each branch
- fix the next priority order for long-task execution
- keep `P4-06` blocked until remaining blocker classes are narrowed again

## Current Post-Split Baseline

Current baseline remains unchanged:

- `20-layer`: `needs_sources`
- `22-layer`: `needs_sources`
- `P4-06`: blocked

What changed is not readiness.

What changed is retrieval safety:

- `22-layer` is now split across acceptance workflow, qualification/listing/release authority, and contract flowdown / lot conformance
- `22-layer` is now also split across Class-3/addendum hierarchy, clause-family visibility, and outgassing / screening acceptance
- `20-layer` is now split across interconnect-reliability workflow, process-window / recipe leakage, and method-versus-qualification
- `20-layer` is now also split across geometry / factory-capability leakage, build-up material pages versus feature-size authority, and any-layer vocabulary versus shop capability

That means the next step should be reassessment of the still-blocked drafts against the narrowed boundary stack, not generic expansion.

## 20-Layer Reassessment

### Highest-Leverage Remaining Blocker

`current blocked-draft dependence on unsupported geometry and shop-capability claims`

### Why This Is Now The Main Risk

The latest `20-layer` splits materially reduced:

- `IST` workflow leakage
- recipe/process-window leakage
- method-versus-qualification collapse
- geometry / factory-capability leakage through build-up language
- feature-size leakage through material pages
- shop-capability leakage through any-layer vocabulary

The largest unresolved risk is now the one still present in the blocked draft even after the containment stack narrowed:

- trace/space capability claims
- drill / via geometry claims
- stacked-via / any-layer geometry implications
- registration / feature-size / shop-strength claims
- build-up material pages being misread as proof of rigid-board capability

### Recommended Next 20-Layer Step

`20-layer blocked-blog reassessment against the narrowed boundary stack`

### Candidate Outputs

- reassess `logs/layer-count-blog-readiness.md`
- decide whether another `20-layer` blocker-reduction pass is needed before any `P4-06` bridge work

### Not Included

This batch should not attempt to recover:

- geometry tables
- trace/space numbers
- drill / laser-via minima
- aspect-ratio numbers
- lamination-count numbers
- shop capability numerics

## 22-Layer Reassessment

### Highest-Leverage Remaining Blocker

`current blocked-draft dependence on unsupported hi-rel thresholds and acceptance-proof language`

### Why This Is Now The Main Risk

The latest `22-layer` splits materially reduced:

- qualification/listing/release-authority collapse
- contract-flowdown / lot-conformance collapse
- supplier-status inference
- `Class 3 / 3A` threshold leakage
- addendum-triggered acceptance-table leakage
- outgassing / screening acceptance leakage

The largest unresolved risk is now the one still present in the blocked draft even after the threshold stack narrowed:

- `Class 3 / 3A` threshold inference
- addendum-triggered acceptance-table inference
- clause-family headings being rewritten as technical criteria
- outgassing and screening values being rewritten as universal acceptance proof

### Recommended Next 22-Layer Step

`22-layer blocked-blog reassessment against the narrowed boundary stack`

### Candidate Outputs

- reassess `logs/layer-count-blog-readiness.md`
- decide whether another `22-layer` blocker-reduction pass is needed before any `P4-06` bridge work

### Not Included

This batch should not attempt to recover:

- `Class 3 / 3A` thresholds
- addendum technical tables
- sample sizes or frequencies
- `PLT` sample plans
- outgassing acceptance numerics

## Current Priority Order

After reassessment, the long-task order should be:

1. reassess both blocked blogs against the narrowed boundary stack
2. keep `P4-06` blocked unless the reassessment verdict materially changes
3. only then decide whether another blocker-reduction pass is needed

## Stop Conditions

Do not treat either branch as unlocked if the batch only improves wording without changing the unsupported claim classes.

`P4-06` must stay blocked if any of the following remain true:

- `20-layer` or `22-layer` still show `needs_sources` in `layer-count-blog-readiness.md`
- public metadata or TOCs can still be reconstructed into threshold tables
- build-up / HDI vocabulary can still be reconstructed into geometry or shop-capability claims
- outgassing, screening, `PLT`, or lot-conformance wording can still be reconstructed into acceptance proof
- supplier/listing/audit ecosystem pages can still be reconstructed into approval or release-authority claims

## Current Decision

The next long-task execution step under `P4-13` should be:

- reassess `20-layer` and `22-layer` together before any `P4-06` bridge work

That reassessment is now complete through `logs/p4-13-blocked-draft-reassessment-and-next-pass.md`.

Current next pass after that reassessment:

- `20-layer` surviving geometry/capability and `HIL`-proof containment pass
- `22-layer` surviving threshold/acceptance and `HIL`-status containment pass

That next pass is now further narrowed by two draft-level control artifacts:

- `logs/p4-13-20-layer-draft-blocker-map.md`
- `logs/p4-13-22-layer-draft-blocker-map.md`

Those blocker maps now act as the bridge between the abstract boundary stack and the next draft-level containment execution.

So the immediate execution shape is:

- `logs/p4-13-20-layer-bridge-exclusion-and-downgrade-map.md` as the `20-layer` draft-level exclusion / downgrade control note
- `logs/p4-13-22-layer-bridge-exclusion-and-downgrade-map.md` as the `22-layer` draft-level exclusion / downgrade control note
- one next containment pass per draft executed inside those two control notes

Until that reassessment is complete and actually changes the blocked ceiling:

- `20-layer` remains `needs_sources`
- `22-layer` remains `needs_sources`
- `P4-06` remains blocked
