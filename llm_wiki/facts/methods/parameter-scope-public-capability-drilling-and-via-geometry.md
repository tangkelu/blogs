---
fact_id: "methods-parameter-scope-public-capability-drilling-and-via-geometry"
title: "English public PCB drilling and HDI pages expose a bounded set of public-site claimed drilling and via-geometry parameters"
topic: "Public-site capability parameter scope for drilling and via geometry"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcb-drilling-page-en"
  - "frontendapt-hdi-pcb-capability-page-en"
  - "frontendapt-pcb-hdi-pcb-page-en"
  - "frontendhil-hdi-pcb-product-page-en"
tags: ["internal", "public-site-claim", "parameters", "drilling", "microvia", "backdrill", "hdi", "geometry"]
---

# Canonical Summary

> The English public non-blog PCB drilling and HDI pages contain explicit parameter claims for minimum mechanical drill, minimum laser microvia, aspect ratio, backdrill depth control, residual stub, and line/space. These can be consumed only as `public-site claimed capability` from the named pages, not as independently verified factory capability.

## Extracted Public-Site Claimed Parameters

- `0.15 mm mechanical drill minimum` on the APT drilling page and APT HDI capability page.
  Source:
  `frontendapt-pcb-drilling-page-en` -> `/code/hileap/frontendAPT/public/static/pcb/en/pcb-drilling.json`
  and `frontendapt-hdi-pcb-capability-page-en` -> `/code/hileap/frontendAPT/public/static/capabilities/en/hdi-pcb.json`
- `0.10 mm CO2 laser microvia` and `0.075 mm UV laser microvia` on the APT drilling page.
  Source:
  `frontendapt-pcb-drilling-page-en` -> `/code/hileap/frontendAPT/public/static/pcb/en/pcb-drilling.json`
- `±50 μm backdrilling accuracy` and `residual stub under 200 μm` on the APT drilling page.
  Source:
  `frontendapt-pcb-drilling-page-en` -> `/code/hileap/frontendAPT/public/static/pcb/en/pcb-drilling.json`
- `15:1 validated process aspect ratio` for mechanical drilling on the APT drilling page.
  Source:
  `frontendapt-pcb-drilling-page-en` -> `/code/hileap/frontendAPT/public/static/pcb/en/pcb-drilling.json`
- `3/3 mil (0.076 mm) finished trace/space` with `2/2 mil (0.0508 mm) possible after DFM review` on the APT HDI capability page.
  Source:
  `frontendapt-hdi-pcb-capability-page-en` -> `/code/hileap/frontendAPT/public/static/capabilities/en/hdi-pcb.json`
- `0.003" (0.075 mm) min laser drill diameter` and `0.004" (0.10 mm) standard` on the APT HDI capability page.
  Source:
  `frontendapt-hdi-pcb-capability-page-en` -> `/code/hileap/frontendAPT/public/static/capabilities/en/hdi-pcb.json`
- `50–150 μm typical microvia diameter` on the APT PCB HDI page FAQ.
  Source:
  `frontendapt-pcb-hdi-pcb-page-en` -> `/code/hileap/frontendAPT/public/static/pcb/en/hdi-pcb.json`
- `50–75 μm laser microvias`, `≤1:1 microvia aspect ratio`, and `75/75 μm standard` with `50/50 μm advanced` trace/space on the HIL HDI product page.
  Source:
  `frontendhil-hdi-pcb-product-page-en` -> `/code/hileap/frontendHIL/public/static/products/en/hdi-pcb.json`

## Scope

- Claim class:
  `public website claim`
- Page context:
  English APT drilling page, English APT HDI capability page, English APT HDI PCB page, English HIL HDI product page
- Language:
  `en`
- Checked date:
  `2026-04-27`

## Consumption Rules

- Treat these numbers as page-scoped parameter claims, not as a normalized factory table.
- Keep the original context attached:
  drilling page, HDI capability page, HDI product page, or FAQ-level claim.
- If a prompt needs one parameter, prefer the narrowest matching source page instead of merging all values into one synthetic capability sheet.
- Values that are framed with `possible after DFM review`, `advanced`, `typical`, or `validated process` must keep those qualifiers.

## Non-Generalization

- These claims are not supplier-independent proof.
- They are not lot capability or line-release evidence.
- They are not qualification evidence.
- They are not acceptance thresholds or IPC pass/fail criteria.
- They do not prove every HDI or high-speed build receives the same drill, microvia, or stub-control window.

## Blog Usage

- Supports `rf-5g` and `telecom high-speed` empty-image families only for conservative routing, backdrill, and microvia vocabulary.
- Supports `ai-server / optical high-speed` empty-image families only for via-transition and HDI-density context.
- Supports `medical imaging / wearable` and `industrial robotics / control` families only when the draft stays at manufacturability and interconnect-planning scope.
- Does not by itself unlock any universal drill table, fabrication promise, or quote-stage factory capability list.

## Source Links

- /code/hileap/frontendAPT/public/static/pcb/en/pcb-drilling.json
- /code/hileap/frontendAPT/public/static/capabilities/en/hdi-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/hdi-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/hdi-pcb.json
