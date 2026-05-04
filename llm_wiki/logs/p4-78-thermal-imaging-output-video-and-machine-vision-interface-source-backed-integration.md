# P4-78 Thermal Imaging Output Video And Machine Vision Interface Source-Backed Integration

Date: 2026-04-30

## Purpose

Recover one narrower authority lane after `P4-77`: the exact output-video and machine-vision interface nouns that appear inside `thermal-imaging-pcb.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote `RS-170`, `STANAG 3350`, subtype or bitrate proof, interoperability proof, compliance proof, or HILPCB-specific thermal-imaging interface capability claims.

## Inputs Reviewed

- `logs/p4-77-embedded-imaging-serial-interface-source-backed-integration.md`
- `logs/p4-76-eo-ir-detector-owner-source-backed-integration.md`
- `logs/p4-69-sensor-navigation-imaging-topic-aggregation.md`
- `/code/blogs/tmps/2026.4.27/en/thermal-imaging-pcb.md`
- existing local support:
  - `wiki/processes/sensor-navigation-imaging-pcb-review-boundaries.md`
  - `wiki/processes/sensor-and-display-serial-interface-review-boundaries.md`
  - `facts/standards/interface-wireless-and-positioning-product-level-boundary.md`
  - `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`
  - `facts/methods/pcba-first-article-inspection-vs-high-speed-validation-boundary.md`

## Integrated Source-Backed Lane

### Output Video And Machine Vision Interface Boundary

Added source records:

- `itu-r-bt470-conventional-analogue-television-systems-page`
- `hdmi-specifications-and-programs-page`
- `smpte-top-standards-page`
- `a3-gige-vision-standard-page`
- `a3-usb3-vision-standard-page`

Added fact card:

- `standards-output-video-and-machine-vision-interface-boundary`

Added topic wiki:

- `processes-output-video-and-machine-vision-interface-review-boundaries`

Supported draft family:

- imaging subset of `/code/blogs/tmps/2026.4.27/en/thermal-imaging-pcb.md`

What is now source-backed:

- the thermal-imaging subset may now use guarded legacy analogue-video wording adjacent to `PAL` / `NTSC`
- the subset may now use guarded `HDMI` and `SDI` nouns at digital-video-interface family level
- the subset may now use guarded `GigE Vision` and `USB3 Vision` nouns at machine-vision transport-interface family level
- the draft may now distinguish sensor-side serial links from downstream output or transport interfaces rather than collapsing all of them into generic `video output` wording

Still blocked:

- exact `RS-170` or `STANAG 3350` authority
- exact `PAL` versus `NTSC` implementation detail, regional doctrine, or standards-equivalence claims
- exact SDI subtype, HDMI version, bitrate, cable-length, frame-rate, latency, compression, or interoperability claims
- any compliance, certification, or qualified-product statement for `HDMI`, `SDI`, `GigE Vision`, or `USB3 Vision`
- HILPCB-specific thermal-imaging product validation, qualification, or customer-program proof

## Residual Disposition After P4-78

- `thermal-imaging-pcb.md` now has narrow source-backed support for:
  - cooled / uncooled detector-family identity via `P4-76`
  - guarded `LVDS` and generic sensor/display serial-interface wording via `P4-77`
  - guarded `PAL/NTSC`, `HDMI`, `SDI`, `GigE Vision`, and `USB3 Vision` identity via `P4-78`
- `night-vision-pcb.md`, `surveillance-pcb.md`, and `targeting-pcb.md` do not participate in this exact lane as currently written
- the imaging subset still does not have source-backed support for:
  - exact `RS-170` or `STANAG 3350` authority
  - detector or interface performance proof
  - military qualification, supplier-proof, or deployment claims

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.27` `thermal-imaging-pcb.md` at output-video and machine-vision interface identity level only
- next likely action:
  - use the new lane for conservative thermal-imaging rewrites, then decide whether exact `RS-170` / `STANAG 3350` or another residual mission-system gap deserves the next narrow recovery pass
