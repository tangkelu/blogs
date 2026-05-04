# Medical Device PCB Evidence Pack

**Pack ID**: `consumption-medical-device`
**Date**: 2026-05-03
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Medical Device PCB/PCBA — broad (patient monitoring, medical imaging, IVD/lab, therapeutic/surgical, wearable/home medical, medical power/isolation)"
scope: |
  Conservative evidence pack for broad medical-device PCB/PCBA content.

  Supports board-class vocabulary for 6 medical sub-families and the medical
  manufacturing-control layer: traceability (DHR/DMR/UDI), conformal coating,
  THT mixed-technology, low-void BGA, and MES documentation discipline.

  FDA 21 CFR 820/QMSR, ISO 13485, IEC 60601 vocabulary at boundary/
  documentation-identity level only.

  No FDA clearance/approval, ISO 13485 certification, IEC 60601 compliance,
  biocompatibility, or patient-safety outcome claims.

  For hearing-aid-specific content, use hearing-aid-evidence-pack.md instead.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Application boundary
  - "applications-medical-application-coverage-gap-map"

  # Medical manufacturing-control layer
  - "methods-pcba-medical-traceability-dhr-dmr-boundary"
  - "methods-medical-manufacturing-control-context-for-coating-tht-and-bga"
  - "methods-pcba-mes-traceability-and-medical-documentation-boundary"

  # Standards boundary
  - "standards-fda-medical-device-documentation-and-traceability-metadata"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"

source_ids:
  - "frontendapt-industry-medical-page-en"
  - "fda-21cfr-82065-traceability-page"
  - "fda-21cfr-820181-device-master-record-page"
  - "fda-21cfr-820184-device-history-record-page"
  - "fda-qmsr-page"
  - "fda-udi-basics-page"
  - "ipc-1782b-traceability-standard-page"

wiki_framing_support:
  - "wiki/applications/medical-device-pcb-pcba-boundary-map"
  - "wiki/applications/medical-standards-routing-boundary"
  - "wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate"

must_refresh:
  - claim: "FDA QMSR implementation status or 21 CFR 820 revision details"
    value: true
  - claim: "ISO 13485 revision or certification cycle status"
    value: true
  - claim: "IEC 60601-1 amendment or particular-standard revision"
    value: true
  - claim: "UDI system implementation requirements or device class status"
    value: true

excluded_claim_classes:
  - "IEC 60601-1 compliance, applied-parts classification (Type B/BF/CF), leakage current proof"
  - "ISO 13485 QMS certification, clause-level requirements, or supplier audit status"
  - "FDA 510(k), PMA, De Novo, or device clearance/approval proof"
  - "ISO 10993 biocompatibility, sterilization compatibility, or patient-contact suitability"
  - "Patient safety outcomes, clinical effectiveness, or device reliability proof"
  - "IEC 60601 specific particular-standard compliance (e.g., -2-x series)"
  - "Cost, lead-time, and yield claims"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `medical device PCB`, `medical PCB`, `medical PCBA`, `patient monitoring board`, `medical imaging PCB`, `IVD PCB` |
