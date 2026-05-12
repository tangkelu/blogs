# P4-515 Post P4-514 Residual Priority And Completion Gap Rerank

Date: 2026-05-11
Parent surfaces:

- `logs/p4-503-2026-5-11-completion-audit-successor-after-handbook-nine-route-state.md`
- `logs/p4-514-2026-5-11-nexperia-wlcsp-same-surface-and-1p50-false-positive-no-reopen.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_residual_priority_rerank`

## Purpose

Rerank the remaining open residual lanes after `P4-514`, keeping the scope narrow:

- identify the smallest still-open blockers that continue to prevent `full_corpus_closed_without_open_residual_authority_gaps`
- avoid reopening already-closed false-positive classes
- recommend one bounded next lane only

## Changed Files

- `logs/p4-515-2026-5-11-post-p4-514-residual-priority-and-completion-gap-rerank.md`

## Residual Lanes Checked

### 1. `1.50 mm` package exact-geometry lane

- still the top remaining reopen lane
- `P4-514` removes the current `Nexperia WLCSP` false-positive class from consideration
- `P4-508` keeps the current `Infineon P-BGA / PG-BGA` URLs blocked
- `P4-509` keeps `Amkor PBGA/TEPBGA` below reopen because the page has pitch identity but not same-surface footprint geometry
- `P4-511` and `P4-512` keep visible `1.50` body-size hits from being mistaken for pitch identity
- `P4-513` keeps same-surface pitch-plus-land-pattern hits below reopen when the true pitch is not `1.50`
- `P4-507` and phase status confirm IPC adds a standards-adjacent geometry boundary, but not a closeout row

### 2. `0.75 mm` package-row lane

- still open, but now lower priority than `1.50 mm`
- current notes already show multiple owner-scoped rows and standards-side framing, but not a single clean universal closeout
- this lane remains a blocker, but it is not the best next bounded step because the `1.50 mm` lane still has the tighter and more actionable exact-geometry gap

### 3. `connector-origin` / `installation mark` doctrine lane

- still open as layered support, not universal cross-vendor closure
- the existing support is split across KiCad/Molex/connector-owner context and remains insufficient for full closeout
- this lane should stay watch-only unless a materially stronger package-owner or standards-adjacent authority appears

### 4. `194页 handbook` residual lane

- still below `full_corpus_closed_without_open_residual_authority_gaps`
- `P4-514` confirms the handbook is not the main reopen target
- `RESETn / nPOR` remains a watched overlap case, not a clean new lane

## Recommended Next Lane

Proceed only on this bounded lane:

- current-public owner surface that visibly exposes both true `1.50 mm` pitch identity and same-surface printed PCB land-pattern geometry

Do not reopen the lane through family pages, visible `1.50` body dimensions, access-blocked URLs, or package-information PDFs that do not prove pitch identity on the same surface as the geometry.

## Non-Reopen Filters Used

- `visible 1.50` in body-dimension context is not pitch identity
- same-surface geometry without true `1.50 mm` pitch identity is not enough
- true pitch without same-surface footprint or land-pattern geometry is not enough
- access-blocked URLs are blocked candidates only
- family-page availability alone is not a reopen signal
- owner-scoped false positives already closed by `P4-514` stay closed

## Rerank Result

- `1.50 mm` exact-geometry recovery remains the highest-priority open residual lane
- `0.75 mm` remains open but secondary
- doctrine and handbook lanes remain below the package-side exact-geometry gap in reopen priority

## Completion Gap Note

The repo still does not satisfy `full_corpus_closed_without_open_residual_authority_gaps`.

The smallest meaningful remaining gap is still on the package side: a genuine public owner surface with both true `1.50 mm` pitch identity and same-surface footprint or land-pattern geometry.
