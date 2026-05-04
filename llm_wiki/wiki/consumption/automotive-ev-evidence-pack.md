# Automotive / EV PCB Evidence Pack

**Pack ID**: `consumption-automotive-ev`
**Date**: 2026-05-03
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Automotive / EV PCB/PCBA (ECU, inverter/motor-control, BMS, OBC/charger, ADAS, infotainment, lighting/body)"
scope: |
  Conservative evidence pack for automotive and EV PCB/PCBA content.

  Supports board-class and execution-context vocabulary for 7 board families:
  ECU/vehicle control, inverter/motor control, BMS, OBC/DC-DC/charger, ADAS/radar/camera,
  infotainment/TCU, and lighting/body/BCM.

  Standards vocabulary (ISO 26262, IATF 16949, AEC-Q) at document-family
  identity level only. Thermal/vibration/cleanliness context vocabulary at
  process-description level only.

  No ASIL compliance proof, PPAP completion, OEM approval, qualification pass-status,
  or field-reliability claims.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Application boundary
  - "applications-automotive-ev-coverage-gap-map"

  # Standards qualification boundary
  - "standards-automotive-medical-aerospace-application-qualification-boundary"

  # High-current / thermal
  - "methods-current-carrying-trace-width-and-copper-boundary"
  - "methods-thermal-pcb-platform-selection-posture"

  # Assembly / validation
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-npi-to-mass-production-gates"
  - "methods-conformal-coating-lane-b-rewrite-gate"

source_ids:
  - "frontendapt-industry-automotive-electronics-page-en"
  - "iso-26262-road-vehicles-functional-safety-package"
  - "iatf-16949-overview-page"
  - "aec-documents-page"

wiki_framing_support:
  - "wiki/applications/automotive-ev-pcb-pcba-boundary-map"
  - "wiki/applications/automotive-ev-standards-routing-boundary"

must_refresh:
  - claim: "ISO 26262 revision or ASIL methodology changes"
    value: true
  - claim: "IATF 16949 audit cycle or certification status claims"
    value: true
  - claim: "AEC-Q qualification standard revision numbers"
    value: true
  - claim: "OEM program deployment or production volume claims"
    value: true

excluded_claim_classes:
  - "ISO 26262 ASIL compliance, functional safety allocation, or PCB ASIL rating"
  - "IATF 16949 certification validity, PPAP completion, or OEM approval"
  - "AEC-Q component qualification proof at PCB level"
  - "Thermal cycling, vibration, cleanliness lot-level pass/fail proof"
  - "Exact creepage, clearance, or high-voltage safety thresholds"
  - "Field reliability, warranty outcomes, or OEM program deployment"
  - "Cost, lead-time, and yield claims"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `automotive PCB`, `EV PCB`, `ECU board`, `BMS PCB`, `ADAS PCB`, `inverter PCB`, `OBC board` |
