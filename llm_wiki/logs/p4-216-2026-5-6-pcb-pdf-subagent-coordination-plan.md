# P4-216 PCB PDF Subagent Coordination Plan

Date: 2026-05-06

## Purpose

This controller log defines how subagents should execute the first exact-data learning wave for `/code/blogs/tmps/PCB资料` without creating indexing drift, overclaiming from secondary PDFs, or losing image / page provenance.

This plan coordinates the three first-wave workstreams:

- `logs/p4-215a-2026-5-6-emc-exact-data-workstream.md`
- `logs/p4-215b-2026-5-6-pcba-inspection-exact-data-workstream.md`
- `logs/p4-215c-2026-5-6-package-footprint-exact-data-workstream.md`

## Workstream Ownership

### Main agent owns

- canonical English naming
- cross-lane deduplication
- final promotion decisions
- tracker updates
- policy enforcement
- final `sources/registry/`, `facts/`, and `wiki/` landing decisions

### Subagents own

- bounded page-slice reading
- figure / table / formula / parameter inventory
- exact-value or structural-meaning extraction
- local asset reference collection
- blocked / unresolved item listing
- source-mapping recommendations

Subagents do not own:

- global tracker updates
- final `fact_id` approval
- final canonical scope widening
- claim promotion from secondary PDF directly into reusable facts

## Subagent Output Contract

Every subagent lane must return:

- page slice covered
- candidate formulas / tables / figures found
- exact values or structural meaning extracted
- image / table asset references
- English canonical concept names
- source-mapping recommendation
- blocked / unresolved items

Each item must be labeled as one of:

- `exact_data_candidate`
- `structural_context_candidate`
- `blocked_secondary_pdf_claim`

Each item must also note:

- source PDF path
- page number
- asset path if any
- whether image understanding was required
- whether branding contamination exists

## Main-Agent Integration Contract

The main agent must:

- decide canonical English names
- deduplicate concepts across lanes
- approve or reject fact promotion
- update trackers
- keep Chinese only as provenance, not as canonical keys

The main agent must also enforce:

- `language-normalization-and-indexing.md`
- `exact-data-admission-policy.md`
- `prompt-consumption-specification.md`
- `p4-214` figure / table learning contract

## Parallel Execution Order

The preferred execution order is:

Round 1: `A1 + B1 + C1`
Round 2: `A2 + B2 + C2`
Round 3: `A3 + B3 + C3`
Round 4: controller integration and promotion review

Reason:

- Round 1 opens the cleanest taxonomy and method-entry lanes first
- Round 2 handles the heaviest image-driven defect and package-drawing material
- Round 3 handles the most interpretation-sensitive EMC routing and governance residue
- Round 4 keeps final policy judgment centralized

## Lane Scene-Setting Rules

Before dispatching a subagent lane, provide:

- the exact workstream log
- the figure / table learning contract
- the exact-data admission policy
- any prior lane-specific controller notes
- the specific page slice and expected outputs

Do not ask subagents to infer the whole project from the repository.

## Review And Integration Rules

After each subagent lane returns:

1. verify that page coverage matches the requested slice
2. verify that English canonical naming is present
3. verify that blocked items remain blocked
4. verify that asset references are traceable
5. merge overlapping concepts across neighboring lanes
6. open narrower source-recovery or fact-promotion tasks only after controller review

## Promotion Guardrails

Subagent outputs may recommend promotion, but promotion is not automatic.

Promotion requires main-agent confirmation that:

- the item fits one exact-data class
- stronger authority exists if needed
- scope is narrow enough
- provenance is complete
- downstream prompt consumption can stay safe

## Completion Criteria

This coordination plan is active only when:

- all three workstream logs exist
- all nine lanes have explicit output contracts
- the main-agent integration contract is explicit
- execution order is defined
- promotion guardrails are explicit

## Current Status

- coordination plan: `defined`
- wave-1 lane dispatch: `round_1_completed`
- main-agent integration round: `round_1_completed`
- wave-2 lane dispatch: `round_2_completed`
- main-agent integration round 2: `round_2_completed`
- wave-3 lane dispatch: `round_3_completed`
- main-agent integration round 3: `round_3_completed`

## Next Step

Use `logs/p4-216c-2026-5-6-pcb-pdf-round-3-a3-b3-c3-controller-integration.md` as the closure log for first-wave lane execution, then move into `Round 4`: controller-owned promotion review and authority recovery.
