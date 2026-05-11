# P4-475 Doctrine Residual Candidate Scout No-Reopen Successor

Date: 2026-05-11
Parent surfaces:

- `logs/p4-463-2026-5-11-package-nonbga-marking-origin-reaudit-and-no-write-closeout.md`
- `logs/p4-467-2026-5-11-pcb-ziliao-completion-audit-successor-after-nxp-third-owner-0p75mm-raise.md`
- `facts/methods/connector-origin-and-installation-mark-boundary.md`
- `facts/methods/iec-zero-orientation-cad-library-construction-boundary.md`
- `facts/methods/iec-smd-component-marking-boundary.md`

Execution mode: `subagent_aided_doctrine_candidate_gated_negative_scout`

## Purpose

Record one candidate-gated scout against the remaining doctrine-side residuals after the package residual negative scouts.

This pass does not reopen the lane.
It checks whether the current doctrine residuals now have any clearly stronger candidate above the existing `KiCad + owner drawings + IEC` ceiling.

## Doctrine Residuals Rechecked

1. `connector-origin universal doctrine`
2. `board-level installation-mark geometry`
3. stronger package-family-specific or connector-family-specific marking rule above the current ceiling

## Current Ceiling Reconfirmed

The current doctrine ceiling remains:

- `connector-origin = KiCad + Molex + Samtec + Amphenol layered support`
- `installation-mark / component-marking = layered support + IEC zero-orientation + IEC pin-1 / polarity route`

This is the same ceiling already fixed by `P4-463` and carried forward in `P4-467`.

## Candidate Findings

### 1. Current IEC support still stays below doctrine closeout

- `IEC 61188-7` still supports orientation-description and CAD-library construction framing
- `IEC 61760-1` still supports `pin-1` and polarity-identification framing
- neither current public IEC surface closes:
  - universal connector-origin doctrine
  - board-level installation-mark geometry
  - universal symbol or layer rule

### 2. Current KiCad/KLC support still stays at CAD-owner convention level

- `KiCad KLC` remains useful as CAD-owner library convention
- it still does not rise to:
  - standards-owner doctrine
  - cross-family connector-origin rule
  - board-level installation-mark geometry rule

### 3. Current connector-owner material still stays at named-family context

- current Molex, Samtec, and Amphenol support still remains named-series layout and `pin-1` context
- one additional public TE candidate class still stays at named-family guidance only
- none of these sources create:
  - one universal connector-origin doctrine
  - one cross-family symbol or layer doctrine
  - one board-level installation-mark geometry rule

### 4. Current package-owner marking material still does not raise the doctrine ceiling

- source classes such as part-identity or resistor-marking guides can help with device-family identity
- they do not create the still-missing doctrine surfaces for the residuals named above
- this keeps them below the reopen threshold for the current doctrine lane

## Audit Result

- no candidate in this pass clearly exceeded the current doctrine ceiling
- no new `sources/registry/` record landed
- no new `facts/` card landed
- no `wiki/` route changed
- the safest result is `no reopen`

## What This Pass Fixes

- future AI should not keep treating the current doctrine residuals as if a stronger public source is already known but merely unlanded
- future AI should not mistake current IEC framing, KiCad convention, TE named-family guidance, or device-marking guides for doctrine-level closure
- current continuation can now describe both remaining doctrine residuals more honestly as `still open in theory, but no reopen from current candidates`

## Continuation Rule

Keep the current doctrine residuals as watch-only residuals below the package residual block.

Do not reopen them again unless a new candidate clearly satisfies one of:

1. a stronger standards-owner doctrine for connector-origin or installation-mark geometry
2. a stronger CAD-owner doctrine above `KLC` convention level
3. a cross-family connector-owner or package-owner rule that truly exceeds the current named-series ceiling
