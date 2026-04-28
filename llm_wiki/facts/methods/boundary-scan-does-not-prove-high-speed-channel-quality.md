---
fact_id: "methods-boundary-scan-does-not-prove-high-speed-channel-quality"
title: "Boundary-scan confirms test access and some digital interconnect conditions, not high-speed channel quality"
topic: "Boundary-scan versus high-speed channel proof"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "ieee-p1149-1-boundary-scan-par-page"
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendhil-turnkey-assembly-product-page-en"
  - "frontendapt-materials-controlled-impedance-stackups-page-en"
  - "frontendhil-high-speed-product-page-en"
  - "pcisig-pcie-5-faq"
  - "pcisig-pcie-6-faq"
tags: ["boundary-scan", "jtag", "high-speed", "signal-integrity", "dft", "channel-validation", "methods", "boundary"]
---

# Canonical Summary

> The current evidence base supports a strict separation: `boundary-scan / JTAG` belongs to the test-access and digital-interconnect layer, while high-speed channel quality still depends on separate stackup, impedance, transition, measurement, and interface-validation work.

## Stable Facts

- The official IEEE SA `P1149.1` page frames boundary-scan around a test access port, boundary-scan architecture, interconnect-oriented testing, and integrated-circuit test, programming, configuration, or debug support.
- The internal SMT/THT PCBA page places boundary-scan inside a broader manufacturing-test stack that also includes inspection and electrical or functional gates.
- The HIL turnkey assembly page likewise treats boundary-scan as one tool inside a wider assembled-board verification flow rather than as a universal pass/fail proof for the finished product.
- The internal controlled-impedance stackups page treats stackup definition, coupon planning, and `TDR / VNA` work as a separate planning and validation discipline.
- The HIL high-speed page places low-loss stackup selection, differential-routing control, backdrill, and validation language in the high-speed engineering layer rather than in the JTAG layer.
- Public PCI-SIG FAQ pages for `PCIe 5.0` and `PCIe 6.0` support the idea that modern high-speed interfaces are system-level channel problems with their own electrical and interoperability context, not just digital access problems.

## Conditions And Methods

- Use this card when a draft needs safe language such as `boundary-scan can help prove access and some digital interconnect conditions on a dense assembly`.
- Pair it with stackup, impedance, backdrill, and validation cards when the article discusses `high-speed PCB`, `SerDes`, `DDR`, `backplane`, or similar channel-sensitive designs.
- Keep `JTAG pass`, `boundary-scan coverage`, or `device access` separate from claims about channel margin, eye opening, timing robustness, or protocol behavior.
- Refresh the official IEEE and PCI-SIG wording before publication because those public pages are dynamic.

## Limits And Non-Claims

- This card does not authorize claims about insertion loss, return loss, jitter, BER, eye-mask compliance, or timing margin.
- It does not prove that a board passing boundary-scan will also pass high-speed protocol training, compliance, or application traffic.
- It does not establish that every device in a design exposes enough boundary-scan access to make JTAG a sufficient production-test method.

## Open Questions

- Add a future source-backed card if the corpus needs a narrower `boundary-scan-versus-protocol-compliance` treatment.

## Source Links

- https://standards.ieee.org/ieee/1149.1/10977
- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json
- /code/hileap/frontendAPT/public/static/materials/en/controlled-impedance-stackups.json
- /code/hileap/frontendHIL/public/static/products/en/high-speed-pcb.json
- https://pcisig.com/faq?field_category_value%5B%5D=pci_express_5.0
- https://pcisig.com/faq?field_category_value%5B%5D=pci_express_6.0
