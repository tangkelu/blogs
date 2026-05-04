---
topic_id: "applications-sensor-navigation-imaging-pcb-review-boundaries"
title: "Sensor Navigation Imaging PCB Review Boundaries"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
activated_at: "2026-05-03"
activation_notes: "P4-177 re-review and repair: Added Standards Context Table (9 standards: DO-160/DO-254/DO-155, MIL-STD-461/810, MIPI/LVDS, HDMI/SDI/PAL/NTSC, GigE/USB3 Vision, GPS/GNSS, Radio Altimeter, Sonar/Hydrophone/Beamforming), Must-Refresh List (10 items: owner pages from Bosch, Honeywell, TE, Exosens, Sony, TI; FAA/RTCA; DLA MIL-STD; RF/OTA), and Cross-Lane Routing Table (11 routes). Retained strong Slug Classification (5 slugs with status labels), Shared Blocked Claim Classes, Drafting Use Notes, and 17 fact cards. Promoted to active."
fact_ids:
  - "methods-internal-application-scenario-coverage-map"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "standards-aviation-altimeter-standards-metadata-boundary"
  - "methods-barometric-pressure-sensor-owner-identity-and-interface-boundary"
  - "methods-eo-ir-detector-owner-identity-and-interface-boundary"
  - "methods-navigation-sensor-technology-owner-identity-boundary"
  - "methods-radio-altimeter-rf-front-end-and-integration-boundary"
  - "methods-sonar-ultrasonic-transducer-front-end-boundary"
  - "methods-hydrophone-and-generic-beamforming-boundary"
  - "methods-rf-validation-capability"
  - "methods-rf-impedance-sparameter-pdn-ota-boundaries"
  - "methods-remote-control-and-drone-control-stack-boundary"
  - "standards-military-environmental-and-emi-qualification-boundary"
  - "standards-embedded-imaging-serial-interface-boundary"
  - "standards-output-video-and-machine-vision-interface-boundary"
  - "standards-interface-wireless-positioning-product-level-boundary"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"
source_ids:
  - "frontendapt-industry-aerospace-defense-page-en"
  - "frontendapt-industry-drone-uav-page-en"
  - "frontendapt-industry-security-equipment-page-en"
  - "faa-ac-21-16g-do160-acceptability-page"
  - "rtca-do-160g-product-page"
  - "rtca-do-254-product-page"
  - "rtca-do-155-product-page"
  - "bosch-bmp390-product-page"
  - "te-ms5611-product-page"
  - "infineon-dps310-datasheet"
  - "honeywell-hg1930-mems-imu-page"
  - "honeywell-hg2802-fiber-optic-gyro-imu-page"
  - "honeywell-gg1320an-digital-ring-laser-gyroscope-page"
  - "bosch-bmm350-magnetometer-product-page"
  - "bartington-mag03-fluxgate-magnetometer-page"
  - "exosens-image-intensifier-tube-page"
  - "sony-starvis-technology-page"
  - "sony-security-camera-image-sensor-products-page"
  - "lynred-about-our-technologies-page"
  - "mipi-csi-2-spec-page"
  - "mipi-d-phy-spec-page"
  - "mipi-dsi-2-spec-page"
  - "mipi-display-command-set-page"
  - "ti-lvds-overview-page"
  - "itu-r-bt470-conventional-analogue-television-systems-page"
  - "hdmi-specifications-and-programs-page"
  - "smpte-top-standards-page"
  - "a3-gige-vision-standard-page"
  - "a3-usb3-vision-standard-page"
  - "faa-pcg-radio-altimeter-glossary-page"
  - "faa-aim-radio-radar-altimeter-anomalies-section"
  - "faa-eb-107-5g-c-band-aero-studies"
  - "faa-ac-20-199-draft-radio-altimeter-installation"
  - "noaa-sonar-basics-page"
  - "noaa-hydrophone-page"
  - "mathworks-isotropic-hydrophone-system-object-page"
  - "mathworks-beamforming-overview-page"
  - "ti-tuss4440-product-page"
  - "ti-tdc1000-product-page"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
  - "frontendapt-dfm-guidelines-resource-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "gps-gov-civil-gps-accuracy-page"
  - "px4-basic-concepts-guide"
  - "mavlink-overview-page"
  - "expresslrs-getting-started"
  - "mil-std-461-emi-control-standard-page"
  - "mil-std-810-environmental-engineering-tests-page"
  - "faa-ac-20-152a-page"
  - "keysight-vna-system-impedance-help"
  - "rohde-schwarz-ts8991-ota-system-page"
