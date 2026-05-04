---
fact_id: "processes-apt-ceramic-capability-specs"
title: "APT Ceramic PCB Manufacturing Capabilities"
topic: "Ceramic PCB manufacturing capabilities"
category: "processes"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendapt-ceramic-pcb-capability-en"
tags: ["apt", "ceramic", "al2o3", "aln", "dpc", "ltcc", "dbc", "thermal-conductivity"]
---

# Canonical Summary

> APT Ceramic capabilities: Al2O3 (20-27 W/m·K), AlN (180-220 W/m·K), DPC/LTCC/DBC, 1-2 layer, 0.06mm drilling, 2/2 mil trace.

## Stable Facts

### Materials
- **96% Alumina (Al2O3)**: Thermal conductivity 20–27 W/m·K
- **Aluminum Nitride (AlN)**: Thermal conductivity 180–220 W/m·K

### Technologies
- **DPC** (Direct Plated Copper)
- **LTCC** (Low-Temperature Co-fired Ceramic)
- **DBC** (Direct Bonded Copper)

### Substrate Size
- **Standard sizes**: 114×114mm, 120×120mm, 140×130mm, 190×140mm
- **Custom**: Available upon request

### Thickness Options
- 0.2mm, 0.25mm, 0.3mm, 0.38mm, 0.5mm, 0.635mm, 0.8mm, 1.0mm, 1.2mm, 1.5mm

### Layers
- 1 Layer, 2 Layers

### Copper Weight
- H/H through 10/10 oz (with DPC/DBC)

### Trace/Space (DPC)
| Copper Thickness | Trace/Space |
|------------------|-------------|
| 5-10 µm | 0.05/0.05 mm (2/2 mil) |
| 18 µm (0.5 oz) | 0.075/0.075 mm (3/3 mil) |
| 35 µm (1 oz) | 0.1/0.1 mm (4/4 mil) |
| 70 µm (2 oz) | 0.127/0.127 mm (5/5 mil) |

### Drilling
- **Min hole**: 0.06 mm (2.4 mil)
- **Tolerance**: ±20%
- **Shift angle**: ±0.025 mm
- **Hole-to-hole spacing**: 0.15 mm center-to-center

### Laser Capabilities
- **Laser drilling**: Based on board thickness
- **Outline/cutting**: Max 3.0mm thickness
- **Scribing**: ≤0.7mm depth

### Tolerances
- **Outer dimensions**: ≤ ±0.05 mm
- **Slot holes**: L≥2×W ±0.05/±0.025mm; L<2×W ±0.025/±0.010mm

### Filled Via (DPC)
- **Aspect ratio**: ≤5:1
- **Max board thickness**: 0.635 mm

### Applications
- Power electronics (LED, IGBT modules)
- Automotive (ECU, power modules)
- Medical (sensors, implantable)
- Aerospace & defense (high-temp, RF)
- High-frequency RF (antennas, filters, amplifiers)

## Conditions And Methods

- DPC for fine-line high-density
- DBC for high-power applications
- LTCC for integrated passive components

## Limits And Non-Claims

- Max 2 layers for standard ceramic
- Aspect ratio limits for filled vias
- Custom sizes subject to lead time

## Source Links

- Internal: `frontendapt-ceramic-pcb-capability-en`
- Public: https://aptpcb.com/en/capabilities/ceramic-pcb
