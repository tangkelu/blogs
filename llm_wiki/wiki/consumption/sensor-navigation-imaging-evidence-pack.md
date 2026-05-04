# Sensor / Navigation / Imaging PCB Evidence Pack

**Pack ID**: `consumption-sensor-navigation-imaging`
**Date**: 2026-05-03
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Sensor / Navigation / Imaging PCB/PCBA (MEMS altimeter, IMU/FOG/RLG, EO/IR, radio altimeter, sonar, machine vision, GNSS, UAV sensor)"
scope: |
  Conservative evidence pack for sensor, navigation, and imaging PCB/PCBA content.

  Supports board-class and execution-context vocabulary for MEMS barometric
  altimeter, IMU/gyroscope/magnetometer, EO/IR imaging, radio altimeter RF,
  sonar/ultrasonic, machine vision/video output, GPS/GNSS receiver, and UAV
  sensor integration board families.

  No sensor accuracy numerics, navigation performance claims, qualification
  proof, DO-160/DO-254/MIL-STD compliance, or mission-system authority.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Application boundary
  - "applications-sensor-navigation-imaging-coverage-gap-map"

  # Sensor owner identity cards
  - "methods-barometric-pressure-sensor-owner-identity-and-interface-boundary"
  - "methods-navigation-sensor-technology-owner-identity-boundary"
  - "methods-eo-ir-detector-owner-identity-and-interface-boundary"

  # Sonar / acoustic
  - "methods-sonar-ultrasonic-transducer-front-end-boundary"
  - "methods-hydrophone-and-generic-beamforming-boundary"

  # RF / altimeter
  - "methods-radio-altimeter-rf-front-end-and-integration-boundary"
  - "methods-rf-validation-capability"
  - "methods-rf-impedance-sparameter-pdn-ota-boundaries"

  # UAV / drone control stack
  - "methods-remote-control-and-drone-control-stack-boundary"

  # Standards boundaries
  - "standards-aviation-altimeter-standards-metadata-boundary"
  - "standards-embedded-imaging-serial-interface-boundary"
  - "standards-output-video-and-machine-vision-interface-boundary"
  - "standards-interface-wireless-positioning-product-level-boundary"
  - "standards-military-environmental-and-emi-qualification-boundary"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"

source_ids:
  - "frontendapt-industry-aerospace-defense-page-en"
  - "frontendapt-industry-drone-uav-page-en"
  - "faa-pcg-radio-altimeter-glossary-page"
  - "rtca-do-160g-product-page"
  - "rtca-do-254-product-page"
  - "bosch-bmp390-product-page"
  - "honeywell-hg1930-mems-imu-page"
  - "honeywell-hg2802-fiber-optic-gyro-imu-page"
  - "honeywell-gg1320an-digital-ring-laser-gyroscope-page"
  - "exosens-image-intensifier-tube-page"
  - "sony-starvis-technology-page"
  - "lynred-about-our-technologies-page"
  - "mipi-csi-2-spec-page"
  - "ti-lvds-overview-page"
  - "noaa-sonar-basics-page"
  - "noaa-hydrophone-page"
  - "ti-tuss4440-product-page"
  - "mil-std-461-emi-control-standard-page"
  - "mil-std-810-environmental-engineering-tests-page"

wiki_framing_support:
  - "wiki/applications/sensor-navigation-imaging-pcb-review-boundaries"

must_refresh:
  - claim: "Sensor product model numbers or generation specifications"
    value: true
  - claim: "Aviation standards version or revision claims (DO-160G vs F etc.)"
    value: true
  - claim: "MIL-STD revision-specific vocabulary"
    value: true
  - claim: "GNSS accuracy or positioning performance statements"
    value: true

excluded_claim_classes:
  - "Exact sensor accuracy, drift, noise, sensitivity, or range numerics"
  - "Navigation system performance (position accuracy, heading accuracy, TTFF)"
  - "DO-160G/DO-254/DO-155 qualification or DAL compliance proof"
  - "MIL-STD-461/810 pass-status, compliance proof, or supplier qualification"
  - "Sonar/hydrophone array performance, beamforming accuracy, marine qualification"
  - "Radio altimeter altitude accuracy or precision navigation claims"
  - "Defense-program proof or mission-system authority"
  - "Cost, lead-time, and yield claims"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `sensor PCB`, `IMU PCB`, `navigation PCB`, `imaging board`, `GNSS PCB`, `EO/IR board`, `radar altimeter PCB` |
