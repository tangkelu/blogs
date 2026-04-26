# P4-06 First-Wave Bridge Queue

Date: 2026-04-26

## Purpose

This control note fixes the first safe bridge queue from `llm_wiki` into `/code/blogs/prompts_template/` evidence-pack usage.

The goal is not to unlock every `mostly_ready` layer-count blog at once.

The goal is:

- decide which branches are safe enough for the first `P4-06` wave
- separate `first-wave`, `second-wave`, `defer`, and `blocked` groups
- keep unsupported numeric classes from being silently carried into prompt execution

## Current Rule

`P4-06` should start from the lowest-overclaim branches first.

That means bridge priority is based on:

1. lower current-draft risk
2. lower concentration of unsupported `B / C / D / E / F / G` claim classes
3. stronger existing `facts/wiki/source` backbone
4. cleaner downgrade/delete path for unsupported numbers

It is not based on:

- article popularity
- how many numbers the current draft already contains
- whether a branch looks impressive or high-end

## Queue Decision

### First-Wave Candidates

Recommended first bridge order:

1. `6-layer`
2. `8-layer`
3. `10-layer`

Why these first:

- they are already `mostly_ready`
- their strongest retained numeric layer is still material-property support
- the unsupported numbers are easier to strip, downgrade, or exclude before prompt use
- they carry less `very_high` draft risk than the higher-layer branches

### Second-Wave Candidates

Recommended second bridge order:

1. `12-layer`
2. `16-layer`
3. `14-layer`

Why not first-wave:

- all three are still `mostly_ready`, but the remaining unsupported claim load is materially heavier
- `12-layer` already mixes high-speed interface context with unsupported board-level SI and fabrication numerics
- `16-layer` mixes power / thermal / verification framing with unsupported capability, standards, and PDN/SI numbers
- `14-layer` is still especially exposed to standards-threshold leakage, rigid-flex reliability thresholds, and fabrication-capability tables

### Deferred High-Risk Mostly-Ready Branches

Defer from the first safe `P4-06` wave:

- `18-layer`
- `24-layer`

Why deferred:

- both remain `mostly_ready` only for conservative rewrites
- both still carry `very_high` current-draft risk
- `18-layer` still overreaches on process tables, Taconic-grade numerics, exact impedance promises, and factory-specific capability statements
- `24-layer` still overreaches on board-level high-speed/channel numerics, `dB/inch` style budgets, backdrill accuracy, and shop-specific measurement guarantees

If one is reconsidered earlier, `18-layer` matures before `24-layer`, but neither belongs in the first safe bridge wave.

### Blocked Branches

Keep blocked from `P4-06`:

- `20-layer`
- `22-layer`

Why blocked:

- `20-layer` still depends on unsupported HIL-specific capability, process-control, and lead-time claims
- `22-layer` still depends on unsupported supplier-status, compliance, and acceptance assertions

## Per-Wave Prompt Discipline

### First-Wave `6 / 8 / 10`

Allowed emphasis:

- material selection framing
- stackup and process planning posture
- validation and impedance workflow context
- conservative architecture vocabulary

Must still be downgraded, deleted, or excluded:

- exact fabrication capability numbers
- dynamic commercial numbers
- unsupported impedance-geometry tables
- unsupported HDI / via / recipe defaults

### Second-Wave `12 / 16 / 14`

Allowed only after extra pre-bridge pruning:

- system-context numerics must stay as ecosystem context, not board guarantees
- fabrication-rule numerics must not survive unless a governed capability source exists
- standards and reliability thresholds must remain excluded

### Deferred `18 / 24`

Do not bridge until a later control note explicitly says their current-draft risk is low enough for prompt execution.

## Prompt Template Mapping

First-wave layer-count manufacturing pages should default to:

- `prompts_template/shared/query.md`
- with `prompts_template/shared/evidence-pack-template.md`
- plus `prompts_template/hilpcb/query-overlay.md`

Use `query` rather than `pillar` because these pages are currently closer to direct engineering decision or manufacturing question pages than to stable hub pages.

## Stop Conditions

Do not move a branch into `P4-06` if any of the following remain true:

- unsupported `B` fabrication capability tables remain in the candidate evidence pack
- unsupported `C` standards / qualification thresholds remain in the candidate evidence pack
- unsupported `D` board-level SI/channel budget numbers remain in the candidate evidence pack
- unsupported `E` build-up / HDI / reliability thresholds remain in the candidate evidence pack
- unsupported `F` dynamic commercial numbers remain in the candidate evidence pack
- unsupported `G` supplier-status or assurance claims remain in the candidate evidence pack

## Current Decision

The first safe `P4-06` bridge wave should start with:

- `6-layer`
- `8-layer`
- `10-layer`

The next bridge wave should be:

- `12-layer`
- `16-layer`
- `14-layer`

Keep deferred:

- `18-layer`
- `24-layer`

Keep blocked:

- `20-layer`
- `22-layer`
