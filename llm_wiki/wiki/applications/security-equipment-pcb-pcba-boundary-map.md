---
topic_id: "applications-security-equipment-pcb-pcba-boundary-map"
title: "Security Equipment PCB PCBA Boundary Map"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
activated_at: "2026-05-03"
activation_notes: "P4-169 review pass: boundary language stable, all 7 board families have safe/blocked pairs, civilian-vs-defense-vs-smart-home routing decision table present, UL/EN/ONVIF standards identity table complete, must-refresh and cross-lane routing present. Promoted to active."
fact_ids:
  - "applications-security-equipment-coverage-gap-map"
  - "applications-application-coverage-gap-map"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-flying-probe-vs-ict-selection-posture"
  - "methods-hidden-joint-xray-inspection-boundary"
source_ids:
  - "frontendapt-industry-security-equipment-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
tags: ["security", "camera", "cctv", "nvr", "access-control", "alarm", "fire-alarm", "intercom", "poe", "pcb", "pcba", "boundary-map", "application-boundary"]
---

# Definition

> Civilian security equipment PCB/PCBA writing is safe at board-class, layout-context, and process-review vocabulary for commercial surveillance, access control, alarm, fire, intercom, and power systems. It is unsafe when it crosses into security-certification listing (UL 864, EN 54, EN 50131), access-control compliance (UL 294, EN 60839), video protocol conformance (ONVIF), biometric data privacy regulation, 24/7 uptime guarantees, or field-reliability outcomes.

## Why This Topic Matters

- Civilian security vocabulary overlaps with **two separate wrong routes**: defense/EW/surveillance (MIL-STD, ISR, targeting) and maker/smart-home (consumer IoT, ESP32, Alexa). This page establishes where civilian security sits and why it is a distinct segment.
- Security certification standards (UL 864, EN 54, EN 50131, UL 294) are frequently cited in the domain but are NOT in the sources registry at any level beyond identity-only.
- Trust-bar marketing labels (`"24/7 Operation"`, `"Long Service Life"`, `"Harsh Environments"`) must not appear as performance specifications in published content.

---

## Routing Decision: Civilian vs. Defense vs. Smart-Home

| Context | Route To |
|---|---|
| Civilian commercial/residential security (cameras, alarms, access control, fire panels) | **This page** |
| Military/defense surveillance, ISR, EW, targeting | `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md` |
| Consumer smart-home security (doorbell cameras, consumer smart locks, Alexa/Google Home) | `wiki/applications/maker-and-smart-home-platform-boundaries.md` |

---

## Board Family Routing

### Control Panel / Central Controller PCBs

**Safe angles:**
- Multizone IO vocabulary: sensor zone inputs, siren/relay outputs, programmable IO, terminal connector layout description
- Communication and network integration vocabulary: Ethernet, RS-485, RS-232, GSM/LTE, Wi-Fi, proprietary RF module integration description (identity-level only)
- User interface vocabulary: LCD/LED display, keypad, indicator, buzzer on main or satellite panel board description
- Input isolation and protection vocabulary: input protection, isolation, surge components for sensor lines and output drivers

**Blocked:**
- EN 50131 grading or system classification claims
- UL 2050 monitoring station approval claims
- Specific zone-count, event-log capacity, or processor performance claims
- Integration with named proprietary security platforms (Bosch, Honeywell, DSC, Hikvision) as proof of compliance

---

### Video Surveillance (Camera / NVR / DVR) PCBs

**Safe angles:**
- Camera and image processing board vocabulary: image sensor, ISP, SoC, memory integration in compact form factor description
- NVR/DVR mainboard vocabulary: multilayer board with video inputs, SATA/NVMe storage, network ports, HDMI/VGA output, control interface description
- PTZ motor control vocabulary: pan/tilt/zoom motor, encoder, position sensor board description
- PoE integration vocabulary: PoE front-end, DC/DC conversion, surge protection on camera PCB description

