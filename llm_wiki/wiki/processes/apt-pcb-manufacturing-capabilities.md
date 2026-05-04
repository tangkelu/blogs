# APT PCB Manufacturing Capabilities

## Overview

This wiki page aggregates APTPCB's confirmed manufacturing capabilities across rigid, flexible, HDI, metal core, rigid-flex, and ceramic PCB technologies. All parameters are sourced from APTPCB's published internal capability pages (Tier-2 authority).

## Technology Comparison Matrix

| Capability | Rigid | Flex | HDI | Metal Core | Rigid-Flex | Ceramic |
|------------|-------|------|-----|------------|------------|---------|
| **Max Layers** | 64 | 16 | 32-64 | 4 | 32 | 2 |
| **Min Trace/Space** | 2/2 mil | 4/4 mil | 3/3 mil (2/2 DFM) | 4/4 mil | 2.5/2.5 mil | 2/2 mil* |
| **Max Copper** | 20 oz | 2 oz | 3 oz (core) | 4 oz | 10 oz (rigid) | 10 oz |
| **Min Drill** | 0.15 mm mech / 0.075 mm laser | 8 mil | 0.075 mm laser | 30-45 mil | 0.075 mm laser | 0.06 mm |
| **Impedance Tol** | ±5Ω/±7% | ±5% | ±5% | ±5% | ±5Ω/±7% | ±5% |
| **Max Board Size** | 610×1100 mm | 20.5"×13" | 24"×18" | 43.3"×19" | 18"×24" | 190×140 mm |

*With 5-10 μm copper (DPC)

## Detailed Capability by Technology

### Rigid PCB Capabilities

**fact_id**: apt_pcb_capability_parameters_rigid

#### Layer and Geometry
- **Max Layers**: 64 layers for complex rigid PCBs
- **Board Size Range**: 10×10 mm to 610×1100 mm
- **Thickness Range**: 0.20 - 8.0 mm
- **Thickness Tolerance**: ±0.10 mm (<1.0mm), ±10% (≥1.0mm)

#### Fine Line Capability
- **Min Trace/Space**: 2/2 mil (0.0508 mm) on both inner and outer layers
- **Max Copper Thickness**: Up to 20 oz on inner and outer layers

#### Drilling and Vias
- **Min Mechanical Drill**: 0.15 mm
- **Min Laser Drill**: 0.075 mm (microvias)
- **Mechanical Aspect Ratio**: Up to 20:1
- **Laser Aspect Ratio**: 1:1 (microvias)
- **Via Types**: Through-hole, blind, buried, via-in-pad, stacked & staggered microvias

#### Precision and Registration
- **Layer-to-Layer Registration**: ±50 μm (typical)
- **Solder Mask Registration**: ±75 μm (typical)
- **PTH Tolerance**: ±0.075 mm
- **NPTH Tolerance**: ±0.05 mm

#### HDI Features
- **SBU Layers**: 1-3 sequential build-up
- **BGA Support**: Down to 0.3 mm pitch with HDI via-in-pad fan-out

#### Quality Standards
- **Warpage**: ≤0.75% per IPC
- **Compliance**: RoHS, UL, ISO 9001:2015, IPC-A-600 Class 2/3

### Flexible PCB Capabilities

**fact_id**: apt_pcb_capability_parameters_flex

#### Materials and Construction
- **Layer Count**: 1-16 layers
- **Base Materials**: Polyimide (PI), PET, PEN, FR-4 (DuPont PI on request)
- **Stiffeners**: FR-4, aluminum, polyimide, stainless steel

#### Geometry
- **Thickness Range**: 0.05 - 2.5 mm (0.002" - 0.10")
- **Board Size**: Max 20.5" × 13" (panelized)

#### Trace/Space by Copper Weight
| Copper | Inner Trace/Space | Outer Trace/Space |
|--------|-------------------|-------------------|
| 0.5 oz | 4/4 mil | 4/4 mil |
| 1 oz | 5/5 mil | 5/5 mil |
| 2 oz | 5/7 mil | 5/7 mil |

