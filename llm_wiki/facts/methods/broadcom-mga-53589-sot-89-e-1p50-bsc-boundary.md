---
fact_id: "methods-broadcom-mga-53589-sot-89-e-1p50-bsc-boundary"
title: "Broadcom MGA-53589 exposes non-BGA `e = 1.50 BSC`, not same-surface PCB geometry"
topic: "Broadcom MGA-53589 non-BGA pitch-identity boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-12"
exact_data_class: "boundary_convention"
scope_type: "owner_scoped_non_bga_pitch_identity_without_same_surface_geometry"
canonical_unit_policy: "Preserve the product-brief pitch statement `e = 1.50 BSC` only as a non-BGA owner-scoped pitch identity. Do not normalize it into a BGA/CSP pitch row or same-surface footprint authority."
source_ids:
  - "broadcom-mga-53589-product-brief-sot-89-e-1p50-bsc"
tags: ["broadcom", "avago", "sot-89", "pitch", "1.50-bsc", "false-positive-filter", "boundary"]
---

# Canonical Summary

> Broadcom's MGA-53589 product brief is strong enough to support one narrow owner-scoped false-positive filter for the current `1.50 mm` package residual: it visibly exposes `e = 1.50 BSC` on a non-BGA `SOT-89` package surface. That is useful as a split-surface boundary, but it does not expose same-surface PCB land-pattern geometry and therefore does not reopen the `1.50 mm` BGA/CSP residual.

## Stable Facts

- The official Broadcom product brief visibly states `e = 1.50 BSC`.
- The package context is `SOT-89`, not the current BGA/CSP residual family.
- The same surface does not expose printed PCB land-pattern or footprint geometry.

## Limits And Non-Claims

- This card does not authorize a `1.50 mm` BGA/CSP reopen.
- It does not authorize same-surface footprint geometry.
- It does not authorize a universal `1.50 mm pitch -> land pattern` rule.

## Source Links

- https://docs.broadcom.com/wcs-public/products/data-sheets--technical-specifications/product-brief/237/316/av02-1308en.pdf
