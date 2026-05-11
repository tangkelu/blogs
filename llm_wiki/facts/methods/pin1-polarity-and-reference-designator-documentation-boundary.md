---
fact_id: "methods-pin1-polarity-and-reference-designator-documentation-boundary"
title: "Pin-1, polarity, and reference-designator language is safe as documentation and inspection governance, not as silkscreen geometry doctrine"
topic: "pin-1 polarity and reference-designator documentation boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-10"
source_ids:
  - "iec-61760-1-smd-specification-page"
  - "iec-61760-1-component-marking-preview-page"
  - "iec-61188-7-zero-orientation-cad-library-page"
  - "frontendapt-blog-assembly-drawing-essentials-en"
  - "frontendapt-blog-smt-component-polarity-en"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-quality-system-page-en"
tags: ["pin-1", "polarity", "reference-designator", "assembly-drawing", "zero-orientation", "aoi", "documentation", "methods", "boundary"]
---

# Canonical Summary

> Current repo coverage is strong enough to keep `pin-1`, polarity, and reference-designator discussion inside a controlled documentation-and-inspection boundary: component-specification marking, zero-orientation library construction, assembly-drawing completeness, and visible inspection vocabulary. It is not strong enough to publish universal silkscreen geometry, text-distance, symbol-shape, or package-family-specific marking rules.

## Stable Facts

- IEC `61760-1` public metadata and preview support guarded wording that `pin-1` and polarity identification belong to controlled component-specification marking scope.
- IEC `61188-7` public metadata supports guarded wording that component orientation belongs to controlled CAD-library construction and zero-orientation discipline.
- The internal `Assembly Drawing Essentials` page supports the posture that assembly drawings should explicitly preserve `pin-1`, polarity, labeling, and special-assembly intent rather than leaving them implicit.
- The internal `SMT Component Polarity` page supports visible pin-1 indicators, polarity annotation, zero-orientation discipline, and inspection-checkpoint posture as documentation-governance ideas.
- The internal AOI and quality-system pages support orientation, polarity, and visible marking review as part of the broader PCBA inspection and release workflow.
- Reference designators are safe as assembly-communication and traceable documentation surfaces, not as proof that one silkscreen layout style is universally required.

## Conditions And Methods

- Use this card when a rewrite needs guarded wording such as `pin-1 and polarity intent should be explicit in the released documentation package` or `orientation review belongs to library construction and visible inspection`.
- Use this card to keep `reference designator visibility`, `pin-1 identification`, and `polarity annotation` inside documentation completeness and inspection vocabulary.
- Pair this card with `methods-iec-smd-component-marking-boundary` when a prompt needs the standards-owner component-marking layer.
- Pair this card with `methods-iec-zero-orientation-cad-library-construction-boundary` when the prompt needs standards-owner zero-orientation wording.
- Pair this card with `methods-component-orientation-and-polarity-inspection-vocabulary-boundary` when the prompt needs visible inspection taxonomy rather than documentation-governance framing alone.

## Limits And Non-Claims

- This card does not authorize universal component-prefix grammar such as `R/C/L/U/Q` as standards truth.
- It does not authorize silkscreen font size, stroke width, keepout, offset, adjacency, or placement-distance rules.
- It does not authorize one universal `pin-1` dot, notch, arrow, bevel, or polarity-mark symbol geometry.
- It does not authorize package-family-specific marking conventions, exact fabrication-layer marks, or board-level installation-mark geometry.
- It does not prove that clearer marking guarantees yield, prevents failure, saves cost, or shortens delivery.

## Source Links

- https://webstore.iec.ch/en/publication/60478
- https://standards.iteh.ai/catalog/standards/iec/6dfaf130-8567-4be5-82db-c971ed995b5e/iec-61760-1-2020
- https://webstore.iec.ch/en/publication/27498
- /code/hileap/frontendAPT/public/static/blogs/2025/06/en/assembly-drawing-essentials.md
- /code/hileap/frontendAPT/public/static/blogs/2025/06/en/smt-component-polarity.md
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
