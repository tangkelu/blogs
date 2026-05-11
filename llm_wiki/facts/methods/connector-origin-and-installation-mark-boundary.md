---
fact_id: "methods-connector-origin-and-installation-mark-boundary"
title: "Connector origin and installation-mark wording is reusable only as CAD-library convention plus series-specific owner drawing context"
topic: "Connector origin and installation-mark boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-08"
exact_data_class: "boundary_convention"
scope_type: "cad_owner_plus_connector_owner_boundary"
canonical_unit_policy: "Preserve original owner wording such as pin-1, recommended PCB layout, F.SilkS, F.Fab, and small arrow indicator. Do not normalize these conventions into a universal connector-origin or installation-mark doctrine."
source_ids:
  - "kicad-library-conventions-footprint-orientation-and-marking"
  - "molex-105133-0002-micro-b-recommended-pcb-layout"
  - "samtec-mb1-recommended-pcb-layout-and-mating-card"
  - "amphenol-10122424-sfp-board-connector-recommended-pcb-layout"
tags: ["connector", "origin", "pin-1", "installation-mark", "kicad", "molex", "samtec", "library-convention", "series-specific"]
---

# Canonical Summary

> Current official support is strong enough to promote one narrow boundary card for connector-origin and installation-mark wording: KiCad's `KLC` gives guarded CAD-owner library conventions for connector orientation and pin-1 marking, while Molex's `105133` sales drawing and Samtec's `MB1` footprint drawing give connector-owner series-specific layout context for named connector families. This supports a layered rule: use CAD-library convention for generic footprint-governance wording and use connector-owner drawings for named series. It does not support one universal connector-origin or installation-mark rule across all connector types.

## Stable Facts

- KiCad `KLC` treats footprint orientation and pin-1 marking as official library conventions, not hard universal rules.
- KiCad states footprints should place `pin 1` in the upper-left corner when possible.
- KiCad states single-line footprints should align `pin 1` on the left side.
- KiCad states multi-purpose connector footprints should be oriented horizontally with `pin 1` on the left side.
- KiCad expects polarity marking or `pin-1` designator on `F.SilkS`.
- KiCad expects pin-1 location to be drawn on `F.Fab`; for connectors, a small arrow indicator next to `pin-1` should be used.
- KiCad states through-hole footprint anchors should be placed at the location of `pin 1`.
- Molex prints a `RECOMMENDED PCB LAYOUT` for the named `105133-0001 / 105133-0002` Micro-USB B receptacle family with explicit `PIN 1` through `PIN 5` numbering and pin assignment.
- Samtec prints `RECOMMENDED PCB LAYOUT`, `RECOMMENDED STENCIL LAYOUT`, and `RECOMMENDED MATING CARD LAYOUT` for the named `MB1-1XX-XX-XX-S-XX-SL-X` footprint family.
- Amphenol prints `RECOMMENDED PCB LAYOUT` with explicit `CONNECTOR MOUNTING SIDE`, `MATING PCB SIDE`, and visible `PIN 1` anchors for the named `10122424` SFP+ board-connector family.

## Conditions And Methods

- Use KiCad only as `CAD-owner library convention` support when a prompt needs guarded generic wording about connector orientation, pin-1 placement, or installation-mark documentation.
- Use connector-owner drawings such as Molex `105133` or Samtec `MB1` when the prompt is about a named connector family and needs exact layout, pin-numbering, or mating-card context.
- Use connector-owner drawings such as Molex `105133`, Samtec `MB1`, or Amphenol `10122424` when the prompt is about a named connector family and needs exact layout, pin-numbering, or named-side context.
- Treat the safe reusable rule as:
  - generic connector-origin defaults should come from controlled library conventions or owner drawings, not from local inference
  - named connector footprints should follow the owner series drawing when one is available
- Explain `installation mark` at two layers when needed:
  - `F.SilkS` or `pin-1` designator for visible assembly cue
  - `F.Fab` small arrow or pin-1 location cue for footprint documentation

## Safe Blog Usage

- Explain that connector orientation should be controlled and documented, not guessed.
- Explain that a library convention may define a default review posture, while a connector-owner drawing defines the exact series-specific layout.
- Explain that pin-1 and visible orientation cues belong in the released footprint documentation package.

## Limits And Non-Claims

- This card does not authorize one universal left/right origin rule for all connectors.
- It does not authorize one universal installation-mark geometry, size, or mandatory symbol across all package and connector families.
- It does not authorize using one USB connector drawing as proof for mezzanine, board-to-board, wire-to-board, coax, or sensor connectors.
- It does not authorize KiCad `KLC` as package-owner or standards-owner authority.

## Relationship To Local PCB资料 Intake

- This card partially narrows two residuals named in `P4-309`:
  - `connector-origin defaulting`
  - stronger `installation mark` authority
- It does so only at the `library-convention plus series-specific owner drawing` layer.
- It does not close either residual at universal-rule level.

## Source Links

- https://klc.kicad.org/
- https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/salesdrawingpdf/105/105133/1051330002_sd.pdf
- https://suddendocs.samtec.com/prints/mb1-1xx-xx-xx-s-xx-sl-x-footprint.pdf
- https://cdn.amphenol-cs.com/media/wysiwyg/files/drawing/10122424.pdf
