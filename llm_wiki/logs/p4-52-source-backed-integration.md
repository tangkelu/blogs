# P4-52 Source-Backed Integration

Date: 2026-04-29

## Purpose

Convert the narrowest remaining `P4-48B` terminology follow-on into reusable `llm_wiki` data by upgrading `pca-vs-pcb.md` only at the bare-board versus assembled-board stage-boundary level.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote draft-originated `PCA` expansions, standards-preference claims, cleaning and contamination causality claims, application-domain requirement claims, SMT / THT decision rules, prototype-to-volume scaling advice, cost / lead-time guidance, or turnkey-partner claims.

## Inputs Reviewed

- `logs/p4-48-parallel-scout-controller-summary.md`
- `logs/p4-48b-electronics-basics-authority-scout.md`
- `logs/p4-49-source-backed-integration.md`
- `/code/blogs/tmps/2025.11.17/en/pca-vs-pcb.md`
- existing IPC terminology metadata, bare-board electrical-test metadata, and internal PCB / PCBA workflow layers already present in `llm_wiki`

## Parallel Work Pattern

- Main agent owned final scope decisions, integration, and tracker updates.
- A bounded low-risk scout re-ranked remaining residual lanes and confirmed the terminology lane is still the quickest narrow promotion candidate.
- A stronger bounded explorer re-checked the local source / fact / wiki corpus and confirmed that a conservative `P4-52` can be landed without new source records if the claim set is kept to the stage boundary only.
- Explorer conclusions aligned with main-agent review:
  - `pca-vs-pcb.md` can now use a bare-board versus assembled-board manufacturing-stage distinction
  - `PCA` normalization remains unresolved
  - all broader cleaning, reliability, assembly-technology, and production-scaling draft claims must stay blocked

## Source Records Reused

No new source-record files were required in this pass.

This integration reuses the strongest existing source layers already in `llm_wiki`:

- `ipc-9252b-toc` for public unpopulated-board electrical-test scope identity
- internal APT PCB fabrication-process record for bare-board manufacturing framing
- internal APT SMT / THT, PCBA quality-system, ICT, FCT, and flying-probe records for later assembled-board process and test language

## Fact Card Added

- `facts/methods/bare-board-vs-assembled-board-stage-boundary.md`

This fact card upgrades the `pca-vs-pcb` family from terminology-blocked-only into a conservative source-backed stage boundary.

What is now source-backed:

- a `PCB` article can safely stay on the unpopulated / bare-board side
- an assembled-board article can safely move into component population, soldering, layered inspection, electrical-access test, powered validation, cleaning, and release-gate language
- bare-board electrical-test scope can be kept separate from assembled-board inspection and electrical-access test scope

## Topic Wiki Added

- `wiki/processes/pcb-and-assembled-board-stage-boundaries.md`

This page makes the new boundary prompt-consumable for:

- `/code/blogs/tmps/2025.11.17/en/pca-vs-pcb.md`

## What This Unlocks

- `pca-vs-pcb.md` can now be conservatively rewritten as a stage-boundary article:
  - bare board versus later assembled board
  - fabrication / bare-board-test scope versus assembly / inspection / validation scope
  - guarded explanation that the term-normalization question remains open
- The article no longer needs to stay fully blocked just because `PCA` terminology is unresolved.

## Still Blocked

- `PCA` as a standards-grade, universally reusable normalized term
- `PCA = PCBA` or `PCA = printed circuit assembly` as a settled public terminology claim
- any claim that IPC publicly defines, prefers, deprecates, or equates those terms unless the definition text itself is available
- universal synonym or hierarchy claims among `PCA`, `PCBA`, `printed board assembly`, and `printed circuit assembly`
- cleaning, corrosion, electrochemical migration, coating-adhesion, or reliability causality claims from this draft family unless separately sourced
- universal SMT-versus-THT decision rules, application-domain requirements, prototype-to-volume cost / lead-time / supplier / turnkey guidance, or similar manufacturing-economics claims

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family: `2025.11.17` `pca-vs-pcb` terminology lane
- next likely residual lane:
  - `protoboard-vs-breadboard` terminology tightening only if a narrower public naming anchor can be found
  - another evidence-dense residual lane from the remaining P4-44 queue
  - dated internal capability evidence only where a lane still cannot cross threshold with public / official sources alone
