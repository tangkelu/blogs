---
fact_id: "processes-hil-through-hole-assembly-capability-specs"
title: "HIL Through-Hole PCB Assembly Capabilities"
topic: "Through-Hole PCB assembly capabilities"
category: "processes"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendhil-through-hole-assembly-product-en"
tags: ["hil", "through-hole", "tht", "wave-solder", "selective-solder", "press-fit", "class-3"]
---

# Canonical Summary

> HIL THT capabilities: Wave/selective solder, 3-4s dwell, >75% barrel fill (C2), >90% (C3), press-fit 10-50N, AOI+X-ray, ICT/FCT >90%.

## Stable Facts

### Soldering Methods
| Method | Application | Features |
|--------|-------------|----------|
| Wave | High-volume | 3–4 s dwell, preheat 100–130°C |
| Selective | Mixed tech | ±0.5 mm accuracy, nitrogen |
| Robotic | Complex | Programmable |
| Hand | Rework | Skilled operators |

### Wave Solder Parameters
- **Preheat topside**: 100–130 °C
- **Dwell time**: 3–4 seconds
- **Thermal profiling**: All phases recorded
- **ΔT control**: <±5 °C across board

### Barrel Fill Requirements
- **Class 2**: >75%
- **Class 3**: >90%
- **Wetting angle**: 30°–60°

### Nitrogen Atmosphere
- **Oxidation reduction**: 50–70%
- **Dross reduction**: Significant
- **Application**: Selective soldering

### Press-Fit
- **Force**: 10–50 N per pin
- **Connection**: Gas-tight
- **Alternative**: Solder-free retention

### Component Types
- **Standard**: Axial, Radial, DIP/SIP, Connectors
- **Advanced**: High-power transformers, custom heatsinks

### Solder Alloys
- **Primary**: Lead-free SAC305
- **Options**: Sn63/Pb37, HMP (high-temp)
- **Standard**: IPC J-STD-006

### Mechanical Retention
- **Pull strength**: 5–10 lb per lead (typical)
- **Advantage**: Superior to SMT for vibration/shock

### Inspection
| Method | Resolution/Feature | Coverage |
|--------|------------------|----------|
| AOI | 50–100 μm | >95% defect detection |
| X-ray | Barrel fill | Sample per IPC |
| Cross-section | 20–25 μm plating | First article |

### Testing
- **ICT**: >90% coverage
- **FCT**: Per specification
- **Boundary-scan**: Digital devices
- **Burn-in**: 60–85 °C, 24–168 h (lifecycle critical)

### Quality Standards
- IPC-A-610 Class 2/3
- IPC J-STD-001
- ISO 9001
- MES traceability

### Applications
- Connectors (high-insertion-force)
- Transformers (high-mass)
- Power components
- Mission-critical assemblies

## Conditions And Methods

- Flux density verification
- Thermal mass compensation for high-current connectors
- Fixture-level SPC

## Limits And Non-Claims

- Barrel fill depends on preheat, flux, and hole aspect ratio
- Press-fit requires precise hole sizing
- Mixed SMT/THT requires careful sequencing

## Source Links

- Internal: `frontendhil-through-hole-assembly-product-en`
- Public: https://www.hilpcb.com/products/through-hole-assembly
