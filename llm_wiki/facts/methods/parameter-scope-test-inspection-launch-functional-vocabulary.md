---
fact_id: "methods-parameter-scope-test-inspection-launch-functional-vocabulary"
title: "FAI, USB-IF functional-test, and IPC metadata support launch and vocabulary boundaries, not generic pass/fail proof"
topic: "Test and inspection launch and functional-test vocabulary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "usb-if-type-c-functional-test-spec-2024-03-03"
  - "usb-if-type-c-cable-connector-spec-r2-0"
  - "usb-if-type-c-compliance-updates-page"
  - "usb-if-pd-compliance-updates-page"
  - "usb-if-qbs-information-page"
  - "usb-if-connector-qbs-guidelines-page"
  - "ipc-a-610h-toc"
  - "ipc-j-std-001j-toc"
  - "ipc-tm650-test-methods-index"
tags: ["fai", "usb-if", "functional-test", "vif", "type-c", "usb-pd", "ipc", "methods"]
---

# Canonical Summary

> The current source layer supports a conservative vocabulary boundary for `FAI` and `USB Type-C functional test`: FAI belongs to first-run verification and release readiness, while USB-IF functional-test material contributes product-specific vocabulary such as `Product Under Test`, `VIF`, `state machine`, and `VCONN`. IPC public metadata can anchor standard names, but none of these sources authorize generic pass/fail claims, certification claims, or exact electrical limits in blog copy.

## Stable Facts

- The internal APT first-article page frames FAI around first-run verification, setup confirmation, and NPI release support.
- The internal APT quality-system page places FAI inside a broader validation ladder that may also include SPI, AOI, AXI, ICT, FCT, burn-in, final inspection, and traceability.
- The USB-IF Type-C functional-test source explicitly supports vocabulary around product implementation data and product-specific functional-test context.
- The USB-IF Type-C cable-and-connector source supports the connector / plug / receptacle / cable-assembly scope boundary for `USB Type-C`.
- The USB-IF compliance-update and QbS sources support the idea that compliance and similarity handling are dynamic program contexts, not static proof that a board is certified.
- IPC public metadata supports naming `IPC-A-610H`, `J-STD-001J`, and `IPC TM-650` as standards anchors only.

## Named Parameters And Method Dimensions

- `FAI`:
  `first-run build verification`, `setup confirmation`, `NPI release`, and `process / materials / documentation readiness` are named by the internal APT first-article and quality-system pages.
- `USB-IF functional-test vocabulary`:
  `Product Under Test`, `VIF`, `functional test`, `state machine`, `VCONN`, and `USB PD implementation context` are named by the USB-IF Type-C functional-test record.
- `USB Type-C scope vocabulary`:
  `receptacle`, `plug`, `cable assembly`, `detection`, and the relationship between `USB Type-C` and `USB Power Delivery` are named by the USB-IF cable-and-connector record.
- `Dynamic compliance-program vocabulary`:
  `USB Type-C compliance updates`, `USB Power Delivery compliance updates`, and `Qualification by Similarity` are named by the USB-IF program pages.
- `IPC metadata anchors`:
  `IPC-A-610H`, `J-STD-001J`, and `IPC TM-650` can be named as public standards identifiers only.

## Scope And Non-Generalization

- Use this card when a draft needs to explain why first-build release, powered bring-up, and compliance vocabulary belong to different layers of the validation stack.
- Treat `FAI` as a launch and documentation gate, not as proof of SI, reliability, safety, or functional compliance.
- Treat `USB-IF functional-test` vocabulary as product-specific input vocabulary, not as permission to publish protocol tables, timers, voltage/current values, or pass/fail rules.
- Treat USB-IF compliance-update and QbS pages as dynamic program-context warnings, not certification evidence.
- Do not claim certification, logo eligibility, interoperability, charger output performance, or charger safety status from these sources alone.
- Do not turn IPC public metadata into clause-level accept/reject or soldering-process requirements.

## Blog Usage

- `FAI`:
  Safe support for wording such as `FAI confirms the first build matches the released package and planned process before broader ramp or validation steps continue`. Not safe support for production release proof by itself.
- `type-c charger`:
  Safe support for saying `Type-C charger boards may require product-specific VIF and powered functional-test inputs rather than a one-size-fits-all FCT script`, and for keeping compliance-program language guarded. Not safe support for certification or output-mode claims.
- `flying-probe / ICT`:
  Safe companion support for separating unpowered access checks from powered functional-test vocabulary.
- `low-void BGA`:
  Use only as a companion boundary: FAI may include launch inspection, but hidden-joint or void wording still belongs to optical / X-ray cards instead of this one.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- https://www.usb.org/sites/default/files/USB%20Type%20C%20Functional%20Test%20Specification%202024%2003%2003.pdf
- https://www.usb.org/sites/default/files/USB%20Type-C%20Spec%20R2.0%20-%20August%202019.pdf
- https://compliance.usb.org/index.asp?Format=Standard&UpdateFile=USBC
- https://compliance.usb.org/index.asp?Format=Standard&UpdateFile=PowerDelivery
- https://compliance.usb.org/qbs/QbSInfo.php
- https://compliance.usb.org/QbS/ConnectorGuide.htm
- https://www.ipc.org/TOC/IPC-A-610H-toc.pdf
- https://www.ipc.org/TOC/IPC-J-STD-001J_TOC.pdf
- https://www.electronics.org/test-methods
