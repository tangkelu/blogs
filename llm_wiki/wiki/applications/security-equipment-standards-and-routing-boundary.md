---
topic_id: "applications-security-equipment-standards-and-routing-boundary"
title: "Security Equipment Standards And Routing Boundary"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "standards-security-equipment-standards-boundary"
  - "standards-security-equipment-standards-official-depth"
  - "applications-security-equipment-coverage-gap-map"
source_ids: []
notes: "No official UL, CENELEC, IEC, or ONVIF page is currently landed in sources/registry. This page is restricted to document-identity and system-scope framing only."
tags: ["security-equipment", "ul-864", "en-54", "nfpa-72", "en-50131", "ul-2050", "ul-294", "en-60839", "ul-62368-1", "iec-62676", "onvif", "fire-alarm", "access-control", "intrusion", "ip-video", "routing", "standards-boundary"]
---

# Governance Summary

> Security-equipment standards names are safe in this corpus only as document-identity and system-scope routing vocabulary. UL, CENELEC, IEC, NFPA, and ONVIF standards describe complete systems, panels, units, devices, or interoperability programs. They do not create PCB-level certification, grade, listing, conformance, or pass-status. The active routing posture is to keep `security application context` separate from `PCB manufacturing language`, and to stop all certification wording at the system or device boundary.

## What This Page Controls

- Use this page when a draft mentions security-equipment standards by name and needs safe routing before application copy is written.
- Treat standard names as `which security system family is this board supporting?` context, not as `what certification does the PCB have?` proof.
- Route board-construction, assembly, interconnect, and hardware-role wording to the security equipment PCB/PCBA boundary page.
- Keep all listing, grade, conformance, and interoperability outcomes at system, device, or OEM level.

## Routing Model

| Draft signal | Safe routing outcome | Stop line |
|---|---|---|
| Fire alarm / fire detection wording | Use UL 864, EN 54, NFPA 72, BS 5839 as system and document identity only | Do not write the PCB as listed, certified, or compliant |
| Intrusion / burglar alarm wording | Use EN 50131, UL 2050, UL 681, EN 50130-4 as system-grade or monitoring-service context only | Do not assign Grade 1-4 or monitoring qualification to the PCB |
| Access control wording | Use UL 294, EN 60839, ANSI/SIA AC-01 as controller, reader, or system-unit context only | Do not convert unit listing or grading into PCB claims |
| IP video / surveillance wording | Use ONVIF, IEC 62676, H.265, H.264, RTSP as device interoperability or codec-identity context only | Do not write ONVIF conformance or video performance as PCB output |
| General product safety wording | Use UL 62368-1 / IEC 62368-1 as safety-sensitive equipment context only | Do not write UL listing, IEC compliance, or creepage proof as PCB manufacturing status |

## Standard Family Routing

### Fire Alarm / Detection

- `UL 864` is safe as the identity of a fire alarm control-unit listing standard.
- `EN 54` is safe as the identity of a European fire detection and alarm system standard family.
- `NFPA 72` and `BS 5839` are safe as system design and installation code identity.
- Safe PCB-side vocabulary: fire alarm control panel PCB, loop controller board, detector interface board, power-supply support board.
- Stop line: fire alarm listing, certification, CE-mark outcome, or approval belongs to the complete panel, system, or listed module, not to PCB fabrication or assembly.

### Intrusion / Burglar Alarm

- `EN 50131` is safe as intrusion and hold-up alarm system identity, including Grade 1-4 language at complete-system level only.
- `UL 2050` is safe as monitoring-service identity, not alarm-board proof.
- `UL 681` and `EN 50130-4` are safe as installation or environmental requirement identity.
- Safe PCB-side vocabulary: zone IO board, alarm controller board, communication module board, tamper input interface.
- Stop line: grade assignment, service listing, or tamper/environmental performance is not a PCB manufacturing attribute.

### Access Control

