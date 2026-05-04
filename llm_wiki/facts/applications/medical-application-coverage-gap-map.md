---
fact_id: "applications-medical-application-coverage-gap-map"
title: "Medical device application coverage gap map: which board families and regulatory layers have wiki-level routing and which remain blocked"
topic: "Medical device PCB/PCBA application coverage"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-159 landed the broad medical boundary page; this card tracks sub-family routing, remaining blocked regulatory layers, and medical-specific reopen conditions"
source_ids:
  - "frontendapt-industry-medical-page-en"
  - "fda-21cfr-82065-traceability-page"
  - "fda-21cfr-820181-device-master-record-page"
  - "fda-21cfr-820184-device-history-record-page"
  - "fda-qmsr-page"
  - "fda-udi-basics-page"
  - "ipc-1782b-traceability-standard-page"
tags: ["medical", "medical-device", "imaging", "wearable", "diagnostics", "iec-60601", "iso-13485", "fda", "coverage-map", "gap-map"]
---

# Canonical Summary

> As of 2026-05-03 after P4-168 activation review, the medical application family has a broad wiki boundary page (`wiki/applications/medical-device-pcb-pcba-boundary-map.md`) that is now `active`, plus a narrow hearing-aid sub-lane and a process-level rewrite gate for imaging/wearable slugs. This card maps what is currently safe, what remains blocked, and which medical sub-families still need narrower follow-on aggregation.

## Coverage State By Sub-Family

### Wiki-Layer: Narrow Lane (Hearing Aid Only)

| Coverage | Wiki Page | What It Covers |
|---|---|---|
| **Hearing Aid PCB** | `wiki/applications/hearing-aid-pcb-review-boundaries.md` | LE Audio, Auracast, telecoil identity nouns; medical-adjacent manufacturing-control vocabulary; does NOT cover general medical device design |

### Process-Layer: Rewrite Gate (Medical Imaging / Wearable Slugs)

| Coverage | Gate Page | What It Covers |
|---|---|---|
| **Medical Imaging / Wearable slug rewrite** | `wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate.md` | MES traceability, conformal coating, THT mixed-technology, low-void BGA for medical-adjacent context; slug-specific safe-angle classification only |

### Fact-Card Layer: Already Landed

| Fact Card | Coverage |
|---|---|
| `methods-pcba-medical-traceability-dhr-dmr-boundary` | MES, DMR/DHR boundary, UDI context (manufacturing-record level only) |
| `methods-medical-manufacturing-control-context-for-coating-tht-and-bga` | Coating, THT, BGA in medical-adjacent manufacturing-control context |
| `methods-pcba-mes-traceability-and-medical-documentation-boundary` | MES and documentation boundary for regulated programs |
| `standards-fda-medical-device-documentation-and-traceability-metadata` | FDA 21 CFR 820.65 / 820.181 / 820.184 / UDI metadata vocabulary |
| `standards-automotive-medical-aerospace-application-qualification-boundary` | FDA MRI/QMSR, ISO 13485, IEC 60601 as qualification-boundary vocabulary (NOT compliance proof) |

### Remaining Sub-Family And Regulatory Gaps

| Sub-Family | Gap | Reopen Condition |
|---|---|---|
| **Patient Monitoring / Life-Support** | No dedicated boundary page; safe board-class vocabulary available from Tier-2 source | New dedicated aggregation pass |
| **Medical Imaging (broad)** | Rewrite gate covers slug-specific framing only; no broad routing page | New dedicated aggregation pass |
| **IVD / Lab Equipment** | No dedicated boundary page | New dedicated aggregation pass |
| **Therapeutic / Surgical Devices** | Covered by broad medical boundary page; cleaning/disinfection context still blocked at compliance level | Official IEC 60601-1 particular-standard and device-class source recovery |
| **Wearable / Home Medical** | Covered by the broad medical boundary page; rewrite gate still provides useful slug-level process routing | New dedicated sub-lane only if a narrower wearable-medical boundary page becomes necessary |
| **Medical Power Supply / Isolation** | Covered by broad medical boundary page; exact compliance-distance and safety-proof claims remain blocked | Official IEC 60601-1 particular-standard and device-class source recovery |
| **ISO 13485 QMS vocabulary** | Only qualification-boundary level (automotive-medical-aerospace fact card); no clause-level source | Official ISO 13485 source recovery |
| **IEC 60601-1 safety standard** | Source is in registry at metadata/identity level only; compliance and applied-parts claims remain blocked | Stronger clause-adjacent or device-class source recovery if later needed |
| **Biocompatibility (ISO 10993)** | Not in sources registry; blocked | Official ISO 10993 source recovery |

## Stable Facts

- The Tier-2 medical source covers 6 board sub-families: patient monitoring/life-support, medical imaging, IVD/lab, therapeutic/surgical, wearable/home medical, and medical power/isolation.
- All 6 sub-families support board-class vocabulary and engineering-context description at Tier-2 level.
- The existing medical-adjacent fact card layer (traceability/MES, coating, THT, BGA) already covers significant manufacturing-control vocabulary for all sub-families.
- IEC 60601-1 (general medical electrical equipment safety) is present in the sources registry at standard-identity level, but that does NOT unlock applied electrical safety, leakage current, creepage/clearance, or applied-parts compliance claims.
- ISO 13485 is available only at QMS vocabulary boundary level (from `standards-automotive-medical-aerospace-application-qualification-boundary`); clause-level sourcing is not available.
- FDA 21 CFR 820 (QMSR) is available at boundary level for documentation (DMR, DHR, UDI) only.

## Conditions And Methods

- When writing any medical-device PCB article, check the "Already Landed" fact cards before writing new boundaries.
- Route hearing-aid-specific content to `wiki/applications/hearing-aid-pcb-review-boundaries.md`.
- Route process-level slug content (conformal coating, THT, low-void BGA, MES) to `wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate.md`.
- Use this broad boundary page (`wiki/applications/medical-device-pcb-pcba-boundary-map.md`) for application-layer routing across all medical sub-families.

## Limits And Non-Claims

- IEC 60601-1 compliance, applied-parts classification (Type B/BF/CF), leakage current, or electrical safety proof is NOT supported.
- ISO 13485 QMS certification, clause-level requirements, or supplier audit status is NOT supported.
- FDA 510(k), PMA, De Novo, or device clearance/approval claims are NOT supported.
- ISO 10993 biocompatibility, sterilization compatibility, or patient-contact suitability is NOT supported.
- Patient safety outcomes, clinical effectiveness, or medical-device reliability proof is NOT supported.
- Yield, throughput, cost, or lead-time claims are NOT supported.
