# P4-473 1.50 mm Candidate-Gated Scout No-Reopen Successor

Date: 2026-05-11
Parent surfaces:

- `logs/p4-319-2026-5-8-1p50mm-public-exact-geometry-recheck.md`
- `logs/p4-387-2026-5-10-package-residual-live-recheck-no-closeout.md`
- `logs/p4-465-2026-5-11-1p50mm-exact-lane-reaudit-after-iec-family-raise.md`
- `logs/p4-467-2026-5-11-pcb-ziliao-completion-audit-successor-after-nxp-third-owner-0p75mm-raise.md`
- `logs/p4-472-2026-5-11-post-p4-471-residual-rerank-toward-1p50mm-candidate-gated-recovery.md`

Execution mode: `subagent_aided_candidate_gated_negative_scout`

## Purpose

Record one more candidate-gated scout against the current top-priority `1.50 mm` residual after `P4-472`.

This pass is not a reopen.
It checks whether any candidate now clearly exceeds the current `1.50 mm` ceiling strongly enough to justify reopening the lane.

## Candidate Gate Rechecked

The current lane should reopen only if one of the following appears:

1. a third materially independent current-public owner exact row
2. a legitimately public official geometry surface above metadata level

## Current Ceiling Reconfirmed

The current repo-supported `1.50 mm` ceiling remains:

- `IEC 60191-6-2` existence boundary
- `IEC 61188-5-8 / 61188-6-2` standards-family boundary
- one NXP current-public exact row
- one Renesas named-package drawing
- one Renesas current-public exact row

This is the same ceiling already fixed in `P4-465` and carried forward by `P4-467`.

## Candidate Findings

### 1. IEC still does not expose a public official geometry surface

- `IEC 61188-5-8` and `IEC 61188-6-2` remain useful as standards-family framing only.
- Their current public surface is still metadata or webstore-level identity, not a public geometry row.
- This means they do not satisfy the reopen gate for a legitimately public official geometry surface.

### 2. The current Infineon candidate still does not rise above the ceiling

- one Infineon package-page candidate again looked like a possible near-hit because public package identity plus `1.5` pitch wording were visible
- but this pass still did not verify a same-document public PCB land-pattern exact row
- that keeps the candidate below the current `NXP exact row + Renesas exact row` ceiling, matching the earlier caution already preserved in `P4-465`

### 3. The current ADI candidate is still a false positive

- one ADI official BGA PDF surfaced multiple visible `1.50` values
- this pass rechecked the candidate class and found the actual package pitch `e` was `1.00`, not `1.50`
- this keeps the ADI hit inside the already-known false-positive family:
  - body-size numbers
  - contact spacing
  - other package dimensions that are not true `1.50 mm` pitch plus exact land-pattern closure

## Audit Result

- no candidate in this pass clearly exceeded the current `1.50 mm` ceiling
- no new `sources/registry/` record landed
- no new `facts/` card landed
- no `wiki/` route changed
- the safest result is `no reopen`

## What This Pass Fixes

- future AI should not treat `P4-472` as an invitation to reopen `1.50 mm` immediately
- future AI should not mistake current IEC metadata pages for a public official geometry surface
- future AI should not mistake package-page `1.5` wording or ADI false positives for a true third-owner exact-row candidate

## Continuation Rule

Keep `1.50 mm` as the first-priority residual only in the candidate-gated sense.

Do not reopen it again unless a new candidate clearly satisfies one of:

1. a third materially independent current-public owner exact row
2. a legitimately public official geometry surface above metadata level
