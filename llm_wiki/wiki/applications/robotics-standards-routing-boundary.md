---
topic_id: "applications-robotics-standards-routing-boundary"
title: "Robotics Standards Routing Boundary"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
activated_at: "2026-05-03"
activation_notes: "P4-173 landing: robotics standards-depth pack created with PCB-stop lines for ISO 10218, ISO 15066, IEC 62061, ISO 13849, EtherCAT, PROFINET. Promoted to active."
fact_ids:
  - "standards-robotics-standards-depth-boundary"
  - "applications-robotics-coverage-gap-map"
source_ids:
  - "iso-10218-robot-safety-page"
  - "iso-15066-cobot-safety-page"
  - "iec-62061-functional-safety-page"
  - "iso-13849-safety-machinery-page"
  - "ethercat-technology-group-page"
  - "profinet-international-page"
notes: "ISO 10218/15066 are robot safety at system/application level. IEC 62061/ISO 13849 are functional safety at machinery level. EtherCAT/PROFINET are protocols. All use publicly known identity metadata from official ISO/IEC/ETG/PI pages."
tags: ["robotics", "robot", "cobot", "agv", "iso-10218", "iso-15066", "iec-62061", "iso-13849", "ethercat", "profinet", "robot-safety", "functional-safety", "standards-boundary", "routing"]
---

# Definition

> Robotics PCB/PCBA writing can reference ISO 10218, ISO 15066, IEC 62061, ISO 13849, EtherCAT, and PROFINET only at document-identity and scope-framing level. It is unsafe to claim robot safety compliance, cobot safety certification, SIL/PL functional safety, protocol conformance, or robot performance (payload/speed/accuracy/navigation) from these sources alone. Use this page to route which robotics standard vocabulary is supportable and where to stop.

## Why This Topic Matters

- Robotics drafts frequently drift from board-class vocabulary into safety compliance claims: ISO 10218 robot safety, ISO 15066 cobot safety, IEC 62061/ISO 13849 functional safety (SIL/PL), or EtherCAT/PROFINET protocol conformance.
- Trust-bar labels like "Field-Proven", "Deterministic", "Vibration Resistant" in the Tier-2 source are marketing framing, NOT qualification proof.
- Without explicit PCB-stop lines, writers overclaim "certified", "compliant", "safety-rated", or "conformant" for robot controller PCBs, E-stop boards, or cobot controllers.

---

## Standards Context Table

| Standard | Safe Use | Blocked Claims |
|---|---|---|
| **ISO 10218** | Industrial robot safety standard identity; system-level safety vocabulary | "ISO 10218 compliant PCB", robot safety certification at board level |
| **ISO 15066** | Collaborative robot safety identity; cobot/HRC safety vocabulary | "ISO 15066 compliant cobot board", cobot safety certification |
| **IEC 62061** | Machinery SIL functional safety vocabulary; SRECS context | "SIL-ready E-stop board", "SIL-2/SIL-3 safety PCB", SIL at PCB level |
| **ISO 13849** | Safety control PL vocabulary; SRP/CS context | "PL-d/PL-e safety controller", PL certification at bare PCB level |
| **EtherCAT** | Industrial Ethernet protocol identity; robot comms vocabulary | Conformance, certification, interoperability proof |
| **PROFINET** | Industrial Ethernet protocol identity; robot comms vocabulary | Conformance, PI certification, interoperability proof |

---

## PCB Stop Lines by Standard

### ISO 10218 Stop Line

**Safe angles:**
- "ISO 10218 industrial robot safety standard context"
- "Robot safety vocabulary at system/integration level"

**Blocked:**
- "ISO 10218 compliant robot controller PCB"
- "Robot safety certified board" or "ISO 10218 approved PCBA"
- E-stop or safety circuit compliance claims at PCB level

> **Stop:** ISO 10218 specifies robot safety at system/integration level. It does NOT certify robot controller PCBs or safety circuits. Keep ISO 10218 at system-safety context only.

---

### ISO 15066 Stop Line

**Safe angles:**
- "ISO 15066 collaborative robot (cobot) safety technical specification"
- "Human-robot collaboration (HRC) safety vocabulary"

**Blocked:**
- "ISO 15066 compliant cobot controller board"
- "Cobot safety certified PCBA" or "collaborative safety compliant"
- Collaborative workspace safety function proof at PCB level

> **Stop:** ISO 15066 specifies cobot safety at application/workspace level. It does NOT certify cobot controller PCBs. Keep ISO 15066 at cobot-safety context only.

---

### IEC 62061 Stop Line

**Safe angles:**
- "IEC 62061 machinery functional safety vocabulary (SIL-based)"
- "Safety-related electrical control systems (SRECS) context"

**Blocked:**
- "SIL-ready E-stop board" or "SIL-2/SIL-3 safety PCB"
- SIL allocation or compliance at PCB level
- "Functional safety certified" manufacturing claims

> **Stop:** IEC 62061 is machinery/system-level functional safety. PCB manufacturing for customer-designed safety architectures is manufacturing support — NOT SIL certification. Keep SIL language at SRECS system level only.

---

### ISO 13849 Stop Line

**Safe angles:**
- "ISO 13849 safety control systems vocabulary (PL-based)"
- "Safety-related parts of control systems (SRP/CS) context"

