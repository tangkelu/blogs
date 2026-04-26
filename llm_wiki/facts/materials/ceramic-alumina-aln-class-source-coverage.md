---
fact_id: "materials-ceramic-alumina-aln-class-source-coverage"
title: "Ceramic, alumina, and AlN material-class coverage is official-source anchored but not parameter-ready"
topic: "Ceramic PCB materials"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids:
  - "frontendhil-ceramic-pcb-product-page-en"
  - "frontendhil-high-thermal-pcb-product-page-en"
  - "frontendapt-pcb-ceramic-pcb-page-en"
  - "ceramtec-ceramic-substrates-page"
  - "maruwa-aln-substrates-page"
tags: ["ceramic", "alumina", "aln", "thermal-pcb", "site-mentioned", "official-source"]
---

# Canonical Summary

> Site-mentioned ceramic, alumina, and AlN material classes now have official manufacturer anchors, but numeric material-property tables still require a current product datasheet refresh.

## Stable Facts

- HIL/APT non-blog pages mention ceramic PCB and high-thermal material contexts, including ceramic-family language that can include alumina and AlN.
- CeramTec has an official ceramic substrate page that identifies common ceramic substrate material classes, including alumina and aluminum nitride.
- MARUWA has an official Aluminum Nitride (AlN) substrate page.
- These sources are suitable for class-level blog framing around ceramic, alumina, and AlN substrates.

## Conditions And Methods

- Use this card when a blog needs to introduce ceramic PCB material families or compare thermal-platform options at a high level.
- Attach a current product-specific datasheet before publishing numeric thermal conductivity, dielectric, CTE, thickness, metallization, or processing claims.

## Limits And Non-Claims

- This card does not certify HIL/APT ceramic manufacturing limits.
- It does not validate any specific ceramic stackup, metallization process, or material grade.
- It does not claim alumina and AlN are interchangeable.

## Open Questions

- Add product-level official datasheets if future blogs compare alumina, AlN, BeO-free alternatives, DBC, AMB, IMS, or metal-core PCB structures.

## Source Links

- /code/hileap/frontendHIL/public/static/products/en/ceramic-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-thermal-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/ceramic-pcb.json
- https://www.ceramtec-group.com/en/ceramtec-us/substrates
- https://www.maruwa-g.com/e/products/ceramic/000314.html
