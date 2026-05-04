---
fact_id: "materials-isola-astra-mt77-hybrid-rf"
title: "Isola Astra MT77 Ultra-Low-Loss RF/Hybrid Laminate"
topic: "RF/high-speed hybrid materials"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendapt-isola-pcb-json"
tags: ["isola", "astra-mt77", "77ghz", "automotive", "radar", "5g", "mmwave", "hybrid", "rf-digital"]
---

# Canonical Summary

> Isola Astra MT77 bridges high-speed digital and RF/microwave applications. Dk stable from -40°C to +140°C up to W-band. FR-4 compatible processing with no plasma desmear required.

## Stable Facts

### Electrical Properties (@ 10 GHz)
- **Dk**: 3.00
- **Df**: 0.0017
- **Test Method**: IPC-TM-650 2.5.5.5
- **Dk Stability**: -40°C to +140°C up to W-band

### Thermal Properties
- **Tg**: 200°C (DSC)
- **Td**: 360°C (TGA 5%)
- **CTE Z**: 40 ppm/°C
- **Moisture Absorption**: 0.10%

### Key Characteristics
- Ultra-low-loss thermoset (no plasma required)
- Bridges high-speed digital and RF/microwave
- Dk stability over wide temperature range
- Compatible with lead-free assembly
- Shorter lamination time than PTFE
- Higher dimensional stability than PTFE

### Applications
- 77 GHz automotive radar
- 5G mmWave antenna panels
- RF/digital hybrid boards
- Satellite communication
- Point-to-point backhaul

## Conditions And Methods

- Stocked at APTPCB
- Hybrid stackable with I-Tera/Tachyon
- No plasma required (unlike PTFE alternatives)
- Compatible with standard FR-4 processing

## Comparison

| Property | Taconic RF-35 | Rogers RO4350B | Astra MT77 |
|----------|---------------|------------------|------------|
| Dk | 3.50 | 3.48 | 3.00 |
| Df | 0.0018 | 0.0037 | 0.0017 |
| Plasma | Recommended | No | No |
| Chemistry | PTFE | Hydrocarbon | Thermoset |

## Advantages vs PTFE
- No plasma desmear required
- Shorter lamination cycles
- Better dimensional stability
- Lower moisture absorption
- Lead-free compatible

## Limits And Non-Claims
- Dk 3.00 lower than common RF materials (affects impedance)
- Higher cost than standard FR-4
- Not for ultra-high-Dk applications

## Source Links

- Internal: `frontendapt-isola-pcb-json`
- Public: https://aptpcb.com/en/materials/isola-pcb
