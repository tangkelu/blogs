---
fact_id: "methods-pcba-boundary-scan-jtag-chain-review-items"
title: "Conservative JTAG design review should name the chain signals, chain topology, and reset-access assumptions"
topic: "PCBA boundary-scan JTAG chain review items"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "ieee-p1149-1-boundary-scan-par-page"
  - "xjtag-jtag-chains"
tags: ["boundary-scan", "jtag", "1149.1", "tdi", "tdo", "tck", "tms", "trst", "chain", "dft", "methods"]
---

# Canonical Summary

> The current public source layer supports a concrete but conservative JTAG review posture: name the actual chain signals and topology in design review, confirm how devices are ordered from TDI to TDO, and state whether optional reset handling is present, rather than treating `JTAG available` as a complete design-for-test answer.

## Stable Facts

- The official IEEE SA `P1149.1` page frames boundary-scan around a test access port and boundary-scan architecture used for interconnect test plus integrated-circuit test, programming, configuration, and debug support.
- The XJTAG chain guide describes a JTAG chain as a 4- or 5-signal structure with serial data entering at `TDI`, moving device-to-device through `TDO` to the next device's `TDI`, and returning to the controller through the final `TDO`.
- The same XJTAG guide describes `TCK`, `TMS`, and optional `nTRST` as shared chain-control signals connected in parallel across the devices in that chain.
- The XJTAG guide also states that a PCB may have multiple separate JTAG chains rather than one universal chain for the whole board.

## Conditions And Methods

- Use this card when a draft needs specific design-review language such as `confirm TDI/TDO device order, shared TCK/TMS routing, and whether optional TRST/nTRST is present or intentionally omitted`.
- Use it to support copy that separates `interconnect/programming/debug access planning` from high-speed electrical validation.
- Use it to justify phrases such as `single chain`, `multiple chains`, `shared control signals`, or `board-level JTAG access architecture`.
- Keep any mention of reset conservative: the public source layer supports `optional TRST/nTRST handling should be reviewed`, not universal statements about every device or chain using the same reset scheme.

## Limits And Non-Claims

- This card does not authorize claims about exact fault coverage, chain throughput, or debug speed.
- It does not prove a given header, connector, or chain is physically accessible after enclosure, shielding, or coating decisions.
- It does not prove that all devices on the BOM participate in the chain.
- It does not turn JTAG chain presence into proof of signal integrity, protocol compliance, or product-level functional readiness.

## Open Questions

- Public evidence is still thin for board-level power-domain sequencing rules across mixed-device JTAG chains; keep power-state wording cautious unless stronger vendor-specific sources are added for the target BOM.

## Source Links

- https://standards.ieee.org/ieee/1149.1/10977
- https://docs.xjtag.com/xjtag/current/concepts/chain.html
