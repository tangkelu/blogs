---
fact_id: "methods-iec-area-array-land-pattern-geometry-family-boundary"
title: "IEC public metadata supports a narrow area-array land-pattern-geometry family boundary, without exposing a public 1.50 mm exact row"
topic: "IEC area-array land-pattern geometry family boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-11"
exact_data_class: "boundary_convention"
scope_type: "standards_owner_area_array_land_pattern_family_boundary"
canonical_unit_policy: "Preserve IEC standards metadata wording such as area array components, land pattern geometries, and land pattern design. Do not convert metadata scope into exact BGA pad-diameter or solder-mask geometry values."
source_ids:
  - "iec-61188-5-8-area-array-land-pattern-page"
  - "iec-61188-6-2-land-pattern-design-smd-page"
tags: ["iec", "61188-5-8", "61188-6-2", "bga", "fbga", "cga", "lga", "1.50-mm-pitch", "land-pattern", "boundary"]
---

# Canonical Summary

> Current public IEC coverage is strong enough to land one narrower standards-owner boundary above the earlier `IEC 60191-6-2` existence card: IEC `61188-5-8` explicitly frames `area array components (BGA, FBGA, CGA, LGA)` as a land-pattern-geometry topic, and the official lifecycle metadata shows that this family is later partially replaced by `IEC 61188-6-2` and `IEC 61188-6-3`. This supports guarded wording that area-array land-pattern design is a formal IEC standards family, not just a package-drawing coincidence. It still does not expose a public `1.50 mm` exact geometry row, and it does not authorize a universal cross-vendor `1.50 mm pitch -> land pattern` rule.

## Stable Facts

- IEC `61188-5-8:2007` is an official standards-owner publication for:
  - `Attachment (land/joint) considerations`
  - `Area array components (BGA, FBGA, CGA, LGA)`
- The public IEC scope states that this part provides information on:
  - `land pattern geometries`
  - `size, shape and tolerances of surface mount land patterns`
  - support for `inspection, testing and reworking` of the resulting solder joints
- The official lifecycle metadata states that `IEC 61188-5-8` has been partially replaced by:
  - `IEC 61188-6-3:2024`
  - `IEC 61188-6-2:2021`
- IEC `61188-6-2:2021` is an official later land-pattern-design publication for the most common surface mounted components, based on `IEC 61191-2:2017`.

## Conditions And Methods

- Use this card when a prompt needs standards-owner confirmation that area-array land-pattern geometry belongs to a formal IEC design family.
- Use it to explain that:
  - `IEC 60191-6-2` confirms coarse-pitch ball/column package-guide existence
  - `IEC 61188-5-8` confirms area-array land-pattern geometry is a formal standards-owner topic
  - `IEC 61188-6-2` confirms that land-pattern design remains a later maintained IEC standard family
- Pair this card with owner-scoped package geometry cards if a prompt needs exact `1.50 mm` or named-package data.
- Keep this card inside metadata and family-scope framing only.

## Safe Blog Usage

- Explain that BGA / FBGA / CGA / LGA land-pattern design is not just vendor folklore; it sits inside a formal IEC standards family.
- Explain that public IEC metadata confirms geometry, tolerance, inspection, testing, and rework framing for area-array attachment considerations.
- Explain that exact package geometry still has to come from package-owner rows or paid standards content that is not publicly exposed on the metadata pages.

## Limits And Non-Claims

- This card does not authorize a public `1.50 mm` BGA pad-diameter row.
- It does not authorize solder-mask opening values, NSMD/SMD defaults, or package-family-specific geometry from metadata alone.
- It does not authorize a universal `1.50 mm pitch -> land pattern` table.
- It does not prove that `IEC 61188-6-2` publicly exposes area-array-specific rows.

## Relationship To Local PCB资料 Intake

- This card raises the `1.50 mm` lane above `IEC 60191-6-2 existence only` by adding one official standards-owner area-array land-pattern family boundary.
- It makes the current standards-side ceiling more accurate:
  - `IEC 60191-6-2` = coarse-pitch package-design-guide existence
  - `IEC 61188-5-8` = area-array land-pattern geometry family
  - `IEC 61188-6-2` = later maintained land-pattern design standard family
- It still does not close the blocked handbook `1.50 mm` row at exact-data level.

## Source Links

- https://webstore.iec.ch/en/publication/4792
- https://webstore.iec.ch/en/publication/65521
