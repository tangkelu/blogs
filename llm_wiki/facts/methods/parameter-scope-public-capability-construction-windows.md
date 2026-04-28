---
fact_id: "methods-parameter-scope-public-capability-construction-windows"
title: "English public HDI, rigid-flex, and PTFE pages expose page-scoped construction-window parameters"
topic: "Public-site capability parameter scope for construction windows"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-hdi-pcb-capability-page-en"
  - "frontendapt-rigid-flex-pcb-capability-page-en"
  - "frontendhil-rigid-flex-pcb-product-page-en"
  - "frontendhil-teflon-pcb-product-page-en"
tags: ["internal", "public-site-claim", "parameters", "layer-count", "thickness", "copper", "rigid-flex", "ptfe", "stackup"]
---

# Canonical Summary

> The English public HDI, rigid-flex, and PTFE pages contain explicit layer-count, thickness, copper-weight, flex-core, lamination, and bend-radius claims. These are usable only as page-scoped public parameter context and must not be rewritten as one consolidated factory capability sheet.

## Extracted Public-Site Claimed Parameters

- APT HDI capability page:
  `Up to 32 Layers (Standard), 64 Layers (Advanced)`, `0.40 mm – 8.0 mm PCB thickness`, `0.5–2 oz finished copper`, `up to 3 oz in specific rigid core layers`, `0.001" (0.025 mm) min flex core thickness`, and `up to 4 sequential laminations`.
  Source:
  `frontendapt-hdi-pcb-capability-page-en` -> `/code/hileap/frontendAPT/public/static/capabilities/en/hdi-pcb.json`
- APT rigid-flex capability page:
  `up to 32 layers`, `2.5/2.5 mil trace/space`, `0.025 mm flex core`, `0.075 mm microvia`, `up to 2 sequential laminations`, `0.3 mm BGA/CSP pitch`, and `up to 10 oz in specific rigid areas`.
  Source:
  `frontendapt-rigid-flex-pcb-capability-page-en` -> `/code/hileap/frontendAPT/public/static/capabilities/en/rigid-flex-pcb.json`
- HIL rigid-flex product page:
  `2–12 layers total` with `up to 30+ layers advanced`, `0.4–3.2 mm standard thickness`, `0.2 mm flex to 5.0 mm rigid advanced`, `0.5–2 oz standard copper`, `up to 6 oz rigid sections`, `0.15 mm mechanical hole`, `0.075 mm laser microvia`, `10× flex thickness dynamic bend radius`, `6× flex thickness static bend radius`, and `±5% with TDR` impedance as advanced posture.
  Source:
  `frontendhil-rigid-flex-pcb-product-page-en` -> `/code/hileap/frontendHIL/public/static/products/en/rigid-flex-pcb.json`
- HIL PTFE product page:
  `1–20 layers standard`, `40+ layers advanced`, `0.20–3.20 mm standard thickness`, `0.10–6.00 mm advanced thickness`, `0.5–2 oz standard copper`, `up to 5 oz advanced`, `75/75 μm standard trace/space`, and `50/50 μm advanced`.
  Source:
  `frontendhil-teflon-pcb-product-page-en` -> `/code/hileap/frontendHIL/public/static/products/en/teflon-pcb.json`

## Scope

- Claim class:
  `public website claim`
- Page context:
  English APT capability pages and English HIL product pages for HDI, rigid-flex, and PTFE families
- Language:
  `en`
- Checked date:
  `2026-04-27`

## Consumption Rules

- Treat each page as a family-specific construction window, not as a universal plant-wide master table.
- Keep `standard`, `advanced`, `specific rigid areas`, and `dynamic vs static` qualifiers attached to the extracted value.
- Rigid-flex mechanical guidance such as bend radius belongs to rigid-flex family prompts only; do not leak it into standard rigid-board prompts.
- PTFE stackup and thickness values belong to PTFE / fluoropolymer context and should not be generalized to all RF boards.

## Non-Generalization

- These claims are not supplier-independent proof.
- They are not lot capability, production release evidence, or program-by-program authorization.
- They are not qualification or durability proof by themselves.
- They are not acceptance thresholds for bend life, thickness tolerance, or copper performance.
- They do not prove all layer counts, copper windows, or stackups are available on every line or every quote.

## Blog Usage

- Supports `rf-5g`, `mmwave`, and `antenna-system` families for PTFE and hybrid-stackup framing.
- Supports `medical imaging / wearable`, `industrial robotics / control`, and `ai-server / optical high-speed` families for HDI and rigid-flex packaging context.
- Supports `power-energy` families only when copper/thickness are discussed as page-scoped options, not as guaranteed heavy-copper proof.
- Does not authorize prompt outputs to invent stackups, generic thickness windows, or bend-life guarantees.

## Source Links

- /code/hileap/frontendAPT/public/static/capabilities/en/hdi-pcb.json
- /code/hileap/frontendAPT/public/static/capabilities/en/rigid-flex-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/rigid-flex-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/teflon-pcb.json
