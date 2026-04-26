# H3 20-Layer Supplier First-Target Intake Pack

Date: 2026-04-26

## Purpose

This note converts the shared `H3` supplier-lane assets into a branch-specific first-target intake pack for `20-layer`.

It exists to:

- define the safest first-target intake shapes for future `20-layer` supplier-lane handling
- narrow first capture to `supplier_process_control_fact` and secondary `supplier_capability_fact`
- keep future intake bounded to supplier-scoped governance facts rather than reusable public numerics

This file is not:

- supplier evidence landed
- an admissibility pass
- a numeric unlock
- permission to genericize geometry, process-window, qualification, or commercial numerics

## Relationship To Shared Assets

This note should be read together with:

- `logs/h3-20-22-supplier-evidence-governance.md`
- `logs/h3-20-22-dated-supplier-record-admissibility.md`
- `logs/h3-20-22-supplier-record-intake-template.md`
- `logs/h3-20-22-supplier-record-filled-examples.md`
- `logs/h3-20-22-supplier-evidence-execution-trigger.md`
- `facts/methods/20-layer-hil-capability-claim-boundary.md`
- `facts/methods/20-layer-hil-process-control-numeric-boundary.md`

Interpretation rule:

- the shared governance files define whether the supplier lane may start at all
- this note defines the narrowest `20-layer` first-target capture posture once that lane is relevant
- the `20-layer` boundary cards remain controlling on what cannot be promoted into HIL capability proof or HIL control numerics

## First-Target Priority

Priority order for `20-layer` first-target intake:

1. `supplier_process_control_fact`
2. `supplier_capability_fact`
3. only later, if ever needed, `supplier_qualification_package_existence`
4. only later, if ever needed, `supplier_geometry_or_recipe_fact`
5. only later, if ever needed, `supplier_operational_fact`

Reason for this order:

- `supplier_process_control_fact` is the safest opening shape because it can capture dated record existence and bounded workflow posture without recovering chemistry, registration, fill-quality, inspection-frequency, or other control numerics
- `supplier_capability_fact` is the next safest shape because it can capture a dated supplier-scoped capability statement without turning architecture vocabulary, any-layer language, or method vocabulary into timeless HIL proof
- qualification, geometry, recipe, and operational/commercial shapes sit closer to blocked numeric recovery and should not be first-entry defaults

## Intake Field Emphasis

For `20-layer`, the shared intake template should be filled with extra emphasis on the following fields.

### 1. Claim Family Discipline

Use exactly one `claim_family`.

Preferred first-target values:

- `supplier_process_control_fact`
- `supplier_capability_fact`

Do not collapse these into:

- qualification-package existence
- geometry or recipe fact
- operational or commercial fact

### 2. Bounded Site And Workflow Context

Require:

- named supplier or site
- bounded workflow, build-family, or line context
- explicit date or bounded time window

For `20-layer`, company-wide slogans are not enough. The intake must prevent drift into timeless `HILPCB can build` language.

### 3. Scope Statement

The `scope_statement` should describe only the narrowest dated fact being captured.

For `supplier_process_control_fact`, the safest shape is:

- one dated statement that a named supplier site maintained a process-control record, control document, or bounded control workflow for one `20-layer` fabrication context

For `supplier_capability_fact`, the safest shape is:

- one dated statement that a named supplier site represented one bounded `20-layer` capability posture in one specific context

The scope statement must not include:

- geometry tables
- process-window numerics
- qualification thresholds
- production-scale or lead-time promises

### 4. Supplier-Scoped Interpretation

The `supplier_scoped_interpretation` should state that any later supported fact remains:

- dated
- supplier-scoped
- site- or workflow-bounded
- non-transferable to generic `20-layer` truth

This is required because the `20-layer` capability boundary does not allow public architecture, method, or material-form vocabulary to become HIL-specific capability proof.

### 5. Non-Override Statement

The `non_override_statement` should explicitly say that the intake does not authorize:

- reusable public numerics
- generic geometry freedom claims
- generic process-control numerics
- qualification or accepted-reliability proof
- commercial capability promises

This is required because the `20-layer` process-control boundary does not allow public process-sensitivity or method-governance vocabulary to become HIL control-plan numerics.

### 6. Forbidden-Use Notes

Every `20-layer` first-target intake should include branch-specific forbidden uses such as:

- do not rewrite into generic `20-layer` geometry tables
- do not recover chemistry-control, registration-control, fill-quality, bath-control, or inspection-frequency numerics
- do not convert method or workflow presence into qualification proof
- do not convert one supplier-scoped capability statement into timeless HIL manufacturing capability
- do not convert supplier-scoped records into lead-time, yield, cost, or scale claims

## Fast Reject Patterns

Reject intake immediately if any of the following appears:

### 1. Numeric Recovery Pressure

Examples:

- via, pad, trace/space, aspect-ratio, lamination-count, or impedance numbers
- bath concentration, interval, inspection cadence, void-rate, registration, or control-limit numbers
- coupon, `IST`, thermal-cycle, or reliability threshold numbers

Rule:

- geometry, process-window, qualification, and commercial numerics remain blocked and must not be genericized

### 2. Method Or Architecture Vocabulary Recast As Proof

Examples:

- `any-layer`, `ELIC`, stacked microvia, or build-up wording rewritten as supplier capability proof
- public method names or process guides rewritten as HIL control-plan proof

Rule:

- architecture and method vocabulary may describe context, not supplier proof strength

### 3. Mixed Claim Families

Examples:

- one intake claims capability plus process control plus qualification plus commercial readiness
- one intake turns a process-control record into accepted reliability or released production evidence

Rule:

- split records; otherwise reject at intake

### 4. Timeless Capability Recasting

Examples:

- one dated supplier statement rewritten as general `20-layer` manufacturability
- one site-scoped process record rewritten as universal HIL control discipline

### 5. Commercial Or Production Inflation

Examples:

- lead time
- yield
- cost
- quick-turn windows
- scale or capacity promises

Rule:

- these are not safe first-target intake shapes for `20-layer`

## Narrowest Allowed Downstream Use

If a real dated-record path appears later, and only if the shared trigger and admissibility controls are satisfied, the narrowest allowed downstream use is:

- a dated supplier-scoped statement that one named site had one bounded process-control record or process-control workflow for one `20-layer` context
- or a dated supplier-scoped statement that one named site represented one bounded `20-layer` capability fact in one explicit context

That downstream use still does not allow:

- supplier evidence landed
- admissibility passed
- numeric unlock
- reusable geometry, process-window, qualification, or commercial numerics
- timeless HIL capability wording

## Example Interpretation

Safe interpretation example for `supplier_process_control_fact`:

- `A dated supplier-scoped record may support the narrow statement that one named site maintained one process-control document for one bounded 20-layer fabrication workflow.`

Unsafe interpretation:

- `HILPCB controls 20-layer process windows to production-ready numeric limits.`

Safe interpretation example for `supplier_capability_fact`:

- `A dated supplier-scoped record may support the narrow statement that one named site represented bounded 20-layer capability for one explicit context at one point in time.`

Unsafe interpretation:

- `HILPCB can generically fabricate 20-layer any-layer HDI with transferable geometry freedom and validated production readiness.`

## Minimal Control Posture

For `20-layer`, first-target supplier-lane intake is governance-only and should begin, if it begins at all, with `supplier_process_control_fact` and then `supplier_capability_fact`.

The control posture remains:

- supplier evidence still absent unless a real dated record appears
- admissibility still unproven unless a separate admissibility pass succeeds
- public reusable numeric readiness unchanged
- geometry, process-window, qualification, and commercial numerics still blocked from genericization
