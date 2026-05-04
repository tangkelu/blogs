---
fact_id: "methods-barometric-pressure-sensor-owner-identity-and-interface-boundary"
title: "Barometric altimeter writing is source-backed only at pressure-sensor owner identity and interface-boundary level"
topic: "barometric pressure sensor owner identity and interface boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-30"
source_ids:
  - "bosch-bmp390-product-page"
  - "te-ms5611-product-page"
  - "infineon-dps310-datasheet"
tags: ["barometric-altimeter", "pressure-sensor", "bmp390", "ms5611", "dps310", "altimeter", "sensor-interface", "owner-identity"]
---

# Canonical Summary

> Current Bosch, TE, and Infineon owner sources support one narrow barometric lane only: `altimeter` drafts may name exact pressure-sensor families such as `BMP390`, `MS5611`, and `DPS310` as digital absolute / barometric pressure-sensor examples, and may use guarded pressure-plus-temperature, `24-bit`, calibration, and interface vocabulary at subsystem level. The current evidence layer does not support turning that into aviation-altimeter proof, board-accuracy proof, pressure-port design doctrine, or universal barometric-board architecture claims.

## Stable Facts

- Bosch Sensortec publishes `BMP390` as a `24-bit absolute barometric pressure sensor` for altitude-tracking applications and exposes public `I2C` and `SPI` interface vocabulary.
- TE publishes `MS5611` as a `digital pressure and altimeter sensor module` with `absolute` pressure framing and `24 bit ADC` field vocabulary.
- Infineon publishes `DPS310` as a digital barometric pressure sensor that measures pressure and temperature, produces `24 bit` results, and stores factory calibration coefficients for conversion into pressure and temperature values.
- Across these owner sources, it is safe to describe the barometric subset of an altitude board as a digital pressure-sensor lane rather than as a generic `aviation altimeter` authority claim.

## Conditions And Methods

- Use this card when `altimeter-pcb.md` needs a safer route than generic aviation or UAV marketing for the barometric subset.
- Safe posture: keep the board role at digital pressure-sensor integration, pressure / temperature data path, interface hookup, power-and-noise awareness, and conservative altitude-tracking context.
- Pair this lane with existing sensor/navigation review, first-article / release-governance, and qualification-boundary cards when the draft also discusses mixed-signal integration or regulated-program context.
- Keep `barometric pressure sensor`, `radio altimeter`, and `laser altimeter` as separate authority lanes instead of collapsing them into one universal `altimeter PCB` claim.

## Limits And Non-Claims

- This card does not authorize `FAR Part 91.411`, `DO-160`, `DO-254`, `DAL-A/B`, aircraft approval, or airworthiness claims for a PCB, assembly, or supplier.
- It does not authorize exact altitude accuracy, pressure resolution, drift, temperature-compensation performance, or calibration-outcome claims at finished-board or finished-system level.
- It does not authorize redundant-sensor architecture, pressure-port geometry, conformal-coating keepout, wind-screening, or bus-interface claims such as `ARINC 429`, `RS-422`, `CAN`, or `MIL-STD-1553B` unless separately sourced.
- It does not authorize HILPCB deployment, customer, aviation-program, or UAV-production proof.

## Open Questions

- Add narrower owner or standards sources later if a future rewrite must retain pressure-port, environmental, or aircraft-bus authority beyond the current sensor-identity lane.
- Add stronger barometric-system or standards-owner sources later if the draft must retain exact altitude-performance or certified-aircraft barometric language.

## Source Links

- https://www.bosch-sensortec.com/en/products/environmental-sensors/pressure-sensors/bmp390/
- https://www.te.com/en/product-MS561101BA03-50.html
- https://www.infineon.com/assets/row/public/documents/24/49/infineon-dps310-datasheet-en.pdf
