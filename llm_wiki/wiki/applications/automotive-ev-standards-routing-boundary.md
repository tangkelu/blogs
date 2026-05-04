---
topic_id: "applications-automotive-ev-standards-routing-boundary"
title: "Automotive and EV Standards Routing Boundary"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
activated_at: "2026-05-03"
activation_notes: "P4-170 landing: automotive standards-depth pack created with PCB-stop lines for ISO 26262, IATF 16949, AEC-Q, CISPR 25, ISO 11452. Promoted to active."
fact_ids:
  - "standards-automotive-ev-standards-depth-boundary"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"
  - "applications-automotive-ev-coverage-gap-map"
source_ids:
  - "iso-26262-road-vehicles-functional-safety-package"
  - "iatf-16949-overview-page"
  - "aec-documents-page"
  - "cispr-25-vehicles-emc-page"
  - "iso-11452-road-vehicles-emc-immunity-page"
notes: "CISPR 25 and ISO 11452 use publicly known standards-identity metadata only — official IEC/ISO source pages confirm standard-family scope without clause-level text."
tags: ["automotive", "ev", "iso-26262", "iatf-16949", "aec-q", "cispr-25", "iso-11452", "emc", "standards-boundary", "routing"]
---

# Definition

> Automotive and EV PCB/PCBA writing can reference ISO 26262, IATF 16949, AEC-Q, CISPR 25, and ISO 11452 only at document-identity and scope-framing level. It is unsafe to claim ASIL allocation, QMS certification, component qualification, EMC compliance, or OEM approval from these sources alone. Use this page to route which automotive standard vocabulary is supportable and where to stop.

## Why This Topic Matters

- Automotive drafts frequently drift from board-class vocabulary into functional-safety claims (ASIL), QMS certification (IATF), component qualification (AEC-Q), or EMC compliance (CISPR 25 / ISO 11452).
- The Tier-2 internal source and official standards pages support standard-family identity but not qualification proof.
- Without explicit PCB-stop lines, writers overclaim "compliant", "qualified", "certified", or "approved" for boards, PCBAs, materials, or suppliers.

---

## Standards Context Table

| Standard | Safe Use | Blocked Claims |
|---|---|---|
| **ISO 26262** | Road-vehicle functional-safety vocabulary; system/software lifecycle context | ASIL allocation, PCB ASIL rating, "compliant manufacturing", safety-case evidence |
| **IATF 16949** | Automotive QMS vocabulary; organization-level framing | Certification status, certificate validity, scope, "certified PCB", "approved supplier" |
| **AEC-Q** | Component-qualification document-family identity; discovery context | PCB qualification, PCBA qualification, "AEC-Q board", lot-level pass/fail |
| **CISPR 25** | Automotive EMC standard identity; emission/immunity vocabulary | EMC compliance proof, pass/fail outcomes, "compliant design" without test evidence |
| **ISO 11452** | Component immunity test-method identity; EMC test vocabulary | Immunity compliance, test pass-status, specific test levels, supplier qualification |

---

## PCB Stop Lines by Standard

### ISO 26262 Stop Line

**Safe angles:**
- "ISO 26262 provides functional-safety context for road-vehicle E/E systems"
- "Functional-safety lifecycle framing for automotive ECU development"

**Blocked:**
- "ISO 26262 compliant PCB manufacturing"
- "ASIL-ready board" or "ASIL-D capable PCBA"
- Any ASIL allocation (ASIL-A through ASIL-D) at PCB level

> **Stop:** ISO 26262 is a system/software lifecycle standard. It does not allocate ASIL to PCBs, materials, or suppliers. Keep ISO 26262 language at system-context level only.

---

### IATF 16949 Stop Line

**Safe angles:**
- "IATF 16949 provides automotive QMS context"
- "Supplier quality-system expectations in automotive supply chain"

**Blocked:**
- "IATF 16949 certified PCB" or "certified PCBA"
- "IATF-approved supplier" or "IATF-compliant manufacturing"
- Certificate validity, scope, or expiration claims

> **Stop:** IATF 16949 certifies organization QMS, not products or PCBs. Keep IATF language at organization/system framing only.

---

### AEC-Q Stop Line

**Safe angles:**
- "AEC-Q document family for automotive electronic component qualification"
- "Component-qualification vocabulary context"

**Blocked:**
- "AEC-Q PCB" or "AEC-Q qualified board"
- "AEC-Q PCBA" or "AEC-Q assembly"
- Lot-level qualification proof or pass-status

