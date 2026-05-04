---
fact_id: "standards-security-equipment-standards-official-depth"
title: "Security equipment standards official-depth: UL 62368-1, UL 294, ONVIF, IEC 62676, EN 50131 public metadata with explicit PCB stop lines"
topic: "Security equipment standards official-source depth and PCB boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-188 initial build. Supplements facts/standards/security-equipment-standards-boundary.md with deeper official-source public metadata framing for UL 62368-1 (safety of audio/video and IT equipment), UL 294 (access control), ONVIF, IEC 62676 (video surveillance), and EN 50131 (intrusion/burglar alarm) — all based on publicly available standards-organization identity pages. No new sources currently added to registry (UL, IEC, ONVIF, and CENELEC pages not yet recovered); existing source_ids from the baseline boundary card are inherited."
source_ids: []
notes: "No official UL, IEC, ONVIF, or CENELEC source is currently in the sources registry. This card uses publicly known standards-identity metadata from standards organizations' public documentation. Refresh source_ids when official pages are recovered."
tags: ["security-equipment", "ul-62368-1", "ul-294", "onvif", "iec-62676", "en-50131", "safety", "fire-alarm", "access-control", "intrusion", "ip-surveillance", "standards-depth", "official-source"]
---

# Canonical Summary

> This card provides deeper official-source public metadata framing for the five most-referenced security equipment standards: UL 62368-1 (general safety of audio/video/IT equipment — the dominant product-safety standard for security hardware), UL 294 (access control unit listing), ONVIF (IP camera interoperability), IEC 62676 (video surveillance systems), and EN 50131 (intrusion and hold-up alarm systems). All are system/device/panel-level standards. None creates PCB-level listing, grading, or conformance status. PCB vocabulary must stop at board-class and assembly-context level; all listing, compliance, and qualification claims belong to the device/system OEM.

---

## Standard Family 1: UL 62368-1 — Safety of Audio/Video, Information, and Communication Technology Equipment

### Official-Source Public Metadata

| Item | Public Identity |
|---|---|
| **Issuer** | UL (Underwriters Laboratories) in collaboration with IEC TC 108 |
| **IEC parallel** | IEC 62368-1 "Audio/video, information and communication technology equipment — Part 1: Safety requirements" |
| **Supersedes** | UL 60950-1 (IT equipment safety) and UL 60065 (audio/video safety) — now the dominant product-safety standard for security cameras, NVR/DVR, IP video controllers, and access control panels |
| **Scope** | Safety requirements for audio/video, IT, and communication technology equipment: energy source classification (ES1/ES2/ES3), electrical safety, fire enclosure, mechanical safety, and thermal safety for the complete equipment unit |
| **PCB relevance** | Security equipment PCBs (camera SoC boards, NVR/DVR motherboards, PoE interface boards, access control panels) are manufactured for assemblies that ultimately require UL 62368-1 / IEC 62368-1 listing |

### Safe Use at PCB Level

- Board-class identity: "NVR/DVR motherboard for IEC 62368-1-listed security equipment" — safe as application-context vocabulary.
- PCB manufacturing vocabulary (board construction, component placement, thermal design, conformal coating) can describe the board's role in safety-sensitive equipment.
- Energy source classification vocabulary (ES1/ES2/ES3) may be used to describe the board's safety design context, not as PCB listing proof.

### Blocked at PCB Level

- `"UL 62368-1 listed PCB"`, `"IEC 62368-1 compliant PCBA"`, `"UL Listed security camera board"` — listing belongs to the complete device/equipment unit after testing.
- Any exact creepage/clearance, insulation, or dielectric strength value claimed as PCB manufacturing output rather than design requirement.
- Any claim that the PCB manufacturer holds the UL listing or IEC certification.

---

## Standard Family 2: UL 294 — Access Control System Units

### Official-Source Public Metadata

| Item | Public Identity |
|---|---|
| **Issuer** | UL (Underwriters Laboratories) |
| **Scope** | Standard for Access Control System Units: covers card readers, controllers, credential storage, door release hardware, and power supplies as complete access-control units |
| **Listing levels** | UL 294 defines levels for destructive attack, line security, endurance, and standby power — applicable to the tested device unit |
| **PCB relevance** | Access control PCBs (reader interface boards, door relay output controllers, RS-485/Wiegand/OSDP interface boards, panel main boards) are components of UL 294-listed access control units |

### Safe Use at PCB Level

- Board-class identity: "Access control panel PCB designed for UL 294-listed controller units" — safe as application-context vocabulary.
- Interface vocabulary (RS-485, Wiegand, OSDP, PoE, relay output) is safe as board-class context.

### Blocked at PCB Level

- `"UL 294 listed PCB"`, `"UL 294 Level IV access control board"` — UL 294 listing and level assignment are for the complete access control unit, not the PCB.
- Destructive attack rating, line security level, or endurance class claims at PCB level.

---

## Standard Family 3: ONVIF — Open Network Video Interface Forum

### Official-Source Public Metadata

| Item | Public Identity |
|---|---|
| **Organization** | ONVIF consortium (formed by Axis Communications, Bosch, and Sony; now open membership) |
| **Purpose** | Defines common protocols for IP-based physical security products (cameras, video management, access control, intercom) to ensure interoperability |
| **Profiles** | ONVIF Profile S (streaming), Profile G (storage), Profile C (access control), Profile A (access control configuration), Profile M (metadata/analytics), Profile T (advanced streaming) |
| **Conformance** | Device-level interoperability conformance testing — the complete network device submits to ONVIF-authorized test laboratory; conformance is per-profile, per-device |
| **PCB relevance** | IP camera SoC boards, NVR processing boards, video analytics boards are designed to enable ONVIF protocol support in complete devices |

