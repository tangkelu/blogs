# P4-532 Dispatch Index Resync After E7 Raise And Infineon State Shift

Date: 2026-05-11
Parent surfaces:

- `logs/p4-506-2026-5-11-e7-graphic-alignment-shared-reference-frame-and-same-coordinate-system-authority-recovery.md`
- `logs/p4-531-2026-5-11-infineon-retrievable-wrong-pitch-current-state-normalization.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_dispatch_index_resync`

## Purpose

Resync the corpus-wide resume index after two later state changes that matter for future dispatch:

- `简单好用！再也不用担心PCB图形对齐问题.pdf` is no longer route-only after `P4-506`
- current package-side live wording should no longer be read through older `Infineon blocked / near-hit` shorthand after `P4-531`

## What Changed

- the article-side residual wording in `p4-325` now explicitly leaves the graphic-alignment PDF out of the hold-only set
- the remaining article residual set is now the three branded-tool `E7` PDFs only
- the package-side recommended-next-action wording in `p4-325` now avoids stale `Infineon near-hit` shorthand and points to the current tighter gate instead
- the corpus-wide master resume wording in `p4-309` and the candidate-gated package wording in `phase-status` now also avoid stale `Infineon near-hit` shorthand and read that class as retrievable-but-wrong-pitch

## Final Verdict

The dispatch index is now aligned with the current `E7` and package-side live state and is safer to use for subagent assignment.