tags: ["sensor-interface", "navigation", "imaging", "uav", "security-equipment", "aerospace-defense", "rf-validation", "qualification-boundary", "review-boundary"]
---

# Definition

> Sensor, navigation, and imaging PCB writing is only safe when it stays inside board-level review boundaries: sensor interface role, mixed-signal or RF front-end context, packaging and isolation pressure, UAV or positioning system context, staged validation, and explicit qualification boundaries. The current corpus does not support turning these slugs into exact sensor, detector, or program-authority proof.

## Why This Topic Matters

- The `2026.4.27/en` sensor batch repeatedly mixes valid board-review pressure with unsupported sensor-technology claims, military language, and qualification leakage.
- Existing `llm_wiki` layers are already strong enough to explain why navigation, imaging, and mixed-signal sensing boards need tighter interface, shielding, packaging, and validation review.
- Without one aggregation page, rewrites drift into ungrounded `MEMS`, `FOG`, `laser altimeter`, `HVPS`, `NETD`, `DO-160`, or mission-system language that the current source base cannot safely support at finished-board claim level.

---

## Standards Context Table

| Standard/Technology | Safe Use | Blocked Claims |
|---|---|---|
| **DO-160G / DO-254 / DO-155** | Document-family and assurance-boundary vocabulary for aviation | Direct qualification, compliance proof, DAL-A/B chains, aircraft certification |
| **MIL-STD-461 / MIL-STD-810** | Standards-context vocabulary for military environmental/EMI | Compliance pass-status, supplier-qualification claims, mission-readiness proof |
| **MIPI CSI-2 / D-PHY / DSI-2** | Sensor/display interface-family identity; compact imaging context | Protocol compliance, lane count, Gbps throughput, jitter, latency claims |
| **LVDS (TI)** | Display interface-family identity for sensor/display link | Exact timing, electrical compliance, performance guarantees |
| **HDMI / SDI / PAL/NTSC** | Video output interface identity for thermal imaging | Video-chain performance, broadcast compliance, signal-quality claims |
| **GigE Vision / USB3 Vision** | Machine-vision interface identity | Protocol compliance, performance, real-time guarantees |
| **GPS/GNSS** | Receiver-system and positioning-context level | Finished-board accuracy proof, precision navigation claims |
| **Radio Altimeter (4.2-4.4 GHz)** | RF transceiver/interface posture; subsystem vocabulary | Exact altitude accuracy, pressure-port doctrine, must-comply wording, aviation-program proof |
| **Sonar / Hydrophone / Beamforming** | Identity-level and receive-element vocabulary; generic beamforming context | Array architecture, beamforming performance, transmit-voltage, marine qualification, naval-program proof |

---

## Stable Facts

