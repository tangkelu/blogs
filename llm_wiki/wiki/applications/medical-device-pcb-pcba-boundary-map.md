---
topic_id: "applications-medical-device-pcb-pcba-boundary-map"
title: "Medical Device PCB PCBA Boundary Map"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
activated_at: "2026-05-03"
activation_notes: "P4-168 review pass: boundary language stable, all 6 board sub-families have safe/blocked pairs, standards context table complete with source-backed IEC 60601/FDA/IPC-1782 identity, must-refresh and routing table present. ISO 10993 correctly blocked (no official source in registry). Promoted to active."
fact_ids:
  - "applications-medical-application-coverage-gap-map"
  - "applications-application-coverage-gap-map"
  - "methods-pcba-medical-traceability-dhr-dmr-boundary"
  - "methods-medical-manufacturing-control-context-for-coating-tht-and-bga"
  - "methods-pcba-mes-traceability-and-medical-documentation-boundary"
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
tags: ["medical", "medical-device", "imaging", "wearable", "diagnostics", "therapeutic", "iec-60601", "iso-13485", "fda", "pcb", "pcba", "boundary-map", "application-boundary"]
---

# Definition

> Medical device PCB/PCBA writing is safe at board-class, manufacturing-control, and documentation-posture levels. It is unsafe when it crosses into IEC 60601-1 electrical safety compliance, ISO 13485 QMS certification, FDA device approval, ISO 10993 biocompatibility, or clinical/patient-safety outcomes. `IEC 60601-1` is present in the source registry at standard-identity level, but that does NOT unlock applied electrical safety, applied-parts, leakage current, hipot, or contact-voltage compliance claims.

## Why This Topic Matters

- Medical vocabulary (`IEC 60601`, `ISO 13485`, `FDA 510(k)`, `Class II`, `biocompatible`, `patient safety`) reads as compliance proof when it is only regulatory-context framing.
- A large body of manufacturing-control fact cards already exists for medical-adjacent content. This page prevents duplication and routes prompts to those cards rather than recreating them.
- Without this page, writers either over-claim by using the medical vocabulary loosely, or under-serve by ignoring the board-class vocabulary the Tier-2 source does support.

---

## Primary Routing Decision

**Before writing any medical PCB content, consult this routing table:**

| Content Type | Route To |
|---|---|
| Hearing aid (LE Audio, Auracast, telecoil) | `wiki/applications/hearing-aid-pcb-review-boundaries.md` |
| Medical imaging / wearable slug-level rewrite (conformal coating, THT, MES, low-void BGA) | `wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate.md` |
| MES / DMR / DHR / UDI traceability vocabulary | `facts/methods/pcba-medical-traceability-dhr-dmr-boundary.md` |
| Coating, THT, BGA in medical-adjacent context | `facts/methods/medical-manufacturing-control-context-for-coating-tht-and-bga.md` |
| ISO 13485 / FDA QMSR / IEC 60601 qualification boundary | `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md` |
| Broad medical application board-class routing (this page) | Continue reading below |

---

## Board Sub-Family Routing

### Patient Monitoring / Life-Support PCBs

**Safe angles:**
- Low-noise analog front-end vocabulary: ECG, SpO₂, NIBP, temperature, respiration sensor routing description
- Mixed-signal layout vocabulary: analog/digital separation, ground plane, power filtering on monitoring boards
- Redundancy and watchdog circuit description: alarm circuit, watchdog, backup power interface framing
- Communication and connectivity vocabulary: Ethernet, Wi-Fi, Bluetooth, proprietary RF module integration description (identity-level only)
- User interface board vocabulary: front panel, keypad, touchscreen, indicator, audio alarm PCB description
- Manufacturing-control context: documentation discipline, traceability, staged inspection framing

**Blocked:**
- IEC 60601-1 compliance, Type B/BF/CF applied-parts classification, leakage current values
- Life-support device safety-function proof, alarm performance, or clinical accuracy claims
- ISO 13485 certification or FDA device approval claims
- MTBF, field reliability, or patient-safety outcome proof

---

### Medical Imaging PCBs (Ultrasound, X-Ray, CT/MRI)

