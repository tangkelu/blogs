# P4-74 Barometric Pressure Sensor Owner Source-Backed Integration

Date: 2026-04-30

## Purpose

Recover one narrower authority lane after `P4-73`: the `barometric altimeter` pressure-sensor subset that appears inside `altimeter-pcb.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote aircraft qualification, exact altitude numerics, pressure-port geometry, redundant-sensor architecture, environmental qualification, or HILPCB-specific aviation / UAV capability claims.

## Inputs Reviewed

- `logs/p4-73-radio-altimeter-rf-front-end-source-backed-integration.md`
- `logs/p4-69-sensor-navigation-imaging-topic-aggregation.md`
- `/code/blogs/tmps/2026.4.27/en/altimeter-pcb.md`
- existing local support:
  - `wiki/processes/sensor-navigation-imaging-pcb-review-boundaries.md`
  - `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`
  - `facts/methods/pcba-first-article-inspection-vs-high-speed-validation-boundary.md`
  - `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md`

## Integrated Source-Backed Lane

### Barometric Pressure Sensor Owner Identity And Interface Boundary

Added source records:

- `bosch-bmp390-product-page`
- `te-ms5611-product-page`
- `infineon-dps310-datasheet`

Added fact card:

- `methods-barometric-pressure-sensor-owner-identity-and-interface-boundary`

Added topic wiki:

- `processes-barometric-altimeter-pressure-sensor-boundaries`

Supported draft family:

- barometric subset of `/code/blogs/tmps/2026.4.27/en/altimeter-pcb.md`

What is now source-backed:

- the barometric subset may now name exact pressure-sensor families such as `BMP390`, `MS5611`, and `DPS310` as owner-backed examples
- the subset may now use guarded digital barometric-pressure, pressure-plus-temperature, `24-bit`, calibration, and sensor-interface vocabulary
- the board may now be described conservatively as a digital pressure-sensor integration lane inside a larger altitude-system board rather than as a certified aircraft altimeter

Still blocked:

- exact altitude accuracy, pressure resolution, drift, compensation, or noise numerics used as finished-system proof
- pressure-port geometry, conformal-coating keepout, redundant-sensor architecture, and bus-interface doctrine
- `FAR Part 91.411`, `DO-160`, `DO-254`, `DAL-A/B`, aircraft approval, or supplier-readiness claims
- HILPCB-specific aviation, UAV production, or customer-program proof

## Residual Disposition After P4-74

- `altimeter-pcb.md` now has narrow source-backed support for:
  - barometric pressure-sensor subset via `P4-74`
  - laser-altimeter subset via `P4-71`
  - radio-altimeter / radar-altimeter subset via `P4-73`
  - guarded altitude-system board-context language through the existing sensor/navigation page
- `altimeter-pcb.md` still does not have source-backed support for:
  - broad aviation qualification claims
  - exact barometric board architecture or pressure-port rules
  - exact RF architecture or performance claims
  - supplier-proof or aircraft-program proof

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.27` `altimeter-pcb.md` at barometric pressure-sensor owner-boundary level only
- next likely action:
  - recover a narrower fire-control / interface-authority lane for `targeting-pcb.md`, or another exact imaging / mission-system authority lane, only if future drafts must retain those exact nouns
