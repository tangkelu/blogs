---
topic_id: "applications-medical-standards-routing-boundary"
title: "Medical Device Standards Routing Boundary"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
activated_at: "2026-05-03"
activation_notes: "P4-172 landing: medical standards-depth pack created with PCB-stop lines for ISO 13485, IEC 60601-1, ISO 10993, FDA 510(k), PMA, UDI. Promoted to active."
fact_ids:
  - "standards-medical-standards-depth-boundary"
  - "applications-medical-application-coverage-gap-map"
  - "standards-fda-medical-device-documentation-and-traceability-metadata"
source_ids:
  - "iso-13485-2016-page"
  - "iec-60601-1-medical-electrical-equipment-page"
  - "iso-10993-biological-evaluation-page"
  - "fda-510k-premarket-notification-page"
  - "fda-pma-premarket-approval-page"
  - "fda-udi-basics-page"
  - "fda-qmsr-page"
notes: "All standards use publicly known identity metadata from official ISO/FDA source pages. No clause-level text, test thresholds, or compliance proof."
tags: ["medical", "medical-device", "iso-13485", "iec-60601", "iso-10993", "fda", "510k", "pma", "udi", "biocompatibility", "regulatory-boundary", "routing"]
---

# Definition

> Medical device PCB/PCBA writing can reference ISO 13485, IEC 60601-1, ISO 10993, FDA 510(k), PMA, and UDI only at document-identity and regulatory-context level. It is unsafe to claim QMS certification, electrical safety compliance, biocompatibility proof, FDA device clearance/approval, or patient-contact suitability from these sources alone. Use this page to route which medical device standard vocabulary is supportable and where to stop.

## Why This Topic Matters

- Medical device drafts frequently drift from manufacturing-control vocabulary into regulatory compliance claims: ISO 13485 QMS certification, IEC 60601-1 electrical safety, ISO 10993 biocompatibility, FDA 510(k)/PMA approval, or UDI traceability compliance.
- The official ISO/FDA sources support standard/program identity but not PCB-level qualification, certification, or approval.
- Without explicit PCB-stop lines, writers overclaim "certified", "compliant", "approved", or "safe" for boards, PCBAs, materials, or suppliers.

---

## Standards Context Table

| Standard/Program | Safe Use | Blocked Claims |
|---|---|---|
| **ISO 13485** | Medical device QMS vocabulary; organization-level framing | QMS certification status, certificate scope, "medical-grade PCB" |
| **IEC 60601-1** | Medical electrical equipment safety vocabulary; equipment-level context | Applied-parts classification (Type B/BF/CF), leakage current, "patient-safe PCBA" |
| **ISO 10993** | Biocompatibility standard-family identity; evaluation framework | "Biocompatible PCB", patient-contact suitability, material safety proof |
| **FDA 510(k)** | Device clearance program identity; regulatory pathway context | "510(k) approved PCB", device clearance proof, supplier clearance |
| **FDA PMA** | Class III device approval program identity; regulatory pathway | "PMA-approved board", device approval proof, supplier approval |
| **FDA UDI** | Device identification system identity; traceability vocabulary | "UDI-compliant bare board", complete lot genealogy, serialization proof |

---

## PCB Stop Lines by Standard

### ISO 13485 Stop Line

**Safe angles:**
- "ISO 13485 provides medical device QMS context"
- "Medical device manufacturer quality expectations"

**Blocked:**
- "ISO 13485 certified PCB" or "certified PCBA"
- "Medical-grade board" or "medical-certified supplier"
- QMS certificate status, scope, or validity claims

> **Stop:** ISO 13485 certifies organization QMS for medical device manufacturing. It does NOT certify PCBs, PCBAs, or bare board suppliers. Keep ISO 13485 at QMS-context level only.

---

### IEC 60601-1 Stop Line

**Safe angles:**
- "IEC 60601-1 medical electrical equipment safety standard"
- "Equipment-level safety and essential performance context"

**Blocked:**
- "IEC 60601-1 compliant PCB" or "compliant PCBA"
- Type B/BF/CF applied-parts classification at PCB level
- Leakage current, creepage/clearance compliance, hipot claims
- "Patient-safe board" or "applied-parts ready PCBA"

> **Stop:** IEC 60601-1 is a finished medical electrical equipment standard. It does NOT certify bare PCBs for patient safety or applied parts. Keep IEC 60601-1 at equipment-safety context only.

---

### ISO 10993 Stop Line

**Safe angles:**
- "ISO 10993 biological evaluation standard family"
- "Biocompatibility testing framework context"

**Blocked:**
- "ISO 10993 biocompatible PCB" or "biocompatible board"
- Patient-contact suitability claims for PCB materials
- Sterilization compatibility claims at bare PCB level
- Material safety or toxicity proof without device-level testing

> **Stop:** ISO 10993 evaluates finished medical devices for biological safety. It does NOT qualify bare PCB materials for patient contact. Keep ISO 10993 at biocompatibility-vocabulary level only.

---

### FDA 510(k) Stop Line

**Safe angles:**
- "FDA 510(k) premarket notification program"
- "Medical device clearance pathway vocabulary"

**Blocked:**
- "510(k) approved PCB" or "FDA cleared board"
- "510(k) compliant PCBA" or "510(k) certified manufacturing"
- Device clearance proof or substantial equivalence claims at PCB level

