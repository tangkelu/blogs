---
fact_id: "methods-high-speed-si-review-dimensions-remain-separate-from-boundary-scan"
title: "High-speed SI review keeps stackup, impedance, return path, via transitions, measurement, and functional validation separate from boundary-scan"
topic: "High-speed SI review dimensions separate from boundary-scan"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-materials-controlled-impedance-stackups-page-en"
  - "frontendapt-pcb-pcb-impedance-control-page-en"
  - "frontendapt-backplane-pcb-page-en"
  - "frontendhil-high-speed-product-page-en"
  - "frontendhil-backplane-product-page-en"
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendhil-turnkey-assembly-product-page-en"
tags: ["high-speed", "signal-integrity", "stackup", "return-path", "backdrill", "tdr", "vna", "functional-test", "boundary-scan", "methods"]
---

# Canonical Summary

> The internal evidence layer already supports a useful review boundary for future public copy: even when a design includes `boundary-scan / JTAG`, the high-speed signoff conversation still has to stay segmented across stackup, controlled impedance, return-path continuity, via-transition cleanup such as backdrill, channel measurement, eye or timing margin investigation, and product-level functional validation.

## Stable Facts

- The controlled-impedance stackups page frames high-speed work around planned stackup architecture, impedance structures, and coupon-oriented validation.
- The APT impedance-control page ties controlled impedance to simulation and `TDR` verification rather than to generic assembled-board access methods.
- The APT backplane page groups high-speed boards around low-loss stackup, long-channel structures, backdrill, and signal-validation posture.
- The HIL high-speed page similarly connects differential-routing discipline, low-loss material choices, backdrill, and validation to the high-speed build flow.
- The HIL backplane page presents channel validation through `TDR / VNA` and related high-speed controls as a separate engineering layer for backplane-class structures.
- The SMT/THT assembly page and the turnkey assembly page place boundary-scan alongside inspection, electrical test, programming, and functional-test workflow, which reinforces that board-access methods and product-behavior validation are not the same gate.

## Conditions And Methods

- Use this card when drafting blog language that needs to say `JTAG does not collapse the rest of SI review`.
- Safe qualitative review dimensions supported by this card include `stackup`, `impedance`, `reference and return-path continuity`, `via transition quality`, `channel measurement`, `eye or timing margin investigation`, and `functional or protocol-level validation`.
- Pair this card with narrower internal cards on `backdrill`, `controlled impedance`, or `advanced validation` when the article needs more context around one sub-discipline.
- Keep the wording qualitative unless a stronger current source explicitly supports exact public facts.

## Limits And Non-Claims

- This card does not authorize numeric impedance tables, loss budgets, skew limits, or eye-mask thresholds.
- It does not prove every build receives `VNA`, eye-diagram, or protocol-compliance lab work by default.
- It does not turn internal service-page language into a published guarantee of interface pass/fail for any specific customer design.

## Open Questions

- Add a later card for `protocol-compliance-versus-functional-validation` if future drafts start mixing those two layers.

## Source Links

- /code/hileap/frontendAPT/public/static/materials/en/controlled-impedance-stackups.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-impedance-control.json
- /code/hileap/frontendAPT/public/static/pcb/en/backplane-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-speed-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/backplane-pcb.json
- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json
