# P4-13 20-Layer And 22-Layer Blocker Reduction Plan

Date: 2026-04-25

## Goal

Define the next long-task batch after the current `H2` governance pass so `20-layer` and `22-layer` can be reduced by blocker class rather than by ad hoc source hunting.

The goal is not to force either blog into `ready` state.

The goal is:

- make the remaining blocker classes explicit
- choose the highest-leverage next batch for each blocked blog
- keep `P4-06` blocked until those blocker classes are genuinely reduced

## Why This Plan Exists

Current `llm_wiki` progress is no longer bottlenecked by broad internal ingestion or broad H2 taxonomy work.

The real remaining bottlenecks are concentrated in two drafts:

- `20-layer-pcb-manufacturing`
- `22-layer-pcb-manufacturing`

Those two drafts still fail for different reasons:

- `20-layer` is still overloaded with `HDI / build-up / ELIC / IST / geometry / process-window` leakage
- `22-layer` is still overloaded with `Class 3 / 3A / addendum / qualification / supplier-status / lot-acceptance` leakage

That means the next batch should no longer be framed as generic source expansion.

It should be framed as blocker reduction.

## Current Baseline

Current baseline remains:

- `20-layer`: `needs_sources`
- `22-layer`: `needs_sources`
- `P4-06`: blocked

The current evidence layer is already strong enough for guarded rewrite boundaries, but not yet strong enough for high-numeric-density prompt bridging.

## 20-Layer Blocker State

### Top Unresolved Blocker Classes

1. `ELIC / any-layer / stacked-microvia` defaults being rewritten as if they were normal `20-layer` architecture
2. `IST`, thermal-cycling, coupon, and interconnect-reliability method names being rewritten as if they already provided public thresholds or qualification plans
3. recipe, lamination-count, bake, cure, and process-window wording being rewritten as transferable manufacturing rules
4. geometry and factory-capability claims surviving through build-up-material or process-guide language

### What Is Already Strong Enough

Current corpus is already strong enough to support:

- guarded `HDI / any-layer / build-up` vocabulary
- guarded `FRCC / RCC / bond ply / no-flow / controlled-flow / ABF / BT` material-form vocabulary
- guarded sequential-lamination and stress-factor framing
- guarded `IST`, `TM-650`, coupon, and microvia-reliability method/report context

### Best Next Batch Theme

`20-layer interconnect-reliability and process-window boundary batch`

This batch should reduce overclaim risk around:

- interconnect-reliability workflow wording
- evaluation-method naming
- recipe/process-window leakage
- build-up-architecture overreach

It should not attempt to recover:

- geometry tables
- lamination-count numbers
- `IST` thresholds
- factory-capability numerics

### Candidate Outputs For This Batch

- `facts/methods/20-layer-interconnect-reliability-workflow-boundary.md`
- `facts/methods/20-layer-process-window-and-recipe-boundary.md`
- `facts/methods/20-layer-method-vs-qualification-boundary.md`
- update `facts/methods/20-layer-any-layer-hdi-rewrite-guardrail.md`
- update `facts/materials/20-layer-build-up-material-boundary-and-non-claims.md`
- update `logs/layer-count-blog-readiness.md`

## 22-Layer Blocker State

### Top Unresolved Blocker Classes

1. `Class 3 / 3A` and addendum-linked thresholds still lacking safe public threshold authority
2. qualification-flow, release-authority, and accepted-lot claims still unsupported
3. supplier-status, listing, validation, certification, and audit language still too easy to overstate as current approval
4. `PLT`, outgassing, sample-plan, and contract-flowdown wording still too easy to overstate as universal acceptance rules

### What Is Already Strong Enough

Current corpus is already strong enough to support:

- guarded `IPC-6012F / IPC-6012EM / IPC-6012FS / IPC-6012FA` hierarchy wording
- guarded `FAI`, traceability, counterfeit-avoidance, configuration-control, and documentation vocabulary
- guarded medical, aerospace, defense, and procurement-governance context
- guarded distinction between governance ecosystem and supplier approval

### Best Next Batch Theme

`22-layer hi-rel acceptance-governance boundary batch`

This batch should reduce overclaim risk around:

- addendum-triggered acceptance hierarchy
- qualification-listing and release-authority boundaries
- lot-conformance and contract-flowdown boundaries
- public bare-board acceptability versus supplier-status confusion

It should not attempt to recover:

- `Class 3 / 3A` threshold tables
- acceptance sample sizes
- supplier approval claims
- outgassing acceptance numerics

### Candidate Outputs For This Batch

- `facts/standards/22-layer-hi-rel-acceptance-workflow-boundary.md`
- `facts/standards/22-layer-qualification-listing-and-release-authority-boundary.md`
- `facts/standards/22-layer-contract-flowdown-and-lot-conformance-boundary.md`
- update `facts/standards/22-layer-high-reliability-rewrite-guardrail.md`
- update `logs/layer-count-blog-readiness.md`

## Execution Pattern

Next long-task execution should use parallel sub-agents by blocker branch:

1. `20-layer` branch:
   - interconnect-reliability workflow
   - process-window / recipe leakage
   - build-up-architecture overclaim boundaries
2. `22-layer` branch:
   - hi-rel acceptance hierarchy
   - qualification / listing / release-authority boundaries
   - lot-conformance / flowdown / supplier-status boundaries
3. main agent:
   - integrate only official or already-registered corpus-safe inputs
   - write the boundary cards
   - refresh readiness wording
   - keep `P4-06` blocked unless the blocker classes actually move

## Stop Conditions

Do not treat either branch as unlocked if the batch only improves vocabulary.

The batch is successful if it does all of the following:

- reduces prompt-side overclaim risk
- narrows which claim classes are still blocked
- makes future evidence-pack exclusions more explicit
- leaves unsupported thresholds and capability numerics out of the repo

The batch is not successful if it:

- reconstructs thresholds from metadata
- turns supplier pages into capability evidence
- turns process guides into reusable recipes
- turns governance ecosystem pages into supplier-status proof

## Current Decision

The next `P4-13` long-task batch should target blocker reduction for `20-layer` and `22-layer`, not broader H2 expansion and not `P4-06`.

Current priority order:

1. `22-layer hi-rel acceptance-governance boundary batch`
2. `20-layer interconnect-reliability and process-window boundary batch`
3. reassess both drafts only after those two boundary batches land

Until then:

- `20-layer` remains `needs_sources`
- `22-layer` remains `needs_sources`
- `P4-06` remains blocked
