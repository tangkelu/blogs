---
topic_id: "materials-ceramic-aln-ims-thermal-platforms"
title: "Ceramic, AlN, And IMS Thermal Platforms"
category: "materials"
status: "draft"
last_reviewed_at: "2026-04-24"
fact_ids:
  - "materials-ceramic-alumina-aln-class-source-coverage"
source_ids:
  - "frontendhil-ceramic-pcb-product-page-en"
  - "frontendhil-high-thermal-pcb-product-page-en"
  - "frontendapt-pcb-ceramic-pcb-page-en"
  - "ceramtec-ceramic-substrates-page"
  - "maruwa-aln-substrates-page"
  - "ventec-ims-family-overview"
tags: ["materials", "ceramic", "alumina", "aln", "ims", "thermal-management"]
---

# Definition

> Ceramic, AlN, and IMS thermal-platform selection should start with platform class, not with isolated conductivity numbers. The first question is whether the design needs a ceramic substrate family, an AlN-specific ceramic option, or an insulated metal substrate path for thermal management.

## Why This Topic Matters

- HIL/APT public pages already talk about ceramic PCB and high-thermal contexts, so the wiki needs a clean thermal-platform framing layer.
- Current official anchors support class-level explanations for ceramic, alumina, AlN, and IMS, but they do not yet justify a frozen cross-vendor property table.
- Without a governance page, it is easy to flatten ceramic and metal-base platforms into one generic "high thermal PCB" claim.

## Stable Facts

- HIL/APT non-blog pages mention ceramic PCB and high-thermal platform contexts.
- CeramTec provides an official ceramic substrate page covering ceramic substrate classes, including alumina and aluminum nitride.
- MARUWA provides an official Aluminum Nitride substrate page.
- Ventec provides an official IMS / thermal-management family page for metal-base laminate context.
- These sources are sufficient to frame ceramic/alumina/AlN as ceramic-substrate families and IMS as a separate thermal-management platform family.

## Engineering Boundaries

- Use ceramic-family sources for class framing, not for vendor-neutral numeric rankings.
- Keep `alumina`, `AlN`, and `IMS` as distinct thermal-platform buckets unless a current datasheet comparison is attached.
- Treat thermal conductivity, dielectric strength, CTE, dielectric constant, thickness, metallization, and bonding-stack claims as refresh-required.
- Do not infer manufacturability limits, metallization compatibility, or package suitability from class-level sources alone.
- Use IMS sources to anchor the existence of metal-base thermal-management families, not to claim equivalence with ceramic substrates.

## Common Misreadings

- `High thermal` does not mean ceramic and IMS are interchangeable.
- `AlN` is not a synonym for the whole ceramic PCB category.
- A class-level ceramic source does not prove a specific direct-bond, active-metal-braze, or thick-film process.
- Internal high-thermal service copy does not replace manufacturer-controlled material sources.

## Must Refresh Before Publishing

- Any thermal conductivity value
- Any dielectric or CTE comparison
- Any statement about exact metallization system or layer build
- Any claim that one thermal platform is universally better than another
- Any specific substrate grade, thickness, or process window

## Related Fact Cards

- `materials-ceramic-alumina-aln-class-source-coverage`

## Primary Sources

- /code/hileap/frontendHIL/public/static/products/en/ceramic-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-thermal-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/ceramic-pcb.json
- https://www.ceramtec-group.com/en/ceramtec-us/substrates
- https://www.maruwa-g.com/e/products/ceramic/000314.html
- https://www.ventec-group.com/products/tec-thermal-thermal-management-ims/
