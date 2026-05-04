# P4-77 Embedded Imaging Serial Interface Source-Backed Integration

Date: 2026-04-30

## Purpose

Recover one narrower authority lane after `P4-76`: the embedded imaging serial-interface subset that appears inside `night-vision-pcb.md`, `thermal-imaging-pcb.md`, and the optical-sensor subset of `targeting-pcb.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote lane counts, bitrates, jitter, latency, serializer / deserializer proof, output-video standard claims, interoperability proof, or HILPCB-specific imaging-interface capability claims.

## Inputs Reviewed

- `logs/p4-76-eo-ir-detector-owner-source-backed-integration.md`
- `logs/p4-75-fire-control-platform-interface-source-backed-integration.md`
- `logs/p4-69-sensor-navigation-imaging-topic-aggregation.md`
- `logs/p4-70-defense-ew-surveillance-targeting-topic-aggregation.md`
- `/code/blogs/tmps/2026.4.27/en/night-vision-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/thermal-imaging-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/targeting-pcb.md`
- existing local support:
  - `wiki/processes/eo-ir-detector-owner-identity-review-boundaries.md`
  - `wiki/processes/fire-control-platform-and-sensor-interface-boundaries.md`
  - `wiki/processes/sensor-navigation-imaging-pcb-review-boundaries.md`
  - `wiki/processes/defense-ew-surveillance-targeting-pcb-review-boundaries.md`
  - `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`
  - `facts/methods/pcba-first-article-inspection-vs-high-speed-validation-boundary.md`

## Integrated Source-Backed Lane

### Embedded Imaging Serial Interface Boundary

Added source records:

- `mipi-csi-2-spec-page`
- `mipi-d-phy-spec-page`
- `mipi-dsi-2-spec-page`
- `mipi-display-command-set-page`
- `ti-lvds-overview-page`

Added fact card:

- `standards-embedded-imaging-serial-interface-boundary`

Added topic wiki:

- `processes-sensor-and-display-serial-interface-review-boundaries`

Supported draft family:

- imaging subset of `/code/blogs/tmps/2026.4.27/en/night-vision-pcb.md`
- imaging subset of `/code/blogs/tmps/2026.4.27/en/thermal-imaging-pcb.md`
- optical-sensor subset of `/code/blogs/tmps/2026.4.27/en/targeting-pcb.md`

What is now source-backed:

- the imaging subset may now use guarded `MIPI CSI-2`, `D-PHY`, `DSI-2`, `Display Command Set`, and `LVDS` interface-family vocabulary
- the subset may now describe a board conservatively as carrying sensor, camera, display, or serial-link interface paths around detector and processing sections
- the targeting optical-sensor subset may now keep `LVDS` or `MIPI CSI-2` nouns at interface-family level when paired with the detector-owner and platform-interface lanes

Still blocked:

- exact lane counts, `Gbps`, jitter, latency, ripple, frame-rate, or serializer / deserializer claims
- `PAL/NTSC`, `RS-170`, `STANAG 3350`, `HDMI`, `SDI`, `GigE Vision`, `USB3 Vision`, `PCIe`, `DDR4`, `MIL-STD-1553`, or `CAN` claims unless separately sourced
- interoperability, compliance, or product-validation claims for any imaging serial interface family
- HILPCB-specific interface validation, qualification, or customer-program proof

## Residual Disposition After P4-77

- `night-vision-pcb.md` now has narrow source-backed support for:
  - detector-owner identity via `P4-76`
  - embedded imaging serial-interface nouns via `P4-77`
  - guarded imaging-system board context through the existing sensor/navigation page
- `thermal-imaging-pcb.md` now has narrow source-backed support for:
  - detector-owner identity via `P4-76`
  - guarded `LVDS` plus generic display-interface-family wording via `P4-77`
  - guarded imaging-system board context through the existing sensor/navigation page
- `targeting-pcb.md` now has narrow source-backed support for:
  - laser timing / pulsed-driver subset via `P4-71`
  - platform-interface and bus noun family subset via `P4-75`
  - optical-sensor detector identity subset via `P4-76`
  - optical-sensor serial-interface nouns via `P4-77`
- these drafts still do not have source-backed support for:
  - exact output-video-standard authority
  - detector or interface performance proof
  - broad surveillance, targeting, or weapon-system authority
  - qualification or supplier-proof claims

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.27` `night-vision-pcb.md` at detector-owner plus imaging-interface identity level only
  - `2026.4.27` `thermal-imaging-pcb.md` at detector-owner plus imaging-interface identity level only
  - `2026.4.27` `targeting-pcb.md` at optical-sensor subset interface identity level only
- next likely action:
  - recover a narrower output-video or military-video-standard lane only if future rewrites must retain exact `HDMI`, `SDI`, `RS-170`, or `STANAG` nouns, otherwise shift effort back to conservative rewrite consumption
