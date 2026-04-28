---
fact_id: "methods-pcba-medical-traceability-dhr-dmr-boundary"
title: "Medical-adjacent MES, traceability, DMR, and DHR language should stay at manufacturing-record boundary level in public PCBA rewrites"
topic: "medical-adjacent PCBA traceability boundary"
category: "methods"
status: "verified"
confidence: "high"
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
tags: ["pcba", "medical", "wearable", "mes", "traceability", "dmr", "dhr", "udi", "documentation", "boundary"]
---

# Canonical Summary

> For public medical-imaging and wearable PCBA rewrites, `MES`, lot history, traveler linkage, component-source control, and build-record discipline can be described as manufacturing-control language. `DMR`, `DHR`, `UDI`, and regulated traceability terms may appear only as adjacent vocabulary that explains why some customers ask for stricter documentation. They must not be used as proof of FDA applicability, device-release authority, supplier certification, or universal finished-device record ownership by the board supplier.

## Stable Facts

- The internal PCBA quality-system page supports traceability, staged inspection, and record-linked production control as part of the assembly workflow.
- The turnkey, small-batch, and large-volume assembly pages support MES and traceability language in the context of BOM review, launch control, and repeat-manufacturing governance.
- The BOM and component-sourcing pages support source-control, lot linkage, lifecycle review, and build-input traceability as part of turnkey PCBA operations.
- The internal medical page supports medical-imaging, monitoring, diagnostics, and wearable application framing without proving regulatory standing.
- `IPC-1782B` supports public traceability vocabulary for fabrication and assembly ecosystems.
- FDA `21 CFR 820.65` supports narrower official traceability language around control numbers and lot, batch, or unit identification in regulated device contexts.
- FDA `21 CFR 820.181` and `21 CFR 820.184` support guarded `DMR` and `DHR` vocabulary for controlled manufacturing documentation and manufacturing-history records.
- FDA `UDI Basics` supports identification vocabulary such as `UDI`, `DI`, and `PI`, but not a blanket claim that every PCB or PCBA supplier owns finished-device identification duties.

## Safe Public Rewrite Boundary

- Use `MES` as manufacturing-execution and record-linkage language:
  traveler status, lot linkage, source tracking, build history, and inspection/report association.
- Use `traceability` as a configurable governance layer around material, component, process, and build records:
  do not flatten it into `full genealogy` unless a narrower source stack exists.
- Use `DMR` and `DHR` only as medical-adjacent reference vocabulary that explains why some regulated programs request stronger document discipline.
- Treat `UDI` as identification-system context, not as a proxy for board-level serialization completeness.
- Keep public rewrite language at `documentation boundary`, `record linkage`, `build packet discipline`, `lot and source visibility`, and `release-workflow inputs`.

## Conditions And Methods

- Use this card for `traceability-mes-medical-imaging-wearable-2`.
- Pair it with `methods-pcba-mes-traceability-and-medical-documentation-boundary` when a draft needs broader shared context, but keep this card as the slug-specific public-safety boundary.
- Pair it with `methods-pcba-fai-fqi-and-traceability-gates` when the article also discusses first-build release evidence.
- Refresh any direct FDA wording before publication because the FDA and eCFR source pages are dynamic.

## Limits And Non-Claims

- This card does not prove that any PCB or PCBA supplier is FDA registered, FDA inspected, ISO 13485 certified, or authorized to release a medical device.
- It does not prove that every medical-imaging or wearable program requires unit-level genealogy, finished-device `DHR` custody, or `UDI` labeling from the board supplier.
- It does not authorize retention-period claims, serialization-schema claims, audit-readiness claims, or release-authority claims.
- It does not turn `MES` or traceability language into proof of patient safety, product effectiveness, field reliability, or customer acceptance.

## Open Questions

- Add a later role-boundary card if a future rewrite must distinguish `board supplier records` from `finished-device manufacturer records` more explicitly.

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