**Blocked:**
- Image resolution, frame rate, low-light sensitivity, WDR, or video analytics performance claims
- ONVIF conformance, H.265/H.264 encoding standard, or streaming protocol compliance
- Camera detection range, field-of-view accuracy, or recognition-rate claims
- GDPR, CCPA, or surveillance data-retention compliance claims

---

### Access Control / Smart Lock / Entry System PCBs

**Safe angles:**
- Credential reader electronics vocabulary: RFID/NFC, magnetic-stripe, QR/barcode, biometric sensor module integration description
- Door and lock control vocabulary: relay/driver circuits for electric locks, magnetic locks, strikes, turnstile mechanisms description
- Network and system integration vocabulary: CAN, RS-485, Ethernet, Wi-Fi integration on field controller PCBs (identity-level only)
- User interface board vocabulary: keypad, status LED, buzzer for wall-mounted reader/panel description

**Blocked:**
- UL 294 or EN 60839 access-control system compliance claims
- Biometric recognition accuracy, FAR/FRR, or liveness detection performance claims
- GDPR, CCPA, or biometric data privacy compliance claims
- Interoperability with named access-control platforms (Lenel, CCURE, Genetec) as compliance proof

---

### Intrusion / Perimeter Sensor PCBs

**Safe angles:**
- Low-noise analog front-end vocabulary: PIR, microwave, acoustic, vibration sensor circuit layout with noise and drift minimization description
- Signal processing and logic vocabulary: MCU, comparator, filtering on detector PCB for event detection, sensitivity adjustment, tamper monitoring
- Power and battery management vocabulary: efficient power circuit for wired and wireless detectors, low-power design description
- Tamper and status interface vocabulary: tamper loop, LED indicator, communication line for panel integration

**Blocked:**
- EN 50131 performance grade (Grade 1–4) compliance claims
- Detection distance, coverage angle, or false-alarm rate performance claims
- Environmental immunity class (WR, IK) compliance claims
- Anti-masking capability proof

---

### Fire Alarm / Gas / Safety Monitoring PCBs

**Safe angles:**
- Detection and measurement front-end vocabulary: smoke, heat, gas sensor PCB with low-noise analog front-end, threshold logic, compensation circuit description
- Fire alarm control panel board vocabulary: multizone or addressable loop controller PCB for managing detector loops, sounder circuits, system interfaces description
- Emergency lighting and exit sign board vocabulary: LED driver, backup power circuit integration
- Building management interface vocabulary: communication circuit for linking to BMS or centralized platforms (identity-level only)

**Blocked:**
- UL 864, EN 54, or NFPA 72 fire-alarm panel listing or approval claims
- EN 61010 / IEC 60079 (hazardous-area / ATEX) compliance claims
- Smoke/heat/gas sensitivity threshold, alarm delay, or response-time specifications
- Life-safety approval, AHJ (Authority Having Jurisdiction) acceptance, or installation-code compliance proof

---

### Intercom / Entry Phone / Communication PCBs

**Safe angles:**
- Audio and voice circuit vocabulary: microphone, speaker, codec, amplification stage layout for low-noise audio description
- Video interface and control vocabulary: camera input, display, control key board for video door phone and indoor unit description
- Network and bus connectivity vocabulary: 2-wire digital bus, IP networking, multi-unit intercom bus integration description
- Front-panel ruggedness vocabulary: electronics behind vandal-resistant, weatherproof panel description

**Blocked:**
- Audio intelligibility, MOS score, or echo-cancellation performance claims
- SIP/VoIP protocol conformance or IP-PBX compatibility proof
- Vandal-resistance IK rating, ingress-protection IP rating proof
- PoE standard (IEEE 802.3af/at) compliance claims

---

### Security Power / Backup / PoE PCBs

**Safe angles:**
- AC-DC and DC-DC conversion vocabulary: main PSU and auxiliary converter PCB topology description
- Battery backup and charging vocabulary: lead-acid/Li-ion/LiFePO4 charging/monitoring/switchover logic description
- Protection and filtering vocabulary: surge protection, fusing, over-voltage/over-current protection on security power PCBs
- Distribution and status monitoring vocabulary: multi-output distribution board with fuse/CB and LED indicator description

