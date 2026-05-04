---
topic_id: "applications-hearing-aid-pcb-review-boundaries"
title: "Hearing Aid PCB Review Boundaries"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
activated_at: "2026-05-03"
activation_notes: "P4-179 re-review and repair: Added Standards Context Table (5 standard/technology families: LE Audio, Auracast, Telecoil/IEC 60118-4, Bluetooth Core, FDA/ISO/IEC medical) and Cross-Lane Routing Table (6 routes). Retained strong Review Lanes (3 lanes), Safe Draft Routing, Common Overclaims (4 entries), Must Refresh (4 items), and 5 fact cards. Promoted to active for narrow hearing-assistance lane."
fact_ids:
  - "standards-hearing-aid-wireless-and-telecoil-identity-boundary"
  - "standards-interface-wireless-positioning-product-level-boundary"
  - "methods-medical-manufacturing-control-context-for-coating-tht-and-bga"
  - "methods-pcba-medical-traceability-dhr-dmr-boundary"
  - "standards-fda-medical-device-documentation-and-traceability-metadata"
source_ids:
  - "bluetooth-le-audio-page"
  - "bluetooth-le-audio-hearing-page"
  - "bluetooth-auracast-page"
  - "iec-60118-4-2014-a1-2017-csv-page"
  - "nidcd-hearing-aids-page"
  - "bluetooth-core-specification-page"
tags: ["hearing-aid", "le-audio", "auracast", "telecoil", "induction-loop", "medical", "wearable", "review-boundary"]
---

# Definition

> Hearing-aid PCB writing is only safe when it keeps two layers separate: exact hearing-assistance identity nouns such as `LE Audio`, `Auracast`, `telecoil`, and `induction loop systems`, and medical-adjacent manufacturing-control language such as traceability, documentation, inspection, coating, and compact mixed-signal assembly review. The current corpus does not support turning that combination into product qualification, regulatory proof, RF performance, antenna doctrine, or venue-readiness claims.

## Why This Topic Matters

- The `2026.4.29/en/hearing-aid-pcb.md` draft mixes compact RF/audio packaging, hearing-assistance nouns, telecoil language, medical-regulated vocabulary, and supplier-readiness claims in one article.
- Existing `llm_wiki` layers already support medical manufacturing-control boundaries and generic Bluetooth product-level boundary language, but they previously lacked a narrow exact-noun lane for `LE Audio`, `Auracast`, and `telecoil`.
- This page creates a prompt-consumable route so future rewrites can retain those exact hearing-assistance nouns without importing unsupported numerics, compliance claims, or supplier proof.

## Stable Facts

- Bluetooth SIG sources now support guarded identity-only use of `LE Audio` as the Bluetooth audio family and `Auracast` as the Bluetooth broadcast-audio capability within hearing-assistance context.
- IEC and NIDCD sources now support guarded identity-only use of `telecoil` and `induction loop systems` for hearing-aid purposes.
- Existing wireless-boundary support still applies: Bluetooth naming may be used for standards-owner and product-level context, not as proof that a PCB, module, or supplier is Bluetooth qualified.
- Existing medical-manufacturing-control boundaries still apply: traceability, documentation, coating, inspection, and mixed-technology language can be used as manufacturing-control posture, not as medical-device approval proof.

---

## Standards Context Table

| Standard/Technology | Safe Use | Blocked Claims |
|---|---|---|
| **Bluetooth LE Audio** | Bluetooth audio family identity; hearing-assistance context | Bluetooth qualification proof, universal phone compatibility, interoperability claims |
| **Auracast** | Bluetooth broadcast-audio capability identity | Public-venue support, deployed assistive-listening readiness, finished-device interoperability |
| **Telecoil / Induction Loop (IEC 60118-4, NIDCD)** | Hearing-aid signal-path nouns; magnetic coupling vocabulary | Field-strength thresholds, frequency-response, magnetic-shielding doctrine, IEC 60118-4 compliance proof |
| **Bluetooth Core Specification** | Bluetooth protocol family identity | RF performance, antenna doctrine, body-loss numerics, LC3/latency numerics, battery-life claims |
| **FDA / ISO 13485 / IEC 60601** | Medical device regulatory context vocabulary | FDA Class II, 510(k), MDR, ISO 13485 certification, IEC 60601 compliance, supplier qualification proof |

---

## Review Lanes

### 1. Hearing-Assistance Identity Layer

