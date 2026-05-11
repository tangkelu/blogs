---
fact_id: "methods-iec-smd-component-marking-boundary"
title: "IEC 61760-1 public metadata plus preview support a narrow component-marking boundary for pin-1 and polarity-identification topic framing, without authorizing board-level installation-mark geometry"
topic: "IEC SMD component marking boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-10"
exact_data_class: "boundary_convention"
scope_type: "iec_component_marking_boundary"
canonical_unit_policy: "Preserve IEC component-marking wording as component-specification scope. Do not rewrite this card into a universal connector-origin doctrine or board-level installation-mark geometry rule."
source_ids:
  - "iec-61760-1-smd-specification-page"
  - "iec-61760-1-component-marking-preview-page"
tags: ["iec", "61760-1", "smd", "component-marking", "pin-1", "polarity", "package-library", "boundary"]
---

# Canonical Summary

> Current public source coverage is strong enough to land one narrow IEC component-marking boundary. The official IEC `61760-1` metadata page establishes that component specification for surface mounting is a formal standards-owner topic, and the visible public preview surface exposes a `component marking` section family with separate multipin-component and polarity-component marking subheads. This supports guarded wording that `pin-1` identification and polarity identification belong to controlled component specification and documentation scope. It does not authorize one universal silkscreen symbol, one universal fabrication-layer mark, or any board-level installation-mark geometry doctrine.

## Stable Facts

- IEC `61760-1:2020` is the standards-owner publication for specification of components for surface mounting.
- The official IEC scope states that the standard covers requirements for component specifications and the same component placement, mounting, cleaning, and inspection processes for all surface-mounted components.
- The visible public preview surface shows a dedicated `component marking` section family, including separate subheads for multipin-component marking and polarity-component marking.
- This is strong enough to support guarded wording that `pin-1` and polarity-identification topics belong to the controlled component-specification layer.

## Conditions And Methods

- Use this card when a prompt needs stronger public support than local handbook or internal blog wording for `pin-1` / polarity-identification topic framing.
- Use it to separate:
  - component-specification marking doctrine
  - CAD-library zero-orientation doctrine
  - connector-owner exact-layout doctrine
- Pair this card with:
  - [iec-zero-orientation-cad-library-construction-boundary.md](/code/blogs/llm_wiki/facts/methods/iec-zero-orientation-cad-library-construction-boundary.md)
  - [padstack-origin-pin1-and-footprint-review-governance-boundary.md](/code/blogs/llm_wiki/facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md)
  - [connector-origin-and-installation-mark-boundary.md](/code/blogs/llm_wiki/facts/methods/connector-origin-and-installation-mark-boundary.md)
- Use named connector-owner drawings instead of this card when exact arrow shape, series-specific front side, or exact recommended PCB layout is needed.

## Safe Blog Usage

- Explain that `pin-1` and polarity-identification intent should be explicit and controlled in the component / footprint specification package.
- Explain that identification discipline belongs upstream in specification and documentation, not only at assembly-time interpretation.
- Explain that standards-backed marking identity still does not remove the need for package-owner or connector-owner exact drawings.

## Limits And Non-Claims

- This card does not authorize one universal connector-origin default.
- It does not authorize one universal silkscreen symbol, `F.Fab` marker shape, arrow size, dot size, or layer-placement rule.
- It does not authorize board-level installation-mark geometry.
- It does not authorize package-family-specific exceptions, test conditions, or marking-durability procedures beyond the public preview surface.

## Relationship To Local PCB资料 Intake

- This card partially narrows the residual lane previously grouped under stronger `installation-mark / component-marking` authority.
- It adds one standards-backed public route for `pin-1` and polarity-identification topic framing beyond `KiCad + owner drawings + local handbook context`.
- It does not close:
  - board-level installation-mark geometry doctrine
  - connector-origin defaulting
  - package-owner exact marking conventions for every family

## Source Links

- https://webstore.iec.ch/en/publication/60478
- https://standards.iteh.ai/catalog/standards/iec/6dfaf130-8567-4be5-82db-c971ed995b5e/iec-61760-1-2020
