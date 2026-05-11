---
fact_id: "methods-iec-square-bga-1mm-or-larger-outline-and-variation-boundary"
title: "IEC public metadata supports a narrow square-BGA 1 mm-or-larger outline, dimensions, and recommended-variations boundary, without exposing a public 1.50 mm exact row"
topic: "IEC square-BGA 1 mm-or-larger outline and variation boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-11"
exact_data_class: "boundary_convention"
scope_type: "standards_owner_square_bga_outline_dimension_variation_boundary"
canonical_unit_policy: "Preserve IEC standards metadata wording such as square BGA, terminal pitch 1 mm or larger, outline drawings, dimensions, and recommended variations. Do not convert metadata scope into exact PCB land-pattern, solder-mask, or pad-diameter values."
source_ids:
  - "iec-60191-6-18-square-bga-design-guide-page"
tags: ["iec", "60191-6-18", "bga", "square-bga", "1.50-mm-pitch", "1-mm-or-larger", "outline", "dimensions", "recommended-variations", "boundary"]
---

# Canonical Summary

> Current public IEC coverage is strong enough to land one narrower standards-owner boundary above the earlier `IEC 60191-6-2` existence card and the broader `IEC 61188-5-8 / 61188-6-2` area-array family framing: IEC `60191-6-18:2010` publicly states that it provides `standard outline drawings, dimensions, and recommended variations` for `all square ball grid array packages (BGA), whose terminal pitch is 1 mm or larger`. This is a real standards-side raise for coarse-pitch square BGA package-family framing. It still does not expose a public `1.50 mm` PCB land-pattern row, and it does not authorize a universal cross-vendor `1.50 mm pitch -> land pattern` rule.

## Stable Facts

- IEC `60191-6-18:2010` is an official standards-owner publication for:
  - `square ball grid array packages (BGA)`
  - `terminal pitch 1 mm or larger`
- The public IEC scope states that this part provides:
  - `standard outline drawings`
  - `dimensions`
  - `recommended variations`
- The official lifecycle metadata states that this standard:
  - cancels and replaces `IEC/PAS 60191-6-18:2008`

## Conditions And Methods

- Use this card when a prompt needs standards-owner confirmation that coarse-pitch square-BGA package design is a formal IEC family with public metadata above simple title-level existence.
- Use it to explain that:
  - `IEC 60191-6-2` confirms coarse-pitch ball/column package-guide existence
  - `IEC 60191-6-18` confirms a tighter square-BGA package family with public outline/dimension/recommended-variation framing for `1 mm or larger`
  - `IEC 61188-5-8` and `IEC 61188-6-2` still carry the separate land-pattern-design family framing
- Pair this card with owner-scoped package geometry cards if a prompt needs exact `1.50 mm` or named-package data.
- Keep this card inside metadata and package-family framing only.

## Safe Blog Usage

- Explain that coarse-pitch square BGA package design is not just a vendor-specific naming accident; it sits inside a formal IEC package-guide family.
- Explain that public IEC metadata now confirms square-BGA package-family scope plus outline, dimension, and recommended-variation framing for `1 mm or larger`.
- Explain that exact `1.50 mm` PCB land-pattern geometry still has to come from package-owner rows or paid standards content that is not publicly exposed on the metadata page.

## Limits And Non-Claims

- This card does not authorize a public `1.50 mm` BGA pad-diameter row.
- It does not authorize solder-mask opening values, NSMD/SMD defaults, or PCB land-pattern geometry from metadata alone.
- It does not authorize a universal `1.50 mm pitch -> land pattern` table.
- It does not prove that the paid standard's package guidance is publicly accessible in exact-row form.

## Relationship To Local PCB资料 Intake

- This card raises the `1.50 mm` lane above the earlier `IEC 60191-6-2 existence only` card by adding one narrower official square-BGA package-family boundary.
- It makes the current standards-side ceiling more accurate:
  - `IEC 60191-6-2` = coarse-pitch ball/column package-guide existence
  - `IEC 60191-6-18` = square-BGA `1 mm or larger` outline/dimension/recommended-variation family
  - `IEC 61188-5-8` = area-array land-pattern geometry family
  - `IEC 61188-6-2` = later maintained land-pattern design standard family
- It still does not close the blocked handbook `1.50 mm` row at exact-data level.

## Source Links

- https://webstore.iec.ch/en/publication/998
