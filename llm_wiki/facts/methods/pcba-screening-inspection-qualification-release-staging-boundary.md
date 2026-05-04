---
fact_id: "methods-pcba-screening-inspection-qualification-release-staging-boundary"
title: "PCBA screening, inspection, qualification, and release staging should stay as separate governance layers"
topic: "PCBA screening inspection qualification release staging boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendapt-pcba-incoming-quality-control-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "frontendapt-pcba-final-quality-inspection-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
tags: ["pcba", "screening", "inspection", "qualification", "release", "staging", "quality", "boundary"]
---

# Canonical Summary

> PCBA governance language is safest when `screening`, `inspection`, `qualification`, and `release staging` stay separate. Electrical screening can narrow defect risk, inspection can confirm visible or hidden build features, qualification remains a broader program-level question, and release staging is the handoff logic that accumulates evidence across gates.

## Stable Facts

- Incoming quality, first-article, final inspection, and test pages describe a staged quality flow rather than one collapsed pass/fail event.
- Flying probe and ICT support electrical screening vocabulary.
- X-ray supports hidden-joint inspection vocabulary.
- FCT supports powered behavior validation vocabulary.
- The quality-system page places these activities inside one broader governance flow rather than treating them as interchangeable labels.

## Conditions And Methods

- Use this card when a rewrite needs to separate defect screening from inspection and from later qualification language.
- Keep `qualification` as a higher-order program or program-family word unless a stronger source stack exists.
- Treat `release staging` as evidence accumulation across gates, not as proof of final product success.

## Limits And Non-Claims

- This card does not define qualification criteria.
- It does not prove a board, line, or supplier is qualified.
- It does not authorize acceptance thresholds, coverage numbers, or release authority.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/incoming-quality-control.json
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/final-quality-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/testing-quality.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
