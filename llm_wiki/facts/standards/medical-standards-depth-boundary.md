---
fact_id: "standards-medical-standards-depth-boundary"
title: "Medical device standards (ISO 13485, IEC 60601-1, ISO 10993, FDA 510(k), PMA, UDI) are device-level regulatory boundaries, not PCB qualification or biocompatibility proof"
topic: "Medical device standards identity and PCB boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "iso-13485-2016-page"
  - "iec-60601-1-medical-electrical-equipment-page"
  - "iso-10993-biological-evaluation-page"
  - "fda-510k-premarket-notification-page"
  - "fda-pma-premarket-approval-page"
  - "fda-udi-basics-page"
  - "fda-qmsr-page"
notes: "All standards use publicly known identity metadata from official ISO/FDA source pages. ISO 13485 is device QMS; IEC 60601-1 is medical electrical equipment safety; ISO 10993 is biocompatibility evaluation; FDA 510(k)/PMA are device clearance/approval pathways; UDI is device identification. None qualify bare PCBs."
tags: ["medical", "medical-device", "iso-13485", "iec-60601", "iso-10993", "fda", "510k", "pma", "udi", "biocompatibility", "regulatory-boundary"]
---

# Canonical Summary

> Medical device standards operate at device-level regulatory boundaries — none create PCB-level qualification, biocompatibility certification, or FDA approval status. ISO 13485 is a medical device QMS standard for organizations; IEC 60601-1 is medical electrical equipment safety and essential performance; ISO 10993 is biological evaluation and biocompatibility; FDA 510(k) is device clearance; PMA is Class III device approval; UDI is device identification and traceability. Mentioning these in PCB/PCBA content is safe only at document-identity and regulatory-context level. All QMS certification, electrical safety compliance, biocompatibility proof, device clearance/approval, and patient-contact suitability claims are blocked.

## Medical Device Standard Families

### ISO 13485 — Medical Device Quality Management System

**Governance Layer:** Organization-level QMS for medical device manufacturers

**PCB Boundary:**
- Safe: Medical device QMS vocabulary, supplier quality expectations, standard-family identity
- Blocked: QMS certification status, certificate scope/validity, supplier audit approval, PCB "medical-grade" claims

**PCB Stop Line:** ISO 13485 certifies organization QMS for medical device manufacturing. It does NOT certify PCBs, PCBAs, materials, or bare board suppliers. Do not claim "ISO 13485 certified PCB", "medical-grade board", or "QMS-approved supplier" from standard identity alone.

---

### IEC 60601-1 — Medical Electrical Equipment Safety

**Governance Layer:** Medical electrical equipment basic safety and essential performance

**PCB Boundary:**
- Safe: Medical electrical equipment safety vocabulary, standard-family identity, equipment-level context
- Blocked: Applied-parts classification (Type B/BF/CF), leakage current values, creepage/clearance compliance, electrical safety proof at PCB level

**PCB Stop Line:** IEC 60601-1 is a finished medical electrical equipment standard. It does NOT certify bare PCBs or PCBAs for patient safety, applied parts, or electrical isolation. Do not claim "IEC 60601-1 compliant PCB", "Type BF board", or "patient-safe PCBA."

---

### ISO 10993 — Biological Evaluation / Biocompatibility

**Governance Layer:** Biological evaluation and biocompatibility testing for medical devices

**PCB Boundary:**
- Safe: Biocompatibility standard-family identity, biological evaluation vocabulary context
- Blocked: Material biocompatibility proof, patient-contact suitability, sterilization compatibility, "biocompatible PCB" claims

**PCB Stop Line:** ISO 10993 evaluates finished medical devices for biological safety. It does NOT qualify bare PCB materials, laminates, finishes, or PCBAs for patient contact. Do not claim "ISO 10993 compliant", "biocompatible board", or "patient-contact safe" from standard identity.

---

### FDA 510(k) — Premarket Notification (Device Clearance)

**Governance Layer:** FDA clearance pathway for medical devices (substantial equivalence)

**PCB Boundary:**
- Safe: FDA 510(k) program identity, device clearance vocabulary, regulatory pathway context
- Blocked: Device clearance proof, "510(k) approved PCB", supplier clearance status, PCB "FDA cleared" claims

