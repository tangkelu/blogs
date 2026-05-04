---
fact_id: "materials-rogers-ro3003-automotive-radar"
title: "Rogers RO3003 Automotive Radar PTFE Laminate"
topic: "RF microwave materials"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendapt-rf-rogers-json"
tags: ["rogers", "ro3003", "ro3000", "ptfe", "77ghz", "automotive", "radar", "adas", "mmwave"]
---

# Canonical Summary

> Rogers RO3003 is the benchmark substrate for 77 GHz automotive radar (ADAS). PTFE with ceramic filler delivers exceptional Dk stability over temperature and low moisture absorption.

## Stable Facts

### Electrical Properties (@ 10 GHz)
- **Dk**: 3.00 ± 0.04
- **Df**: 0.0010
- **Test Method**: IPC-TM-650 2.5.5.5

### Thermal/Mechanical
- **Thermal Conductivity**: 0.50 W/m·K
- **CTE Z-axis**: 24 ppm/°C
- **Dk vs Temp Stability**: Excellent
- **Moisture Absorption**: 0.04% (typical)

### Key Characteristics
- PTFE with ceramic filler
- Exceptional Dk stability over temperature
- Low moisture absorption for outdoor stability
- Requires plasma desmear
- Benchmark for 77 GHz automotive radar

### Applications
- 77 GHz automotive radar (ADAS)
- mmWave sensors
- RF front-end modules
- Point-to-point microwave links

## Conditions And Methods

- Stocked at APTPCB
- Plasma desmear mandatory for via reliability
- Available as RO3003G2 (enhanced version)
- Compatible with hybrid FR-4 builds

## Limits And Non-Claims

- PTFE processing more demanding than RO4000
- Dk 3.00 requires larger trace widths than high-Dk materials
- Does not guarantee specific radar performance

## Source Links

- Internal: `frontendapt-rf-rogers-json`
- Public: https://aptpcb.com/en/materials/rf-rogers
