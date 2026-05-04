---
fact_id: "applications-sensor-navigation-imaging-coverage-gap-map"
title: "Sensor / Navigation / Imaging application coverage gap map: which board families have wiki-level routing and which remain overview-only"
topic: "Sensor, navigation, and imaging PCB/PCBA application coverage"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-184 initial build; sourced from wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md (active as of P4-177), related sensor/altimeter/imaging fact cards in facts/methods/ and facts/standards/"
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
tags: ["sensor-interface", "navigation", "imaging", "imu", "altimeter", "sonar", "gnss", "eo-ir", "coverage-map", "gap-map"]
---

# Canonical Summary

> As of 2026-05-03 after P4-184 initial build, the sensor/navigation/imaging application family has a dedicated wiki boundary page (`wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md`) and that page is now `active`. This fact card maps what the current internal and public source layer supports, which board families are addressable, and which accuracy/performance layers remain blocked.

## Board Family Coverage State

### Supported at Scenario + Board-Class Level

All entries below are supported by Tier-2 internal sources, owner-backed product pages, and public standards-identity pages. They support board-class and execution-context vocabulary only. They do NOT prove sensor accuracy, navigation performance, qualification pass-status, or mission-system authority.

| Board Family | Application Context | PCB/PCBA Vocabulary Supported |
|---|---|---|
| **MEMS Barometric Altimeter Board** | Pressure-sensing front-end for altitude context; aviation and UAV context | Bosch BMP390, TE MS5611, Infineon DPS310 identity-level vocabulary; compact interface and isolation design context |
| **IMU / Gyroscope / Magnetometer Board** | Inertial navigation, orientation sensing; aerospace-defense and UAV context | Honeywell HG1930 (MEMS IMU), HG2802 (FOG), GG1320AN (RLG) and Bosch BMM350 identity-level vocabulary; sensor-interface and isolation review |
| **EO/IR Imaging Board** | Optical sensor front-end for surveillance, targeting, machine-vision context | Exosens image intensifier, Sony STARVIS CMOS, Lynred IR detector identity-level vocabulary; MIPI/LVDS interface review |
| **Radio Altimeter RF Board** | Radar altimeter (4.2–4.4 GHz) RF transceiver/interface | RF front-end context, FAA altimeter vocabulary at document-family level; NOT exact altitude accuracy, aviation-program proof |
| **Sonar / Ultrasonic Transducer Board** | Underwater acoustic front-end; sonar, hydrophone, beamforming context | TI TUSS4440, TI TDC1000 identity vocabulary; receive-element interface; generic beamforming context; NOT array performance, transmit-voltage, marine qualification |
| **Machine Vision / Video Output Board** | Camera or video output for machine-vision, inspection, imaging applications | GigE Vision, USB3 Vision, HDMI/SDI/PAL-NTSC interface identity vocabulary; NOT video performance or broadcast compliance |
| **GPS/GNSS Receiver Board** | Positioning/navigation front-end board; UAV, automotive, aerospace context | Receiver-system and positioning-context vocabulary; NOT finished-board accuracy, precision navigation claims |
| **UAV Sensor Integration Board** | Sensor fusion, control integration, telemetry for drone/UAV platforms | PX4/MAVLink/ExpressLRS architecture-level vocabulary; UAV sensor-integration board context |

### Fact Cards Supported

| Fact Card | What It Supports |
|---|---|
| `methods-barometric-pressure-sensor-owner-identity-and-interface-boundary` | Barometric pressure sensor owner identity (Bosch, TE, Infineon) and interface boundary |
| `methods-navigation-sensor-technology-owner-identity-boundary` | IMU/FOG/RLG/magnetometer owner identity boundary (Honeywell, Bosch, Bartington) |
| `methods-eo-ir-detector-owner-identity-and-interface-boundary` | EO/IR detector owner identity (Exosens, STARVIS, Lynred) and interface boundary |
| `methods-radio-altimeter-rf-front-end-and-integration-boundary` | Radio altimeter RF front-end and integration boundary |
| `methods-sonar-ultrasonic-transducer-front-end-boundary` | Sonar/ultrasonic transducer front-end vocabulary boundary |
| `methods-hydrophone-and-generic-beamforming-boundary` | Hydrophone and generic beamforming vocabulary boundary |
| `methods-rf-validation-capability` | RF validation (TDR/VNA/OTA/coupon) capability vocabulary |
| `methods-rf-impedance-sparameter-pdn-ota-boundaries` | RF impedance, S-parameters, PDN, OTA boundaries |
| `methods-remote-control-and-drone-control-stack-boundary` | UAV/drone control-stack boundary (PX4, MAVLink, ExpressLRS) |
| `standards-aviation-altimeter-standards-metadata-boundary` | Aviation altimeter standards metadata boundary (DO-160G, DO-254, DO-155, FAA AC/EB) |
| `standards-embedded-imaging-serial-interface-boundary` | MIPI CSI-2/D-PHY/DSI-2, LVDS interface boundary |
| `standards-output-video-and-machine-vision-interface-boundary` | HDMI, SDI, GigE Vision, USB3 Vision output/machine-vision boundary |
| `standards-interface-wireless-positioning-product-level-boundary` | GPS/GNSS/Bluetooth/Wi-Fi wireless positioning product-level boundary |
| `standards-military-environmental-and-emi-qualification-boundary` | MIL-STD-461/810 standards-context boundary |
| `standards-automotive-medical-aerospace-application-qualification-boundary` | Aerospace application qualification boundary |

