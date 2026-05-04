---
fact_id: "standards-robotics-standards-depth-boundary"
title: "Robotics standards (ISO 10218, ISO 15066, IEC 62061, ISO 13849, EtherCAT, PROFINET) are robot safety, functional safety, and fieldbus boundaries — not PCB compliance or performance proof"
topic: "Robotics standards identity and PCB boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "iso-10218-robot-safety-page"
  - "iso-15066-cobot-safety-page"
  - "iec-62061-functional-safety-page"
  - "iso-13849-safety-machinery-page"
  - "ethercat-technology-group-page"
  - "profinet-international-page"
notes: "ISO 10218/15066 are robot safety standards at system/application level. IEC 62061/ISO 13849 are functional safety (SIL/PL) at machinery/system level. EtherCAT/PROFINET are industrial Ethernet protocols. All use publicly known identity metadata from official ISO/IEC/protocol organization pages. No PCB-level safety certification or protocol conformance proof."
tags: ["robotics", "robot", "cobot", "agv", "iso-10218", "iso-15066", "iec-62061", "iso-13849", "ethercat", "profinet", "robot-safety", "functional-safety", "fieldbus", "qualification-boundary"]
---

# Canonical Summary

> Robotics standards operate at distinct governance layers — none create PCB-level certification, safety compliance, or qualification status. ISO 10218 is industrial robot safety at system level; ISO 15066 is collaborative robot (cobot) safety at application level; IEC 62061 is machinery functional safety with SIL approach; ISO 13849 is safety control systems with PL approach; EtherCAT and PROFINET are industrial Ethernet fieldbus protocols. Mentioning these in PCB/PCBA content is safe only at document-identity and scope-framing level. All robot safety compliance, SIL/PL functional safety certification, protocol conformance, and performance claims are blocked.

## Robotics Standard Families

### ISO 10218 — Industrial Robot Safety

**Governance Layer:** Robot arm and robot system/integration safety requirements

**PCB Boundary:**
- Safe: Robot safety standard-family identity, industrial robot safety vocabulary context
- Blocked: Robot safety compliance at PCB level, E-stop/safety circuit certification, "ISO 10218 compliant board"

**PCB Stop Line:** ISO 10218 specifies safety requirements for industrial robots and robotic devices at system/integration level. It does NOT certify PCBs, E-stop circuits, or safety controllers. Do not claim "ISO 10218 compliant PCB" or "robot safety certified board."

---

### ISO 15066 — Collaborative Robot (Cobot) Safety

**Governance Layer:** Collaborative robot safety for human-robot collaboration (HRC)

**PCB Boundary:**
- Safe: Cobot safety standard-family identity, collaborative workspace safety vocabulary
- Blocked: Cobot safety compliance at PCB level, collaborative safety function proof, "ISO 15066 compliant cobot board"

**PCB Stop Line:** ISO/TS 15066 specifies safety requirements for collaborative robots at application/workspace level. It does NOT certify cobot controller PCBs or safety systems. Do not claim "ISO 15066 compliant PCB" or "cobot safety certified."

---

### IEC 62061 — Safety of Machinery (SIL Approach)

**Governance Layer:** Functional safety of machinery with Safety Integrity Level (SIL)

**PCB Boundary:**
- Safe: Machinery functional-safety vocabulary context, SIL terminology at system level
- Blocked: SIL allocation at PCB level, "SIL-ready" E-stop board, safety circuit SIL certification

**PCB Stop Line:** IEC 62061 specifies safety-related electrical control systems (SRECS) with SIL at machinery/system level. Safety controller PCBs manufactured for customer-designed architectures are manufacturing support only — NOT SIL certification. Do not claim "SIL-2/SIL-3 safety board" or "SIL-certified E-stop PCB."

---

### ISO 13849 — Safety of Control Systems (PL Approach)

**Governance Layer:** Safety-related parts of control systems with Performance Level (PL)

**PCB Boundary:**
- Safe: Safety control systems vocabulary context, PL terminology at system/component level
- Blocked: PL allocation at bare PCB level, "PL-d/PL-e safety board", safety controller certification

