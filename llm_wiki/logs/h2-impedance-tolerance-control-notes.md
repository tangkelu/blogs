# H2 Impedance Tolerance Control Notes

Date: 2026-04-25

## Purpose

This note tells the main agent how to reflect the `impedance_tolerance` bucket kickoff in control docs without overstating recovery progress.

Current true posture:

- `H2` governance is landed
- `impedance_tolerance` is the first recovery bucket
- no reusable impedance-tolerance number has been recovered yet
- no capability fact card should be implied yet

## Backlog Wording

Use short wording that shows execution start, not numeric recovery.

Recommended wording:

- `H2 Capability Bucket Recovery`
  - `status: now`
  - `current bucket: impedance_tolerance`
  - `goal: establish dated-source intake and bucket-level recovery rules before any numeric fact-card promotion`

Do not word it as:

- `impedance tolerance coverage completed`
- `impedance tolerance fact cards added`
- `controlled impedance numerics recovered`

## Phase-Status Wording

Use wording that marks `impedance_tolerance` as the first active H2 recovery bucket while keeping output posture conservative.

Recommended wording:

- `H2 capability bucket recovery has started with impedance_tolerance as the first execution bucket after policy, inventory, and dated-source schema landing`
- `Current work is bucket intake and source-discipline setup, not reusable numeric recovery yet`
- `Verification posture may remain usable from existing method/wiki pages even if tolerance numerics remain blocked`

## Update-Log Entry Language

Keep the entry operational and non-celebratory.

Recommended entry:

- `Started H2 bucket-level execution with impedance_tolerance as the first governed recovery target, using the H2 capability-number policy, inventory, and dated capability-source schema as intake controls; no impedance-tolerance numbers or fact cards were promoted in this step`

Optional second sentence if needed:

- `This kickoff only opens bucket-scoped source review and downstream guardrails, not capability-table restoration`

## Guardrails: What Must Not Be Claimed Yet

- Do not claim that any `±X%` impedance value is now approved for reuse.
- Do not claim that existing internal impedance / TDR / coupon / validation pages prove a transferable tolerance promise.
- Do not claim that `impedance_tolerance` recovery is complete just because the bucket is first in sequence.
- Do not imply that verification-method coverage equals current production capability coverage.
- Do not imply that any future evidence pack may restore impedance-tolerance numerics before a dated capability record exists.
- Do not imply broader `Class B` readiness from this kickoff alone.

## Exact Next-Bucket Sequencing Recommendation

After `impedance_tolerance`, keep the next buckets in this order:

1. `trace_space`
2. `drill_and_via_geometry`
3. `aspect_ratio`
4. `backdrill_and_stub`

Reason for this order:

- `trace_space` and `drill_and_via_geometry` are the densest adjacent geometry buckets and commonly co-occur with impedance language in the layer-count blogs
- `aspect_ratio` depends on the same capability-discipline posture and should follow the core geometry buckets
- `backdrill_and_stub` should follow after the base geometry/tolerance buckets because it is more exposed to SI-threshold leakage and method/capability mixing

## Minimal Control-Doc Posture

If control docs need one-line shorthand, use:

- `H2 is now in first-bucket recovery with impedance_tolerance intake active; numeric promotion remains blocked pending dated capability-source records`
