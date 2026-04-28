---
fact_id: "methods-2025-7-mixed-service-draft-consumption-boundary"
title: "2025.7 mixed Rogers / PCBA / SMT / THT / keyboard drafts route to existing data layers but do not prove Highleap capability"
topic: "2025.7 mixed service draft consumption boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids:
  - "rogers-ro3000-datasheet"
  - "rogers-ro3003-product-page"
  - "rogers-ro3006-product-page"
  - "rogers-ro4003c-product-page"
  - "rogers-ro4350b-product-page"
  - "rogers-ro3000-fabrication-guidelines"
  - "frontendapt-materials-rf-rogers-page-en"
  - "frontendapt-materials-rogers-pcb-manufacturing-page-en"
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendapt-pcba-turnkey-assembly-page-en"
  - "frontendhil-smt-assembly-product-page-en"
  - "frontendhil-through-hole-assembly-product-page-en"
  - "frontendhil-turnkey-assembly-product-page-en"
  - "frontendapt-pcba-spi-inspection-page-en"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-pcb-stencil-page-en"
  - "frontendapt-pcba-pcb-selective-soldering-page-en"
  - "frontendapt-pcba-bga-qfn-fine-pitch-page-en"
tags: ["2025-7", "rogers", "pcba", "smt", "tht", "keyboard", "highleap", "draft-boundary"]
---

# Canonical Summary

> The `/code/blogs/tmps/2025.7/en` batch should be consumed as a small routing layer into existing `llm_wiki` facts: Rogers PCB maps to official Rogers and RF-process cards; PCBA service, SMT assembly, and through-hole assembly map to existing PCBA process and inspection cards; keyboard PCB types remain claim inventory only. The drafts do not prove Highleap capability, equipment, quality outcomes, production scale, cost, lead time, yield, market positioning, or keyboard performance.

## Stable Facts

- The batch contains five temporary drafts: `Rogers PCB.md`, `keyboard-pcb-types.md`, `pcba-service.md`, `smt-assembly.md`, and `through-hole-assembly.md`.
- Current `llm_wiki` already has source-backed Rogers material and processing support through official Rogers records and registered internal Rogers framing.
- Current `llm_wiki` already has source-backed PCBA / SMT / THT workflow support through internal APT / HIL PCBA pages covering SMT/THT, turnkey assembly, inspection, ICT, FCT, stencil, selective solder, fine-pitch controls, and through-hole assembly.
- Current `llm_wiki` supports keyboard PCB content only at generic input-device and PCB / PCBA process-boundary level; it does not support keyboard product-performance or market claims from these drafts.

## Conditions And Methods

- Use `logs/p4-32-2025-7-mixed-service-blog-ingestion-map.md` before creating evidence packs from this batch.
- For Rogers writing, pull all material values and process boundaries from official Rogers and existing `llm_wiki` Rogers cards.
- For PCBA, SMT, and THT writing, pull workflow claims from mixed-technology assembly, layered inspection, stencil / selective-solder / fine-pitch, ICT/FCT, NPI / FAI, and THT route-boundary cards.
- For keyboard writing, pair this card with `methods-hilpcb-blog1-13-input-device-draft-consumption-boundary` and avoid product-performance, market, firmware, wireless, and commercial claims unless later sourced.
- Require a dated Highleap capability record before writing shop-specific capability, equipment, quality coverage, sourcing, volume, lead-time, or delivery claims.

## Limits And Non-Claims

- This card does not add new Rogers material values, RF design rules, cost models, process-control parameters, or finished-board performance claims.
- It does not prove Highleap SMT precision, speed, reliability, equipment level, automation, quality outcomes, test coverage, sourcing capability, scalability, prototype-to-mass-production readiness, or turnkey completeness.
- It does not prove through-hole solder-joint reliability, process parameters, selective-solder coverage, press-fit suitability, sector qualification, or durability outcomes.
- It does not prove keyboard market segmentation, keyboard PCB type ranking, hot-swap, RGB, wireless, firmware compatibility, consumer compliance, production cost, or scale-up performance.
- It does not authorize copying any numeric value, marketing claim, CTA, partner-selection promise, or commercial statement from the drafts into reusable facts.

## Open Questions

- Whether Highleap has dated capability records for SMT, THT, turnkey PCBA, component sourcing, inspection coverage, and volume ramp claims.
- Whether keyboard PCB type content should receive a separate source-backed lane for QMK / VIA, hot-swap sockets, RGB, wireless, and compliance before article generation.
- Whether the Italian `keyboard-pcb-types.md` draft should be normalized into an English claim inventory if it becomes a recurring topic source.

## Source Links

- https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro3000-laminate-data-sheet-ro3003----ro3006----ro3010----ro3035.pdf
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3003-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3006-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro4000-series-laminates/ro4003c-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro4000-series-laminates/ro4350b-laminates
- https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/fabrication-information/fabrication-guidelines-ro3000-and-ro3200-series-high-frequency-circuit-materials.pdf
- /code/hileap/frontendAPT/public/static/materials/en/rf-rogers.json
- /code/hileap/frontendAPT/public/static/materials/en/rogers-pcb-manufacturing.json
- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendAPT/public/static/pcba/en/turnkey-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/smt-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/through-hole-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/spi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-stencil.json
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-selective-soldering.json
- /code/hileap/frontendAPT/public/static/pcba/en/bga-qfn-fine-pitch.json
