---
topic_id: "materials-flex-material-classes-pi-lcp-and-rigid-flex-boundaries"
title: "Flex Material Classes: PI, LCP, And Rigid-Flex Boundaries"
category: "materials"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "materials-flex-polyimide-and-lcp-class-source-coverage"
  - "materials-flex-exact-product-anchor-map"
  - "standards-ipc-flex-rigid-flex-standards-hierarchy-boundary"
source_ids:
  - "frontendhil-flex-pcb-product-page-en"
  - "frontendhil-rigid-flex-pcb-product-page-en"
  - "frontendapt-pcb-flex-pcb-page-en"
  - "frontendapt-pcb-rigid-flex-pcb-page-en"
  - "panasonic-felios-series-page"
  - "panasonic-felios-lcp-page"
  - "panasonic-felios-frcc-page"
  - "panasonic-r-f705s-product-summary-pdf"
  - "ube-upilex-grade-details"
  - "ube-upilex-advantages-page"
  - "dupont-kapton-hn-product-page"
  - "dupont-kapton-hn-data-sheet"
  - "agc-n7000-3f-datasheet"
tags: ["materials", "flex-pcb", "rigid-flex", "polyimide", "lcp", "frcc", "kapton", "upilex", "routing", "boundaries"]
---

# Routing Summary

> Route `PI` and `LCP` as material classes. Route `rigid-flex` as a board architecture and manufacturing context. Route `FRCC` only as a narrow source-owner material/form-factor lane, not as a synonym for generic flex, RCC, or rigid-flex construction. Keep exact-product anchors separate from class-level routing.

## Classification Matrix

| Term | Route As | Safe Use | Do Not Collapse Into |
|---|---|---|---|
| `PI` / `polyimide` | material class | generic flex-material family wording | `rigid-flex`, universal bend claims, one exact product |
| `LCP` | material class | source-scoped flex-material family wording | generic PI substitute, universal RF outcome |
| `FRCC` | narrow material/form-factor lane | Panasonic `R-FR10` style exact-product framing | generic `RCC`, generic prepreg, rigid-flex architecture |
| `rigid-flex` | architecture class | board construction and manufacturing route | material identity, PI grade, LCP grade |

## What This Page Governs

- Use this page when a draft mixes `flex PCB`, `PI`, `LCP`, `FRCC`, and `rigid-flex` as if they were the same layer of meaning.
- Use `flex PCB` and `rigid-flex PCB` as product or architecture routes from HIL/APT service context.
- Use `PI` and `LCP` when the sentence is about material family identity.
- Use exact-product names only when the sentence needs a source-owner anchor.

## Material-Class Routing

### PI / Polyimide

- `PI` is a material-class label, not a board architecture.
- The corpus has narrow exact-product PI anchors across film and laminate examples:
  - `UPILEX-S`
  - `Kapton HN`
  - `85N`
  - `85NT`
  - `N7000-3F`
- These anchors support source-scoped wording only. They do not make all PI films, PI laminates, and rigid-flex builds interchangeable.

### LCP

- `LCP` is also a material-class label.
- The current corpus uses Panasonic `FELIOS LCP` for class-level context and `R-F705S` for a narrow exact-product anchor.
- `LCP` may be routed as a distinct flex-material family, but not as a generic substitute for all `PI` materials or all flex constructions.

### FRCC

- `FRCC` is not the same route as `PI` or `LCP`.
- In this corpus, `FRCC` is a narrow Panasonic-owned lane anchored by `R-FR10`.
- Treat it as an exact material/form-factor branch for guarded discussion of flexible resin-coated copper context.
- Do not convert `FRCC` into generic `RCC`, generic bond-ply language, or a default rigid-board build-up dielectric claim.

## Architecture Routing

### Rigid-Flex

- `rigid-flex` is an architecture and manufacturing route, not a material class.
- A rigid-flex board may use PI-family materials, but the architecture name does not prove any one material system.
- Routing a draft into `rigid-flex` means the next authority layer is construction, design, and performance-specification context, not automatic material substitution.
- For standards context, keep `IPC-2223E` and `IPC-6013E` as design/performance family anchors distinct from rigid-board `IPC-6012F`.

## Exact-Product Anchor Boundary

| Anchor | Route | Boundary |
|---|---|---|
| `UPILEX-S` | exact-product PI film | not generic PI, not rigid-flex proof |
| `Kapton HN` | exact-product PI film | not all Kapton grades, not bend-life proof |
| `85N` | exact-product PI laminate | not generic flex-film shorthand |
| `85NT` | exact-product PI nonwoven-aramid laminate | not interchangeable with `85N` |
| `N7000-3F` | exact-product toughened filled PI laminate | not a standard PI-film example |
| `R-F705S` | exact-product LCP material | not universal LCP or RF-flex proof |
| `R-FR10` | exact-product FRCC material | not generic `RCC`, not rigid-flex architecture |

## Safe Prompting Rules

- If the prompt says `flex PCB material`, first decide whether it means material class or board architecture.
- If the prompt says `rigid-flex material`, split the claim into architecture plus separately evidenced material.
- If the prompt says `Kapton`, `UPILEX`, `R-F705S`, `R-FR10`, `85N`, `85NT`, or `N7000-3F`, keep the sentence tied to that exact product.
- If the prompt needs standards framing, route flex and rigid-flex language through the `IPC-2223E` / `IPC-6013E` hierarchy, not through rigid-board `IPC-6012F` alone.

## Non-Claims And Stop Lines

- This page does not prove bend-cycle guarantees.
- This page does not prove `Dk` or `Df` without exact-product datasheet support.
- This page does not authorize architecture-to-material substitution claims.
- This page does not support cost, lead-time, or yield claims.
- This page does not prove that HIL/APT production uses any named PI, LCP, or FRCC product.

## Related Fact Cards

- `materials-flex-polyimide-and-lcp-class-source-coverage`
- `materials-flex-exact-product-anchor-map`
- `standards-ipc-flex-rigid-flex-standards-hierarchy-boundary`

## Primary Sources

- /code/hileap/frontendHIL/public/static/products/en/flex-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/rigid-flex-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/flex-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/rigid-flex-pcb.json
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/lineup/felios-series
- https://industrial.panasonic.com/ww/products/pt/felios/felioslcp
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/felios-series/series/133871
- https://industrial.panasonic.com/content/data/EM/PDF/DataS_FELIOS_R-F705S_en_202508.pdf
- https://www.ube.com/ube/en/contents/chemical/polyimide/upilex/upilex_grade.html
- https://www.ube.com/ube/en/contents/chemical/polyimide/upilex/upilex.html
- https://www.dupont.com/electronics-industrial/product-family/kapton-hn.html
- https://www.dupont.com/content/dam/dupont/amer/us/en/ei-transformation/public/documents/en/EI-10206-Kapton-HN-Data-Sheet.pdf
- https://www.agc-multimaterial.com/agc-downloads/AGC_N7000-3F_TDS.pdf
