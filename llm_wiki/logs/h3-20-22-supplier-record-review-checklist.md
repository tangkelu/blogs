# H3 20-Layer And 22-Layer Supplier Record Review Checklist

Date: 2026-04-26

## Purpose

This checklist is the reviewer-side companion to `h3-20-22-supplier-record-intake-template.md`.

Use it when a filled supplier or lot record template is proposed for the blocked `20-layer` or `22-layer` branches.

## Review Steps

1. Confirm the intake is targeting exactly one branch: `20-layer` or `22-layer`.
2. Confirm every required field is filled.
3. Confirm the claim family is singular.
4. Confirm the record is supplier-scoped or lot-scoped, not public-general.
5. Confirm the record does not violate any hard-rejection rule.
6. Confirm the record does not conflict with the branch's `never genericize` classes.
7. Confirm the proposed downstream use is still governance-only.

## Accept / Reject Logic

Accept for governed review only if all are true:

- no hard rejection pattern is present
- bounded context is explicit
- warning text and forbidden uses are explicit
- the record can only support narrow supplier- or lot-scoped facts

Reject immediately if any are true:

- missing date
- missing named subject
- missing bounded context
- mixed claim families
- threshold recovery attempt
- timeless capability recast
- commercial fact presented as stable evidence

## Output Labels

Use one of:

- `reject_at_intake`
- `hold_for_governed_review`

Do not use:

- `ready_for_evidence_pack`
- `numeric_recovered`
- `branch_unlocked`
