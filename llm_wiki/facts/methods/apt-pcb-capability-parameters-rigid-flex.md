# Fact Card: APT PCB Manufacturing Capability Parameters - Rigid-Flex PCB

## Fact Metadata

- **fact_id**: apt_pcb_capability_parameters_rigid_flex
- **fact_type**: capability_parameters
- **source_id**: apt_rigid_flex_pcb_capability_page
- **authority_tier**: Tier-2
- **domain**: pcb_manufacturing
- **application**: rigid_flex_pcb
- **date_extracted**: 2026-05-02
- **verification_status**: verified

## Capability Parameters

### Layer Count

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Max overall layers | 32 | layers | |
| Min configuration | 2 | layers | 1L flex + 1L rigid |
| Sequential laminations | Up to 2 | | |

### Trace and Space

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Inner layer min trace/space | 2.5/2.5 | mil | 0.0635 mm |
| Outer layer min trace/space | 2.5/2.5 | mil | 0.0635 mm |

### Copper Weight

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Max inner copper | 3 | oz | 105 μm |
| Max outer copper | 3 | oz | 105 μm |
| Max in rigid areas | 10 | oz | Special areas |

### Flex Core

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Min flex core thickness | 0.001 | inch | 0.025 mm, adhesiveless PI |

### Drilling

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Min mechanical drill | 0.0079 | inch | 0.20 mm |
| Min laser drill (microvia) | 0.003 | inch | 0.075 mm |
| Min finished hole | 0.006 | inch | 0.15 mm |
| Max mech drill aspect ratio | 12:1 | | Up to 15:1 consult |
| Max blind via aspect ratio | 0.75:1 | | |
| Max laser aspect ratio | 1:1 | | Microvias |

### Tolerances

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Press fit hole | ±0.05 | mm | |
| PTH | ±0.075 | mm | |
| NPTH | ±0.05 | mm | |
| Countersink | ±0.15 | mm | |
| Board thickness (<1.0mm) | ±0.10 | mm | |
| Board thickness (≥1.0mm) | ±10 | % | |
| Contour | ±0.08 | mm | Tighter with laser |

### Board Geometry

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Board thickness (overall) | 0.4 - 3.2 | mm | Rigid + flex |
| Min board size | 5 × 5 | mm | Panelized |
| Max panel size | 18 × 24 | inch | 457 × 610 mm |

### Impedance Control

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Single-ended (≤50Ω) | ±5 | Ω | |
| Single-ended (>50Ω) | ±7 | % | |
| Differential (≤50Ω) | ±5 | Ω | |
| Differential (>50Ω) | ±7 | % | |

### Solder Mask and Legend

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Min solder mask clearance | 1.5 | mil | 0.038 mm |
| Min solder mask dam | 3 | mil | 0.076 mm |
| Min legend width/height | 3.5/20 | mil | |

### Mechanical

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Strain relief fillet | 1.5 ± 0.5 | mm | |
| Bow & twist | ≤0.5 | % | Rigid areas per IPC |

### Assembly

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Min SMT component | 01005 | | 0.4 × 0.2 mm, rigid |
| Min BGA/CSP pitch | 0.3 | mm | 12 mil, rigid |
| Max component height | 25 | mm | Top/bottom |

### Via Types

- Through-hole vias
- Blind vias
- Buried vias
- Microvias (laser drilled)
- Via-in-Pad (VIP)
- Conductive filled (copper-filled)
- Non-conductive filled

### Quality Standards

- IPC-A-600 Class 2 / Class 3
- ISO 9001:2015
- UL Certified
- RoHS compliant
- IATF 16949 and REACH on request

### Inspection

- 100% E-test (Flying Probe or Fixture)

## Surface Finishes

- ENIG
- Gold Finger (Hard Gold)
- Immersion Silver
- Immersion Tin
- Lead-free HASL (rigid areas)
- OSP
- ENEPIG
- Flash Gold

## Solder Mask Colors

Green, Black, Blue, Red, Matte Green (others on request)

## Legend Colors

White, Black, Red, Yellow (others on request)

## Lead Time

7-20 working days (quick-turn available)

## Source Reference

> "来自 APTPCB 已审核静态页面, 发布于 aptpcb.com"
> - Source: apt_rigid_flex_pcb_capability_page
> - URL: file:///code/hileap/frontendAPT/public/static/capabilities/en/rigid-flex-pcb.json
> - Authority: Tier-2 (internal_published_page)

## Usage Notes

These parameters represent confirmed rigid-flex PCB manufacturing capabilities. Values are suitable for:
- 3D integration design
- Bend area planning
- Dynamic flex applications
- High-reliability aerospace/medical designs

## Design Considerations

- Bend radius affects material and copper thickness selection
- Copper balancing needed in transition zones
- Stiffener design critical for connector compatibility
- Early engagement recommended for complex designs

## Limitations

- Higher layer counts require consultation
- Tight bend radii need special materials
- Assembly limited to rigid areas
