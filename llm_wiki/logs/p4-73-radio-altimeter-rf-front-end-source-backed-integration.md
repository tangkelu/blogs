# P4-73 Radio Altimeter RF Front-End Source-Backed Integration

Date: 2026-04-30

## Purpose

Recover one narrower authority lane after `P4-72`: the `radio altimeter` / `radar altimeter` identity, RF-band, and subsystem-boundary subset that appears inside `altimeter-pcb.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote aviation qualification, exact altitude or RF-performance numerics, universal material or layer-stack claims, product certification, or HILPCB-specific aviation-program claims.

## Inputs Reviewed

- `logs/p4-69-sensor-navigation-imaging-topic-aggregation.md`
- `logs/p4-71-targeting-laser-tof-and-pulsed-driver-source-backed-integration.md`
- `/code/blogs/tmps/2026.4.27/en/altimeter-pcb.md`
- existing local support:
  - `facts/methods/rf-impedance-sparameter-pdn-ota-boundaries.md`
  - `facts/methods/rf-validation-capability.md`
  - `facts/methods/pcba-first-article-inspection-vs-high-speed-validation-boundary.md`
  - `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md`
  - `wiki/processes/sensor-navigation-imaging-pcb-review-boundaries.md`
  - `wiki/processes/laser-time-of-flight-and-pulsed-driver-boundaries.md`

## Integrated Source-Backed Lane

### Radio Altimeter RF Front-End And Integration Boundary

Added source records:

- `faa-pcg-radio-altimeter-glossary-page`
- `faa-aim-radio-radar-altimeter-anomalies-section`
- `faa-eb-107-5g-c-band-aero-studies`
- `faa-ac-20-199-draft-radio-altimeter-installation`

Added fact card:

- `methods-radio-altimeter-rf-front-end-and-integration-boundary`

Added topic wiki:

- `processes-radio-altimeter-rf-front-end-boundaries`

Supported draft family:

- radio-altimeter subset of `/code/blogs/tmps/2026.4.27/en/altimeter-pcb.md`

What is now source-backed:

- `radar altimeter` and `radio altimeter` may now be treated as the same aircraft-system noun family
- the radio-altimeter subset may now use direct height-above-terrain system-role language rather than generic avionics marketing
- the subset may now use guarded `4.2-4.4 GHz` RF-band context
- the board may now be described conservatively as a transceiver / antenna-path / RF-cabling / display-interface subsystem rather than as a certified aviation product

Still blocked:

- exact accuracy, resolution, latency, range, delay, gain, isolation, or other RF / altitude numerics
- universal claims about Rogers, PTFE, hybrid stackups, layer counts, heavy copper, antenna topology, or return loss
- `DO-160`, `DO-155`, `DO-254`, `TSO`, `DAL-A/B`, airworthiness, or supplier-approval claims
- HILPCB-specific aviation, airline, military, or fielded-program claims

## Residual Disposition After P4-73

- `altimeter-pcb.md` now has narrow source-backed support for:
  - laser-altimeter subset via `P4-71`
  - radio-altimeter / radar-altimeter subset via `P4-73`
  - guarded altitude-system board-context language through the existing sensor/navigation page
- `altimeter-pcb.md` still does not have source-backed support for:
  - broad aviation qualification claims
  - barometric exact-sensor authority
  - exact RF architecture or performance claims
  - supplier-proof or aircraft-program proof

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.27` `altimeter-pcb.md` at radio-altimeter RF-front-end boundary level only
- next likely action:
  - recover a narrower fire-control / interface-authority lane for `targeting-pcb.md`, or a barometric-sensor-owner lane for the remaining `altimeter` residue, only if future drafts must retain those exact nouns
