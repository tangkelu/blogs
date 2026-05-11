---
fact_id: "methods-exposed-pad-ground-tie-and-local-thermal-spreading-boundary"
title: "Exposed-pad guidance may be reused only as a package-scoped board-attach, local thermal-spreading, and conditional low-impedance tie boundary"
topic: "Exposed-pad ground tie and local thermal spreading boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-11"
exact_data_class: "boundary_convention"
scope_type: "owner_scoped_exposed_pad_board_attach_and_conditional_ground_tie_boundary"
canonical_unit_policy: "Preserve wording such as exposed pad or exposed paddle soldered to the board, local heat-spreading or thermal path into the PCB, and conditional low-impedance electrical tie only when the owner package or datasheet shows that the pad is externally grounded or assigned to ground. Do not normalize this into universal `EPAD = GND`, exact via arrays, paste-window rules, or guaranteed EMI / thermal outcomes."
source_ids:
  - "analog-devices-exposed-pads-brief-introduction"
  - "ti-powerpad-thermally-enhanced-package"
tags: ["exposed-pad", "thermal-pad", "powerpad", "epad", "thermal", "ground", "package", "board-attach", "methods"]
---

# Canonical Summary

> Current public semiconductor-owner guidance is strong enough to support one narrow exposed-pad boundary: an exposed pad or paddle is a package-scoped board-attach region that supports local heat spreading into the PCB, and it may also serve as a low-impedance electrical tie only when the owner package or datasheet shows that the pad is externally grounded or otherwise assigned to that net. This supports guarded layout-review wording only. It does not authorize a universal `EPAD = GND` rule, exact via arrays, exact paste or stencil recipes, or guaranteed thermal, EMI, or reliability outcomes.

## Stable Facts

- Analog Devices treats the exposed paddle as a package feature that provides a thermal path from the die into the PCB.
- Analog Devices also states that the same paddle may provide a low-impedance electrical path when the die-attach region is externally grounded.
- TI treats the exposed PowerPAD as a package feature that is meant to be soldered to the PCB rather than left electrically and thermally floating.
- TI also states that the correct plane or net tie must be verified from the owner datasheet because the exposed pad may connect to signal, power, or ground depending on the device.

## Exact Data Scope

- exact for:
  - exposed-pad or exposed-paddle board attach as a package-scoped thermal path into the PCB
  - local heat spreading or heat transfer into the board as the primary role vocabulary
  - conditional low-impedance electrical tie only when owner documentation shows the pad is grounded or assigned to that net
  - the need to verify the exposed-pad electrical role from package-owner or device-owner documentation
- not exact for:
  - a universal `thermal pad must connect to GND` rule
  - exact via counts, via diameters, via-in-pad rules, or fill / cap rules
  - exact stencil aperture, paste-windowing, voiding, or solder-thickness rules
  - exact thermal resistance improvement, junction temperature improvement, or current-capacity gains
  - guaranteed EMI, EMC, impedance, noise, or reliability outcomes

## Conditions And Methods

- Use this card when a prompt needs safe wording for `exposed pad`, `thermal pad`, `PowerPAD`, `EPAD`, or package underside thermal attach.
- Keep the language at boundary level:
  - solder the exposed pad to the PCB as part of the package attach strategy
  - treat the pad as a local heat-spreading path into the board
  - treat the pad as a low-impedance electrical tie only when the owner package or datasheet assigns it to ground or another specific net
  - verify the net assignment from owner documentation before reusing the wording
- Pair this card with `methods-ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity` only when the draft separately needs generic return-path continuity language.
- Pair this card with `methods-switch-mode-power-emc-placement-and-hot-loop-boundary` only when the draft separately needs switcher hot-loop or noisy power-stage placement language.
- Pair this card with `methods-processor-power-pin-local-decoupling-capacitor-placement-boundary` only when the draft separately needs near-device decoupling placement language.

## Safe Blog Usage

- Explain that an exposed pad is first a package-attach and thermal-path feature, not automatically a universal ground doctrine.
- Explain that some owner package designs also use the same pad as a low-impedance electrical connection, but that this depends on the device and package definition.
- Explain that the correct net tie must be checked from the owner datasheet or package note before turning exposed-pad language into board guidance.
- Explain that this lane supports guarded package-review posture, not proof of thermal closure or EMI success.

## Limits And Non-Claims

- This card does not authorize a universal `EPAD = GND` rule.
- It does not authorize exact via arrays, exact hole sizes, or exact via-in-pad manufacturing posture.
- It does not authorize exact stencil, paste, or voiding rules.
- It does not authorize exact thermal-resistance, junction-temperature, current-capacity, EMI, EMC, or reliability outcomes.
- It does not prove that one package family's exposed-pad practice transfers unchanged across vendors or package families.

## Source Links

- https://www.analog.com/en/resources/design-notes/2022/07/16/08/51/exposed-pads-a-brief-introduction.html
- https://www.ti.com/lit/an/slma002h/slma002h.pdf
