# Hearing Aid PCB Evidence Pack

**Pack ID**: `consumption-hearing-aid`
**Date**: 2026-05-03
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Hearing Aid PCB/PCBA (compact medical-adjacent mixed-signal board with wireless audio)"
scope: |
  Conservative evidence pack for hearing-aid PCB/PCBA content.
  Narrow medical sub-lane.

  Supports board-class vocabulary for compact mixed-signal hearing-aid boards:
  LE Audio / Auracast / telecoil / induction-loop identity vocabulary, medical
  manufacturing-control posture (traceability, coating, inspection), and compact
  assembly review language.

  No Bluetooth qualification, FDA/ISO 13485/IEC 60601 approval proof,
  interoperability proof, RF performance, or audio quality numerics.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Application boundary
  - "applications-hearing-aid-coverage-gap-map"

  # Wireless / telecoil identity
  - "standards-hearing-aid-wireless-and-telecoil-identity-boundary"
  - "standards-interface-wireless-positioning-product-level-boundary"

  # Medical manufacturing control
  - "methods-medical-manufacturing-control-context-for-coating-tht-and-bga"
  - "methods-pcba-medical-traceability-dhr-dmr-boundary"

  # FDA documentation context
  - "standards-fda-medical-device-documentation-and-traceability-metadata"

source_ids:
  - "bluetooth-le-audio-page"
  - "bluetooth-le-audio-hearing-page"
  - "bluetooth-auracast-page"
  - "iec-60118-4-2014-a1-2017-csv-page"
  - "nidcd-hearing-aids-page"
  - "bluetooth-core-specification-page"

wiki_framing_support:
  - "wiki/applications/hearing-aid-pcb-review-boundaries"

must_refresh:
  - claim: "Bluetooth LE Audio version or feature revision statements"
    value: true
  - claim: "Auracast ecosystem deployment status or venue support"
    value: true
  - claim: "FDA hearing device regulatory class or guidance revision"
    value: true

excluded_claim_classes:
  - "Bluetooth qualification, certification, or universal phone compatibility proof"
  - "Public-venue Auracast support, induction-loop deployment prevalence"
  - "Telecoil field-strength, IEC 60118-4 compliance, or coil geometry doctrine"
  - "FDA Class II, 510(k) clearance, MDR, or CE medical device approval proof"
  - "ISO 13485 certification or IEC 60601 compliance proof"
  - "RF performance, antenna doctrine, LC3 latency, battery-life, audio quality numerics"
  - "Cost, lead-time, and yield claims"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `hearing aid PCB`, `hearing device board`, `LE Audio PCB`, `Auracast board`, `telecoil PCB` |
