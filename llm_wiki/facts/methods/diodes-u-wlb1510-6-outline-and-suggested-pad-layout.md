---
fact_id: "methods-diodes-u-wlb1510-6-outline-and-suggested-pad-layout"
title: "Diodes U-WLB1510-6 values are reusable only as the named package outline and suggested pad layout from DMN1016UCB6"
topic: "Diodes U-WLB1510-6 named-package outline and suggested pad layout"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-05-11"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_outline_and_suggested_pad_layout"
canonical_unit_policy: "Preserve original Diodes millimeter values and figure labels such as D, E, e, C, and C1. Keep the visible `1.50` attached to package body dimension `D`, not package pitch `e`."
source_ids:
  - "diodes-dmn1016ucb6-u-wlb1510-6-outline-and-suggested-pad-layout"
tags: ["diodes", "dmn1016ucb6", "u-wlb1510-6", "wlb", "1.50-mm-body", "suggested-pad-layout", "exact-data", "footprint"]
---

# Canonical Summary

> Diodes' `DMN1016UCB6` datasheet is strong enough to support one narrow exact-data layer for the package lane: the local corpus may reuse the named `U-WLB1510-6` package identity, printed package-outline values, and printed `Suggested Pad Layout` dimensions when the package identity and document context stay attached. This card is a vendor-scoped named-package page only. It does not authorize a `1.50 mm pitch` rule, because the visible `1.50` in this document belongs to package body dimension `D` while the printed pitch is `e = 0.50`.

## Exact Data Scope

- exact for:
  - Diodes' printed `U-WLB1510-6` package identity
  - the printed outline values `D 1.40 / 1.50 / 1.50`
  - the printed outline values `E 0.90 / 1.00 / 1.00`
  - the printed package pitch `e = 0.50`
  - the printed suggested-pad-layout values `C 0.50 / C1 1.00 / D 0.25`
- not exact for:
  - all `1.50 mm` pitch packages
  - all WLB packages
  - cross-vendor footprint defaults
  - handbook generic pitch tables

## Admitted Data

- Diodes prints this named package identity:
  - `U-WLB1510-6`
- Diodes prints these package-outline values:
  - `D 1.40 / 1.50 / 1.50`
  - `E 0.90 / 1.00 / 1.00`
  - `e 0.50`
- Diodes prints these suggested-pad-layout values:
  - `C 0.50`
  - `C1 1.00`
  - `D 0.25`
- Diodes prints this mounting note:
  - `Device mounted on FR-4 PCB with minimum recommended pad layout`

## Conditions And Methods

- Treat this card as one owner-scoped exact-data page for the named `U-WLB1510-6` package.
- Keep the outline values and suggested-pad-layout geometry attached to the Diodes package identity and datasheet context.
- Use this card when a prompt needs one safe current-public exact-geometry example for a named small-package owner page.
- Use this card to show that visible `1.50` package geometry can belong to package body size rather than package pitch, while still preserving the exact owner-scoped footprint page.

## Limits And Non-Claims

- This card does not authorize a `1.50 mm pitch -> land pattern` rule.
- It does not authorize direct equivalence between this Diodes suggested-pad-layout page and every other WLB or CSP package.
- It does not authorize package-library defaults outside the named `U-WLB1510-6` package.
- It does not reopen the current BGA/CSP `1.50 mm pitch` residual by itself.

## Relationship To Local PCB资料 Intake

- This card gives the package lane one more current-public owner exact-geometry example with named-package scope.
- It also strengthens the local search discipline by recording one official case where visible `1.50` belongs to package body dimension rather than package pitch.
- It does not replace the current `1.50 mm` BGA/CSP owner stack or public IPC geometry boundary.

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating continuation:
  - post-`P4-510` owner same-surface exact-geometry scout
- authority replacement used here:
  - official Diodes datasheet `DMN1016UCB6`
- exact-data shape:
  - vendor-scoped named-package outline and suggested-pad-layout page

## Source Links

- https://www.diodes.com/datasheet/download/DMN1016UCB6.pdf
