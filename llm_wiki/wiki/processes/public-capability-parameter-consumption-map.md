---
topic_id: "processes-public-capability-parameter-consumption-map"
title: "Public Capability Parameter Consumption Map"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
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
tags: ["processes", "public-site-claim", "parameters", "prompt-consumption", "governance", "active-routing"]
---

# Definition

> This map is active for consuming parameter-like numbers from local English APT and HIL public JSON pages. It keeps every extracted value inside `public-site claimed capability` scope and blocks upgrades into dated factory capability, acceptance criteria, qualification proof, standards thresholds, or lot-release evidence.

## Routing Guidance

- Start by classifying the parameter family: drilling and via geometry, impedance and validation, construction windows, or coating and fine-pitch assembly.
- Pull only the matching fact card and preserve the original page family, source ID, and qualifier language with every reused number.
- Use `methods-internal-json-coverage-boundary` only to explain source inventory and page-registration scope, not to upgrade parameter claims.
- Add adjacent application or standards boundary cards if the draft enters medical, automotive, RF/mmWave, optical, power-safety, or regulated territory.
- Stop and mark a source gap if the prompt needs lot capability, qualification proof, compliance thresholds, or release criteria.

## Stable Facts

- The landed parameter fact cards support explicit public-site claimed numbers for drilling, microvia, backdrill, impedance, TDR or VNA posture, construction windows, coating thickness vocabulary, fine-pitch assembly values, and inspection-coverage language.
- Those values are page-scoped to named English APT service or capability pages and named English HIL product pages, not normalized into one plant-wide master capability table.
- Qualifiers such as `standard`, `advanced`, `typical`, `possible after DFM review`, `sample-based`, `with TDR`, `validated process`, `specific rigid areas`, `dynamic`, and `static` are part of the usable fact and must stay attached.
- `methods-internal-json-coverage-boundary` confirms that internal JSON inventory and extracted fact cards are separate layers: page coverage does not automatically create a stronger evidence class.
- Across this page, the safe claim ceiling remains `the English public site page claims` or `the page presents`.

## Allowed Use

- Use the four parameter-scope fact cards as page-scoped prompt support.
- Preserve the family context:
  drilling, HDI, PTFE, rigid-flex, coating, fine-pitch assembly, or SMT assembly.
- Preserve qualifiers such as `standard`, `advanced`, `typical`, `possible after DFM review`, `sample-based`, `with TDR`, `risk-based`, and `specific rigid areas`.
- Use them to support conservative public drafting about manufacturability, routing, validation posture, inspection flow, or application-fit context.

## Blocked Claims

- Do not rewrite public-site page claims as independently verified factory capability, lot capability, or guaranteed production performance.
- Do not convert page-scoped values into supplier-independent industry defaults or cross-supplier truths.
- Do not use these values as acceptance thresholds for impedance, voiding, cleanliness, bend radius, drill tolerance, backdrill residual stub, coating thickness, or inspection disposition.
- Do not use these values as qualification proof, compliance proof, release criteria, shipment criteria, or standards pass/fail thresholds.
- Do not merge unrelated page families into one synthetic capability sheet unless the prompt explicitly preserves them as separate page claims.
- Do not let source inventory coverage become evidence that every indexed page has dedicated fact extraction or verified capability status.

## Common Misreadings

- `the factory can hold this value on all lots` when the source only says a public page claims it
- `this is the supplier standard capability` when the number appears only in one family-specific page context
- `with TDR`, `sample-based VNA`, and `100% TDR` all mean the same validation posture
- rigid-flex bend-radius values or PTFE stackup windows apply to all rigid boards
- coating thickness, void, cleanliness, or placement figures from public pages are automatic release criteria
- page inventory coverage proves qualification, certification, or current production availability

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

## Must Refresh Before Publishing

- Any statement framed as current capability, current default production window, or current guaranteed tolerance.
- Any product-line, quote-stage, or line-wide capability table assembled from multiple page families.
- Any acceptance threshold, pass/fail rule, or standards-compliance statement.
- Any supplier-specific availability, lead-time, qualification, or deployment statement.

## Related Facts And Source Scope

- `methods-parameter-scope-public-capability-drilling-and-via-geometry` governs mechanical drill, laser via, backdrill, aspect-ratio, and HDI geometry claims.
- `methods-parameter-scope-public-capability-impedance-and-validation` governs impedance targets, tolerance wording, and TDR or VNA validation posture.
- `methods-parameter-scope-public-capability-construction-windows` governs layer-count, thickness, copper, rigid-flex, PTFE, and bend-radius claims.
- `methods-parameter-scope-public-capability-coating-and-fine-pitch-assembly` governs conformal-coating, fine-pitch, hidden-joint, inspection, and cleanliness page claims.
- `methods-internal-json-coverage-boundary` governs page-inventory and extraction-layer separation only.
- Source scope for this page is limited to the already-landed local English public JSON records listed in frontmatter; no URL-only refreshes belong in this lane.

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
