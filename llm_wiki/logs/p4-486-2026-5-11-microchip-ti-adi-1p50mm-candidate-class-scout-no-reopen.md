# P4-486 Microchip TI ADI 1.50 mm Candidate-Class Scout No-Reopen

Date: 2026-05-11
Parent surfaces:

- `logs/p4-485-2026-5-11-infineon-package-portal-1p50mm-candidate-false-positive-no-reopen.md`
- `logs/p4-480-2026-5-11-completion-audit-successor-after-amd-third-owner-1p50mm-raise.md`
- `logs/p4-484-2026-5-11-completion-audit-successor-after-altium-cad-owner-doctrine-raise.md`

Execution mode: `subagent_aided_candidate_gated_negative_scout`

## Purpose

Record one bounded scout across three additional official owner-source classes that looked structurally plausible for the still-open `1.50 mm` residual lane.

This pass is not a reopen.
It checks whether current-public Microchip, TI, or ADI package-guideline classes actually expose a new `1.50 mm` owner exact row above the current `NXP + Renesas + AMD` ceiling.

## Candidate Gate Rechecked

The current lane should reopen only if one of the following appears:

1. a new materially stronger current-public owner exact row
2. a legitimately public official geometry surface above metadata level

## Candidate Classes Rechecked

1. Microchip official BGA rule-table class
2. TI official MicroStar or package-guideline class
3. ADI official BGA package-guideline class

## Findings

### 1. Current-public Microchip rule-table class stays below reopen

- the rechecked Microchip official BGA rule-table surface is structurally real and current-public
- but the visible pitch rows remain:
  - `1.0 mm`
  - `0.8 mm`
  - `0.5 mm`
- this means the current surfaced Microchip public class does not provide:
  - a true `1.50 mm` owner exact row
  - a stronger `1.50 mm` package-owner geometry surface

### 2. Current-public TI MicroStar guide also stays below reopen

- the rechecked TI `MicroStar BGA Packaging Reference Guide` is a real owner-guidance class with package appendices and PCB-design framing
- but the visible package-pitch coverage in the rechecked current-public guide remains limited to:
  - `0.5 mm`
  - `0.8 mm`
  - `1.0 mm`
- this keeps the current surfaced TI class below reopen for the `1.50 mm` residual lane

### 3. Current-public ADI BGA guideline class is still generic or coordinate-hit noise

- the rechecked ADI app-note class is real and current-public
- but the visible public page supports:
  - generic BGA PCB design guidance
  - generic NSMD/SMD and stencil/process framing
- it does not itself expose one public `1.50 mm` owner exact row
- this keeps the current ADI class inside the already-known false-positive family:
  - generic package-guideline prose
  - or package PDFs where visible `1.50` values do not become true `e = 1.50 mm` exact-lane closure

### 4. The safest result remains `no reopen`

- Microchip does not add a `1.50 mm` row from the current surfaced public class
- TI does not add a `1.50 mm` row from the rechecked MicroStar guide class
- ADI does not add a `1.50 mm` row from the current surfaced public guideline class
- the repo-supported `1.50 mm` ceiling therefore still remains:
  - `IEC 60191-6-2` existence boundary
  - `IEC 61188-5-8 / 61188-6-2` standards-family boundary
  - one NXP current-public exact row
  - one Renesas named-package drawing
  - one Renesas current-public exact row
  - one AMD-hosted third-owner exact row

## Audit Result

- no new `sources/registry/` record landed
- no new `facts/` card landed
- no `wiki/` route changed
- no completion threshold changed
- the safest result is `no reopen`

## What This Pass Fixes

- future AI should not reopen `1.50 mm` on the current surfaced Microchip rule-table class alone
- future AI should not treat the current-public TI MicroStar guide as if it already contains a `1.50 mm` exact row
- future AI should not treat the current surfaced ADI BGA-guideline class as package-exact closure
- future AI should keep reserving reopen for a source that really exposes a true `1.50 mm` owner exact row or public standards geometry surface

## Continuation Rule

Keep `1.50 mm` as a watch-only residual under the same candidate-gated standard.

The next strongest current-public owner candidate class to watch remains:

1. owner-controlled package portal or package drawing surfaces that visibly show a true `1.50 mm` pitch identity
2. and printed PCB land-pattern geometry in the same public owner surface
