---
fact_id: "methods-cad-owner-footprint-reference-point-and-layer-role-boundary"
title: "CAD-owner footprint reference point and layer-role support is reusable only as tool-owned construction boundary, not universal package doctrine"
topic: "CAD-owner footprint reference point and layer-role boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-11"
exact_data_class: "boundary_convention"
scope_type: "cad_owner_footprint_construction_boundary"
canonical_unit_policy: "Preserve original tool-owner wording such as reference point, Set Reference, Top Overlay, mechanical layers, courtyard, designator, comment, F.SilkS, and F.Fab. Do not normalize these into one universal connector-origin doctrine, one mandatory pin-1 origin rule, or one universal installation-mark geometry law."
source_ids:
  - "kicad-library-conventions-footprint-orientation-and-marking"
  - "altium-designer-pcb-footprint-reference-point-and-layer-boundary"
tags: ["cad-owner", "footprint", "reference-point", "origin", "overlay", "mechanical-layer", "pin-1", "courtyard", "library-convention"]
---

# Canonical Summary

> Current official CAD-owner support is strong enough to promote one narrow cross-tool boundary card for footprint construction. KiCad `KLC` gives guarded library conventions for `pin-1`, `F.SilkS`, `F.Fab`, and some connector-orientation defaults, while official Altium documentation shows that footprint construction is organized around a configurable `reference point` and separated layer/object roles such as overlay, courtyard/body documentation, and designator/comment objects. Together these sources support a safer rule: footprint origin and visible/documentation marking should be treated as controlled CAD-library construction choices with tool-owner conventions. They do not support one universal connector-origin doctrine, one mandatory `pin-1` origin across all package families, or one board-level installation-mark geometry law.

## Stable Facts

- KiCad `KLC` treats footprint orientation and `pin-1` marking as official library conventions, not universal package law.
- KiCad expects visible polarity or `pin-1` marking on `F.SilkS`.
- KiCad expects `pin-1` location to be documented on `F.Fab`, and for connectors a small arrow indicator next to `pin-1` should be used there.
- KiCad states through-hole footprint anchors should be placed at the location of `pin 1`.
- Official Altium footprint-construction documentation builds the footprint around a workspace `reference point`.
- Official Altium documentation states the footprint reference point can be changed with `Set Reference`.
- Official Altium documentation shows layer/object role separation between visible overlay graphics, mechanical/body-or-courtyard documentation, and `Designator and Comment` objects.
- Official Altium documentation therefore supports guarded wording that origin handling and visible/documentation marks are controlled CAD-library construction choices rather than one universal package truth.

## Conditions And Methods

- Use this card when a prompt needs guarded wording about footprint-origin handling, visible cue placement, documentation-layer separation, or CAD-library construction posture.
- Use KiCad for explicit `pin-1`, `F.SilkS`, `F.Fab`, and through-hole-anchor convention language.
- Use Altium for explicit `reference point`, `Set Reference`, and layer/object role separation language.
- Treat the safe reusable rule as:
  - footprint origin should be intentionally chosen and documented inside the library workflow rather than guessed from local habit
  - visible assembly cues and documentation cues may live on different controlled layers or objects
  - CAD-owner conventions can differ across tools without creating one universal package doctrine

## Safe Blog Usage

- Explain that footprint origin is a controlled library decision, not something that should be inferred ad hoc from a screenshot or one local habit.
- Explain that visible assembly cues and documentation cues may be separated into different controlled drawing objects or layers.
- Explain that CAD tool documentation can support workflow and review posture, while package-owner drawings still control named-family exact geometry.

## Limits And Non-Claims

- This card does not authorize one universal left/right or `pin-1` origin rule for all connectors and packages.
- It does not authorize one universal installation-mark geometry, symbol, or size.
- It does not authorize replacing package-owner drawings with CAD-owner tool documentation when exact family geometry is needed.
- It does not authorize board-level assembly acceptability, polarity judgment, or manufacturing success claims.

## Relationship To Local PCB资料 Intake

- This card partially strengthens two open doctrine surfaces named in `P4-309`:
  - `connector-origin defaulting at universal-rule level`
  - `board-level installation-mark geometry and stronger package-family-specific marking authority`
- It does so only by raising the CAD-owner side from `KiCad/KLC alone` to `KiCad + Altium` cross-tool construction support.
- It still does not close either residual at standards-owner, package-owner, or universal-rule level.

## Source Links

- https://klc.kicad.org/
- https://www.altium.com/documentation/altium-designer/creating-pcb-footprint?version=21.0
