---
fact_id: "methods-pcba-test-method-input-package-boundary"
title: "Selecting PCBA test methods requires design-intent inputs beyond Gerbers, and each method depends on different review artifacts"
topic: "PCBA test method input package boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-27"
source_ids:
  - "ieee-p1149-1-boundary-scan-par-page"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-x-ray-inspection-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-ic-programming-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendhil-turnkey-assembly-product-page-en"
tags: ["pcba", "methods", "test-inputs", "gerber", "bom", "schematic", "jtag", "fct", "x-ray"]
---

# Canonical Summary

> The current corpus supports a guarded planning rule: selecting among boundary-scan / JTAG, ICT, flying probe, X-ray / AXI, FCT, and programming requires more than fabrication outputs alone. Different methods depend on different design and manufacturing inputs, so the review package should expose board construction, component identity, physical access, digital test-access intent, powered behavior goals, and programming requirements.

## Stable Facts

- The IEEE `P1149.1` source supports boundary-scan as a test-access and device-programming architecture, which implies that chain support and intended access behavior must be understood before relying on it.
- The ICT and flying-probe sources support electrical-test planning around nets, nodes, continuity, opens, shorts, polarity, and component-value checks, which depend on accessible electrical points and assembly context.
- The X-ray source supports hidden-joint inspection planning for dense packages and concealed solder features, which depends on package mix and hidden-joint risk rather than on electrical access alone.
- The FCT source supports powered functional validation under a custom test environment, which implies the need for defined power-up behavior, interface expectations, and application-specific pass/fail logic.
- The IC-programming source supports device programming and board bring-up flows, which depend on firmware / configuration intent and device handling requirements.
- The internal quality-system and turnkey-assembly sources support a broader DFM/DFT and layered-production-review model rather than a Gerber-only test decision.

## Conditions And Methods

- Treat Gerber, drill, and stackup files as the baseline inputs for fabrication and access-context review, not as the complete package for PCBA test-method selection.
- Add a BOM with manufacturer part numbers when the decision depends on device support, programming needs, hidden-joint package risk, or component-specific handling.
- Add pick-and-place or assembly data when the decision depends on physical access, density, orientation, or package visibility.
- Add schematic or test-access excerpts when considering boundary-scan / JTAG, ICT access planning, reset behavior, power dependencies, or programming path design.
- Add explicit test objectives when choosing between electrical defect screening, hidden-joint inspection, device programming, bring-up, and powered functional validation.
- Add production-stage context when asking whether a fixture-free or fixture-based electrical method is more appropriate.

## Limits And Non-Claims

- This card does not claim Gerber files are useless; it claims they are not sufficient by themselves for the full test-method decision.
- It does not define a universal minimum document list for every supplier or every product class.
- It does not claim that having the right files guarantees a feasible ICT fixture, boundary-scan chain, or functional-test setup.
- It does not authorize exact requirements for test pads, chain topology, fixture design, software harnesses, or acceptance thresholds.

## Open Questions

- Add a future card if prompt work starts needing a separate `minimum-input-package-for-high-speed-si-validation-versus-pcba-test-selection` split.

## Source Links

- https://standards.ieee.org/ieee/1149.1/10977
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/x-ray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/ic-programming.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json
