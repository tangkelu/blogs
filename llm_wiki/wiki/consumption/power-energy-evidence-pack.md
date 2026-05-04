# Power / Energy PCB Evidence Pack

**Pack ID**: `consumption-power-energy`
**Date**: 2026-05-03
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Power / Energy PCB/PCBA (inverter, EV charger, smart meter, renewable-energy board, thermal platform)"
scope: |
  Conservative evidence pack for power and energy PCB/PCBA content.

  Supports board-class and execution-context vocabulary for central inverter,
  ultra-fast charger, Type-C charger, smart meter, EV charger control, boundary-
  scan/JTAG, DFM/DFT/DFA review, and conformal coating board families, plus
  thermal platform (heavy copper, MCPCB, high thermal) vocabulary.

  No inverter efficiency, EV charger compliance, smart meter metrology approval,
  grid compliance, or coating qualification proof.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Application boundary
  - "applications-power-energy-coverage-gap-map"

  # Power/energy method cards
  - "methods-power-energy-inverter-charger-rewrite-boundary"
  - "methods-thermal-pcb-platform-selection-posture"
  - "methods-tht-pressfit-terminal-route-boundary"

  # Assembly / test method cards
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-boundary-scan-jtag-positioning"
  - "methods-conformal-coating-lane-b-rewrite-gate"

  # Standards cards
  - "standards-smart-meter-standards-and-metrology-identity-boundary"
  - "standards-smart-meter-communication-protocol-identity-boundary"
  - "standards-ev-charger-control-stack-and-protocol-identity-boundary"

source_ids:
  - "frontendapt-industry-power-energy-page-en"
  - "frontendapt-pcb-heavy-copper-pcb-page-en"
  - "frontendapt-pcb-high-thermal-pcb-page-en"
  - "frontendapt-pcb-metal-core-pcb-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "iec-61851-1-2017-product-page"
  - "iec-61851-23-2023-product-page"
  - "iso-15118-1-2019-page"
  - "iso-15118-20-2022-page"
  - "sae-j1772-202401-recommended-practice-page"
  - "charin-iso-iec-15118-communication-standard-page"
  - "open-charge-alliance-ocpp-protocols-page"

wiki_framing_support:
  - "wiki/applications/power-energy-pcb-pcba-review-boundaries"

must_refresh:
  - claim: "EV charging protocol revision numbers (IEC 61851, ISO 15118, SAE J3400)"
    value: true
  - claim: "Smart meter regulation regime or MID revision status"
    value: true
  - claim: "Thermal platform product family availability"
    value: true
  - claim: "OCPP version or backend connectivity revision claims"
    value: true

excluded_claim_classes:
  - "Inverter or charger efficiency, power density, or grid compliance proof"
  - "EV charger IEC 61851/ISO 15118/SAE J1772/CCS/NACS/OCPP compliance or interoperability"
  - "Smart meter accuracy class, MID marking, metrology approval, or service-life claims"
  - "Coating qualification (ASIL, ISO 26262, creepage/clearance, qualification outcomes)"
  - "Thermal platform universal recipe or superiority claims"
  - "Field-reliability or lifetime claims for power/energy hardware"
  - "Cost, lead-time, and yield claims"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `power electronics PCB`, `EV charger PCB`, `inverter PCB`, `smart meter PCB`, `heavy copper PCB`, `MCPCB` |
