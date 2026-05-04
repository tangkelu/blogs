# Fact Card: APT PCB Manufacturing Capability Parameters - Ceramic PCB

## Fact Metadata

- **fact_id**: apt_pcb_capability_parameters_ceramic
- **fact_type**: capability_parameters
- **source_id**: apt_ceramic_pcb_capability_page
- **authority_tier**: Tier-2
- **domain**: pcb_manufacturing
- **application**: ceramic_pcb
- **date_extracted**: 2026-05-02
- **verification_status**: verified

## Capability Parameters

### Base Materials

| Material | Thermal Conductivity | Unit |
|----------|---------------------|------|
| 96% Alumina (Al₂O₃) | 20-27 | W/m·K |
| Aluminum Nitride (AlN) | 180-220 | W/m·K |

### Board Geometry

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Max substrate size | 190 × 140 | mm | |
| Standard sizes | 114×114, 120×120, 140×130, 190×140 | mm | |
| Material thickness options | 0.2-1.5 | mm | Various steps |
| Layers | 1-2 | layers | |

### Production Technologies

| Technology | Copper Range | Application |
|------------|------------|-------------|
| DPC | 0.5-10 oz | Fine line, high density |
| LTCC | Multi-layer | Complex circuits |
| DBC | High power | Power electronics |

### Line/Space (DPC Process)

| Copper Thickness | Min Line | Min Space | Unit |
|------------------|----------|-----------|------|
| 5-10 μm | 0.05 | 0.05 | mm (2/2 mil) |
| 0.5 oz (18 μm) | 0.075 | 0.075 | mm (3/3 mil) |
| 1 oz (35 μm) | 0.1 | 0.1 | mm (4/4 mil) |
| 2 oz (70 μm) | 0.127 | 0.127 | mm (5/5 mil) |
| 3 oz (105 μm) | 0.3 | 0.3 | mm (12/12 mil) |
| 6 oz (210 μm) | 0.5 | 0.5 | mm (20/20 mil) |
| 9 oz (300 μm) | 0.6 | 0.6 | mm (24/24 mil) |

### Drilling

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Min mechanical hole | 0.06 | mm | 2.4 mil |
| Hole diameter tolerance | ±20 | % | Drilling |
| Drilling shift angle | ±0.025 | mm | |
| Min hole-to-hole spacing | 0.15 | mm | Center to center |

### Special Features

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Copper filled via | Aspect ≤5:1, thickness ≤0.635 | mm | DPC |
| Outer shape to Cu distance | 0.15-0.2 | mm | |
| Outer dimensions tolerance | ≤±0.05 | mm | |
| Laser outline tolerance | ±0.1 | mm | |
| Max laser thickness | ≤3.0 | mm | |
| Laser scribing depth | ≤0.7 | mm | |

### Slot Holes Tolerance

| Condition | Long Tolerance | Wide Tolerance | Unit |
|-----------|---------------|----------------|------|
| L ≥ 2×W | ±0.05 | ±0.025 | mm |
| L < 2×W | ±0.025 | ±0.010 | mm |

### Laser Drilling Capabilities

| Board Thickness | Laser Drill Range | Unit |
|-----------------|-------------------|------|
| 0.25/0.38/0.5 mm | 0.1 | mm |
| 0.635 mm | 0.15-0.2 | mm |
| 1.0 mm | 0.2-0.35 | mm |
| 1.5 mm | 0.4-0.5 | mm |
| 2.0 mm | 0.5-0.6 | mm |

### Solder Mask

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Thickness | 10-30 | μm | Line surface |
| Tolerance | ±0.05 | mm | |
| Min opening (pad) | 0.15 | mm | |

### Silkscreen

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Min line width | 0.15 | mm | |
| To pad distance | 0.15 | mm | |
| Min diameter | 0.75 | mm | |
| Min gap | 0.15 | mm | |

### Surface Finishes

| Finish | Specification | Unit |
|--------|---------------|------|
| OSP | 0.2-0.5 | μm |
| Immersion Silver | ≥0.5 | μm |
| Immersion Tin | 0.8-1.2 | μm |
| ENIG | Ni 3-8, Au 0.03-0.3 | μm |
| ENEPIG | Ni 3-8, Pd 0.05-0.1, Au 0.05-0.1 | μm |

### Performance Tests

| Test | Requirement | Standard |
|------|-------------|----------|
| Copper peel strength | >2 N/mm | IPC-TM-650 2.4.8 |
| Thermal resistance | 350±10°C, 15 min no delamination | IPC-TM-650 2.4.7 |
| Solderability | >95% wetting | IPC-TM-650 2.4.14 |
| Bow & twist | ≤0.3 mm (3‰ per 100 mm) | |

### Quality Standards

- IPC-A-600 Class 2 / Class 3
- ISO 9001:2015
- UL Certified
- RoHS & REACH compliant
- IATF 16949 (automotive) on request

### Testing

- 100% E-test (Flying Probe or Fixture)

## Source Reference

> "来自 APTPCB 已审核静态页面, 发布于 aptpcb.com"
> - Source: apt_ceramic_pcb_capability_page
> - URL: file:///code/hileap/frontendAPT/public/static/capabilities/en/ceramic-pcb.json
> - Authority: Tier-2 (internal_published_page)

## Usage Notes

These parameters represent confirmed ceramic PCB manufacturing capabilities using DPC, LTCC, and DBC technologies. Values are suitable for:
- High-power LED design
- IGBT module substrates
- RF/microwave applications
- High-temperature electronics

## Applications

- LED lighting
- Power electronics / IGBT modules
- Automotive engine control
- Medical implantable devices
- Aerospace high-temp modules
- RF/microwave components

## Key Selection Guidance

- **Alumina (Al₂O₃)**: Cost-effective, 20-27 W/m·K, general purpose
- **Aluminum Nitride (AlN)**: High performance, 180-220 W/m·K, extreme thermal management

## Limitations

- Limited to 1-2 layers
- Maximum board size 190×140 mm
- Finest line/space requires thin copper (DPC)
- Heavy copper affects line/space capability significantly
