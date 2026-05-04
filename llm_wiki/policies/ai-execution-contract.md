# AI Execution Contract For `llm_wiki`

Last updated: 2026-05-01

This is the primary operating contract for any AI that reads or edits `llm_wiki`.

## Purpose

`llm_wiki` is a source-backed PCB / PCBA knowledge base, not a blog rewrite workspace.
The default goal is to promote real knowledge into `sources/`, `facts/`, and `wiki/` so later AI can reuse it safely.

## Precedence

If instructions conflict, use this order:

1. Current user instruction
2. This contract
3. `policies/execution-priority-and-anti-drift.md`
4. `README.md`
5. `ROADMAP.md`
6. `logs/phase-status.md`
7. `logs/backlog.md`
8. `logs/update-log.md`
9. Any batch log

## Default Execution Loop

Always follow this loop:

1. `claim inventory`
2. `source gap`
3. `official source recovery`
4. `source records`
5. `fact cards`
6. `topic wiki`
7. `prompt consumption gate`

Do not make `rewrite`, `normalization`, or `prompt handoff` the default next step.

## Source Refresh Rule

- Rechecking a source and updating `URL`, `checked_at`, or other source metadata is only a source refresh step.
- Source refresh is not completion.
- If the refresh yields reusable public metadata, create or update the local `source record` and land the matching `fact card`.
- If the refresh yields only confirmation with no reusable local fact, keep the task in `recheck` or `blocked`, not `completed`.
- For standards/compliance lanes, public metadata still counts as landing only when it is written into `sources/registry/` and `facts/`.

## Authority Rules

- `sources/registry/` records authority.
- `facts/` stores atomic reusable facts.
- `wiki/` aggregates facts into topic guidance.
- `logs/` records progress only.
- `tmps/` is input inventory only, never authority.

## What To Avoid

- Treating `done`, `landed`, `ready`, `absorbed`, `consumed`, or `normalized` as knowledge completion
- Using logs as the source layer
- Promoting draft claims without official source support
- Writing numbers, thresholds, performance, compliance, supplier proof, or capability proof without a source
- Expanding rewrite work when the remaining gap is actually a source gap

## Subagent Rules

- Use subagents for independent lanes only.
- Give each subagent one bounded lane and one clear output.
- Do not let subagents rewrite shared trackers unless explicitly assigned.
- Main agent owns final source promotion, tracker updates, and conflict resolution.

## Stop Conditions

Stop and return to source-backed work if:

- the next step is only rewrite-layer cleanup
- the lane still needs official source recovery
- the claim cannot be promoted into `facts/` or `wiki/`
- the only evidence is `logs/` or `tmps/`

## File Roles

- `README.md`: entry overview
- `ROADMAP.md`: phase plan
- `policies/*`: execution rules
- `logs/*`: progress records
