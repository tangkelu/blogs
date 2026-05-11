---
fact_id: "methods-amd-bg225-bgg225-1p50mm-bga-footprint-row"
title: "AMD-hosted UG112 BG225/BGG225 values are reusable only as one owner-scoped 1.50 mm BGA footprint row"
topic: "AMD-hosted UG112 BG225/BGG225 1.50 mm BGA footprint row"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-05-11"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_bga_footprint_table_row"
canonical_unit_policy: "Preserve original row labels and values from the AMD-hosted UG112 table, including BG225/BGG225, Component Land, Solder Land (NSMD), Stencil Opening, Pitch, Line Width, Distance, Via Land, and Through Hole. Do not normalize this owner-scoped row into a universal 1.50 mm pitch conversion table."
source_ids:
  - "amd-ug112-bg225-bgg225-1p50mm-bga-footprint-row"
tags: ["amd", "xilinx", "bg225", "bgg225", "1.50-mm-pitch", "bga", "footprint-row", "exact-data", "third-owner"]
---

# Canonical Summary

> The AMD-hosted `UG112 Device Package User Guide` is strong enough to support one narrow exact-data layer for the `PCB资料` `1.50 mm` package lane: the local corpus may reuse the printed `BG225 / BGG225` row with its same-table `Pitch 1.50` and footprint geometry values when the package-row identity and document context stay attached. This card is a vendor-scoped exact row only. It does not authorize a universal `1.50 mm pitch -> land pattern` rule.

## Exact Data Scope

- exact for:
  - the printed package row `BG225 / BGG225`
  - the printed pitch value `1.50`
  - the same-table geometry values `Component Land 0.63`, `Solder Land (NSMD) 0.58`, `Stencil Opening 0.68`, `Line Width 0.300`, `Distance 1.06`, `Via Land 0.65`, and `Through Hole 0.356`
- not exact for:
  - all AMD or Xilinx BGA packages
  - all vendors at `1.50 mm`
  - generic handbook `MIN / MAX / recommended` closeout
  - package-library defaults outside this package-row document context

## Admitted Data

- AMD hosts this package guide:
  - `UG112 Device Package User Guide`
- the guide prints this package row:
  - `BG225 / BGG225`
- the guide prints this pitch value:
  - `1.50`
- the guide prints these same-table geometry values:
  - `Component Land 0.63`
  - `Solder Land (NSMD) 0.58`
  - `Stencil Opening 0.68`
  - `Line Width 0.300`
  - `Distance 1.06`
  - `Via Land 0.65`
  - `Through Hole 0.356`

## Conditions And Methods

- Treat this card as one AMD-hosted owner-scoped exact row for the printed `BG225 / BGG225` package context.
- Keep the `1.50` pitch and geometry values attached to the `UG112` table row.
- Use this card when a prompt needs one more materially independent current-public `1.50 mm` owner exact row and can stay inside named-package row scope.
- Pair this card with:
  - [nxp-1p50mm-bga225-reflow-footprint.md](/code/blogs/llm_wiki/facts/methods/nxp-1p50mm-bga225-reflow-footprint.md)
  - [renesas-1p50mm-bga-package-drawing-prbg0225cb-a.md](/code/blogs/llm_wiki/facts/methods/renesas-1p50mm-bga-package-drawing-prbg0225cb-a.md)
  - [renesas-1p50mm-bga-lga-mount-pad-dimensions-row.md](/code/blogs/llm_wiki/facts/methods/renesas-1p50mm-bga-lga-mount-pad-dimensions-row.md)
  - [iec-area-array-land-pattern-geometry-family-boundary.md](/code/blogs/llm_wiki/facts/methods/iec-area-array-land-pattern-geometry-family-boundary.md)

## Limits And Non-Claims

- This card does not authorize a universal `1.50 mm` BGA conversion table.
- It does not authorize package-family-specific geometry outside the printed `BG225 / BGG225` row.
- It does not authorize cross-vendor defaulting or handbook table closeout.
- It does not close `connector-origin` or `installation-mark` residuals.

## Relationship To Local PCB资料 Intake

- This card gives the package lane one materially independent third-owner exact row for `1.50 mm`.
- It raises the residual state from `IEC family boundary + one NXP exact row + one Renesas named-package drawing + one Renesas exact row` to that same stack plus one AMD-hosted `BG225 / BGG225` exact row.
- It still does not turn the blocked handbook table into a reusable generic pitch law.

## Source Links

- https://docs.amd.com/v/u/en-US/ug112
