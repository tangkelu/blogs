# H3 20-Layer And 22-Layer Supplier Record Decision Matrix

Date: 2026-04-26

## Purpose

This file converts the shared intake checklist into a branch-aware reviewer decision matrix for the blocked `20-layer` and `22-layer` supplier-evidence lane.

It exists to:

- make `reject_at_intake` versus `hold_for_governed_review` decisions more repeatable
- separate reviewable narrow fact shapes from hard-stop claim shapes
- keep future supplier-record handling aligned with the current `H3` governance boundary

This file is not:

- a supplier-evidence batch
- an admissibility pass for any real record
- a readiness unlock

## Relationship To Shared Assets

Use this note together with:

- `logs/h3-20-22-supplier-record-intake-template.md`
- `logs/h3-20-22-supplier-record-review-checklist.md`
- `logs/h3-20-22-dated-supplier-record-admissibility.md`
- `logs/h3-20-22-supplier-evidence-governance.md`
- `logs/h3-20-22-supplier-record-filled-examples.md`
- `logs/h3-20-22-supplier-evidence-execution-trigger.md`

Interpretation rule:

- the template defines fields
- the checklist defines minimum review steps
- this matrix defines the safest default disposition by claim shape

## Output Labels

Use only:

- `reject_at_intake`
- `hold_for_governed_review`

Do not use:

- `evidence_pack_ready`
- `numeric_recovered`
- `branch_unlocked`

## Shared Automatic Reject Rules

Immediately label `reject_at_intake` if any of the following is true:

1. no explicit date or bounded time window
2. no named supplier, site, lot, build, program, or equivalent bounded context
3. multiple claim families are collapsed into one record
4. public standards, method, workflow, or listing vocabulary is being rewritten as proof of supplier capability, accepted-lot status, conformance, or release authority
5. a dated event is being rewritten as timeless capability, acceptance, or conformance
6. the record is trying to recover generic thresholds, reusable numerics, or universal release logic
7. commercial, lead-time, yield, or scale facts are being presented as stable reusable evidence

## Shared Hold Logic

Label `hold_for_governed_review` only when all of the following are true:

1. the record stays inside one allowed claim family
2. bounded context is explicit
3. supplier-scoped interpretation is explicit
4. non-override statement is explicit
5. forbidden uses are explicit
6. the narrowest downstream use is still governance-only and supplier-scoped

## Decision Matrix

| Branch | Candidate shape | Default label | Why |
| --- | --- | --- | --- |
| `20-layer` | dated `supplier_process_control_fact` with named site and bounded workflow context, but no numeric extraction | `hold_for_governed_review` | This is the safest first-target shape for `20-layer` because it can remain supplier-scoped without recovering process windows, geometry, or qualification logic. |
| `20-layer` | dated `supplier_capability_fact` stating existence of one bounded supplier capability record, with no geometry, scale, or commercial promotion | `hold_for_governed_review` | This can remain narrow if it stays as existence-shaped supplier context rather than a reusable capability table. |
| `20-layer` | any process-control record rewritten into chemistry limits, registration thresholds, inspection intervals, or void-control numerics | `reject_at_intake` | This attempts threshold or numeric recovery from a supplier-scoped record. |
| `20-layer` | any capability record rewritten into feature-size tables, lamination-count defaults, yield, lead-time, or production-scale claims | `reject_at_intake` | These classes are explicitly parked or never genericize. |
| `20-layer` | any record that collapses method presence, qualification, and accepted reliability into one claim | `reject_at_intake` | This recreates the exact `method to qualification` collapse the branch boundary forbids. |
| `22-layer` | dated `lot_or_build_workflow_fact` with named site and bounded build or lot context, but no accepted-result implication | `hold_for_governed_review` | This is the safest first-target shape for `22-layer` because it can stay at workflow existence rather than acceptance authority. |
| `22-layer` | dated `supplier_status_or_listing_fact` with named source, explicit time window, and no timeless conformance rewrite | `hold_for_governed_review` | This can remain narrow if it stays as date-bound status context rather than approval or release proof. |
| `22-layer` | any workflow record rewritten into accepted-lot status, qualification success, release authority, or default contract compliance | `reject_at_intake` | This collapses workflow context into proof or authority. |
| `22-layer` | any listing or status record rewritten into `Class 3 / 3A` conformance, acceptance logic, or timeless supplier compliance | `reject_at_intake` | These are explicitly blocked proof classes and must not be genericized. |
| `22-layer` | any record attempting to recover `PLT` sample plans, lot-conformance numerics, or universal acceptance tables | `reject_at_intake` | This is threshold recovery from a supplier or lot record. |

## Branch-Specific Review Emphasis

### For 20-Layer

Reviewers should ask:

- Is this only an existence-shaped supplier process or capability fact?
- Is the record still free of geometry, process-window, qualification, and commercial numerics?
- Would the narrowest truthful downstream sentence still sound supplier-scoped and date-bound?

If any answer is `no`, reject at intake.

### For 22-Layer

Reviewers should ask:

- Is this only a workflow or status fact, not an accepted result?
- Is the record still free of `Class 3 / 3A`, `PLT`, release-authority, and timeless conformance logic?
- Would the narrowest truthful downstream sentence still sound date-bound and context-bound rather than universal?

If any answer is `no`, reject at intake.

## Narrowest Allowed Downstream Use

If a record is labeled `hold_for_governed_review`, the downstream use is still limited to:

- one narrow supplier-scoped factual statement
- one date-bound or lot-bound context
- one branch-specific claim family

It is not enough to support:

- evidence-pack-ready numeric reuse
- public threshold recovery
- generic capability tables
- generic acceptance logic

## Minimal Control Posture

This matrix improves intake consistency only.

It does not mean:

- a real supplier record exists
- any record has passed governed review
- either blocked branch is closer to numeric unlock
