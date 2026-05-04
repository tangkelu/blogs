---
fact_id: "applications-hearing-aid-coverage-gap-map"
title: "Hearing Aid application coverage gap map: which board families have wiki-level routing and which remain overview-only"
topic: "Hearing aid PCB/PCBA application coverage"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-186 initial build; sourced from wiki/applications/hearing-aid-pcb-review-boundaries.md (active as of P4-179), related hearing-aid, wireless, and medical boundary cards"
source_ids:
  - "bluetooth-le-audio-page"
  - "bluetooth-le-audio-hearing-page"
  - "bluetooth-auracast-page"
  - "iec-60118-4-2014-a1-2017-csv-page"
  - "nidcd-hearing-aids-page"
  - "bluetooth-core-specification-page"
tags: ["hearing-aid", "le-audio", "auracast", "telecoil", "induction-loop", "medical-adjacent", "wearable", "coverage-map", "gap-map"]
---

# Canonical Summary

> As of 2026-05-03 after P4-186 initial build, the hearing-aid application family has a dedicated wiki boundary page (`wiki/applications/hearing-aid-pcb-review-boundaries.md`) and that page is now `active`. This is a narrow medical sub-lane; this fact card maps what the current source layer supports, which board families are addressable, and which qualification/performance layers remain blocked.

## Board Family Coverage State

### Supported at Scenario + Board-Class Level

The hearing-aid lane is a narrow medical sub-lane with a small source footprint. It is supported by official Bluetooth SIG pages, IEC/NIDCD hearing standards identity pages, and the broader medical manufacturing-control fact layer. It does NOT prove qualification, interoperability, RF performance, or medical device approval.

| Board Family | Application Context | PCB/PCBA Vocabulary Supported |
|---|---|---|
| **Hearing Aid PCB** | Compact medical-adjacent mixed-signal board with wireless audio context | Guarded LE Audio / Auracast / telecoil / induction loop identity vocabulary; documentation-aware manufacturing posture; compact mixed-signal board review language |

### Review Lanes Supported

| Review Lane | Safe Vocabulary |
|---|---|
| Hearing-Assistance Identity Layer | LE Audio, Auracast, telecoil, induction loop systems — as exact noun families with explicit owner/standards context only |
| Medical Manufacturing-Control Layer | Compact assembly, documentation discipline, source traceability, inspection handoff, coating planning, mixed-signal packaging pressure |
| Telecoil And Wireless Coexistence Boundary | Telecoil and induction loop systems as hearing-aid signal-path nouns; Bluetooth hearing-assistance vocabulary separately |

### Fact Cards Supported

| Fact Card | What It Supports |
|---|---|
| `standards-hearing-aid-wireless-and-telecoil-identity-boundary` | LE Audio, Auracast, telecoil, induction loop identity boundary |
| `standards-interface-wireless-positioning-product-level-boundary` | Bluetooth product-level positioning boundary |
| `methods-medical-manufacturing-control-context-for-coating-tht-and-bga` | Medical manufacturing control for coating, THT, BGA |
| `methods-pcba-medical-traceability-dhr-dmr-boundary` | Medical traceability, DHR, DMR boundary |
| `standards-fda-medical-device-documentation-and-traceability-metadata` | FDA medical device documentation and traceability vocabulary |

### Standards Context Supported (Public Sources)

| Standard/Technology | What It Supports |
|---|---|
| `Bluetooth LE Audio` | Bluetooth audio family identity; hearing-assistance context vocabulary; NOT qualification or universal phone compatibility |
| `Auracast` | Bluetooth broadcast-audio capability identity; NOT public-venue support, deployed assistive-listening readiness |
| `Telecoil / Induction Loop (IEC 60118-4, NIDCD)` | Hearing-aid signal-path nouns; magnetic coupling vocabulary; NOT field-strength thresholds, IEC 60118-4 compliance proof |
| `Bluetooth Core Specification` | Bluetooth protocol family identity; NOT RF performance, antenna doctrine, LC3/latency numerics |
| `FDA / ISO 13485 / IEC 60601` | Medical device regulatory context vocabulary only; NOT FDA Class II, 510(k), ISO 13485 certification proof |

## Stable Facts

- The hearing-aid source layer is narrow: 5 fact cards and 6 official sources (Bluetooth SIG x3, IEC x1, NIDCD x1, Bluetooth Core x1).
- LE Audio and Auracast vocabulary is supported at Bluetooth SIG identity level; device qualification or ecosystem interoperability is NOT supported.
- Telecoil vocabulary is supported at hearing-aid signal-path noun level via IEC/NIDCD identity sources; field-strength thresholds or coil geometry doctrine are NOT supported.
- The medical manufacturing-control boundary applies: traceability, coating, inspection, and mixed-signal packaging can be discussed as manufacturing posture, NOT as medical-device approval proof.
- This lane is a narrow sub-lane of the broader medical application family; for broader medical device routing, use `wiki/applications/medical-device-pcb-pcba-boundary-map.md`.

## Conditions And Methods

- Use this card to confirm what vocabulary is safe before writing a hearing-aid PCB article.
- For broader medical device context, route to `wiki/applications/medical-device-pcb-pcba-boundary-map.md`.
- For medical manufacturing control vocabulary, route to `facts/methods/medical-manufacturing-control-context-for-coating-tht-and-bga`.
- For medical traceability vocabulary, route to `facts/methods/pcba-medical-traceability-dhr-dmr-boundary`.
- For Bluetooth product-level boundary, route to `facts/standards/interface-wireless-positioning-product-level-boundary`.
- Update `last_reconciled_at` when a new hearing-aid wiki boundary page is created.

## Limits And Non-Claims

- Bluetooth qualification, universal phone compatibility, or interoperability proof is NOT supported.
- Public-venue Auracast support, induction-loop installation prevalence, or finished-device interoperability is NOT supported.
- Telecoil field-strength, response, intelligibility, or immunity thresholds are NOT supported.
- IEC 60118-4 compliance proof or coil geometry doctrine is NOT supported.
- FDA Class II, 510(k), MDR, ISO 13485 certification, IEC 60601 compliance, or supplier qualification is NOT supported.
- RF performance, antenna doctrine, LC3 latency, battery-life, or audio quality numerics are NOT supported.
- Yield, throughput, cost, or lead-time claims are NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|---|---|
| Dedicated hearing-aid wiki boundary page | Closed — created and promoted to `active` in P4-179 |
| Companion fact card (this file) | Closed — created in P4-186 |
| Bluetooth LE Audio certification process vocabulary | Official Bluetooth SIG qualification/test page with stable URL |
| Auracast ecosystem deployment vocabulary | Official CSA or Bluetooth SIG deployment documentation |
| Telecoil field-strength / IEC 60118-4 vocabulary | Official IEC 60118-4 standard page with stable public URL |
| FDA Class II / 510(k) clearance vocabulary | Official FDA guidance page recovery for hearing device regulation |
| ISO 13485 certification vocabulary for hearing devices | Official ISO 13485 or notified-body documentation page |