> **Stop:** AEC-Q qualifies electronic components (ICs, discretes, passives). It does not qualify bare PCBs, PCBAs, or materials. Keep AEC-Q at component-qualification scope only.

---

### CISPR 25 Stop Line

**Safe angles:**
- "CISPR 25 automotive EMC standard for vehicles and components"
- "Radio disturbance characteristics and limits vocabulary"

**Blocked:**
- "CISPR 25 compliant PCB" or "CISPR 25 compliant design"
- Emission pass/fail claims without test evidence
- "EMC-certified board" or "EMC-ready PCBA"

> **Stop:** CISPR 25 provides limits and measurement methods. Compliance requires actual testing. Keep CISPR 25 at standard-identity and EMC-framing level only.

---

### ISO 11452 Stop Line

**Safe angles:**
- "ISO 11452 component immunity test methods for narrowband radiated energy"
- "Immunity testing vocabulary for road-vehicle components"

**Blocked:**
- "ISO 11452 immune" or "immune to narrowband radiation"
- Test pass/fail claims without documented evidence
- Specific test level claims (volts/meter, frequency ranges)

> **Stop:** ISO 11452 specifies test methods. Immunity is proven through testing, not inherent in design. Keep ISO 11452 at test-method context only.

---

## Routing Table: Where Standards Vocabulary Is Safe

| Content Type | Route To |
|---|---|
| ISO 26262 system-level functional safety | Keep at system/software lifecycle context; do not route to PCB manufacturing |
| IATF 16949 supplier QMS | Keep at organization/supplier-system framing; do not route to PCB qualification |
| AEC-Q component qualification | Route to component-level discussions; do not extend to bare PCB or PCBA |
| CISPR 25 vehicle EMC | Keep at EMC vocabulary and standard-identity level; do not claim compliance |
| ISO 11452 immunity testing | Keep at test-method vocabulary level; do not claim immunity or pass-status |
| EV charging protocol claims | Route to `wiki/applications/power-energy-pcb-pcba-review-boundaries.md` |
| ADAS radar/sensor front-end | Route to `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md` |

---

## Common Misreadings

| Misreading | Correction |
|---|---|
| "ISO 26262 compliant PCB manufacturing" → | ISO 26262 is system lifecycle, not PCB manufacturing compliance. Safe: "automotive E/E functional-safety context." |
| "ASIL-ready board" or "ASIL-D capable PCBA" → | ASIL is system/software allocation, not PCB rating. Safe: "board for automotive ECU applications." |
| "IATF 16949 certified PCB" → | IATF certifies organization QMS, not products. Safe: "automotive supplier quality context." |
| "AEC-Q PCB" or "AEC-Q qualified board" → | AEC-Q is component qualification. Safe: "board for automotive electronics." |
| "CISPR 25 compliant design" → | Compliance requires testing. Safe: "automotive EMC context." |
| "ISO 11452 immune board" → | Immunity is tested, not inherent. Safe: "automotive immunity-test context." |
| "PPAP-approved board" → | PPAP is customer-specific. Safe: "automotive production-part approval context." |

---

## Must Refresh Before Publishing

- Any ISO 26262 ASIL allocation claim
- Any IATF 16949 certification status or scope claim
- Any AEC-Q PCB/PCBA qualification claim
- Any CISPR 25 EMC compliance or pass-status claim
- Any ISO 11452 immunity pass-status or test outcome claim
- Any OEM approval, PPAP completion, or supplier qualification claim

---

## Cross-Lane Routing

| Content Type | Route To |
|---|---|
| Automotive board family routing | `wiki/applications/automotive-ev-pcb-pcba-boundary-map.md` |
| EV charging protocol standards | `wiki/applications/power-energy-pcb-pcba-review-boundaries.md` |
| ADAS/sensor RF front-end | `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md` |
| DFM/DFT review gates | `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md` |
| Thermal platform selection | `facts/methods/thermal-pcb-platform-selection-posture.md` |
| General qualification boundary | `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md` |

---

## Related Pages

- `facts/standards/automotive-ev-standards-depth-boundary.md` — Fact card with PCB stop lines
- `wiki/applications/automotive-ev-pcb-pcba-boundary-map.md` — Active application boundary for 7 board families
- `facts/applications/automotive-ev-coverage-gap-map.md` — Coverage map with residual gaps
