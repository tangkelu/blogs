---
fact_id: "materials-isola-itera-mt40-56g-pam4"
title: "Isola I-Tera MT40 Very Low-Loss 56G PAM4 Laminate"
topic: "High-speed digital materials"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendapt-isola-pcb-json"
tags: ["isola", "i-tera-mt40", "56g", "pam4", "400g", "ethernet", "automotive", "adas", "hybrid-rf"]
---

# Canonical Summary

> Isola I-Tera MT40 is a very low-loss thermoset laminate for 56G PAM4 applications. Dk stable from -55°C to +125°C up to W-band frequencies. Multiple Dk options (3.38, 3.45, 3.60, 3.75) for impedance flexibility.

## Stable Facts

### Electrical Properties (@ 10 GHz)
- **Dk**: 3.45 (other options: 3.38, 3.60, 3.75)
- **Df**: 0.0031
- **Test Method**: IPC-TM-650 2.5.5.5

### Thermal Properties
- **Tg**: 200°C (DSC)
- **Td**: 360°C (TGA 5%)
- **CTE Z**: 38 ppm/°C (below Tg)
- **Dk Stability**: Stable -55°C to +125°C up to W-band

### Key Characteristics
- Very low-loss thermoset (no plasma required)
- Multiple Dk options for impedance flexibility
- All glass is spread weave (skew control)
- No PTFE-type through-hole treatment required
- Thermally compatible with Astra MT77 for hybrid builds

### Applications
- 56G PAM4 backplanes
- High-speed switch ASICs
- 100G/400G Ethernet
- Automotive ADAS digital processing
- Hybrid RF/digital boards

## Conditions And Methods

- Stocked at APTPCB: Dk 3.45 grade
- Other Dk options: 3.38, 3.60, 3.75
- Compatible with I-Tera/Tachyon/Astra hybrid stacks
- TDR/VNA validation recommended

## Comparison

| Property | I-Speed | I-Tera MT40 | Tachyon 100G |
|----------|---------|-------------|--------------|
| Dk | 3.64 | 3.45 | 3.02 |
| Df | 0.0060 | 0.0031 | 0.0021 |
| Use Case | 25G | 56G | 112G |

## Limits And Non-Claims

- Df 0.0031 insufficient for 112G PAM4 (use Tachyon 100G)
- Multiple Dk options require careful stock management
- Does not guarantee specific channel compliance

## Source Links

- Internal: `frontendapt-isola-pcb-json`
- Public: https://aptpcb.com/en/materials/isola-pcb
