# Security Equipment PCB Evidence Pack

**Pack ID**: `consumption-security-equipment`
**Date**: 2026-05-03
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Security Equipment PCB/PCBA — civilian (alarm panel, IP camera/NVR, access control, intrusion sensor, fire alarm, security power)"
scope: |
  Conservative evidence pack for civilian security equipment PCB/PCBA content.

  Supports board-class vocabulary for 6 civilian security board families:
  control panel/central controller, video surveillance, access control/smart lock,
  intrusion/perimeter sensors, fire alarm/gas/safety monitoring, and
  security power/backup/PoE.

  Covers official-depth standards identity (UL 62368-1, UL 294, ONVIF, IEC 62676,
  EN 50131) at document-identity and system-scope level only.

  No UL/EN certification proof, ONVIF conformance, video performance proof,
  privacy compliance, or uptime guarantee claims.

  IMPORTANT: This pack covers CIVILIAN security only. For military/defense
  surveillance and ISR, use defense-ew-surveillance-evidence-pack.md.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Application boundary
  - "applications-security-equipment-coverage-gap-map"

  # Official-depth standards card (P4-188)
  - "standards-security-equipment-standards-official-depth"

  # Test / inspection
  - "methods-pcba-inspection-process-governance-boundary"
  - "methods-pcba-flying-probe-vs-ict-selection-posture"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-hidden-joint-xray-inspection-boundary"

source_ids:
  - "frontendapt-industry-security-equipment-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"

wiki_framing_support:
  - "wiki/applications/security-equipment-pcb-pcba-boundary-map"
  - "wiki/applications/security-equipment-standards-and-routing-boundary"

must_refresh:
  - claim: "UL 62368-1 revision or UL 294 edition updates"
    value: true
  - claim: "ONVIF profile revision or conformance program status"
    value: true
  - claim: "EN 50131 or IEC 62676 amendment status"
    value: true

excluded_claim_classes:
  - "UL 2050 / EN 50131 intrusion-detection certification proof"
  - "UL 864 / EN 54 / NFPA 72 fire-alarm panel listing proof"
  - "UL 294 / EN 60839 access-control compliance proof"
  - "ONVIF conformance, H.265/H.264 encoding performance, video analytics accuracy"
  - "GDPR / CCPA / biometric data privacy or surveillance data-retention compliance"
  - "24/7 uptime, MTBF, or field-failure rate claims"
  - "Cost, lead-time, and yield claims"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `security camera PCB`, `alarm panel PCB`, `access control board`, `NVR PCB`, `fire alarm PCB`, `CCTV board` |
