# P4-49 Source-Backed Integration

Date: 2026-04-29

## Purpose

Convert the strongest `P4-48` follow-on lane into reusable `llm_wiki` data by adding external authority for beginner workflow and prototyping-stage language.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote draft-originated quantity ladders, stackup defaults, pricing, lead-time, supplier guidance, universal terminology claims, or prototype-platform performance rankings.

## Inputs Reviewed

- `logs/p4-48-parallel-scout-controller-summary.md`
- `logs/p4-48b-electronics-basics-authority-scout.md`
- `/code/blogs/tmps/2025.11.17/en/first-circuit-board.md`
- `/code/blogs/tmps/2025.11.17/en/pca-vs-pcb.md`
- `/code/blogs/tmps/2025.11.17/en/protoboard-vs-breadboard.md`
- existing KiCad, CAM, prototype-routing, and PCBA workflow layers already present in `llm_wiki`

## Parallel Work Pattern

- Main agent owned final integration and tracker updates.
- Two bounded local-review explorers were used in parallel:
  - one for `PCB / PCBA / PCA` terminology and stage-boundary reuse
  - one for `first board` and `breadboard / prototyping` workflow reuse
- Explorer conclusion aligned with main-agent source recovery:
  - `first-circuit-board` can now be upgraded at conservative workflow-boundary level
  - `pca-vs-pcb` remains blocked for standards-grade terminology conclusions about `PCA`
  - `protoboard-vs-breadboard` can now use only a temporary-versus-more-permanent prototype-stage contrast, not universal naming or performance claims

## Source Records Added

- `sources/registry/standards/ipc-t50-terms-and-definitions-toc.md`
- `sources/registry/methods/kicad-getting-started-guide.md`
- `sources/registry/methods/sparkfun-breadboard-guide.md`
- `sources/registry/methods/adafruit-breadboards-for-beginners.md`

These source records add:

- official IPC terminology-family metadata for `IPC-T-50N`
- official KiCad beginner workflow identity
- authoritative education-source coverage for solderless breadboard identity
- authoritative education-source coverage for breadboard-like soldered transfer context

## Fact Card Added

- `facts/methods/first-board-and-breadboard-prototyping-boundary.md`

This fact card upgrades the `first-circuit-board` / `protoboard-vs-breadboard` family from scout-only into a conservative source-backed workflow boundary.

What is now source-backed:

- a staged beginner path from temporary circuit exploration into schematic capture, PCB layout, checks, fabrication-output handoff, assembly choice, bring-up, and iteration
- breadboard identity as a temporary solderless prototyping platform
- a more permanent soldered transfer-board concept as a separate later-stage prototype posture
- explicit non-claims around universal naming, universal laddering, and numeric performance comparisons

## Topic Wiki Added

- `wiki/processes/first-board-and-prototyping-workflow-boundaries.md`

This page makes the new boundary prompt-consumable for:

- `/code/blogs/tmps/2025.11.17/en/first-circuit-board.md`
- `/code/blogs/tmps/2025.11.17/en/protoboard-vs-breadboard.md`

## What This Unlocks

- `first-circuit-board.md` can now be conservatively rewritten as a staged beginner workflow article:
  - temporary experimentation when appropriate
  - schematic and layout workflow
  - checks and manufacturing-output handoff
  - assembly-path choice
  - bring-up and iteration
- `protoboard-vs-breadboard.md` can now be conservatively rewritten only at the stage-boundary level:
  - solderless temporary experimentation versus more permanent soldered transfer
  - guarded reminder that naming and performance claims still need narrower evidence

## Still Blocked

- `PCA` as a standards-grade, universally reusable term
- `PCA = PCBA` or `PCA = printed circuit assembly` as a settled public terminology claim
- universal synonym or hierarchy claims among `protoboard`, `perfboard`, `stripboard`, and breadboard
- fixed beginner ladders such as `breadboard -> protoboard -> PCB` as if always required
- numeric current, frequency, thermal, durability, reliability, or signal-integrity comparisons for beginner prototype platforms
- stackup defaults, quantity defaults, cost ladders, lead-time ladders, and supplier-choice claims from the drafts

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family: `2025.11.17` beginner workflow and prototyping-stage lane
- remaining terminology blocker:
  - `pca-vs-pcb.md` still needs stronger public terminology evidence before any durable `PCA` normalization or synonym claim
- next likely residual lanes:
  - remote-control protocol authority
  - HDI / BOM cost-driver official-source recovery
  - narrower public terminology recovery if future `PCA` publication is still desired