**PCB Stop Line:** ISO 13849 specifies PL for safety-related parts of control systems (SRP/CS). PCB manufacturing for customer-designed safety controllers is manufacturing support — NOT PL certification. Do not claim "PL-e safety PCBA" or "safety-certified controller board."

---

### EtherCAT — Industrial Ethernet Protocol

**Governance Layer:** Industrial Ethernet fieldbus protocol specification

**PCB Boundary:**
- Safe: EtherCAT protocol identity, industrial Ethernet fieldbus vocabulary for robot controller communication
- Blocked: EtherCAT conformance, certification, interoperability proof, "EtherCAT compliant robot controller"

**PCB Stop Line:** EtherCAT is an industrial Ethernet protocol. Protocol identity on a robot controller PCB is NOT conformance proof. Do not claim "EtherCAT compliant", "conformance tested", or "interoperability guaranteed" for robotics boards.

---

### PROFINET — Industrial Ethernet Protocol

**Governance Layer:** Industrial Ethernet protocol based on PROFIBUS

**PCB Boundary:**
- Safe: PROFINET protocol identity, industrial Ethernet fieldbus vocabulary for robot controller communication
- Blocked: PROFINET conformance, PI certification, interoperability proof, "PROFINET certified robot controller"

**PCB Stop Line:** PROFINET is an industrial Ethernet protocol from PI. Protocol identity is NOT conformance. Do not claim "PROFINET compliant" or "PI-certified" for robotics boards.

---

## Cross-Standard Safe Vocabulary

The following angles are safe across all robotics standards:

| Vocabulary Type | Safe Usage |
|---|---|
| Standard names | ISO 10218, ISO 15066, IEC 62061, ISO 13849, EtherCAT, PROFINET as document/protocol identifiers |
| Document families | "robot safety standards", "functional safety standards", "industrial Ethernet protocols" |
| Scope framing | "robot safety context", "collaborative workspace safety", "machinery functional safety vocabulary", "fieldbus protocol identity" |
| Process context | "robotics manufacturing support", "industrial automation practice" |

## Common Misreadings to Block

| Misreading | Why It's Blocked |
|---|---|
| "ISO 10218 compliant robot controller PCB" | Robot safety is system-level, not PCB-level |
| "ISO 15066 cobot safety certified board" | Cobot safety is application-level, not board certification |
| "SIL-ready E-stop board" or "SIL-2 safety PCB" | SIL is system/machinery level; PCB manufacturing ≠ SIL certification |
| "PL-d/PL-e safety controller PCBA" | PL is system/component level; PCB is manufacturing support only |
| "EtherCAT compliant robot controller" | Conformance requires testing, not protocol naming |
| "PROFINET certified cobot controller" | Certification requires PI testing |
| "Safety-certified robot safety circuit" | Safety certification is system-level with evidence |
| "Functional safety compliant PCB manufacturing" | Manufacturing ≠ functional safety compliance |
| "Field-proven robot board" → | Marketing label, not lot-level qualification proof |
| "Deterministic robot controller" → | Performance claim requiring evidence |

## Related Fact Cards

- `facts/applications/robotics-coverage-gap-map.md` — Application coverage for 7 robotics board families
- `wiki/applications/robotics-agv-cobot-pcb-pcba-boundary-map.md` — Active routing boundary for robotics PCB content
- `facts/standards/industrial-control-standards-depth-boundary.md` — Industrial control standards (overlaps with robotics)

## Source Links

- https://www.iso.org/standard/51330.html (ISO 10218)
- https://www.iso.org/standard/62996.html (ISO 15066)
- https://www.iec.ch/dyn/www/f?p=103:38:0::::FSP_ORG_ID:1363 (IEC 62061)
- https://www.iso.org/standard/69834.html (ISO 13849)
- https://www.ethercat.org/en/technology.html (EtherCAT)
- https://www.profibus.com/technology/profinet (PROFINET)
