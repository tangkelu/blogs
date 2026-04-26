---
fact_id: "materials-hil-base-laminate-and-build-stage-family-map"
title: "HIL internal product pages split baseline PCB offerings by laminate family, layer complexity, and build stage"
topic: "HIL baseline laminate and build-stage family map"
category: "materials"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendhil-fr4-pcb-product-page-en"
  - "frontendhil-halogen-free-pcb-product-page-en"
  - "frontendhil-high-tg-pcb-product-page-en"
  - "frontendhil-multilayer-pcb-product-page-en"
  - "frontendhil-single-double-layer-pcb-product-page-en"
tags: ["hilpcb", "fr4", "halogen-free", "high-tg", "multilayer", "single-double-layer", "internal", "materials"]
---

# Canonical Summary

> HIL's baseline product family is internally segmented by laminate posture and build complexity: `single/double-layer` covers simple cost-sensitive boards, `FR-4` covers the mainstream multilayer baseline, `high-Tg` and `halogen-free` are positioned as constrained FR-4-family variants for thermal or compliance needs, and `multilayer` covers stackup and registration complexity beyond low-layer routing.

## Stable Facts

- The HIL single/double-layer page frames 1-2 layer boards as the low-complexity, cost-sensitive entry point for basic routing and quick-turn demand.
- The HIL FR-4 page frames standard, high-Tg, and lower-loss FR-4 options as the broad mainstream laminate family rather than as one fixed material definition.
- The HIL high-Tg page reframes FR-4-family selection around thermal and reflow resilience, Z-axis stability, and harsher operating conditions.
- The HIL halogen-free page reframes FR-4-family selection around environmental and safety positioning, low-smoke language, and regulated-application fit.
- The HIL multilayer page shifts the discussion from laminate identity toward stackup architecture, registration, via strategy, sequential lamination, and impedance-related controls.
- Taken together, these pages form an internal routing map from simple low-layer boards toward more demanding multilayer and requirement-driven laminate choices.

## Conditions And Methods

- Use this card when deciding which HIL page family should support a draft about baseline PCB options before jumping into specialty RF, ceramic, metal-core, or HDI topics.
- Treat the five source pages as product-family and service-scope framing, not as final material-property authority.
- If a draft needs exact Tg bands, loss values, compliance thresholds, or lead-time promises, refresh against stronger primary sources or current internal operations data.

## Limits And Non-Claims

- This card does not define universal FR-4, high-Tg, or halogen-free numeric properties.
- It does not claim that single/double-layer, FR-4, and multilayer are mutually exclusive categories; they overlap as routing and stackup complexity grows.
- It does not prove that every multilayer job is suitable for high-Tg, halogen-free, or low-loss material without project review.

## Open Questions

- Add a later routing card that cleanly separates `baseline FR-4 family choice` from `specialty material choice` across both HIL and APT.

## Source Links

- /code/hileap/frontendHIL/public/static/products/en/fr4-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/halogen-free-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-tg-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/multilayer-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/single-double-layer-pcb.json
