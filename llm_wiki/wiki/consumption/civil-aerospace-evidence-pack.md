# Civil Aerospace PCB Evidence Pack

**Pack ID**: `consumption-civil-aerospace`
**Date**: 2026-05-03
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Civil Aerospace PCB/PCBA — civil/commercial (avionics, comm/RF/data-link, power/actuation, ground systems, ruggedization)"
scope: |
  Conservative evidence pack for civil aerospace PCB/PCBA content.
  CIVIL context only — commercial aviation, civil avionics, non-defense electronics.

  Supports board-class vocabulary for 5 board families: avionics/flight control/navigation,
  communication/RF/data links, power/actuation, ground systems/test equipment,
  and ruggedization/materials/stackup.

  Standards vocabulary (AS9100, DO-160G, DO-254, FAA TSO, AS9102) from P4-190
  official-assurance-depth card at governance-layer identity level only.

  CRITICAL: The Tier-2 source contains "AS9100 Certified – Mission Assurance" as a
  trust-bar/marketing label. This does NOT prove a current AS9100 certificate or
  OASIS registration. Treat the Tier-2 source as scenario-framing only.

  No airworthiness, AS9100 cert status, DO-160G pass-status, DO-254 DAL,
  TSO authorization, ITAR compliance, or mission reliability claims.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Application boundary
  - "applications-civil-aerospace-coverage-gap-map"

  # Official assurance depth (P4-190)
  - "standards-civil-aerospace-official-assurance-depth"

  # Aviation standards identity
  - "standards-aviation-altimeter-standards-metadata-boundary"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"

  # Assembly / inspection / traceability
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"

source_ids:
  - "frontendapt-industry-aerospace-defense-page-en"
  - "faa-ac-20-152a-page"
  - "faa-ac-21-16g-do160-acceptability-page"
  - "rtca-do-160g-product-page"
  - "rtca-do-254-product-page"
  - "as9102c-first-article-inspection-page"

wiki_framing_support:
  - "wiki/applications/civil-aerospace-pcb-pcba-boundary-map"
  - "wiki/applications/civil-aerospace-assurance-routing-boundary"

must_refresh:
  - claim: "AS9100 revision status or OASIS registration of the PCB supplier"
    value: true
  - claim: "DO-160G version or FAA AC 21-16G revision acceptance status"
    value: true
  - claim: "DO-254 version or FAA AC 20-152A guidance update"
    value: true
  - claim: "FAA TSO authorization status for any specific product"
    value: true

excluded_claim_classes:
  - "AS9100 certificate validity, OASIS registration, or QMS audit status"
  - "DO-160G section-level test, test-condition value, or pass-status proof"
  - "DO-254 DAL assignment, design-assurance level, or compliance proof"
  - "Airworthiness, TSO authorization, STC, FAA approval, or installation approval"
  - "ITAR, EAR, export-control, or classified-program compliance"
  - "Mission reliability, MTBF, or field-deployment statistics"
  - "Cost, lead-time, and yield claims"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `avionics PCB`, `civil aerospace PCB`, `avionics board`, `DO-254 PCB`, `DO-160 board`, `aerospace PCBA` |
