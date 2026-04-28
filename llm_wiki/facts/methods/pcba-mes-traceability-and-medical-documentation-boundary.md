---
fact_id: "methods-pcba-mes-traceability-and-medical-documentation-boundary"
title: "MES and traceability language for medical-adjacent PCBA should stay at build-history and documentation control level, not compliance-proof level"
topic: "PCBA MES traceability and medical documentation boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendhil-turnkey-assembly-product-page-en"
  - "frontendhil-small-batch-assembly-product-page-en"
  - "frontendhil-large-volume-assembly-product-page-en"
  - "frontendapt-pcba-components-bom-page-en"
  - "frontendapt-pcba-component-sourcing-page-en"
  - "frontendapt-industry-medical-page-en"
  - "ipc-1782b-traceability-standard-page"
  - "fda-21cfr-82065-traceability-page"
  - "fda-21cfr-820181-device-master-record-page"
  - "fda-21cfr-820184-device-history-record-page"
  - "fda-udi-basics-page"
tags: ["pcba", "mes", "traceability", "medical", "wearable", "documentation", "dhr", "dmr", "udi", "methods", "boundary"]
---

# Canonical Summary

> The current source layer supports a guarded traceability rewrite for medical-adjacent PCBA: `MES`, lot history, traveler-linked records, BOM/source control, and build-document discipline can be discussed as manufacturing-control and documentation layers, while medical `QMS`, `UDI`, `DMR`, and `DHR` vocabulary must remain contextual and must not be rewritten as proof that a PCB or PCBA supplier is itself FDA-compliant, device-approved, or universally required to maintain finished-device records.

## Stable Facts

- The internal PCBA quality-system page supports `traceability` and layered quality reporting as part of the assembly workflow.
- The HIL turnkey and small-batch assembly pages support traceability language in the context of BOM review, assembly/test planning, and launch-stage control.
- The HIL large-volume assembly page supports a later-stage manufacturing context where MES and traceability language can appear alongside scale-up framing, but its SPC and DPPM language remains refresh-sensitive.
- The internal BOM and component-sourcing pages support lot/source control, lifecycle review, authenticity checks, and build-input traceability as part of the turnkey PCBA workflow.
- The internal medical industry page supports application context for imaging, diagnostics, monitoring, and wearable hardware without proving regulatory status.
- `IPC-1782B` publicly supports internal and external traceability vocabulary across printed-board fabrication and assembly.
- FDA `21 CFR 820.65` supports narrower official traceability vocabulary around control numbers and lot/batch/unit traceability in regulated device contexts.
- FDA `21 CFR 820.181` and `21 CFR 820.184` support guarded `DMR` and `DHR` vocabulary for controlled manufacturing documentation and build-history records.
- FDA `UDI Basics` supports `UDI`, `DI`, and `PI` terminology as identification vocabulary rather than as a shortcut to complete PCB genealogy.

## Conditions And Methods

- Use this card for `traceability-mes-medical-imaging-wearable-2` and related medical-adjacent PCBA rewrites that need controlled vocabulary for build records, serialization context, lot traceability, traveler-linked reporting, or manufacturing-history framing.
- Keep `MES` language tied to manufacturing execution, record linkage, traceability, and release-document control rather than to regulatory approval.
- Treat `DMR`, `DHR`, and `UDI` as adjacent medical-documentation vocabulary that can explain why some programs ask for stronger document discipline; do not map those terms one-to-one onto every PCB traveler, every lot record, or every PCBA build packet.
- Pair this card with `pcba-fai-fqi-and-traceability-gates` and `pcba-bom-sourcing-and-traceability-posture` when the draft also discusses launch gates, sourcing control, or release evidence.
- Refresh any direct FDA wording before publication because the FDA and eCFR sources are dynamic.

## Limits And Non-Claims

- This card does not prove that any PCB or PCBA supplier is FDA registered, FDA inspected, ISO 13485 certified, or authorized to release a medical device.
- It does not prove that every wearable or medical-imaging program requires full unit-level genealogy, UDI labeling, or finished-device `DHR` records from the board supplier.
- It does not authorize claims about exact traceability levels, retention periods, serialization schemas, audit criteria, or release authority.
- It does not convert MES presence into proof of field reliability, supplier qualification, or customer acceptance.

## Open Questions

- Add a later card if a future rewrite needs a narrower split between `MES as manufacturing record layer` and `medical-device regulatory-role boundaries`.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/small-batch-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/large-volume-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/components-bom.json
- /code/hileap/frontendAPT/public/static/pcba/en/component-sourcing.json
- /code/hileap/frontendAPT/public/static/industries/en/medical-pcb.json
- https://shop.electronics.org/ipc-1782/ipc-1782-standard-only/Revision-b/english
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.65
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.181
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.184
- https://www.fda.gov/medical-devices/unique-device-identification-system-udi-system/udi-basics
