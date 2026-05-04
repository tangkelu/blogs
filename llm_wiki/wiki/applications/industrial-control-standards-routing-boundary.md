---
topic_id: "applications-industrial-control-standards-routing-boundary"
title: "Industrial Control Standards Routing Boundary"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
activated_at: "2026-05-03"
activation_notes: "P4-171 landing: industrial-control standards-depth pack created with PCB-stop lines for IEC 61131, IEC 62061, ISO 13849, EtherCAT, PROFINET, IEC 61000, CISPR 11. Promoted to active."
fact_ids:
  - "standards-industrial-control-standards-depth-boundary"
  - "applications-industrial-control-coverage-gap-map"
source_ids:
  - "iec-61131-plc-programming-page"
  - "iec-62061-functional-safety-page"
  - "iso-13849-safety-machinery-page"
  - "ethercat-technology-group-page"
  - "profinet-international-page"
  - "iec-61000-emc-page"
  - "cispr-11-ism-equipment-page"
notes: "All standards use publicly known identity metadata from official IEC/ISO/protocol organization pages. No clause-level text or conformance proof."
tags: ["industrial-control", "iec-61131", "iec-62061", "iso-13849", "ethercat", "profinet", "iec-61000", "cispr-11", "plc", "functional-safety", "fieldbus", "emc", "standards-boundary", "routing"]
---

# Definition

> Industrial control PCB/PCBA writing can reference IEC 61131, IEC 62061, ISO 13849, EtherCAT, PROFINET, IEC 61000, and CISPR 11 only at document-identity and scope-framing level. It is unsafe to claim PLC programming compliance, SIL/PL safety certification, protocol conformance, EMC compliance, or 24/7 uptime from these sources alone. Use this page to route which industrial control standard vocabulary is supportable and where to stop.

## Why This Topic Matters

- Industrial control drafts frequently drift from board-class vocabulary into PLC programming claims (IEC 61131), functional-safety certification (SIL/PL), protocol compliance (EtherCAT/PROFINET), or EMC compliance (IEC 61000/CISPR 11).
- The Tier-2 internal source and official standards/protocol pages support identity-level vocabulary but not qualification or conformance proof.
- Without explicit PCB-stop lines, writers overclaim "compliant", "certified", "conformant", or "approved" for boards, PCBAs, materials, or suppliers.

---

## Standards Context Table

| Standard | Safe Use | Blocked Claims |
|---|---|---|
| **IEC 61131** | PLC programming standard identity; modular PLC board format vocabulary | Programming compliance, instruction set implementation, "IEC 61131 certified PCB" |
| **IEC 62061** | Machinery functional safety vocabulary (SIL context); SRECS system level | SIL allocation at PCB level, "SIL-ready board", safety case claims |
| **ISO 13849** | Machinery safety control vocabulary (PL context); SRP/CS system level | PL allocation at PCB level, "PL-d/PL-e board", safety certification |
| **EtherCAT** | Industrial Ethernet protocol identity; fieldbus vocabulary | Conformance, certification, interoperability proof, "EtherCAT compliant" |
| **PROFINET** | Industrial Ethernet protocol identity; PI technology vocabulary | Conformance, certification, interoperability proof, "PI certified" |
| **IEC 61000** | EMC standard-family identity; immunity/emission vocabulary | EMC compliance proof, pass/fail outcomes, "EMC certified" |
| **CISPR 11** | ISM equipment EMC identity; radio disturbance vocabulary | CISPR compliance proof, emission pass/fail, "Class A/B certified" |

---

## PCB Stop Lines by Standard

### IEC 61131 Stop Line

**Safe angles:**
- "IEC 61131 provides PLC programming standard context"
- "Modular PLC board format: CPU, IO cards, communication modules"

**Blocked:**
- "IEC 61131 compliant PLC board"
- "IEC 61131 programming implementation"
- PLC instruction set or certification claims

> **Stop:** IEC 61131 is a PLC programming model standard. It does not certify PCBs or PCBAs for PLC implementation. Keep IEC 61131 at programming-context level only.

---

### IEC 62061 Stop Line

**Safe angles:**
- "IEC 62061 machinery functional safety vocabulary (SIL-based)"
- "Safety-related electrical control systems (SRECS) context"

**Blocked:**
- "SIL-ready PCB" or "SIL-2/SIL-3 capable board"
- SIL allocation at PCB level
- Functional safety compliance or certification claims

> **Stop:** IEC 62061 is system-level functional safety with SIL. It does not allocate SIL to bare PCBs. Keep SIL language at SRECS system level only.

---

### ISO 13849 Stop Line

**Safe angles:**
- "ISO 13849 machinery safety control vocabulary (PL-based)"
- "Safety-related parts of control systems (SRP/CS) context"

**Blocked:**
- "PL-d/PL-e safety board" or "PL-ready PCBA"
- PL allocation at bare PCB level
- Safety controller certification claims

> **Stop:** ISO 13849 is system/component safety with PL. It does not qualify bare PCBs or PCBAs. Keep PL language at SRP/CS level only.

---

### EtherCAT Stop Line

**Safe angles:**
- "EtherCAT industrial Ethernet protocol identity"
- "Fieldbus communication vocabulary for industrial automation"

**Blocked:**
- "EtherCAT compliant" or "EtherCAT certified"
- Conformance, interoperability, or device approval claims
- "EtherCAT tested" without explicit test evidence

> **Stop:** EtherCAT is an industrial Ethernet protocol. Protocol name on a board is NOT conformance proof. Keep EtherCAT at identity vocabulary only.