| **Page Type** | `query` |
| **Search Intent** | Compact medical-adjacent audio device hardware, wireless hearing assistance, hearing device manufacturing |
| **Target Reader** | Hearing device engineers, medical wearable designers, compact audio hardware integrators |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` — identity vocabulary and medical manufacturing-control posture supported; Bluetooth qualification, medical device approval, and RF/audio performance claims blocked.

> **Note**: This is a narrow sub-lane. For broader medical device manufacturing context, the `medical-device-evidence-pack.md` (P4-198) should be used as the primary routing entry.

---

## 3. Review Lanes (Evidence Scope)

### 3.1 Hearing-Assistance Identity Layer

| Technology | Safe Vocabulary | Blocked Vocabulary |
|---|---|---|
| **Bluetooth LE Audio** | Bluetooth audio family identity; hearing-assistance context; "LE Audio is Bluetooth SIG's modern audio framework targeting hearing aids and wireless audio" | Device qualification, ecosystem interoperability, universal phone compatibility proof |
| **Auracast** | Bluetooth broadcast-audio capability identity; assistive-listening context naming | Public-venue Auracast installed base, deployed assistive-listening readiness claims |
| **Telecoil** | Hearing-aid signal-path noun; magnetic coupling vocabulary; IEC/NIDCD identity-level framing | Field-strength thresholds, coil geometry doctrine, IEC 60118-4 compliance proof |
| **Induction Loop** | Hearing loop system identity as counterpart to telecoil; assistive listening context | Loop installation prevalence, field uniformity, system-level performance claims |

### 3.2 Medical Manufacturing-Control Layer

| Aspect | Evidence Support |
|--------|-----------------|
| Compact assembly documentation discipline | Supported at medical manufacturing-control vocabulary level |
| Source traceability (DHR/DMR framing) | Supported at medical traceability boundary vocabulary level |
| Inspection handoff posture | Supported at manufacturing-control posture level |
| Conformal coating planning for medical-adjacent boards | Supported at coating-process vocabulary level |
| Mixed-signal packaging pressure vocabulary | Supported at design-consideration level |
| FDA Class II, 510(k), ISO 13485 certification, IEC 60601 compliance proof | ❌ Blocked |

### 3.3 Telecoil and Wireless Coexistence Boundary

| Aspect | Evidence Support |
|--------|-----------------|
| Telecoil as a hearing-aid signal-path noun | Supported — distinct from Bluetooth hearing-assistance vocabulary |
| Induction loop systems as counterpart to telecoil | Supported at identity-level |
| Wireless coexistence framing (LE Audio + telecoil on same board) | Supported at architecture-consideration vocabulary |
| Magnetic field uniformity, IEC 60118-4 coil specifications, RF interference proof | ❌ Blocked |

---

## 4. Standards Context (Identity Only)

| Standard / Technology | Safe Use | Blocked Use |
|---|---|---|
| **Bluetooth LE Audio** | Audio family identity; hearing device context vocabulary | Device qualification, interoperability certification, LC3 codec performance |
| **Auracast** | Broadcast-audio capability identity; assistive-listening context | Venue deployment count, ecosystem readiness, device support breadth |
| **IEC 60118-4** | Telecoil standard-family identity (hearing aid inductance measurement) | Compliance proof, field-strength thresholds, coil geometry requirements |
| **NIDCD guidance** | Hearing aid technology context vocabulary from US health authority | Clinical efficacy, audiological outcome claims |
| **Bluetooth Core Specification** | Protocol family identity | RF performance, antenna doctrine, latency numerics |
| **FDA / ISO 13485 / IEC 60601** | Medical device regulatory context vocabulary only | FDA clearance/approval, ISO 13485 certification, IEC 60601 compliance proof |

---

## 5. Allowed vs Blocked

### 5.1 Allowed (Board-Class and Identity Context)

| Claim Pattern | Example |
|---|---|
| Technology identity framing | "Hearing aid boards increasingly integrate Bluetooth LE Audio for modern wireless hearing-assistance connectivity" |
| Telecoil identity vocabulary | "Telecoil (T-coil) remains a hearing-aid signal-path feature for magnetic induction loop compatibility" |
| Medical manufacturing posture | "Hearing-aid PCBs benefit from medical manufacturing-control discipline: documentation, traceability (DHR/DMR), and inspection handoffs" |
| Compact board context | "Hearing aid boards combine analog front-end, DSP, wireless, and power management in extremely compact form factors" |
| Coexistence framing | "Boards supporting both telecoil and Bluetooth LE Audio must coordinate magnetic and RF signal paths" |

### 5.2 Blocked (Qualification / Performance / Approval)

| Blocked Claim | Reason |
|---|---|
| "Works with all iPhone and Android devices" | Bluetooth interoperability proof — not supported at wiki level |
| "Auracast compatible in [N] public venues" | Deployment count — not available in current source layer |
| "IEC 60118-4 telecoil compliant board" | IEC compliance belongs to the complete hearing device |
| "FDA cleared hearing aid PCB" | FDA clearance is granted to the complete device, not the PCB |
| "Battery life: 20 hours continuous streaming" | Audio performance numeric — not a PCB manufacturing claim |

---

## 6. Handoff

**Core Answer**:

> Hearing-aid PCBs are a narrow medical sub-lane supported through identity vocabulary for LE Audio, Auracast, telecoil, and induction-loop systems, combined with medical manufacturing-control posture (traceability, coating, compact assembly). The current evidence supports technology naming and manufacturing-discipline vocabulary. It does not support Bluetooth qualification, FDA/ISO approval proof, RF performance, or audio quality claims.

**Safe Reusable Shapes**:

- "Hearing-aid boards occupy a compact medical-adjacent space where Bluetooth LE Audio and telecoil represent distinct wireless hearing-assistance paths — LE Audio uses RF; telecoil uses magnetic induction."
- "Medical manufacturing control discipline (DHR/DMR traceability, documentation, inspection) applies even when the final device is medical-adjacent rather than formally FDA-regulated."
- "Auracast and telecoil are safer named as board-context nouns than as deployment-readiness proof."

---

## 7. Pre-flight

- [x] Hearing-aid wiki boundary page referenced (`wiki/applications/hearing-aid-pcb-review-boundaries.md`)
- [x] Application fact card referenced (`facts/applications/hearing-aid-coverage-gap-map.md`)
- [x] All 6 fact_ids from existing landed records — no new records required
- [x] All 6 source_ids from existing landed registry records
- [x] Bluetooth qualification and FDA approval blocked claims explicitly documented
- [x] Telecoil vocabulary limited to hearing-aid signal-path noun level
- [x] `must_refresh` items identified for LE Audio revision, Auracast status, FDA guidance
- [x] Narrow sub-lane note included — routes to medical-device pack for broader context

**Verdict**: ✅ `go_now_conservative` — identity vocabulary and medical manufacturing-control posture. Exclude all Bluetooth qualification, medical device approval, RF performance, and audio quality claims.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