| **Page Type** | `query` |
| **Search Intent** | Civil avionics hardware, commercial aerospace PCBs, aviation electronics manufacturing |
| **Target Reader** | Avionics engineers, commercial aircraft hardware designers, civil aerospace system integrators |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` — board-class vocabulary and standards-identity governance framing supported; AS9100 certification, DO-160G/DO-254 pass-status, airworthiness, and TSO authorization blocked.

> **Critical governance note**: The Tier-2 source (`frontendapt-industry-aerospace-defense-page-en`) contains `"AS9100 Certified – Mission Assurance"` as a trust-bar/marketing label. This does **NOT** prove:
> - A current AS9100 certificate held by the supplier
> - OASIS registration status
> - Any specific build or program is AS9100-conforming
>
> Treat the Tier-2 source as application-scenario framing only. AS9100 and certification claims **must be refreshed** from official records before any publication.

> **Routing note**: For defense/military aviation (EW, radar, ISR, MIL-STD): use `wiki/consumption/defense-ew-surveillance-evidence-pack.md`.

---

## 3. Board Families (Evidence Scope)

### 3.1 Avionics / Flight Control / Navigation

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Flight computer, avionics I/O board, cockpit display PCB, sensor interface board, data concentrator context |
| Architecture vocabulary | Multilayer processor/FPGA/memory/mixed-signal board description |
| Redundancy vocabulary | Redundant channel + voting logic layout description (customer-design basis) |
| Sensor interface vocabulary | Air-data/IMU/GNSS/altimeter sensor interface vocabulary |
| Airworthiness, DAL assignment, flight qualification proof | ❌ Blocked |

### 3.2 Communication / RF / Data Links

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Airborne radio, satcom board, data link PCBA context |
| RF vocabulary | RF/microwave layer and matching network board description |
| Signal processing vocabulary | High-speed ADC/DAC/FPGA/DSP signal processing board vocabulary |
| Thermal vocabulary | Thermal/conduction-cooled layout vocabulary |
| RF performance, compliance with FAA frequency authorizations, satcom certification | ❌ Blocked |

### 3.3 Power / Actuation

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Power supply, DC-DC converter, motor/actuator driver, PDU board context |
| Design vocabulary | High-voltage/high-current creepage/clearance description (vocabulary, not thresholds) |
| Circuit vocabulary | MOSFET/IGBT/gate driver/current-sense layout vocabulary |
| Layout vocabulary | EMC-aware power layout, redundancy and monitoring vocabulary |
| Airworthiness, DO-160G environmental qualification, efficiency proof | ❌ Blocked |

### 3.4 Ground Systems / Test Equipment

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Rugged computer, command-console PCB, test rack, simulator board context |
| Materials vocabulary | Long-lifecycle materials and process description |
| DO-160G pass-status, military-ground qualification, system certification | ❌ Blocked |

### 3.5 Ruggedization / Materials / Stackup

| Aspect | Evidence Support |
|--------|-----------------|
| Materials vocabulary | High-Tg material vocabulary (customer-specified) |
| Stackup vocabulary | Controlled impedance, high-speed layer, via/PTH integrity vocabulary |
| Coating vocabulary | Conformal coating vocabulary for aerospace context |
| Specific material thermal/mechanical proof, DO-160G section pass-status | ❌ Blocked |

---

## 4. Standards Context (Governance-Layer Identity — from P4-190 Official-Depth Card)

| Standard | Safe Use | Blocked Use |
|---|---|---|
| **AS9100** | QMS standard-family identity; aerospace quality management system vocabulary | Certificate validity, OASIS registration, audit status, any "AS9100 certified" claim |
| **DO-160G** | Environmental test procedure document identity; FAA AC 21-16G recognition context | Section-level test, test-condition values, pass-status, qualification proof |
| **DO-254** | Design assurance guidance document identity; circuit-board-assembly scope (FAA AC 20-152A) | DAL assignment, compliance declaration, "DO-254 certified" claim |
| **FAA TSO** | Technical Standard Order authorization framework identity | TSO authorization status, TSO holder status, device approval proof |
| **AS9102** | First-article inspection standard identity; FAI documentation context vocabulary | Process-capability proof, AS9100 audit readiness, FAI pass-status |
| **FAA AC 20-152A** | Circuit-board-assembly design-assurance context only | Airworthiness approval, TSO authorization, installation approval |

---

## 5. Civil vs Defense Aerospace Separation

| Context | Correct Pack |
|---|---|
| Commercial aircraft avionics | This pack |
| Civil navigation systems | This pack |
| Civil communication / satcom boards | This pack |
| Civil ground systems / ATC support equipment | This pack |
| Defense / military EW, radar, ISR | `defense-ew-surveillance-evidence-pack.md` |
| MIL-STD-461/810 classified program boards | `defense-ew-surveillance-evidence-pack.md` |

---

## 6. AS9100 Claim Handling — Critical Rules

Because the Tier-2 source uses "AS9100 Certified" as a marketing label, the following rules apply to any civil aerospace content:

| Situation | Required Action |
|---|---|
| Writing about AS9100 generally | Use AS9100 as QMS standard-family identity vocabulary only |
| Referencing a specific supplier's AS9100 status | Must refresh from official OASIS registration or certificate — NOT from Tier-2 source |
| Any "AS9100 certified" claim about HILPCB | Must be verified against current certificate before publication |
| AS9100 as design requirement context | Safe — framing AS9100 as the aerospace QMS governance framework is identity vocabulary |

---

## 7. Allowed vs Blocked

### 7.1 Allowed (Board-Class and Governance-Identity Context)

| Claim Pattern | Example |
|---|---|
| Board-class vocabulary | "Civil avionics boards combine processor, FPGA, mixed-signal sensing, and communication interfaces in multilayer assemblies" |
| Standards-identity framing | "DO-160G defines environmental test procedures for airborne equipment; DO-254 provides design-assurance guidance for programmable electronic hardware" |
| Process-context vocabulary | "Civil aerospace PCBs typically reference AS9100 QMS governance; FAI (AS9102) documentation supports build-record completeness" |
| Material context | "Civil aerospace boards often specify high-Tg materials and controlled-impedance stackups for thermal and signal integrity planning" |

### 7.2 Blocked (Certification / Qualification / Airworthiness)

| Blocked Claim | Reason |
|---|---|
| "AS9100 certified avionics PCB" | AS9100 certification belongs to the organization's QMS — must be verified from OASIS, not from the Tier-2 source |
| "DO-160G Section 8 vibration qualified" | Section-level qualification requires the complete equipment to pass the specified test |
| "DO-254 DAL-C compliant design" | DAL assignment is a system-level design assurance obligation, not a PCB manufacturing claim |
| "FAA TSO authorized component" | TSO authorization is granted to a specific device by the FAA — the PCB alone is not the authorization unit |
| "ITAR compliant manufacturing" | ITAR compliance is a regulatory/export-control obligation — completely outside current source scope |

---

## 8. Handoff

**Core Answer**:

> Civil aerospace PCBs are addressed through 5 board families at board-class vocabulary level plus governance-layer identity framing for AS9100, DO-160G, DO-254, FAA TSO, and AS9102. The current evidence supports design vocabulary, standards-identity context, and manufacturing-posture framing. AS9100 certification claims in the Tier-2 source are marketing framing and must not be promoted without verified current certificate status. Airworthiness, DO qualification, DAL assignment, TSO authorization, and ITAR compliance are all blocked.

**Safe Reusable Shapes**:

- "Civil aerospace standards (DO-160G, DO-254, AS9100) are governance frameworks that define the qualification and assurance requirements — they describe what the complete device or organization must demonstrate, not what the PCB manufacturing step certifies."
- "DO-254 specifically addresses the design-assurance process for programmable electronic hardware; FAA AC 20-152A extends this to circuit-board-assembly context — but neither certifies the PCB alone."
- "AS9100 names a QMS framework — any reference to specific AS9100 certification status requires current verification from official OASIS records, not from marketing source material."

---

## 9. Pre-flight

- [x] Civil aerospace wiki boundary page referenced
- [x] Application fact card referenced (`facts/applications/civil-aerospace-coverage-gap-map.md`)
- [x] P4-190 official assurance depth card referenced (`facts/standards/civil-aerospace-official-assurance-depth.md`)
- [x] All 6 fact_ids from existing landed records — no new records required
- [x] All 6 source_ids from existing landed registry records
- [x] Critical governance note on Tier-2 "AS9100 Certified" marketing label prominently documented
- [x] Civil vs defense aerospace separation explicitly documented
- [x] ITAR/EAR completely outside scope — explicitly noted
- [x] AS9100 claim handling rules table included
- [x] `must_refresh` items identified for AS9100 certificate status, DO-160G version, TSO authorization

**Verdict**: ✅ `go_now_conservative` — civil board-class vocabulary and governance-layer identity context. Exclude all AS9100 certification claims, DO qualification pass-status, airworthiness, TSO authorization, and ITAR compliance claims.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
