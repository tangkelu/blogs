---
fact_id: "processes-hil-fr4-capability-specs"
title: "HIL FR-4 PCB Manufacturing Capabilities"
topic: "FR-4 PCB manufacturing capabilities"
category: "processes"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendhil-fr4-pcb-product-en"
tags: ["hil", "fr4", "standard-pcb", "hdi", "high-tg", "low-loss", "12h-express", "ldi"]
---

# Canonical Summary

> HIL FR-4 capabilities: 1-32 layers, Tg 130-180°C, 0.075mm laser microvia, ±5% impedance, 12h express, IATF 16949.

## Stable Facts

### Layer Count
- **Standard**: 1–8 layers
- **Advanced**: Up to 32 layers

### Glass Transition Temperature (Tg)
- **Standard FR-4**: 130–140°C
- **Mid-Tg**: 150–160°C
- **High-Tg**: 170–180°C+

### Board Thickness
- **Standard**: 0.8–2.4 mm
- **Advanced**: 0.4–6.0 mm

### Dielectric Properties
| Property | Standard | Low-Loss |
|----------|----------|----------|
| Dk | ≈4.2 | ≈4.2 |
| Df @ 1GHz | 0.015–0.020 | 0.009–0.012 |
| Application | General | 10–25 Gbps |

### Imaging
- **Method**: LDI (Laser Direct Imaging)
- **Registration accuracy**: ±12.5 μm

### Drilling
- **Mechanical**: 0.20 mm (8 mil)
- **Laser microvias**: 0.075 mm (3 mil)

### HDI Capability
- **Technology**: Plasma desmear, filled microvias
- **Build-up**: Sequential up to 3+n+3
- **BGA pitch**: 0.3 mm support

### Plating
- **Method**: Pulse-reverse plating
- **Via copper variation**: ±10%

### Impedance Control
- **Tolerance**: ±5%
- **Validation**: TDR correlation

### Lead Time
- **Express**: 12-hour manufacturing available

### Quality Standards
- IPC-A-600 Class 2/3
- IPC-6012
- IPC-4101
- IATF 16949 (where applicable)
- ISO 13485 (where applicable)

### Applications
- Consumer electronics
- Industrial controls
- Automotive (high-Tg variants)
- Medical devices
- Telecommunications

## Conditions And Methods

- Material selection based on thermal and signal requirements
- Hybrid stackups for cost-performance balance
- 100% AOI, X-ray, and electrical testing

## Limits And Non-Claims

- Z-axis expansion increases above Tg
- Multiple reflow cycles require high-Tg materials
- Low-loss materials cost premium over standard FR-4

## Source Links

- Internal: `frontendhil-fr4-pcb-product-en`
- Public: https://www.hilpcb.com/products/fr4-pcb
