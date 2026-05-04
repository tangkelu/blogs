---
fact_id: "methods-laser-time-of-flight-pulsed-driver-and-safety-boundary"
title: "Laser ToF writing is source-backed only at timing, pulsed-driver, and safety-boundary level"
topic: "laser time-of-flight, pulsed-driver, and safety boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-30"
source_ids:
  - "ti-tdc7200-product-page"
  - "ti-lmh13000-product-page"
  - "noaa-lidar-basics-page"
  - "fda-laser-products-and-instruments-page"
tags: ["laser", "time-of-flight", "lidar", "rangefinder", "pulsed-driver", "targeting", "altimeter", "safety-boundary"]
---

# Canonical Summary

> Current owner and regulator sources support one narrow laser-electronics boundary only: laser-bearing PCB drafts may use `time-of-flight`, `timing path`, `pulsed laser driver`, and `laser safety control` vocabulary at subsystem level. The current evidence layer does not support converting that into military rangefinder authority, weapon-system proof, eye-safe product claims, or exact performance numerics.

## Stable Facts

- Official NOAA lidar material supports the high-level measurement idea that distance can be derived from the round-trip travel time of laser pulses.
- The official TI `TDC7200` page supports `time-to-digital converter` identity and elapsed-time measurement between `START` and `STOP` pulses in time-of-flight contexts.
- The official TI `LMH13000` page supports `laser driver` identity, pulsed-current control, fast-edge timing context, and thermal-protection vocabulary for lidar / time-of-flight subsystems.
- The official FDA laser page supports laser hazard-class, labeling, engineering-control, and risk-communication boundary language.

## Conditions And Methods

- Use this card when `targeting-pcb.md`, `altimeter-pcb.md`, or a future laser-rangefinder / lidar draft needs a safer route than generic military or performance language.
- Safe posture: keep the board role at timing measurement, pulsed-driver segregation, control-path timing, isolation, and safety-control vocabulary.
- Pair this lane with current-carrying, first-article, and qualification-boundary cards when the draft also discusses pulse paths, release governance, or harsh-environment context.
- Keep `laser time-of-flight principle`, `timing hardware`, `pulsed-current driver`, and `laser safety controls` as separate but related layers.

## Limits And Non-Claims

- This card does not authorize exact range, altitude, timing-jitter, pulse-energy, eye-safety, or accuracy numerics.
- It does not authorize military designator, fire-control, ballistic, targeting, or weapon-program authority claims.
- It does not authorize optical-train, detector, beam-shaping, or optical-alignment claims beyond high-level subsystem context.
- It does not authorize supplier qualification, environmental qualification, export-control, or deployment-proof claims.

## Open Questions

- Add exact rangefinder-owner or laser-altimeter-owner sources later if a future draft must retain narrower subsystem identity beyond ToF timing context.
- Add laser-safety standards-owner sources later if a future draft must discuss class-specific controls beyond the FDA overview boundary.

## Source Links

- https://www.ti.com/product/TDC7200
- https://www.ti.com/product/LMH13000
- https://oceanservice.noaa.gov/geodesy/lidar.html
- https://www.fda.gov/radiation-emitting-products/home-business-and-entertainment-products/laser-products-and-instruments
