---
fact_id: "applications-security-equipment-coverage-gap-map"
title: "Security equipment application coverage gap map: which board families have wiki-layer routing and which remain blocked"
topic: "Security equipment PCB/PCBA application coverage"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-161 initial build; sourced from frontendapt-industry-security-equipment-page-en (Tier-2), defense-ew-surveillance-targeting-pcb-review-boundaries, and maker-and-smart-home-platform-boundaries. Civilian security equipment is now separated from defense/EW/surveillance overlap."
source_ids:
  - "frontendapt-industry-security-equipment-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
tags: ["security", "camera", "access-control", "alarm", "fire-alarm", "intercom", "cctv", "coverage-map", "gap-map"]
---

# Canonical Summary

> As of 2026-05-03, civilian security equipment has a dedicated wiki boundary page (`wiki/applications/security-equipment-pcb-pcba-boundary-map.md`) created by P4-161. Prior to this lane, civilian security (camera, access-control, alarm, fire-system) was incidentally covered under `defense-ew-surveillance-targeting-pcb-review-boundaries.md`. The Tier-2 internal source supports 6 board families. It does NOT prove retail-security certification (UL 2050, EN 50131), fire-alarm listing (UL 864), access-control compliance (EN 60839), privacy/data regulation compliance, or 24/7 uptime outcomes.

## Board Family Coverage State

### Supported at Scenario + Board-Class Level (Tier-2 Internal Source)

| Board Family | Application Context | PCB/PCBA Vocabulary Supported |
|---|---|---|
| **Control Panel / Central Controller** | Alarm control panels, access controller mainboards, integrated security hubs, zone expanders | Multizone IO (sensor zones, siren/relay outputs), RS-485/RS-232/Ethernet/GSM/Wi-Fi/RF module integration, keypad/LED/display board, input isolation/surge vocabulary |
| **Video Surveillance (Camera / NVR / DVR)** | IP cameras, PTZ cameras, NVR/DVR mainboards, encoder/decoder boards | Image sensor + ISP/SoC/memory board compact form factor, NVR/DVR multilayer (SATA/NVMe/network/HDMI/VGA), PTZ motor control, PoE front-end + DC-DC + surge protection vocabulary |
| **Access Control / Smart Lock / Entry** | Door controllers, RFID/badge readers, biometric PCBAs, smart locks, turnstile controllers | RFID/NFC/magnetic-stripe/biometric sensor module integration, door/lock relay/driver output stage, RS-485/Ethernet/Wi-Fi/CAN fieldbus identity vocabulary, keypad/status indicator board |
| **Intrusion / Perimeter Sensors** | PIR motion detectors, door/window contacts, glass break sensors, vibration detectors, IR beam barriers | Low-noise analog front-end for PIR/microwave/acoustic/vibration sensing, MCU/comparator/filtering on detector PCB, battery + low-power design vocabulary, tamper/status interface |
| **Fire Alarm / Gas / Safety Monitoring** | Fire alarm control panels, smoke/heat detectors, gas detectors, emergency lighting | Detection/measurement front-end (smoke/heat/gas low-noise analog), addressable loop controller board vocabulary, emergency LED + backup power circuit, BMS interface vocabulary |
| **Security Power / Backup / PoE** | AC-DC PSU, battery charger/backup, UPS/backup PCBAs, PoE injector/switch power boards | AC-DC/DC-DC conversion, battery backup/charging (lead-acid/Li-ion/LiFePO4) with health monitoring, surge/fuse/OV/OC protection, PoE front-end board vocabulary |

### Process / Test Coverage Already Applicable

| Capability | Supporting Fact Card |
|---|---|
| Layered PCBA inspection: SPI → AOI → X-ray → ICT/FP → FCT | `methods-pcba-inspection-process-governance-boundary` |
| Flying probe vs ICT selection | `methods-pcba-flying-probe-vs-ict-selection-posture` |
| DFM / DFT review gates | `methods-pcba-dfm-dft-dfa-review-gate-positioning` |
| X-ray for BGA/LGA/SoC hidden joints | `methods-hidden-joint-xray-inspection-boundary` |

### Critical Separation From Defense/EW

`defense-ew-surveillance-targeting-pcb-review-boundaries.md` covers:
- Military/defense ISR, EW, and surveillance missions (MIL-STD vocabulary, classified-system context)
- Defense drone control stacks

It does **NOT** cover civilian security:
- Retail/commercial IP camera systems
- Building access control panels
- Intrusion alarm systems
- Civilian fire alarm panels
- Commercial intercom systems

Use **this card** (and `wiki/applications/security-equipment-pcb-pcba-boundary-map.md`) for civilian security equipment.

## Stable Facts

- The Tier-2 civilian security source covers 6 board families: control panel/central controller, video surveillance, access control/smart lock, intrusion/perimeter sensors, fire alarm/gas/safety, and security power/backup.
- Trust-bar labels (`"24/7 Operation – Reliable"`, `"Long Service Life – Proven"`, `"Harsh Environments – Robust"`) are marketing framing — NOT uptime guarantees or qualification proof.
- Fire alarm PCB vocabulary is NOT equivalent to UL 864, EN 54, or NFPA 72 panel listing.
- Access control PCB vocabulary is NOT equivalent to EN 60839, UL 294, or regulatory compliance.
- Video surveillance PCB vocabulary is NOT equivalent to ONVIF conformance, video analytics performance, or privacy-compliance proof.

## Conditions And Methods

- Use this card for civilian security equipment routing.
- For defense/military surveillance or ISR contexts, use `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md`.
- For smart-home IoT security devices (doorbell cameras, consumer smart locks), also check `wiki/applications/maker-and-smart-home-platform-boundaries.md` for boundary overlap.

## Limits And Non-Claims

- UL 2050, EN 50131, or national intrusion-detection certification claims NOT supported.
- UL 864, EN 54, or NFPA 72 fire-alarm listing claims NOT supported.
- UL 294 or EN 60839 access-control compliance claims NOT supported.
- ONVIF conformance, H.265/H.264 encoding performance, or video analytics accuracy claims NOT supported.
- GDPR, CCPA, biometric data privacy, or surveillance data-retention compliance claims NOT supported.
- 24/7 uptime, MTBF, DPPM, or field-failure rate claims NOT supported.
- Yield, throughput, cost, or lead-time claims NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|-----|-----------------|
| UL 864 / EN 54 fire-panel listing vocabulary depth | Official UL or CENELEC source recovery |
| EN 50131 / UL 2050 intrusion-alarm standard vocabulary | Official EN/UL source recovery |
| ONVIF / video-encoding standard vocabulary | Official ONVIF source recovery |
| EN 60839 / UL 294 access-control standard vocabulary | Official EN/UL source recovery |
| Dedicated security-equipment wiki page status | Reopen only if the page later regresses and requires demotion from `active` |
