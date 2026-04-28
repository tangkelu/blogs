---
fact_id: "methods-pcba-electrical-test-vs-reliability-evidence-boundary"
title: "Electrical defect screening and functional test are not the same as reliability evidence"
topic: "PCBA electrical test versus reliability evidence boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-industry-industrial-control-page-en"
  - "frontendapt-industry-robotics-page-en"
  - "nasa-physics-of-failure-pcb-reliability-2021-page"
tags: ["pcba", "electrical-test", "flying-probe", "ict", "fct", "reliability", "robotics", "industrial-control", "methods", "boundary"]
---

# Canonical Summary

> The current evidence base supports a strict boundary for public copy: flying probe, ICT, and FCT can provide manufacturing-defect screening and powered-behavior evidence, but reliability remains a broader evaluation problem that may involve build history, defect trends, structural or process analysis, and program-specific environmental or life-related validation.

## Stable Facts

- The internal testing-quality and quality-system pages place flying probe, ICT, FCT, burn-in, ESS, inspection, and traceability inside a layered quality flow rather than treating one method as full proof of product robustness.
- The flying-probe page supports fixture-free electrical checks such as continuity, opens, shorts, value, and polarity verification.
- The ICT page supports fixture-based node-level electrical verification on assembled boards.
- The FCT page supports powered behavior validation under an application-specific setup rather than structural or life evaluation.
- The industrial-control and robotics pages support application framing for control-heavy hardware where service conditions, power stages, sensors, and motion interfaces may matter, but they do not prove a single electrical-test method is a reliability surrogate.
- The NASA `physics of failure` source supports public vocabulary that frames PCB reliability as risk-based evaluation and mitigation planning rather than one isolated test event.

## Conditions And Methods

- Use this card for `flying-probe-test-industrial-robotics-control-pcb-reliability` and similar slugs where a test-method title risks overpromising reliability proof.
- Keep `flying probe` attached to electrical defect screening and access economics.
- Keep `ICT` attached to fixture-based node access and fault localization.
- Keep `FCT` attached to intended powered behavior under a defined setup.
- If a draft keeps the word `reliability`, narrow it to `reliability workflow`, `reliability evidence stack`, or `program-dependent reliability evaluation` rather than claiming that one electrical test establishes reliability.
- Pair this card with `pcba-flying-probe-vs-ict-selection-posture` and `pcba-quality-gates-and-test-strategy` so the article stays in a layered quality model.

## Limits And Non-Claims

- This card does not authorize field-life claims, MTBF claims, burn-in effectiveness claims, ESS effectiveness claims, or environmental-test pass claims.
- It does not prove that flying probe, ICT, or FCT alone can qualify an industrial-control or robotics PCBA for service conditions.
- It does not establish universal reliability acceptance criteria, screening plans, or release authority.

## Open Questions

- Add a later card if the corpus needs a narrower `burn-in-and-ESS-versus-production-electrical-test` split.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/testing-quality.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/industries/en/industrial-control-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/robotics-pcb.json
- https://ntrs.nasa.gov/citations/20210026410
