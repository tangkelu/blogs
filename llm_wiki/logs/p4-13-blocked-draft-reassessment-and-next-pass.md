# P4-13 Blocked-Draft Reassessment And Next Pass

Date: 2026-04-26

## Purpose

This control note records the next `P4-13` reassessment after `NQ-4` closeout.

The reassessment was run directly against the current blocked English drafts:

- `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en/20-layer-pcb-manufacturing.md`
- `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en/22-layer-pcb-manufacturing.md`

The purpose is not to reopen source hunting or to promote either draft into `ready`.

The purpose is:

- test whether the current boundary stack is now strong enough for a readiness-note-only update
- identify the highest-leverage unsupported claim clusters still active inside the blocked drafts
- fix the next blocker-reduction pass if structural blockers still remain

## Current Reassessment Verdict

Current verdict remains unchanged:

- `20-layer`: `needs_sources`
- `22-layer`: `needs_sources`
- `P4-06`: blocked

The current boundary stack is stronger than before, but the blocked ceiling did not move.

Reason:

- the unsupported claim classes are still active inside the draft bodies themselves
- the problem is no longer broad corpus weakness alone
- the problem is draft-structural overclaim density that still reconstructs unsupported numerics, qualification logic, and supplier-proof language

## New Control Outputs From This Reassessment

This reassessment now also yields two draft-level control artifacts:

- `logs/p4-13-20-layer-draft-blocker-map.md`
- `logs/p4-13-22-layer-draft-blocker-map.md`

These blocker maps should now be treated as first-class `P4-13` control inputs.

They move the next pass from abstract blocker classes toward draft-area-specific deletion, downgrade, and supplier-evidence hold control.

The immediate execution outputs for that next pass are now:

- `logs/p4-13-20-layer-bridge-exclusion-and-downgrade-map.md`
- `logs/p4-13-22-layer-bridge-exclusion-and-downgrade-map.md`

## 20-Layer Draft Reassessment

### Surviving Blocker Cluster 1

`geometry and architecture-to-capability collapse`

Current draft still rewrites:

- `any-layer`
- `ELIC`
- stacked microvias
- hybrid `5+10+5`
- sequential build-up language

into unsupported:

- build rules
- lamination-count expectations
- stack-height limits
- via diameters
- capture-pad tables
- registration budgets
- impedance geometries
- `2.5/2.5 mil`-style capability claims

### Surviving Blocker Cluster 2

`HIL-specific capability and commercial proof`

Current draft still asserts:

- specific stacked-span capability
- specific feature-size capability
- `200+ / 300+` reliability performance
- NPI-to-volume production strength
- commercial lead-time and production-discipline proof

These remain unsupported as reusable public supplier evidence in the current repo.

### Surviving Blocker Cluster 3

`reliability, qualification, and process-control pseudo-proof`

Current draft still converts public method and workflow vocabulary into unsupported:

- `IPC requirements`
- `IST` thresholds
- thermal-shock claims
- coupon or sample-plan rules
- copper-fill specifications
- bath-control intervals
- registration-control numerics
- process trigger thresholds

### 20-Layer Reassessment Result

This is still a blocker-reduction problem, not a readiness-note-only problem.

Immediate next `20-layer` control step:

- use `logs/p4-13-20-layer-draft-blocker-map.md` as the governing surface for the current blocked draft
- use `logs/p4-13-20-layer-bridge-exclusion-and-downgrade-map.md` as the draft-level exclusion / downgrade control note
- run the next containment pass only against those governed draft areas

Recommended later `20-layer` pass after that control note lands:

- one more blocker-reduction pass focused on surviving `geometry/capability`
- one more blocker-reduction pass focused on `HIL-specific proof`
- one more blocker-reduction pass focused on `reliability/process numeric leakage`

## 22-Layer Draft Reassessment

### Surviving Blocker Cluster 1

`Class 3 / 3A / addendum threshold reconstruction`

Current draft still exposes reusable acceptance numerics and derived criteria such as:

- `Class 2` versus `Class 3` tables
- `Class 3A` thermal, outgassing, and ionic thresholds
- annular-ring and registration math
- per-test acceptance tables
- plating minima and achievable geometry claims

### Surviving Blocker Cluster 2

`qualification / workflow / lot-evidence language collapsing into acceptance proof`

Current draft still turns:

- coupons
- `FAI`
- `IST`
- traceability
- project-specific testing
- lot-level workflow language

into proof-style claims that boards are verified, baselined, releasable, or already accepted.

### Surviving Blocker Cluster 3

`HIL-specific supplier-status, compliance, and customer-proof marketing`

Current draft still asserts:

- customer dependence
- `Class 3 / 3A` fabrication capability
- `AS9102` documentation strength
- `MIL-PRF` compliance posture
- first-submission qualification success
- retained traceability as proof of accepted quality-system status

These remain unsupported as current supplier-status or acceptance-proof claims in the public repo layer.

### 22-Layer Reassessment Result

This is still a blocker-reduction problem, not a readiness-note-only problem.

Immediate next `22-layer` control step:

- use `logs/p4-13-22-layer-draft-blocker-map.md` as the governing surface for the current blocked draft
- use `logs/p4-13-22-layer-bridge-exclusion-and-downgrade-map.md` as the draft-level exclusion / downgrade control note
- run the next containment pass only against those governed draft areas

Recommended later `22-layer` pass after that control note lands:

- one more blocker-reduction pass focused on `threshold tables`
- one more blocker-reduction pass focused on `workflow-to-acceptance` collapse
- one more blocker-reduction pass focused on `HIL-specific compliance/status assertions`

## New Priority Order

The next `P4-13` long-task sequence should now be:

1. promote the two draft blocker maps into first-class control inputs
2. use `logs/p4-13-20-layer-bridge-exclusion-and-downgrade-map.md` as the `20-layer` draft-level control note
3. use `logs/p4-13-22-layer-bridge-exclusion-and-downgrade-map.md` as the `22-layer` draft-level control note
4. run the next containment pass only inside those governed draft-control surfaces
5. reassess both blocked drafts again only after that draft-level control pass lands

## What This Reassessment Does Not Change

This reassessment does not change:

- `20-layer` blocked status
- `22-layer` blocked status
- `P4-06` blocked status
- the current `18-layer` / `24-layer` conservative-rewrite posture

It only changes the next execution shape.

## Recommended Tracking Wording

Recommended wording:

- `Post-NQ-4 P4-13 reassessment confirms that 20-layer and 22-layer still fail because unsupported claim clusters remain active inside the current drafts, not only in the abstract source map`
- `The reassessment now outputs draft-level blocker maps for both blocked branches, so the next pass should be draft-level exclusion/downgrade control rather than another abstract reassessment`
- `20-layer next pass should use the blocker map to govern geometry/capability collapse, HIL-specific proof, and reliability/process numeric leakage at draft-section level`
- `22-layer next pass should use the blocker map to govern threshold tables, workflow-to-acceptance collapse, and HIL-specific compliance/status assertions at draft-section level`
- `P4-06 remains blocked until those surviving draft-structural blocker classes are narrowed again`

## Minimal One-Line Control Posture

- `20-layer` and `22-layer` remain `needs_sources` after direct blocked-draft reassessment, so the next `P4-13` step is draft-level exclusion/downgrade control from the new blocker maps rather than a readiness-note-only update
