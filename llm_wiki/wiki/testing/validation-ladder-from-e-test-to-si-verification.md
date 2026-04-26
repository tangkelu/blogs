---
topic_id: "testing-validation-ladder-from-e-test-to-si-verification"
title: "Validation Ladder From E-Test To SI Verification"
category: "testing"
status: "draft"
last_reviewed_at: "2026-04-24"
fact_ids:
  - "methods-rf-validation-capability"
  - "methods-advanced-validation-scope-segmentation"
  - "methods-spi-aoi-ict-boundaries"
source_ids:
  - "frontendhil-rogers-product-page-en"
  - "frontendhil-high-frequency-product-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
  - "frontendapt-pcb-quality-page-en"
  - "frontendapt-backplane-pcb-page-en"
  - "frontendhil-backplane-product-page-en"
  - "koh-young-spi-technology"
  - "koh-young-aoi-technology"
  - "keysight-ict-systems"
tags: ["testing", "validation", "e-test", "ict", "aoi", "tdr", "vna", "si"]
---

# Definition

> The validation ladder from e-test to SI verification is a layered way to describe board evidence: baseline electrical checks, optical and assembly inspection, impedance correlation, and higher-order signal-integrity validation each answer a different question.

## Why This Topic Matters

- RF and high-speed content is easy to overstate when `e-test`, `AOI`, `ICT`, `TDR`, and `VNA` are blended into one undifferentiated proof claim.
- The existing internal corpus already points to a staged model, but the evidence is split across quality, RF capability, and inspection-boundary fact cards.
- This page gives wiki consumers a stable vocabulary for separating routine manufacturing verification from deeper SI-oriented validation.

## Stable Facts

- Internal RF capability pages converge on a common validation stack that includes `impedance coupons`, `TDR`, sample-based or project-based `VNA` work, and traceability.
- Internal quality and high-speed pages separate baseline electrical continuity or isolation checks from deeper SI-oriented measurements and destructive metrology.
- The same corpus places `microsection`, finish metrology, AOI, X-ray, and reliability or environmental checks in the broader quality system rather than as synonyms for RF validation.
- Internal high-speed and backplane pages describe `TDR/VNA` as channel or SI verification layers on top of standard fabrication controls.
- External inspection-boundary sources reinforce that `SPI`, `AOI`, and `ICT` cover different defect classes and board stages.
- Taken together, the current sources support a ladder that runs from board-level electrical defect coverage to impedance correlation and then to RF/SI verification.

## Engineering Boundaries

- Do not describe `AOI`, `ICT`, `TDR`, and `VNA` as interchangeable proof of RF performance.
- Keep `baseline manufacturing quality`, `electrical fault coverage`, `impedance verification`, and `channel or S-parameter validation` as separate evidence layers.
- Avoid turning optional or program-specific advanced validation into an unconditional standard-scope claim.
- When writing about coverage, distinguish whether the claim is about `defect detection`, `impedance correlation`, `SI behavior`, or `environmental reliability`.
- If a page needs exact maximum frequency, fixture scope, report depth, or guaranteed coverage percentage, re-check current engineering availability before publication.

## Common Misreadings

- A board passing `electrical test` does not automatically prove RF channel performance.
- `AOI` and `X-ray` can identify assembly defects, but they do not replace impedance or `VNA`-based correlation.
- `TDR` is not the same thing as full-path insertion-loss or S-parameter validation.
- Listing `VNA` on a capability page does not mean every order receives the same frequency range or reporting depth.
- `ICT` belongs to assembled-board electrical defect coverage, not to upstream paste or optical inspection.

## Must Refresh Before Publishing

- Any exact maximum validated frequency or current `VNA` ceiling
- Any claim about standard-scope versus optional-scope validation packages
- Any customer-facing commitment on report depth, fixture type, or environmental-test conditions

## Related Fact Cards

- `methods-rf-validation-capability`
- `methods-advanced-validation-scope-segmentation`
- `methods-spi-aoi-ict-boundaries`

## Primary Sources

- /code/hileap/frontendHIL/public/static/products/en/rogers-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/microwave-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-quality.json
- /code/hileap/frontendAPT/public/static/pcb/en/backplane-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/backplane-pcb.json
- https://kohyoung.com/en/solder-paste-inspection-technology/
- https://kohyoung.com/en/automated-optical-inspection-technology/
- https://www.keysight.com/us/en/products/in-circuit-test-for-manufacturing/in-circuit-test-systems.html