| **Page Type** | `query` |
| **Search Intent** | Automotive electronics hardware, EV powertrain boards, ADAS sensor boards, vehicle control PCBs |
| **Target Reader** | Automotive hardware engineers, EV system integrators, Tier-1/Tier-2 automotive suppliers |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` — board-class execution context and design-consideration vocabulary supported; ASIL compliance, OEM approval, qualification proof, and field reliability blocked.

---

## 3. Board Families (Evidence Scope)

### 3.1 ECU / Vehicle Control

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Engine ECU, BCM, domain controller, gateway ECU board context |
| Material context | High-Tg material selection vocabulary |
| Interface vocabulary | CAN/LIN/FlexRay/Automotive Ethernet trace-routing vocabulary |
| ASIL compliance, OEM program approval, reliability proof | ❌ Blocked |

### 3.2 Inverter / Motor Control

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Traction inverter, e-axle, auxiliary drive board vocabulary |
| Design language | High-voltage design language (creepage/clearance as vocabulary, not thresholds) |
| Thermal vocabulary | Thick copper, thermal vias, thermal-integration planning |
| Layout vocabulary | Gate-driver/MCU/sensing integration, EMC-aware layout context |
| Exact creepage/clearance thresholds, efficiency proof, qualification pass-status | ❌ Blocked |

### 3.3 BMS (Battery Management System)

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Pack BMS master, cell monitoring slave, LV/HV junction box board context |
| Routing vocabulary | Differential cell-sense routing, isolation slot design, coating planning |
| Interface vocabulary | CAN/SPI/UART balancing interface context |
| Cell capacity, pack voltage, safety qualification, BMS algorithm proof | ❌ Blocked |

### 3.4 OBC / DC-DC / Charger

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | On-board charger, DC-DC converter, wallbox charger, fast DC charger board context |
| Layout vocabulary | AC-DC/DC-DC power stage layout, isolation/creepage design language |
| Thermal vocabulary | Thermal-mechanical integration context |
| Charging efficiency, EMC compliance, isolation proof | ❌ Blocked — route EV charger protocol vocabulary to `power-energy-evidence-pack.md` |

### 3.5 ADAS / Radar / Camera

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Radar module, camera board, sensor fusion domain controller context |
| Interface vocabulary | RF/LVDS/MIPI front-end layout vocabulary |
| Environmental vocabulary | Exterior-mounting material and coating option context |
| Network vocabulary | CAN/Automotive Ethernet integration vocabulary |
| Radar detection performance, object recognition accuracy, NCAP ratings | ❌ Blocked — see also `sensor-navigation-imaging-evidence-pack.md` for radar front-end overlap |

### 3.6 Infotainment / TCU

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | Head unit, digital cluster, telematics control unit, gateway board context |
| Interface vocabulary | LVDS/MIPI/HDMI display link vocabulary; 4G/5G/GNSS/Wi-Fi/Bluetooth antenna interface vocabulary |
| Network vocabulary | CAN/Automotive Ethernet gateway context |
| OTA update performance, cybersecurity compliance, connectivity certification | ❌ Blocked |

### 3.7 Lighting / Body / BCM

| Aspect | Evidence Support |
|--------|-----------------|
| Board-class vocabulary | LED headlamp, DRL/tail lamp, BCM, seat/HVAC/window control board vocabulary |
| Thermal platform vocabulary | MCPCB/FR-4 LED board context |
| Environmental vocabulary | Vibration/moisture design consideration vocabulary |
| LED luminous flux, photometric proof, vibration qualification proof | ❌ Blocked |

---

## 4. Standards Context (Identity Only)

| Standard | Safe Use | Blocked Use |
|---|---|---|
| **ISO 26262** | Road-vehicle functional-safety standard identity; ASIL level naming as system-context vocabulary | ASIL compliance proof, safety allocation, PCB ASIL rating |
| **IATF 16949** | Automotive QMS standard identity; PPAP/validation phase vocabulary as process-description context | Certification validity, PPAP completion, OEM approval |
| **AEC-Q** | Automotive electronic component qualification document-family identity | Component qualification proof at PCB or supplier level |

---

## 5. Context Vocabulary Notes (Process Description Only)

The Tier-2 internal source references the following contextual vocabulary. These are process-description level only — **not** lot-level guarantees or published specification proof:

| Vocabulary | Status |
|---|---|
| Thermal cycling (-40 to 125 °C) | Process-description context vocabulary only — not lot-level proof |
| Vibration (5 Grms / 10 h) | Process-description context vocabulary only — not lot-level proof |
| Cleanliness (ROSE ≤1.5 µg/cm²) | Process-description context vocabulary only — not published specification proof |
| VIN-to-board traceability | Process-description vocabulary |
| PPAP / validation phase staging | Description-level vocabulary only |

---

## 6. Routing Notes

- **EV charger protocol vocabulary** (IEC 61851, ISO 15118, SAE J1772, OCPP): route to `wiki/consumption/power-energy-evidence-pack.md`
- **ADAS radar/sensor front-end context**: partial overlap with `wiki/consumption/sensor-navigation-imaging-evidence-pack.md`

---

## 7. Allowed vs Blocked

### 7.1 Allowed (Board-Class and Design Context)

| Claim Pattern | Example |
|---|---|
| Board-class naming | "Automotive BMS PCBs require differential cell-sense routing, isolation slots, and protective coating planning" |
| Standards identity framing | "ISO 26262 defines the functional safety lifecycle for automotive E/E systems; ASIL levels describe safety requirements at the system level" |
| Process-description vocabulary | "Automotive PCBs typically reference thermal cycling and vibration test contexts during design validation" |
| Design-consideration framing | "ADAS boards combine RF front-end, LVDS/MIPI imaging interfaces, and CAN/Ethernet network integration on a single assembly" |

### 7.2 Blocked (Compliance / Qualification / Field Proof)

| Blocked Claim | Reason |
|---|---|
| "ASIL-B compliant inverter PCB" | ASIL compliance is a system-level functional safety outcome, not a PCB attribute |
| "IATF 16949 certified automotive PCB" | Certification applies to the organization's QMS, not individual PCBs |
| "Passed AEC-Q200 qualification" | AEC-Q qualification is a component-level test outcome, not a PCB manufacturing claim |
| "Proven in OEM production programs" | OEM program deployment requires a specific authority source |

---

## 8. Handoff

**Core Answer**:

> Automotive and EV PCBs are addressed through 7 board families at board-class execution-context level. The current evidence supports design vocabulary, materials context, interface naming, and standards-identity framing (ISO 26262, IATF 16949, AEC-Q). It does not support ASIL compliance, OEM approval, PPAP completion, qualification proof, or field-reliability claims.

**Safe Reusable Shapes**:

- "Automotive standards names (ISO 26262, IATF 16949, AEC-Q) are design-context reference frameworks — they set the qualification bar, but they do not certify the PCB."
- "Automotive board families create distinct design pressures: BMS boards require isolation and differential sensing; inverter boards require high-voltage layout discipline; ADAS boards require RF and high-speed interface coordination."
- "Process-description vocabulary (thermal cycling, vibration, cleanliness) describes the design-validation context — it is not a lot-level outcome guarantee."

---

## 9. Pre-flight

- [x] Automotive/EV wiki boundary page referenced
- [x] Application fact card referenced (`facts/applications/automotive-ev-coverage-gap-map.md`)
- [x] All 7 fact_ids from existing landed records — no new records required
- [x] All 4 source_ids from existing landed registry records
- [x] ASIL/IATF/AEC-Q vocabulary limited to document-family identity
- [x] Process-description context vocabulary (thermal/vibration/cleanliness) flagged as non-proof
- [x] Cross-routing notes to power-energy and sensor packs included
- [x] `must_refresh` items identified for standards revision and OEM program claims

**Verdict**: ✅ `go_now_conservative` — board-class design context vocabulary. Exclude all ASIL compliance, OEM approval, qualification pass-status, and field-reliability claims.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
