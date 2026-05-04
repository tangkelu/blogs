# P4-75 Fire Control Platform Interface Source-Backed Integration

Date: 2026-04-30

## Purpose

Recover one narrower authority lane after `P4-74`: the `fire control` / platform-interface subset that appears inside `targeting-pcb.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote ballistic computation, weapon release, targeting accuracy, exact environmental qualification, interoperability proof, or HILPCB-specific defense capability claims.

## Inputs Reviewed

- `logs/p4-74-barometric-pressure-sensor-owner-source-backed-integration.md`
- `logs/p4-70-defense-ew-surveillance-targeting-topic-aggregation.md`
- `logs/p4-71-targeting-laser-tof-and-pulsed-driver-source-backed-integration.md`
- `/code/blogs/tmps/2026.4.27/en/targeting-pcb.md`
- existing local support:
  - `wiki/processes/defense-ew-surveillance-targeting-pcb-review-boundaries.md`
  - `facts/standards/interface-wireless-and-positioning-product-level-boundary.md`
  - `facts/methods/laser-time-of-flight-pulsed-driver-and-safety-boundary.md`
  - `facts/methods/pcba-first-article-inspection-vs-high-speed-validation-boundary.md`
  - `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md`

## Integrated Source-Backed Lane

### Fire Control Platform Interface Boundary

Added source records:

- `mil-std-1553-data-bus-page`
- `mil-hdbk-1553-multiplex-application-handbook-page`
- `bosch-can-protocols-page`

Added fact card:

- `methods-fire-control-platform-interface-boundary`

Added topic wiki:

- `processes-fire-control-platform-and-sensor-interface-boundaries`

Supported draft family:

- fire-control / platform-interface subset of `/code/blogs/tmps/2026.4.27/en/targeting-pcb.md`

What is now source-backed:

- the targeting subset may now use guarded `MIL-STD-1553`, `CAN`, `Ethernet`, and GPS receiver-system context as interface-family vocabulary
- the board may now be described conservatively as coordinating sensor-input paths with platform communication links
- the control-board section may now stay at interface-boundary, timing-sensitive partitioning, and staged-validation language rather than generic weapons marketing

Still blocked:

- ballistic computation, firing-solution, target-recognition, or weapon-accuracy claims
- compliance, interoperability, galvanic-isolation, throughput, latency, or redundancy claims for the named interface families
- `MIL-STD-810`, `MIL-STD-461`, supplier qualification, or defense-program proof
- HILPCB-specific military, customer, or deployment claims

## Residual Disposition After P4-75

- `targeting-pcb.md` now has narrow source-backed support for:
  - laser timing / pulsed-driver subset via `P4-71`
  - platform-interface and bus noun family subset via `P4-75`
  - guarded defense-adjacent board-review context through the existing defense targeting page
- `targeting-pcb.md` still does not have source-backed support for:
  - broad fire-control authority
  - ballistic computation claims
  - EO / IR detector or video-interface authority
  - military qualification or supplier-proof claims

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.27` `targeting-pcb.md` at platform-interface boundary level only
- next likely action:
  - recover a narrower EO / IR detector-owner or imaging-interface lane only if future drafts must retain exact optical-sensor nouns beyond the current conservative boundary
