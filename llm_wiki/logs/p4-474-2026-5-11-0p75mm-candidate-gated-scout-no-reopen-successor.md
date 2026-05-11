# P4-474 0.75 mm Candidate-Gated Scout No-Reopen Successor

Date: 2026-05-11
Parent surfaces:

- `logs/p4-389-2026-5-10-renesas-second-owner-0p75mm-package-land-pattern-boundary.md`
- `logs/p4-400-2026-5-10-renesas-second-owner-0p75mm-exact-data-page-landing.md`
- `logs/p4-466-2026-5-11-nxp-third-owner-0p75mm-reflow-footprint-landing.md`
- `logs/p4-467-2026-5-11-pcb-ziliao-completion-audit-successor-after-nxp-third-owner-0p75mm-raise.md`
- `logs/p4-472-2026-5-11-post-p4-471-residual-rerank-toward-1p50mm-candidate-gated-recovery.md`

Execution mode: `subagent_aided_candidate_gated_negative_scout`

## Purpose

Record one candidate-gated scout against the current second-priority `0.75 mm` residual.

This pass is not a reopen.
It checks whether any current candidate clearly exceeds the `0.75 mm` ceiling strongly enough to justify another landing wave.

## Candidate Gate Rechecked

The current lane should reopen only if one of the following appears:

1. a fourth materially stronger current-public owner exact row
2. a legitimately public standards geometry surface above the current family-boundary level

## Current Ceiling Reconfirmed

The current repo-supported `0.75 mm` ceiling remains:

- three Microchip current-public exact rows
- one Renesas second-owner exact-data page
- one NXP third-owner exact-data page

This is the same ceiling already fixed in `P4-467`.

## Candidate Findings

### 1. Current NXP general-BGA guidance does not create a fourth `0.75 mm` owner exact row

- one already-known NXP guidance class remains useful for named pitch families such as `1.0 / 0.8 / 0.65 / 0.5 mm`
- this pass did not find a true `0.75 mm` row in that NXP public guidance class
- this means it does not satisfy the gate for a fourth materially stronger `0.75 mm` owner exact row

### 2. IEC still does not expose a public `0.75 mm` geometry surface

- the current IEC public surface remains at metadata and family-boundary level
- this is still useful for standards-family framing
- it is not a legitimately public exact `0.75 mm` geometry row and therefore does not justify reopening the lane

### 3. Current Renesas common-pitch material does not rise above the present ceiling

- Renesas common-pitch material can still confirm a `0.75` row inside the same vendor family
- but this does not create a fourth owner
- and it does not exceed the current `Microchip x3 + Renesas + NXP` multi-owner ceiling strongly enough to justify a new landing on its own

## Audit Result

- no candidate in this pass clearly exceeded the current `0.75 mm` ceiling
- no new `sources/registry/` record landed
- no new `facts/` card landed
- no `wiki/` route changed
- the safest result is `no reopen`

## What This Pass Fixes

- future AI should not treat `0.75 mm` as if another obvious owner exact row is already sitting just below the current repo surface
- future AI should not mistake current IEC metadata for a public standards geometry row
- future AI should not reopen the lane on another same-owner or not-actually-`0.75 mm` candidate that fails to exceed the `P4-467` ceiling

## Continuation Rule

Keep `0.75 mm` as a watch-only residual below `1.50 mm`.

Do not reopen it again unless a new candidate clearly satisfies one of:

1. a fourth materially stronger current-public owner exact row
2. a legitimately public standards geometry surface above the current family-boundary layer
