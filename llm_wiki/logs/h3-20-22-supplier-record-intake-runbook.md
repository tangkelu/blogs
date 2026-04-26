# H3 20-Layer And 22-Layer Supplier Record Intake Runbook

Date: 2026-04-26

## Purpose

This runbook defines the controller-owned intake order for any future real dated-record path proposed for the blocked `20-layer` and `22-layer` supplier lane.

It exists to:

- force one ordered intake sequence before any branch-specific handling
- keep template capture, precheck, branch split, and label selection consistent
- preserve governance posture while future supplier-scoped records are screened

This runbook is not:

- supplier evidence landed
- an admissibility pass
- a numeric unlock
- permission to start generic recovery from supplier-scoped or lot-scoped material

## Relationship To Existing Assets

Use this runbook together with:

- `logs/h3-20-22-supplier-evidence-execution-trigger.md`
- `logs/h3-20-22-supplier-record-intake-template.md`
- `logs/h3-20-22-supplier-record-review-checklist.md`
- `logs/h3-20-22-supplier-record-decision-matrix.md`
- `logs/h3-20-layer-supplier-first-target-intake-pack.md`
- `logs/h3-22-layer-supplier-first-target-intake-pack.md`

Interpretation rule:

- the execution-trigger note decides whether intake may start at all
- the intake template defines what the proposer must fill
- the review checklist defines the shared reviewer precheck and minimum completeness test
- the decision matrix defines the shared disposition rule for `reject_at_intake` versus `hold_for_governed_review`
- the branch-specific intake pack is consulted only after the shared precheck confirms the candidate is still reviewable for that branch

## Roles

- `proposer` identifies the future real dated-record path and fills the intake template
- `controller` confirms trigger eligibility, enforces ordered execution, and preserves governance-only posture
- `reviewer` runs the shared precheck, applies the checklist, checks the branch-specific pack when required, and assigns the allowed output label

Rule:

- if proposer, controller, and reviewer are the same person in a small workflow, the role boundaries still apply in sequence

## Ordered Execution Flow

### 1. Trigger Check

Before any template is filled, the controller must read `h3-20-22-supplier-evidence-execution-trigger.md` and confirm that a real dated-record path actually exists.

The trigger is open only if all of the following are true:

1. there is a non-example candidate record
2. the record has an explicit date or bounded time window
3. the record names a real supplier, site, build, lot, program, or equivalent bounded context
4. the record can be captured in the shared template without inventing fields
5. the proposed fact shape stays inside one allowed claim family

If any trigger condition fails, stop immediately. Do not fill the template, do not open branch review, and record readiness as unchanged.

### 2. Template Ownership And Capture

If the trigger check passes, the `proposer` fills `h3-20-22-supplier-record-intake-template.md`.

The proposer is responsible for:

- filling every required field
- choosing exactly one `target_branch`
- choosing exactly one `claim_family`
- writing the supplier-scoped interpretation
- writing the non-override statement
- listing explicit forbidden uses
- filling all proposer-owned required fields in the template
- leaving `reviewer_precheck` for reviewer completion during shared precheck

The filled template is still only an intake stub. It is not evidence landed, not admissibility passed, and not a numeric unlock.

### 3. Shared Precheck

After the template is filled, the `reviewer` runs the shared precheck by using the template fields and `h3-20-22-supplier-record-review-checklist.md`.

The precheck must confirm at minimum:

1. one branch only: `20-layer` or `22-layer`
2. every required field is filled
3. the claim family is singular
4. the record is supplier-scoped or lot-scoped rather than public-general
5. no hard-rejection pattern is already present
6. downstream use is still governance-only

The reviewer should explicitly validate the template booleans for:

- `has_explicit_date`
- `has_named_subject`
- `has_singular_claim_family`
- `has_bounded_context`
- `has_supplier_scoped_interpretation`
- `has_non_override_statement`
- `has_traceable_identity_reference`
- `triggers_hard_rejection`

If the shared precheck fails, assign `reject_at_intake` without moving to branch-specific review.

### 4. Shared Reject / Hold Gate

If the template survives shared precheck, the reviewer applies the shared decision logic in `h3-20-22-supplier-record-decision-matrix.md`.

Immediately assign `reject_at_intake` if any shared automatic reject rule appears, including:

