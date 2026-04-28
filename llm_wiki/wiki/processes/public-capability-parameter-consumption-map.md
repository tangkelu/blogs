---
topic_id: "processes-public-capability-parameter-consumption-map"
title: "Public Capability Parameter Consumption Map"
category: "processes"
status: "draft"
last_reviewed_at: "2026-04-27"
fact_ids:
  - "methods-parameter-scope-public-capability-drilling-and-via-geometry"
  - "methods-parameter-scope-public-capability-impedance-and-validation"
  - "methods-parameter-scope-public-capability-construction-windows"
  - "methods-parameter-scope-public-capability-coating-and-fine-pitch-assembly"
  - "methods-internal-json-coverage-boundary"
source_ids:
  - "frontendapt-pcb-drilling-page-en"
  - "frontendapt-pcb-pcb-impedance-control-page-en"
  - "frontendapt-hdi-pcb-capability-page-en"
  - "frontendapt-rigid-flex-pcb-capability-page-en"
  - "frontendapt-pcb-pcb-conformal-coating-page-en"
  - "frontendapt-pcba-pcb-conformal-coating-page-en"
  - "frontendapt-pcba-bga-qfn-fine-pitch-page-en"
  - "frontendhil-hdi-pcb-product-page-en"
  - "frontendhil-rigid-flex-pcb-product-page-en"
  - "frontendhil-teflon-pcb-product-page-en"
  - "frontendhil-smt-assembly-product-page-en"
  - "frontendhil-high-speed-product-page-en"
tags: ["processes", "public-site-claim", "parameters", "prompt-consumption", "governance"]
---

# Definition

> This map defines how prompt inputs may consume parameter-like numbers from local English APT and HIL public JSON pages. It exists to keep `public-site claimed capability` separate from stronger evidence classes such as dated capability records, qualification sources, standards thresholds, or lot-release proof.

## Why This Topic Matters

- The local English public JSON pages contain many useful parameter claims.
- The same pages are marketing-adjacent service or product pages, not dated Tier 1 capability records.
- Without a consumption map, prompts tend to merge page-scoped claims into one invented factory capability sheet.

## Allowed Use

- Use the four parameter-scope fact cards as page-scoped prompt support.
- Preserve the family context:
  drilling, HDI, PTFE, rigid-flex, coating, fine-pitch assembly, or SMT assembly.
- Preserve qualifiers such as `standard`, `advanced`, `typical`, `possible after DFM review`, `sample-based`, `with TDR`, `risk-based`, and `specific rigid areas`.
- Use them to support conservative public drafting about manufacturability, routing, validation posture, inspection flow, or application-fit context.

## Disallowed Use

- Do not rewrite these page claims as independently verified factory capability.
- Do not convert them into supplier-independent industry defaults.
- Do not use them as lot capability, release criteria, or qualification proof.
- Do not use them as acceptance thresholds for impedance, voiding, cleanliness, bend radius, drill tolerance, or backdrill residual stub.
- Do not merge numbers from unrelated page families into one synthetic table unless the prompt explicitly says they are separate page claims.

## Recommended Consumption Order

1. Pick the family:
   drilling and via geometry, impedance and validation, construction windows, or coating and fine-pitch assembly.
2. Pull only the fact card that matches the draft’s topic family.
3. Keep the exact `source_id` and page path attached to each parameter you reuse.
4. Add application boundary cards if the draft enters medical, automotive, RF/mmWave, optical, or power-safety territory.
5. Strip any wording that upgrades a page claim into a guarantee, threshold, qualification, or cross-supplier truth.

## Decision Rules

- If the prompt needs `can the site publicly say X exists`:
  these cards are usable.
- If the prompt needs `what exact public parameter does this English page claim`:
  these cards are usable.
- If the prompt needs `what can the factory actually hold today across lots`:
  these cards are not sufficient.
- If the prompt needs `what threshold proves acceptance or compliance`:
  these cards are not sufficient.

## Claim Ceiling

- Maximum safe statement:
  `the English public site page claims` or `the page presents`.
- Unsafe upgrade:
  `the factory can`, `the supplier guarantees`, `the process is qualified to`, `all lots meet`, or `industry standard is`.

## Primary Sources

- /code/hileap/frontendAPT/public/static/pcb/en/pcb-drilling.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-impedance-control.json
- /code/hileap/frontendAPT/public/static/capabilities/en/hdi-pcb.json
- /code/hileap/frontendAPT/public/static/capabilities/en/rigid-flex-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-conformal-coating.json
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-conformal-coating.json
- /code/hileap/frontendAPT/public/static/pcba/en/bga-qfn-fine-pitch.json
- /code/hileap/frontendHIL/public/static/products/en/hdi-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/rigid-flex-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/teflon-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/smt-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/high-speed-pcb.json
