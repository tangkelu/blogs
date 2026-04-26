---
fact_id: "materials-flex-polyimide-and-lcp-class-source-coverage"
title: "Flex polyimide and LCP material classes now have both class-level anchors and narrow Panasonic exact-product exceptions"
topic: "Flexible PCB materials"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-25"
source_ids:
  - "frontendhil-flex-pcb-product-page-en"
  - "frontendhil-rigid-flex-pcb-product-page-en"
  - "frontendapt-pcb-flex-pcb-page-en"
  - "frontendapt-pcb-rigid-flex-pcb-page-en"
  - "panasonic-felios-series-page"
  - "panasonic-felios-lcp-page"
  - "panasonic-felios-frcc-page"
  - "panasonic-r-f705s-product-summary-pdf"
tags: ["flex-pcb", "rigid-flex", "polyimide", "lcp", "felios", "official-source"]
---

# Canonical Summary

> Flexible-material coverage now has official class-level anchors for flex / rigid-flex discussion, plus two narrow Panasonic product-grade exceptions: `R-F705S` for `LCP` and `R-FR10` for `FRCC`. Generic `polyimide / Kapton / UPILEX / adhesiveless flex` numerics still remain under gap-control.

## Stable Facts

- HIL/APT non-blog pages include flex PCB and rigid-flex PCB service contexts.
- Panasonic's official FELIOS series page covers flexible circuit-board materials.
- Panasonic's official FELIOS LCP page covers LCP (Liquid Crystal Polymer) flexible circuit-board materials.
- Panasonic's official `R-F705S` page and linked product-summary PDF now support one exact-product `LCP` numeric row with stated conditions.
- Panasonic's official `FELIOS FRCC` page now supports one exact-product `R-FR10` material row for guarded `FRCC` / resin-coated-copper discussion.
- These sources can now support both high-level family discussion and a narrow Panasonic-only exact-product layer.

## Conditions And Methods

- Use this card for class-level discussion of flex and rigid-flex materials, especially when `LCP` is relevant to RF/mobile applications.
- Use `R-F705S` only as a Panasonic exact-product `LCP` exception, not as a stand-in for generic flex or rigid-flex `LCP`.
- Use `R-FR10` only as a Panasonic exact-product `FRCC` exception, not as a stand-in for generic `RCC`, prepreg, or rigid-board build-up dielectric.
- When a draft says `polyimide`, `Kapton`, `UPILEX`, or `adhesiveless flex`, attach a product-specific source if the claim goes beyond generic family framing.
- For bend reliability, copper type, adhesiveless construction, cycle life, and generic rigid-flex numerics, keep the branch under explicit gap-control.

## Limits And Non-Claims

- This card does not assert a universal flex stackup rule.
- It does not validate Panasonic FELIOS as the material used by HIL/APT.
- It does not turn one Panasonic `LCP` or `FRCC` row into generic `polyimide`, `Kapton`, `UPILEX`, or rigid-flex numeric coverage.
- It does not provide bend-radius, cycle-life, or IPC qualification values.

## Open Questions

- Add another official polyimide flex-laminate source if future blogs require direct PI-specific supplier data rather than Panasonic-centric flex-material coverage.

## Source Links

- /code/hileap/frontendHIL/public/static/products/en/flex-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/rigid-flex-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/flex-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/rigid-flex-pcb.json
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/lineup/felios-series
- https://industrial.panasonic.com/ww/products/pt/felios/felioslcp
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/felios-series/series/133871
- https://industrial.panasonic.com/content/data/EM/PDF/DataS_FELIOS_R-F705S_en_202508.pdf
