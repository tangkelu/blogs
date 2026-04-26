---
fact_id: "methods-pcba-ict-vs-fct-boundary"
title: "Internal PCBA test pages separate fixture-based ICT from powered functional test"
topic: "ICT vs FCT boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendhil-turnkey-assembly-product-page-en"
tags: ["internal", "pcba", "ict", "fct", "boundary-scan", "functional-test", "methods"]
---

# Canonical Summary

> The internal PCBA test pages separate ICT from FCT: ICT is presented as fixture-based electrical verification at nodes and components, while FCT is presented as powered functional validation of whether the assembled board behaves correctly in its intended operating context.

## Stable Facts

- The APT ICT page describes ICT as using a bed-of-nails fixture to apply test signals to specific nodes on an assembled board.
- The same ICT page positions ICT around electrical performance, interconnections, component integration, shorts, opens, and manufacturing defects.
- The APT FCT page defines functional test as a powered test of whether the assembled board performs intended functions correctly under real operating conditions.
- The FCT page also frames custom fixtures, firmware loading, and a complete test environment as part of functional-test setup.
- The APT PCBA quality-system page includes both ICT and FCT in electrical and functional validation, without collapsing them into one step.
- The HIL turnkey page similarly lists ICT/FCT/boundary-scan coverage as part of the broader turnkey test strategy.

## Conditions And Methods

- Use ICT for manufacturing-defect and electrical-connectivity framing.
- Use FCT for powered behavior and end-use simulation framing.
- Keep boundary scan adjacent to ICT/FCT planning, especially for dense digital assemblies.

## Limits And Non-Claims

- This card does not claim ICT or FCT alone is sufficient for full PCBA validation.
- It does not claim every design has physical access for ICT.
- It does not state a required coverage percentage for any program.

## Open Questions

- Add a future card for `flying-probe-vs-ict-for-low-volume-pcba`.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json

