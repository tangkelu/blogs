# P4-79 Navigation Sensor Technology Owner Source-Backed Integration

Date: 2026-05-01

## Purpose

Recover one narrower authority lane after `P4-78`: the exact navigation-sensor technology nouns that appear inside `gyroscope-pcb.md` and `compass-pcb.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote drift, heading-accuracy, calibration-outcome, qualification, supplier-proof, or HILPCB-specific navigation capability claims.

## Inputs Reviewed

- `logs/p4-69-sensor-navigation-imaging-topic-aggregation.md`
- `logs/p4-78-thermal-imaging-output-video-and-machine-vision-interface-source-backed-integration.md`
- `/code/blogs/tmps/2026.4.27/en/gyroscope-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/compass-pcb.md`
- existing local support:
  - `wiki/processes/sensor-navigation-imaging-pcb-review-boundaries.md`
  - `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`
  - `facts/methods/pcba-first-article-inspection-vs-high-speed-validation-boundary.md`
  - `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md`

## Integrated Source-Backed Lane

### Navigation Sensor Technology Owner Identity Boundary

Added source records:

- `honeywell-hg1930-mems-imu-page`
- `honeywell-hg2802-fiber-optic-gyro-imu-page`
- `honeywell-gg1320an-digital-ring-laser-gyroscope-page`
- `bosch-bmm350-magnetometer-product-page`
- `bartington-mag03-fluxgate-magnetometer-page`

Added fact card:

- `methods-navigation-sensor-technology-owner-identity-boundary`

Added topic wiki:

- `processes-navigation-sensor-technology-review-boundaries`

Supported draft family:

- `/code/blogs/tmps/2026.4.27/en/gyroscope-pcb.md`
- `/code/blogs/tmps/2026.4.27/en/compass-pcb.md`

What is now source-backed:

- the gyroscope subset may now use guarded `MEMS gyroscope`, `fiber-optic gyroscope`, `FOG`, `ring laser gyroscope`, and `RLG` nouns at owner-identity level
- the compass subset may now use guarded `magnetometer` and `fluxgate magnetometer` nouns at owner-identity level
- both drafts may now describe the board conservatively as a navigation-sensor interface, low-noise analog, magnetic-cleanliness, packaging, and staged-validation lane rather than as finished navigation-system proof

Still blocked:

- exact drift, bias stability, angle random walk, heading accuracy, or calibration-outcome claims
- exact jitter, loop-area, ADC, compensation, or sensor-fusion performance claims
- `DO-160`, `MIL-STD-810`, naval qualification, airworthiness, defense-program, or supplier-proof claims
- HILPCB-specific navigation deployment, customer, or program-history claims

## Residual Disposition After P4-79

- `gyroscope-pcb.md` now has narrow source-backed support for:
  - owner-backed `MEMS gyroscope`, `FOG`, and `RLG` technology identity
  - guarded inertial-sensor interface and staged-validation framing through existing review pages
- `compass-pcb.md` now has narrow source-backed support for:
  - owner-backed `magnetometer` and `fluxgate magnetometer` technology identity
  - guarded magnetic-cleanliness and staged-validation framing through existing review pages
- these drafts still do not have source-backed support for:
  - performance numerics
  - military or marine qualification proof
  - deployment or supplier-readiness claims

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.27` `gyroscope-pcb.md` at sensor-technology identity level only
  - `2026.4.27` `compass-pcb.md` at sensor-technology identity level only
- next likely action:
  - keep the combined `RS-170/STANAG 3350` phrase blocked after parallel scouting; if that branch is reopened later, treat `STANAG 3350` and `RS-170` as separate identity-only questions rather than one mixed output-format bucket
  - otherwise prefer another multi-file residual lane inside `2026.4.27` over a weak single-line video-standard cleanup
