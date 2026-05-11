---
fact_id: "methods-iec-zero-orientation-cad-library-construction-boundary"
title: "IEC 61188-7 gives standards-owner support for zero-orientation wording in CAD library construction, without closing connector-origin or installation-mark geometry doctrine"
topic: "IEC zero orientation CAD library construction boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-10"
exact_data_class: "boundary_convention"
scope_type: "standards_owner_zero_orientation_boundary"
canonical_unit_policy: "Preserve IEC zero-orientation and orientation-description wording as CAD-library construction scope. Do not rewrite this card into a universal connector-origin, pin-1 symbol, polarity-mark, or installation-mark geometry rule."
source_ids:
  - "iec-61188-7-zero-orientation-cad-library-page"
tags: ["iec", "61188-7", "zero-orientation", "cad-library", "component-orientation", "land-pattern", "package-library", "boundary"]
---

# Canonical Summary

> Current official support is strong enough to land one narrow standards-owner boundary for `zero orientation`: IEC `61188-7` treats electronic-component zero orientation and orientation-description technique as a formal CAD-library construction topic tied to land-pattern geometry description. This supports guarded wording that orientation intent belongs to controlled library construction rather than ad hoc operator inference. It does not create a universal connector-origin default, a universal `pin-1` or polarity-mark rule, or a board-level installation-mark geometry doctrine.

## Stable Facts

- IEC `61188-7:2017` is an official standards-owner publication for `electronic component zero orientation for CAD library construction`.
- The public IEC scope states that the document establishes a consistent technique for the description of electronic component orientation and their land-pattern geometries.
- This is strong enough to support standards-owner wording that `zero orientation` is a controlled library-construction topic.
- This is not the same as a released assembly-mark geometry rule or a connector-series exact-layout drawing.

## Conditions And Methods

- Use this card when a prompt needs guarded standards-owner wording that orientation description belongs to CAD-library construction.
- Use it to separate:
  - standards-owner `zero orientation` framing
  - CAD-library conventions such as KiCad `KLC`
  - connector-owner exact drawings for named series
- Pair this card with connector-owner drawings when the prompt is about a named connector family rather than generic library construction.
- Pair this card with documentation-governance cards when the prompt needs `pin-1`, polarity, or assembly-document completeness language.

## Safe Blog Usage

- Explain that orientation intent should be normalized inside the controlled CAD-library / footprint-construction workflow.
- Explain that zero orientation is a standards-backed library-construction concept, not something that should be improvised at assembly time.
- Explain that exact connector layout and visible marking still need stronger series-specific or process-specific authority.

## Limits And Non-Claims

- This card does not authorize one universal connector-origin default across connector families.
- It does not authorize `pin-1` symbol shape, polarity-mark symbol choice, or silkscreen / fabrication-layer geometry.
- It does not authorize one universal `installation-mark` arrow, bevel, dot, line width, or placement rule.
- It does not authorize exact package land-pattern geometry from the IEC metadata page alone.

## Relationship To Local PCB资料 Intake

- This card partially narrows the residual lane previously grouped under stronger `installation-mark` authority.
- It upgrades the repo from `KiCad + owner drawings + local handbook context` to one standards-owner anchor for `zero orientation`.
- It does not close the broader residual for:
  - board-level installation-mark geometry doctrine
  - universal `pin-1` / polarity-mark rule
  - connector-origin defaulting

## Source Links

- https://webstore.iec.ch/en/publication/27498