- The internal application layer already supports aerospace-defense, drone-UAV, and security-equipment hardware as real scenario families rather than as generic marketing labels.
- The current DFM and quality-workflow layer supports early review, access planning, inspection handoff, and staged validation language for mixed-signal and sensor-heavy assemblies.
- The existing GPS / interface boundary layer supports GPS and GNSS only at receiver-system and positioning-context level, not as finished-board accuracy proof.
- The current drone-control-stack layer supports UAV control, autopilot, and telemetry vocabulary only at system-architecture level.
- The new aviation altimeter standards metadata boundary supports guarded `DO-160G`, `DO-254`, and `DO-155` vocabulary only at document-family and assurance-boundary level.
- The new navigation-sensor technology boundary supports guarded `MEMS gyroscope`, `FOG`, `ring laser gyroscope`, `magnetometer`, and `fluxgate magnetometer` vocabulary only at owner-identity level.
- The new radio-altimeter boundary layer supports guarded `radio altimeter` / `radar altimeter` identity, `4.2-4.4 GHz` RF-band context, and transceiver / antenna / interface vocabulary only at subsystem level.
- The new EO/IR detector boundary layer supports guarded `image intensifier tube`, `STARVIS` CMOS image sensor, and cooled / uncooled infrared-detector vocabulary only at owner identity and detector-interface level.
- The new imaging serial-interface boundary layer supports guarded `MIPI CSI-2`, `D-PHY`, `DSI-2`, `Display Command Set`, and `LVDS` vocabulary only at sensor/display interface-family level.
- The new output-video and machine-vision interface boundary layer supports guarded `PAL/NTSC`, `HDMI`, `SDI`, `GigE Vision`, and `USB3 Vision` vocabulary only at interface identity level for the thermal-imaging subset.
- The new military environmental and EMI standards boundary supports guarded `MIL-STD-461` and `MIL-STD-810` vocabulary only at standards-context level, not as board-qualification proof.
- The current RF boundary and validation layers support guarded use of impedance, S-parameters, OTA workflow, TDR, and VNA vocabulary when a draft crosses into radar, RF, or mixed-signal front-end context.
- The new sonar front-end boundary layer supports guarded `active/passive sonar`, transducer-drive, receive-path, and echo-qualification vocabulary only at subsystem front-end level.
- The new hydrophone-and-generic-beamforming boundary supports guarded `hydrophone`, guarded receive-side `hydrophone array`, and generic `beamforming` vocabulary only at identity level.
- The current regulated-application boundary layer supports aerospace and regulated-market vocabulary only as system or program boundary, not as supplier-readiness proof.

## Slug Classification

### `accelerometer-pcb.md`

- Status:
  `go_now_conservative`
- Safe article frame:
  sensor interface layout, isolation or magnetic-cleanliness pressure, multi-axis integration context, packaging and environmental review, and staged validation workflow.
- Required posture:
  keep `IMU`, `navigation`, `heading`, or `shock monitoring` at board-role and system-context level.
- Blocked claims:
  exact `MEMS`, `piezoelectric`, drift, calibration accuracy, shock-threshold, or interference-rejection claims without narrower owner sources.

### `gyroscope-pcb.md`, `compass-pcb.md`

- Status:
  `go_now_conservative`
- Safe article frame:
  owner-backed `MEMS gyroscope`, `FOG`, `ring laser gyroscope`, `magnetometer`, or `fluxgate magnetometer` identity paired with sensor-interface, magnetic-cleanliness or low-noise analog review, packaging, and staged validation workflow.
- Required posture:
  keep exact sensor-technology nouns at owner-identity level and treat the board as a navigation-sensor interface and review lane, not as navigation-grade performance or qualification authority.
- Blocked claims:
  exact drift, heading accuracy, bias stability, calibration accuracy, shock-threshold, interference-rejection, or military / marine qualification claims.

### `altimeter-pcb.md`

- Status:
  `needs_refresh_then_go`
- Why:
  the current corpus now supports UAV / positioning context plus narrow barometric pressure-sensor, laser-altimeter, and radio-altimeter subset lanes, but the draft still leans heavily on aviation qualification, exact RF architecture, and performance language that the current source layer does not directly prove.
- Safe article frame:
  altitude-system board context, guarded `DO-160G`, `DO-254`, and radar-altimeter-only `DO-155` document-family vocabulary, owner-published barometric pressure-sensor vocabulary, laser timing subset, radio-altimeter RF transceiver/interface posture, UAV integration posture, interface isolation, and review workflow.
- Blocked claims:
  exact altitude accuracy, pressure-port or redundancy doctrine, universal radar-altimeter architecture, `must comply` wording, exact `DO-160G` sections or environmental numerics, `DAL-A/B` chains, aircraft qualification, or aviation-program proof.

### `night-vision-pcb.md`, `thermal-imaging-pcb.md`

- Status:
  `go_now_conservative`
- Safe article frame:
  owner-backed detector-family naming, guarded `LVDS` / `MIPI CSI-2` or generic display-interface-family vocabulary, and for `thermal-imaging-pcb.md` only, guarded `PAL/NTSC`, `HDMI`, `SDI`, `GigE Vision`, and `USB3 Vision` identity-level wording around detector-interface and processing-board context, compact packaging pressure, power / thermal / isolation review, environmental workflow, and DFM plus production-test staging.
