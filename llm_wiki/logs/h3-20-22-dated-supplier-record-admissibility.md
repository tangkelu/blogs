# H3 20-Layer And 22-Layer Dated Supplier And Lot Record Admissibility

Date: 2026-04-26

## Purpose

This note defines the admissibility rules for any future supplier- or lot-scoped evidence considered for the two still-blocked `H3` branches.

It exists to:

- extend the general `H2` dated capability schema into an `H3` supplier/lot admissibility layer
- define the minimum fields required before a supplier or lot record may even enter review
- define hard rejection patterns
- define which record types are the best first targets if supplier evidence ever becomes available

This file is not:

- a supplier-evidence batch
- a readiness unlock
- a claim that admissible records already exist

## Relationship To Existing Governance

This note should be read together with:

- `logs/h2-dated-capability-source-schema.md`
- `logs/h3-20-22-supplier-evidence-governance.md`
- the branch-specific `20-layer` and `22-layer` boundary cards

Interpretation rule:

- `H2` governs reusable fabrication-capability numerics in general
- this note governs whether a future supplier/lot record is even admissible for `20-layer` or `22-layer`
- admissible does not mean reusable
- admissible only means the record is scoped well enough to evaluate under the supplier-evidence lane

## Shared Minimum Required Fields

No future `20-layer` or `22-layer` supplier/lot record is admissible unless all of the following are present:

### 1. Date

Required:

- explicit date or bounded time window

Reason:

- undated facts cannot distinguish current scoped truth from stale capability or old workflow history

### 2. Named Subject

Required:

- named supplier, organization, or site

Reason:

- company-level blur is not enough for blocked-branch evidence

### 3. Named Scope

Required:

- explicit statement of what kind of fact the record is

Examples:

- capability fact
- process-control fact
- qualification-package existence fact
- listing or certification fact
- first-article or lot workflow fact
- accepted-lot or release-event fact

Reason:

- mixed claim families are not admissible

### 4. Named Context

Required:

- at least one of the following:
  - site
  - line or build family
  - lot
  - build
  - program
  - customer scope

Reason:

- blocked-branch supplier evidence must be bounded tightly enough that it cannot drift into universal capability language

### 5. Supplier-Scoped Interpretation Statement

Required:

- an explicit statement that the record supports a supplier-scoped or lot-scoped fact only

Reason:

- the record must not masquerade as a public-general rule

### 6. Non-Override Statement

Required:

- an explicit statement that the record does not override current `H2` / `H3` governance on reusable numerics, standards thresholds, qualification logic, or commercial claims

Reason:

- admissibility is not an unlock by itself

### 7. Traceable Record Shape

Required:

- enough identity and control detail to review provenance later

Minimum acceptable examples:

- internal record id
- lot or build id
- certificate or listing id
- package or document id
- controlled attachment reference

Reason:

- the record must be reviewable after intake

## Additional Branch-Specific Requirements

## For 20-Layer

Any future admissible `20-layer` record should also identify which branch it belongs to:

- supplier-specific capability fact
- supplier-specific process-control fact
- supplier-specific qualification or reliability-package existence fact
- supplier-specific geometry or recipe fact
- supplier-specific operational or delivery fact

Additional rule:

- method identity, public process guides, and material-form pages are not substitutes for this record class

## For 22-Layer

Any future admissible `22-layer` record should also identify which branch it belongs to:

- supplier status, approval, listing, or certification fact
- build- or lot-specific workflow fact
- qualification-package or compliance-package existence fact
- accepted-lot or release-event fact
- program-specific readiness fact

Additional rule:

- certification, listing, qualification, approval, and release authority must remain separate claim families inside the record

## Hard Rejection Patterns

Reject the record immediately if any of the following is true:

### 1. No Date

Examples:

- marketing page
- generic capability page
- sales deck
- static prose with no capture time

### 2. No Named Site / Lot / Build / Program Context

Examples:

- `HILPCB supports 20-layer any-layer HDI`
- `HILPCB provides full traceability`

Reason:

- timeless supplier slogans are not admissible evidence

### 3. Mixed Claim Families In One Record

Examples:

- one record claims certification, qualification, release authority, and capability all at once
- one record blends method presence into accepted-result logic

Reason:

- this recreates exactly the collapse the governance layer was built to prevent

### 4. Public Vocabulary Rewritten As Supplier Proof

Examples:

- method names rewritten as qualification proof
- public process guides rewritten as HIL control numerics
- public listing ecosystems rewritten as HIL approval or release authority

### 5. Timeless Capability Recasting

Examples:

- dated event rewritten as permanent capability
- one accepted build rewritten as generic layer-count readiness

### 6. Attempted Threshold Recovery

Examples:

- supplier or lot record used to recover generic `Class 3 / 3A` thresholds
- supplier record used to genericize `IST`, coupon, `PLT`, outgassing, screening, or process-window numerics

### 7. Commercial Data Presented As Stable Evidence

Examples:

- yield
- lead time
- cost
- volume
- quick-turn windows

Reason:

- these may exist as dated operational facts, but they are not admissible as stable reusable evidence-pack numerics

## Best First Record Types If Supplier Evidence Ever Appears

### For 20-Layer

Priority order:

1. dated supplier-scoped capability fact records
2. dated process-control record-existence facts
3. dated qualification or reliability-package existence facts
4. dated operational or delivery facts

Reason:

- the narrowest current blocker is missing HIL-specific capability/proof support
- record-existence facts are safer than threshold-heavy internals

### For 22-Layer

Priority order:

1. dated supplier status / certification / listing facts with site and scope
2. dated build- or lot-specific workflow facts
3. dated qualification-package or compliance-package existence facts
4. dated accepted-lot or release-event facts

Reason:

- the narrowest current blocker is missing HIL-specific compliance / acceptance proof
- status and workflow facts are easier to keep narrow than threshold or release logic

## Intake Checklist

Before any future supplier or lot record enters the repo, confirm all answers are `yes`:

1. Is there an explicit date?
2. Is the supplier or site named?
3. Is the claim family singular and explicit?
4. Is there a named lot, build, program, line, or equivalent bounded context?
5. Can the record be interpreted only as supplier-scoped or lot-scoped?
6. Does the record avoid generic thresholds, generic capability tables, and generic acceptance logic?
7. Does the record avoid turning status, workflow, or one event into timeless readiness?
8. Is there enough record identity to review provenance later?

If any answer is `no`, reject the record.

## Downstream Usage Rule

Even if a record is admissible:

- it still enters the repo only as a governed supplier-evidence object
- it does not become a reusable evidence-pack numeric by default
- it must still respect the `never genericize` rules already fixed in `h3-20-22-supplier-evidence-governance.md`

## Tracking Interpretation

If a future admissible record is accepted, tracking must say:

- `supplier/lot record admissible and parked under governed supplier lane`

Tracking must not say:

- `numeric recovered`
- `branch unlocked`
- `ready for P4-06`

unless a later dedicated readiness note separately proves those outcomes.

## Completion Criteria

This admissibility note is complete when:

1. shared minimum fields are explicit
2. branch-specific record classes are explicit
3. hard rejection patterns are explicit
4. first-target record priorities are explicit
5. tracking language stays governance-only

## Minimal Control Posture

For `20-layer` and `22-layer`, admissibility is only the first gate.

It means:

- the record is bounded enough to review

It does not mean:

- the record is reusable
- the branch is unlocked
- generic numerics may return
