# P4-71 Targeting Laser ToF And Pulsed Driver Source-Backed Integration

Date: 2026-04-30

## Purpose

Recover one narrower authority lane after `P4-70`: the laser time-of-flight, pulsed-driver, and safety-control subset that appears inside `targeting-pcb.md` and touches the laser-altimeter subset of `altimeter-pcb.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote fire-control authority, weapon-system proof, exact range or altitude accuracy, pulse-energy numerics, eye-safe product claims, environmental-qualification outcomes, or HILPCB-specific defense capability claims.

## Inputs Reviewed

- `logs/p4-70-defense-ew-surveillance-targeting-topic-aggregation.md`
- `/code/blogs/tmps/2026.4.27/en/targeting-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/altimeter-pcb.md`
- existing local support:
  - `facts/methods/current-carrying-trace-width-and-copper-boundary.md`
  - `facts/methods/pcba-first-article-inspection-vs-high-speed-validation-boundary.md`
  - `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md`
  - `wiki/processes/defense-ew-surveillance-targeting-pcb-review-boundaries.md`
  - `wiki/processes/sensor-navigation-imaging-pcb-review-boundaries.md`

## Integrated Source-Backed Lane

### Laser Time-Of-Flight And Pulsed-Driver Boundary

Added source records:

- `ti-tdc7200-product-page`
- `ti-lmh13000-product-page`
- `noaa-lidar-basics-page`
- `fda-laser-products-and-instruments-page`

Added fact card:

- `methods-laser-time-of-flight-pulsed-driver-and-safety-boundary`

Added topic wiki:

- `processes-laser-time-of-flight-and-pulsed-driver-boundaries`

Supported draft family:

- `/code/blogs/tmps/2026.4.27/en/targeting-pcb.md`
- laser-altimeter subset of `/code/blogs/tmps/2026.4.27/en/altimeter-pcb.md`

What is now source-backed:

- laser-bearing PCB drafts may use official `time-of-flight` and `time-to-digital converter` vocabulary at subsystem timing-path level
- pulsed laser-driver sections may be described as isolated current-control and fast-edge review problems rather than as generic `military laser` claims
- laser-related drafts may use regulator-backed hazard-class, labeling, and engineering-control boundary language
- the `targeting` draft now has a narrower prompt-consumable route if it is reframed as laser timing/control-board content rather than fire-control or weapon authority

Still blocked:

- exact rangefinding, altitude, jitter, pulse-current, pulse-width, optical power, eye-safe, or accuracy numerics
- fire-control, ballistic, targeting, designator, weapon-program, or military deployment proof
- environmental qualification, export-control, or supplier-approval claims
- HILPCB-specific defense, targeting, or fielded-program claims

## Residual Disposition After P4-71

- `targeting-pcb.md` now has narrow source-backed support for:
  - laser time-of-flight subsystem context
  - pulsed-driver board-section vocabulary
  - safety-control and release-boundary language
- `targeting-pcb.md` still does not have source-backed support for:
  - fire-control-system authority
  - weapon-system or ballistic-computation claims
  - military qualification or deployment proof
- `altimeter-pcb.md` gains only a narrow laser-altimeter subset route; radar-altimeter and aviation claims remain blocked

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.27` `targeting-pcb.md` at laser ToF and pulsed-driver boundary level only
  - `2026.4.27` `altimeter-pcb.md` at laser-altimeter subset level only
- next likely action:
  - recover a narrower radar-altimeter or sonar authority lane, or a fire-control / interface-authority lane, only if future drafts must retain those exact subsystem nouns
