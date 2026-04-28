---
fact_id: "methods-aptpcb260401-2-layer-draft-consumption-boundary"
title: "APTPCB260401 2-layer drafts are rewrite-intent inventory, not 2-layer design-rule or capability evidence"
topic: "APTPCB260401 2-layer draft consumption boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids:
  - "isola-fr408-datasheet"
  - "isola-fr408hr-datasheet"
  - "frontendapt-materials-spread-glass-fr4-page-en"
  - "rogers-ro3003-product-page"
  - "rogers-ro3006-product-page"
  - "rogers-ro4003c-product-page"
  - "rogers-ro4350b-product-page"
  - "frontendapt-materials-teflon-pcb-page-en"
  - "frontendhil-teflon-pcb-product-page-en"
  - "frontendapt-pcb-metal-core-pcb-page-en"
  - "frontendhil-metal-core-pcb-product-page-en"
  - "frontendapt-pcb-ceramic-pcb-page-en"
  - "frontendhil-ceramic-pcb-product-page-en"
  - "ceramtec-ceramic-substrates-page"
  - "maruwa-aln-substrates-page"
  - "frontendapt-pcb-surface-finishes-page-en"
  - "frontendhil-pcb-surface-finish-landing-en"
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendapt-pcba-turnkey-assembly-page-en"
  - "frontendapt-pcb-pcb-prototype-page-en"
  - "frontendapt-pcb-quick-turn-pcb-page-en"
  - "frontendapt-pcb-npi-small-batch-pcb-manufacturing-page-en"
  - "frontendapt-pcb-mass-production-pcb-manufacturing-page-en"
tags: ["aptpcb", "2-layer", "draft-boundary", "materials", "surface-finish", "quick-turn", "rewrite-gate"]
---

# Canonical Summary

> The APTPCB260401 English draft batch under `/code/blogs/tmps/APTPCB260401/en` should be consumed as 2-layer PCB topic intent, outline shape, and blocked-claim inventory. Existing `llm_wiki` cards can support conservative material-family, surface-finish, PCBA, thermal-platform, RF, prototype, and quick-turn context, but the drafts do not prove universal 2-layer design rules, material parameters, impedance geometry, thermal resistance, surface-finish chemistry, pricing, lead time, supplier capability, qualification, or APTPCB capability claims.

## Stable Facts

- The batch contains 27 temporary English drafts centered on 2-layer PCB variants, including FR-4, high-Tg, aluminum, copper core, ceramic, polyimide, PTFE, Teflon, Rogers, RF, microwave, HASL, lead-free HASL, OSP, ENIG, assembly, prototype, quick-turn, low-cost, manufacturer, and supplier topics.
- Existing `llm_wiki` support is broad enough for conservative context language across FR-4, Rogers, PTFE / RF processing, ceramic / alumina / AlN classes, flex / polyimide / LCP classes, IMS / MCPCB, surface-finish selection, PCBA flow, prototype / quick-turn routing, and RF validation.
- Existing support is not enough to recover draft-originated numeric design rules, material values, process windows, thermal calculations, impedance examples, price / lead-time claims, supplier audit claims, or application qualification claims.
- The matching ingestion map is `logs/p4-31-aptpcb260401-2-layer-blog-ingestion-map.md`.

## Conditions And Methods

- Use the P4-31 ingestion map before creating any evidence pack from this batch.
- Pull material values only from official product-level fact cards, not from the drafts.
- Pull surface-finish, PCBA, prototype, quick-turn, and RF-validation wording only from existing source-backed `llm_wiki` cards.
- Treat draft headings and sections as useful query / outline signals.
- Stop and require a separate source lane when the target article needs exact design rules, cost, lead time, qualification proof, supplier proof, or APTPCB capability.

## Limits And Non-Claims

- This card does not verify any 2-layer stackup default, board thickness, copper weight, trace width, spacing, annular ring, via, drill, impedance, current-capacity, thermal-resistance, or reflow-profile value.
- It does not verify ENIG, ENEPIG, HASL, lead-free HASL, or OSP chemistry values, shelf life, thickness, planarity, solderability, or black-pad prevention claims.
- It does not verify aluminum-core, copper-core, ceramic, alumina, AlN, polyimide, Kapton, PTFE, Teflon, Rogers, FR-4, or high-Tg material properties unless a separate product-specific source card is cited.
- It does not prove APTPCB quick-turn windows, low-cost positioning, MOQ, pricing, yield, throughput, equipment, direct-factory status, supplier qualification, VMI, inventory, lifecycle management, or production-scale readiness.
- It does not prove automotive, medical, aerospace, defense, satellite, 5G, drone, industrial, RoHS, halogen-free, or other application qualification or compliance status for any board or supplier.

## Open Questions

- Whether to create a 2-layer-specific rewrite gate that maps common article patterns to existing FR-4, Rogers, IMS, ceramic, finish, PCBA, and prototype / quick-turn cards.
- Whether APTPCB has dated capability records for 2-layer quick-turn, low-cost, mass-production, surface-finish, supplier, or process-limit claims.
- Whether additional official HASL / OSP / ENIG / ENEPIG source records are needed before surface-finish-specific 2-layer articles are generated.

## Source Links

- https://www.isola-group.com/wp-content/uploads/data-sheets/fr408-laminate-and-prepreg.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/fr408hr-laminate-and-prepreg.pdf
- /code/hileap/frontendAPT/public/static/materials/en/spread-glass-fr4.json
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3003-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3006-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro4000-series-laminates/ro4003c-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro4000-series-laminates/ro4350b-laminates
- /code/hileap/frontendAPT/public/static/materials/en/teflon-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/teflon-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/metal-core-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/metal-core-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/ceramic-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/ceramic-pcb.json
- https://www.ceramtec-group.com/en/ceramtec-us/substrates
- https://www.maruwa-g.com/e/products/ceramic/000314.html
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-surface-finishes.json
- /code/hileap/frontendHIL/data/service-landings/en/pcb-surface-finish.json
- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendAPT/public/static/pcba/en/turnkey-assembly.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-prototype.json
- /code/hileap/frontendAPT/public/static/pcb/en/quick-turn-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/npi-small-batch-pcb-manufacturing.json
- /code/hileap/frontendAPT/public/static/pcb/en/mass-production-pcb-manufacturing.json
