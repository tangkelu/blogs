---
fact_id: "methods-pcba-test-method-selection-framework"
title: "PCBA test-method selection should be framed as a layered decision across access, defect visibility, powered behavior, and programming intent"
topic: "PCBA test method selection framework"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "ieee-p1149-1-boundary-scan-par-page"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-x-ray-inspection-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-ic-programming-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
tags: ["pcba", "methods", "test-strategy", "boundary-scan", "ict", "flying-probe", "x-ray", "fct", "programming"]
---

# Canonical Summary

> The current source layer supports a conservative PCBA selection framework: boundary-scan / JTAG belongs to the digital test-access layer, ICT and flying probe belong to electrical manufacturing-defect screening with different access and tooling assumptions, X-ray belongs to hidden-joint visibility, FCT belongs to powered product-behavior validation, and programming / bring-up belongs to device configuration and board enablement. These methods are complementary and should not be asked to prove the same thing.

## Stable Facts

- IEEE `P1149.1` defines boundary-scan around test access, interconnect test, and integrated-circuit test/programming/configuration/debug support.
- The internal ICT page frames ICT as fixture-based node-level electrical verification on assembled PCBAs.
- The internal flying-probe page frames flying probe as a fixture-free electrical method for continuity, opens, shorts, value, and polarity checks on bare boards and assembled PCBAs.
- The internal X-ray page frames X-ray and CT around hidden solder-joint and internal defect visibility, especially for dense packages such as BGA, QFN, and CSP.
- The internal FCT page frames functional test as powered validation of intended board behavior under an application-specific test environment.
- The internal IC-programming page frames programming and configuration as a separate production and bring-up activity tied to device loading and board enablement.
- The internal quality-system and testing-quality pages place these methods inside a layered quality flow rather than as interchangeable single-step substitutes.

## Conditions And Methods

- Use boundary-scan / JTAG when compatible digital devices and chain planning can provide controlled test access, interconnect-oriented checks, programming support, or bring-up visibility where physical probing is constrained.
- Use ICT when the design exposes enough planned node access to justify fixture-based electrical verification in the assembly flow.
- Use flying probe when fixture-free electrical verification is needed, especially while layouts are still changing or dedicated ICT tooling is not the right choice yet.
- Use X-ray or AXI when hidden solder joints or internal solder-related defects must be inspected beyond what visual or optical access can show.
- Use FCT when the goal is to verify powered behavior, interface operation, or application-specific functions after assembly.
- Use programming / bring-up as its own planning layer for firmware loading, configuration, and controlled board enablement, even when those steps are adjacent to JTAG or FCT.
- Pair these methods instead of collapsing them: access methods, electrical defect-screen methods, hidden-joint inspection, programming, and functional validation address different decision questions.

## Limits And Non-Claims

- This card does not authorize claims about exact fault coverage, throughput, cycle time, fixture payback, or cost ranking among methods.
- It does not claim every board needs all listed methods.
- It does not claim boundary-scan, ICT, flying probe, X-ray, FCT, or programming alone is sufficient for full PCBA release.
- It does not treat programming success as proof of solder-joint quality, powered functional behavior, or high-speed channel margin.
- It does not treat X-ray visibility as proof of digital logic behavior, firmware state, or system-level function.

## Open Questions

- Add a future card if prompt work starts needing a separate `burn-in-and-ess-versus-production-test-selection` boundary.

## Source Links

- https://standards.ieee.org/ieee/1149.1/10977
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/x-ray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/ic-programming.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/testing-quality.json
