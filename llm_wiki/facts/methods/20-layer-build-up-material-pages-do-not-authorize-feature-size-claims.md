---
fact_id: "methods-20-layer-build-up-material-pages-do-not-authorize-feature-size-claims"
title: "20-layer build-up material pages do not authorize feature-size claims for rigid-board capability"
topic: "20-layer build-up material pages and feature-size claim boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-26"
source_ids:
  - "ipc-jpca-4104-toc"
  - "panasonic-felios-frcc-page"
  - "panasonic-megtron-6-family-page"
  - "panasonic-megtron-6-halogen-free-page"
  - "agc-fastrise-family-page"
  - "agc-bond-plies-prepregs-page"
  - "agc-meteorwave-1000nf-page"
  - "ventec-ultrathin-build-up-datasheet-page"
  - "ventec-vt-47lt-datasheet-page"
  - "ventec-pro-bond-4c-vt-464lt-rcc-datasheet-page"
  - "resonac-mcl-hs200-build-up-page"
  - "resonac-mcl-e700g-build-up-page"
  - "resonac-mcl-e705g-build-up-page"
  - "mitsui-rcc-engineered-materials-page"
  - "rogers-2929-bondply-datasheet"
  - "arlon-controlled-flow-prepreg-application-page"
  - "arlon-37n-product-page"
  - "arlon-47n-product-page"
  - "ajinomoto-fine-techno-abf-page"
  - "mgc-bt-materials-page"
  - "isola-370hr-datasheet"
  - "ats-hdi-anylayer-page"
tags: ["20-layer", "build-up", "materials", "feature-size", "geometry", "boundary", "gap-control", "hdi"]
---

# Canonical Summary

> Current official build-up, `bond ply`, `RCC`, `FRCC`, ultrathin, and supplier-side any-layer material pages are strong enough to support guarded material-form and architecture vocabulary for `20-layer` writing. They are not strong enough to authorize feature-size claims, via minima, aspect-ratio claims, registration windows, or factory-capability statements for rigid `20-layer` boards.

## Stable Facts

- Official build-up-oriented material pages can support guarded vocabulary such as `FRCC`, `RCC`, `bond ply`, `bondply`, `controlled-flow prepreg`, `no-flow prepreg`, `ultrathin build-up`, `ABF`, and `BT`.
- Those pages can support the statement that some material families are publicly positioned for `HDI`, build-up construction, or sequential-lamination context.
- Panasonic `FRCC` is a guarded material-form anchor, not a rigid-board feature-size or geometry source.
- `RCC` identity pages and `bondply` pages can support resin-coated-copper or unreinforced-bonding-layer vocabulary, not laser-via, drill, or capture-pad limits.
- Supplier-side wording such as `Any-layer HDI Designs`, `Sequential Laminations`, `stacked or staggered microvias`, or `high reliability for HDI designs` can remain as page-positioning context only.
- Public any-layer architecture wording can support guarded architecture vocabulary, not transferable rigid-board capability claims.
- Historical `IPC/JPCA-4104` material taxonomy can support legacy `HDI` / `microvia` materials vocabulary, not current geometry rules.
- Build-up material families can be named as examples of material-form or application context without becoming proof that ordinary rigid `20-layer` boards use substrate-style constructions.
- Public build-up material pages may imply process sensitivity or application direction, but they do not provide a Tier 1 dated capability record for rigid-board feature-size claims.
- The presence of build-up, microvia, or any-layer terms on an official material page does not authorize minimum line/space, minimum laser via, minimum drill, stacked-via height, or aspect-ratio numbers.
- The presence of `HDI` or `sequential lamination` wording on a material page does not authorize registration windows, cumulative misregistration tables, or production-readiness conclusions.
- Material-form and family-positioning pages remain useful as negative-control sources: they help explain what a material family is, while also showing that capability numerics still require separate source control.

## Conditions And Methods

- Use this card when a `20-layer` draft starts to turn build-up material pages into drill, via, line/space, or registration capability evidence.
- Use this card as a containment layer whenever `FRCC`, `RCC`, `bond ply`, `bondply`, `no-flow`, `controlled-flow`, `ultrathin`, `ABF`, `BT`, or supplier any-layer wording appears near geometry claims.
- Pair this card with the current `20-layer` rewrite guardrails and material-boundary cards so material-form vocabulary does not silently become feature-size proof.
- Prefer wording such as `is publicly positioned as`, `is a material-form anchor`, `belongs to build-up vocabulary`, and `does not by itself authorize geometry claims`.
- Keep any-layer or build-up material references attached to architecture vocabulary or material-form identity, not to capability verbs such as `supports`, `achieves`, `allows`, or `can manufacture`.
- When feature-size, via, aspect-ratio, registration, or capability language appears, require a separate current primary source instead of inheriting authority from the material page.

## Limits And Non-Claims

- This card does not authorize minimum line/space claims for rigid `20-layer` boards.
- It does not authorize minimum mechanical-drill, minimum laser-via, capture-pad, stacked-via, skip-via, or blind/buried-via geometry claims.
- It does not authorize aspect-ratio claims, registration windows, cumulative misregistration tables, or layer-to-layer alignment numerics.
- It does not authorize stack-recipe claims, lamination-count claims, or process-window claims from material-form pages alone.
- It does not turn supplier-side `any-layer`, `HDI`, `sequential lamination`, or `high reliability` wording into factory-capability evidence.
- It does not turn `FRCC`, `RCC`, `bondply`, `no-flow prepreg`, or `controlled-flow prepreg` identity into rigid-board-default architecture or manufacturability proof.
- It does not turn build-up-material application language into accepted interconnect-reliability, qualification, or production-yield evidence.
- It does not replace the need for separate governance over `drill_and_via_geometry`, registration, or other fabrication-capability buckets.

## Open Questions

- Add a narrower cross-reference if future `20-layer` work creates a dedicated feature-size or geometry boundary card tied directly to the `drill_and_via_geometry` governance branch.
- Reassess whether any build-up-material page can support more than vocabulary only if a future source batch adds a separate current primary authority for the exact rigid-board capability claim.

## Source Links

- https://www.electronics.org/TOC/IPC-JPCA-4104.pdf
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/felios-series/series/133871
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/lineup/megtron-series/series/127603
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/megtron-series/series/127605
- https://www.agc-multimaterial.com/fastrise/
- https://www.agc-multimaterial.com/bond-plies-prepregs/
- https://www.ventec-group.com/cht/products/special-applications/ultrathin/datasheet/
- https://www.ventec-group.com/cht/products/lead-free-assembly/vt-47lt/datasheet/
- https://www.ventec-group.com/cht/products/bondply/pro-bond-4c-vt-464lt-rcc/datasheet/
- https://eu.resonac.com/project/hs200/
- https://eu.resonac.com/project/e700gr/
- https://eu.resonac.com/project/e705g/
- https://www.mitsui-kinzoku.com/en/seihin/engineered_materials/
- https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/2929-bondply-data-sheet.pdf
- https://www.arlon-med.com/products/controlled-flow-prepreg/
- https://www.arlon-med.com/products/37n/
- https://www.arlon-med.com/products/47n/
- https://www.aft-website.com/en/products/insulating_film-abf/
- https://www.mgc.co.jp/eng/products/sc/btprint/
- https://www.isola-group.com/wp-content/uploads/data-sheets/370hr-laminate-prepreg.pdf
- https://ats.net/en/products/hdi-printed-circuit-boards/
