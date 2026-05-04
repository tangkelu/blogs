# P4-116 2026-05-02 Execution Controller Note

Date: 2026-05-02
Scope: `P4-116 Batch A execution split`
Status: `controller_active`

## Purpose

Lock the post-planning execution split for `P4-116` so Batch A proceeds as disjoint source-first lanes instead of drifting back into broad rewrite or generic backlog expansion.

## Lane Split

### Batch A: source-first lanes

1. `grounding-and-return-path-execution-boundary`
2. `optical-module-handling-contamination-control`
3. `Taconic product-grade official datasheet anchors`
4. `Arlon product-grade official datasheet anchors`

### Batch B: narrow controller/log promotion only

1. `compute exact interface / cooling / deployment boundary strengthening`
2. `ohms-law-and-watts-to-amps chain`
3. `current-carrying / high-current layout strengthening`

### Residual inventory lanes

1. `2026.4.27/en` residual exact-claim inventory
2. `2026.4.29/en` residual exact-claim inventory

### Explicit holds

- `biological-computing`
- `20-layer`
- `22-layer`
- `tmps/materias_pdf`

## Execution Rules

- Batch A lanes are independent and may run in parallel.
- Each Batch A subagent owns one lane log plus any lane-local `sources/registry/*` and `facts/*` outputs.
- Batch A may add a fact card only if a current official source yields a condition-bound reusable statement.
- Batch A does not justify broad topic rewrites.
- Batch B remains tracker-level only unless exact new authority appears.
- Residual corpus work stays claim-inventory-only and must not reopen normalized draft prose by default.

## Write Ownership

- Worker A: `grounding-and-return-path-execution-boundary`
- Worker B: `optical-module-handling-contamination-control`
- Worker C: `Taconic product-grade official datasheet anchors`
- Worker D: `Arlon product-grade official datasheet anchors`
- Main agent: tracker updates, conflict resolution, hold enforcement, final wording

## Success Criteria

- Each Batch A lane ends in one of:
  - `source_only_with_new_records`
  - `source_backed_fact_layer_partial`
  - `remains_hold_due_to_missing_current_authority`
- No lane overstates readiness.
- `phase-status.md`, `backlog.md`, and `update-log.md` continue to describe Batch A as source-first and hold-sensitive.