**Safe angles:**
- High-density analog front-end vocabulary: many-channel signal routing, grounding, crosstalk reduction description for ultrasound / detector front-ends
- High-speed digital processing board vocabulary: FPGA/DSP/CPU/GPU/memory multilayer PCB framing, high-speed interface routing description
- Interface and control module vocabulary: gantry control, detector control, motor/positioning control PCB description
- Mechanical and thermal integration description: mounting, shielding, cooling, enclosure integration framing
- Manufacturing-control context: first-build confirmation, X-ray inspection for BGA/LGA, documentation workflow

**Blocked:**
- Image quality, SNR, resolution, or diagnostic accuracy claims
- Radiation safety, X-ray dose, MRI compatibility, or electromagnetic-interference shielding compliance
- IEC 60601-1 / IEC 60601-2-x series compliance for specific imaging modalities
- FDA 510(k), PMA, or imaging-device clearance claims

---

### IVD / Lab Equipment PCBs

**Safe angles:**
- Sensor and measurement board vocabulary: optical, electrochemical, impedance measurement PCB with low-noise routing description
- Fluid control and motor driver board vocabulary: pump/valve/stepper/DC motor driver with feedback sensor integration description
- User interface and control electronics vocabulary: touchscreen, button, indicator, printer PCB integration description
- Lab automation and connectivity vocabulary: Ethernet, LIS connectivity interface description (identity-level only)
- Manufacturing-control context: traceability, staged inspection, documentation

**Blocked:**
- Measurement accuracy, linearity, repeatability, or calibration-interval claims
- IVD regulatory classification (EU IVDR, FDA 21 CFR 809) compliance claims
- Cross-contamination prevention, biosafety, or containment proof
- ISO 15189 lab accreditation claims

---

### Therapeutic / Surgical Device PCBs

**Safe angles:**
- Control and feedback loop vocabulary: sensor, actuator, control-board integration description for flow/pressure/energy delivery
- Power and driver circuit vocabulary: power conversion, motor/actuator drive, RF power stage, isolation/protection description
- User interface and safety logic vocabulary: panel, indicator, alarm, interlock PCB description
- Environmental and cleaning description: layout and assembly practices compatible with cleaning/disinfection context (description only — NOT compliance proof)
- Manufacturing-control context: documentation, traceability, staged inspection

**Blocked:**
- Sterilization compatibility (ETO, autoclave, radiation), biocompatibility, or patient-contact material claims
- IEC 60601-1 / IEC 60601-2-x applied-parts, leakage, or electrical safety compliance
- FDA 510(k), PMA, or therapeutic-device clearance claims
- Clinical dose accuracy, therapeutic efficacy, or patient-safety outcome proof
- RF/laser output power, safety interlocks, or IEC 60825 laser safety claims

---

### Wearable / Home Medical Device PCBs

**Safe angles:**
- Compact and low-power design vocabulary: small form-factor, rigid-flex, flex PCB description for body-worn or handheld devices
- Integrated sensing and wireless vocabulary: biosensor, motion/position sensor, Bluetooth/Wi-Fi/cellular module integration description (identity-level only)
- Battery management and charging vocabulary: battery charging, protection, power management circuit description
- User interface electronics vocabulary: display, LED, haptic, simple control PCB description

**Blocked:**
- Sensor accuracy, clinical-grade measurement, or clinical validation claims
- Bluetooth, Wi-Fi, or cellular qualification, FCC/CE/RED certification claims
- IP/waterproofing rating claims (IP67, IP68 — these are device-level, not PCB-level)
- Battery life, charge cycle, or power autonomy claims
- FDA OTC device clearance or ISO 11608 (drug delivery) claims

---

### Medical Power Supply / Isolation PCBs

**Safe angles:**
- Isolation and safety distance description: creepage/clearance, slot/cutout design vocabulary (description of design intent — NOT compliance values)
- Power conversion vocabulary: AC-DC, DC-DC PCB topology description (stable voltage/current framing)
- Thermal and mechanical integration vocabulary: heatsink, baseplate, chassis alignment description
- Signal and power separation vocabulary: separation framing for safety and reduced interference

**Blocked:**
- IEC 60601-1 / IEC 60950-1 / IEC 62368-1 leakage current, hipot, or electrical safety compliance values
- Exact creepage/clearance distances as compliance proof (only design-intent description)
- Medical power supply certification, approval, or listing claims
- MOOP / MOPP isolation level claims

---

## Standards Context

