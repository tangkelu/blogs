---
topic_id: "processes-usb-c-charger-readiness-classification"
title: "USB-C Charger Readiness Classification"
category: "processes"
status: "draft"
last_reviewed_at: "2026-04-27"
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

> This readiness classification maps what the current local source layer can and cannot support for the `type-c-charger` empty-image candidate and its adjacent charger or inverter slugs. It is designed to prevent protocol and power-performance drift while still unlocking conservative PCB and PCBA rewrite language.

## Readiness Verdicts

- `type-c-charger`
  Verdict: `boundary_ready_with_usb_if_vocabulary`
- `ultra-fast-charger-power-energy`
  Verdict: `boundary_ready_with_blocked_performance_claims`
- `central-inverter-power-energy`
  Verdict: `adjacent_context_only`

## What Is Now Safe

- `type-c-charger` can now be written as a compact charger-board manufacturing article focused on connector-zone planning, interface-side protection review, controller and power-stage vocabulary separation, assembly inspection, and powered FCT handoff.
- USB-IF source coverage now supports controlled vocabulary such as `USB Type-C`, `USB-C`, `USB Power Delivery`, `PPS`, `VIF`, compliance updates, and QbS context.
- `ultra-fast-charger-power-energy` can now reuse the same board-partition and validation workflow language, but only at the level of charger-board architecture, interface review, and test sequencing.
- `central-inverter-power-energy` may borrow boundary wording only where it helps separate board-level power, control, connector, cable, and test vocabulary from unsupported charger-style protocol drift.

## Blocked Claim Classes

- USB-C connector-role detail, CC behavior, cable-role logic, e-marker behavior, alternate mode, and exact interface behavior
- PD and PPS revision detail, message sequencing, mode tables, output profiles, and negotiation specifics
- QbS eligibility, USB-IF certification status, logo-use claims, or current compliance-program requirements without live refresh
- Exact charger output power, voltage, current, charging speed, efficiency, thermal-rise, power density, or adapter claims
- Exact ESD, surge, fuse, protection, safety, isolation, creepage, clearance, and compliance claims
- Exact connector mechanical dimensions, retention numbers, footprint values, and routing or spacing prescriptions
- Claims that any named controller topology, semiconductor choice, or protection stack is required by default

## Rewrite Posture By Slug

- `type-c-charger`
  Preferred language: connector shell anchoring, compact interface layout review, nearby protection placement, controller-zone separation, solder-joint inspection, and powered functional bring-up.
- `ultra-fast-charger-power-energy`
  Preferred language: power-board and control-board partitioning, cable or connector handoff, heat-oriented platform choice as project-dependent, and staged inspection plus FCT workflow.
- `central-inverter-power-energy`
  Preferred language: interface vocabulary boundaries only, especially where writers might otherwise blur board-level connector or cable planning into charger-protocol language.

## Remaining Gaps

- USB-IF source records now cover USB Type-C / USB-C vocabulary, Type-C functional-test context, compliance updates, QbS context, and language guidance.
- No admissible current extraction for exact charger connector geometry, role behavior, PD / PPS values, cable-marker behavior, or protocol tables
- No current support for fast-charge marketing claims, compliance claims, or power-performance numerics

## Publication Rule

- Do not treat this note as a protocol-data unlock. It upgrades `type-c-charger` from manufacturing-boundary-only support to USB-IF-vocabulary-aware conservative rewrite posture, but exact protocol, connector, certification, power, thermal, and compliance claims remain blocked.

## Related Fact Cards

- `methods-usb-c-pd-pps-protocol-context-boundary`
- `methods-charger-pcb-pcba-manufacturing-boundary`
- `methods-power-energy-inverter-charger-rewrite-boundary`
- `methods-tht-pressfit-terminal-route-boundary`
- `methods-pcba-ict-vs-fct-boundary`

## Primary Sources

- https://www.usb.org/sites/default/files/USB%20Type-C%20Spec%20R2.0%20-%20August%202019.pdf
- https://www.usb.org/sites/default/files/USB%20Type%20C%20Functional%20Test%20Specification%202024%2003%2003.pdf
- https://compliance.usb.org/index.asp?Format=Standard&UpdateFile=PowerDelivery
- https://compliance.usb.org/index.asp?Format=Standard&UpdateFile=USBC
- https://compliance.usb.org/QbS/ConnectorGuide.htm
- https://compliance.usb.org/qbs/QbSInfo.php
- https://www.usb.org/sites/default/files/usb_type-c_language_product_and_packaging_guidelines_20230320.pdf
- /code/hileap/frontendAPT/public/static/industries/en/power-energy-pcb.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendHIL/public/static/products/en/through-hole-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/cable-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/harness-assembly.json
