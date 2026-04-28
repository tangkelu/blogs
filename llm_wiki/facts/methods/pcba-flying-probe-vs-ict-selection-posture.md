---
fact_id: "methods-pcba-flying-probe-vs-ict-selection-posture"
title: "Internal PCBA pages separate fixture-free flying probe from fixture-based ICT as a program-selection choice"
topic: "PCBA flying probe versus ICT selection posture"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-industry-industrial-control-page-en"
  - "frontendapt-industry-robotics-page-en"
tags: ["internal", "pcba", "flying-probe", "ict", "selection", "industrial-control", "robotics", "methods"]
---

# Canonical Summary

> The internal test corpus already supports a conservative selection rule: flying probe is the fixture-free electrical option for boards that are still changing or do not justify dedicated tooling, while ICT is the fixture-based option when node access and program economics support repeatable production testing.

## Stable Facts

- The flying-probe page describes fixture-free electrical verification for bare PCBs and assembled PCBAs.
- The same flying-probe page frames continuity, open, short, value, and polarity checks as core use cases.
- The ICT page describes a bed-of-nails fixture and node-level electrical verification on assembled PCBAs.
- The quality-system and testing-quality pages place electrical test choices inside a broader layered quality flow rather than treating one method as universally sufficient.
- The industrial-control page provides application context for PLCs, servo drives, motor control, IO modules, and other automation hardware.
- The robotics page provides application context for controllers, motion control, AGV/AMR, and embedded power-stage hardware where debug access and product-change cadence may vary by program.

## Conditions And Methods

- Use this card when a rewrite needs guarded language such as `flying probe is often used where dedicated ICT tooling is not yet justified`.
- Use the industrial-control and robotics pages only for application framing, not as proof that one electrical-test method is always preferred in those sectors.
- Pair this card with traceability or layered-inspection cards when a draft starts making broader reliability statements.
- Keep any claims about volume thresholds, throughput, fault coverage, or fixture payback out of public copy unless stronger current evidence is added.

## Limits And Non-Claims

- This card does not claim flying probe is always better for reliability-critical boards.
- It does not claim ICT is mandatory for robotics or industrial-control programs.
- It does not authorize exact cycle-time, coverage, or cost-comparison claims.

## Open Questions

- Add a future card if the rewrite program needs a separate `electrical-test-selection-for-service-and-repairable-control-boards` topic.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/testing-quality.json
- /code/hileap/frontendAPT/public/static/industries/en/industrial-control-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/robotics-pcb.json
