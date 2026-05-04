---
fact_id: "materials-taconic-tlx-moderate-loss-ptfe"
title: "Taconic TLX Moderate-Loss PTFE RF Laminate"
topic: "RF microwave materials"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendapt-taconic-pcb-json"
tags: ["taconic", "tlx", "ptfe", "rf-laminate", "moderate-loss", "base-station", "gps"]
---

# Canonical Summary

> Taconic TLX is a moderate-loss PTFE laminate with slightly higher Dk than TLY, enabling more compact microstrip trace geometries while maintaining good dimensional stability.

## Stable Facts

### Electrical Properties (@ 10 GHz)
- **Dk**: 2.55 ± 0.04
- **Df**: 0.0019
- **Test Method**: IPC-TM-650 2.5.5.5

### Mechanical/Thermal
- **CTE X/Y**: 15 ppm/°C
- **CTE Z**: 280 ppm/°C
- **Thermal Conductivity**: 0.26 W/m·K

### Key Characteristics
- Moderate-loss PTFE (higher Dk than TLY)
- More compact microstrip geometries possible
- Good balance of electrical performance and dimensional stability
- Plasma desmear required
- Woven E-glass reinforced

### Applications
- Base-station duplexers and bandpass filters
- Wilkinson power dividers
- GPS/GNSS patch arrays
- Radar transmit/receive modules

## Conditions And Methods

- Dk 2.55 enables ~15% smaller trace width vs. TLY for same impedance
- Plasma desmear mandatory for reliable vias
- Suitable for moderate-frequency RF applications

## Limits And Non-Claims

- Not for ultra-low-loss applications (use TLY instead)
- CTE Z similar to other PTFE materials
- Processing requires same care as TLY

## Source Links

- Internal: `frontendapt-taconic-pcb-json`
- Public: https://aptpcb.com/en/materials/taconic-pcb
