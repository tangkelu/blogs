---
fact_id: "standards-industrial-control-standards-depth-boundary"
title: "Industrial control standards (IEC 61131, IEC 62061, ISO 13849, EtherCAT, PROFINET, IEC 61000, CISPR 11) are PLC programming, functional safety, fieldbus, and EMC boundaries — not PCB compliance or qualification proof"
topic: "Industrial control standards identity and PCB boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "iec-61131-plc-programming-page"
  - "iec-62061-functional-safety-page"
  - "iso-13849-safety-machinery-page"
  - "ethercat-technology-group-page"
  - "profinet-international-page"
  - "iec-61000-emc-page"
  - "cispr-11-ism-equipment-page"
notes: "All standards use publicly known identity metadata from official IEC/ISO/protocol organization pages. No clause-level text or conformance proof. IEC 61131 is PLC programming standard; IEC 62061/ISO 13849 are machinery functional safety (SIL/PL); EtherCAT/PROFINET are industrial Ethernet protocols; IEC 61000/CISPR 11 are EMC standards."
tags: ["industrial-control", "iec-61131", "iec-62061", "iso-13849", "ethercat", "profinet", "iec-61000", "cispr-11", "plc", "functional-safety", "fieldbus", "emc", "qualification-boundary"]
---

# Canonical Summary

> Industrial control standards operate at distinct governance layers — none create PCB-level certification, compliance, or qualification status. IEC 61131 is a PLC programming standard; IEC 62061 is machinery functional safety with SIL approach; ISO 13849 is machinery safety control systems with PL approach; EtherCAT and PROFINET are industrial Ethernet protocols; IEC 61000 and CISPR 11 are EMC standards. Mentioning these in PCB/PCBA content is safe only at document-identity and scope-framing level. All PLC programming compliance, SIL/PL safety certification, protocol conformance, and EMC compliance claims are blocked.

## Industrial Control Standard Families

### IEC 61131 — Programmable Controllers (PLC)

**Governance Layer:** PLC programming model, languages, and functional specifications

**PCB Boundary:**
- Safe: PLC control board identity, modular PLC format vocabulary, industrial control context
- Blocked: IEC 61131 programming compliance, instruction set implementation, certification claims

**PCB Stop Line:** IEC 61131 specifies PLC programming models and languages. It does NOT certify a PCB, PCBA, or supplier for PLC implementation. Do not claim "IEC 61131 compliant PCB" or "IEC 61131 certified control board."

---

### IEC 62061 — Safety of Machinery (SIL Approach)

**Governance Layer:** Functional safety of machinery with Safety Integrity Level (SIL)

**PCB Boundary:**
- Safe: Machinery functional-safety vocabulary context, SIL terminology at system level
- Blocked: SIL allocation at PCB level, SIL compliance proof, safety system implementation claims

**PCB Stop Line:** IEC 62061 specifies safety-related electrical control systems (SRECS) with SIL. It is system-level functional safety, not PCB-level safety certification. Do not claim "SIL-ready PCB" or "SIL-2/SIL-3 compliant board."

---

### ISO 13849 — Safety of Control Systems (PL Approach)

**Governance Layer:** Safety-related parts of control systems with Performance Level (PL)

**PCB Boundary:**
- Safe: Machinery safety control vocabulary context, PL terminology at system level
- Blocked: PL allocation at PCB level, PL compliance proof, safety controller certification

**PCB Stop Line:** ISO 13849 specifies PL for safety-related parts of control systems (SRP/CS). It is system/component safety level, not bare PCB or PCBA qualification. Do not claim "PL-d/PL-e PCB" or "safety-certified board."

---

### EtherCAT — Industrial Ethernet Protocol

**Governance Layer:** Industrial Ethernet fieldbus protocol specification

**PCB Boundary:**
- Safe: EtherCAT protocol identity, industrial Ethernet fieldbus vocabulary
- Blocked: EtherCAT conformance, protocol certification, interoperability proof, device approval

**PCB Stop Line:** EtherCAT is an industrial Ethernet protocol. Protocol identity on a board is NOT conformance proof. Do not claim "EtherCAT compliant", "conformance tested", or "interoperability guaranteed."

