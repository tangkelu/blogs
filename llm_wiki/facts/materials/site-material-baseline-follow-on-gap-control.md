---
fact_id: "materials-site-material-baseline-follow-on-gap-control"
title: "P4-08 follow-on closes material-class anchors while keeping product-level gaps controlled"
topic: "Site material baseline coverage"
category: "materials"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids:
  - "frontendhil-ceramic-pcb-product-page-en"
  - "frontendhil-flex-pcb-product-page-en"
  - "frontendhil-ic-substrate-pcb-product-page-en"
  - "frontendapt-pcb-ceramic-pcb-page-en"
  - "frontendapt-pcb-flex-pcb-page-en"
  - "frontendapt-pcb-advanced-pcb-manufacturing-page-en"
  - "ceramtec-ceramic-substrates-page"
  - "maruwa-aln-substrates-page"
  - "ajinomoto-fine-techno-abf-page"
  - "mgc-bt-materials-page"
  - "panasonic-felios-series-page"
  - "panasonic-felios-lcp-page"
tags: ["baseline", "coverage-gap", "site-mentioned", "materials", "source-governance"]
---

# Canonical Summary

> P4-08 adds official anchors for site-mentioned material classes, but it does not turn unresolved Taconic or Arlon product families into parameter-ready facts.

## Stable Facts

- Ceramic, alumina, AlN, ABF, BT, flexible circuit-board materials, and LCP now have official class-level source anchors.
- The new anchors are sufficient for blog planning, topic scoping, and evidence-pack discovery.
- Product-level Taconic and several Arlon grade anchors remain unresolved or incomplete.
- The baseline rule remains: internal site JSON can trigger coverage, but official manufacturer sources decide material facts.

## Conditions And Methods

- Use this card as a gate in blog readiness reviews when a draft mentions a material class already named by HIL/APT.
- If the blog uses only class-level framing, these anchors may be sufficient.
- If the blog uses numeric product values, a current grade-level datasheet must be registered or live-checked before publication.

## Limits And Non-Claims

- This card does not approve a full material-comparison table.
- It does not make Taconic TLY/TLX/TLC/TLE/RF-35 or Arlon 33N/35N/45N/47N/CLTE-XT/TC350/AD250/AD255/AD300 parameter-ready.
- It does not certify current availability, regional support, or supplier lead time.

## Open Questions

- Continue product-level recovery for Taconic and Arlon from official manufacturer-controlled pages only.
- Add direct PI-specific flexible-laminate sources if future flex blogs need PI values rather than class-level framing.

## Source Links

- /code/blogs/llm_wiki/facts/materials/site-material-baseline-gap-map.md
- https://www.ceramtec-group.com/en/ceramtec-us/substrates
- https://www.maruwa-g.com/e/products/ceramic/000314.html
- https://www.aft-website.com/en/products/insulating_film-abf/
- https://www.mgc.co.jp/eng/products/sc/btprint/
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/lineup/felios-series
- https://industrial.panasonic.com/ww/products/pt/felios/felioslcp
