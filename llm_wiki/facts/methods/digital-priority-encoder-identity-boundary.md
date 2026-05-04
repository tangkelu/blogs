---
fact_id: "methods-digital-priority-encoder-identity-boundary"
title: "Digital encoder writing is source-backed only for narrow priority-encoder identity, not for mixed mechanical encoder or broad pedagogy claims"
topic: "Digital priority encoder identity boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-30"
source_ids:
  - "ti-sn74ls148-product-page"
  - "ti-sn74ls148-datasheet"
  - "onsemi-mc14532b-datasheet"
tags: ["priority-encoder", "digital-logic", "sn74ls148", "mc14532b", "active-low", "cascade-boundary"]
---

# Canonical Summary

> Official logic-vendor sources support a conservative digital-priority-encoder boundary only at device-identity level: a priority encoder is a logic-device family that encodes the highest-priority active input into a smaller binary-address output, with vendor-documented example parts and narrow enable / cascade behavior. These sources do not authorize mixed mechanical-encoder content, broad textbook pedagogy, or generic application advice.

## Stable Facts

- TI's official `SN74LS148` product and datasheet pages identify the device as an `8-line to 3-line priority encoder`.
- TI's official documentation supports the boundary that only the highest-priority active input is encoded for this device family.
- TI's datasheet documents active-low input / output treatment and `EI` / `EO` cascade-related signals for the `SN74LS148` family.
- onsemi's official `MC14532B` datasheet identifies that device as an `8-Bit Priority Encoder`.
- onsemi's datasheet supports cross-vendor confirmation that a priority encoder is a standard logic-device category with enable and grouped-output behavior at device level.

## Conditions And Methods

- Use this card for `/code/blogs/tmps/2025.11.10/en/encoder‑circuit.md` only after splitting the draft into a digital priority-encoder lane separate from mechanical encoder claims.
- Safe posture: describe `digital priority encoder` as a logic-device category and use vendor-documented example parts such as `SN74LS148` or `MC14532B` only at identity level.
- Safe behavior posture: mention highest-priority-active-input behavior and vendor-documented enable / cascade-related signaling where the wording stays tied to the sourced example devices.
- Keep device identity separate from generic truth-table teaching, broad Boolean pedagogy, PCB layout guidance, and application claims.

## Limits And Non-Claims

- This card does not authorize the mixed mechanical encoder lane: absolute / incremental, rotary / linear, SSI / EnDat, environmental, or positioning claims.
- It does not authorize textbook-style `2^n to n` teaching as a universal sourced rule beyond the narrow example-device framing.
- It does not authorize broad truth-table, Boolean-expression, troubleshooting, fan-in, DFM, or PCB-layout advice.
- It does not authorize memory-decoding, interrupt-prioritization, I/O-expansion, multiplexing, or signal-compression application claims without narrower sources.
- It does not authorize procurement, lifecycle, power, delay, compatibility, or performance claims beyond what a specific vendor page states for a specific part.

## Open Questions

- Add a separate source lane if future drafts need `simple binary encoder` identity beyond `priority encoder`.
- Add separate application-note or institutional sources only if future drafts need bounded logic-pedagogy or application-family language.
- Add a separate mechanical-encoder lane if future drafts need motion-sensing or industrial-positioning content.

## Source Links

- https://www.ti.com/product/SN74LS148
- https://www.ti.com/lit/gpn/sn74ls148
- https://www.onsemi.com/pdf/datasheet/mc14532b-d.pdf
