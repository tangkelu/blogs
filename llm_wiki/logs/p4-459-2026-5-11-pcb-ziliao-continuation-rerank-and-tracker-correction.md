# P4-459 PCB资料 Continuation Rerank And Tracker Correction

Date: 2026-05-11
Parent surfaces:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/p4-387-2026-5-10-package-residual-live-recheck-no-closeout.md`
- `logs/p4-394-2026-5-10-pcb-ziliao-completion-audit-successor-after-residual-lane-raises.md`
- `logs/p4-399-2026-5-10-pcb-ziliao-completion-audit-successor-after-second-owner-1p50mm-raise.md`
- `logs/p4-400-2026-5-10-renesas-second-owner-0p75mm-exact-data-page-landing.md`
- `logs/p4-405-2026-5-10-renesas-second-owner-1p50mm-exact-row-landing.md`
- `logs/p4-458-2026-5-11-e7-residual-route-reaudit-and-no-write-closeout.md`

Execution mode: `controller_owned_no_write_audit_and_tracker_refresh`

## Purpose

Correct the continuation priority after the later package-residual raises and the `E7` re-audit.

This pass does not land new `sources/`, `facts/`, or `wiki/`.
It only fixes stale tracker wording so future AI does not keep treating `1.50 mm public exact-geometry recovery` as the default blind-search-first next action.

## Rechecked Continuation Surfaces

1. package residual continuation wording in `P4-309`
2. dispatch guidance in `P4-325`
3. same-day completion-audit successors in `P4-394` and `P4-399`
4. later package-residual raises through `P4-400` and `P4-405`
5. later `E7` no-write re-audit through `P4-458`

## Findings

### 1. `P4-309` and `P4-325` still carry stale next-action wording

- both files were written before the later residual raises that materially changed the real package snapshot
- `P4-309` still names `1.50 mm public exact geometry` as the highest-value next gap
- `P4-325` still recommends `1.50 mm public exact-geometry recovery` as priority `1`
- that wording is now stale relative to the later landed state

### 2. The current package residual block is materially stronger than the old priority text implies

Current repo-supported package snapshot is now:

- `1.50 mm`:
  - `IEC` standards-existence boundary
  - one current-public `NXP` exact row
  - one current-public `Renesas` named-package drawing
  - one current-public `Renesas` exact row
- `0.75 mm`:
  - three current-public `Microchip` exact rows
  - one current-public `Renesas` second-owner exact-data page
- `connector-origin`:
  - `KiCad` convention plus `Molex`, `Samtec`, and `Amphenol` named-series routes
- `installation mark / component marking`:
  - layered boundary support
  - one `IEC` zero-orientation anchor
  - one `IEC` `pin-1 / polarity-identification` route

This still does not close any of those lanes as universal doctrine.
It does mean the old `1.50 mm first` continuation wording is no longer the most accurate default restart instruction.

### 3. The cleanest next continuation class is tracker correction first, then article-side narrow recovery

- `P4-458` already re-audited current `E7` residuals and ruled out missed safe raises there
- the current package residual block should now be reopened only when a materially stronger owner or standards-adjacent source appears
- the best default continuation class from current in-repo evidence therefore shifts to article-side narrow official-source recovery from controller-routed PDFs, using `P4-325` as the exact dispatch map

## Audit Result

- no new `sources/registry/` record landed
- no new `facts/` card landed
- no `wiki/` page changed
- tracker wording required refresh

## What This Pass Fixes

- future AI should not keep reopening `1.50 mm` as if the repo still only had a thin standards-existence gap
- future AI should treat the current package residual block as `stronger but still open`, not as `obvious immediate blind-search priority`
- future AI should treat article-side narrow recovery as the default next continuation class unless a genuinely stronger package source appears

## Recommended Next Action

If `/goal` continues from here:

1. use `P4-325` as the dispatch index for article-side narrow recovery
2. prefer controller-routed article PDFs over blind package-residual reopening
3. reopen current package residuals only if a materially stronger owner or standards-adjacent source appears
