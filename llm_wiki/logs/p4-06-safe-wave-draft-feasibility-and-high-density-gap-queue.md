# P4-06 Safe-Wave Draft Feasibility And High-Density Gap Queue

Date: 2026-04-26

## Purpose

This control note turns the six landed safe-wave evidence packs into an execution decision.

It answers two questions:

1. can `6 / 8 / 10 / 12 / 14 / 16-layer` now be drafted in conservative mode
2. what numeric blocker queue still stands between these six pages and true high-numeric-density article generation

This file is not a blog rewrite.

It is a control note for long-task sequencing after both safe waves now have:

- bridge-prep notes
- evidence-pack inputs

## Current Decision

### Conservative Draftability

All six safe-wave pages are now draftable in conservative mode.

This means:

- they can support controlled `query`-style article drafting
- they can use exact-product material numerics where official product identity and conditions are preserved
- they can use internal workflow posture for stackup, impedance, validation, rigid-flex, and branch-process framing
- they must still exclude unsupported `B / C / D / E / F / G` numerics

### High-Numeric-Density Readiness

None of the six safe-wave pages is ready for true high-numeric-density drafting.

This remains blocked because the packs still deliberately exclude:

- fabrication capability tables
- standards / qualification thresholds
- board-level SI / PDN / thermal heuristic tables
- rigid-flex reliability thresholds
- service / coverage / lead-time numerics

So the six landed packs unlock `conservative draft execution`, not `high-density draft execution`.

## Per-Blog Conservative Feasibility

### `6-layer`

- draftable: `yes`
- safe keep zone:
  - baseline FR-4 vs higher-performance material framing
  - stackup / planning posture
  - impedance / validation workflow language
  - exact-product material examples
- must stay out:
  - capability numbers
  - impedance geometry tables
  - via-rule numerics
  - cost / lead-time claims
  - hard reliability thresholds

### `8-layer`

- draftable: `yes`
- safe keep zone:
  - multilayer planning logic
  - material-family selection
  - conservative impedance / validation posture
  - guarded rigid-flex / mechanical branch framing
- must stay out:
  - standards thresholds
  - rigid-flex / mechanical rule numerics
  - HDI / via / cost tables
  - exact tolerance and testing-capability claims

### `10-layer`

- draftable: `yes`
- safe keep zone:
  - multilayer architecture vocabulary
  - material-selection ladders
  - impedance / verification posture
  - non-numeric HDI / topology framing
- must stay out:
  - blind-via and registration capability numbers
  - BGA escape recipes
  - exact capability windows
  - cost / turnaround numerics

### `12-layer`

- draftable: `yes`
- safe keep zone:
  - high-layer planning
  - material-grade selection
  - high-speed ecosystem context as background only
  - validation / backdrill posture without board guarantees
- must stay out:
  - SI / DDR geometry tables
  - skew / timing budgets
  - impedance / backdrill numerics
  - stack-thickness windows
  - QA / turnaround numbers

### `14-layer`

- draftable: `yes`
- safe keep zone:
  - rigid vs rigid-flex branch framing
  - high-layer manufacturability posture
  - non-numeric process / risk framing
  - class-level flex-material framing
- must stay out:
  - `Class 2 / Class 3` threshold leakage
  - registration / annular-ring tables
  - bend-life and bend-radius thresholds
  - fine-feature / via-geometry / lead-time numerics

### `16-layer`

- draftable: `yes`
- safe keep zone:
  - power / thermal architecture framing
  - material and platform selection logic
  - conservative validation / process posture
  - system-context high-speed background
- must stay out:
  - copper-weight / process-window tables
  - current-density and PDN heuristic numerics
  - thermal outcome claims
  - service / capability promises
  - turnaround numbers

## What Conservative Drafting Can Now Produce

The six landed packs are now strong enough to support:

- direct-answer intros
- early fact tables
- exact-product material examples
- stackup and process-planning posture
- branch construction framing such as `HDI`, `hybrid RF`, `rigid-flex`, `thermal platform`
- supplier-review checklists

The six landed packs are not yet strong enough to support:

- capability comparison tables
- standards-threshold tables
- board-level SI / PDN / thermal rule tables
- commercial timing or pricing tables
- article bodies that preserve the current blog numeric density

## Cross-Blog High-Density Blocker Clusters

These are the main unresolved cross-blog blocker clusters across `6 / 8 / 10 / 12 / 14 / 16`.

### Cluster 1: `B` Fabrication Capability Numerics

Recurring shapes:

- impedance tolerance
- trace/space
- drill / laser via geometry
- aspect ratio
- registration
- annular ring
- board-thickness windows
- backdrill windows
- heavy-copper and process-window tables

Most affected blogs:

- all six

Priority reason:

- this is the most common blocker class across the safe wave
- it blocks direct reuse of the existing blog style more than any other class

### Cluster 2: `D` Board-Level SI / PDN / Thermal Interpretation Numerics

Recurring shapes:

- impedance / width tables
- DDR / PCIe / timing / skew budgets
- backdrill frequency thresholds
- PDN / decoupling / thermal-via heuristics
- board-level thermal outcome rules

Most affected blogs:

- `8-layer`
- `10-layer`
- `12-layer`
- `16-layer`

Priority reason:

