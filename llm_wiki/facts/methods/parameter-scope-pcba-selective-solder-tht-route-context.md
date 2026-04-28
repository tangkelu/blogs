---
fact_id: "methods-parameter-scope-pcba-selective-solder-tht-route-context"
title: "Selective-solder and THT parameter cards may use route-stage vocabulary and page-scoped values without turning them into general process settings"
topic: "PCBA parameter scope for selective solder and THT route context"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcba-pcb-selective-soldering-page-en"
  - "frontendhil-through-hole-assembly-product-page-en"
  - "frontendapt-blog-selective-solder-design-en"
  - "frontendapt-blog-wave-solder-fixture-intro-en"
  - "frontendapt-pcba-quality-system-page-en"
tags: ["parameter-scope", "pcba", "selective-solder", "through-hole", "tht", "mixed-technology", "route-selection"]
---

# Canonical Summary

> For selective solder and THT, the reusable parameter layer is mainly route-stage vocabulary plus geometry / access / thermal-review context. Real values may appear only as page-scoped examples from one named source context, especially on the HIL through-hole page, and must never be promoted into generic process settings or acceptance defaults.

## Source-Backed Parameters

- The APT selective-solder page supports route-stage terms `flux application`, `preheating`, `soldering`, `post-solder cleaning`, and `inspection`.
- The same page supports application-method vocabulary such as `miniature solder wave nozzle` and `laser soldering`, plus the distinction between selective, wave, manual, and reflow routes.
- The HIL through-hole page contains page-scoped numeric examples such as `10-50 N per pin` for press-fit, `>90% coverage` for ICT/FCT in that page's trust bar, and several wave / THT numeric examples in its marketing copy.
- The selective-solder design and wave-fixture sources support the review dimensions `access`, `shadowing`, `nearby SMT protection`, `board support`, and `fixture opening` as route-selection inputs.
- The quality-system page supports post-solder inspection and electrical-validation placement inside the larger release flow.

## Scope And Applicability Limits

- Use this card for `selective-wave-soldering-medical-imaging-wearable`, `tht-through-hole-soldering-medical-imaging-wearable`, and `tht-through-hole-soldering-renewable-energy-inverter`.
- Safe broad reuse: route-stage order, mixed-technology route choice, access review, thermal-demand review, and shielding / support vocabulary.
- Page-scoped values from the HIL through-hole page may be cited only as `HIL page-stated examples` or `HIL page marketing-context values`, never as generic engineering defaults.
- If a later draft needs exact dwell, preheat, conveyor, barrel-fill, press-fit, or hole-fill numbers, it must refresh them from the exact named source and keep the value tagged to that source context in the same sentence.

## Explicit Blocked Uses

- Do not turn HIL through-hole page values into generic selective-solder recipes, wave recipes, THT acceptance thresholds, or press-fit standards.
- Do not use page-scoped values as void thresholds, coating thickness or cure defaults, or any other unrelated process window.
- Do not use these sources to make HIL capability claims, universal Class 2 / Class 3 claims, yield claims, cost claims, or lead-time claims.
- Do not convert access-review language into dimensioned nozzle, keep-out, fixture-wall, or lead-protrusion rules without stronger primary evidence.
- Do not treat marketing examples from the HIL page as neutral industry standards.

## Blog Usage

- empty-image slugs: `selective-wave-soldering-medical-imaging-wearable`, `tht-through-hole-soldering-medical-imaging-wearable`, `tht-through-hole-soldering-renewable-energy-inverter`
- families supported:
  - `selective-solder`
  - `through-hole-assembly`
  - `mixed-technology-route-selection`

## Open Questions

- The HIL through-hole page contains many numeric claims, but several are marketing-scope or standards-adjacent; a future pass should split which of those deserve dedicated higher-trust source backing versus permanent quarantine.
- If inverter content later needs real terminal, busbar, or press-fit thresholds, that should be a separate card with product or standard sources.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/pcb-selective-soldering.json
- /code/hileap/frontendHIL/public/static/products/en/through-hole-assembly.json
- /code/hileap/frontendAPT/public/static/blogs/2025/12/en/selective-solder-design.md
- /code/hileap/frontendAPT/public/static/blogs/2025/12/en/wave-solder-fixture-intro.md
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