---

### PROFINET — Industrial Ethernet Protocol

**Governance Layer:** Industrial Ethernet protocol based on PROFIBUS

**PCB Boundary:**
- Safe: PROFINET protocol identity, industrial Ethernet fieldbus vocabulary
- Blocked: PROFINET conformance, protocol certification, interoperability proof, device approval

**PCB Stop Line:** PROFINET is an industrial Ethernet protocol from PROFIBUS & PROFINET International (PI). Protocol identity is NOT conformance. Do not claim "PROFINET compliant" or "PI-certified board."

---

### IEC 61000 — Electromagnetic Compatibility

**Governance Layer:** EMC immunity and emission requirements for electrical/electronic equipment

**PCB Boundary:**
- Safe: EMC standard-family identity, electromagnetic compatibility vocabulary context
- Blocked: EMC compliance proof, immunity/emission pass-fail, test level claims, certification

**PCB Stop Line:** IEC 61000 specifies EMC requirements and test methods. Compliance requires testing. Do not claim "IEC 61000 compliant", "EMC certified", or immunity/emission pass-status without test evidence.

---

### CISPR 11 — ISM Equipment EMC

**Governance Layer:** Radio disturbance characteristics for industrial, scientific, medical (ISM) equipment

**PCB Boundary:**
- Safe: ISM equipment EMC vocabulary, industrial EMC context
- Blocked: CISPR 11 compliance proof, emission pass-fail, Group/Class classification claims

**PCB Stop Line:** CISPR 11 specifies limits and measurement methods for ISM equipment radio disturbance. Compliance requires testing. Do not claim "CISPR 11 compliant", "Class A/B certified", or emission pass-status without test evidence.

---

## Cross-Standard Safe Vocabulary

The following angles are safe across all industrial control standards:

| Vocabulary Type | Safe Usage |
|---|---|
| Standard names | IEC 61131, IEC 62061, ISO 13849, EtherCAT, PROFINET, IEC 61000, CISPR 11 as document/identifier names |
| Document families | "IEC 61131 standard family", "industrial Ethernet protocols", "IEC 61000 EMC series" |
| Scope framing | "PLC programming context", "machinery functional safety vocabulary", "fieldbus protocol identity", "industrial EMC standards" |
| Process context | "industrial automation practice", "control system design considerations" |

## Common Misreadings to Block

| Misreading | Why It's Blocked |
|---|---|
| "IEC 61131 compliant PLC board" | IEC 61131 is programming model, not PCB manufacturing compliance |
| "SIL-ready PCB" or "SIL-2 capable board" | SIL is system-level functional safety (IEC 62061), not PCB rating |
| "PL-d/PL-e safety board" | PL is system/component safety (ISO 13849), not bare PCB qualification |
| "EtherCAT compliant design" | Compliance requires conformance testing, not just protocol naming |
| "PROFINET certified board" | Certification requires PI testing, not protocol vocabulary |
| "IEC 61000 EMC compliant" | Compliance requires test evidence, not design intent |
| "CISPR 11 Class A certified" | Certification requires testing and classification evidence |
| "Functional safety certified PCBA" | Safety certification is system-level with SIL/PL, not board-level |
| "24/7 reliable industrial board" | Reliability/uptime requires field evidence, not standards vocabulary |

## Related Fact Cards

- `facts/applications/industrial-control-coverage-gap-map.md` — Application coverage for 6 board families
- `wiki/applications/industrial-control-pcb-pcba-boundary-map.md` — Active routing boundary for industrial control PCB content
- `facts/methods/industrial-robotics-control-review-gates-and-claim-boundary.md` — DFM/DFT review gates

## Source Links

- https://www.iec.ch/dyn/www/f?p=103:38:0::::FSP_ORG_ID:1363 (IEC 61131, IEC 62061, IEC 61000)
- https://www.iso.org/standard/69834.html (ISO 13849)
- https://www.ethercat.org/en/technology.html (EtherCAT)
- https://www.profibus.com/technology/profinet (PROFINET)
- https://www.iec.ch/dyn/www/f?p=103:38:0::::FSP_ORG_ID:1363 (CISPR 11)
