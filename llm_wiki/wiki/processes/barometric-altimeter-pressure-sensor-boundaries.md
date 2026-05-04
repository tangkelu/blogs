---
topic_id: "processes-barometric-altimeter-pressure-sensor-boundaries"
title: "Barometric Altimeter Pressure Sensor Boundaries"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
fact_ids:
  - "standards-aviation-altimeter-standards-metadata-boundary"
  - "methods-barometric-pressure-sensor-owner-identity-and-interface-boundary"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"
source_ids:
  - "faa-ac-21-16g-do160-acceptability-page"
  - "rtca-do-160g-product-page"
  - "rtca-do-254-product-page"
  - "bosch-bmp390-product-page"
  - "te-ms5611-product-page"
  - "infineon-dps310-datasheet"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "faa-ac-20-152a-page"
  - "as9102c-first-article-inspection-page"
tags: ["barometric-altimeter", "pressure-sensor", "bmp390", "ms5611", "dps310", "altimeter", "sensor-interface", "mixed-signal", "routing-boundary"]
---

# Governance Summary

> Barometric-altimeter board writing is safe in this corpus only when it stays at pressure-sensor identity, interface, mixed-signal integration, and staged review-gate level. The active routing posture is: keep named barometric sensors at owner-backed identity level, treat `DO-160G` and `DO-254` as standards-family metadata only, keep `DO-155` out of the barometric lane, and route validation and release language through DFM / first-article / qualification boundaries instead of turning a sensor page into aviation proof.

## Routing Sequence

| Step | Safe question | What this page allows |
|---|---|---|
| 1. Sensor identity | "Which named barometric pressure sensor family is the board integrating?" | Owner-backed sensor identity and guarded vocabulary |
| 2. Measurement path | "What pressure / temperature data path exists at subsystem level?" | Pressure-plus-temperature and interface framing |
| 3. Mixed-signal review | "How should the board be framed in engineering review?" | DFM/DFT/DFA and first-build review language |
| 4. Standards metadata | "Are aviation document names being used only at scope-boundary level?" | `DO-160G` and `DO-254` metadata only; not qualification proof |
| 5. Release boundary | "Is the draft drifting into approval, supplier proof, or exact performance?" | Keep those claims blocked or move them to narrower evidence lanes |

## What This Page Controls

- Use this page when a draft mentions barometric altitude sensing, pressure sensors, or `altimeter` language but only the barometric subset is actually supported.
- Treat `BMP390`, `MS5611`, and `DPS310` as named sensor examples at owner-identity and subsystem-integration level only.
- Keep pressure / temperature conversion, `24-bit`, calibration, and digital-interface wording at guarded feature-identity level.
- Route design assurance, first-article, and regulated-program language through workflow and qualification boundaries rather than through the sensor lane itself.

## Stable Facts

- Bosch Sensortec publicly identifies `BMP390` as a digital `24-bit absolute barometric pressure sensor` for altitude-tracking contexts and exposes `I2C` / `SPI` interface vocabulary.
- TE publicly identifies `MS5611` as a digital pressure and altimeter sensor module with absolute-pressure and `24 bit ADC` framing.
- Infineon publicly identifies `DPS310` as a digital barometric pressure sensor with pressure-plus-temperature measurement, `24-bit` result vocabulary, and factory calibration coefficients.
- Across these owner sources, it is safe to describe the barometric subset as a digital pressure-sensor lane rather than as a general aviation-altimeter authority claim.
- FAA and RTCA public pages support `DO-160G` and `DO-254` as document-family vocabulary for airborne environmental test procedures and airborne electronic hardware design assurance, not as qualification proof for a PCB, PCBA, supplier, or program.
- RTCA `DO-155` is explicitly limited to airborne low-range radar altimeters and must not be imported into the barometric lane.
- Existing DFM / first-article / regulated-application cards support separate discussion of mixed-signal review workflow, first-build confirmation, and regulated-program boundary language.

## Boundary Split

### Sensor Identity And Interface Boundary

- Safe posture: describe the board as integrating one or more digital barometric pressure sensors that provide pressure and temperature data into a wider altitude-related system path.
- Safe vocabulary: digital pressure sensor, absolute pressure, pressure-plus-temperature measurement, `24-bit` result framing, calibration coefficients, `I2C`, and `SPI`.
- Stop line: do not turn named sensor identity into exact altitude accuracy, drift, compensation outcome, or finished-board performance proof.

