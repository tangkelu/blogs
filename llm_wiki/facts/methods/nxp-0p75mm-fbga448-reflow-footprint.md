---
fact_id: "methods-nxp-0p75mm-fbga448-reflow-footprint"
title: "NXP SOT1908-1 visible values are reusable only as the named 0.75 mm FBGA448 reflow-footprint pages"
topic: "NXP 0.75 mm FBGA448 reflow footprint for the named SOT1908-1 package"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-05-11"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_bga_reflow_footprint_pages"
canonical_unit_policy: "Preserve original NXP package identity and visible page wording such as FBGA448, SOT1908-1, 0.75 mm pitch, Reflow soldering footprint part 1/2/3, and recommended stencil thickness 0.125. Do not normalize these visible page values into a universal 0.75 mm pitch conversion table."
source_ids:
  - "nxp-sot1908-1-fbga448-0p75mm-reflow-footprint"
tags: ["nxp", "fbga448", "sot1908-1", "0.75-mm-pitch", "reflow-footprint", "exact-data", "third-owner"]
---

# Canonical Summary

> NXP's `SOT1908-1` package-information PDF is strong enough to support one narrow exact-data layer for the `PCB资料` package lane: the local corpus may reuse this named-package `FBGA448` `0.75 mm` pitch identity and its visible `Reflow soldering footprint` page values when the package identity and page context stay attached. This card is a vendor-scoped named-package page set only. It does not authorize a universal `0.75 mm pitch -> land pattern` rule.

## Exact Data Scope

- exact for:
  - NXP's printed `FBGA448` named-package identity
  - the printed package code `SOT1908-1`
  - the printed package pitch `0.75 mm`
  - the printed body statement `17 mm x 17 mm x 2.46 mm body`
  - the visible page identities `Reflow soldering footprint part 1`, `part 2`, and `part 3`
  - the visible page-scoped values `448X φ0.45`, `448X φ0.35`, `27X 0.75`, and `recommended stencil thickness: 0.125`
- not exact for:
  - all `0.75 mm` BGA or FBGA packages
  - any semantic relabeling beyond the visible page wording and value context
  - cross-vendor `0.75 mm pitch -> pad diameter` rules
  - residual `1.50 mm` package closure

## Admitted Data

- NXP prints this named package identity:
  - `FBGA448`
  - `SOT1908-1`
- NXP prints this package pitch and body statement:
  - `0.75 mm pitch`
  - `17 mm x 17 mm x 2.46 mm body`
- NXP shows these visible reflow-footprint page identities:
  - `Reflow soldering footprint part 1`
  - `Reflow soldering footprint part 2`
  - `Reflow soldering footprint part 3`
- NXP shows these visible page-scoped values:
  - `448X φ0.45`
  - `448X φ0.35`
  - `27X 0.75`
  - `recommended stencil thickness: 0.125`

## Conditions And Methods

- Treat this card as one owner-scoped package-information page set for the named `FBGA448 / SOT1908-1` package.
- Keep the `0.75 mm` pitch and visible footprint-page values attached to the NXP package identity and page context.
- Use this card when a prompt needs one safe current-public third-owner `0.75 mm` replacement page set and can stay inside named-package scope.
- Use this card to show that the `0.75 mm` residual is no longer limited to `Microchip + Renesas` owner families.
- Pair this card with:
  - [microchip-0p75mm-tfbga-land-pattern-4lx.md](/code/blogs/llm_wiki/facts/methods/microchip-0p75mm-tfbga-land-pattern-4lx.md)
  - [microchip-0p75mm-tfbga-land-pattern-7g.md](/code/blogs/llm_wiki/facts/methods/microchip-0p75mm-tfbga-land-pattern-7g.md)
  - [microchip-0p75mm-tfbga-land-pattern-bab.md](/code/blogs/llm_wiki/facts/methods/microchip-0p75mm-tfbga-land-pattern-bab.md)
  - [renesas-0p75mm-fbga-package-land-pattern-bcg48d1.md](/code/blogs/llm_wiki/facts/methods/renesas-0p75mm-fbga-package-land-pattern-bcg48d1.md)

## Limits And Non-Claims

- This card does not authorize a universal `0.75 mm` BGA / FBGA conversion table.
- It does not authorize unlabeled interpretation of each visible NXP footprint value beyond the page wording.
- It does not authorize package-library defaults outside the named `FBGA448 / SOT1908-1` package.
- It does not close the remaining `1.50 mm`, connector-origin, or stronger installation-mark authority gaps.

## Relationship To Local PCB资料 Intake

- This card gives the package lane one current-public third-owner exact-data route for `0.75 mm`.
- It narrows the residual state from `three Microchip exact rows plus one Renesas second-owner exact-data page` to `three Microchip exact rows plus one Renesas second-owner exact-data page plus one NXP third-owner exact-data page`.
- It still does not turn the blocked handbook table into a reusable generic pitch law.

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating secondary-PDF candidate:
  - `P4-215C2` page-28 `bga pitch-to-pad-diameter table`
- authority replacement used here:
  - official NXP package-information PDF `SOT1908-1`
- exact-data shape:
  - vendor-scoped named-package BGA reflow-footprint pages

## Source Links

- https://www.nxp.com/docs/en/package-information/SOT1908-1.pdf
