---
fact_id: "materials-abf-and-bt-substrate-source-coverage"
title: "ABF and BT substrate material classes are officially anchored for IC-substrate context"
topic: "IC substrate materials"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids:
  - "frontendhil-ic-substrate-pcb-product-page-en"
  - "frontendapt-pcb-advanced-pcb-manufacturing-page-en"
  - "ajinomoto-abf-innovation-story"
  - "ajinomoto-fine-techno-abf-page"
  - "mgc-bt-materials-page"
tags: ["abf", "bt", "ic-substrate", "package-substrate", "build-up", "official-source"]
---

# Canonical Summary

> ABF and BT are now covered as official-source material classes for IC-substrate and advanced build-up discussions, but grade-level values remain gated on current manufacturer datasheets.

## Stable Facts

- HIL/APT non-blog content includes IC-substrate and advanced PCB manufacturing contexts where build-up material classes such as ABF and BT can become relevant.
- Ajinomoto and Ajinomoto Fine-Techno provide official ABF background and product-family pages.
- Mitsubishi Gas Chemical provides an official page for laminated materials for printed circuit boards / BT materials.
- These sources support class-level framing for package-substrate and IC-substrate blogs.

## Conditions And Methods

- Use ABF sources for build-up film / insulating-film context in high-performance semiconductor substrate discussions.
- Use the MGC BT source as a BT-material class anchor, not as a complete property table.
- Require current grade-level datasheets before publishing Dk, Df, CTE, Tg, modulus, laser-drilling, desmear, or reliability values.

## Limits And Non-Claims

- This card does not choose ABF or BT for a customer design.
- It does not assert HIL/APT can manufacture every ABF or BT package-substrate structure.
- It does not replace customer stackup, substrate vendor, or OSAT/package-house requirements.

## Open Questions

- Add grade-specific ABF and BT datasheets if future content needs material-constant tables or package-substrate design windows.

## Source Links

- /code/hileap/frontendHIL/public/static/products/en/ic-substrate-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/advanced-pcb-manufacturing.json
- https://www.ajinomoto.com/innovation/our_innovation/buildupfilm
- https://www.aft-website.com/en/products/insulating_film-abf/
- https://www.mgc.co.jp/eng/products/sc/btprint/