| **Page Type** | `query` |
| **Search Intent** | Sensing, navigation, and imaging hardware, sensor interface boards, precision measurement PCBs |
| **Target Reader** | Hardware engineers, aerospace/defense designers, UAV platform developers, machine-vision integrators |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` — board-class identity and interface execution context is supported; sensor performance numerics and qualification proof are blocked.

---

## 3. Board Families (Evidence Scope)

### 3.1 MEMS Barometric Altimeter Board

| Aspect | Evidence Support |
|--------|-----------------|
| Sensor owner identity | Bosch BMP390, TE MS5611, Infineon DPS310 — identity-level vocabulary supported |
| Interface design context | SPI/I²C footprint, isolation, filtering review vocabulary |
| Compact board context | Small-footprint PCB layout considerations |
| Exact pressure accuracy, altitude precision, or compensation claims | ❌ Blocked |

### 3.2 IMU / Gyroscope / Magnetometer Board

| Aspect | Evidence Support |
|--------|-----------------|
| Sensor owner identity | Honeywell HG1930 (MEMS IMU), HG2802 (FOG), GG1320AN (RLG), Bosch BMM350 — identity-level vocabulary |
| Technology class identity | MEMS IMU, Fiber Optic Gyroscope (FOG), Ring Laser Gyroscope (RLG) — class vocabulary |
| Sensor-interface and isolation review | Board-level mounting, grounding, shielding vocabulary |
| Drift rate, bias, noise, accuracy, navigation performance claims | ❌ Blocked |

### 3.3 EO/IR Imaging Board

| Aspect | Evidence Support |
|--------|-----------------|
| Detector owner identity | Exosens image intensifier, Sony STARVIS CMOS, Lynred IR detector — identity-level vocabulary |
| Interface identity | MIPI CSI-2, LVDS, GigE Vision interface routing vocabulary |
| Board-class vocabulary | Sensor front-end, readout circuit, interface board context |
| Imaging resolution, sensitivity, NEP, or quantum efficiency claims | ❌ Blocked |

### 3.4 Radio Altimeter RF Board

| Aspect | Evidence Support |
|--------|-----------------|
| RF front-end vocabulary | 4.2–4.4 GHz RF transceiver/interface board vocabulary |
| FAA document-identity framing | DO-155, FAA PCG glossary, FAA EB 107/5G C-band context |
| Assurance context | DO-160G/DO-254 document-family identity for aviation hardware |
| Exact altitude accuracy, landing-system proof, aviation-program qualification | ❌ Blocked |

### 3.5 Sonar / Ultrasonic Transducer Board

| Aspect | Evidence Support |
|--------|-----------------|
| Component owner identity | TI TUSS4440, TI TDC1000 — identity-level vocabulary |
| Receive-element interface vocabulary | Transducer interface, receive amplifier, digitizer board context |
| Generic beamforming context | Array geometry framing vocabulary |
| Transmit voltage, array performance, sonar range, marine qualification | ❌ Blocked |

### 3.6 Machine Vision / Video Output Board

| Aspect | Evidence Support |
|--------|-----------------|
| Interface identity | GigE Vision, USB3 Vision, HDMI, SDI, PAL/NTSC — identity-level vocabulary |
| Board-class vocabulary | Camera interface board, frame-grabber board, video output board context |
| Video resolution, frame rate, latency, broadcast compliance | ❌ Blocked |

### 3.7 GPS / GNSS Receiver Board

| Aspect | Evidence Support |
|--------|-----------------|
| Receiver-system vocabulary | Multi-constellation receiver board, antenna feed, RF ground plane vocabulary |
| Architecture context | GPS/GLONASS/BeiDou/Galileo multi-constellation framing |
| UAV and automotive GNSS board context | Positioning-context vocabulary |
| Finished-board accuracy, CEP, fix rate, anti-jamming claims | ❌ Blocked |

### 3.8 UAV Sensor Integration Board

| Aspect | Evidence Support |
|--------|-----------------|
| Platform stack identity | PX4, MAVLink, ExpressLRS — identity-level architecture vocabulary |
| Sensor fusion context | IMU + barometer + GNSS integration board vocabulary |
| Interface vocabulary | Flight controller PCB, sensor integration bus vocabulary |
| Navigation accuracy, autonomy performance, mission-proof claims | ❌ Blocked |

---

## 4. Standards Context (Identity Only)

| Standard | Safe Use | Blocked Use |
|---|---|---|
| **DO-160G** | Document-family identity for airborne equipment environmental test procedures | Section-level pass-status, specific test values, equipment qualification proof |
| **DO-254** | Design-assurance guidance document identity; circuit-board-assembly scope (FAA AC 20-152A) | DAL assignment, compliance declaration, "DO-254 certified" |
| **DO-155** | Low-range radar altimeter standards identity | Altitude accuracy, performance proof |
| **MIL-STD-461** | EMI/EMC standards-context vocabulary for military equipment | Compliance proof, pass-status, supplier qualification |
| **MIL-STD-810** | Environmental test standards-context vocabulary | Pass-status, ruggedization proof, qualification claim |
| **MIPI CSI-2 / D-PHY** | Sensor interface-family identity | Protocol compliance, throughput proof |
| **LVDS** | Display/sensor link interface identity | Electrical compliance proof |
| **GigE Vision / USB3 Vision** | Machine-vision interface identity | Protocol compliance, real-time performance |
| **GPS / GNSS** | Receiver-system positioning-context vocabulary | Accuracy, CEP, fix rate, anti-jamming proof |

---

## 5. Allowed vs Blocked

### 5.1 Allowed (Board-Class and Interface Context)

| Claim Pattern | Example |
|---|---|
| Sensor owner identity | "Honeywell HG1930 MEMS IMU and HG2802 FOG represent different inertial sensing technology classes for navigation board context" |
| Interface planning vocabulary | "EO/IR imaging boards typically use MIPI CSI-2 or LVDS for high-bandwidth sensor data output" |
| Assurance framing | "Aviation sensor hardware references DO-160G environmental test procedures and DO-254 design-assurance guidance" |
| Military context framing | "Defense sensor boards are typically designed in the context of MIL-STD-461 EMI and MIL-STD-810 environmental requirements" |
| Board-class execution context | "Radio altimeter RF front-end boards require RF layout discipline at the 4.2–4.4 GHz range" |

### 5.2 Blocked (Performance / Qualification / Mission Proof)

| Blocked Claim | Reason |
|---|---|
| "Our IMU board achieves 0.01°/hr bias stability" | Sensor accuracy is a component + system attribute, not a PCB claim |
| "DO-160G Section 8 Category S vibration passed" | Section-level pass-status requires the complete equipment test |
| "MIL-STD-461 CE102 compliant PCB" | MIL-STD compliance belongs to the complete equipment/system |
| "GNSS board achieves 1.5 m CEP accuracy" | Accuracy is receiver firmware + satellite geometry, not PCB |
| "Proven in [program name] defense deployment" | Mission authority is outside current source layer |

---

## 6. Handoff

**Core Answer**:

> Sensor, navigation, and imaging PCBs are supported through board-class execution-context vocabulary covering 8 board families. The current evidence supports sensor owner identity naming, interface planning vocabulary (MIPI/LVDS/GigE/GNSS), aviation and military standards-context framing, and board-level assembly/validation posture. It does not support sensor accuracy numerics, DO/MIL qualification proof, navigation performance claims, or mission-system authority.

**Safe Reusable Shapes**:

- "Sensor families (MEMS IMU, FOG, RLG, EO/IR, barometric, sonar) are safer named as technology-class board families than as performance-level capabilities."
- "Aviation and military standards (DO-160G, DO-254, MIL-STD-461/810) are reference frameworks for equipment qualification, not PCB-level certifications."
- "GNSS and inertial navigation boards provide the physical interface layer — accuracy and performance belong to the receiver firmware, correction service, and system architecture."

---

## 7. Pre-flight

- [x] Sensor/navigation/imaging wiki boundary page referenced
- [x] Application fact card referenced (`facts/applications/sensor-navigation-imaging-coverage-gap-map.md`)
- [x] All 15 fact_ids from existing landed records — no new records required
- [x] All 19 source_ids from existing landed registry records
- [x] Sensor performance numerics and accuracy blocked claims explicitly documented
- [x] DO-160G/DO-254/MIL-STD compliance claims blocked
- [x] `must_refresh` items identified for product model numbers, standards revisions, GNSS performance

**Verdict**: ✅ `go_now_conservative` — board-class identity and interface execution context. Exclude all sensor accuracy numerics, qualification proof, and mission-system authority claims.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
