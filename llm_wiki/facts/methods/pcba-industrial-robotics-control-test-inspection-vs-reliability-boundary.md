---
fact_id: "methods-pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary"
title: "Industrial robotics and control boards need inspection, electrical test, and reliability language kept in separate evidence lanes"
topic: "Industrial robotics control test inspection versus reliability boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "frontendapt-industry-industrial-control-page-en"
  - "frontendapt-industry-robotics-page-en"
  - "nasa-physics-of-failure-pcb-reliability-2021-page"
tags: ["industrial-control", "robotics", "inspection", "flying-probe", "ict", "fct", "x-ray", "reliability", "methods", "boundary"]
---

# Canonical Summary

> For industrial robotics and control boards, the current evidence supports three separate public lanes: process inspection verifies how the assembly was built, electrical test verifies connectivity or powered behavior, and reliability language belongs to a broader evidence stack that is not proven by one inspection or test method alone.

## Stable Facts

- The PCBA quality-system page supports a staged quality flow that includes inspection, electrical or functional validation, burn-in-related workflow language, final inspection, and traceability.
- The testing-quality page supports layered test and quality reporting rather than one universal proof method.
- The flying-probe page supports fixture-free electrical screening such as continuity, open, short, value, and polarity checks.
- The ICT page supports fixture-based node access and manufacturing-defect localization on assembled boards.
- The FCT page supports powered board-behavior validation in an application-specific setup.
- The X-ray page supports hidden-joint and internal-defect visibility for dense packages.
- The industrial-control and robotics pages support scenario framing for boards that may mix motion control, power interfaces, sensors, communications, and service considerations.
- The NASA reliability source supports public wording that PCB reliability is a broader risk-evaluation problem, not a one-test conclusion.

## Evidence Lanes

### Process Inspection Lane

- Safe scope:
  SPI, AOI, X-ray or AXI, hidden-joint visibility, solder-feature review, and first-build inspection checkpoints.
- Safe claim shape:
  `inspection helps confirm build execution and hidden-joint visibility`.
- Blocked drift:
  inspection as universal proof of service life, field endurance, or program acceptance.

### Electrical Test Lane

- Safe scope:
  flying probe for fixture-free electrical screening, ICT for fixture-based node verification, FCT for powered behavior under a defined setup.
- Safe claim shape:
  `electrical test helps screen manufacturing defects or confirm intended board behavior under the planned test environment`.
- Blocked drift:
  fault-coverage percentages, fixture payback, cycle-time claims, or reliability proof.

### Reliability Proof Lane

- Safe scope:
  reliability workflow, accumulated evidence, program-dependent validation, and risk-reduction planning.
- Safe claim shape:
  `reliability needs a broader evidence stack than one inspection or production-test event`.
- Blocked drift:
  MTBF, uptime, DPPM, field-life, environmental-pass, or outcome-improvement claims.

## Conditions And Methods

- Use this card for `flying-probe-test-industrial-robotics-control-pcb-reliability` and any industrial-control or robotics slug that mixes test-method language with `reliability`.
- If the article keeps `reliability` in the title, rewrite the body around `reliability evidence boundary`, `quality stack`, or `program-dependent validation`.
- Keep flying probe and ICT attached to electrical screening choices, not to reliability proof.
- Keep X-ray attached to hidden-joint visibility, not to electrical or field-performance proof.
- Keep FCT attached to intended powered behavior, not to lifetime or environmental qualification.

## Limits And Non-Claims

- This card does not authorize exact acceptance thresholds, defect classes, or test-coverage claims.
- It does not prove industrial-control or robotics boards receive the same screening stack on every program.
- It does not convert burn-in, ESS, inspection, or electrical test vocabulary into field-reliability evidence.
- It does not establish release authority for safety-critical or regulated systems.

## Open Questions

- Add a narrower industrial-control follow-on later if prompt retrieval starts needing a separate `serviceable-control-board-test-access` topic.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/testing-quality.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- /code/hileap/frontendAPT/public/static/industries/en/industrial-control-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/robotics-pcb.json
- https://ntrs.nasa.gov/citations/20210026410
