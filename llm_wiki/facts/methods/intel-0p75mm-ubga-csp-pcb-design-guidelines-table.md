---
fact_id: "methods-intel-0p75mm-ubga-csp-pcb-design-guidelines-table"
title: "Intel-hosted .75mm µBGA CSP values are reusable only as one owner-scoped 0.75 mm PCB design table"
topic: "Intel-hosted .75mm µBGA CSP PCB design guidelines table"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-05-11"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_ubga_csp_pcb_design_guideline_table"
canonical_unit_policy: "Preserve original table labels and values from the Intel-hosted packaging databook, including .75mm µBGA CSP Package, Soldermask Opening Dia, Pad Diameter, Via Diameter, and Number of Traces Between Pads. Do not normalize this owner-scoped table into a universal 0.75 mm pitch conversion table."
source_ids:
  - "intel-0p75mm-ubga-csp-pcb-design-guidelines-table"
tags: ["intel", "ubga", "csp", "0.75-mm-pitch", "pcb-design-guidelines", "exact-data", "fourth-owner"]
---

# Canonical Summary

> The Intel-hosted `Packaging Chapter 15 Databook` is strong enough to support one narrow exact-data layer for the `PCB资料` `0.75 mm` package lane: the local corpus may reuse the printed `.75mm µBGA CSP Package` `PCB Design Guidelines` table when the package-table identity and document context stay attached. This card is a vendor-scoped exact table only. It does not authorize a universal `0.75 mm pitch -> land pattern` rule.

## Exact Data Scope

- exact for:
  - the printed `.75mm µBGA CSP Package` table context
  - the same-table values `Soldermask Opening Dia 0.375-0.425`, `Pad Diameter 0.325-0.375`, `Via Diameter 0.25-0.30`, and `Number of Traces Between Pads 1`
- not exact for:
  - all Intel BGA, CSP, or µBGA packages
  - all vendors at `0.75 mm`
  - generic handbook `MIN / MAX / recommended` closeout
  - residual `1.50 mm` package closure

## Admitted Data

- Intel hosts this package-guide context:
  - `Packaging Chapter 15 Databook`
- the guide prints this table context:
  - `.75mm µBGA CSP Package`
- the guide prints these same-table guideline values:
  - `Soldermask Opening Dia 0.375-0.425`
  - `Pad Diameter 0.325-0.375`
  - `Via Diameter 0.25-0.30`
  - `Number of Traces Between Pads 1`

## Conditions And Methods

- Treat this card as one Intel-hosted owner-scoped exact table for the printed `.75mm µBGA CSP Package` context.
- Keep the `0.75 mm` package context and guideline values attached to the Intel-hosted table.
- Use this card when a prompt needs one more materially independent current-public `0.75 mm` owner exact row and can stay inside package-table scope.
- Use this card to show that the `0.75 mm` residual is no longer limited to `Microchip + Renesas + NXP` owner families.
- Pair this card with:
  - [microchip-0p75mm-tfbga-land-pattern-4lx.md](/code/blogs/llm_wiki/facts/methods/microchip-0p75mm-tfbga-land-pattern-4lx.md)
  - [microchip-0p75mm-tfbga-land-pattern-7g.md](/code/blogs/llm_wiki/facts/methods/microchip-0p75mm-tfbga-land-pattern-7g.md)
  - [microchip-0p75mm-tfbga-land-pattern-bab.md](/code/blogs/llm_wiki/facts/methods/microchip-0p75mm-tfbga-land-pattern-bab.md)
  - [renesas-0p75mm-fbga-package-land-pattern-bcg48d1.md](/code/blogs/llm_wiki/facts/methods/renesas-0p75mm-fbga-package-land-pattern-bcg48d1.md)
  - [nxp-0p75mm-fbga448-reflow-footprint.md](/code/blogs/llm_wiki/facts/methods/nxp-0p75mm-fbga448-reflow-footprint.md)

## Limits And Non-Claims

- This card does not authorize a universal `0.75 mm` BGA / CSP conversion table.
- It does not authorize package-family-specific geometry outside the printed `.75mm µBGA CSP Package` table.
- It does not authorize cross-vendor defaulting or handbook table closeout.
- It does not close the remaining `1.50 mm`, connector-origin, or stronger installation-mark authority gaps.

## Relationship To Local PCB资料 Intake

- This card gives the package lane one materially independent fourth-owner exact row for `0.75 mm`.
- It raises the residual state from `three Microchip exact rows plus one Renesas second-owner exact-data page plus one NXP third-owner exact-data page` to that same stack plus one Intel-hosted `.75mm µBGA CSP Package` exact table.
- It still does not turn the blocked handbook table into a reusable generic pitch law.

## Source Links

- https://www.intel.com/content/dam/www/public/us/en/documents/packaging-databooks/packaging-chapter-15-databook.pdf
