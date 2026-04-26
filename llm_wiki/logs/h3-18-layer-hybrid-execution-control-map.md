# H3 18-Layer Hybrid Execution Control Map

Date: 2026-04-26

## Purpose

This file converts the current `18-layer` live-draft audit into execution-grade control.

It defines:

- what `18-layer` draft clusters must be removed from live reuse
- what residual wording may remain safely after containment
- what HIL-specific capability, validation, and production wording must wait for separate supplier evidence

This file is not:

- a numeric recovery note
- a supplier-capability unlock
- permission to reuse impedance, RF, backdrill, cost, or qualification numerics

## Queue Baseline

Current `18-layer` posture:

- conservative rewrite support already exists for hybrid material framing, PTFE/RF process sensitivity, and validation-ladder context
- the current live draft still carries a large `numeric + supplier-proof + acceptance` surface
- `public_threshold_available`: `none`

So this execution note exists to stop `18-layer` wording from drifting back into:

- hybrid-material tables presented as reusable defaults
- impedance and transmission-line numerics presented as public design rules
- RF/backdrill/via geometry thresholds
- HIL-specific capability, verification, quality-system, and commercial proof claims

## Blacklist Clusters

### 1. Supplier-Proof And Capability Blocks

Blacklist:

- frontmatter and opening trust banners that market HIL-specific RF/digital production proof
- `HILPCB Manufacturing Capability` quote blocks
- closing `Partnering with HILPCB` capability summaries
- customer-region, production-grade, or preferred-supplier assertions

Default action:

- `hold_for_supplier_evidence`

### 2. Material Numeric Ladders

Blacklist:

- `Dk`, `Df`, `CTE`, peel-strength, and frequency-window tables
- material selection decision tables
- exact-product examples widened into hybrid-default rules

Default action:

- `delete` or `downgrade_to_boundary_only`

### 3. Impedance / Transmission-Line Numeric Guidance

Blacklist:

- trace-width tables
- impedance-tolerance tables
- frequency-stability numerics
- simulation-error percentages used as design-rule proof
- transmission-line structures rewritten as threshold guidance

Default action:

- `delete`

### 4. RF / Backdrill / Via Geometry Rule Clusters

Blacklist:

- anti-pad, residual-stub, backdrill-depth, via-fence, and spacing thresholds
- RF exclusion zones and matching numerics
- resonance numerics and return-loss outcome claims

Default action:

- `delete`

### 5. Commercial / Delivery / Qualification Blocks

Blacklist:

- cost multipliers
- lead-time promises
- quality-system banners
- pass/fail or verification-package wording collapsed into accepted capability proof

Default action:

- `hold_for_supplier_evidence`

## Allowed Residual Wording Classes

The following residual shapes remain safe:

### 1. Hybrid RF / Digital Application Context

Allowed:

- `18-layer` boards may appear when RF routing and denser digital routing have to coexist
- mixed-material stackups may be reviewed when loss, routing, and integration goals pull in different directions
- application examples remain illustrative rather than proof of one default construction

### 2. Class-Level Material Framing

Allowed:

- `Rogers`, `PTFE`, `Megtron`, and `FR-4` may frame the material conversation
- material-family names do not authorize default stack rules, impedance promises, or reliability outcomes
- exact-product examples must remain narrow if they appear at all

### 3. Process-Sensitivity Context

Allowed:

- multi-material lamination can be more review-sensitive than simpler multilayer builds
- material boundaries, registration, adhesion, and return-path planning deserve dedicated review
- transition planning may be described qualitatively without turning into recipe authority

### 4. Validation-Workflow Context

Allowed:

- coupon review, TDR, VNA, and adjacent verification vocabulary may appear as workflow context
- validation wording must stay at planning level, not accepted-performance proof
- method names do not by themselves establish channel, RF, or lot-acceptance outcomes

### 5. Non-RF Variant Context

Allowed:

- `18-layer` designs may also branch into full low-loss digital or power-dense variants
- those branches remain planning context, not recipe or capability proof

## HIL-Specific Wording Held For Supplier Evidence

The following must not survive in bridge-safe form without separate supplier evidence:

- `we manufacture`
- `verified by TDR and VNA`
- `production-grade`
- any `±%` impedance claim
- any frequency-limit verification claim
- any explicit backdrill, fine-line, via-type, or assembly capability claim
- quality-system, testing-coverage, lead-time, cost, or production-scale claims
- bundled HIL manufacturing summary sections

Default action:

- `hold_for_supplier_evidence`

Rule:

- tone softening is not enough for these claims

## Draft-Area Actions

| Draft cluster | Action | Allowed residual shape |
| :--- | :--- | :--- |
| frontmatter and opening trust banners | `hold_for_supplier_evidence` | none in supplier-specific form |
| hybrid application framing | `downgrade_to_boundary_only` | qualitative RF/digital integration context only |
| material-family sections | `downgrade_to_boundary_only` | class-level framing only |
| impedance / transmission-line sections | `delete` or `downgrade_to_boundary_only` | planning-sensitive boundary wording only |
| DFM / via / backdrill rule sections | `delete` or `downgrade_to_boundary_only` | review categories only |
| validation / tolerance / quality sections | `downgrade_to_boundary_only` or `delete` | workflow-level validation context only |
| cost / delivery / partner closeout blocks | `hold_for_supplier_evidence` | none in supplier-specific form |

## Completion Criteria

This execution-control note is complete when:

1. all `18-layer` numeric tables and supplier-proof clusters are routed to `delete` or `hold_for_supplier_evidence`
2. material-family wording is narrowed back to class-level planning context
3. impedance, transmission-line, backdrill, and via wording no longer acts as reusable public design-rule guidance
4. validation language stays at workflow level rather than performance-proof or lot-acceptance level
5. `public_threshold_available` remains explicitly `none`, and the note states that risk reduction does not change readiness

## Minimal Control Posture

For `18-layer`, safe residual content is limited to hybrid application context, class-level material framing, process-sensitivity context, validation-workflow context, and non-RF variant context. Numeric tables, RF geometry rules, supplier-proof wording, and commercial claims remain blocked by default.