| **Page Type** | `query` |
| **Search Intent** | Medical electronics hardware, regulated device manufacturing, medical-grade PCB assembly |
| **Target Reader** | Medical device engineers, regulatory affairs professionals, medical hardware manufacturers |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` — medical manufacturing-control vocabulary and board-class context supported; device approval proof, compliance claims, and biocompatibility blocked.

> **Routing note**: For hearing-aid-specific content, use `wiki/consumption/hearing-aid-evidence-pack.md` instead. For slug-level process content (conformal coating, THT, MES, low-void BGA), route to `wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate.md`.

---

## 3. Sub-Family Coverage (Evidence Scope)

### 3.1 Patient Monitoring / Life-Support

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Patient monitoring, life-support electronics, vital-signs acquisition board context |
| Manufacturing-control vocabulary | Traceability (DHR/DMR/UDI), inspection discipline, documentation posture |
| IEC 60601-1 applied-parts classification, leakage current, clinical performance proof | ❌ Blocked |

### 3.2 Medical Imaging

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Imaging electronics, sensor/detector interface, image-processing board context |
| Process vocabulary | Low-void BGA, conformal coating planning for imaging boards |
| Imaging resolution, diagnostic accuracy, device clearance proof | ❌ Blocked |

### 3.3 IVD / Lab Equipment

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | IVD instrument, lab automation, analyzer board context |
| Manufacturing posture | Documentation discipline, traceability framing |
| Diagnostic accuracy, assay performance, IVD regulatory clearance | ❌ Blocked |

### 3.4 Therapeutic / Surgical Devices

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Therapeutic device, surgical system electronics board context |
| Manufacturing-control vocabulary | Cleaning/disinfection context (vocabulary only, no compliance) |
| Device safety classification, IEC 60601-1 particular-standard compliance, clinical efficacy | ❌ Blocked |

### 3.5 Wearable / Home Medical

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Medical wearable, home monitoring device board context |
| Compact board context | Mixed-signal, compact assembly vocabulary |
| Device clearance, wireless connectivity compliance, patient-contact suitability | ❌ Blocked |

### 3.6 Medical Power Supply / Isolation

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Medical power supply, isolation power board context |
| Design language | Creepage/clearance design language as vocabulary (not thresholds) |
| IEC 60601-1 compliance, safety class, leakage current proof | ❌ Blocked |

---

## 4. Medical Manufacturing-Control Layer (Main Safe Coverage)

The medical manufacturing-control layer is the strongest coverage area in this evidence pack:

| Control Layer | Evidence Support | Fact Card |
|---|---|---|
| **DMR / DHR framing** | Design Master Record / Device History Record vocabulary; manufacturing-record level only | `methods-pcba-medical-traceability-dhr-dmr-boundary` |
| **UDI context** | Unique Device Identifier vocabulary at documentation-context level | `standards-fda-medical-device-documentation-and-traceability-metadata` |
| **MES traceability** | Manufacturing Execution System traceability vocabulary for regulated programs | `methods-pcba-mes-traceability-and-medical-documentation-boundary` |
| **Conformal coating** | Coating planning and workflow for medical-adjacent boards | `methods-medical-manufacturing-control-context-for-coating-tht-and-bga` |
| **THT / BGA** | THT mixed-technology and low-void BGA review for medical-adjacent boards | `methods-medical-manufacturing-control-context-for-coating-tht-and-bga` |
| **FDA 21 CFR 820 / QMSR** | Documentation vocabulary: 820.65 traceability, 820.181 DMR, 820.184 DHR, QMSR alignment | `standards-fda-medical-device-documentation-and-traceability-metadata` |

---

## 5. Standards Context (Identity / Boundary Only)

| Standard | Safe Use | Blocked Use |
|---|---|---|
| **IEC 60601-1** | General medical electrical equipment standard identity; safety-standard context vocabulary | Applied-parts classification, leakage current, creepage/clearance compliance proof |
| **ISO 13485** | Medical device QMS standard identity; QMS vocabulary at boundary level | Clause-level requirements, certification validity, supplier audit status |
| **FDA 21 CFR 820 / QMSR** | Documentation framework identity: DMR, DHR, UDI, traceability vocabulary | 510(k), PMA, or device clearance/approval proof |
| **ISO 10993** | Biocompatibility standard identity only | Biocompatibility proof, sterilization suitability, patient-contact classification |
| **IPC-1782B** | Traceability standard identity for medical electronics documentation | Traceability certification or compliance proof |

---

## 6. Allowed vs Blocked

### 6.1 Allowed (Manufacturing Control and Board-Class Context)

| Claim Pattern | Example |
|---|---|
| Manufacturing-control vocabulary | "Medical device PCB/PCBA manufacturing references DHR/DMR documentation discipline and UDI traceability requirements" |
| Standards identity framing | "IEC 60601-1 defines safety requirements for medical electrical equipment — board design must consider the test environment and isolation expectations of the complete device" |
| Process-posture vocabulary | "Medical-adjacent assemblies benefit from conformal coating planning, low-void BGA process review, and MES-linked traceability from the earliest production stages" |
| Board-class context | "Medical imaging electronics and patient monitoring boards require tight documentation discipline and inspection gate adherence" |

### 6.2 Blocked (Approval / Compliance / Clinical Proof)

| Blocked Claim | Reason |
|---|---|
| "FDA cleared medical device PCB" | FDA clearance/approval is granted to the complete medical device, not the PCB |
| "ISO 13485 certified supplier" | ISO 13485 certification applies to the organization's QMS, checked via audit |
| "IEC 60601-1 Type BF compliant isolation" | Applied-parts classification requires complete device testing |
| "Biocompatible PCB per ISO 10993" | Biocompatibility evaluation requires material and device-level testing |
| "Clinically proven performance" | Clinical evidence is a device-level outcome, not a PCB manufacturing claim |

---

## 7. Handoff

**Core Answer**:

> Broad medical-device PCBs are supported through 6 sub-family board-class vocabularies and the medical manufacturing-control layer (DHR/DMR, UDI, MES traceability, conformal coating, low-void BGA). Standards (IEC 60601-1, ISO 13485, FDA 21 CFR 820) are available at identity and documentation-boundary level only. Device approval, compliance proof, biocompatibility, and clinical performance claims are blocked.

**Safe Reusable Shapes**:

- "Medical device manufacturing discipline starts at the PCB/PCBA level — documentation (DHR/DMR), traceability (UDI, MES), inspection gates, and process controls are the manufacturing vocabulary, not the regulatory approval."
- "IEC 60601-1, ISO 13485, and FDA 21 CFR 820 are the regulatory context frameworks — they describe what the device and organization must demonstrate; the PCB supplier's role is in manufacturing-discipline and documentation support."
- "The strongest medical PCB manufacturing story is in the process layer: how documentation is structured, how traceability is maintained, and how process controls are applied."

---

## 8. Pre-flight

- [x] Medical device wiki boundary page referenced
- [x] Application fact card referenced (`facts/applications/medical-application-coverage-gap-map.md`)
- [x] All 6 fact_ids from existing landed records — no new records required
- [x] All 7 source_ids from existing landed registry records
- [x] FDA/ISO/IEC vocabulary limited to boundary/documentation-identity level
- [x] ISO 10993 biocompatibility blocked — no source in registry
- [x] Routing notes to hearing-aid and process-level packs included
- [x] `must_refresh` items identified for QMSR status, ISO 13485 revision, IEC 60601 amendments

**Verdict**: ✅ `go_now_conservative` — medical manufacturing-control vocabulary and board-class context. Exclude all device approval, compliance proof, biocompatibility, and clinical performance claims.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
