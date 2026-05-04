# P4-82 Sonar Hydrophone And Generic Beamforming Source-Backed Integration

Date: 2026-05-01

## Purpose

Recover the next narrower authority lane after `P4-81`: the exact `hydrophone`, `hydrophone array`, and generic `beamforming` nouns that still appear inside `sonar-pcb.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote naval-program proof, exact hydrophone-array architecture, channel counts, simultaneous-sampling requirements, FPGA implementation claims, target bearing / range / velocity extraction, exact acoustic-performance numerics, marine qualification claims, or HILPCB-specific sonar capability claims.

## Inputs Reviewed

- `logs/p4-72-sonar-transducer-front-end-source-backed-integration.md`
- `logs/p4-81-altimeter-aviation-standards-metadata-source-backed-integration.md`
- `wiki/processes/sonar-and-ultrasonic-transducer-front-end-boundaries.md`
- `wiki/processes/sensor-navigation-imaging-pcb-review-boundaries.md`
- `/code/blogs/tmps/2026.4.27/en/sonar-pcb.md`
- existing local support:
  - `facts/methods/sonar-ultrasonic-transducer-front-end-boundary.md`
  - `facts/methods/current-carrying-trace-width-and-copper-boundary.md`
  - `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`
  - `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md`

## Integrated Source-Backed Lane

### Hydrophone And Generic Beamforming Boundary

Added source records:

- `noaa-hydrophone-page`
- `mathworks-isotropic-hydrophone-system-object-page`
- `mathworks-beamforming-overview-page`

Reused existing source record:

- `noaa-sonar-basics-page`

Added fact card:

- `methods-hydrophone-and-generic-beamforming-boundary`

Updated topic wiki:

- `processes-sonar-and-ultrasonic-transducer-front-end-boundaries`
- `processes-sensor-navigation-imaging-pcb-review-boundaries`

Supported draft family:

- `/code/blogs/tmps/2026.4.27/en/sonar-pcb.md`

What is now source-backed:

- `hydrophone` may now be used as an underwater acoustic receive-device or receive-element noun
- `hydrophone array` may now be used only as multiple hydrophones used together on the receive side
- `beamforming` may now be used only as generic array-processing or spatial-filtering vocabulary
- the `sonar` draft may now keep these exact nouns conservatively while still routing board-role language through the existing sonar transducer-front-end boundary

Still blocked:

- `naval hydrophone arrays` or any naval-program framing
- `beamforming processors`, `beamforming boards`, or real-time FPGA implementation claims
- channel counts, simultaneous-sampling rules, phase matching, target bearing / range / velocity extraction, or acoustic imaging claims
- exact noise-floor, isolation, sensitivity, bandwidth, power, or other performance numerics
- marine qualification, submarine deployment, supplier qualification, or HILPCB sonar-program proof

## Residual Disposition After P4-82

- `sonar-pcb.md` now has narrow source-backed support for:
  - active / passive sonar identity
  - transducer-driver versus receive-path vocabulary
  - guarded `hydrophone` and `hydrophone array` receive-side wording
  - guarded generic `beamforming` array-processing wording
- `sonar-pcb.md` still does not have source-backed support for:
  - exact hydrophone-array architecture
  - beamforming implementation or performance claims
  - naval qualification, deployment proof, or marine-environment survival claims

## Queue Note

- `/code/blogs/tmps/2026.4.29/en` has now been added to the next learning queue as a new expert-written batch, but it has not yet been made deletion-safe or source-backed.

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.27` `sonar-pcb.md` at hydrophone and generic beamforming identity level only
- next likely action:
  - start deletion-safe intake and claim-family routing for `/code/blogs/tmps/2026.4.29/en` while keeping the combined `RS-170 / STANAG 3350` phrase and other unsupported performance claims blocked
