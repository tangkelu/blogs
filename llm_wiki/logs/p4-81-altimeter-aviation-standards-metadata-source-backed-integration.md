# P4-81 Altimeter Aviation Standards Metadata Source-Backed Integration

Date: 2026-05-01

## Purpose

Recover the next narrower authority lane after `P4-80`: the exact `DO-160G`, `DO-254`, and `DO-155` standards family that appears inside `altimeter-pcb.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote `must comply` language, exact section or category claims, exact environmental numerics, DAL chains, `TSO` or airworthiness approval, supplier qualification, or HILPCB-specific aviation readiness claims.

## Inputs Reviewed

- `logs/p4-80-military-environmental-and-emi-standards-source-backed-integration.md`
- `logs/p4-74-barometric-pressure-sensor-owner-source-backed-integration.md`
- `logs/p4-73-radio-altimeter-rf-front-end-source-backed-integration.md`
- `logs/p4-71-targeting-laser-tof-and-pulsed-driver-source-backed-integration.md`
- `/code/blogs/tmps/2026.4.27/en/altimeter-pcb.md`
- existing local support:
  - `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md`
  - `facts/methods/barometric-pressure-sensor-owner-identity-and-interface-boundary.md`
  - `facts/methods/radio-altimeter-rf-front-end-and-integration-boundary.md`
  - `facts/methods/laser-time-of-flight-pulsed-driver-and-safety-boundary.md`
  - `wiki/processes/barometric-altimeter-pressure-sensor-boundaries.md`
  - `wiki/processes/radio-altimeter-rf-front-end-boundaries.md`

## Integrated Source-Backed Lane

### Aviation Altimeter Standards Metadata Boundary

Added source records:

- `faa-ac-21-16g-do160-acceptability-page`
- `rtca-do-160g-product-page`
- `rtca-do-254-product-page`
- `rtca-do-155-product-page`

Reused existing source record:

- `faa-ac-20-152a-page`

Added fact card:

- `standards-aviation-altimeter-standards-metadata-boundary`

Added topic wiki:

- `processes-altimeter-aviation-standards-and-assurance-boundaries`

Supported draft family:

- aviation-standards subset of `/code/blogs/tmps/2026.4.27/en/altimeter-pcb.md`

What is now source-backed:

- exact `DO-160G` may now be used as the named RTCA airborne-equipment environmental-test document family, with FAA `AC 21-16G` recognition context and FAA encouragement of `DO-160G` for new articles
- exact `DO-254` may now be used as the named RTCA airborne electronic hardware design-assurance document, with guarded circuit-board-assembly context
- exact `DO-155` may now be used only as the named RTCA minimum-performance-standard document for airborne low-range radar altimeters
- the `altimeter` draft may now keep these exact document nouns conservatively at standards-metadata and assurance-boundary level while separating barometric, radio-altimeter, and laser subsets

Still blocked:

- `with DO-160 qualification`
- `must comply with DO-160G Section 21`
- exact environmental ranges, sections, categories, or test numerics
- `DO-254` duty chains, `DAL-A/B` obligations, or manufacturing-control claims for a PCB fabricator
- `TSO`, airworthiness, installation approval, supplier qualification, or program proof
- `DO-155` widened beyond the low-range radar-altimeter subset

## Residual Disposition After P4-81

- `altimeter-pcb.md` now has narrow source-backed support for:
  - exact `DO-160G`, `DO-254`, and `DO-155` document-family vocabulary
  - FAA-recognition context for `DO-160G`
  - guarded circuit-board-assembly context for `DO-254`
  - guarded low-range radar-altimeter scope for `DO-155`
- `altimeter-pcb.md` still does not have source-backed support for:
  - `must comply` language
  - exact section or category claims
  - environmental numerics
  - `DAL-A/B` requirement chains
  - `TSO` or supplier-readiness claims

## Draft Line Disposition Preserved

- downgradeable only:
  - the `DO-160` section heading and general `DO-160G` environmental-document framing
  - guarded `DO-155` document-family reference within the radar-altimeter subset
  - high-level `DO-160G` and `DO-254` assurance-context wording
- still blocked:
  - `with DO-160 qualification`
  - `must comply`
  - `DO-160G Section 21` used as direct support
  - `DO-254 requires ... extending to the PCB fabricator`
  - exact temperature, altitude, vibration, and EMI section numerics

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.27` `altimeter-pcb.md` at aviation standards-metadata level only
- next likely action:
  - recover the narrower `hydrophone` plus generic `beamforming` identity lane for `sonar-pcb.md` while keeping naval-program, acoustic-performance, and mission-proof claims blocked