### Standards Context Supported (Public Sources)

| Standard | What It Supports |
|---|---|
| `DO-160G / DO-254 / DO-155` | Document-family and assurance-boundary vocabulary for aviation; NOT direct qualification, compliance proof, DAL chains |
| `MIL-STD-461 / MIL-STD-810` | Standards-context vocabulary for military environmental/EMI; NOT compliance proof |
| `MIPI CSI-2 / D-PHY / DSI-2` | Sensor/display interface-family identity; NOT protocol compliance, throughput proof |
| `LVDS (TI)` | Display interface identity for sensor/display link; NOT electrical compliance |
| `GigE Vision / USB3 Vision` | Machine-vision interface identity; NOT protocol compliance, real-time performance |
| `GPS/GNSS` | Receiver-system and positioning-context vocabulary; NOT finished-board accuracy proof |
| `HDMI / SDI / PAL-NTSC` | Video output interface identity for thermal/optical imaging context; NOT video-chain performance |

## Stable Facts

- The source layer supports 8 distinct sensor/navigation/imaging board families via owner-backed product pages and public standards-identity sources.
- Sensor performance vocabulary (accuracy, drift, noise, sensitivity) is NOT supported beyond identity-level and interface-design context.
- DO-160G/DO-254/DO-155 vocabulary is supported at document-family and assurance-boundary level; NOT as direct qualification or DAL chains.
- MIL-STD vocabulary is supported at standards-context level only; NOT as pass-status or supplier qualification.
- MIPI/LVDS/GigE/USB3 Vision vocabulary is supported at interface-family identity level; NOT as compliance or performance proof.
- Radio altimeter vocabulary is supported at RF front-end and FAA document-identity level only; NOT as exact altitude accuracy.
- Sonar/hydrophone/beamforming vocabulary is at identity-level and receive-element context; transmit-voltage, array performance, and marine qualification are NOT supported.

## Conditions And Methods

- Use this card to confirm what vocabulary is safe before writing a sensor/navigation/imaging PCB article.
- For barometric sensor owner identity, route to `facts/methods/barometric-pressure-sensor-owner-identity-and-interface-boundary`.
- For IMU/FOG/RLG owner identity, route to `facts/methods/navigation-sensor-technology-owner-identity-boundary`.
- For EO/IR detector vocabulary, route to `facts/methods/eo-ir-detector-owner-identity-and-interface-boundary`.
- For aviation standards context, route to `facts/standards/aviation-altimeter-standards-metadata-boundary`.
- For MIL-STD environmental/EMI vocabulary, route to `facts/standards/military-environmental-and-emi-qualification-boundary`.
- Update `last_reconciled_at` when a new sensor/navigation/imaging wiki boundary page is created.

## Limits And Non-Claims

- Exact sensor accuracy, drift, noise, sensitivity, or range numerics are NOT supported.
- Navigation system performance (position accuracy, heading accuracy) is NOT supported.
- DO-160G/DO-254/DO-155 qualification or compliance proof is NOT supported.
- MIL-STD compliance proof, pass-status, or supplier qualification is NOT supported.
- Sonar/hydrophone array performance, beamforming accuracy, or marine qualification is NOT supported.
- Radio altimeter altitude accuracy or precision navigation claims are NOT supported.
- Qualification proof, defense program history, or mission-system authority is NOT supported.
- Yield, throughput, cost, or lead-time claims are NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|---|---|
| Dedicated sensor/navigation/imaging wiki boundary page | Closed — created and promoted to `active` in P4-177 |
| Companion fact card (this file) | Closed — created in P4-184 |
| Inertial sensor performance vocabulary (accuracy, drift) | Official Honeywell or equivalent datasheet with stable public product specification page |
| MEMS pressure sensor performance vocabulary | Official Bosch, TE, or Infineon dated product specification page |
| Radio altimeter exact altitude vocabulary | Official FAA TSO or aircraft program documentation |
| Sonar array architecture/beamforming performance | Project-specific acoustic engineering records |
| Aviation altimeter DO-160G/DO-254 exact clause vocabulary | Official RTCA document page with stable public URL |
| Military sensor qualification vocabulary (MIL-STD exact clauses) | Official DLA Quick Search document page with stable URL |
