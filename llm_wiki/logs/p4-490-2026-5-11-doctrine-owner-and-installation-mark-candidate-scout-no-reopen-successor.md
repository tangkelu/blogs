# P4-490 Doctrine Owner And Installation-Mark Candidate Scout No-Reopen Successor

Date: 2026-05-11
Parent surfaces:

- `logs/p4-475-2026-5-11-doctrine-residual-candidate-scout-no-reopen-successor.md`
- `logs/p4-483-2026-5-11-altium-cad-owner-footprint-reference-point-and-layer-boundary.md`
- `logs/p4-488-2026-5-11-completion-audit-successor-after-iec-square-bga-family-raise.md`

Execution mode: `subagent_aided_doctrine_candidate_gated_negative_scout`

## Purpose

Record one more bounded scout against the still-open doctrine-side residuals after `P4-489`.

This pass does not reopen the lane.
It checks whether newly surfaced current-public owner, CAD-owner, or standards-side candidates now clear the current doctrine ceiling for:

1. `connector-origin universal doctrine`
2. `board-level installation-mark geometry`

## Candidate Gate Rechecked

The current doctrine lane should reopen only if one of the following appears:

1. a stronger standards-owner doctrine for connector-origin or installation-mark geometry
2. a stronger CAD-owner doctrine above the current `KiCad + Altium` construction ceiling
3. a cross-family connector-owner or package-owner rule that truly exceeds the current named-series ceiling

## Candidate Classes Rechecked

### Connector-origin side

1. Hirose current-public connector product pages with owner-hosted `2D` and ECAD footprint assets
2. TE Connectivity current-public product pages with drawings, CAD files, and explicit design-activity note
3. Samtec current-public product pages and model disclaimers
4. Cadence public footprint-guidance prose as a CAD-owner / process-owner comparison surface

### Installation-mark and board-level marking side

1. IPC `7351` public TOC and scope surface
2. IEC `61188-6-1:2021` public preview
3. IEC `61191-1:2018` official metadata page
4. Altium public documentation for assembly/documentation layer objects
5. Cadence public silkscreen-versus-assembly-layer guidance

## Findings

### 1. No new connector-origin surface exceeds the current `KiCad + Molex + Samtec + Amphenol` ceiling

- Hirose is the strongest new connector-owner near-hit because it publicly exposes owner-hosted `2D`, `3D`, and ECAD footprint assets across multiple connector families
- TE also strengthens the `use owner drawing for named part` posture because its public product pages expose product drawings, CAD files, and an explicit `Use the Product Drawing for all design activity` note
- but neither Hirose nor TE publicly exposes one reusable cross-family doctrine that clearly states:
  - recommended PCB layout origin
  - origin datum
  - universal `pin-1` orientation handling
- Samtec remains strong per-series authority but still bounded by its series-print confirmation rule and public model disclaimers
- Cadence remains generic footprint/process guidance rather than connector-owner or standards-owner doctrine

### 2. No new board-level installation-mark or placement-marking surface exceeds the current layered ceiling

- IPC `7351` is the strongest standards-side near-hit from this pass because the current public TOC/scope proves internal coverage for:
  - marking
  - zero component orientations
  - courtyard
  - orientation
  - fiducials
  - mounting-condition topics such as solder mask, paste stencil, keepout areas, and adjacent-component clearance
- but the visible public IPC surface still does not expose one clause, figure rule, or normative wording that safely authorizes:
  - one board-level installation-mark geometry doctrine
  - one universal component-placement marking construction
  - one universal layer or symbol default
- `IEC 61188-6-1:2021` public preview remains at generic land-pattern-requirement framing rather than placement-mark geometry doctrine
- `IEC 61191-1:2018` metadata remains useful only as assembly-documentation framing, not public geometry doctrine
- Altium and Cadence remain useful CAD-owner construction surfaces, but they do not rise to one standards-grade universal board-level marking law

### 3. The safest result remains `no reopen`

- no new connector-owner, CAD-owner, or standards-side public surface clearly exceeded the current doctrine ceiling
- the repo-supported doctrine ceiling therefore still remains:
  - `connector-origin = KiCad + Molex + Samtec + Amphenol layered support`
  - `installation-mark / component-marking = layered support + IEC zero-orientation + IEC pin-1 / polarity route`
  - `CAD-owner footprint doctrine = KiCad + Altium cross-tool support for reference-point handling and visible/documentation layer-role separation`

## Audit Result

- no new `sources/registry/` record landed
- no new `facts/` card landed
- no `wiki/` route changed
- no completion threshold changed
- the safest result is `no reopen`

## What This Pass Fixes

- future AI should not treat Hirose cross-family owner ECAD availability as if it already closes universal connector-origin doctrine
- future AI should not treat TE product-page drawing and CAD access as if named-part design-activity wording already becomes cross-family connector-origin doctrine
- future AI should not treat public `IPC-7351` TOC/scope visibility as if it already exposes one citable board-level installation-mark geometry rule
- future AI should not overpromote Altium or Cadence layer-object guidance into universal standards-owner installation-mark geometry doctrine

## Continuation Rule

Keep the current doctrine residuals as watch-only residuals below the package residual block.

Do not reopen them again unless a future pass recovers either:

1. a stronger current-public standards-owner doctrine for connector-origin or board-level installation-mark geometry
2. a stronger cross-family connector-owner rule that truly exceeds current named-series and per-part asset support
3. one current-public primary surface that actually exposes normative geometry or symbol-construction wording above the current layered ceiling
