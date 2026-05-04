---
fact_id: "materials-isola-tachyon-100g-ultra-low-loss"
title: "Isola Tachyon 100G Ultra-Low-Loss 112G PAM4 Laminate"
topic: "High-speed digital materials"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendapt-isola-pcb-json"
tags: ["isola", "tachyon-100g", "112g", "pam4", "800g", "ethernet", "hpc", "co-packaged-optics"]
---

# Canonical Summary

> Isola Tachyon 100G is an ultra-low-loss thermoset laminate for the most demanding 112G PAM4 and next-generation channels. Thermally compatible with I-Tera MT40 and Astra MT77 for hybrid multilayer constructions.

## Stable Facts

### Electrical Properties (@ 10 GHz)
- **Dk**: 3.02
- **Df**: 0.0021
- **Test Method**: IPC-TM-650 2.5.5.5

### Thermal Properties
- **Tg**: 215°C (DSC)
- **Td**: 360°C (TGA 5%)
- **CTE Z**: 40 ppm/°C (below Tg)
- **Moisture Absorption**: 0.10%

### Key Characteristics
- Ultra-low-loss thermoset (no plasma required)
- Lowest Df in Isola portfolio
- Spread-glass weave for skew control
- Thermally compatible with I-Tera MT40 and Astra MT77
- Lead-free compatible

### Applications
- 112G PAM4 channels
- Next-gen data center switch fabrics
- HPC interconnects
- Co-packaged optics host boards
- 800G Ethernet

## Conditions And Methods

- Available from Isola distributors (5-10 days)
- Hybrid stack compatible with I-Tera/Astra
- TDR/VNA validation essential
- Polar Si9000 simulation recommended

## Comparison

| Property | I-Tera MT40 | Tachyon 100G | Astra MT77 |
|----------|-------------|--------------|------------|
| Dk | 3.45 | 3.02 | 3.00 |
| Df | 0.0031 | 0.0021 | 0.0017 |
| Use Case | 56G | 112G | RF/mmWave |
| Tg | 200°C | 215°C | 200°C |

## Limits And Non-Claims

- Higher cost than I-Tera MT40
- Not stocked (distributor lead time 5-10 days)
- Requires careful hybrid stack engineering

## Source Links

- Internal: `frontendapt-isola-pcb-json`
- Public: https://aptpcb.com/en/materials/isola-pcb