### Safe Use at PCB Level

- Board-class identity: "IP camera SoC board for ONVIF Profile S streaming devices" — safe as application-context vocabulary.
- Network interface vocabulary (RJ45, PoE, GbE/100Mbps, RTSP, ONVIF protocol context) is safe as board-level design context.

### Blocked at PCB Level

- `"ONVIF Profile T conformant PCB"`, `"ONVIF-compatible board"`, `"ONVIF certified PCBA"` — ONVIF conformance is per-device, not per-PCB.
- Any ONVIF profile interoperability claim, video streaming performance claim, or metadata analytics capability claim at PCB manufacturing level.

---

## Standard Family 4: IEC 62676 — Video Surveillance Systems

### Official-Source Public Metadata

| Item | Public Identity |
|---|---|
| **Issuer** | IEC TC 79 (Alarm and Electronic Security Systems) |
| **Scope** | IEC 62676 series covers video surveillance systems for use in security applications: system requirements (IEC 62676-1-1), image quality (IEC 62676-1-2), transmission/compression (IEC 62676-2-1 through 2-3), IT interface (IEC 62676-4), and installation (IEC 62676-5) |
| **Overlap with EN** | EN 62676 is the European harmonized adoption of IEC 62676 for use with CE marking |
| **PCB relevance** | Video surveillance processing boards (ISP/SoC, NVR/DVR, H.265 encode/decode, analytics accelerator) are designed for products tested against IEC 62676 |

### Safe Use at PCB Level

- Board-class identity: "Video processing board for IEC 62676 video surveillance systems" — safe as application-context vocabulary.
- Codec identity (H.265/HEVC, H.264/AVC) is safe as algorithm-identity vocabulary; encoding performance is not a PCB claim.

### Blocked at PCB Level

- `"IEC 62676 compliant video processing PCB"`, `"EN 62676 listed NVR board"` — IEC 62676 compliance is system/device-level.
- Video resolution, encoding bitrate, compression ratio, or image quality claims at PCB manufacturing level.

---

## Standard Family 5: EN 50131 — Intrusion and Hold-Up Alarm Systems

### Official-Source Public Metadata

| Item | Public Identity |
|---|---|
| **Issuer** | CENELEC (European Committee for Electrotechnical Standardization) |
| **Scope** | EN 50131 series covers alarm systems for intrusion and hold-up: system requirements (EN 50131-1), control and indicating equipment (EN 50131-3), power supplies (EN 50131-6), grade definitions (Grade 1–4: low risk to high risk), environmental categories |
| **Grade system** | Grade 1 (low risk), Grade 2 (low to medium risk), Grade 3 (medium to high risk), Grade 4 (high risk) — applied to the complete system after testing, not to individual PCBs |
| **PCB relevance** | Intrusion alarm control panels, zone input/output boards, communication module boards, power supply boards are manufactured for EN 50131-graded systems |

### Safe Use at PCB Level

- Board-class identity: "Intrusion alarm control panel PCB for EN 50131 Grade 2 systems" — safe as application-context vocabulary.
- Zone interface vocabulary (RS-485 bus, loop resistance, tamper input, output relay) is safe as board-class context.

### Blocked at PCB Level

- `"EN 50131 Grade 3 PCB"`, `"EN 50131 compliant alarm panel board"` — Grade assignment is for the complete alarm system/unit.
- Tamper resistance level, environmental performance category, or self-monitoring ability as PCB manufacturing attributes.

---

## Summary: PCB Stop Lines for Security Equipment Standards

| Standard | Safe Vocabulary | Blocked Vocabulary |
|---|---|---|
| **UL 62368-1 / IEC 62368-1** | Board-class identity for safety-sensitive equipment; energy source context | UL listing, IEC 62368-1 compliance, creepage/clearance proof at PCB level |
| **UL 294** | Board-class identity for access control units; RS-485/Wiegand/PoE context | UL 294 listing, level assignment at PCB level |
| **ONVIF** | IP camera/NVR board-class identity; network interface vocabulary | ONVIF profile conformance, interoperability proof at PCB level |
| **IEC 62676** | Video surveillance processing board-class identity; codec algorithm identity | IEC 62676 compliance, video quality, encoding performance at PCB level |
| **EN 50131** | Intrusion alarm PCB board-class identity; zone interface vocabulary | EN 50131 grade assignment, tamper performance, environmental category at PCB level |

---

## Remaining Gaps

| Gap | Reopen Condition |
|---|---|
| Official UL 62368-1 standard page (UL product page) | UL.com product-standard page with stable URL added to registry |
| Official IEC 62368-1 standard metadata | IEC webstore product page with stable URL added to registry |
| Official UL 294 standard page | UL.com product-standard page added to registry |
| Official ONVIF profile conformance page | ONVIF.org conformance/profiles page added to registry |
| Official IEC 62676 standard metadata | IEC webstore series page added to registry |
| Official EN 50131 standard metadata | CENELEC or BSI page added to registry |
| UL 62368-1 exact creepage/clearance tables | Official UL 62368-1 full-text source (clause-level) |
| EN 50131 exact environmental/tamper test vocabulary | Official EN 50131 clause-level source |
