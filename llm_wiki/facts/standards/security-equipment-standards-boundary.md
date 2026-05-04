---
fact_id: "standards-security-equipment-standards-boundary"
title: "Security equipment standards (UL 864, EN 54, EN 50131, UL 294, EN 60839, ONVIF) are system/panel/device listing boundaries, not PCB qualification proof"
topic: "Security equipment standards identity and PCB boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids: []
notes: "No official UL, CENELEC, or ONVIF source is currently in the sources registry. This card uses publicly known standards-identity metadata to establish document-level boundary framing only. Refresh to add official sources when recovered."
tags: ["security-equipment", "ul-864", "en-54", "nfpa-72", "en-50131", "ul-2050", "ul-294", "en-60839", "onvif", "fire-alarm", "access-control", "intrusion", "standards-boundary"]
---

# Canonical Summary

> Security equipment standards such as UL 864, EN 54, NFPA 72 (fire alarm), EN 50131, UL 2050 (intrusion/burglar alarm), UL 294, EN 60839 (access control), and ONVIF (IP video interoperability) are system-level panel-listing, device-listing, or interoperability standards. They define requirements for the complete system, panel, or device — not for PCB or PCBA manufacturing. Mentioning these standard names in PCB/PCBA content is safe only as document-identity context; it is not safe as listing, conformance, compliance, or qualification proof at the PCB level.

## Standards Identity Reference

### Fire Alarm / Detection Standards

| Standard | Issuer | Scope (Identity Level) |
|---|---|---|
| **UL 864** | UL (Underwriters Laboratories) | Standard for Control Units and Accessories for Fire Alarm Systems (US market) — panel/control-unit listing |
| **EN 54 series** | CENELEC (European) | Fire Detection and Fire Alarm Systems — component and system standards, including EN 54-2 (control equipment), EN 54-4 (power supply), EN 54-7 (smoke detectors) etc. |
| **NFPA 72** | NFPA (US) | National Fire Alarm and Signaling Code — installation and system design code, not component listing |
| **BS 5839** | BSI (UK) | Fire Detection and Alarm Systems for Buildings — UK system design code |

**PCB boundary for fire alarm standards:**
- Fire alarm PCB manufacturing vocabulary (board construction, assembly) is safe.
- Any fire alarm standard listing (UL 864 listing, EN 54 certification) is a device/panel-level authorization — the PCB manufacturer does not hold it, and the PCB alone cannot have it.
- "EN 54 compliant PCB" and "UL 864 listed PCB" are both unsupported claims.

---

### Intrusion / Burglar Alarm Standards

| Standard | Issuer | Scope (Identity Level) |
|---|---|---|
| **EN 50131 series** | CENELEC (European) | Alarm Systems — Intrusion and Hold-up Alarm Systems — covers system grading (Grade 1–4), component categories, and installation |
| **UL 2050** | UL (US) | Standard for National Industrial Monitoring Association Monitoring of Security Systems — central-station monitoring service requirements |
| **UL 681** | UL (US) | Standard for Installation and Classification of Burglar and Holdup Alarm Systems — installation standard |
| **EN 50130-4** | CENELEC | Alarm Systems — Environmental requirements (immunity) |

**PCB boundary for intrusion alarm standards:**
- Alarm control-panel PCB vocabulary (zone IO, RS-485, sensor interface) is safe.
- EN 50131 Grade (Grade 1–4 tamper resistance, environmental performance) is a system/device classification — not a PCB classification.
- "EN 50131 Grade 2 PCB" is an unsupported claim.

---

### Access Control Standards

| Standard | Issuer | Scope (Identity Level) |
|---|---|---|
| **EN 60839-11 series** | IEC/CENELEC | Electronic Access Control Systems — system and component requirements, performance grading |
| **UL 294** | UL (US) | Standard for Access Control System Units — device/unit listing standard |
| **ANSI/SIA AC-01** | SIA (US) | Access Control Standard — communication and protocol identity |

**PCB boundary for access control standards:**
- Access control PCB vocabulary (RFID reader board, door relay output, RS-485/Ethernet interface board) is safe.
- UL 294 listing is a device/unit-level listing — PCB manufacturers do not hold it.
- EN 60839 grading is a system/component classification — not a PCB manufacturing claim.
- "UL 294 listed PCB" and "EN 60839 compliant PCBA" are unsupported claims.

---

### IP Video / Surveillance Standards

| Standard | Issuer | Scope (Identity Level) |
|---|---|---|
| **ONVIF** (Open Network Video Interface Forum) | ONVIF consortium | IP video device interoperability profiles (Profile S, G, C, A, M, T) — device-level conformance testing |
| **H.265 / HEVC** | ITU-T / ISO/IEC | Video compression standard — codec algorithm identity; performance is device/chip implementation dependent |
| **H.264 / AVC** | ITU-T / ISO/IEC | Video compression standard — codec algorithm identity |
| **RTSP** | IETF | Real-Time Streaming Protocol — network streaming identity |

**PCB boundary for IP video standards:**
- Video surveillance PCB vocabulary (ISP/SoC board, NVR/DVR mainboard, PoE front-end, signal processing board) is safe.
- ONVIF conformance is device-level interoperability testing — PCBs are not ONVIF-conformant independently.
- H.265/H.264 encoding quality, bitrate, latency, or resolution performance are implementation claims — not PCB manufacturing claims.
- "ONVIF-conformant PCB", "H.265 PCB", or "4K PCB" are all unsupported claims.

---

## Stable Facts

- All the above standards operate at system, panel, device, or component level — none of them define PCB manufacturing requirements or create PCB-level listing, grading, or conformance status.
- A PCB manufacturer supports these ecosystems by producing board hardware according to a customer's design; the listing, conformance, or grading decision belongs to the customer (system integrator, device OEM, or test laboratory) testing the final product.
- Standard identity vocabulary (named standard, scope sentence) is safe for application-context framing.
- Listing proof, grading assignment, clause compliance, pass-status, and conformance outcome are all blocked at the PCB level.
- No official UL, CENELEC, IEC, or ONVIF source is currently in the sources registry; this card relies on publicly known standards-identity metadata only.

## Conditions And Methods

- Use this card for any security-equipment draft that mentions fire alarm, intrusion, access control, or IP video standards by name.
- Pair with `wiki/applications/security-equipment-pcb-pcba-boundary-map.md` for full application routing.
- Pair with `wiki/applications/security-equipment-standards-and-routing-boundary.md` for the prompt-consumable companion.
- When official UL listing pages, CENELEC standard metadata pages, or ONVIF profile pages are added to the sources registry, refresh this card to reflect their exact scope language.

## Limits And Non-Claims

- UL 864 panel listing, UL 294 device listing, UL 2050 monitoring-service listing NOT supported.
- EN 54 CE marking, EN 50131 Grade assignment, EN 60839 conformance NOT supported.
- ONVIF profile conformance, H.265/H.264 encoding performance NOT supported.
- GDPR, CCPA, biometric data, or privacy-regulation compliance NOT supported.
- Any "compliant PCB", "listed PCB", or "certified PCB" claim for any security equipment standard NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|-----|-----------------|
| Official UL 864 public metadata source | UL standard page added to sources registry |
| Official EN 54 public metadata source | CENELEC / BSI standard page added to sources registry |
| Official ONVIF conformance profile documentation | ONVIF public registry page added to sources registry |
| Official EN 50131 / UL 2050 source | Added to sources registry |
| Official UL 294 / EN 60839 source | Added to sources registry |
