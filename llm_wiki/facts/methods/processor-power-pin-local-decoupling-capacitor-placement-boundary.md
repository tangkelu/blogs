---
fact_id: "methods-processor-power-pin-local-decoupling-capacitor-placement-boundary"
title: "Processor power-pin local decoupling placement may be reused only as a near-device transient-current and mounting-inductance boundary"
topic: "Processor power-pin local decoupling capacitor placement boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-11"
exact_data_class: "boundary_convention"
scope_type: "owner_scoped_processor_fpga_power_pin_local_decoupling_placement_boundary"
canonical_unit_policy: "Preserve wording such as decoupling or bypass capacitor near the device or power-pin region being decoupled, close package-side placement, reduced current-path distance, reduced mounting inductance, power and ground planes kept close to the package, and board-side underside or periphery placement only in owner-scoped package-shadow context. Do not normalize this into exact capacitor values, counts, backside-only rules, one-via-per-pin doctrine, or rail-specific sufficiency claims."
source_ids:
  - "analog-devices-decoupling-capacitors-on-power-pins"
  - "amd-ug583-decoupling-capacitor-placement-background"
  - "intel-fpga-general-rules-for-capacitor-and-power-plane-placement"
  - "intel-agilex-7-board-decoupling-capacitors-guide"
tags: ["processor", "fpga", "power-pins", "decoupling", "bypass", "placement", "mounting-inductance", "pdn", "methods"]
---

# Canonical Summary

> Current public semiconductor-owner guidance is strong enough to support one narrow local-decoupling placement boundary: processor or FPGA decoupling capacitors belong close to the device, power-pin region, or package-side power structure they support; current-path distance and mounting inductance should be kept low; and board-side capacitor placement may use close package-shadow families such as underside, via-field, or periphery context when that keeps the decoupling local to the package region. This supports guarded layout-review wording only. It does not authorize exact capacitor counts, exact capacitor values, exact via recipes, universal backside rules, or rail-specific sufficiency claims.

## Stable Facts

- Analog Devices distinguishes `decoupling / bypass capacitors` and `bulk capacitors` in IC power-distribution context and ties adequate type, value, and placement to supplying switching current during runtime.
- AMD supports keeping the decoupling capacitor close to the device being decoupled and treats extra spacing as extra current-path distance and mounting inductance.
- Intel supports placing a decoupling capacitor in close proximity to the power plane, power-pin field, or package-side structure it supports rather than treating it as generic board-wide capacitance.
- Intel supports keeping package-side power and ground structures close enough that BGA-via and local-loop inductance stay controlled.
- Intel also shows that owner-scoped board decoupling may use close package-shadow placement families such as underside, via-field, or periphery context when the capacitor remains local to the package region.

## Exact Data Scope

- exact for:
  - local decoupling as a near-device transient-current support family
  - placement close to the device, package region, power-pin field, or power structure being decoupled
  - minimizing current-path distance and mounting inductance as the reason for local placement
  - treating underside, via-field, or periphery placement as owner-scoped close package-shadow options rather than as generic board placement
- not exact for:
  - exact capacitor values, counts, dielectric mixes, or capacitor ladders
  - exact top-side versus bottom-side hierarchy rules
  - exact via counts, exact via geometry, or one-via-per-pin doctrine
  - exact voltage-drop, EMI, transient, or PDN sufficiency outcomes
  - RK3588-specific rail recipes or any generic `one capacitor per pin cluster` rule

## Conditions And Methods

- Use this card when a prompt needs safe wording for `power-pin decoupling`, `local bypass placement`, `package-shadow capacitor placement`, or `near-device transient-current support`.
- Keep the language at boundary level:
  - close to the device or power-pin region being decoupled
  - keep the local current path short
  - reduce mounting inductance
  - keep the capacitor local to the package-shadow or package-side power structure
  - underside, via-field, or periphery placement only as owner-scoped examples of close package-side placement
- Pair this card with `methods-capacitor-parasitic-self-resonance-and-antiresonance-boundary` only when the draft also needs role or frequency-behavior vocabulary.
- Pair this card with `methods-current-carrying-trace-width-and-copper-boundary` only when the draft separately needs conductor-sizing or thermal-stress consequences.
- Pair this card with `methods-switch-mode-power-emc-placement-and-hot-loop-boundary` only when the draft separately needs switcher-side input-loop or hot-loop language.

## Safe Blog Usage

- Explain that local decoupling placement is a near-device current-path and inductance problem before it is a capacitor-count problem.
- Explain that the capacitor should stay close to the power-pin region or package-side structure it supports rather than being treated as generic board-level bulk capacitance.
- Explain that close package-shadow placement can include underside, via-field, or periphery context when the owner guide keeps those capacitors local to the package region.
- Explain that this lane is about guarded placement posture, not proof of PDN sufficiency or board readiness.

## Limits And Non-Claims

- This card does not authorize exact capacitor values, counts, or size ladders.
- It does not authorize universal backside-only placement rules.
- It does not authorize one-via-per-pin doctrine, via-count equality rules, or exact via geometry.
- It does not authorize RK3588 rail-specific sufficiency, exact trace widths, exact copper widths, or exact voltage-drop closure.
- It does not prove EMI, transient-response, stability, compliance, or production-readiness outcomes by itself.