| **Page Type** | `query` |
| **Search Intent** | Power electronics hardware, EV charging infrastructure, energy metering, thermal-platform selection |
| **Target Reader** | Power electronics engineers, EV infrastructure designers, energy system integrators |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` — board-class partition vocabulary and thermal platform context supported; compliance proof, efficiency numerics, and metrology approval blocked.

---

## 3. Board Families (Evidence Scope)

### 3.1 Central Inverter Board

| Aspect | Evidence Support |
|--------|-----------------|
| Board partition review (power stage / control / monitoring) | Supported at partition-vocabulary level |
| Heavy copper vocabulary for high-current power stages | Supported as route-choice vocabulary |
| Thermal via and heat-spreading design language | Supported at vocabulary level |
| DFM/DFT/DFA vocabulary | Supported at gate-positioning level |
| Inverter efficiency, power factor, insulation, or grid compliance proof | ❌ Blocked |

### 3.2 Ultra-Fast Charger Board

| Aspect | Evidence Support |
|--------|-----------------|
| Power-board + control-board partitioning | Supported at partition-vocabulary level |
| Isolation / creepage design language (context only) | Supported at vocabulary/framing level |
| Layered validation workflow vocabulary | Supported at gate-positioning level |
| Charging speed, connector protocol behavior, compliance proof | ❌ Blocked |

### 3.3 Type-C Charger Board

| Aspect | Evidence Support |
|--------|-----------------|
| Compact board assembly vocabulary | Supported at DFM/DFA vocabulary level |
| Connector-access planning | Supported at layout-consideration vocabulary |
| Powered functional test context | Supported at FCT vocabulary level |
| USB PD compliance, power delivery performance, GaN efficiency claims | ❌ Blocked |

### 3.4 Smart Meter PCB

| Aspect | Evidence Support |
|--------|-----------------|
| Metrology front-end board partitioning | Supported at partition-vocabulary level |
| IEC 62052/62053, MID/MI-003, ANSI C12.20 identity-level vocabulary | Supported at standards-family identity level |
| AMI communication identity (DLMS/COSEM, PRIME, G3-PLC, Wi-SUN, Zigbee, NB-IoT, LTE-M) | Supported at identity-only level |
| Accuracy class, metrology approval, MID marking, service-life claims | ❌ Blocked |

### 3.5 EV Charger Control Board

| Aspect | Evidence Support |
|--------|-----------------|
| Board partitioning (charger controller, protocol interface, backend) | Supported at partition-vocabulary level |
| IEC 61851-1/-23/-24 identity-level vocabulary | Supported at standards-family identity level |
| ISO 15118 / SAE J1772 / J3400 (CCS/NACS) identity-level vocabulary | Supported at standards-family identity level |
| OCPP 2.0.1 identity-level vocabulary | Supported at protocol-identity level |
| Compliance, interoperability, plug-and-charge, or payment integration proof | ❌ Blocked |

### 3.6 Boundary-Scan / JTAG Board

| Aspect | Evidence Support |
|--------|-----------------|
| Boundary-scan test-access vocabulary | Supported for digital control/monitoring subassemblies |
| JTAG scan chain planning | Supported at test-access vocabulary level |
| Power-stage correctness or in-circuit power test proof | ❌ Blocked — boundary-scan is digital-access only |

### 3.7 DFM / DFT / DFA Review

| Aspect | Evidence Support |
|--------|-----------------|
| Review sequencing and gate vocabulary | Supported at gate-positioning level |
| Access planning for power boards | Supported at DFA/DFT vocabulary level |
| Field reliability proof or standards approval | ❌ Blocked |

### 3.8 Conformal Coating (EV / Automotive Power)

| Aspect | Evidence Support |
|--------|-----------------|
| Coating workflow vocabulary (apply, mask, cure sequence) | Supported at process-vocabulary level |
| Environmental protection context | Supported at application-context level |
| Automotive qualification, ASIL, ISO 26262, creepage/clearance proof | ❌ Blocked |

---

## 4. Thermal Platform Context

| Platform | Safe Vocabulary | Blocked Vocabulary |
|---|---|---|
| **Heavy Copper PCB** | Distinct route-choice for high-current power stages; copper thickness naming as design-context vocabulary | Universal recipe, guaranteed thermal outcome, cost comparison |
| **MCPCB (Metal Core PCB)** | Distinct thermal option for LED/power boards; board-type identity vocabulary | Exact thermal resistance, universal superiority, LED driver guarantee |
| **High Thermal PCB** | Distinct option family; thermal-platform selection context | Exact recipe, performance comparison, qualification proof |

---

## 5. Standards Context (Identity Only)

| Standard / Protocol | Safe Use | Blocked Use |
|---|---|---|
| **IEC 61851-1/-23/-24** | EV charging system architecture identity; conductive charging vocabulary | Compliance proof, interoperability, current/power behavior |
| **ISO 15118 (V2G/V2X)** | V2G/V2X communication vocabulary; protocol-identity framing | Plug-and-charge interoperability, data security proof |
| **SAE J1772 / J3400 (CCS/NACS)** | North American charging connector/protocol identity | Connector protocol behavior, interoperability, NACS transition claims |
| **OCPP 2.0.1** | Backend connectivity identity; open charge point protocol naming | Payment integration, roaming interoperability, network behavior |
| **IEC 62052/62053** | Metrology standard-family vocabulary; utility-meter context | Exact accuracy class, compliance proof |
| **MID / MI-003 / ANSI C12.20** | Metrology regulation regime identity | Metrology approval, service-life guarantee, accuracy certification |
| **DLMS/COSEM / PRIME / G3-PLC / Wi-SUN / Zigbee / NB-IoT / LTE-M** | AMI communication technology identity | Protocol interoperability, network topology, performance claims |

---

## 6. Allowed vs Blocked

### 6.1 Allowed (Board-Class and Execution Context)

| Claim Pattern | Example |
|---|---|
| Board partition vocabulary | "Inverter designs typically separate power stage, control, and monitoring zones at the PCB level" |
| Thermal platform choice context | "Heavy copper boards support high-current power stages; MCPCB provides an alternative thermal path for LED-based power hardware" |
| Protocol identity framing | "EV charger control boards interface with IEC 61851 and ISO 15118 protocol stacks; board design must accommodate the communication interface requirements" |
| Validation gate framing | "DFM/DFT/DFA review gates and functional test (FCT) workflows support quality control for power/energy assemblies" |
| Standards-family context | "Smart meter PCBs are designed for utility meter applications referencing IEC 62052/62053 metrology standards and AMI communication protocols" |

### 6.2 Blocked (Compliance / Performance / Certification)

| Blocked Claim | Reason |
|---|---|
| "99% inverter efficiency achieved" | Inverter efficiency is a system-level measured outcome, not a PCB claim |
| "IEC 61851-23 DC charging compliant" | Compliance belongs to the complete charging system after testing |
| "ISO 15118 plug-and-charge capable" | Interoperability proof requires complete V2G stack testing |
| "MID approved smart meter PCB" | MID approval is granted to the complete meter device |
| "Conformal coating per ASIL-B requirements" | Automotive qualification belongs to the program, not the PCB supplier |

---

## 7. Handoff

**Core Answer**:

> Power and energy PCBs are supported through board-class partition vocabulary covering 8 board families plus three thermal platform route-choice families. The current evidence supports design-partition framing, thermal platform selection context, EV charger and smart meter protocol identity vocabulary, and DFM/DFT/DFA validation gate positioning. It does not support efficiency numerics, compliance proof, metrology approval, grid authorization, or thermal-outcome guarantees.

**Safe Reusable Shapes**:

- "EV charger and smart meter standards (IEC 61851, ISO 15118, IEC 62052/62053) are design-context reference families — they create board-level requirements but they do not certify the PCB."
- "Thermal platform selection (heavy copper, MCPCB, high thermal) is a design-trade vocabulary — the correct choice depends on the application's current density, thermal budget, and space constraints."
- "Power electronics PCBs benefit from early DFM/DFT/DFA review to avoid access, isolation, and test-point conflicts that become expensive to correct after layout is locked."

---

## 8. Pre-flight

- [x] Power/energy wiki boundary page referenced (`wiki/applications/power-energy-pcb-pcba-review-boundaries.md`)
- [x] Application fact card referenced (`facts/applications/power-energy-coverage-gap-map.md`)
- [x] All 9 fact_ids from existing landed records — no new records required
- [x] All 13 source_ids from existing landed registry records
- [x] EV charger and smart meter protocol vocabulary limited to identity-level
- [x] Thermal platform claims limited to route-choice vocabulary
- [x] `must_refresh` items identified for protocol revision numbers and metrology regime changes

**Verdict**: ✅ `go_now_conservative` — board-class partition vocabulary and thermal platform context. Exclude all efficiency numerics, compliance proof, metrology approval, and certification claims.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