- `UL 294` is safe as access control system unit listing identity.
- `EN 60839` is safe as electronic access control system identity and grading context.
- `ANSI/SIA AC-01` is safe as protocol and communication identity.
- Safe PCB-side vocabulary: RFID/NFC reader board, access-control panel main board, relay output controller, RS-485/Wiegand/OSDP interface board.
- Stop line: UL 294 listing level, EN 60839 grading, or device compliance does not belong to the PCB alone.

### IP Video / Surveillance

- `ONVIF` is safe as IP-security device interoperability identity, including profile names as device-context vocabulary.
- `IEC 62676` is safe as video surveillance system identity.
- `H.265`, `H.264`, and `RTSP` are safe as codec or protocol identity.
- Safe PCB-side vocabulary: camera SoC board, NVR/DVR mainboard, PoE front-end board, PTZ driver board, analytics accelerator board.
- Stop line: ONVIF conformance, image quality, bitrate, latency, resolution, and interoperability pass-status are device and firmware outcomes, not PCB outputs.

### General Security-Hardware Safety

- `UL 62368-1 / IEC 62368-1` is safe as product-safety context for security cameras, NVR/DVR hardware, access-control panels, and similar equipment.
- Safe PCB-side vocabulary: board for safety-sensitive security equipment, power-isolation context, energy-source context.
- Stop line: listing, certification, creepage/clearance proof, dielectric proof, and safety pass-status belong to the complete equipment unit and its qualification program.

## System-Level vs PCB-Level Stop Line

### Safe PCB / PCBA Framing

- board role inside a fire alarm, intrusion, access-control, or IP-video device
- assembly context for controller, reader, camera, recorder, interface, power, relay, or communication boards
- standards names as market or system-family vocabulary

### Blocked System-Level Leakage

- listing number, certification mark, grade, conformance profile, compliance status, or approval outcome
- device qualification, interoperability pass-status, or installation-code satisfaction
- wording that turns the PCB manufacturer into the holder of UL, EN, IEC, NFPA, or ONVIF status

## Common Misreadings

- `UL 864 listed PCB` is not supported; the listing belongs to the complete fire alarm control unit or system equipment.
- `EN 54 certified board` is not supported; EN 54 certification applies to the tested system or component family.
- `EN 50131 Grade 2 PCB` is not supported; grade applies to the complete installed system.
- `UL 294 compliant PCBA` is not supported; listing belongs to the access-control unit.
- `ONVIF-compatible PCB` is not supported; conformance is evaluated at device and firmware level.
- `H.265 4K PCB` is not supported; codec identity is safe, but image or streaming performance is not a PCB manufacturing claim.
- `UL 62368-1 listed security camera board` is not supported; safety listing belongs to the complete equipment unit.

## Explicit Blocked Claims

- `certification-validity claims`: do not state or imply that a PCB or PCBA is certified, listed, CE-marked, ONVIF-conformant, or otherwise officially validated under these standards.
- `qualification pass-status`: do not claim that a PCB has passed grade assignment, interoperability testing, environmental qualification, or regulatory acceptance.
- `supplier-proof claims`: do not claim the PCB manufacturer or assembler holds the system-level listing, conformance, or approval.
- `cost/lead-time/yield claims`: do not derive any commercial, schedule, or production-yield conclusion from the standards names on this page.

## Must Refresh Before Publishing

- any exact UL listing number, UL file number, or category code
- any EN, IEC, NFPA, or ONVIF clause-specific requirement wording
- any ONVIF registry result, profile conformance result, or device-registration statement
- any EN 50131 grade claim, UL 294 level claim, or UL 62368-1 pass-status statement
- any privacy, biometric, GDPR, or CCPA compliance statement
- any cost, lead-time, throughput, or yield statement

## Related Pages

- `facts/standards/security-equipment-standards-boundary.md`
- `facts/standards/security-equipment-standards-official-depth.md`
- `wiki/applications/security-equipment-pcb-pcba-boundary-map.md`
- `facts/applications/security-equipment-coverage-gap-map.md`
- `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md`
- `wiki/applications/maker-and-smart-home-platform-boundaries.md`
