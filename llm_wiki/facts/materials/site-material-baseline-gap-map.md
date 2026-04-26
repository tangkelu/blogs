---
fact_id: "materials-site-material-baseline-gap-map"
title: "Site-mentioned materials need baseline llm_wiki coverage before blog consumption"
topic: "Site material baseline coverage"
category: "materials"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-materials-arlon-pcb-page-en"
  - "frontendapt-materials-isola-pcb-page-en"
  - "frontendapt-materials-megtron-pcb-page-en"
  - "frontendapt-materials-remaining-index-en"
  - "frontendapt-materials-taconic-pcb-page-en"
  - "frontendapt-materials-teflon-pcb-page-en"
  - "frontendapt-materials-spread-glass-fr4-page-en"
  - "frontendhil-rogers-product-page-en"
  - "frontendhil-teflon-pcb-product-page-en"
  - "frontendhil-ceramic-pcb-product-page-en"
  - "frontendhil-high-thermal-pcb-product-page-en"
  - "frontendhil-remaining-products-index-en"
tags: ["internal", "materials", "baseline", "coverage-gap", "site-mentioned"]
---

# Canonical Summary

> Materials already mentioned on APT/HIL non-blog pages should have at least baseline `llm_wiki` coverage. Internal pages identify the public service vocabulary, while official manufacturer sources decide product-level facts.

## Stable Facts

- APT/HIL non-blog content mentions Rogers, Isola, Panasonic MEGTRON, Taconic, Arlon, AGC, Ventec, PTFE/Teflon, FR-4, spread-glass FR-4, polyimide, metal-core/IMS, ceramic, alumina, AlN, BT resin, and ABF-style substrate materials.
- Rogers, Isola, Panasonic, Ventec, and AGC already have multiple official source records in `llm_wiki`.
- Arlon now has official directory/product/guide anchors, but many named Arlon grades still need product-level datasheets before parameter extraction.
- Taconic remains a controlled gap for product-level values because stable official product datasheet anchors have not yet been verified.
- Generic ceramic, alumina, AlN, BT resin, ABF, LCP, and flex-polyimide film sources still need official class-level or manufacturer anchors if future blogs use numeric claims.

## Conditions And Methods

- Use this card to decide whether a blog draft is relying on a material named by the sites but missing official source coverage.
- Treat site mentions as a coverage trigger, not as a datasheet.
- Before publication, refresh any material value against official manufacturer data.

## Limits And Non-Claims

- This card does not validate every numeric value present in the two sites.
- It does not claim all site-mentioned materials are stocked, recommended, or available.
- It does not provide product-level material constants.

## Open Questions

- Confirm Taconic product-level source anchors.
- Confirm Arlon product-level datasheets for the exact grades named in APT.
- Add generic ceramic / AlN / alumina / BT / ABF / LCP anchors if those topics become blog priorities.

## Source Links

- /code/hileap/frontendAPT/public/static/materials/en/arlon-pcb.json
- /code/hileap/frontendAPT/public/static/materials/en/isola-pcb.json
- /code/hileap/frontendAPT/public/static/materials/en/megtron-pcb.json
- /code/hileap/frontendAPT/public/static/materials/en
- /code/hileap/frontendAPT/public/static/materials/en/taconic-pcb.json
- /code/hileap/frontendAPT/public/static/materials/en/teflon-pcb.json
- /code/hileap/frontendAPT/public/static/materials/en/spread-glass-fr4.json
- /code/hileap/frontendHIL/public/static/products/en/rogers-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/teflon-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/ceramic-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-thermal-pcb.json
