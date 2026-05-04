---
fact_id: "materials-rogers-rt-duroid-5880-ultra-low-loss"
title: "Rogers RT/duroid 5880 Ultra-Low-Loss PTFE Laminate"
topic: "RF microwave materials"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendapt-rf-rogers-json"
tags: ["rogers", "rt-duroid-5880", "ptfe", "ultra-low-loss", "aerospace", "defense", "mmwave", "space"]
---

# Canonical Summary

> Rogers RT/duroid 5880 delivers the lowest electrical loss in commercial PCB laminates with Df 0.0009 at 10 GHz. Aerospace and defense heritage for demanding mmWave applications.

## Stable Facts

### Electrical Properties (@ 10 GHz)
- **Dk**: 2.20 ± 0.02
- **Df**: 0.0009 (lowest commercial)
- **Test Method**: IPC-TM-650 2.5.5.5

### Thermal/Mechanical
- **Thermal Conductivity**: 0.20 W/m·K
- **CTE Z-axis**: 237 ppm/°C
- **CTE X/Y**: ~30 ppm/°C

### Key Characteristics
- PTFE composite with glass microfiber reinforcement
- Lowest Df available in commercial laminates
- Aerospace and defense heritage
- Requires plasma desmear
- Surface treatment for copper adhesion

### Applications
- Aerospace radar systems
- Satellite communications
- Defense microwave systems
- mmWave antennas (>40 GHz)
- High-frequency test fixtures

## Conditions And Methods

- Specialized PTFE processing required
- Plasma desmear mandatory
- Surface preparation critical for copper adhesion
- TDR/VNA validation essential

## Comparison

| Property | RO3003 | RT/duroid 5880 | Taconic TLY-5A |
|----------|--------|----------------|----------------|
| Dk | 3.00 | 2.20 | 2.17 |
| Df | 0.0010 | 0.0009 | 0.0009 |
| Chemistry | PTFE Ceramic | PTFE Glass | PTFE Glass |

## Advantages
- Lowest Df (0.0009) = lowest insertion loss
- Proven aerospace heritage
- Excellent for >40 GHz applications

## Limits And Non-Claims
- Very high CTE Z (237 ppm/°C) - PTH reliability concerns
- Lower thermal conductivity (0.20 W/m·K)
- Most demanding processing requirements
- Higher cost than RO3000 series

## Source Links

- Internal: `frontendapt-rf-rogers-json`
- Public: https://aptpcb.com/en/materials/rf-rogers
