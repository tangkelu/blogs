---
source_id: "infineon-igbt-discretes-page"
title: "IGBT discretes"
organization: "Infineon Technologies"
source_type: "manufacturer_product_family_page"
url: "https://www.infineon.com/products/power/igbt/igbt-discretes"
jurisdiction: "global"
published_at: ""
checked_at: "2026-04-29"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
topic_tags: ["infineon", "igbt", "collector", "emitter", "gate", "anti-parallel-diode", "high-voltage"]
status: "active"
notes: "Official Infineon IGBT discretes page. Use for IGBT device-class identity, collector/emitter/gate vocabulary, anti-parallel diode packaging boundary, and broad high-voltage application context only."
---

# Source Summary

## What It Covers

- Infineon's official IGBT discrete-device family page
- gate-controlled transistor framing
- collector / emitter / gate terminal vocabulary
- package variants with and without anti-parallel diode
- broad application context including motor drives, solar, UPS, welding, and other industrial power uses

## Why It Matters

- Provides an official owner source for IGBT identity and diode-boundary framing, which are central to a conservative `IGBT vs MOSFET` rewrite boundary.
- Helps separate IGBT device-class facts from draft-originated operating-window and performance claims.

## Extraction Notes

- Safe for IGBT identity as a gate-controlled power device with collector, emitter, and gate terminals.
- Safe for the boundary that an IGBT package may be offered with or without an anti-parallel diode, so a diode is not an inherent universal IGBT property.
- Do not use this page alone for switching-loss, frequency, efficiency, current-density, or replacement-rule claims.

## Refresh Notes

- Refresh before publication if the copy cites current Infineon series names, specific package options, or live product availability.
