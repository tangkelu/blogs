# Fact Card: APT PCB Manufacturing Capability Parameters - HDI PCB

## Fact Metadata

- **fact_id**: apt_pcb_capability_parameters_hdi
- **fact_type**: capability_parameters
- **source_id**: apt_hdi_pcb_capability_page
- **authority_tier**: Tier-2
- **domain**: pcb_manufacturing
- **application**: hdi_pcb
- **date_extracted**: 2026-05-02
- **verification_status**: verified

## Capability Parameters

### Layer Count and Configurations

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Max layers (standard) | 32 | layers | |
| Max layers (advanced) | 64 | layers | |
| HDI configurations | 1+N+1 through 4+N+4 | | Plus Any Layer HDI (ELIC) |
| Sequential laminations | Up to 4 | | |

### Trace and Space

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Standard min trace/space | 3/3 | mil | 0.076 mm |
| Tighter trace/space | 2/2 | mil | After DFM review |

### Board Geometry

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| PCB thickness | 0.40 - 8.0 | mm | |
| Max panel size | 24 × 18 | inch | 610 × 457 mm |
| Min flex core thickness | 0.001 | inch | 0.025 mm, adhesiveless PI |

### Drilling

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Min mechanical drill | 0.006 | inch | 0.15 mm, core layers |
| Min laser drill (advanced) | 0.003 | inch | 0.075 mm, microvias |
| Standard laser drill | 0.004 | inch | 0.10 mm, microvias |
| Max through-hole aspect ratio | 10:1 | | Mechanical |
| Max blind via aspect ratio | 0.75:1 | | Laser |
| Max laser aspect ratio | 1:1 | | Microvias |
| Min annular ring | 1 | mil | 0.025 mm |

### Microvia Types

- Blind microvias
- Buried microvias
- Stacked microvias (copper-filled)
- Staggered microvias
- Via-in-Pad (VIP)

### Copper and Materials

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Copper weights | 0.5 - 2 | oz | 18-70 μm |
| Max copper in rigid cores | 3 | oz | 105 μm |
| Base materials | FR-4, HF, PI, Rogers, Arlon, Teflon, Taconic | | |

### Impedance and Registration

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Impedance tolerance | ±5 | % | Highly precise |
| Solder mask registration | Within 0.002 | inch | 0.051 mm |
| Min solder mask dam | 0.003 | inch | 0.076 mm |

### Quality and Tolerances

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Thickness tolerance | ±0.002" or ±10% | | Whichever greater |
| Bow & twist | ≤0.05 | % | Per IPC |

### Assembly Capabilities

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Min SMT component | 01005 | | 0.4 × 0.2 mm |
| Min BGA/CSP pitch | 0.3 | mm | 12 mil |
| Max component height | 25 | mm | Top/bottom |

### Quality Standards

- IPC-A-600 Class 2 / Class 3
- ISO 9001:2015
- UL Certified
- RoHS & REACH compliant
- IATF 16949 (automotive) on request

### Inspection & Testing

- AOI / 3D AOI
- 3D SPI (Solder Paste Inspection)
- X-Ray Inspection
- ICT (In-Circuit Test)
- FCT (Functional Circuit Test)
- 100% E-test (Flying Probe or Fixture)

## Surface Finishes

- ENIG
- Immersion tin
- Immersion silver
- OSP
- Electrolytic gold (hard/soft)
- Lead-free HASL
- Soft wire bondable gold

## Source Reference

> "来自 APTPCB 已审核静态页面, 发布于 aptpcb.com"
> - Source: apt_hdi_pcb_capability_page
> - URL: file:///code/hileap/frontendAPT/public/static/capabilities/en/hdi-pcb.json
> - Authority: Tier-2 (internal_published_page)

## Usage Notes

These parameters represent confirmed HDI PCB manufacturing capabilities. Values are suitable for:
- HDI stack-up design
- Microvia feasibility assessment
- Fine-pitch BGA routing
- High-density interconnect planning

## Limitations

- 2/2 mil trace/space requires DFM review
- ELIC (Any Layer) has specific design constraints
- Stacked microvias require copper filling
