---
fact_id: "standards-fda-medical-device-documentation-and-traceability-metadata"
title: "Public FDA and eCFR records support medical-device supplier-control, traceability, and documentation vocabulary, not blanket PCB regulatory claims"
topic: "FDA medical device documentation and traceability metadata"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids:
  - "fda-qmsr-page"
  - "fda-udi-basics-page"
  - "fda-21cfr-82050-purchasing-controls-page"
  - "fda-21cfr-82065-traceability-page"
  - "fda-21cfr-820181-device-master-record-page"
  - "fda-21cfr-820184-device-history-record-page"
tags: ["fda", "qmsr", "udi", "21-cfr-part-820", "purchasing-controls", "traceability", "dmr", "dhr", "medical-devices", "metadata"]
---

# Canonical Summary

> Public FDA and eCFR records are now strong enough to support guarded medical-device quality-system vocabulary in `llm_wiki`: `QMSR` for the current FDA quality-system framing, `UDI` for identification terms, `21 CFR 820.50` for supplier and purchasing-control language, `21 CFR 820.65` for traceability and control-number vocabulary, `21 CFR 820.181` for `DMR` and controlled manufacturing-document language, and `21 CFR 820.184` for `DHR` and manufacturing-history / release-record vocabulary. None of these sources make bare PCB fabrication a universal FDA-regulated activity, and none prove supplier qualification by themselves.

## Stable Facts

- FDA's public `QMSR` page is the top-level current regulatory anchor in this corpus for medical-device quality-system framing tied to `21 CFR Part 820` and `ISO 13485:2016`.
- FDA's public `UDI Basics` page supports guarded vocabulary for `DI`, `PI`, `GUDID`, and related device-identification terms.
- `21 CFR 820.50` gives this corpus a public regulatory anchor for purchasing controls, supplier evaluation/selection, defined supplier controls, and documented purchasing requirements.
- `21 CFR 820.65` gives this corpus a narrower official traceability anchor tied to control numbers and lot/batch/unit traceability where the device-risk context requires it.
- `21 CFR 820.181` gives this corpus a clean official anchor for `Device Master Record` vocabulary and controlled manufacturing-document language.
- `21 CFR 820.184` gives this corpus a clean official anchor for `Device History Record`, build-history, acceptance-record, and release-record vocabulary.

## Conditions And Methods

- Use this card when a `22-layer` or other hi-rel draft needs medical-device-adjacent vocabulary for supplier control, lot traceability, approved build documentation, or manufacturing history.
- Pair it with customer flowdowns, actual supplier certifications, and program-specific role definitions before making claims about regulatory applicability, compliance, or release authority.
- Use this card to keep medical-device quality-system language precise instead of flattening all high-reliability PCB work into generic `FDA-compliant` marketing claims.

## Limits And Non-Claims

- This card does not prove that any PCB fabricator or assembler is FDA registered, inspected, compliant, or approved.
- It does not establish that bare-PCB fabrication is automatically subject to these rules in every project context.
- It does not provide document templates, audit criteria, retention periods, release conditions, or supplier-approval thresholds.

## Open Questions

- Decide whether future hi-rel evidence packs need a separate card for medical-device supplier-role boundaries so `component / PCB / PCBA / finished-device` obligations are not collapsed into one layer.
- Decide whether the FDA/eCFR medical-documentation layer should be merged into the broader hi-rel metadata card or kept separate for cleaner regulatory scoping.

## Source Links

- https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-system-qs-regulationmedical-device-current-good-manufacturing-practices-cgmp
- https://www.fda.gov/medical-devices/unique-device-identification-system-udi-system/udi-basics
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.50
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.65
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.181
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.184