**Blocked:**
- UL 603, EN 50131-6 security power supply standard compliance claims
- IEEE 802.3af/at/bt PoE compliance proof
- Battery backup duration or hold-up time performance claims
- Exact efficiency, ripple, or regulation specification claims

---

## Standards Context

| Standard | Safe Use |
|---|---|
| `EN 50131` | European intrusion alarm standard identity — NOT compliance or grading proof |
| `UL 2050 / UL 681` | US security alarm monitoring standard identity — NOT certification proof |
| `UL 864 / EN 54` | Fire alarm panel listing standard identity — NOT listing or approval proof |
| `UL 294 / EN 60839` | Access-control system standard identity — NOT compliance proof |
| `ONVIF` | IP camera interoperability standard identity — NOT conformance proof |
| `NFPA 72` | National fire alarm code identity — NOT code-compliance or AHJ-approval proof |
| `IEEE 802.3af/at/bt` | PoE standard identity — NOT PoE-compliance or interoperability proof |

---

## Engineering Boundaries

- Civilian security equipment has no defense context; do not borrow MIL-STD vocabulary from the defense page.
- Treat all security board content as board-class and process-review stories, not as certification-listing or compliance stories.
- Fire alarm and life-safety vocabulary is highest risk for overclaiming; frame all fire PCB content as manufacturing support, never as listing or approval proof.
- Biometric and video analytics vocabulary is highest risk for privacy overclaiming; keep at "sensor module integration" level only.

---

## Common Misreadings

- `"24/7 Operation – Reliable"` trust-bar → does NOT prove uptime guarantee, MTBF, or field-failure rate.
- `"Long Service Life – Proven"` trust-bar → does NOT prove qualification cycle, deployment volume, or reliability statistic.
- Fire alarm PCB manufactured → does NOT prove UL 864, EN 54, or NFPA 72 listing; panel listing is a system-level certification.
- Access control PCB built → does NOT prove UL 294 or EN 60839 compliance.
- Biometric sensor integrated on PCB → does NOT prove recognition accuracy, liveness detection, or GDPR compliance.
- PoE circuitry on camera board → does NOT prove IEEE 802.3af/at/bt compliance.
- This page is used → does NOT mean defense/ISR vocabulary is permitted; see `defense-ew-surveillance-targeting-pcb-review-boundaries.md` for that context.

---

## Must Refresh Before Publishing

- Any EN 50131, UL 2050/681, or national intrusion-alarm standard compliance claims
- Any UL 864, EN 54, NFPA 72, or fire-alarm listing/approval claims
- Any UL 294, EN 60839, or access-control compliance claims
- Any ONVIF conformance, H.265/H.264 encoding, or video-standard compliance claims
- Any GDPR, CCPA, or biometric/surveillance data-privacy regulation claims
- Any 24/7 uptime, MTBF, DPPM, or field-reliability outcome claims

---

## Cross-Lane Routing

| Content Type | Route To |
|---|---|
| Defense / military surveillance, ISR, EW targeting | `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md` |
| Consumer smart-home security (doorbell, consumer smart lock) | `wiki/applications/maker-and-smart-home-platform-boundaries.md` |
| DFM / DFT review gates | `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md` |
| Flying probe vs ICT | `facts/methods/pcba-flying-probe-vs-ict-selection-posture.md` |
| X-ray hidden-joint inspection | `facts/methods/hidden-joint-xray-inspection-boundary.md` |
| Industrial control overlap (security gateway as industrial controller) | `wiki/applications/industrial-control-pcb-pcba-boundary-map.md` |

---

## Related Pages

- `facts/applications/security-equipment-coverage-gap-map.md`
- `wiki/applications/application-routing-and-boundary-map.md`
- `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md`
- `wiki/applications/maker-and-smart-home-platform-boundaries.md`

## Primary Sources

- /code/hileap/frontendAPT/public/static/industries/en/security-equipment-pcb.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/testing-quality.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
