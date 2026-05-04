# Lane Log: P4-184 Sensor Navigation Imaging Application Fact Card

## Task Metadata

| Field | Value |
|-------|-------|
| `task_id` | `p4-184-sensor-navigation-imaging-application-fact-card` |
| `status` | `completed` |
| `owner` | `cascade` |
| `lane` | `sensor-navigation-imaging application fact-card extraction` |
| `completed_at` | `2026-05-03` |

---

## Write Scope Completed

| File | Type | Description |
|---|---|---|
| `facts/applications/sensor-navigation-imaging-coverage-gap-map.md` | **NEW** | Companion fact card for the sensor/navigation/imaging application lane |
| `logs/p4-184-sensor-navigation-imaging-application-fact-card.md` | **NEW** | This lane log |

---

## Extraction Summary

Fact card created by extracting structured coverage information from `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md` (active as of P4-177) and cross-referencing against 17 related sensor/altimeter/imaging fact cards.

**Board families documented:** 8 (MEMS barometric altimeter, IMU/gyroscope/magnetometer, EO/IR imaging, radio altimeter RF, sonar/ultrasonic transducer, machine vision/video output, GPS/GNSS receiver, UAV sensor integration)

**Fact cards documented:** 15 (barometric-pressure-sensor, navigation-sensor-owner-identity, eo-ir-detector, radio-altimeter-rf, sonar-ultrasonic, hydrophone-beamforming, rf-validation, rf-impedance-sparameter, remote-control-drone, aviation-altimeter-standards, embedded-imaging-serial, output-video-machine-vision, interface-wireless-positioning, military-environmental-emi, automotive-medical-aerospace-qualification)

**Standards documented:** 7 (DO-160G/DO-254/DO-155, MIL-STD-461/810, MIPI CSI-2/D-PHY/DSI-2, LVDS/TI, GigE Vision/USB3 Vision, GPS/GNSS, HDMI/SDI/PAL-NTSC)

**Sources documented:** Rich source set including Bosch, Honeywell (HG1930/HG2802/GG1320AN), TE, Infineon, Exosens, Sony, Lynred, TI, FAA, RTCA, NOAA, Bartington (38 total sources)

**Remaining gaps documented:** 7 (inertial sensor performance vocabulary, MEMS pressure sensor performance, radio altimeter exact altitude, sonar array/beamforming, DO-160G/DO-254 clause-level, MIL-STD exact clauses)

---

## Blocked Claims (Maintained)

- Exact sensor accuracy, drift, noise, sensitivity, or range numerics
- Navigation system performance (position accuracy, heading accuracy)
- DO-160G/DO-254/DO-155 qualification or compliance proof
- MIL-STD compliance proof, pass-status, or supplier qualification
- Sonar/hydrophone array performance, beamforming accuracy
- Radio altimeter altitude accuracy or precision navigation claims
- Qualification proof, defense program history, or mission-system authority
- Yield, cost, lead-time claims

---

## Completion Status

**Status:** `completed` — fact card created for sensor/navigation/imaging companion gap mapping.
