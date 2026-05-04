---
topic_id: "processes-usb-c-charger-readiness-classification"
title: "USB-C Charger Readiness Classification"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
fact_ids:
  - "methods-usb-c-pd-pps-protocol-context-boundary"
  - "methods-charger-pcb-pcba-manufacturing-boundary"
  - "methods-power-energy-inverter-charger-rewrite-boundary"
  - "methods-tht-pressfit-terminal-route-boundary"
  - "methods-pcba-ict-vs-fct-boundary"
source_ids:
  - "usb-if-type-c-cable-connector-spec-r2-0"
  - "usb-if-type-c-functional-test-spec-2024-03-03"
  - "usb-if-pd-compliance-updates-page"
  - "usb-if-type-c-compliance-updates-page"
  - "usb-if-connector-qbs-guidelines-page"
  - "usb-if-qbs-information-page"
  - "usb-if-type-c-language-guidelines-2023"
  - "frontendapt-industry-power-energy-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendhil-through-hole-assembly-product-page-en"
  - "frontendapt-pcba-cable-assembly-page-en"
  - "frontendapt-pcba-harness-assembly-page-en"
tags: ["usb-c", "charger", "type-c", "readiness", "power-energy", "fct", "boundary"]
---

# Definition

> This page classifies what the current local source and fact layer can safely support for `type-c-charger` and adjacent charger-language rewrites. It promotes the topic to active only at a manufacturing-boundary and controlled-vocabulary level, not as a protocol-detail or power-performance unlock.

## Routing Guidance

- Use this page when the article needs a go or no-go boundary for `type-c-charger` rewrite posture.
- Route connector-zone planning, interface-side protection review, controller-versus-power-stage separation, assembly inspection, and powered functional handoff here.
- Route `USB Type-C`, `USB-C`, `USB Power Delivery`, `PPS`, `VIF`, compliance-update, and QbS wording here only as controlled vocabulary.
- Route ICT-versus-FCT framing here when the story needs to separate manufacturing-defect checks from powered bring-up checks.
- Route exact protocol behavior, negotiation flow, connector mechanics, charger topology, certification, logo-use, and numeric performance claims elsewhere.

## Why This Topic Matters

- USB-C charger drafts become unsafe when connector language, protocol language, and power-board manufacturing language get collapsed into one claim set.
- The current corpus is strong enough to support a conservative charger-board rewrite, but only when the page keeps USB-IF terms as context and keeps manufacturing claims at PCB and PCBA review level.
- This classification gives writers one place to separate safe local facts from blocked charger-performance and compliance drift.

## Stable Facts

- `type-c-charger` is active for a conservative charger-board manufacturing article focused on connector access, local protection review, controller-zone separation, assembly checks, and powered functional validation.
- USB-IF source coverage supports controlled vocabulary for `USB Type-C`, `USB-C`, `USB Power Delivery`, `PPS`, `VIF`, compliance updates, and QbS program context.
- USB-IF functional-test context supports the idea that Type-C and PD test applicability is implementation-dependent and should not be treated as one universal script.
- The internal power-energy page supports generic charger and charging-electronics context inside a broader power-board, control-board, and interface-board story.
- The internal PCBA quality and FCT pages support staged DFM, DFT, inspection, electrical validation, and final powered functional-test handoff after assembly.
- The current internal interface-route facts support separating board-mounted connector retention from off-board cable or harness integration instead of assuming one universal charger interface route.
- `ultra-fast-charger-power-energy` can reuse the same partitioning and validation posture at board-review level, but it remains blocked from performance proof.
- `central-inverter-power-energy` is adjacent context only and may borrow only the board-partition and validation boundary, not charger-protocol language.

## Engineering Boundaries

- Keep `USB-C` and `USB Type-C` as connector-family and interface-context terms, not as proof of exact connector behavior, cable capability, or pin-level implementation.
- Keep `PD`, `Power Delivery`, and `PPS` as protocol-context vocabulary only. They do not authorize negotiation-sequence detail, output-profile detail, or charger capability tables.
- Keep charger-board language on connector shell anchoring, board-edge access, nearby protection review, controller and power-stage separation, inspection, and powered bring-up.
- Keep interface-route wording generic: board-mounted connector retention, press-fit-versus-solder route choice, and cable or harness handoff stay design-dependent choices.
- Keep validation wording split between ICT for electrical-connectivity and manufacturing-defect framing, and FCT for powered behavior and end-use simulation framing.
- Keep thermal-platform, heavy-copper, and board-topology language project-dependent. The current corpus does not support a universal charger architecture.

## Blocked Claims

- protocol-detail and negotiation claims, including CC behavior, role logic, message sequence, mode tables, cable-marker behavior, and alternate-mode behavior
- exact power, thermal, or compliance numerics, including output power, charging speed, efficiency, temperature rise, current, voltage, density, spacing, creepage, or clearance values
- certification or logo-use claims, including USB-IF certification status, current compliance-program status, QbS eligibility outcomes, and trademark or logo authorization
- universal charger-topology claims, including any statement that a named power stage, controller stack, protection topology, or thermal platform is required by default
- exact connector mechanical, footprint, retention, drilling, or routing-prescription claims
- exact safety, surge, fuse, isolation, ESD, or protection-stack performance claims

## Common Misreadings

- `USB-C charger` is not a permission to publish PD or PPS negotiation detail.
- USB-IF vocabulary support is not certification proof.
- QbS program context is not a no-test or auto-approval claim.
- A powered FCT handoff is not the same thing as protocol compliance validation.
- A charger-board rewrite is not evidence for exact charging speed, thermal behavior, or adapter compatibility.
- Power-energy board partitioning does not prove one charger topology is universal.

## Must Refresh Before Publishing

- Any exact PD, PPS, CC, role-detection, cable-marker, alternate-mode, or message-sequencing statement
- Any exact power, current, voltage, charging-speed, efficiency, thermal-rise, density, or safety-spacing number
- Any USB-IF certification, compliance-program, QbS eligibility, trademark, or logo-use statement
- Any exact connector footprint, retention, pad geometry, mechanical dimension, or routing-rule claim
- Any statement that moves from conservative board-review language into universal topology or compliance proof

## Related Facts And Source Scope

- `methods-usb-c-pd-pps-protocol-context-boundary`
- `methods-charger-pcb-pcba-manufacturing-boundary`
- `methods-power-energy-inverter-charger-rewrite-boundary`
- `methods-tht-pressfit-terminal-route-boundary`
- `methods-pcba-ict-vs-fct-boundary`

## Source Scope

- `usb-if-type-c-cable-connector-spec-r2-0`
- `usb-if-type-c-functional-test-spec-2024-03-03`
- `usb-if-pd-compliance-updates-page`
- `usb-if-type-c-compliance-updates-page`
- `usb-if-connector-qbs-guidelines-page`
- `usb-if-qbs-information-page`
- `usb-if-type-c-language-guidelines-2023`
- `frontendapt-industry-power-energy-page-en`
- `frontendapt-pcba-quality-system-page-en`
- `frontendapt-pcba-fct-test-page-en`
- `frontendhil-through-hole-assembly-product-page-en`
- `frontendapt-pcba-cable-assembly-page-en`
- `frontendapt-pcba-harness-assembly-page-en`
