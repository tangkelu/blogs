---
fact_id: "methods-parameter-scope-test-inspection-electrical-access-method-dimensions"
title: "Electrical-access test sources support concrete access and topology dimensions, not universal fault-coverage or performance proof"
topic: "Test and inspection electrical-access method dimensions"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "keysight-ict-systems"
  - "xjtag-jtag-chains"
  - "xjtag-bsdl-file"
  - "ipc-9252b-toc"
tags: ["ict", "flying-probe", "boundary-scan", "jtag", "bsdl", "fixture", "electrical-test"]
---

# Canonical Summary

> The current source layer supports detailed vocabulary for `ICT`, `flying probe`, and `boundary-scan / JTAG`: ICT is fixture-based node-level electrical verification, flying probe is fixture-free probe-driven electrical verification, and JTAG depends on concrete chain topology and device-description data such as BSDL. These sources do not authorize universal test coverage percentages, fixture-elimination claims, or proof that a passing electrical-access test validates high-speed channel behavior.

## Stable Facts

- The internal APT ICT page frames ICT as fixture-based electrical verification and explicitly includes bed-of-nails and boundary-scan support.
- The internal APT flying-probe page frames flying probe as fixture-free electrical verification for bare PCBs and assembled PCBAs.
- The internal APT AOI page helps distinguish optical inspection from node-level electrical verification by describing ICT as the node-level electrical layer after visual / geometric gates.
- Keysight positions ICT as a production-line method for manufacturing-defect detection, but its performance language remains vendor framing.
- XJTAG's chain documentation supports concrete JTAG chain-topology review items.
- XJTAG's BSDL documentation supports the idea that usable boundary-scan access depends on per-device description data, not just a header or connector.
- IPC-9252B TOC metadata supports a separate bare-board electrical-test identity anchor when a draft needs to distinguish unpopulated-board electrical test from PCBA electrical-access test.

## Named Parameters And Method Dimensions

- `ICT`:
  `bed-of-nails`, `fixture-based`, `node-level electrical verification`, `continuity`, `shorts`, `component values`, and `some functional parameters` are named across the internal APT ICT and AOI pages.
- `Flying probe`:
  `fixture-free`, `bare PCB`, `assembled PCBA`, `continuity`, `opens`, `shorts`, `value`, and `polarity` are named by the internal APT flying-probe page.
- `JTAG chain topology`:
  `TDI`, `TDO`, shared `TCK`, shared `TMS`, optional `nTRST`, and the possibility of `multiple separate chains` on one board are named by the XJTAG chain source.
- `BSDL prerequisites`:
  `TAP pin identification`, `instruction-register description`, `register access`, `boundary-register description`, `package mapping`, and `compliance-pin` information are named by the XJTAG BSDL source.
- `Bare-board electrical-test anchor`:
  `IPC-9252B` can be cited as a public identity anchor for unpopulated-board electrical-test scope only.

## Scope And Non-Generalization

- Use these dimensions to explain access mode, tooling posture, and the difference between board-level electrical access and performance validation.
- Treat `ICT` and `flying probe` checks as test-method vocabulary, not as proof of a specific fault-coverage percentage.
- Treat `JTAG` chain fields and `BSDL` contents as prerequisites or review items, not as proof that a specific board is production-test ready.
- Do not claim fixture elimination, full-board validation, cycle-time superiority, or universal defect coverage from these sources alone.
- Do not let `boundary-scan` absorb high-speed SI, BER, protocol-compliance, or interoperability claims.
- Do not extract IPC-9252 requirements, parameters, or thresholds from the public TOC record.

## Blog Usage

- `boundary-scan / JTAG`:
  Safe support for wording such as `review chain order, shared TCK/TMS control, optional nTRST handling, and BSDL availability before treating JTAG as a usable production-test path`. Not safe support for coverage or high-speed proof claims.
- `flying-probe / ICT`:
  Safe support for positioning `flying probe` as fixture-free and `ICT` as bed-of-nails / fixture-based with node-level checks. Not safe support for cost, speed, or yield superiority claims.
- `type-c charger`:
  Safe support for describing electrical-access-test planning around continuity, shorts, component values, and polarity, especially where connector or power-stage builds still need separate powered functional bring-up. Not safe support for USB compliance or charger-output claims.
- `high-speed SI`:
  Safe support only for saying these access tests are separate from channel validation. Use a high-speed measurement card for TDR / VNA specifics.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- https://www.keysight.com/us/en/products/in-circuit-test-for-manufacturing/in-circuit-test-systems.html
- https://docs.xjtag.com/xjtag/current/concepts/chain.html
- https://www.xjtag.com/about-jtag/bsdl-files/
- https://www.ipc.org/TOC/IPC-9252B.pdf
