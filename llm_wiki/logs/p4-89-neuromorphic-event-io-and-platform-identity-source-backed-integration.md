# P4-89 Neuromorphic Event-IO And Platform Identity Source-Backed Integration

Date: 2026-05-01

## Purpose

Recover the next narrow exact-noun lane for `/code/blogs/tmps/2026.4.29/en/neuromorphic-computing-pcb.md` after the smart-meter, EV-charger, hearing-aid, and satellite follow-on passes. This integration keeps the neuromorphic draft as claim inventory only and upgrades only source-backed platform and event-IO identity nouns.

This pass does not promote electrical-behavior claims, architecture claims, deployment claims, throughput or timing claims, production-readiness claims, or supplier-readiness claims.

## Inputs Reviewed

- `logs/p4-83-2026-4-29-expert-batch-controller-summary.md`
- `logs/p4-87c-neuromorphic-event-io-authority-scout.md`
- `/code/blogs/tmps/2026.4.29/en/neuromorphic-computing-pcb.md`
- existing local support:
  - `facts/methods/high-speed-interface-system-context.md`
  - `wiki/processes/sensor-and-display-serial-interface-review-boundaries.md`
  - `wiki/processes/compute-infrastructure-pcb-review-boundaries.md`

## Integrated Source-Backed Lane

### Neuromorphic Event-IO And Platform Identity Boundary

Added source records:

- `intel-neuromorphic-computing-page`
- `intel-loihi-2-technology-brief-page`
- `brainchip-akida-page`
- `synsense-speck-page`
- `synsense-xylo-page`
- `synsense-dvs-page`
- `pmbus-about-page`
- `pmbus-current-specifications-page`

Added fact card:

- `interfaces-neuromorphic-event-io-and-platform-identity-boundary`

Added topic wiki:

- `processes-neuromorphic-pcb-review-boundaries`

Supported draft family:

- neuromorphic platform / event-IO identity noun subset of `/code/blogs/tmps/2026.4.29/en/neuromorphic-computing-pcb.md`

What is now source-backed:

- exact `Loihi 2` may now be used as an Intel neuromorphic platform noun
- exact `Akida` may now be used as a BrainChip neuromorphic platform noun
- exact `Speck` and `Xylo` may now be used as SynSense neuromorphic product-family nouns
- exact `DVS` may now be used as a SynSense product-family noun in guarded neuromorphic sensor context
- exact `PMBus` may now be used as the Power Management Bus name and specification-family noun

## Boundary Added

The new lane is intentionally identity-only:

- keep `Loihi 2`, `Akida`, `Speck`, `Xylo`, `DVS`, and `PMBus` at owner-backed naming level
- route `neuromorphic-computing-pcb.md` through `processes-neuromorphic-pcb-review-boundaries`
- pair neuromorphic nouns with existing board-review pages before any rewrite
- do not widen this lane into implementation detail, electrical requirements, platform compatibility, or supplier capability

## Blocked Claim Classes

Still blocked after P4-89:

- exact `AER`, `STDP`, `silicon cochlea`, `sub-LVDS`, `COM Express`, or `Jetson-compatible` claims
- exact power, noise, PSRR, skew, jitter, timestamp, thermal, converter-efficiency, layer-count, board-size, turnaround, or production-volume numerics
- any claim that `Loihi 2`, `Akida`, `Speck`, `Xylo`, `DVS`, or `PMBus` proves PCB capability, interoperability, implementation quality, deployment maturity, or production readiness
- any use of `PCIe`, `USB 3.2`, `Ethernet`, or `LVDS` inside the neuromorphic lane without a separate independently sourced boundary
- any claim that neuromorphic products are already shipping in named end markets such as robotics, hearing aids, satellite payloads, medical, defense, or industrial inspection unless separate owner-backed evidence is registered
- any HILPCB-specific capability, validated noise-floor, module-volume, qualification, or supplier-readiness claim

## Residual Disposition After P4-89

- `neuromorphic-computing-pcb.md` now has narrow source-backed support for:
  - exact neuromorphic platform nouns `Loihi 2`, `Akida`, `Speck`, and `Xylo`
  - exact neuromorphic sensor noun `DVS`
  - exact `PMBus` specification-family identity wording
- `neuromorphic-computing-pcb.md` still does not have source-backed support for:
  - event-bus behavior or exact interface implementation claims
  - concept-family nouns such as `AER`, `STDP`, or `silicon cochlea`
  - benchmark, power, timing, thermal, deployment, or qualification claims
  - supplier capability or production-module claims

## Next-Session Handoff

Recommended next session:

- decide whether the rewrite truly needs exact `AER`, `STDP`, `silicon cochlea`, `COM Express`, `Jetson-compatible`, or `sub-LVDS` nouns
- if yes, split those into separate narrow lanes rather than widening P4-89:
  - `AER` and `STDP` likely need literature-backed or owner-technical-document recovery
  - `COM Express` and `Jetson-compatible` need owner or consortium platform-identity recovery
  - `sub-LVDS` needs a narrower interface-source lane beyond the current `LVDS` boundary
- otherwise, rewrite `neuromorphic-computing-pcb.md` conservatively using:
  - `interfaces-neuromorphic-event-io-and-platform-identity-boundary`
  - `processes-neuromorphic-pcb-review-boundaries`
  - existing generic board-review and validation boundaries only when they do not introduce new exact interface nouns

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.29` `neuromorphic-computing-pcb.md` at platform and event-IO identity level only
- next likely action:
  - use the new neuromorphic identity lane for conservative rewrites, then recover only the residual exact nouns that remain necessary for publication
