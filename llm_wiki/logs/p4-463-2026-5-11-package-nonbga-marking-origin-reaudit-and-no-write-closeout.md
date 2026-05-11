# P4-463 Package Non-BGA Marking/Origin Re-Audit And No-Write Closeout

Date: 2026-05-11
Parent surfaces:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/p4-317-2026-5-8-connector-origin-and-installation-mark-boundary-landing.md`
- `logs/p4-322-2026-5-8-samtec-connector-owner-layout-route-landing.md`
- `logs/p4-393-2026-5-10-amphenol-connector-owner-layout-route.md`
- `facts/methods/connector-origin-and-installation-mark-boundary.md`
- `facts/methods/iec-zero-orientation-cad-library-construction-boundary.md`
- `facts/methods/iec-smd-component-marking-boundary.md`
- `facts/local_pdf/pin1-origin-installation-mark-visual-boundary.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`

Execution mode: `subagent_aided_non_article_residual_reaudit`

## Purpose

Re-audit whether the current non-BGA `connector-origin / installation-mark / visible-vs-fab cue` lane can be promoted above its present fact layer using the already-landed `KiCad + connector-owner + IEC + local handbook` source set.

This pass is an audit only.
It does not assume that more careful wording on the same source set automatically creates a genuinely new authority surface.

## Audit Scope

1. current fact and wiki layer
   - `facts/methods/connector-origin-and-installation-mark-boundary.md`
   - `facts/methods/iec-zero-orientation-cad-library-construction-boundary.md`
   - `facts/methods/iec-smd-component-marking-boundary.md`
   - `facts/local_pdf/pin1-origin-installation-mark-visual-boundary.md`
   - `wiki/processes/package-library-governance-and-footprint-review-map.md`
2. parent route landings
   - `P4-317`
   - `P4-322`
   - `P4-393`
3. candidate residual sub-surface rechecked
   - whether `visible cue` versus `F.Fab` documentation cue is still unlanded
   - whether the latest owner-drawing and IEC anchors create a new generic doctrine beyond the current cards

## Findings

### 1. The current repo has already absorbed the clean visible-versus-fabrication cue split

- `P4-317` already landed the safe KLC split between:
  - visible `F.SilkS` or `pin-1` designator cue
  - `F.Fab` pin-1 location or small-arrow documentation cue
- `facts/methods/connector-origin-and-installation-mark-boundary.md` already preserves that split as the reusable ceiling for the current KLC-backed cue layer.
- This means `visible cue versus F.Fab cue` is not an unlanded gap in the current repo.

### 2. The later owner-drawing and IEC raises do not create a new generic doctrine

- `P4-322` and `P4-393` only add more named-series connector-owner drawings.
- Those drawings strengthen the rule `use owner drawing for named connector family`, but they do not create:
  - universal connector-origin defaulting
  - board-level installation-mark geometry
  - cross-family symbol or layer doctrine
- `IEC 61188-7` keeps `zero orientation` inside CAD-library construction and orientation-description technique.
- `IEC 61760-1` keeps `pin-1` and polarity-identification inside controlled component-specification framing.
- Neither IEC surface cleanly closes visible-mark geometry, symbol choice, layer-specific rule closure, or board-level installation-mark doctrine.

### 3. The safest result is a no-write closeout at the current source layer

- no new `facts/`, `wiki/`, or `sources/registry/` files were admitted in this pass
- the current non-BGA marking/origin lane remains correctly indexed as:
  - `KiCad/KLC` for CAD-library convention
  - `Molex / Samtec / Amphenol` for named-series owner layout context
  - `IEC 61188-7` for zero-orientation library-construction framing
  - `IEC 61760-1` for component-marking topic framing
- the current repo still does not have a clean authority surface for:
  - universal connector-origin doctrine
  - board-level installation-mark geometry
  - universal visible-mark or fabrication-mark symbol/layer rule

## Audit Result

- no new non-BGA package authority lane was admitted
- no per-file status in `P4-325` changed
- current package residual wording needed tracker refresh, not another fact promotion
- the current `connector-origin / installation-mark / visible-vs-fab cue` lane is now explicitly re-audited closed at the present source layer

## What This Audit Fixes

- future AI should not reopen the current `KiCad + Molex/Samtec/Amphenol + IEC + local handbook` set expecting one missed narrow authority raise
- future AI should not treat `visible cue versus F.Fab cue` as an unlanded residual, because that split is already absorbed in the current fact layer
- the repo now records a more exact reopen condition for this non-BGA residual lane

## Recommended Next Action

If `/goal` continues from here:

1. do not reopen the current non-BGA `connector-origin / installation-mark / visible-vs-fab cue` lane on the present source set alone
2. reopen it only if a materially stronger standards-owner, CAD-owner, package-owner, or connector-owner source explicitly closes one still-open surface such as universal connector-origin doctrine, board-level installation-mark geometry, or layer/symbol-specific marking rules
3. otherwise shift continuation pressure to other residual authority gaps rather than rephrasing the same KLC, owner-drawing, and IEC anchors again
