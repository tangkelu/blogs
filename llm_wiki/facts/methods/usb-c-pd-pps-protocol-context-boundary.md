---
fact_id: "methods-usb-c-pd-pps-protocol-context-boundary"
title: "USB-C, PD, and PPS vocabulary should be treated as protocol context, not as charger-performance proof"
topic: "USB-C PD PPS protocol context boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
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
tags: ["usb-c", "type-c", "usb-pd", "pps", "charger", "protocol", "controller", "fct", "methods"]
---

# Canonical Summary

> The current source layer now includes official USB-IF anchors for USB Type-C connector / cable scope, Type-C functional-test context, USB PD / Type-C compliance updates, QbS program context, and Type-C language guidance. That is enough to use `USB-C`, `USB Type-C`, `USB Power Delivery`, `PPS`, `VIF`, `compliance update`, and `Qualification by Similarity` as controlled vocabulary in `type-c-charger` planning copy. It is still not enough to publish exact protocol behavior, pinout tables, power-mode tables, certification status, charger-output claims, or connector mechanical prescriptions.

## Stable Facts

- USB-IF Type-C specification coverage supports Type-C connector and cable ecosystem vocabulary, and it positions Type-C alongside USB 2.0, USB 3.2, USB4, and USB Power Delivery scope.
- USB-IF Type-C functional-test coverage supports functional-test and product-implementation vocabulary such as `Product Under Test`, `VIF`, and implementation-dependent test applicability.
- USB-IF PD and Type-C compliance-update pages support a dynamic compliance-program context; they must be refreshed before any current policy, date, certification, or PPS-related statement is published.
- USB-IF QbS pages support the idea that connector, cable, and product-family similarity is a formal program context, not an automatic certification or no-test claim.
- USB-IF language guidance supports terminology discipline for `USB Type-C` / `USB-C` wording without proving engineering performance.
- The current internal power-energy page supports generic charging-electronics context, which is enough to place a compact charger board inside a broader power-control and interface story.
- The current PCBA quality-system page supports DFM, DFT, inspection, electrical validation, and final functional validation as a staged workflow around an assembled board.
- The current FCT page supports powered functional verification, fixture planning, firmware or configuration loading, and application-specific pass or fail checks after assembly.
- Taken together, these sources support a conservative claim that protocol-aware charger products need board-level planning across connector access, controller behavior, powered test setup, and assembly review.

## Conditions And Methods

- Use `USB Type-C` / `USB-C` as connector-family and interface-context vocabulary, not as proof of any exact power lane, signaling map, mechanical prescription, or cable capability.
- Use `PD` or `Power Delivery` only as negotiation-context vocabulary that tells the writer a charger board may include policy, role-management, or source/sink interaction logic.
- Use `PPS` only as a refresh-sensitive USB PD / compliance-context term; do not publish behavior, mode, or output tables from this card.
- Use `VIF` as a clue that Type-C / PD functional testing can be product-implementation-specific; do not imply one universal FCT script.
- Use `QbS` only to explain why connector, cable, or design similarity is a controlled compliance-program topic; do not claim reduced testing, certification status, or eligibility.
- Safe `type-c-charger` posture: describe connector-side planning, control-path coordination, and powered verification without claiming exact source or sink behavior.
- Safe control-language examples: `CC/PD controller`, `power-path controller`, `charger controller`, `role-detection logic`, `firmware-assisted bring-up`, and `functional-test script inputs`, provided the wording stays generic.
- If the draft moves from protocol names into `who negotiates what, when, or at which exact levels`, stop and require a separate current USB-IF extraction pass.

## Limits And Non-Claims

- This card does not authorize exact USB-C pin, lane, resistor, orientation, cable-marker, current-advertisement, or alternate-mode claims.
- It does not authorize exact PD or PPS revisions, message flow, voltage or current steps, source or sink tables, EPR / SPR tables, or charger output modes.
- It does not authorize `fast charging`, `ultra fast charging`, `high wattage`, `smart charging`, `safe charging`, or adapter-compatibility claims.
- It does not prove a given charger design uses a dedicated `CC`, `PD`, or `PPS` controller instead of an integrated power-management IC.
- It does not support USB-IF certification, logo, compliance, QbS eligibility, interoperability, thermal-rise, efficiency, reliability, or safety claims.

## Open Questions

- Add a separate parameter-governed extraction pass if future drafts need exact PD / PPS / EPR / SPR values, message behavior, cable markers, or connector mechanical data.
- Add a separate certification / logo-use boundary card if future drafts need USB-IF certification or trademark claims.

## Source Links

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