#### Flex-Specific Features
- **Insulation Range**: 0.5 mil (12.7 μm) to 2 mil (50 μm)
- **Min Finished Hole**: 8 mil
- **Coverlay Alignment**: ±3 mil
- **Profile Tolerances**: ±2 mil (accurate mould) to ±15 mil (hand-cut)

### HDI PCB Capabilities

**fact_id**: apt_pcb_capability_parameters_hdi

#### Build Configurations
- **HDI Types**: 1+N+1 through 4+N+4, Any Layer HDI (ELIC)
- **Max Layers**: 32 (standard), 64 (advanced)
- **Sequential Laminations**: Up to 4

#### Microvia Technology
- **Min Laser Drill**: 0.075 mm (advanced), 0.10 mm (standard)
- **Microvia Types**: Blind, buried, stacked (copper-filled), staggered, VIP
- **Aspect Ratios**: 0.75:1 (blind), 1:1 (laser)

#### Fine Feature Capability
- **Min Trace/Space**: 3/3 mil standard, 2/2 mil after DFM
- **Min Annular Ring**: 1 mil (0.025 mm)
- **Impedance Tolerance**: ±5%

#### Assembly Integration
- **Component Size**: Down to 01005 (0.4 × 0.2 mm)
- **BGA Pitch**: 0.3 mm (12 mil)
- **Component Height**: Up to 25 mm

### Metal Core PCB Capabilities

**fact_id**: apt_pcb_capability_parameters_metal_core

#### Metal Base Options
- **Materials**: Aluminum, Copper, Iron bases
- **Suppliers**: Ximai (China), Bergquist (USA)
- **Layer Count**: 1-4 layers

#### Thermal Design Parameters
| Copper Weight | Trace/Space | Hole Ring |
|---------------|-------------|-----------|
| 0.5 oz | 4/4 mil | 4 mil |
| 1 oz | 5/5 mil | 5 mil |
| 2 oz | 5/7 mil | 7 mil |
| 3 oz | 7/8 mil | 10 mil |
| 4 oz | 10/10 mil | 16 mil |

#### Form Factor
- **Thickness Range**: 0.5 - 4.6 mm (0.02" - 0.18")
- **Max Board Size**: 43.3" × 19"
- **V-cut Angles**: 15°, 20°, 30°, 45°, 60°

### Rigid-Flex PCB Capabilities

**fact_id**: apt_pcb_capability_parameters_rigid_flex

#### Layer Configuration
- **Max Overall Layers**: 32 layers
- **Flex Core Thickness**: Down to 0.001" (0.025 mm, adhesiveless PI)
- **Sequential Laminations**: Up to 2

#### Precision Capability
- **Min Trace/Space**: 2.5/2.5 mil (all layers)
- **Min Mechanical Drill**: 0.20 mm
- **Min Laser Drill**: 0.075 mm
- **Max Mech Aspect Ratio**: 12:1 (up to 15:1 with consultation)

#### Mechanical Design
- **Overall Thickness**: 0.4 - 3.2 mm
- **Strain Relief Fillet**: 1.5 ± 0.5 mm
- **Contour Tolerance**: ±0.08 mm

#### Bend Area Considerations
- Copper balancing required across flex areas
- Stiffener design critical for connector compatibility
- Assembly limited to rigid sections only

### Ceramic PCB Capabilities

**fact_id**: apt_pcb_capability_parameters_ceramic

#### Material Options

| Material | Thermal Conductivity | Application |
|----------|---------------------|-------------|
| 96% Alumina (Al₂O₃) | 20-27 W/m·K | Cost-effective thermal management |
| Aluminum Nitride (AlN) | 180-220 W/m·K | Extreme thermal performance |

#### Production Technologies
- **DPC (Direct Plated Copper)**: Fine line, 0.5-10 oz
- **LTCC (Low-Temperature Co-fired Ceramic)**: Multi-layer
- **DBC (Direct Bonded Copper)**: High power

