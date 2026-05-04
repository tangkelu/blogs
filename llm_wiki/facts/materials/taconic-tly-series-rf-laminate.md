---
fact_id: "materials-taconic-tly-series-rf-laminate"
title: "Taconic TLY/TLY-5A Ultra-Low-Loss PTFE RF Laminate"
topic: "RF microwave materials"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendapt-taconic-pcb-json"
tags: ["taconic", "tly", "ptfe", "rf-laminate", "ultra-low-loss", "satellite", "ka-band"]
---

# Canonical Summary

> Taconic TLY and TLY-5A are ultra-low-loss PTFE laminates with woven E-glass reinforcement. TLY-5A offers improved dimensional stability over standard TLY. Both require plasma desmear for reliable via metallization.

## Stable Facts

### Electrical Properties (@ 10 GHz)
- **Dk**: 2.17 ± 0.02 (TLY-5A)
- **Dk**: 2.33 ± 0.02 (TLY-3 variant)
- **Df**: 0.0009
- **Test Method**: IPC-TM-650 2.5.5.5 (clamped stripline resonator)

### Mechanical/Thermal
- **CTE X/Y**: 25 ppm/°C (TLY-5A), 18 ppm/°C (TLY-3)
- **CTE Z**: 280 ppm/°C
- **Thermal Conductivity**: 0.23 W/m·K (TLY-5A), 0.26 W/m·K (TLY-3)
- **Moisture Absorption**: 0.02% (very low)

### Key Characteristics
- Lowest-loss Taconic laminate series
- Woven fiberglass provides mechanical stability
- PTFE matrix delivers ultra-low dielectric loss
- Requires plasma desmear (not standard chemistry)
- Very low moisture absorption

### Applications
- Satellite LNA boards
- Ka-band phased-array antenna feeds
- Military EW wideband receivers
- Stripline power combiners
- VNA calibration substrates

## Conditions And Methods

- Values measured at 10 GHz unless noted
- Temperature coefficients apply over operating range
- Plasma desmear mandatory for via reliability

## Limits And Non-Claims

- This card does not prove HIL/APT fabrication capability
- Does not validate specific stackup performance
- Processing parameters vary by thickness and copper weight

## Source Links

- Internal: `frontendapt-taconic-pcb-json`
- Public: https://aptpcb.com/en/materials/taconic-pcb