**PCB Stop Line:** 510(k) is device-level FDA clearance (not approval). It does NOT extend to PCBs, PCBAs, materials, or suppliers. Do not claim "510(k) approved board", "FDA cleared PCB", or "510(k) compliant manufacturing."

---

### FDA PMA — Premarket Approval (Class III Devices)

**Governance Layer:** FDA approval for Class III high-risk medical devices

**PCB Boundary:**
- Safe: PMA program identity, Class III device approval vocabulary, regulatory pathway context
- Blocked: Device approval proof, "PMA-approved PCB", supplier approval status, PCB "FDA approved" claims

**PCB Stop Line:** PMA is Class III device-level FDA approval. It does NOT extend to PCBs, PCBAs, or suppliers. Do not claim "PMA approved board", "FDA approved PCB", or "Class III certified manufacturing."

---

### FDA UDI — Unique Device Identification

**Governance Layer:** Medical device identification and traceability system

**PCB Boundary:**
- Safe: UDI system identity, device identification vocabulary, traceability context (at description level)
- Blocked: Complete PCB lot genealogy, bare-board serialization proof, supplier traceability system compliance

**PCB Stop Line:** UDI is a finished-device identification system (DI + PI). It supports traceability vocabulary at manufacturing-record level. Do not equate UDI with bare PCB serialization, lot genealogy, or supplier traceability compliance.

---

## Cross-Standard Safe Vocabulary

The following angles are safe across all medical device standards:

| Vocabulary Type | Safe Usage |
|---|---|
| Standard names | ISO 13485, IEC 60601-1, ISO 10993, FDA 510(k), PMA, UDI as document/program identifiers |
| Document families | "IEC 60601 series", "ISO 10993 biological evaluation", "FDA QMSR" |
| Scope framing | "medical device QMS context", "equipment safety vocabulary", "biocompatibility evaluation framework" |
| Regulatory context | "FDA regulatory pathway", "device clearance/approval process", "UDI traceability system" |
| Manufacturing posture | "medical-adjacent manufacturing control", "documentation discipline", "traceability posture" |

## Common Misreadings to Block

| Misreading | Why It's Blocked |
|---|---|
| "ISO 13485 certified PCB" | ISO 13485 is organization QMS, not product certification |
| "Medical-grade board" or "medical-certified PCBA" | No such PCB-level medical certification exists |
| "IEC 60601-1 compliant PCB" | IEC 60601-1 is finished equipment, not bare PCB |
| "Type BF/CF board" or "patient-safe PCBA" | Applied parts classification is device-level, not PCB-level |
| "ISO 10993 biocompatible PCB" | ISO 10993 evaluates devices, not bare PCB materials |
| "FDA 510(k) approved board" | 510(k) is device clearance, not PCB approval |
| "FDA cleared PCB manufacturer" | FDA does not clear PCB manufacturers or bare boards |
| "PMA-approved PCB supplier" | PMA is Class III device approval, not supplier certification |
| "UDI-compliant bare board" | UDI is finished-device ID, not bare PCB requirement |
| "Patient-contact safe PCB material" | Material suitability requires device-level biocompatibility testing |

## Related Fact Cards

- `facts/applications/medical-application-coverage-gap-map.md` — Application coverage for 6 medical board sub-families
- `wiki/applications/medical-device-pcb-pcba-boundary-map.md` — Active routing boundary for medical device PCB content
- `facts/methods/pcba-medical-traceability-dhr-dmr-boundary.md` — MES/DMR/DHR/UDI traceability boundary
- `facts/standards/fda-medical-device-documentation-and-traceability-metadata.md` — FDA 21 CFR 820 documentation metadata
- `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md` — Cross-application qualification boundaries

## Source Links

- https://www.iso.org/standard/59752.html (ISO 13485)
- https://webstore.iec.ch/en/publication/2612 (IEC 60601-1)
- https://www.iso.org/standard/55890.html (ISO 10993)
- https://www.fda.gov/medical-devices/premarket-notifications-510k (FDA 510(k))
- https://www.fda.gov/medical-devices/premarket-approval-pma (FDA PMA)
- https://www.fda.gov/medical-devices/unique-device-identification-system-udi-system/udi-basics (FDA UDI)
