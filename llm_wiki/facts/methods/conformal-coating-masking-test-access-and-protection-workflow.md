---
fact_id: "methods-conformal-coating-masking-test-access-and-protection-workflow"
title: "Conformal coating should be framed as a masking, keep-out, inspection, and test-access workflow"
topic: "Conformal coating masking and test-access workflow"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcba-pcb-conformal-coating-page-en"
  - "frontendapt-pcb-pcb-conformal-coating-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-final-quality-inspection-page-en"
tags: ["conformal-coating", "masking", "test-access", "inspection", "ict", "flying-probe", "workflow"]
---

# Canonical Summary

> The safe rewrite posture for conformal coating is to treat it as a workflow problem: decide what must be protected, what must stay accessible for connectors or test, how coating is applied, and what inspection or validation happens before release.

## Stable Facts

- The internal conformal-coating pages describe coating as a post-assembly protection step and explicitly mention manual, automated, and selective application methods.
- The same pages describe pre-cleaning, component spacing, over-coating risk, and robotic-access limitations as preparation concerns for successful coating.
- The internal PCBA quality-system page places cleaning, inspection, electrical test, and final inspection inside a broader release workflow rather than as isolated steps.
- The ICT page frames electrical verification as fixture-based access to nodes and interconnections on assembled boards.
- The flying-probe page frames fixture-free electrical verification as useful when custom fixtures are not yet available or designs are still changing.
- The final-inspection page provides an internal release-gate anchor after production and verification steps are complete.

## Conditions And Methods

- Use this card when a rewrite needs to explain why connectors, programming headers, contact pads, switch interfaces, optical interfaces, or other non-coatable areas must be identified before coating.
- Frame masking or selective coating as one way to preserve access and function, not as a universal requirement or dimensioned design rule.
- Connect coating planning to DFT and release workflow: test access that must remain available should be agreed before coating is locked, especially on boards that may use ICT, flying probe, or final powered validation.
- Safe wording for mixed programs: assemblies may be electrically tested before final protection, and any areas needing later mating, probing, or adjustment should be considered in the coating plan.
- Use this card to support conservative statements about protection workflow for optical modules, medical electronics, dense communications boards, or vehicle electronics where service access and protected areas can compete.

## Limits And Non-Claims

- This card does not provide masking keep-out dimensions, connector exclusion distances, test-pad coating rules, or universal order-of-operations requirements.
- It does not prove that all coated boards must be tested before coating, or that every coated board remains probe-accessible after coating.
- It does not set cleanliness acceptance thresholds, UV-inspection criteria, or defect pass/fail criteria.
- It does not authorize claims that selective coating eliminates all masking in every design.

## Open Questions

- Add source support for rework and depanelization interactions if future rewrites need service or repair workflow language.
- Add a dedicated connector and optical-interface protection card if the data-center optical-module rewrite needs narrower interface exclusions.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/pcb-conformal-coating.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-conformal-coating.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/final-quality-inspection.json