> **Stop:** 510(k) is device-level FDA clearance (not PCB approval). It does NOT extend to PCBs, PCBAs, or suppliers. Keep 510(k) at regulatory-pathway vocabulary only.

---

### FDA PMA Stop Line

**Safe angles:**
- "FDA PMA premarket approval program"
- "Class III high-risk device approval pathway"

**Blocked:**
- "PMA-approved PCB" or "FDA approved board"
- "PMA-compliant PCBA" or "Class III certified manufacturing"
- Device approval proof or safety/effectiveness claims at PCB level

> **Stop:** PMA is Class III device-level FDA approval. It does NOT extend to PCBs, PCBAs, or suppliers. Keep PMA at regulatory-pathway vocabulary only.

---

### FDA UDI Stop Line

**Safe angles:**
- "FDA UDI unique device identification system"
- "Device identification and traceability vocabulary"
- "Manufacturing-record level traceability context"

**Blocked:**
- "UDI-compliant bare board" or "UDI-certified PCB"
- Complete PCB lot genealogy claims
- Bare-board serialization or supplier traceability compliance

> **Stop:** UDI is a finished-device identification system (Device Identifier + Production Identifier). It supports traceability vocabulary but does NOT equate to bare PCB serialization or lot genealogy. Keep UDI at device-traceability context only.

---

## Routing Table: Where Standards Vocabulary Is Safe

| Content Type | Route To |
|---|---|
| ISO 13485 QMS context | Keep at organization-level; do not claim PCB certification |
| IEC 60601-1 safety context | Keep at finished-equipment level; do not claim PCB compliance |
| ISO 10993 biocompatibility | Keep at device-evaluation level; do not claim material suitability |
| FDA 510(k) clearance context | Keep at device-level; do not claim PCB approval |
| FDA PMA approval context | Keep at Class III device-level; do not claim PCB approval |
| FDA UDI traceability | Keep at device-identification level; do not claim bare-board serialization |
| Medical board sub-family routing | `wiki/applications/medical-device-pcb-pcba-boundary-map.md` |
| MES/DMR/DHR/UDI traceability | `facts/methods/pcba-medical-traceability-dhr-dmr-boundary.md` |
| Medical manufacturing control | `facts/methods/medical-manufacturing-control-context-for-coating-tht-and-bga.md` |
| Hearing aid (LE Audio/Auracast) | `wiki/applications/hearing-aid-pcb-review-boundaries.md` |
| Imaging/wearable slug process | `wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate.md` |

---

## Common Misreadings

| Misreading | Correction |
|---|---|
| "ISO 13485 certified PCB" → | ISO 13485 is org QMS. Safe: "medical device manufacturing context." |
| "Medical-grade board" → | No PCB-level medical grade exists. Safe: "board for medical device applications." |
| "IEC 60601-1 compliant PCBA" → | Equipment standard ≠ PCB compliance. Safe: "medical electrical equipment context." |
| "Type BF patient-safe board" → | Applied parts are device-level. Safe: "board for patient-monitoring applications." |
| "ISO 10993 biocompatible PCB" → | Device evaluation ≠ material proof. Safe: "biocompatibility vocabulary context." |
| "510(k) approved PCB manufacturer" → | 510(k) is device clearance. Safe: "medical device regulatory context." |
| "FDA cleared bare board" → | FDA does not clear bare PCBs. Safe: "medical device component context." |
| "PMA-approved PCB supplier" → | PMA is Class III device approval. Safe: "high-risk medical device context." |
| "UDI-compliant serialization" → | UDI is device ID, not bare PCB req. Safe: "traceability and identification context." |

---

## Must Refresh Before Publishing

- Any ISO 13485 QMS certification or scope claim
- Any IEC 60601-1 compliance, applied-parts, or electrical safety claim
- Any ISO 10993 biocompatibility or patient-contact suitability claim
- Any FDA 510(k) clearance or "approved" claim
- Any FDA PMA approval or "Class III certified" claim
- Any UDI compliance, serialization, or traceability system claim
- Any patient-safety outcome, clinical effectiveness, or reliability claim

---

## Cross-Lane Routing

| Content Type | Route To |
|---|---|
| Medical device board families (6 sub-families) | `wiki/applications/medical-device-pcb-pcba-boundary-map.md` |
| Hearing aid specific (LE Audio/Auracast) | `wiki/applications/hearing-aid-pcb-review-boundaries.md` |
| Medical imaging/wearable process | `wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate.md` |
| MES/DMR/DHR/UDI traceability | `facts/methods/pcba-medical-traceability-dhr-dmr-boundary.md` |
| Coating/THT/BGA in medical context | `facts/methods/medical-manufacturing-control-context-for-coating-tht-and-bga.md` |
| FDA 21 CFR 820 documentation | `facts/standards/fda-medical-device-documentation-and-traceability-metadata.md` |
| General qualification boundary | `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md` |
| Medical coverage gaps | `facts/applications/medical-application-coverage-gap-map.md` |

---

## Related Pages

- `facts/standards/medical-standards-depth-boundary.md` — Fact card with PCB stop lines
- `wiki/applications/medical-device-pcb-pcba-boundary-map.md` — Active application boundary for 6 board sub-families
- `facts/applications/medical-application-coverage-gap-map.md` — Coverage map with residual gaps
