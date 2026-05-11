# P4-465 1.50 mm Exact Lane Re-Audit After IEC Family Raise

Date: 2026-05-11
Parent surfaces:

- `logs/p4-319-2026-5-8-1p50mm-public-exact-geometry-recheck.md`
- `logs/p4-387-2026-5-10-package-residual-live-recheck-no-closeout.md`
- `logs/p4-399-2026-5-10-pcb-ziliao-completion-audit-successor-after-second-owner-1p50mm-raise.md`
- `logs/p4-401-2026-5-10-pcb-ziliao-completion-audit-successor-after-renesas-0p75mm-exact-data-raise.md`
- `logs/p4-459-2026-5-11-pcb-ziliao-continuation-rerank-and-tracker-correction.md`
- `logs/p4-464-2026-5-11-iec-area-array-land-pattern-family-boundary.md`
- `facts/methods/bga-1p50mm-pitch-standards-existence-boundary.md`
- `facts/methods/iec-area-array-land-pattern-geometry-family-boundary.md`
- `facts/methods/nxp-1p50mm-bga225-reflow-footprint.md`
- `facts/methods/renesas-1p50mm-bga-package-drawing-prbg0225cb-a.md`
- `facts/methods/renesas-1p50mm-bga-lga-mount-pad-dimensions-row.md`

Execution mode: `subagent_aided_non_article_residual_reaudit`

## Purpose

Re-audit whether the `1.50 mm` package lane is now ready for exact-lane closeout after the new IEC family-boundary raise in `P4-464`.

This pass is an audit only.
It distinguishes two separate questions:

1. did `P4-464` materially improve the standards-side framing?
2. did anything in the fresh scout or new standards pages actually close the still-open public exact-geometry lane?

## Audit Scope

1. current in-repo `1.50 mm` stack
   - `IEC 60191-6-2` existence boundary
   - `IEC 61188-5-8 / 61188-6-2` area-array and land-pattern family boundary
   - one NXP current-public exact row
   - one Renesas named-package drawing
   - one Renesas current-public exact row
2. fresh scout result
   - no clearly stronger third independent current-public owner exact row
   - one optional `IEC 61188-5-8` standards-side raise
   - no new public exact `1.50 mm` standards geometry surface

## Findings

### 1. `P4-464` is a real standards-side raise

- the repo no longer stops at `IEC 60191-6-2` coarse-pitch package-guide existence
- the repo now also has one official standards-owner metadata boundary that area-array land-pattern geometry is a formal IEC topic
- this is materially stronger than the old `existence only` wording

### 2. The exact lane is still not closed

- the fresh scout still did not recover a clearly stronger third independent current-public owner exact row
- the new IEC metadata pages still do not expose:
  - a public `1.50 mm` pad-diameter row
  - a public `1.50 mm` solder-mask row
  - a public exact BGA/LGA land-pattern row that can replace the blocked handbook geometry
- one optional Infineon package-page candidate did not rise high enough:
  - public page identity plus `1.5 mm` terminal-pitch wording were visible
  - but no directly verified public footprint geometry row was obtained in this pass
  - this stays below the current `NXP exact row + Renesas exact row` ceiling

### 3. The safest result is a no-write exact-lane closeout successor

- `1.50 mm` should now be described as:
  - `IEC 60191-6-2` existence boundary
  - `IEC 61188-5-8 / 61188-6-2` standards-family boundary
  - one NXP current-public exact row
  - one Renesas named-package drawing
  - one Renesas current-public exact row
- this is stronger than the pre-`P4-464` ceiling
- it is still not a universal or public exact-lane closeout

## Audit Result

- no new `sources/registry/` record landed in this pass
- no new `facts/` card landed in this pass
- no `wiki/` route changed in this pass
- the `1.50 mm` standards-side ceiling is now higher, but the exact lane remains intentionally open

## What This Audit Fixes

- future AI should not reopen `1.50 mm` as if the repo still only had `IEC 60191-6-2 existence only`
- future AI should not claim that `P4-464` closed the exact-data lane
- future AI should reopen `1.50 mm` only for:
  - a third materially independent current-public owner exact row
  - or a legitimately public official geometry surface above metadata level

## Recommended Next Action

If `/goal` continues from here:

1. keep using `P4-464` for standards-family framing
2. keep using the existing NXP and Renesas cards for exact owner-scoped data
3. do not blind-search `1.50 mm` again unless a candidate clearly exceeds the current ceiling before landing
