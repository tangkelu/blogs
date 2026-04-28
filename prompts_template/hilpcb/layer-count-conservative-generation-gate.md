# HILPCB Layer-Count Conservative Generation Gate

Date: 2026-04-27

This file encodes the current HILPCB layer-count generation gate from:

- `llm_wiki/logs/en-layer-count-blog-generation-gate.md`

Use it as a guardrail overlay for future layer-count blog generation.

## How To Use

- Apply this file on top of `../shared/query.md` or `../shared/pillar.md`.
- Also apply the relevant HILPCB overlay such as `query-overlay.md` or `pillar-overlay.md`.
- This file is a generation guardrail overlay, not a replacement for the relevant evidence pack.
- Before drafting, check the target slug here first.
- If the slug is `still_hold`, stop generation.
- If the slug is `go_now_conservative`, continue only with the allowed mode and exclusions below.

## Gate Lists

### `go_now_conservative`

- `6-layer-pcb-manufacturing`
- `8-layer-pcb-manufacturing`
- `10-layer-pcb-manufacturing`
- `12-layer-pcb-manufacturing`
- `14-layer-pcb-manufacturing`
- `16-layer-pcb-manufacturing`
- `18-layer-pcb-manufacturing`
- `24-layer-pcb-manufacturing`

### `still_hold`

- `20-layer-pcb-manufacturing`
- `22-layer-pcb-manufacturing`

`20-layer` and `22-layer` remain held pending supplier-scoped dated records or pack/supplier-lane reassessment.

## Per-Slug Allowed Generation

| slug | decision | allowed_mode | main exclusions |
| --- | --- | --- | --- |
| `6-layer-pcb-manufacturing` | `go_now_conservative` | `conservative_general_multilayer_rewrite` | no shared capability numerics; no cost/lead-time tables; no generic FR-4 numeric tables; no supplier-proof claims |
| `8-layer-pcb-manufacturing` | `go_now_conservative` | `conservative_general_multilayer_rewrite` | no standards-threshold drift; no mechanical/capability tables; no rigid-flex criteria leakage; no commercial numerics |
| `10-layer-pcb-manufacturing` | `go_now_conservative` | `conservative_impedance_and_validation_rewrite` | no capability windows; no yield/lead-time numbers; no hidden tolerance tables; no supplier-proof language |
| `12-layer-pcb-manufacturing` | `go_now_conservative` | `conservative_high_layer_planning_rewrite` | no tolerance numerics; no interface-budget claims; no factory-capability tables; no dynamic commercial claims |
| `14-layer-pcb-manufacturing` | `go_now_conservative` | `conservative_branch_bounded_rewrite` | no rigid-flex reliability thresholds; no standards-threshold recovery; no supplier-proof claims; no shared capability numerics |
| `16-layer-pcb-manufacturing` | `go_now_conservative` | `conservative_high_layer_rewrite` | no process-window numerics; no power/thermal outcome guarantees; no capability tables; no commercial claims |
| `18-layer-pcb-manufacturing` | `go_now_conservative` | `conservative_hybrid_rf_digital_rewrite` | no RF geometry tables; no impedance-budget claims; no qualification proof; no supplier-proof claims |
| `24-layer-pcb-manufacturing` | `go_now_conservative` | `conservative_high_speed_system_context_rewrite` | no channel-budget numerics; no process-window tables; no compliance authority claims; no supplier-proof language |

## Held Slugs

| slug | decision | hold mode | hold reason |
| --- | --- | --- | --- |
| `20-layer-pcb-manufacturing` | `still_hold` | `hold_for_pack_or_supplier_lane` | missing HIL-specific capability, process-control, geometry, and supplier-evidence authority; do not write geometry/process-window numerics, stack recipes, qualification proof, reliability proof, or HIL-specific capability/process-control claims |
| `22-layer-pcb-manufacturing` | `still_hold` | `hold_for_pack_or_supplier_lane` | branch still blocked on HIL-specific compliance, qualification, and acceptance assertion risk; do not write `Class 3 / 3A` threshold recovery, acceptance or release logic, supplier approval/compliance proof, or accepted-lot implications |

## Generation Order

1. `6-layer-pcb-manufacturing`
2. `8-layer-pcb-manufacturing`
3. `10-layer-pcb-manufacturing`
4. `12-layer-pcb-manufacturing`
5. `16-layer-pcb-manufacturing`
6. `14-layer-pcb-manufacturing`
7. `18-layer-pcb-manufacturing`
8. `24-layer-pcb-manufacturing`

Interpretation:

- start with the lowest-friction general multilayer rewrites
- then move into higher-layer but still conservative process and validation pieces
- leave RF/hybrid and highest-speed conservative rewrites for the end of the current allowed batch
- keep `20-layer` and `22-layer` out of the generation queue

## Global Blocked Claim Classes

For every `go_now_conservative` slug, keep these claim classes blocked unless the relevant evidence pack explicitly supports a narrower statement:

1. shared capability numerics such as `trace/space`, drill or laser-via minima, aspect ratio, annular ring, impedance tolerance, registration tolerance, and similar capability tables
2. standards-threshold or acceptance-threshold recovery, including `IPC Class 2 / 3 / 3A`, `IPC-6012 / 6013`, `IST`, `PLT`, coupon plans, plating minima, bow/twist limits, and similar threshold criteria
3. supplier-proof claims, including supplier approval, qualification, compliance, release authority, accepted-lot status, and transferable HIL-specific factory-capability claims
4. process-window or recipe claims, including lamination-count allowances, stack recipes, bake/press cycles, generic build-up defaults, and transferable manufacturability windows
5. high-speed or RF budget numerics, including channel-loss budgets, insertion-loss tables, Nyquist-budget claims, RF geometry rules, and similar performance tables
6. dynamic commercial numerics, including lead time, quick-turn windows, yield, cost uplifts, MOQ, and regional or customer commercial claims

Interpretation:

- if a sentence needs one of the blocked classes above to sound persuasive, rewrite it or drop it
- conservative generation means structure, workflow, material-family, and validation-language reuse only where the current corpus already supports it

## Operational Rule

- This file decides whether a layer-count slug may be generated now.
- The relevant evidence pack still decides what public facts, project-level judgments, and exclusions are admissible inside the draft.
- Do not treat this file as a readiness unlock.
- Do not use it to bypass evidence-pack boundaries.