- no explicit date or bounded time window
- no named supplier, site, lot, build, or equivalent bounded context
- multiple claim families collapsed into one record
- public standards, workflow, or listing vocabulary rewritten as supplier proof
- dated event rewritten as timeless capability, acceptance, or conformance
- generic thresholds, reusable numerics, or universal release logic being recovered
- commercial, lead-time, yield, or scale facts presented as stable reusable evidence

Move forward only if the record still qualifies for `hold_for_governed_review` under the shared matrix.

## Branch Split Point

The branch split point happens only after the shared trigger check and shared precheck both pass.

### When To Look At Branch-Specific Pack

Open the branch-specific pack only after:

1. the trigger check is satisfied
2. the template is fully filled
3. the shared precheck is complete
4. the record has not already been rejected under shared automatic reject rules

At that point:

- use `h3-20-layer-supplier-first-target-intake-pack.md` for `20-layer`
- use `h3-22-layer-supplier-first-target-intake-pack.md` for `22-layer`

### How To Use Branch-Specific Pack

For `20-layer`, confirm the candidate still behaves like the safest first-target classes:

- `supplier_process_control_fact`
- `supplier_capability_fact`

Reject if the candidate drifts into:

- geometry tables
- process-window numerics
- qualification thresholds
- timeless HIL capability language
- commercial or scale claims

For `22-layer`, confirm the candidate still behaves like the safest first-target classes:

- `lot_or_build_workflow_fact`
- `supplier_status_or_listing_fact`

Reject if the candidate drifts into:

- accepted-lot status
- `Class 3 / 3A` conformance
- `PLT` or acceptance numerics
- release-authority logic
- timeless supplier compliance language

### When To Use Decision Matrix

Use the shared decision matrix twice:

1. immediately after the shared precheck, to determine whether the candidate is already a shared reject
2. after consulting the branch-specific pack, to confirm the final label remains `reject_at_intake` or `hold_for_governed_review`

The branch-specific pack narrows interpretation. The decision matrix still controls the label vocabulary.

## Allowed Output Labels

Use only:

- `reject_at_intake`
- `hold_for_governed_review`

Assign `reject_at_intake` when:

- trigger conditions fail
- required template fields are missing
- reviewer precheck fails
- shared automatic reject rules fire
- branch-specific pack shows the fact shape has drifted into blocked classes

Assign `hold_for_governed_review` only when:

- the trigger check passed
- the template is complete
- the shared precheck passed
- the candidate stayed inside one allowed claim family
- the branch-specific pack confirms the narrow fact shape is still safe
- downstream use remains governance-only and supplier-scoped

Do not assign:

- `supplier evidence landed`
- `admissibility passed`
- `numeric unlocked`
- `evidence_pack_ready`
- `branch_unlocked`

## Tracking Language

If intake does not start because the trigger check failed, record:

- `governance workflow improved`
- `supplier evidence still absent`
- `public reusable numeric readiness unchanged`

If intake starts but the record is rejected at intake, record:

- `supplier record screened at intake`
- `reject_at_intake applied`
- `public reusable numeric readiness unchanged`

If intake starts and the record is held for governed review, record:

- `supplier record captured for governed review`
- `hold_for_governed_review applied`
- `readiness unchanged`
- `public reusable numeric readiness unchanged`

Use `readiness unchanged` whenever the workflow result is only governance progression, intake progression, or narrow supplier-record handling without a separate later proof of admissibility and unlock.

## Stop Conditions

Stop the runbook immediately if any of the following becomes true:

- the candidate turns out to be an example, blank template, marketing page, or public-general page
- no real dated-record path exists after trigger review
- the template cannot be completed without inventing fields
- more than one claim family is required
- the reviewer precheck exposes a hard rejection pattern
- the branch-specific pack shows the record would recover blocked numerics, thresholds, acceptance logic, or timeless capability/conformance
- someone tries to treat intake completion as supplier evidence landed, admissibility passed, or numeric unlock

Once stopped, the output remains `reject_at_intake` or no intake opened. In both cases, readiness remains unchanged.

## Minimal Control Posture

The default posture for both supplier lanes remains parked.

This runbook only defines the order to follow if a future real dated-record path actually appears:

1. run trigger check
2. have the proposer fill the template
3. run shared precheck and checklist
4. apply shared decision matrix
5. consult the branch-specific pack at the branch split point
6. assign only `reject_at_intake` or `hold_for_governed_review`
7. record `readiness unchanged` unless a separate later governance note proves something stronger

Nothing in this runbook by itself means:

- supplier evidence landed
- admissibility passed
- numeric unlock occurred