- Required posture:
  treat `night vision` and `thermal imaging` as imaging-system context with owner-backed detector examples and guarded interface-family nouns only; for `thermal-imaging-pcb.md`, keep exact output or transport names at identity level and continue to block `RS-170` and `STANAG 3350`.
- Blocked claims:
  exact detector architecture or material claims, lane counts, `Gbps`, jitter, latency, `ENVG-B`, `FLIR`, `CCD`, `NETD`, lux / `QE`, cryogenic-cooler performance, `RS-170`, `STANAG 3350`, exact video-standard subtype or compliance claims, optics or video-chain performance, military qualification, or program proof.

### `sonar-pcb.md`

- Status:
  `needs_refresh_then_go`
- Why:
  the current corpus now supports active/passive sonar identity plus transducer-drive, receive-path, echo-qualification, guarded `hydrophone`, guarded receive-side `hydrophone array`, and generic `beamforming` vocabulary, but the draft still leans heavily on architecture, performance, naval-program, and marine-qualification claims that the current source layer does not directly prove.
- Safe article frame:
  active or passive sonar context, transducer-driver versus receive-path segregation, guarded hydrophone receive-element wording, guarded generic beamforming wording, current-path and isolation review, echo-conditioning vocabulary, and staged validation workflow.
- Blocked claims:
  exact hydrophone-array architecture, beamforming implementation or performance, transmit-voltage claims, marine qualification, and naval-program proof.

## Shared Blocked Claim Classes

- exact sensor, detector, material, optics, or subsystem-technology claims beyond current owner-backed identity lanes
- exact accuracy, drift, sensitivity, range, altitude, heading, acoustic, thermal, or radar-performance numerics
- `DO-160`, aerospace, military, marine, defense, qualification, or compliance claims used as supplier or board-readiness proof
- HILPCB capability, customer, deployment, or program-history claims

## Must-Refresh List

| Item | Refresh Trigger |
|---|---|
| DO-160/DO-254/DO-155 revision/status | Before any aviation qualification or DAL-A/B claim |
| Bosch (BMP390, BMM350) product pages | Before any MEMS accelerometer/magnetometer performance claim |
| Honeywell (HG1930, HG2802, GG1320AN) product pages | Before any IMU/FOG/ring laser gyroscope performance claim |
| TE/Infineon pressure sensor pages | Before any barometric altimeter accuracy claim |
| Exosens/Sony/Lynred detector pages | Before any EO/IR detector (image intensifier, STARVIS, IR) performance claim |
| TI (TUSS4440, TDC1000, LVDS) product pages | Before any sonar/transducer/interface timing claim |
| FAA AC/EB/PCG/aim sources | Before any FAA altimeter/radar/aircraft claim |
| RTCA DO-160/DO-254/DO-155 products | Before any RTCA standard citation |
| DLA MIL-STD-461/810 sources | Before any MIL-STD compliance or qualification claim |
| RF/OTA/S-parameter validation sources | Before any radar, antenna, or RF performance claim |

---

## Cross-Lane Routing Table

| Content Type | Route To |
|---|---|
| RF front-end / radar / defense | `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md` |
| EO/IR detector / imaging sensor | `facts/methods/eo-ir-detector-owner-identity-and-interface-boundary` |
| Imaging serial interfaces (MIPI/LVDS) | `facts/standards/embedded-imaging-serial-interface-boundary` |
| Video output (HDMI/SDI/GigE Vision/USB3 Vision) | `facts/standards/output-video-and-machine-vision-interface-boundary` |
| GPS/GNSS / wireless positioning | `facts/standards/interface-wireless-positioning-product-level-boundary` |
| UAV / drone control stack | `facts/methods/remote-control-and-drone-control-stack-boundary` |
| Aviation altimeter standards (DO-160/DO-254/DO-155) | `facts/standards/aviation-altimeter-standards-metadata-boundary` |
| MIL-STD environmental/EMI | `facts/standards/military-environmental-and-emi-qualification-boundary` |
| Sonar / hydrophone / beamforming | `facts/methods/sonar-ultrasonic-transducer-front-end-boundary` |
| DFM/DFT/DFA review gates | `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning` |
| FAI vs RF validation | `facts/methods/pcba-first-article-inspection-vs-high-speed-validation-boundary` |

---

## Drafting Use Notes

