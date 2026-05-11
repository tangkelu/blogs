---
fact_id: "methods-bga-1p50mm-pitch-standards-existence-boundary"
title: "1.50 mm BGA and column-package wording is reusable only as standards-owner existence and scope metadata, not as geometry"
topic: "1.50 mm BGA and column package standards existence boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-08"
exact_data_class: "boundary_convention"
scope_type: "standards_metadata_for_ball_and_column_package_design_guide"
canonical_unit_policy: "Preserve IEC's scope wording and pitch labels such as 1.50 mm, 1.27 mm, and 1.00 mm. Do not convert metadata scope into numeric land-pattern guidance."
source_ids:
  - "iec-60191-6-2-ball-column-package-design-guide-page"
tags: ["iec", "bga", "cga", "1.50-mm-pitch", "1.27-mm-pitch", "1.00-mm-pitch", "standards-metadata", "boundary"]
---

# Canonical Summary

> The official IEC webstore metadata for `IEC 60191-6-2` is strong enough to support one narrow boundary card for the `1.50 mm` residual lane: the local corpus may state that a standards-owner design-guide family exists for `1.50 mm`, `1.27 mm`, and `1.00 mm` pitch ball and column terminal packages, and may name the package classes within that scope. This metadata page does not authorize exact land-pattern geometry, numeric replacement rows, or direct closure of the handbook `1.50 mm` row.

## Stable Facts

- IEC publishes `IEC 60191-6-2:2001` as a standards-owner document for preparation of outline drawings of surface-mounted semiconductor device packages.
- The official scope statement names `1.50 mm`, `1.27 mm`, and `1.00 mm` pitch ball and column terminal packages.
- The official scope statement names package-class examples such as:
  - `ceramic ball grid array (C-BGA)`
  - `plastic ball grid array (P-BGA)`
  - `tape ball grid array (T-BGA)`
  - `column terminal packages`, such as `C-CGA`
- The official IEC metadata page shows publication date `2001-12-11`, edition `1.0`, and stability date `2027`.

## Conditions And Methods

- Use this card when a prompt needs standards-owner confirmation that `1.50 mm` coarse-pitch ball and column package guidance exists as a formal design-guide family.
- Use this card for terminology, package-class identity, and existence framing only.
- Pair this card with owner-scoped package drawings or application notes if a prompt needs exact package geometry or land-pattern data.
- Explain that the safe current rule is:
  - standards-owner metadata confirms the guide family exists
  - exact numeric row replacement still requires a package-owner or public standards table that is not yet in hand

## Safe Blog Usage

- Explain that coarse-pitch ball and column terminal packages are standardized enough to have named design-guide families.
- Explain that `1.50 mm` package guidance exists in standards scope, but the current repo does not yet hold a public exact-geometry replacement row.

## Limits And Non-Claims

- This card does not authorize the handbook `1.50 mm` pitch row as exact geometry.
- It does not authorize numeric PCB pad diameter, solder-mask opening, or ball-size values.
- It does not authorize free/public access to the standard contents beyond metadata and scope.
- It does not close the `1.50 mm` exact-data residual.

## Relationship To Local PCB资料 Intake

- This card narrows the `1.50 mm` residual from `discovery-level only` to `standards-owner existence and scope confirmed`.
- It does not provide the owner-scoped or standards-table exact row needed to replace the blocked handbook geometry.

## Source Links

- https://webstore.iec.ch/en/publication/1002
