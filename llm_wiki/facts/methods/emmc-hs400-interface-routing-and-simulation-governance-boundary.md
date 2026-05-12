---
fact_id: "methods-emmc-hs400-interface-routing-and-simulation-governance-boundary"
title: "TI AM62Px guidance supports a narrow eMMC HS400 interface routing and simulation-governance boundary"
topic: "eMMC HS400 interface routing governance, return-path continuity, stubs, and simulation validation"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-12"
source_ids:
  - "ti-am62px-emmc-hs400-board-design-and-simulation-guidelines"
  - "raspberry-pi-compute-module-5-product-page"
  - "ti-high-speed-layout-guidelines"
tags: ["emmc", "hs400", "routing", "reference-plane", "return-path", "simulation", "ibis", "methods"]
---

# Canonical Summary

> Current public owner guidance is strong enough to support one narrow eMMC/HS400 governance boundary: TI AM62Px eMMC HS400 board designs should treat the interface as point-to-point high-speed routing that preserves ground/reference-plane and return-path continuity, avoids plane-split crossings, minimizes layer transitions, uses nearby ground vias when return currents must transition between reference planes, avoids stubs or branched test/probe access, and relies on close TI EVM implementation or extraction/simulation before claiming full interface performance. This does not authorize handbook-derived pull-up tables, matching values, routing numerics, timing closure, or customer-board HS400 performance claims.

## Stable Facts

- TI's AM62Px application report is an official owner source for eMMC HS400 board-design and simulation guidance.
- TI frames full eMMC interface-frequency and data-rate support as dependent on excellent PCB implementation, close EVM/layout reuse, and simulation when the customer design diverges from TI's EVM.
- TI treats the eMMC signals as point-to-point and recommends minimizing layer transitions.
- TI ties reference-plane changes to nearby ground vias so return current can transition with a low-inductance path.
- TI warns against crossing plane splits in signal reference planes and against return-path discontinuities.
- TI disallows stubs on the eMMC nets and requires test/probe access to avoid branches or stubs.
- TI's simulation section treats board extraction, board-model validation, power / signal model extraction, IBIS simulation, and pass/fail checks as part of eMMC HS400 design validation.
- The Raspberry Pi CM5 product page is useful only for platform identity and eMMC-option vocabulary; it is not an eMMC routing-rule or HS400 validation authority.

## Conditions And Methods

- Use this card when a prompt needs guarded eMMC/HS400 interface routing language without numeric routing tables.
- Keep the language at governance level: point-to-point interface, reference-plane continuity, local return-current transition path, no stubs, crosstalk-sensitive clock/strobe posture, and simulation / EVM-based validation.
- Pair this card with DDR/memory-interface or generic return-path cards only when a prompt compares high-speed interface governance patterns, not when it needs exact values.
- Use a named device owner's data sheet, design guide, EVM files, and simulation package before making board-specific speed, timing, or validation claims.

## Limits And Non-Claims

- This card does not authorize eMMC pull-up / pull-down tables, matching resistor values, trace width, spacing, impedance, layer count, via count, via distance, compensation factor, frequency, slew-rate, setup/hold, skew, or timing-budget numbers.
- It does not authorize universal eMMC, HS200, HS400, DDR, LPDDR, or memory-bus routing recipes.
- It does not prove timing closure, SI margin, eye opening, compliance, validation pass, data rate, bandwidth, or customer-board performance.
- It does not prove that HIL, APT, or any supplier can build or validate eMMC HS400 boards by default.
- It does not promote any numeric table or figure from `【PCB必备】194页-PCB设计规范经验之书.pdf`.

## Open Questions

- A later lane may add owner-specific eMMC power-integrity or PDN simulation wording if it stays tied to the named owner guide and does not generalize exact TI example values.
- Package-family-specific marking authority from Analog Devices LFCSP package outlines remains a candidate, but it was not promoted in this pass because main-controller retrieval of the source PDF did not complete.

## Source Links

- https://www.ti.com/lit/an/spradp5/spradp5.pdf
- https://www.raspberrypi.com/products/compute-module-5/