- these numbers are highly attractive in current blog prose but remain structurally unsupported
- they cause overclaim risk even when materials and process posture are otherwise strong

### Cluster 3: `C` Standards / Qualification / Acceptance Thresholds

Recurring shapes:

- `IPC Class 2 / Class 3`
- plating / annular-ring / registration thresholds
- reliability / acceptance-style quality numbers
- coverage-style testing claims used as assurance proof

Most affected blogs:

- `8-layer`
- `12-layer`
- `14-layer`
- `16-layer`

Priority reason:

- these claims are hard to soften once they appear in table form
- `14-layer` is especially exposed here

### Cluster 4: `E` Rigid-Flex / HDI / Reliability Numerics

Recurring shapes:

- microvia and build-up defaults
- bend-radius and flex-life tables
- transition-zone rules
- representative rigid-flex constructions written as defaults

Most affected blogs:

- `8-layer`
- `10-layer`
- `12-layer`
- `14-layer`

Priority reason:

- this cluster blocks safe reuse of branch-process sections
- it is the main reason `14-layer` remains much riskier than the other second-wave pages

### Cluster 5: `F` Dynamic Commercial Numerics

Recurring shapes:

- cost uplifts
- prototype days
- production windows
- service / stock style claims

Most affected blogs:

- all six

Priority reason:

- easy to identify and exclude
- low value for current high-density readiness compared with `B/C/D/E`

## Recommended Next Numeric-Supplementation Queue

The next queue should optimize for cross-blog payoff, not one-page completion theater.

### Queue NQ-1: Finish H2 Capability Recovery For Shared `B` Buckets

Current status:

- governance complete through [p4-06-nq-1-shared-b-buckets-closeout.md](/code/blogs/llm_wiki/logs/p4-06-nq-1-shared-b-buckets-closeout.md)
- no shared `B` numeric is unlocked yet
- this queue is now complete as a governance pass, not as a numeric-recovery pass

Priority buckets:

1. `impedance_tolerance`
2. `testing_and_verification_capability`
3. `trace_space`
4. `drill_and_via_geometry`
5. `aspect_ratio`
6. `registration`
7. `board_thickness`
8. `backdrill_and_stub`

Why first:

- they hit all six safe-wave pages
- they are the largest gap between conservative packs and denser future drafts

### Queue NQ-2: Targeted `D` Interpretation Guardrails For Safe-Wave Blogs

Current status:

- guardrail pass complete through [p4-06-nq-2-d-interpretation-guardrails-closeout.md](/code/blogs/llm_wiki/logs/p4-06-nq-2-d-interpretation-guardrails-closeout.md)
- no `D` interpretation numeric is unlocked yet
- this queue is now complete as a guardrail pass, not as a numeric-recovery pass

Priority subareas:

1. high-speed ecosystem context vs board-guarantee split for `12-layer`
2. impedance table / geometry implication containment for `8 / 10 / 12`
3. PDN / thermal heuristic containment for `16-layer`

Why second:

- these claims are not ordinary capability tables, but they still block denser writing
- they need controlled interpretation rules, not just more prose

### Queue NQ-3: `14-layer` Special-Risk Branch

Current status:

- containment pass complete through [p4-06-nq-3-14-layer-special-risk-closeout.md](/code/blogs/llm_wiki/logs/p4-06-nq-3-14-layer-special-risk-closeout.md)
- no `14-layer` special-risk numeric is unlocked yet
- this queue is now complete as a containment pass, not as a numeric-recovery pass

Priority subareas:

1. standards-threshold containment
2. rigid-flex reliability numeric containment
3. flex-material product-grade supplementation where official exact-product support is possible

Why third:

- `14-layer` is the most fragile of the safe-wave pages
- it needs a dedicated branch rather than generic second-wave handling

### Queue NQ-4: `A` Material Completion For Remaining Exact-Product Gaps

Current status:

- first micro-batch now landed through `Isola IS410 / 370HR / FR408 / FR408HR` exact-product cards plus `Arlon 85NT` pack normalization
- first micro-batch now also has a dedicated closeout through `logs/p4-06-nq-4-first-micro-batch-closeout.md`
- full queue now also has a final closeout through `logs/p4-06-nq-4-final-closeout.md`
- queue is now complete rather than still active

Priority subareas:

1. broader FR-4 exact-product coverage where current comparison tables still rely on family shortcuts
2. flex-material exact-product exceptions beyond current Panasonic-only narrow coverage when stable official pages can be confirmed
3. any remaining safe-wave product names that still lack exact-product support

Why fourth:

- `A` is already the strongest class
- further gains here help polish, but they do not remove the main blocker wall

## Immediate Execution Recommendation

The most efficient next step is:

1. do not start high-density drafting yet
2. if writing output is needed now, use the six landed packs for conservative draft generation only
3. treat `NQ-4` as complete and move the high-density mainline back to the broader blocked-readiness track rather than reopening more low-payoff named-product cleanup

That sequencing preserves current draftability without pretending readiness has already moved to high density.

## One-Line Control Posture

- `6 / 8 / 10 / 12 / 14 / 16-layer` are now conservative-draftable from landed evidence packs, `NQ-1` through `NQ-4` are complete as governance/guardrail/containment/exact-product-cleanup passes, and the next active mainline should move back to blocked-readiness work rather than more safe-wave exact-product cleanup
