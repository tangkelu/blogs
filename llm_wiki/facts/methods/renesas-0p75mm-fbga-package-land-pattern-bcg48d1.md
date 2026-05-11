---
fact_id: "methods-renesas-0p75mm-fbga-package-land-pattern-bcg48d1"
title: "Renesas BCG48D1 values are reusable only as the named 0.75 mm FBGA package land-pattern page"
topic: "Renesas 0.75 mm FBGA land pattern for the named BCG48D1 package"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-10"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_bga_land_pattern_document"
canonical_unit_policy: "Preserve original Renesas millimeter values, package identity, and page wording such as 48-FBGA, 10.0 x 10.0 x 1.27 mm Body, 0.75mm Pitch, and RECOMMENDED LAND PATTERN DIMENSION. Do not normalize this page into a universal 0.75 mm pitch conversion table."
source_ids:
  - "renesas-bcg48d1-48-fbga-package-land-pattern-0p75mm"
tags: ["renesas", "fbga", "bga", "0.75-mm-pitch", "package-land-pattern", "bcg48d1", "second-owner", "source-coverage"]
---

# Canonical Summary

> Renesas' `BCG48D1` package land-pattern PDF is strong enough to support one narrow exact-data layer for the `PCB资料` package lane: the local corpus may reuse this named-package `0.75 mm` pitch page and its visible `RECOMMENDED LAND PATTERN DIMENSION` geometry when the package identity and page context stay attached. This card is a vendor-scoped named-package page only. It does not authorize a universal `0.75 mm pitch -> land pattern` rule.

## Exact Data Scope

- exact for:
  - the printed document class `Package Land Pattern`
  - the named package identity `48-FBGA`
  - the printed body statement `10.0 x 10.0 x 1.27 mm Body`
  - the printed package pitch `0.75mm Pitch`
  - the named package code `BCG48D1`
  - the visible land-pattern geometry values `0.300`, `0.75`, `3.750`, `5.25`, and `10.000`
  - the visible note context `ALL DIMENSIONS ARE IN MM. ANGLES IN DEGREES.`, `LAND PATTERN RECOMMENDATION PER IPC-7351B GENERIC`, and `SMD PATTERN ASSUMED`
- not exact for:
  - any geometry label or semantic interpretation not visible on the verified page
  - all `0.75 mm` FBGA or BGA packages
  - generic cross-vendor `0.75 mm pitch -> pad diameter` rules
  - residual `1.50 mm` package closure

## Admitted Data

- Renesas prints this document class:
  - `48-FBGA, Package Land Pattern`
- Renesas prints this named-package body statement:
  - `10.0 x 10.0 x 1.27 mm Body`
- Renesas prints this package pitch:
  - `0.75mm Pitch`
- Renesas prints this package code:
  - `BCG48D1`
- Renesas shows this visible `RECOMMENDED LAND PATTERN DIMENSION` geometry:
  - `0.300`
  - `0.75`
  - `3.750`
  - `5.25`
  - `10.000`
- Renesas shows this visible note context:
  - `ALL DIMENSIONS ARE IN MM. ANGLES IN DEGREES.`
  - `LAND PATTERN RECOMMENDATION PER IPC-7351B GENERIC`
  - `SMD PATTERN ASSUMED`

## Conditions And Methods

- Treat this card as one second-owner package land-pattern page for the named `BCG48D1` package.
- Keep the `0.75mm Pitch` statement and visible geometry values attached to the Renesas package identity and page context.
- Use this card when a prompt needs one safe current-public second-owner `0.75 mm` replacement page and can stay inside named-package scope.
- Use this card to show that the `0.75 mm` residual is no longer limited to three Microchip owner rows plus one geometry-unverified Renesas document.
- Pair this card with:
  - [microchip-0p75mm-tfbga-land-pattern-4lx.md](/code/blogs/llm_wiki/facts/methods/microchip-0p75mm-tfbga-land-pattern-4lx.md)
  - [microchip-0p75mm-tfbga-land-pattern-7g.md](/code/blogs/llm_wiki/facts/methods/microchip-0p75mm-tfbga-land-pattern-7g.md)
  - [microchip-0p75mm-tfbga-land-pattern-bab.md](/code/blogs/llm_wiki/facts/methods/microchip-0p75mm-tfbga-land-pattern-bab.md)

## Limits And Non-Claims

- This card does not authorize a universal `0.75 mm` BGA / FBGA conversion table.
- It does not authorize semantic relabeling of each Renesas dimension beyond the visible page wording.
- It does not authorize package-library defaults outside the named `BCG48D1` package document.
- It does not close the remaining `1.50 mm`, connector-origin, or stronger installation-mark authority gaps.

## Relationship To Local PCB资料 Intake

- This card gives the package lane one directly verified current-public second-owner `0.75 mm` named-package exact-data page.
- It narrows the residual state from `three Microchip rows plus one Renesas second-owner named-package document` to `three Microchip exact rows plus one Renesas second-owner exact-data page`.
- It still does not turn the blocked handbook table into a reusable generic pitch law.

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating secondary-PDF candidate:
  - `P4-215C2` page-28 `bga pitch-to-pad-diameter table`
- authority replacement used here:
  - official Renesas named-package land-pattern document `BCG48D1`
- exact-data shape:
  - vendor-scoped named-package BGA land-pattern page

## Source Links

- https://www.renesas.com/us/en/document/psc/48-fbga-package-land-pattern-100-x-100-x-127-mm-body075mm-pitch-bcg48d1
