---
fact_id: "pcba-ict-boundary-and-flying-probe-method-identity"
title: "ICT is a fixture-based manufacturing test method; flying probe is a fixture-free manufacturing test method"
topic: "PCBA ICT and flying probe method identity"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-04"
source_ids:
  - "keysight-in-circuit-test-systems-page"
  - "seica-flying-probe-page"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
tags: ["pcba", "ict", "flying-probe", "manufacturing-test", "fixture-free", "test-access"]
---

# Canonical Summary

> ICT and flying probe solve different manufacturing-test problems. ICT is the fixture-based lane for in-circuit verification on assembled boards, while flying probe is the fixture-free lane for electrical verification when dedicated tooling is not the right fit.

## Stable Facts

- The official Keysight ICT page provides a public manufacturing-test anchor for ICT as an in-circuit-test system family.
- The official SEICA flying-probe page provides a public manufacturing-test anchor for flying probe as a fixture-free test-system family.
- The internal PCBA ICT and flying-probe pages frame ICT as bed-of-nails / node-access testing and flying probe as fixture-free electrical verification.
- The two methods belong in the same broader quality flow, but they do not use the same access model.

## Conditions And Methods

- Use this card when a rewrite needs a compact, public-safe identity statement for ICT versus flying probe.
- Pair this card with DFM/DFT review-gate language when the draft needs to explain why test access is prepared before fixture release.

## Limits And Non-Claims

- This card does not authorize throughput, cost, coverage, or payback claims.
- It does not claim one method is universally superior.

## Source Links

- https://www.keysight.com/us/en/products/in-circuit-test-for-manufacturing/in-circuit-test-systems.html
- https://www.seica.com/en/products/flying-probe-test-systems
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
