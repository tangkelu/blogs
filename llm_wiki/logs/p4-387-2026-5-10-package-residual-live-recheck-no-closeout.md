# P4-387 Package Residual Live Recheck No-Closeout

Date: 2026-05-10
Parent surfaces:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-315-2026-5-8-package-residual-authority-recovery.md`
- `logs/p4-317-2026-5-8-connector-origin-and-installation-mark-boundary-landing.md`
- `logs/p4-318-2026-5-8-iec-1p50mm-bga-standards-existence-boundary.md`
- `logs/p4-319-2026-5-8-1p50mm-public-exact-geometry-recheck.md`
- `logs/p4-322-2026-5-8-samtec-connector-owner-layout-route-landing.md`
- `logs/p4-323-2026-5-8-1p50mm-search-filter-note.md`
- `logs/p4-329-2026-5-9-1p50mm-nxp-legacy-pbga-route.md`
- `logs/p4-386-2026-5-10-pcb-ziliao-residual-route-audit-and-no-write-closeout.md`

Execution mode: `subagent_aided_live_public_recheck`

## Purpose

Record one fresh current-public recheck against the still-open `package` residual authority gaps after the residual-route audit.

This pass is not a new landing wave.
It is a freshness check for whether any of the remaining residual package lanes can now be safely closed.

## Rechecked Lanes

1. public exact-geometry recovery for residual handbook pitch class `1.50 mm`
2. stronger current-public source class for residual handbook pitch class `0.75 mm`
3. stronger public authority for `connector-origin defaulting`
4. stronger public authority for `installation-mark conventions`

## What This Pass Reconfirmed

### 1. `1.50 mm` still has no clean current-public exact-geometry closeout

- the current repo still only supports three levels for this lane:
  - `P4-318` standards-owner existence and scope
  - `P4-329` one current-public owner-scoped near-hit through legacy `PBGA` guidance
  - `P4-323` false-positive filter requiring a real `Pitch = 1.50 BSC` plus printed land-pattern geometry in the same owner document
- the fresh public search surface still does not produce one stronger named-package owner row above that ceiling
- high-frequency public hits still include false positives where `1.50` belongs to body size, contact-pad spacing, total span, or non-BGA package dimensions rather than true `1.50 mm` pitch closure
- the best currently preserved owner-scoped near-hit remains `AN1231`, and it still stays below clean exact-geometry closure because it is legacy family guidance and explicitly requires package-specific diameter confirmation before layout

### 2. `0.75 mm` still stops at three Microchip owner-scoped rows

- the current repo still only supports this lane at:
  - three official Microchip named-package `0.75 BSC` rows
  - package-scoped exact-data cards tied to those named drawings
- no stronger current-public second-owner drawing was identified that exposes both:
  - a real `0.75 BSC` package-pitch row
  - and a printed PCB land-pattern row in the same document
- package-identity pages from other owners can confirm that `0.75 mm` package families exist, but they still do not strengthen generic admissible wording because they do not add package-owner land-pattern geometry
- the current safe ceiling therefore remains `three owner-scoped Microchip rows`, not cross-vendor or standards-adjacent closeout

### 3. `connector-origin defaulting` still stops at layered boundary support

- the strongest current admissible layer remains:
  - KiCad `KLC` as CAD-owner library convention
  - Molex named-series owner drawing
  - Samtec named-series owner drawing
- no stronger current-public cross-vendor or standards-grade source was identified that would safely upgrade this lane into a universal connector-origin rule

### 4. `installation-mark conventions` still stop at layered boundary support

- the current fact layer already preserves the highest safe reusable wording found so far:
  - visible `pin-1` / polarity cue on documentation or assembly-facing layers
  - `F.Fab`-style documentation cue for footprint definition
  - exact geometry only when attached to a named owner series drawing
- no current-public standards-grade doctrine was identified that would safely authorize one universal installation-mark geometry or default across connector families

## Controller Result

- no new `sources/registry/` record landed
- no new `facts/` card landed
- no `wiki/` route changed
- no residual package lane changed state

## What This Pass Fixes

- future AI should treat the current residual package gaps as freshly rechecked on `2026-05-10`, not as stale gaps that obviously just need another immediate blind search
- the current continuation order stays accurate:
  - keep `1.50 mm` open only for a genuinely stronger owner document
  - keep `0.75 mm` open only for a genuinely stronger second-owner or standards-adjacent geometry source
  - keep connector-origin and installation-mark residuals open only for a materially stronger cross-vendor or standards-adjacent source

## Continuation Rule

Only reopen these lanes if one of the following appears:

1. a current-public owner document that exposes both a real `1.50 BSC` package-pitch row and printed PCB land-pattern geometry
2. a current-public second-owner document that exposes both a real `0.75 BSC` package-pitch row and printed PCB land-pattern geometry
3. a current-public source class stronger than `KiCad + Molex + Samtec` for generic connector-origin wording
4. a current-public source class stronger than the current layered boundary for installation-mark wording