| Standard | Safe Use |
|---|---|
| `ISO 13485` | Medical device QMS vocabulary — NOT certification status or audit proof |
| `IEC 60601-1` | General medical electrical equipment safety standard identity — NOT compliance proof; official source exists in registry at metadata/identity level only |
| `FDA 21 CFR 820 (QMSR)` | Device manufacturer QMS regulatory context — NOT supplier registration or approval proof |
| `FDA 21 CFR 820.65 / 820.181 / 820.184` | Traceability, DMR, DHR vocabulary boundary — at manufacturing-record level only |
| `FDA UDI` | Device identification system identity — NOT board-level serialization completeness proof |
| `IPC-1782B` | PCB/PCBA traceability vocabulary — supported at IPC standard-identity level |
| `ISO 10993` | Biocompatibility standard identity — NOT compliance proof; **official source NOT in registry** |

---

## Manufacturing-Control Vocabulary Already Supported

The following vocabulary is already covered by existing fact cards — do NOT rewrite from scratch:

| Topic | Route To |
|---|---|
| MES / lot history / traveler / build records | `facts/methods/pcba-medical-traceability-dhr-dmr-boundary.md` |
| DMR / DHR / UDI adjacency vocabulary | `facts/methods/pcba-medical-traceability-dhr-dmr-boundary.md` |
| Conformal coating in medical context | `facts/methods/medical-manufacturing-control-context-for-coating-tht-and-bga.md` |
| THT in medical mixed-technology context | `facts/methods/medical-manufacturing-control-context-for-coating-tht-and-bga.md` + `facts/methods/tht-heavy-assemblies-power-and-medical-context.md` |
| Low-void BGA in medical context | `facts/methods/medical-manufacturing-control-context-for-coating-tht-and-bga.md` |
| Broad MES and documentation boundary | `facts/methods/pcba-mes-traceability-and-medical-documentation-boundary.md` |
| Qualification boundary (ISO 13485 / FDA / IEC 60601 context) | `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md` |

---

## Engineering Boundaries

- Treat all medical PCB content as board-class and manufacturing-control stories, not as device-safety or regulatory-compliance stories.
- IEC 60601-1 is in the source registry only at metadata/identity level; do not use it for applied-parts (B/BF/CF), leakage current, hipot, or electrical safety compliance vocabulary.
- ISO 13485 is at QMS boundary level only; do not use audit, clause-level, or certification-status language.
- Biocompatibility (ISO 10993) is blocked entirely; no patient-contact, body-contacting material, or sterilization-method claims.
- Wearable and home medical PCBs are particularly high risk for over-claiming clinical accuracy, wireless qualification, or FDA OTC classification.

---

## Common Misreadings

- `"Safe & Reliable"` trust-bar label in source → does NOT prove IEC 60601-1 compliance or clinical safety.
- `"Validation Package: FAI / PPAP / DHR"` in source → does NOT mean the PCB supplier owns DHR custody or device validation authority.
- `"ISO 13485"` mentioned in application context → does NOT prove the supplier is currently certified or that any specific program is qualified.
- `"Medical imaging PCB"` → does NOT prove diagnostic accuracy, imaging performance, or radiation-safety compliance.
- Conformal coating applied to medical PCB → does NOT prove biocompatibility, sterilization compatibility, or IP rating.
- Traceability vocabulary (DMR, DHR, UDI) → does NOT prove FDA registration, finished-device release authority, or audit readiness.

---

## Must Refresh Before Publishing

- Any IEC 60601-1 compliance, applied-parts, leakage, or hipot claim
- Any ISO 13485 certification status, audit, or clause-level claim
- Any FDA 510(k), PMA, De Novo, clearance, or registration claim
- Any ISO 10993 biocompatibility, patient-contact, or sterilization-method claim
- Any clinical accuracy, diagnostic performance, or patient-safety outcome claim
- Any exact DHR retention period, serialization schema, or release-authority claim
- Any wireless qualification, FCC/CE/RED certification, or radio performance claim

---

## Related Pages

- `facts/applications/medical-application-coverage-gap-map.md`
- `wiki/applications/application-routing-and-boundary-map.md`
- `wiki/applications/hearing-aid-pcb-review-boundaries.md` (hearing-aid narrow lane)
- `wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate.md` (slug-level process rewrite gate)
- `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md`

## Primary Sources

- /code/hileap/frontendAPT/public/static/industries/en/medical-pcb.json
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.65
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.181
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.184
- https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-system-qs-regulationmedical-device-current-good-manufacturing-practices-cgmp
- https://www.fda.gov/medical-devices/unique-device-identification-system-udi-system/udi-basics