- If a rewrite starts from `what sensor technology is best`, stop and reframe around board interface, isolation, packaging, and validation pressure.
- If a rewrite needs GPS, GNSS, Bluetooth, Wi-Fi, or UAV vocabulary, keep it at receiver-system or control-stack context level.
- If a rewrite needs radar, OTA, S-parameters, or RF validation wording, keep the measured layer explicit and avoid finished-system performance claims.
- If a rewrite needs exact `MIL-STD-461` or `MIL-STD-810` wording, keep it at standards-context level and do not convert it into pass-status or supplier-readiness proof.
- If a rewrite needs exact `DO-160G`, `DO-254`, or `DO-155` wording, keep it at document-family and assurance-boundary level and do not convert it into direct qualification or supplier-readiness proof.
- If a rewrite needs aviation, military, or regulated-application language, keep it at program-boundary vocabulary level and do not convert it into supplier qualification proof.

## Related Fact Cards

- `methods-internal-application-scenario-coverage-map`
- `methods-pcba-dfm-dft-dfa-review-gate-positioning`
- `standards-aviation-altimeter-standards-metadata-boundary`
- `methods-barometric-pressure-sensor-owner-identity-and-interface-boundary`
- `methods-eo-ir-detector-owner-identity-and-interface-boundary`
- `methods-radio-altimeter-rf-front-end-and-integration-boundary`
- `methods-sonar-ultrasonic-transducer-front-end-boundary`
- `methods-hydrophone-and-generic-beamforming-boundary`
- `methods-rf-validation-capability`
- `methods-rf-impedance-sparameter-pdn-ota-boundaries`
- `methods-remote-control-and-drone-control-stack-boundary`
- `standards-military-environmental-and-emi-qualification-boundary`
- `standards-embedded-imaging-serial-interface-boundary`
- `standards-interface-wireless-positioning-product-level-boundary`
- `standards-automotive-medical-aerospace-application-qualification-boundary`

## Primary Sources

- /code/hileap/frontendAPT/public/static/industries/en/aerospace-defense-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/drone-uav-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/security-equipment-pcb.json
- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1019280
- https://my.rtca.org/productdetails?id=a1B36000001IcnSEAS
- https://my.rtca.org/productdetails?id=a1B36000001IcjTEAS
- https://my.rtca.org/productdetails?id=a1B36000001IcnqEAC
- https://www.exosens.com/products/image-intensifier-tube
- https://www.sony-semicon.com/en/technology/security/index.html
- https://www.sony-semicon.com/en/products/is/security/index.html
- https://www.lynred.com/about-our-technologies
- https://www.mipi.org/specifications/csi-2
- https://www.mipi.org/specifications/d-phy
- https://www.mipi.org/specifications/dsi-2
- https://www.mipi.org/specifications/display-command-set
- https://www.ti.com/product-category/interface/lvds/overview.html
- https://www.faa.gov/air_traffic/publications/atpubs/pcg_html/glossary-r.html
- https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap7_section_6.html
- https://www.faa.gov/airports/engineering/engineering_briefs/eb_107_5G_Aero_Studies
- https://www.faa.gov/aircraft/draft_docs/ac_20_199
- https://oceanservice.noaa.gov/facts/sonar.html
- https://oceanservice.noaa.gov/facts/hydrophone.html
- https://www.mathworks.com/help/phased/ref/phased.isotropichydrophone-system-object.html
- https://www.mathworks.com/help/phased/beamforming.html
- https://www.ti.com/product/TUSS4440
- https://www.ti.com/product/TDC1000
- /code/hileap/frontendAPT/public/static/pcb/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/microwave-pcb.json
- /code/hileap/frontendAPT/public/static/resources/en/dfm-guidelines.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- https://www.gps.gov/gps-accuracy
- https://docs.px4.io/main/en/getting_started/px4_basic_concepts.html
- https://mavlink.io/en/about/overview.html
- https://www.expresslrs.org/quick-start/getting-started/
- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35789
- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35978
- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1041323
- https://helpfiles.keysight.com/csg/N52xxB/System/System_Impedance.htm
- https://www.rohde-schwarz.com/us/products/test-and-measurement/conformance-test-systems-3gpp-ctia/rs-ts8991-ota-performance-test-system_63493-8444.html