**Blocked:**
- "PL-d/PL-e safety controller PCBA" or "PL-ready safety board"
- PL allocation or certification at bare PCB level
- "Safety-certified controller" without system-level evidence

> **Stop:** ISO 13849 is system/component-level safety with PL. PCB manufacturing for customer-designed safety controllers is manufacturing support — NOT PL certification. Keep PL language at SRP/CS level only.

---

### EtherCAT Stop Line

**Safe angles:**
- "EtherCAT industrial Ethernet protocol identity"
- "Fieldbus communication vocabulary for robot controllers"

**Blocked:**
- "EtherCAT compliant robot controller" or "EtherCAT certified board"
- Conformance, interoperability, or device approval claims
- "EtherCAT tested" without explicit ETG certification

> **Stop:** EtherCAT is an industrial Ethernet protocol. Protocol name on a robot controller PCB is NOT conformance proof. Keep EtherCAT at protocol-identity only.

---

### PROFINET Stop Line

**Safe angles:**
- "PROFINET industrial Ethernet protocol identity"
- "PI (PROFIBUS & PROFINET International) technology vocabulary"

**Blocked:**
- "PROFINET compliant robot controller" or "PI certified board"
- Conformance, interoperability, or device approval claims
- "PROFINET tested" without PI certification

> **Stop:** PROFINET is an industrial Ethernet protocol from PI. Protocol name is NOT PI certification. Keep PROFINET at protocol-identity only.

---

## Routing Table: Where Standards Vocabulary Is Safe

| Content Type | Route To |
|---|---|
| ISO 10218 robot safety context | Keep at system/integration level; do not claim PCB compliance |
| ISO 15066 cobot safety context | Keep at application/workspace level; do not claim board certification |
| IEC 62061 SIL functional safety | Keep at SRECS machinery level; manufacturing support ≠ SIL certification |
| ISO 13849 PL safety control | Keep at SRP/CS level; manufacturing support ≠ PL certification |
| EtherCAT/PROFINET protocol | Keep at identity level; do not claim conformance |
| Robotics board family routing | `wiki/applications/robotics-agv-cobot-pcb-pcba-boundary-map.md` |
| Industrial control overlap | `wiki/applications/industrial-control-pcb-pcba-boundary-map.md` |
| DFM/DFT review gates | `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md` |
| Test vs reliability boundary | `facts/methods/pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary.md` |
| Robotics coverage gaps | `facts/applications/robotics-coverage-gap-map.md` |

---

## Common Misreadings

| Misreading | Correction |
|---|---|
| "ISO 10218 compliant robot controller" → | Robot safety is system-level. Safe: "board for robot controller applications." |
| "ISO 15066 cobot safety certified" → | Cobot safety is application-level. Safe: "board for cobot controller applications." |
| "SIL-2 E-stop board" → | SIL is machinery level; PCB is manufacturing support. Safe: "E-stop circuit board (customer design basis)." |
| "PL-e safety controller PCBA" → | PL is system level; PCB is manufacturing support. Safe: "safety controller board (customer design basis)." |
| "EtherCAT compliant robot controller" → | Conformance requires testing. Safe: "EtherCAT protocol interface identity." |
| "PROFINET certified cobot controller" → | Certification requires PI testing. Safe: "PROFINET protocol interface identity." |
| "Field-proven robot board" → | Marketing label. Safe: "industrial-grade design considerations." |
| "Deterministic robot controller" → | Performance claim. Safe: "real-time control context (design-dependent)." |

---

## Must Refresh Before Publishing

- Any ISO 10218 robot safety compliance or certification claim
- Any ISO 15066 cobot safety compliance claim
- Any IEC 62061 SIL allocation or compliance claim
- Any ISO 13849 PL allocation or safety certification claim
- Any EtherCAT conformance, interoperability, or certification claim
- Any PROFINET conformance, PI certification, or interoperability claim
- Any robot payload, speed, accuracy, repeatability performance claim
- Any AGV/AMR navigation accuracy, obstacle avoidance, or fleet routing claim
- Any 24/7 uptime, MTBF, DPPM, or field-reliability claim

---

## Cross-Lane Routing

| Content Type | Route To |
|---|---|
| Robotics board families (7 families) | `wiki/applications/robotics-agv-cobot-pcb-pcba-boundary-map.md` |
| Industrial control overlap (servo, IO, fieldbus) | `wiki/applications/industrial-control-pcb-pcba-boundary-map.md` |
| Industrial control standards (IEC 62061, ISO 13849, EtherCAT, PROFINET) | `wiki/applications/industrial-control-standards-routing-boundary.md` |
| Automotive/EV overlap (BMS, motor control) | `wiki/applications/automotive-ev-pcb-pcba-boundary-map.md` |
| Sensor/navigation overlap (LiDAR, radar) | `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md` |
| DFM/DFT review gates | `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md` |
| Flying probe vs ICT | `facts/methods/pcba-flying-probe-vs-ict-selection-posture.md` |
| Test vs reliability boundary | `facts/methods/pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary.md` |
| Robotics coverage gaps | `facts/applications/robotics-coverage-gap-map.md` |

---

## Related Pages

- `facts/standards/robotics-standards-depth-boundary.md` — Fact card with PCB stop lines
- `wiki/applications/robotics-agv-cobot-pcb-pcba-boundary-map.md` — Active application boundary for 7 board families
- `facts/applications/robotics-coverage-gap-map.md` — Coverage map with residual gaps
