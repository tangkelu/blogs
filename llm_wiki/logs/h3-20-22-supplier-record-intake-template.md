# H3 20-Layer And 22-Layer Supplier Record Intake Template

Date: 2026-04-26

## Purpose

This file defines the blank intake template for any future supplier- or lot-scoped record proposed for the blocked `20-layer` and `22-layer` branches.

It exists to:

- standardize how a future supplier record is captured before review
- separate required fields from optional fields
- attach fixed warning language so intake cannot silently drift into readiness or generic-numeric promotion

This file is not:

- an admissibility decision
- a landed supplier-evidence record
- a readiness unlock

## Usage Rule

Use this template only after reading:

- `logs/h3-20-22-dated-supplier-record-admissibility.md`
- `logs/h3-20-22-supplier-evidence-governance.md`
- `logs/h2-dated-capability-source-schema.md`

If a proposed record cannot fill all required fields below, stop intake and reject it before review.

## Blank Intake Template

```yaml
record_id: ""
record_type: "supplier_or_lot_scoped_record"
target_branch: ""  # required: 20-layer | 22-layer
capture_date: ""   # required
record_status: "candidate"  # candidate | rejected | accepted_for_governed_review

source_owner: ""   # required
source_subject: "" # required: supplier / site / organization / lot owner
source_origin_class: "" # required

claim_family: ""   # required, singular only
claim_summary: ""  # required

site_scope: ""     # required unless truly unavailable; if unavailable, reject
line_or_build_scope: ""   # optional
lot_scope: ""      # optional
program_scope: ""  # optional
customer_scope: "" # optional

scope_statement: ""   # required
supplier_scoped_interpretation: ""  # required
non_override_statement: ""          # required

record_identity_reference: ""   # required: certificate id / lot id / package id / document id / controlled ref
linked_attachment_or_url: ""    # optional
validity_window: ""             # optional but strongly recommended
refresh_trigger: ""             # optional but strongly recommended

branch_specific_class: ""       # required
fact_shape_notes: ""            # optional
warning_flags: []               # optional
forbidden_uses: []              # required

reviewer_precheck:
  has_explicit_date: false
  has_named_subject: false
  has_singular_claim_family: false
  has_bounded_context: false
  has_supplier_scoped_interpretation: false
  has_non_override_statement: false
  has_traceable_identity_reference: false
  triggers_hard_rejection: false

preliminary_disposition: ""  # reject | hold_for_governed_review
notes: ""
```

## Required Fields

The following fields are mandatory for every intake:

- `record_id`
- `target_branch`
- `capture_date`
- `source_owner`
- `source_subject`
- `source_origin_class`
- `claim_family`
- `claim_summary`
- `site_scope`
- `scope_statement`
- `supplier_scoped_interpretation`
- `non_override_statement`
- `record_identity_reference`
- `branch_specific_class`
- `forbidden_uses`
- all `reviewer_precheck` booleans
- `preliminary_disposition`

If any required field is missing, the record must not enter governed review.

## Optional Fields

The following fields may be blank if truly unavailable:

- `line_or_build_scope`
- `lot_scope`
- `program_scope`
- `customer_scope`
- `linked_attachment_or_url`
- `validity_window`
- `refresh_trigger`
- `fact_shape_notes`
- `warning_flags`
- `notes`

Rule:

- optional does not mean low-value
- if the record involves lot, build, certification, qualification package, or release event, relevant optional fields should be filled whenever available

## Allowed Claim Families

Use one and only one `claim_family` value per intake.

### For 20-Layer

Allowed examples:

- `supplier_capability_fact`
- `supplier_process_control_fact`
- `supplier_qualification_package_existence`
- `supplier_geometry_or_recipe_fact`
- `supplier_operational_fact`

### For 22-Layer

Allowed examples:

- `supplier_status_or_listing_fact`
- `lot_or_build_workflow_fact`
- `qualification_or_compliance_package_existence`
- `accepted_lot_or_release_event_fact`
- `program_specific_readiness_fact`

If the proposer wants more than one claim family, split into multiple intake records.

## Fixed Warning Language

The following warning text should be copied verbatim into future intake workflows.

### Shared Warning

`This intake record is supplier-scoped or lot-scoped only. It does not authorize reusable public numerics, reusable standards thresholds, generic capability tables, generic acceptance logic, or readiness unlock by itself.`

### 20-Layer Warning

`For 20-layer, supplier records must not be rewritten into generic geometry tables, process-window numerics, qualification thresholds, stack-recipe defaults, or commercial capability promises.`

### 22-Layer Warning

`For 22-layer, supplier or lot records must not be rewritten into generic Class 3 / 3A thresholds, acceptance tables, PLT rules, release-authority logic, or timeless conformance claims.`

## Hard-Rejection Reminder Block

Include this checklist in every intake review:

- reject if there is no explicit date
- reject if there is no named site, lot, build, program, or equivalent bounded context
- reject if multiple claim families are collapsed into one record
- reject if public method, process-guide, listing, or workflow vocabulary is being rewritten as supplier proof
- reject if the record turns a dated event into timeless capability
- reject if the record attempts threshold recovery
- reject if operational or commercial facts are presented as stable reusable evidence

## Recommended Default Warning Flags

These flags are optional in the YAML, but recommended when relevant:

- `marketing_shape_risk`
- `timeless_capability_risk`
- `threshold_recovery_risk`
- `workflow_to_acceptance_risk`
- `commercial_fact_risk`
- `mixed_claim_family_risk`
- `site_scope_missing_risk`

## Intake Review Checklist

Before moving a filled template into governed review, confirm all items below:

1. The record uses exactly one claim family.
2. The record has an explicit capture date.
3. The record names a real supplier, site, or lot-bound subject.
4. The record includes a bounded context that prevents universalization.
5. The record includes both required warning statements and forbidden-use notes.
6. The record does not contradict `never genericize` rules already fixed for the branch.
7. The record is still being treated as governance-only, not as evidence-pack-ready support.

## Minimal Control Posture

This template is only a collection stub.

Filling it out does not mean:

- the record is admissible
- the record is accepted
- the branch is unlocked

It only means the proposer supplied enough structure for governed review to begin.