---

### PROFINET Stop Line

**Safe angles:**
- "PROFINET industrial Ethernet protocol identity"
- "PI (PROFIBUS & PROFINET International) technology vocabulary"

**Blocked:**
- "PROFINET compliant" or "PI certified board"
- Conformance, interoperability, or device approval claims
- "PROFINET tested" without PI certification

> **Stop:** PROFINET is an industrial Ethernet protocol from PI. Protocol name is NOT PI certification. Keep PROFINET at identity vocabulary only.

---

### IEC 61000 Stop Line

**Safe angles:**
- "IEC 61000 EMC standard-family identity"
- "Electromagnetic compatibility vocabulary context"

**Blocked:**
- "IEC 61000 EMC compliant" or "EMC certified"
- Immunity/emission pass/fail claims without test evidence
- Specific test level claims (volts/meter, surge levels)

> **Stop:** IEC 61000 specifies EMC requirements and test methods. Compliance requires testing. Keep IEC 61000 at EMC-framing level only.

---

### CISPR 11 Stop Line

**Safe angles:**
- "CISPR 11 ISM equipment EMC standard identity"
- "Industrial radio disturbance characteristics vocabulary"

**Blocked:**
- "CISPR 11 compliant" or "Class A/B certified"
- Emission pass/fail claims without test evidence
- Group/Class classification claims (Group 1/2, Class A/B)

> **Stop:** CISPR 11 specifies limits and methods for ISM equipment radio disturbance. Compliance requires testing. Keep CISPR 11 at standard-identity level only.

---

## Routing Table: Where Standards Vocabulary Is Safe

| Content Type | Route To |
|---|---|
| PLC programming standard context | Keep at IEC 61131 identity level; do not claim PCB compliance |
| Machinery functional safety (SIL) | Keep at SRECS system level (IEC 62061); do not allocate to PCB |
| Machinery safety control (PL) | Keep at SRP/CS level (ISO 13849); do not allocate to bare PCB |
| EtherCAT fieldbus identity | Keep at protocol identity; do not claim conformance |
| PROFINET fieldbus identity | Keep at protocol identity; do not claim PI certification |
| Industrial EMC standards | Keep at EMC vocabulary level; do not claim compliance |
| Industrial control board family routing | `wiki/applications/industrial-control-pcb-pcba-boundary-map.md` |
| DFM/DFT review gates | `facts/methods/industrial-robotics-control-review-gates-and-claim-boundary.md` |
| Test/inspection boundaries | `facts/methods/pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary.md` |
| Robotics safety protocols | `wiki/applications/robotics-agv-cobot-pcb-pcba-boundary-map.md` |

---

## Common Misreadings

| Misreading | Correction |
|---|---|
| "IEC 61131 compliant PLC board" → | IEC 61131 is programming model. Safe: "board for PLC applications." |
| "SIL-ready board" or "SIL-2 capable PCBA" → | SIL is system-level (IEC 62061). Safe: "board for industrial control applications." |
| "PL-d/PL-e safety PCB" → | PL is system/component safety (ISO 13849). Safe: "board for safety controller applications (customer design basis)." |
| "EtherCAT compliant design" → | Conformance requires testing. Safe: "EtherCAT fieldbus interface identity." |
| "PROFINET certified board" → | Certification requires PI testing. Safe: "PROFINET protocol identity." |
| "IEC 61000 EMC compliant" → | Compliance requires test evidence. Safe: "industrial EMC context." |
| "CISPR 11 Class A certified" → | Classification requires testing. Safe: "ISM equipment EMC context." |
| "Functional safety certified PCBA" → | Safety certification is system-level. Safe: "board manufactured to support customer-designed safety systems." |
| "24/7 reliable industrial board" → | Reliability requires field evidence. Safe: "industrial-grade design considerations." |

---

## Must Refresh Before Publishing

- Any IEC 61131 programming compliance or certification claim
- Any IEC 62061 SIL allocation or compliance claim
- Any ISO 13849 PL allocation or safety certification claim
- Any EtherCAT conformance, interoperability, or certification claim
- Any PROFINET conformance, PI certification, or interoperability claim
- Any IEC 61000 EMC compliance or pass-status claim
- Any CISPR 11 compliance, emission pass, or classification claim
- Any 24/7 uptime, MTBF, DPPM, or field-reliability claim
- Any fieldbus protocol interoperability or integration-test claim

---

## Cross-Lane Routing

| Content Type | Route To |
|---|---|
| Industrial control board families (6 families) | `wiki/applications/industrial-control-pcb-pcba-boundary-map.md` |
| Robotics/AGV safety protocols | `wiki/applications/robotics-agv-cobot-pcb-pcba-boundary-map.md` |
| Sensor/field sensor front-end | `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md` |
| DFM/DFT/DFA review gates | `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md` |
| Flying probe vs ICT | `facts/methods/pcba-flying-probe-vs-ict-selection-posture.md` |
| Test vs reliability boundary | `facts/methods/pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary.md` |
| Industrial control coverage gaps | `facts/applications/industrial-control-coverage-gap-map.md` |

---

## Related Pages

- `facts/standards/industrial-control-standards-depth-boundary.md` — Fact card with PCB stop lines
- `wiki/applications/industrial-control-pcb-pcba-boundary-map.md` — Active application boundary for 6 board families
- `facts/applications/industrial-control-coverage-gap-map.md` — Coverage map with residual gaps
