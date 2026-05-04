---
fact_id: "standards-automotive-ev-standards-depth-boundary"
title: "Automotive and EV standards (ISO 26262, IATF 16949, AEC-Q, CISPR 25, ISO 11452) are system / component / EMC boundaries, not PCB qualification proof"
topic: "Automotive and EV standards identity and PCB boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "iso-26262-road-vehicles-functional-safety-package"
  - "iatf-16949-overview-page"
  - "aec-documents-page"
  - "cispr-25-vehicles-emc-page"
  - "iso-11452-road-vehicles-emc-immunity-page"
notes: "CISPR 25 and ISO 11452 EMC standards use publicly known identity metadata — official IEC/ISO source pages confirm standard-family scope only, no clause-level text. AEC-Q remains component-qualification document-family, not PCB qualification. ISO 26262 is functional-safety system lifecycle, not PCB ASIL allocation. IATF 16949 is organization QMS, not supplier certificate proof."
tags: ["automotive", "ev", "iso-26262", "iatf-16949", "aec-q", "cispr-25", "iso-11452", "emc", "functional-safety", "qualification-boundary"]
---

# Canonical Summary

> Automotive and EV standards operate at distinct governance layers — none create PCB-level certification, qualification, or authorization status. ISO 26262 is a functional-safety lifecycle standard for road-vehicle E/E systems; IATF 16949 is an automotive QMS standard for organizations; AEC-Q is a component-qualification document family; CISPR 25 and ISO 11452 are EMC standards for vehicles and components. Mentioning these in PCB/PCBA content is safe only at document-identity and scope-framing level. All ASIL allocation, QMS certification, component qualification, and EMC compliance claims are blocked.

## Automotive Standard Families

### ISO 26262 — Road Vehicle Functional Safety

**Governance Layer:** System / software lifecycle for road-vehicle electrical/electronic systems

**PCB Boundary:**
- Safe: Document identity, functional-safety vocabulary context, system-lifecycle framing
- Blocked: ASIL allocation (ASIL-A through ASIL-D), PCB ASIL rating, compliance proof, safety-case evidence

**PCB Stop Line:** ISO 26262 supports system-level E/E functional-safety lifecycle language. It does NOT qualify a PCB, PCBA, material, or supplier for automotive use. Do not claim "ISO 26262 compliant PCB manufacturing" or ASIL-ready boards.

---

### IATF 16949 — Automotive Quality Management System

**Governance Layer:** Organization-level QMS for automotive supply chain

**PCB Boundary:**
- Safe: QMS vocabulary, automotive supplier-system context, standard-family identity
- Blocked: Certification status, certificate validity, scope of certification, PPAP completion, OEM approval

**PCB Stop Line:** IATF 16949 is an organization QMS standard, not a product or PCB qualification. Mentioning IATF is safe for supplier-system framing only. Do not use to prove a PCB, PCBA, lot, or material is automotive-grade, qualified, or released.

---

### AEC-Q — Automotive Electronic Component Qualification

**Governance Layer:** Component-level qualification documents (AEC-Q100, Q101, Q200, etc.)

**PCB Boundary:**
- Safe: Document-family identity, component-qualification vocabulary context, AEC discovery
- Blocked: PCB qualification, PCBA qualification, supplier qualification, lot-level pass/fail, specific test outcomes

**PCB Stop Line:** AEC-Q documents qualify electronic components (ICs, discretes, passives) for automotive use. They do NOT qualify bare PCBs, PCBAs, or materials. Do not claim "AEC-Q PCB" or "AEC-Q qualified PCBA" from the document hub alone.

---

### CISPR 25 — Vehicles, Boats, Internal Combustion Engines EMC

**Governance Layer:** Vehicle and component EMC emission limits and measurement methods

**PCB Boundary:**
- Safe: Standard-family identity, automotive EMC vocabulary context, emission/immunity framing
- Blocked: EMC compliance proof, emission pass/fail, immunity pass/fail, test lot outcomes, supplier EMC qualification

**PCB Stop Line:** CISPR 25 provides radio disturbance limits and test methods for vehicles and components. Mentioning CISPR 25 is safe for EMC context framing. Do not claim CISPR 25 compliance, EMC pass-status, or supplier qualification without test evidence.

---

### ISO 11452 — Road Vehicles Component Immunity Testing

**Governance Layer:** Component test methods for narrowband radiated electromagnetic immunity

**PCB Boundary:**
- Safe: Standard-family identity, immunity-test vocabulary context, component-EMC framing
- Blocked: Immunity compliance proof, test pass/fail, specific test levels, supplier qualification

**PCB Stop Line:** ISO 11452 specifies test methods for component immunity to narrowband radiated energy. Safe for test-method context only. Do not claim ISO 11452 compliance, immunity pass-status, or qualification without documented test evidence.

---

## Cross-Standard Safe Vocabulary

The following angles are safe across all automotive standards:

| Vocabulary Type | Safe Usage |
|---|---|
| Standard names | ISO 26262, IATF 16949, AEC-Q, CISPR 25, ISO 11452 as document identifiers |
| Document families | "AEC-Q document family", "ISO 11452 series", "CISPR 25 standard" |
| Scope framing | "functional safety context", "automotive QMS framing", "component qualification documents", "automotive EMC standards" |
| Process context | "automotive industry practice", "supplier quality expectations" |

## Common Misreadings to Block

| Misreading | Why It's Blocked |
|---|---|
| "ISO 26262 compliant PCB" | ISO 26262 is system lifecycle, not PCB manufacturing compliance |
| "ASIL-ready board" | ASIL allocation is system/software level, not PCB level |
| "IATF 16949 certified PCB" | IATF is organization QMS, not product certification |
| "AEC-Q PCB" | AEC-Q is component qualification, not bare PCB or PCBA |
| "CISPR 25 compliant design" | Compliance requires testing evidence, not design intent alone |
| "ISO 11452 immune" | Immunity is tested and proven, not inherent in design |
| "PPAP-approved board" | PPAP is customer-specific approval, not generic PCB claim |
| "OEM-grade manufacturing" | OEM approval is program-specific, not supplier capability proof |

## Related Fact Cards

- `facts/applications/automotive-ev-coverage-gap-map.md` — Application coverage for 7 automotive board families
- `wiki/applications/automotive-ev-pcb-pcba-boundary-map.md` — Active routing boundary for automotive/EV PCB content
- `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md` — Cross-application qualification boundaries

## Source Links

- https://www.iso.org/publication/PUB200262.html (ISO 26262)
- https://www.iatfglobaloversight.org/iatf-16949/ (IATF 16949)
- https://www.aecouncil.com/AECDocuments.html (AEC-Q)
- https://www.iec.ch/dyn/www/f?p=103:38:0::::FSP_ORG_ID:1363 (CISPR 25)
- https://www.iso.org/standard/61357.html (ISO 11452)
