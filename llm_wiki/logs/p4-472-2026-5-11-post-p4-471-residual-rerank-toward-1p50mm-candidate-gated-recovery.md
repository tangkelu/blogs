# P4-472 Post-P4-471 Residual Rerank Toward 1.50 mm Candidate-Gated Recovery

Date: 2026-05-11
Parent surfaces:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/p4-458-2026-5-11-e7-residual-route-reaudit-and-no-write-closeout.md`
- `logs/p4-460-2026-5-11-e4-mark-fiducial-route-reaudit-and-no-write-closeout.md`
- `logs/p4-461-2026-5-11-post-e4-article-residual-exhaustion-rerank.md`
- `logs/p4-463-2026-5-11-package-nonbga-marking-origin-reaudit-and-no-write-closeout.md`
- `logs/p4-465-2026-5-11-1p50mm-exact-lane-reaudit-after-iec-family-raise.md`
- `logs/p4-467-2026-5-11-pcb-ziliao-completion-audit-successor-after-nxp-third-owner-0p75mm-raise.md`
- `logs/p4-471-2026-5-11-194-page-handbook-four-route-successor-no-write-closeout.md`

Execution mode: `subagent_aided_controller_rerank`

## Purpose

Refresh the next continuation priority after the `194页 handbook` four-route closeout in `P4-471`.

This pass does not land new `sources/`, `facts/`, or `wiki/`.
It only records the cleanest next residual order so future AI does not fall back to broad handbook rereads, re-audited article residuals, or blind package searching.

## Rechecked Surfaces

1. article residual truth after `P4-458`, `P4-460`, and `P4-461`
2. non-BGA doctrine residual truth after `P4-463`
3. package exact-data residual truth after `P4-465` and `P4-467`
4. handbook residual truth after `P4-471`

## Findings

### 1. The current article residual set is not the best restart class

- `P4-461` already records that the remaining article residual set is re-audited closed at the current authority layer.
- The current `E4 Mark` and `E7` residuals therefore do not justify default continuation pressure unless genuinely new authority appears.

### 2. The current non-BGA doctrine residual is also not the best restart class

- `P4-463` already re-audited the current `connector-origin / installation-mark / visible-vs-fab cue` lane closed on the present `KiCad + owner drawings + IEC + local handbook` stack.
- That residual remains open only in the narrow sense of missing stronger universal doctrine, not in the sense of a likely near-term missed route.

### 3. The cleanest next reopen candidate is now `1.50 mm`

- `P4-465` records that `1.50 mm` is materially stronger than `IEC 60191-6-2 existence only`, because the repo now also has:
  - `IEC 61188-5-8 / 61188-6-2` standards-family framing
  - one NXP current-public exact row
  - one Renesas named-package drawing
  - one Renesas current-public exact row
- `P4-465` also records the exact missing step:
  - a third materially independent current-public owner exact row
  - or a legitimately public official geometry surface
- That means one strong candidate could still materially raise the ceiling, but only if it clearly exceeds the current stack before landing.

### 4. `0.75 mm` remains open, but now ranks below `1.50 mm`

- `P4-467` records that `0.75 mm` already sits at:
  - three Microchip exact rows
  - one Renesas second-owner exact-data page
  - one NXP third-owner exact-data page
- This is still not universal closeout.
- It does mean the marginal value of another routine scout is now lower than for `1.50 mm`, unless a clearly stronger fourth-owner or public standards geometry candidate appears.

### 5. The next-action rule must now be `candidate-gated`, not `blind-search-first`

- `1.50 mm` is the best current reopen candidate.
- It is not an open invitation to re-search the whole web or reopen every package page that contains `1.5 mm`.
- Reopening should happen only after a candidate visibly clears the `P4-465` bar.

## Audit Result

- no new residual lane was landed
- no per-PDF state changed
- tracker wording required refresh because the next continuation order is now sharper than the existing generic residual wording

## Recommended Residual Order

If `/goal` continues from here, use this order:

1. `1.50 mm` package exact-geometry residual
   - but only as `candidate-gated recovery`
   - reopen only if a candidate looks like:
     - a third materially independent current-public owner exact row
     - or a legitimately public official geometry surface
2. `0.75 mm` package exact-data residual
   - only if a candidate clearly exceeds the current `Microchip x3 + Renesas + NXP` ceiling
3. `connector-origin / installation-mark` universal-doctrine residual
   - only if a stronger standards-owner, CAD-owner, package-owner, or connector-owner doctrine source appears

## What This Pass Fixes

- future AI should not keep using broad residual wording after `P4-471`
- future AI should not reopen article residuals or the `194页 handbook` by default
- future AI should treat `1.50 mm` as the first reopen candidate, but with a hard candidate gate rather than blind search
