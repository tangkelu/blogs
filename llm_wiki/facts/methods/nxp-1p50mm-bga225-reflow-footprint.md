---
fact_id: "methods-nxp-1p50mm-bga225-reflow-footprint"
title: "NXP SOT648-1 BGA225 values are reusable only as the named 1.50 mm package outline and reflow footprint row"
topic: "NXP 1.50 mm BGA225 reflow footprint for the named SOT648-1 package"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-05-10"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_bga_outline_and_reflow_footprint"
canonical_unit_policy: "Preserve original NXP millimeter values, package identity, and column labels such as e, P, SL, SP, SR, Hx, and Hy. Do not normalize this package row into a universal 1.50 mm pitch conversion table."
source_ids:
  - "nxp-sot648-1-bga225-1p50mm-reflow-footprint"
tags: ["nxp", "bga225", "sot648-1", "1.50-mm-pitch", "reflow-footprint", "exact-data", "land-pattern"]
---

# Canonical Summary

> NXP's `SOT648-1` package-information PDF is strong enough to support one narrow exact-data layer for the `PCB资料` package lane: the local corpus may reuse this named-package `BGA225` `1.50 mm` package-pitch statement and printed reflow footprint geometry when the package identity and document context stay attached. This card is a vendor-scoped named-package row only. It does not authorize a universal `1.50 mm pitch -> land pattern` rule.

## Exact Data Scope

- exact for:
  - NXP's printed `BGA225 (SOT648-1)` package identity
  - the printed package outline pitch statement `e = 1.5`
  - the printed reflow footprint row `P 1.50 / SL 0.750 / SP 0.650 / SR 0.900 / Hx 27.500 / Hy 27.500`
  - the printed figure identity `Reflow soldering footprint for BGA225 (SOT648-1)`
- not exact for:
  - all `1.50 mm` BGA or PBGA packages
  - cross-vendor `1.50 mm` footprint defaults
  - handbook `MIN / MAX / recommended` generic framing
  - connector-origin or installation-mark doctrine

## Admitted Data

- NXP prints this named package identity:
  - `BGA225`
  - `SOT648-1`
- NXP prints this package pitch:
  - `e = 1.5`
- NXP prints this reflow footprint geometry row:
  - `P 1.50`
  - `SL 0.750`
  - `SP 0.650`
  - `SR 0.900`
  - `Hx 27.500`
  - `Hy 27.500`

## Conditions And Methods

- Treat this card as one owner-scoped package-information row for the named `BGA225 / SOT648-1` package.
- Keep the `1.50 mm` pitch and reflow-footprint geometry attached to the NXP package identity and document context.
- Use this card when a prompt needs one safe current-public `1.50 mm` pitch replacement row and can stay inside named-package scope.
- Use this card to show that the `1.50 mm` residual is no longer limited to standards metadata or legacy near-hit language.
- Pair this card with:
  - [bga-1p50mm-pitch-standards-existence-boundary.md](/code/blogs/llm_wiki/facts/methods/bga-1p50mm-pitch-standards-existence-boundary.md)
  - [nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md](/code/blogs/llm_wiki/facts/methods/nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md)

## Limits And Non-Claims

- This card does not authorize a universal `1.50 mm` BGA conversion table.
- It does not authorize direct equivalence between this NXP reflow-footprint row and every other vendor's pad terminology or package family.
- It does not authorize package-library defaults outside the named `BGA225 / SOT648-1` package.
- It does not close the remaining connector-origin or stronger installation-mark authority gaps.

## Relationship To Local PCB资料 Intake

- This card gives the package lane its first directly verified current-public owner-scoped `1.50 mm` named-package exact row.
- It narrows the residual state from `standards existence plus near-hit only` to `one named-package current-public exact row landed`.
- It still does not turn the blocked handbook table into a reusable generic pitch law.

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating secondary-PDF candidate:
  - `P4-215C2` page-28 `bga pitch-to-pad-diameter table`
- authority replacement used here:
  - official NXP package-information PDF `SOT648-1`
- exact-data shape:
  - vendor-scoped named-package BGA outline and reflow-footprint row

## Source Links

- https://www.nxp.com/docs/en/package-information/SOT648-1.pdf