#### Fine Line (DPC)
| Copper | Line/Space |
|--------|------------|
| 5-10 μm | 0.05/0.05 mm (2/2 mil) |
| 0.5 oz | 0.075/0.075 mm (3/3 mil) |
| 1 oz | 0.1/0.1 mm (4/4 mil) |
| 2 oz | 0.127/0.127 mm (5/5 mil) |
| 3 oz+ | Progressive increase |

#### Precision Machining
- **Min Mechanical Hole**: 0.06 mm
- **Outline Tolerance**: ±0.05 mm
- **Laser Cutting**: Max 3.0 mm thickness

#### Performance Specifications
- **Copper Peel Strength**: >2 N/mm (IPC-TM-650 2.4.8)
- **Thermal Resistance**: 350±10°C, 15 min (IPC-TM-650 2.4.7)
- **Solderability**: >95% wetting (IPC-TM-650 2.4.14)

## Cross-Technology Design Guidelines

### Impedance Control
All technologies support controlled impedance with ±5% tolerance (or ±5Ω for ≤50Ω targets). Specific tolerances:
- Single-ended ≤50Ω: ±5Ω
- Single-ended >50Ω: ±7%
- Differential ≤50Ω: ±5Ω
- Differential >50Ω: ±7%

### Surface Finish Availability

| Finish | Rigid | Flex | HDI | Metal | Rigid-Flex | Ceramic |
|--------|-------|------|-----|-------|------------|---------|
| ENIG | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ENEPIG | ✓ | - | ✓ | - | ✓ | ✓ |
| OSP | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Immersion Ag | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Immersion Sn | ✓ | - | ✓ | ✓ | ✓ | ✓ |
| HASL/LF HASL | ✓ | - | ✓ | ✓ | Rigid only | - |
| Hard Gold | ✓ | ✓ | ✓ | ✓ | ✓ | - |

### Quality Standards (All Technologies)
- IPC-A-600 Class 2 / Class 3
- ISO 9001:2015
- UL Certified
- RoHS & REACH compliant
- IATF 16949 available on request (automotive)

## Selection Guide

### Choose Rigid PCB When:
- Maximum layer count needed (up to 64 layers)
- Finest trace/space required (2/2 mil)
- Standard industrial/automotive applications
- Cost optimization priority

### Choose Flex PCB When:
- Dynamic bending required
- 3D packaging constraints
- Lightweight critical
- Interconnection between subsystems

### Choose HDI PCB When:
- High component density (0.3 mm BGA pitch)
- Fine-pitch devices (01005 components)
- Space-constrained designs
- High-speed signal routing

### Choose Metal Core When:
- Thermal management critical (LED, power)
- Heat dissipation required
- Single/double-sided with thick copper
- Large board formats acceptable

### Choose Rigid-Flex When:
- 3D integration with rigid component areas
- Dynamic flex + rigid mounting combined
- Reduced interconnects/cables needed
- Medical/aerospace reliability requirements

### Choose Ceramic When:
- Extreme thermal conductivity needed (AlN)
- High-temperature operation
- RF/microwave applications
- Hermetic sealing requirements

## Source References

All data sourced from APTPCB Tier-2 internal published pages:

1. `apt_rigid_pcb_capability_page` - file:///code/hileap/frontendAPT/public/static/capabilities/en/rigid-pcb.json
2. `apt_flex_pcb_capability_page` - file:///code/hileap/frontendAPT/public/static/capabilities/en/flex-pcb.json
3. `apt_hdi_pcb_capability_page` - file:///code/hileap/frontendAPT/public/static/capabilities/en/hdi-pcb.json
4. `apt_metal_pcb_capability_page` - file:///code/hileap/frontendAPT/public/static/capabilities/en/metal-pcb.json
5. `apt_rigid_flex_pcb_capability_page` - file:///code/hileap/frontendAPT/public/static/capabilities/en/rigid-flex-pcb.json
6. `apt_ceramic_pcb_capability_page` - file:///code/hileap/frontendAPT/public/static/capabilities/en/ceramic-pcb.json

## Last Updated

2026-05-02
