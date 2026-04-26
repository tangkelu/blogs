---
fact_id: "methods-pcba-bom-sourcing-and-traceability-posture"
title: "Internal PCBA pages tie BOM sourcing, lifecycle review, authenticity, and traceability into turnkey assembly"
topic: "PCBA BOM sourcing and traceability"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcba-component-sourcing-page-en"
  - "frontendapt-pcba-turnkey-assembly-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendhil-turnkey-assembly-product-page-en"
  - "frontendhil-box-build-assembly-product-page-en"
tags: ["internal", "pcba", "bom", "component-sourcing", "traceability", "turnkey", "supply-chain"]
---

# Canonical Summary

> The internal PCBA pages treat component sourcing as part of manufacturing quality, not merely purchasing: BOM review, authorized sourcing, authenticity checks, lifecycle / obsolescence management, lot traceability, and assembly/test records are all framed as part of the turnkey PCBA workflow.

## Stable Facts

- The APT component-sourcing page frames sourcing as integrated with PCB manufacturing and assembly.
- The same page discusses authenticity, supplier qualification, component inspection, compliance, BOM review, technical support, and obsolescence management.
- The APT turnkey assembly page frames BOM review, lifecycle checks, AVL alignment, component sourcing, SMT/THT assembly, test, box build, and logistics as one service scope.
- The APT quality-system page places IQC, test evidence, traceability, and final inspection inside the PCBA quality system.
- The HIL turnkey page similarly frames BOM lifecycle control, sourcing, SMT/THT, inspection, ICT/FCT/boundary scan, and MES traceability as connected.
- The HIL box-build page extends traceability from PCBA into enclosure integration, harness, firmware, system test, packaging, and logistics.

## Conditions And Methods

- Use this card for turnkey PCBA, BOM-risk, supply-chain, traceability, and NPI-to-production planning content.
- Refresh supplier counts, lead-time claims, lifecycle notification windows, and current market availability before publication.
- Treat third-party component examples as internal page content, not proof of current stocking or authorized distribution.

## Limits And Non-Claims

- This card does not guarantee availability, pricing, lead time, or authorized status for any named component.
- It does not prove every BOM receives the same level of authenticity testing.
- It does not replace a live BOM scrub, AVL review, or supplier-status check.

## Open Questions

- Add an official standards metadata batch for AS6081, IPC-1782, and related traceability / counterfeit-prevention references.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/component-sourcing.json
- /code/hileap/frontendAPT/public/static/pcba/en/turnkey-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/box-build-assembly.json