| **Page Type** | `query` |
| **Search Intent** | Security system hardware, surveillance equipment electronics, alarm panel manufacturing, access control PCBs |
| **Target Reader** | Security system engineers, surveillance hardware designers, building security integrators |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` — board-class design vocabulary and standards-identity framing supported; UL/EN certification proof, ONVIF conformance, and privacy compliance blocked.

> **Critical routing note**: This pack covers **civilian** security equipment only. For military/defense ISR, EW, and surveillance missions, use `wiki/consumption/defense-ew-surveillance-evidence-pack.md`.

---

## 3. Board Families (Evidence Scope)

### 3.1 Control Panel / Central Controller

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Alarm control panel, access controller mainboard, security hub, zone expander board context |
| IO vocabulary | Multizone IO (sensor zones, siren/relay outputs), input isolation/surge vocabulary |
| Interface vocabulary | RS-485/RS-232/Ethernet/GSM/Wi-Fi/RF module integration vocabulary |
| UL 864/EN 54 panel listing, EN 50131 alarm compliance proof | ❌ Blocked |

### 3.2 Video Surveillance (Camera / NVR / DVR)

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | IP camera board, PTZ camera board, NVR/DVR mainboard, encoder/decoder board context |
| Camera board vocabulary | Image sensor + ISP/SoC/memory board compact form factor vocabulary |
| NVR/DVR vocabulary | Multilayer (SATA/NVMe/network/HDMI/VGA), PTZ motor control vocabulary |
| Power vocabulary | PoE front-end + DC-DC + surge protection vocabulary |
| ONVIF conformance, video analytics accuracy, resolution, encoding performance proof | ❌ Blocked |

### 3.3 Access Control / Smart Lock / Entry

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Door controller, RFID/badge reader, biometric PCBA, smart lock, turnstile controller board context |
| Sensor vocabulary | RFID/NFC/magnetic-stripe/biometric sensor module integration vocabulary |
| Output vocabulary | Door/lock relay/driver output stage vocabulary |
| Interface vocabulary | RS-485/Ethernet/Wi-Fi/CAN fieldbus identity vocabulary |
| EN 60839 / UL 294 access-control compliance, biometric privacy, GDPR proof | ❌ Blocked |

### 3.4 Intrusion / Perimeter Sensors

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | PIR motion detector, door/window contact, glass break sensor, vibration detector, IR beam barrier board context |
| Analog vocabulary | Low-noise analog front-end for PIR/microwave/acoustic/vibration sensing |
| Circuit vocabulary | MCU/comparator/filtering on detector PCB, battery + low-power design vocabulary |
| Interface vocabulary | Tamper/status interface vocabulary |
| EN 50131 Grade classification, detection range, false-alarm rate proof | ❌ Blocked |

### 3.5 Fire Alarm / Gas / Safety Monitoring

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Fire alarm control panel, smoke/heat detector, gas detector, emergency lighting board context |
| Front-end vocabulary | Detection/measurement front-end (smoke/heat/gas low-noise analog) vocabulary |
| Controller vocabulary | Addressable loop controller board vocabulary |
| Power vocabulary | Emergency LED + backup power circuit, BMS interface vocabulary |
| UL 864 / EN 54 / NFPA 72 fire-alarm listing, detection performance proof | ❌ Blocked |

### 3.6 Security Power / Backup / PoE

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | AC-DC PSU, battery charger/backup, UPS/backup PCBA, PoE injector/switch power board context |
| Power conversion vocabulary | AC-DC/DC-DC conversion board vocabulary |
| Battery vocabulary | Battery backup/charging (lead-acid/Li-ion/LiFePO4) with health monitoring vocabulary |
| Protection vocabulary | Surge/fuse/OV/OC protection, PoE front-end vocabulary |
| Efficiency proof, uptime guarantee, UPS certification | ❌ Blocked |

---

## 4. Standards Context (Identity Only — from P4-188 Official-Depth Card)

| Standard | Safe Use | Blocked Use |
|---|---|---|
| **UL 62368-1** | Audio/video and IT equipment safety standard identity; system-scope framing | Product listing validity, PCB-level certification proof |
| **UL 294** | Access control systems standard identity; system-scope document identity | Access control compliance proof, product listing |
| **ONVIF** | IP physical security interoperability standard identity; profile family identity (Profile S/G/T/M) | Conformance certification, product interoperability proof |
| **IEC 62676** | Video surveillance systems standard identity; document-family framing | Compliance proof, performance specification |
| **EN 50131** | Intrusion and hold-up alarm systems standard identity; grade and class vocabulary at identity level | Grade compliance proof, product listing, alarm response claim |

---

## 5. Civilian vs Defense Separation

| Category | Correct Pack |
|---|---|
| Retail/commercial IP cameras, CCTV systems | This pack (`security-equipment-evidence-pack.md`) |
| Building access control panels | This pack |
| Intrusion/burglar alarm systems | This pack |
| Civilian fire alarm panels | This pack |
| Commercial intercom systems | This pack |
| Military/defense ISR, EW, surveillance | `defense-ew-surveillance-evidence-pack.md` |
| Defense drone control stacks | `defense-ew-surveillance-evidence-pack.md` |
| Smart-home consumer security devices | Also check `maker-smart-home-evidence-pack.md` |

---

## 6. Allowed vs Blocked

### 6.1 Allowed (Board-Class and Standards-Identity Context)

| Claim Pattern | Example |
|---|---|
| Board-class vocabulary | "Security alarm control panels combine multizone IO, communication interfaces, and relay outputs on mixed-signal PCBs" |
| Standards-identity framing | "Security equipment design references standards families such as UL 62368-1 for product safety and EN 50131 for intrusion-alarm system architecture" |
| PoE vocabulary | "IP camera boards integrate PoE front-end, DC-DC conversion, and surge protection alongside the image-processing SoC" |
| Power backup vocabulary | "Security power supplies include battery backup/charging circuits for continued operation during mains failure" |

### 6.2 Blocked (Certification / Compliance / Performance)

| Blocked Claim | Reason |
|---|---|
| "UL 864 listed fire alarm PCB" | UL listing is granted to the complete fire-alarm panel/system, not the PCB |
| "ONVIF Profile S conformant IP camera" | ONVIF conformance requires complete device testing through an authorized test lab |
| "EN 50131 Grade 2 alarm system" | EN 50131 grade applies to the complete alarm system, not the PCB |
| "24/7 operation guaranteed" | Uptime is a system-level operational claim, not a PCB manufacturing specification |
| "GDPR compliant biometric reader" | Privacy compliance is a system/software/organizational obligation, not a PCB attribute |

---

## 7. Handoff

**Core Answer**:

> Civilian security equipment PCBs are supported through 6 board families at board-class vocabulary level, plus standards-identity framing for UL 62368-1, UL 294, ONVIF, IEC 62676, and EN 50131. The current evidence supports design vocabulary, interface naming, and standards context. It does not support certification proof, ONVIF conformance, video analytics performance, privacy compliance, or uptime guarantees.

**Safe Reusable Shapes**:

- "Security equipment standards (UL 62368-1, EN 50131, ONVIF) define the system-scope requirements — the PCB provides the physical hardware layer; the complete device must go through the applicable listing or conformance program."
- "Civilian security board families (alarm panels, IP cameras, access control, intrusion sensors, fire alarm) each have distinct PCB design pressures: analog front-ends, communication interface integration, PoE power, and battery backup."
- "Civilian security equipment is distinct from military/defense ISR and EW applications — the standards framework, vocabulary, and claim boundaries are different."

---

## 8. Pre-flight

- [x] Security equipment wiki boundary page referenced
- [x] Application fact card referenced (`facts/applications/security-equipment-coverage-gap-map.md`)
- [x] P4-188 official-depth standards card referenced (`facts/standards/security-equipment-standards-official-depth.md`)
- [x] All 6 fact_ids from existing landed records — no new records required
- [x] All 5 source_ids from existing landed registry records
- [x] Civilian vs defense/EW separation explicitly documented
- [x] Trust-bar marketing labels flagged
- [x] UL/EN/ONVIF certification blocked claims documented
- [x] `must_refresh` items identified for standard revisions and ONVIF profile updates

**Verdict**: ✅ `go_now_conservative` — civilian board-class vocabulary and standards-identity context. Exclude all certification proof, ONVIF conformance, video performance, privacy compliance, and uptime claims.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
