# P4-76 EO/IR Detector Owner Source-Backed Integration

Date: 2026-04-30

## Purpose

Recover one narrower authority lane after `P4-75`: the EO/IR detector-owner subset that appears inside `night-vision-pcb.md`, `thermal-imaging-pcb.md`, and the optical-sensor subset of `targeting-pcb.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote detector performance, optics authority, exact video-chain architecture, military qualification, defense-program proof, or HILPCB-specific imaging or targeting capability claims.

## Inputs Reviewed

- `logs/p4-75-fire-control-platform-interface-source-backed-integration.md`
- `logs/p4-69-sensor-navigation-imaging-topic-aggregation.md`
- `logs/p4-70-defense-ew-surveillance-targeting-topic-aggregation.md`
- `/code/blogs/tmps/2026.4.27/en/night-vision-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/thermal-imaging-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/targeting-pcb.md`
- existing local support:
  - `wiki/processes/sensor-navigation-imaging-pcb-review-boundaries.md`
  - `wiki/processes/defense-ew-surveillance-targeting-pcb-review-boundaries.md`
  - `wiki/processes/fire-control-platform-and-sensor-interface-boundaries.md`
  - `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`
  - `facts/methods/pcba-first-article-inspection-vs-high-speed-validation-boundary.md`
  - `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md`

## Integrated Source-Backed Lane

### EO/IR Detector Owner Identity And Interface Boundary

Added source records:

- `exosens-image-intensifier-tube-page`
- `sony-starvis-technology-page`
- `sony-security-camera-image-sensor-products-page`
- `lynred-about-our-technologies-page`

Added fact card:

- `methods-eo-ir-detector-owner-identity-and-interface-boundary`

Added topic wiki:

- `processes-eo-ir-detector-owner-identity-review-boundaries`

Supported draft family:

- imaging subset of `/code/blogs/tmps/2026.4.27/en/night-vision-pcb.md`
- imaging subset of `/code/blogs/tmps/2026.4.27/en/thermal-imaging-pcb.md`
- optical-sensor subset of `/code/blogs/tmps/2026.4.27/en/targeting-pcb.md`

What is now source-backed:

- the imaging subset may now name owner-backed detector families such as `image intensifier tube`, `STARVIS` CMOS image sensor, and cooled / uncooled infrared detector families
- the subset may now use guarded detector-chain vocabulary such as `photocathode`, `microchannel plate`, `phosphor screen`, `CMOS image sensor`, and `microbolometer`
- the board may now be described conservatively as a detector-interface, readout, conditioning, and processing-board lane rather than as optics, surveillance, or targeting authority

Still blocked:

- exact detector architecture, generation class, detector material, or cryocooler-behavior claims
- exact sensitivity, `QE`, lux, `NETD`, range, resolution, frame-rate, or video-chain outcome claims
- optics, lens, image-registration, target-tracking, target-recognition, surveillance-program, or fire-control outcome claims
- military qualification, defense-program, supplier-proof, or HILPCB deployment / customer claims

## Residual Disposition After P4-76

- `night-vision-pcb.md` now has narrow source-backed support for:
  - image-intensifier detector identity via `P4-76`
  - low-light CMOS detector identity via `P4-76`
  - guarded imaging-system board context through the existing sensor/navigation page
- `thermal-imaging-pcb.md` now has narrow source-backed support for:
  - cooled / uncooled infrared-detector family identity via `P4-76`
  - guarded imaging-system board context through the existing sensor/navigation page
- `targeting-pcb.md` now has narrow source-backed support for:
  - laser timing / pulsed-driver subset via `P4-71`
  - platform-interface and bus noun family subset via `P4-75`
  - optical-sensor detector identity subset via `P4-76`
- these drafts still do not have source-backed support for:
  - exact imaging serial-interface authority
  - detector-performance or optics proof
  - broad surveillance, targeting, or weapon-system authority
  - qualification or supplier-proof claims

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.27` `night-vision-pcb.md` at detector-owner identity level only
  - `2026.4.27` `thermal-imaging-pcb.md` at detector-owner identity level only
  - `2026.4.27` `targeting-pcb.md` at optical-sensor subset identity level only
- next likely action:
  - recover a narrower imaging serial-interface lane such as `MIPI CSI-2`, `MIPI D-PHY`, or `LVDS`, or another exact mission-system authority lane, only if future rewrites must retain those exact nouns
