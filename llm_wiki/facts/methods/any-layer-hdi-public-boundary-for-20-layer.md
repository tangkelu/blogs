---
fact_id: "methods-any-layer-hdi-public-boundary-for-20-layer"
title: "Current public sources support any-layer HDI as a guarded 20-layer vocabulary layer, not as a generic numeric capability table"
topic: "any-layer HDI public boundary for 20-layer"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids:
  - "ipc-board-design-standards-page"
  - "ipc-2226a-hdi-standard-page"
  - "ipc-jpca-4104-toc"
  - "ipc-2315-legacy-hdi-guide-page"
  - "ipc-tm650-test-methods-index"
  - "ipc-microvia-reliability-warning-2019"
  - "ipc-stacked-microvia-reliability-paper"
  - "nasa-nepp-microvia-reliability-2006"
  - "panasonic-felios-frcc-page"
  - "mitsui-rcc-engineered-materials-page"
  - "arlon-controlled-flow-prepreg-application-page"
  - "arlon-37n-product-page"
  - "arlon-47n-product-page"
  - "ats-hdi-anylayer-page"
  - "ajinomoto-fine-techno-abf-page"
  - "mgc-bt-materials-page"
tags: ["20-layer", "hdi", "any-layer", "elic", "microvia", "build-up", "rcc", "abf", "gap-control"]
---

# Canonical Summary

> Public IPC, NASA, and manufacturer sources are now strong enough to support guarded `20-layer` writing that mentions `HDI`, sequential build-up, `FRCC`, `RCC`, low-flow / controlled-flow prepreg, `ABF`, `BT`, and microvia-reliability caution. They are still not strong enough to justify generic `ELIC` defaults, lamination-cycle counts, laser-via geometry tables, capture-pad tables, `IST` thresholds, or shop-level stacked-microvia promises in evidence packs.

## Stable Facts

- Public IPC pages confirm that `HDI` remains an active design-standards topic, while the older `IPC/JPCA-2315` guide should not be treated as a current universal rules table.
- Legacy `IPC/JPCA-4104` adds only a historical materials-taxonomy layer for `HDI` / `microvia` materials and should not be treated as current active IPC guidance.
- Public NASA and IPC reliability material supports treating microvias and stacked microvias as reliability-sensitive build-up structures rather than as default density upgrades with universally safe stack heights.
- IPC's 2019 public warning confirms that weak microvia interfaces may escape traditional fabrication acceptance and appear later under assembly or field stress.
- Panasonic's official `FRCC` page provides a guarded public anchor for resin-coated-copper / build-up-material-form vocabulary.
- Mitsui's official engineered-materials page provides a guarded public `RCC` anchor for resin-coated copper foil as a material form, not as a rigid-board stack rule.
- Arlon's official controlled-flow application page plus official `37N` and `47N` product pages provide a guarded public low-flow / controlled-flow prepreg identity layer, not a datasheet-grade process rule layer.
- AT&S's official HDI page provides a guarded supplier-side `Anylayer` architecture anchor showing that any-layer interconnection can be described in public microvia terms without turning that wording into a generic numeric capability table.
- Official Ajinomoto and MGC pages support `ABF` and `BT` as build-up-material classes, not as proof that a rigid `20-layer` board should default to substrate-style materials.

## Conditions And Methods

- Use this card when a `20-layer` article needs to explain why any-layer or stacked-microvia language requires caution and source discipline.
- Pair it with the current build-up/material-context card when discussing material families, and with licensed standards or supplier-specific evidence before discussing geometry, reliability qualification, or capability limits.
- Keep `AT&S` `Anylayer` wording attached to supplier-side architecture vocabulary, not to geometry tables, yield, or production approval.
- Use this card to block unsupported inheritance of old `ELIC` blog numbers into future evidence packs.

## Limits And Non-Claims

- This card does not support generic claims such as `10+` sequential lamination cycles, `40-80 μm` `RCC` defaults, `60-100 μm` laser-via diameters, `5-7` stacked-microvia limits, `200/300` `IST` cycle thresholds, or `2.5/2.5 mil` any-layer capability.
- It does not turn legacy `IPC/JPCA-4104` taxonomy or supplier-side `AT&S` `Anylayer` wording into current maintained IPC rules, geometry limits, or factory capability.
- It does not prove that a given `20-layer` design should use no-core `ELIC`, hybrid core-plus-build-up, or any specific material recipe.
- It does not turn `RCC`, low-flow prepreg, or controlled-flow prepreg wording into dielectric-thickness rules, lamination recipes, or rigid-board-default architecture.
- It does not establish authenticity, qualification, or release authority for any shop-specific `HDI` capability statement.

## Open Questions

- Add a stronger public product-grade source layer for current build-up dielectric families only if stable official datasheets can be confirmed beyond the current guarded `FRCC` / `RCC` / low-flow product-identity anchors.
- Reassess `20-layer` readiness again after future public source recovery for build-up materials or current performance-specification metadata.

## Source Links

- https://www.electronics.org/ipc-board-design-standards
- https://shop.electronics.org/ipc-2226/ipc-2226-standard-only/Revision-a/english
- https://www.electronics.org/TOC/IPC-JPCA-4104.pdf
- https://shop.electronics.org/ipc-2315/ipc-2315-standard-only/Revision-0/english
- https://www.electronics.org/test-methods
- https://www.ipc.org/news-release/ipc-issues-electronics-industry-warning-printed-board-microvia-reliability-high
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/felios-series/series/42051
- https://ats.net/en/products/hdi-printed-circuit-boards/
- https://www.aft-website.com/en/products/insulating_film-abf/
- https://www.mgc.co.jp/eng/products/sc/btprint/
