---
fact_id: "methods-inspection-planning-around-connector-and-shield-obstructions"
title: "Inspection planning around connectors and shields should be framed as visibility and method selection, not universal coverage"
topic: "Inspection planning around connector and shield obstructions"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-05-01"
source_ids:
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "frontendapt-pcba-x-ray-inspection-page-en"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-bga-qfn-fine-pitch-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "frontendapt-pcba-pcb-selective-soldering-page-en"
tags: ["inspection", "connector", "shield", "visibility", "x-ray", "aoi", "methods"]
---

# Canonical Summary

> Connectors, shields, brackets, and dense hidden-joint features change what inspection can see. The safe position is to choose inspection methods around visibility and access, not to assume one method covers every obstruction.

## Stable Facts

- The X-ray pages support hidden-joint visibility for dense packages and concealed solder features.
- The AOI page supports visible geometry and placement checks, but not hidden-joint coverage.
- The ICT and flying-probe pages support electrical verification through different access models.
- The quality-system and selective-solder pages show that obstruction-aware inspection planning belongs with the assembly route, not after it.

## Conditions And Methods

- Use this card when a draft needs to explain how connector overhang, shield cans, or dense parts affect method choice.
- Separate visible inspection, hidden-joint inspection, and fixture/probe access into distinct review items.
- Keep the language at planning level: visibility, obstruction, access, and method selection.

## Limits And Non-Claims

- This card does not define universal coverage percentages or mandatory X-ray rules.
- It does not authorize dimensioned inspection layouts or pass/fail thresholds.
- It does not prove one method is sufficient for every dense assembly.

## Open Questions

- Add a narrower camera-module or optical-module inspection card later if a future batch needs more exact package-specific wording.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/x-ray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/bga-qfn-fine-pitch.json
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-selective-soldering.json
