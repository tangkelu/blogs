# P4-69 Sensor Navigation Imaging Topic Aggregation

Date: 2026-04-30

## Purpose

Convert the next strongest reusable slice of the `P4-67` batch into prompt-consumable `llm_wiki` data by aggregating the `2026.4.27/en` sensor, navigation, and imaging drafts into one conservative review-boundary page with explicit go / hold classifications.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote draft-originated sensor-technology authority, accuracy numerics, drift or calibration outcomes, detector-performance claims, military or aviation qualification proof, supplier capability claims, or HILPCB-specific program history.

## Inputs Reviewed

- `logs/p4-67-2026-4-27-application-computing-sensor-defense-controller-summary.md`
- `/code/blogs/tmps/2026.4.27/en/accelerometer-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/altimeter-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/compass-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/gyroscope-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/night-vision-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/sonar-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/thermal-imaging-pcb.md`
- existing application, interface-positioning, drone-control-stack, RF test-boundary, RF validation, and qualification-boundary layers already present in `llm_wiki`

## Source Records Reused

No new source-record files were required in this pass.

This aggregation reuses the strongest existing source layers already in `llm_wiki`:

- internal aerospace-defense, drone-UAV, security-equipment, and server-independent application framing
- internal DFM and quality workflow records
- existing GPS.gov positioning context and PX4 / MAVLink / ExpressLRS drone-control identity sources
- existing public RF test-boundary and internal RF validation sources
- existing automotive / medical / aerospace qualification-boundary metadata

## Fact Cards Reused

No new fact-card files were required in this pass.

This topic page aggregates the already-landed reusable method and standards layer:

- `methods-internal-application-scenario-coverage-map`
- `methods-pcba-dfm-dft-dfa-review-gate-positioning`
- `methods-rf-validation-capability`
- `methods-rf-impedance-sparameter-pdn-ota-boundaries`
- `methods-remote-control-and-drone-control-stack-boundary`
- `standards-interface-wireless-positioning-product-level-boundary`
- `standards-automotive-medical-aerospace-application-qualification-boundary`

## Topic Wiki Added

- `wiki/processes/sensor-navigation-imaging-pcb-review-boundaries.md`

This page makes the sensor/navigation/imaging slice of `2026.4.27/en` prompt-consumable for:

- `accelerometer-pcb.md`
- `altimeter-pcb.md`
- `compass-pcb.md`
- `gyroscope-pcb.md`
- `night-vision-pcb.md`
- `sonar-pcb.md`
- `thermal-imaging-pcb.md`

## What This Unlocks

- The sensor and imaging drafts can now be conservatively rewritten as board-role and review-boundary articles rather than as sensor-authority or qualification-proof articles.
- Navigation language can now use GPS / GNSS and UAV-stack vocabulary only at receiver-system or control-stack context level.
- Accelerometer, gyroscope, and compass slugs can now stay at sensor interface, isolation, packaging, and validation-workflow level without pretending to prove exact sensing technology or performance.
- Night-vision and thermal-imaging slugs can now stay at detector-interface, power / packaging pressure, environmental workflow, and staged validation level without claiming detector, cooler, or military-program proof.

## Still Blocked

- exact `MEMS`, `piezoelectric`, `fluxgate`, `FOG`, `ring laser`, `hydrophone`, `focal plane array`, `HVPS`, `NETD`, `ENVG-B`, `FLIR`, or similar product / detector / sensor-family claims used as authority without narrower owner sources
- exact drift, heading, altitude, range, accuracy, sensitivity, shock, radar, acoustic, or imaging-performance numerics
- `DO-160`, defense, marine, military, aerospace, or aviation qualification claims used as supplier or board-readiness proof
- HILPCB-specific capability, defense-program, or deployment claims

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family: `2026.4.27` sensor / navigation / imaging lane
- next likely residual lane:
  - narrower defense / EW / surveillance authority if those drafts must retain exact mission-system language
  - narrower owner or standards authority only if sonar, radar-altimeter, or detector-technology claims must survive beyond the current conservative boundary
