---
fact_id: "methods-pcba-boundary-scan-jtag-bsdl-device-prerequisites"
title: "Usable boundary-scan access depends on per-device support and current BSDL or equivalent device-description data"
topic: "PCBA boundary-scan JTAG BSDL and device prerequisites"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "ieee-p1149-1-boundary-scan-par-page"
  - "xjtag-bsdl-file"
tags: ["boundary-scan", "jtag", "bsdl", "1149.1", "device-support", "programming", "debug", "methods"]
---

# Canonical Summary

> The current source layer supports a practical gating rule for public copy: a board is only meaningfully `JTAG-capable` for boundary-scan work when the target devices actually implement usable boundary-scan features and the team has the vendor description data needed to address those devices correctly.

## Stable Facts

- The official IEEE SA `P1149.1` page ties boundary-scan to test access plus integrated-circuit test, programming, configuration, and debug support rather than to one narrow production-test use case.
- The XJTAG BSDL page states that a BSDL file describes how boundary-scan architecture is implemented in a component and that test systems use BSDL information to determine how to access a device in the JTAG chain.
- The same BSDL page lists practical contents including TAP pin identification, device-package pin mapping, instruction-register description, register-access description, and boundary-register description.
- The XJTAG BSDL page also states that, where a device only complies in a specific test mode, the BSDL file can provide the required compliance-pin pattern for entering boundary-scan mode.

## Conditions And Methods

- Use this card when a draft needs guarded language such as `confirm which ICs in the BOM actually support boundary-scan and gather the matching BSDL or equivalent vendor description files before assuming the chain is usable`.
- Use it to support design-review items around device support, package-specific descriptions, TAP-definition needs, and compliance or mode-entry conditions.
- Pair it with the chain-review card when a draft discusses connector access, chain order, or programming/debug separation.
- Keep `programming`, `configuration`, and `debug` language tied to per-device capability and setup prerequisites, not to a blanket statement that any JTAG header can perform all three.

## Limits And Non-Claims

- This card does not claim every processor, FPGA, CPLD, memory, or peripheral on a board has usable boundary-scan support.
- It does not claim a BSDL file alone guarantees a working production test program.
- It does not authorize claims about testing analog, RF, power-conversion, or non-scan devices through JTAG alone.
- It does not support exact claims about coverage, cycle time, fixture elimination, or supplier qualification.

## Open Questions

- If future public copy needs stronger wording around non-BSDL description formats or vendor-specific debug/programming file dependencies, add a separate evidence card for those ecosystems instead of stretching this one.

## Source Links

- https://standards.ieee.org/ieee/1149.1/10977
- https://www.xjtag.com/about-jtag/bsdl-files/