- Safe posture:
  use `LE Audio`, `Auracast`, `telecoil`, `induction loop systems`, and `hearing assistance` only as exact noun families with explicit owner or standards context.
- Safe companion layers:
  `standards-hearing-aid-wireless-and-telecoil-identity-boundary`,
  `standards-interface-wireless-positioning-product-level-boundary`.
- Do not drift into:
  interoperability, compatibility, qualification, deployment, or real-environment performance claims.

### 2. Medical Manufacturing-Control Layer

- Safe posture:
  describe compact assembly, documentation discipline, source traceability, inspection handoff, coating planning, and mixed-signal packaging pressure.
- Safe companion layers:
  `methods-medical-manufacturing-control-context-for-coating-tht-and-bga`,
  `methods-pcba-medical-traceability-dhr-dmr-boundary`,
  `standards-fda-medical-device-documentation-and-traceability-metadata`.
- Do not drift into:
  `FDA Class II`, `510(k)`, `MDR`, `ISO 13485`, `IEC 60601`, or supplier qualification claims.

### 3. Telecoil And Wireless Coexistence Boundary

- Safe posture:
  describe `telecoil` and `induction loop systems` as hearing-aid signal-path nouns, and describe Bluetooth hearing-assistance vocabulary separately.
- Do not drift into:
  telecoil field-strength or frequency-response thresholds, magnetic-shielding doctrine, antenna keepout rules, coexistence proof, or claims that one PCB architecture is standardized by these sources.

## Safe Draft Routing

### `hearing-aid-pcb.md`

- Status:
  `partial_support_for_hearing_assistance_identity_only`
- Safe angle:
  compact medical-adjacent mixed-signal board review with guarded `LE Audio`, `Auracast`, `telecoil`, and `induction loop systems` vocabulary plus documentation-aware manufacturing posture.
- Keep out:
  antenna-gain numerics, body-loss numerics, LC3 or latency numerics, battery-life claims, telecoil thresholds, biocompatibility claims, IP68 claims, regulatory approval claims, and supplier capability proof.

## Common Overclaims

- `LE Audio hearing-aid PCB` used as if it proves Bluetooth qualification or universal phone compatibility
- `Auracast-ready hearing aid` used as if it proves public-venue support or deployed assistive-listening readiness
- `telecoil PCB` used as if it proves exact coil geometry, orientation doctrine, or `IEC 60118-4` compliance
- `medical device PCB` used as if it proves `FDA`, `ISO 13485`, `IEC 60601`, or release authority

## Must Refresh Before Publishing

- Any exact RF, latency, codec, battery-life, or antenna-performance numeric
- Any telecoil field-strength, response, intelligibility, or immunity threshold
- Any `FDA`, `IEC 60601`, `ISO 13485`, `ISO 10993`, `510(k)`, `MDR`, or supplier certification claim
- Any statement about public `Auracast` rollout, induction-loop installation prevalence, or finished-device interoperability

## Cross-Lane Routing Table

| Content Type | Route To |
|---|---|
| Broader medical device context | `wiki/applications/medical-device-pcb-pcba-boundary-map.md` |
| Medical manufacturing control (coating/THT/BGA) | `facts/methods/medical-manufacturing-control-context-for-coating-tht-and-bga` |
| Medical traceability / DHR / DMR / UDI | `facts/methods/pcba-medical-traceability-dhr-dmr-boundary` |
| Wireless positioning / product-level Bluetooth | `facts/standards/interface-wireless-positioning-product-level-boundary` |
| Hearing aid wireless/telecoil identity | `facts/standards/hearing-aid-wireless-and-telecoil-identity-boundary` |
| General application routing | `wiki/applications/application-routing-and-boundary-map.md` |

---

## Related Fact Cards

- `standards-hearing-aid-wireless-and-telecoil-identity-boundary`
- `standards-interface-wireless-positioning-product-level-boundary`
- `methods-medical-manufacturing-control-context-for-coating-tht-and-bga`
- `methods-pcba-medical-traceability-dhr-dmr-boundary`
- `standards-fda-medical-device-documentation-and-traceability-metadata`

## Primary Sources

- https://www.bluetooth.com/learn-about-bluetooth/feature-enhancements/le-audio/
- https://www.bluetooth.com/learn-about-bluetooth/feature-enhancements/le-audio/hearing/
- https://www.bluetooth.com/auracast/
- https://webstore.iec.ch/en/publication/61949
- https://www.nidcd.nih.gov/health/hearing-aids
- https://www.bluetooth.com/specifications/specs/core-specification/