### Mixed-Signal Review Boundary

- Safe posture: describe conservative mixed-signal review language around interface hookup, power-and-noise awareness, sensor placement context, and first-build review discipline.
- Safe companion layers:
  `methods-pcba-dfm-dft-dfa-review-gate-positioning` and
  `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`.
- Stop line: do not publish exact bus doctrine, noise numerics, layout prescriptions, or signal-validity guarantees from this page.

### Aviation Standards Metadata Boundary

- Safe posture: treat `DO-160G` as airborne-environmental-test document-family vocabulary and `DO-254` as airborne electronic-hardware design-assurance vocabulary.
- Keep `DO-155` out of the barometric subset because it is a low-range radar-altimeter standard, not a barometric-pressure-sensor standard.
- Stop line: do not convert standards names into airworthiness, installation approval, DAL, TSO, or supplier-qualification proof.

### Release And Qualification Boundary

- Safe posture: describe staged validation, first-build confirmation, and regulated-program boundary language around barometric-sensor-bearing boards.
- Safe companion layer:
  `standards-automotive-medical-aerospace-application-qualification-boundary`.
- Stop line: do not imply that sensor identity or early-run review proves a program is approved, certified, or production-ready.

## Safe Draft Routing

### `altimeter-pcb.md`

- Status:
  `partial_support_for_barometric_subset_only`
- Safe angle:
  separate the barometric subset as a digital pressure-sensor integration lane inside a larger altitude-system article, with guarded pressure / temperature path, mixed-signal review, and staged validation language.
- Keep out:
  aviation-grade board doctrine, exact altitude accuracy, redundant-sensor proof, aircraft-bus doctrine, pressure-port geometry, and program-approval claims.

## Common Overclaims To Block

- `barometric altimeter PCB` used as if a named pressure sensor proves a certified aircraft altimeter
- `24-bit pressure sensor` used as if it proves finished-board altitude accuracy
- `DO-160G` or `DO-254` used as if they prove board qualification or supplier approval
- `DO-155` used as if it governs barometric altimeters
- `pressure sensor example` widened into universal architecture, redundancy, or aircraft-bus doctrine
- `consumer or drone sensor page` reused as if it proves aviation or military readiness

## Explicit Blocked Claims

- `aviation qualification proof`: do not claim airworthiness, certification, approval, DAL, TSO, or aviation-program qualification from this page.
- `exact altitude or pressure performance claims`: do not publish exact altitude accuracy, pressure resolution, drift, compensation, noise, or finished-system performance claims.
- `universal architecture and interface doctrine`: do not claim required redundancy, pressure-port geometry, conformal-coating keepout, or aircraft-bus choices such as `ARINC 429`, `RS-422`, `CAN`, or `MIL-STD-1553B` without narrower evidence.
- `supplier-proof or production-readiness claims`: do not claim that a supplier, PCB, or PCBA is aviation-ready, approved, or deployment-proven because the page names a sensor or standards family.

## Must Refresh Before Publishing

- any exact pressure, altitude, drift, calibration, compensation, or noise numeric
- any statement about aircraft bus integration, port geometry, conformal-coating keepout, or environmental hardening
- any claim that moves from sensor identity into aviation qualification, system approval, or supplier proof
- any statement that uses `DO-160G`, `DO-254`, or `DO-155` as if they prove board-level compliance

## Related Fact Cards

- `methods-barometric-pressure-sensor-owner-identity-and-interface-boundary`
- `methods-pcba-dfm-dft-dfa-review-gate-positioning`
- `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`
- `standards-aviation-altimeter-standards-metadata-boundary`
- `standards-automotive-medical-aerospace-application-qualification-boundary`

## Primary Sources

- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1019280
- https://my.rtca.org/productdetails?id=a1B36000001IcnSEAS
- https://my.rtca.org/productdetails?id=a1B36000001IcjTEAS
- https://www.bosch-sensortec.com/en/products/environmental-sensors/pressure-sensors/bmp390/
- https://www.te.com/en/product-MS561101BA03-50.html
- https://www.infineon.com/assets/row/public/documents/24/49/infineon-dps310-datasheet-en.pdf
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1041323
- https://saemobilus.sae.org/standards/as9102c-aerospace-series-first-article-inspection-requirements
