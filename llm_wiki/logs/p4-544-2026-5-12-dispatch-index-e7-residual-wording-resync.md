# P4-544 Dispatch Index E7 Residual Wording Resync

Date: 2026-05-12
Parent surfaces:

- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/p4-535-2026-5-11-last-two-live-e7-hold-pdfs-reaudit-and-no-write-closeout.md`
- `logs/p4-537-2026-5-12-current-state-completion-audit-successor-after-e7-closeout-and-1p50-recheck.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_dispatch_index_resync`

## Purpose

Remove one stale article-residual wording fragment from the per-PDF dispatch index so future `/goal` work does not resume from the pre-`P4-535` `E7` count.

This pass does not change completion status.
It only synchronizes the dispatch index with the already-landed current-state audits.

## What Was Stale

- `P4-325` still said the current article residual set was `three remaining branded-tool E7 PDFs`
- that wording predates:
  - `P4-534` raising one `E7` PDF above pure hold-only
  - `P4-535` re-auditing the last two live `E7` hold-only PDFs
  - `P4-537` refreshing the current completion wording

## What Changed

- the dispatch index now says the current live article residual set is `two branded-tool E7 hold-only PDFs`
- the recommended-next-action wording now also uses `two` instead of `three`

## Final Status

- lane result:
  - `dispatch_index_resynced`
- continuation state:
  - `future_resume_surfaces_now_match_the_current_two_pdf_e7_hold_only_state`

## Continuation Rule

Future AI should now read:

- `P4-325` is safe again as a dispatch index for the article-side residual count

Future AI still should not read:

- the article-side residual set as a broad reopen class
- the current goal as complete
