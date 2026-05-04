---
fact_id: "materials-taconic-cer-series-high-dk"
title: "Taconic CER-10/20/30 High-Dk Ceramic PTFE Laminate"
topic: "RF microwave materials"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendapt-taconic-pcb-json"
tags: ["taconic", "cer-10", "cer-20", "cer-30", "high-dk", "ptfe", "miniaturization", "antenna"]
---

# Canonical Summary

> Taconic CER series (CER-10/20/30) are extremely high dielectric constant PTFE/ceramic laminates enabling physically small antennas and filters. CER-10 (Dk 10) is most common for extreme miniaturization.

## Stable Facts

### Electrical Properties (@ 10 GHz)
| Grade | Dk | Df |
|-------|-----|-----|
| CER-10 | 10.0 ± 0.25 | 0.0035 |
| CER-20 | ~20 | 0.0035 |
| CER-30 | ~30 | 0.0035 |

### Mechanical/Thermal
- **CTE Z**: 20 ppm/°C (CER-10)
- **Thermal Conductivity**: 0.42 W/m·K (CER-10)
- **CTE X/Y**: 8 ppm/°C (CER-10, low)

### Key Characteristics
- Extremely high Dk enables miniaturization
- Ceramic loading provides excellent Dk stability over temperature
- Plasma desmear required
- CER-10 most commonly specified

### Applications
- Dielectric resonator antennas (DRA)
- Compact cavity filters
- Horn antenna feed elements
- Miniaturized GPS L1/L2 patch antennas

## Conditions And Methods

- Stocked at APTPCB: CER-10 in 20-40 mil
- Smaller antenna size at same frequency vs. low-Dk materials
- Higher Dk = shorter wavelength = smaller components

## Limits And Non-Claims

- Df 0.0035 higher than low-Dk PTFE materials
- Narrower bandwidth for given antenna size
- Requires careful impedance matching design

## Source Links

- Internal: `frontendapt-taconic-pcb-json`
- Public: https://aptpcb.com/en/materials/taconic-pcb
