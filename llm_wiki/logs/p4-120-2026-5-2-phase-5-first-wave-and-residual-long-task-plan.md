# P4-120 Phase 5 First-Wave And Residual Long-Task Plan

Date: 2026-05-02

## Purpose

Convert the current post-`P4-119` state into a durable long-task plan that uses subagents only for bounded, independent lanes.

This plan does not reopen broad rewrite work. It ranks the next mainline workstreams and fixes which batch should move first.

## Planning Baseline

Current controller state after `P4-119`:

- no new exact non-held lane is open by default inside `2026.4.27/en` or `2026.4.29/en`
- `audio-amplifier` and `wearable compact access` are already the newest landed narrow lanes
- `medical role-boundary` and `compact imaging inspection planning` are already covered strongly enough
- explicit holds remain closed: `biological-computing`, `quantum-computing`, `20-layer`, `22-layer`, and `tmps/materias_pdf`

Because the latest residual recheck did not expose a strong new source-backed lane, the best long-task pivot is now `Phase 5 first-wave evidence-pack handoff`, not another forced lane opening.

## Ranked Workstreams

### Tier A: Mainline Now

#### `P4-06` Phase 5 Batch 1

Scope:

- connect the existing first-wave layer-count evidence packs into stable `prompts_template` consumption rules
- limit Batch 1 to:
  - `6-layer`
  - `8-layer`
  - `10-layer`

Why first:

- the first-wave queue, bridge-prep notes, and evidence-pack drafts already exist
- `prompts_template` already has evidence-pack consumption contracts, but the repo still lacks a clean first-wave handoff layer
- this moves the knowledge base closer to the stated end goal without reopening blocked numerics

Required inputs:

- `logs/p4-06-first-wave-bridge-queue.md`
- `logs/p4-06-6-layer-bridge-prep.md`
- `logs/p4-06-8-layer-bridge-prep.md`
- `logs/p4-06-10-layer-bridge-prep.md`
- `logs/p4-06-6-layer-evidence-pack.md`
- `logs/p4-06-8-layer-evidence-pack.md`
- `logs/p4-06-10-layer-evidence-pack.md`
- `logs/evidence-pack-minimum-checklist.md`
- `prompts_template/shared/query.md`
- `prompts_template/shared/evidence-pack-template.md`
- `prompts_template/shared/evidence-pack-consumption-contract.md`
- `prompts_template/hilpcb/query-overlay.md`

Hard boundaries:

- no new fact/wiki/source promotion by default
- no high-density numeric unlock
- no `12 / 14 / 16 / 18 / 20 / 22 / 24-layer` expansion inside Batch 1
- no supplier-proof, standards-threshold, process-window, or dynamic commercial numerics

Expected outputs:

- one controller note that defines the Batch 1 handoff contract
- one topic-to-prompt mapping note for the first-wave packs
- targeted prompt-template wording updates only if the current contract is ambiguous for first-wave use

### Tier B: Secondary Source-Backed Candidates

These stay eligible, but they are not the mainline until Tier A lands.

1. `buying-pcb` commercial-free workflow boundary reuse
2. `electronics-assembly` process-layer strengthening
3. `rf-antenna` narrow feed-network / validation boundary strengthening

Controller interpretation:

- these are lower urgency because each already has meaningful conservative routing
- if reopened, each must stay narrow and source-backed
- they must not replace Phase 5 Batch 1 as the default next move

### Tier C: Watch / Hold Only

- `biological-computing`
- `quantum-computing`
- `20-layer`
- `22-layer`
- `tmps/materias_pdf`
- any residual lane that depends on blocked numerics, standards thresholds, supplier proof, or broad commercial claims

## Subagent Batch Structure

### Batch 1: `P4-06` First-Wave Prompt Handoff

Use bounded subagents for:

1. prompt-side contract audit
2. first-wave evidence-pack mapping audit
3. controller integration draft

Main agent owns:

- final scope
- any edits to shared trackers
- final wording
- verification

### Batch 2: Secondary Residual Lanes

Only start if Batch 1 is closed or explicitly paused.

Use bounded subagents for independent lane scouts:

1. `buying-pcb`
2. `electronics-assembly`
3. `rf-antenna`

Main agent owns:

- whether any one of these is worth promoting
- whether a lane deserves actual source recovery or only tracker disposition

## Stop Conditions

Record `readiness unchanged` and stop if the work only does one or more of the following:

- restates existing evidence-pack files without adding a cleaner prompt-consumption contract
- tries to sneak blocked numerics into prompt-use status
- reopens `20-layer` or `22-layer`
- turns residual commercial or performance claims into a fake source lane

## Status

- controller status: `long_task_ranked`
- mainline next batch: `P4-06 Phase 5 Batch 1`
- secondary candidates:
  - `buying-pcb`
  - `electronics-assembly`
  - `rf-antenna`
