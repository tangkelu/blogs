# Fact Card: APT PCB Manufacturing Capability Parameters - Flexible PCB

## Fact Metadata

- **fact_id**: apt_pcb_capability_parameters_flex
- **fact_type**: capability_parameters
- **source_id**: apt_flex_pcb_capability_page
- **authority_tier**: Tier-2
- **domain**: pcb_manufacturing
- **application**: flex_pcb
- **date_extracted**: 2026-05-02
- **verification_status**: verified

## Capability Parameters

### Layer Count and Materials

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Layer count | 1-16 | layers | Standard flex |
| Base materials | PI, PET, PEN, FR-4 | | DuPont PI on request |
| Stiffeners | FR-4, Al, PI, SS | | Per design requirements |

### Board Geometry

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Final thickness | 0.05 - 2.5 | mm | 0.002" - 0.10" |
| Min board size | 0.2 × 0.3 | inch | |
| Max board size | 20.5 × 13 | inch | Panelized |

### Trace and Space (Inner Layers)

| Copper Weight | Min Trace | Min Space | Unit |
|---------------|-----------|-----------|------|
| 0.5 oz | 4 | 4 | mil |
| 1 oz | 5 | 5 | mil |
| 2 oz | 5 | 7 | mil |

### Trace and Space (Outer Layers)

| Copper Weight | Min Trace | Min Space | Unit |
|---------------|-----------|-----------|------|
| 1/3 - 0.5 oz | 4 | 4 | mil |
| 1 oz | 5 | 5 | mil |
| 2 oz | 5 | 7 | mil |

### Copper and Insulation

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Copper thickness | 1/3 - 2 | oz | Thinner/thicker on request |
| Max insulation | 2 | mil | 50 μm |
| Min insulation | 0.5 | mil | 12.7 μm |

### Holes and Slots

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Min finished hole | 8 | mil | |
| PTH tolerance | ±3 | mil | |
| NPTH tolerance | ±2 | mil | |
| Min slot | 24 × 35 | mil | 0.6 × 0.9 mm |

### Alignment Tolerances

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Coverlay alignment | ±3 | mil | |
| Silkscreen alignment | ±6 | mil | |
| Min silkscreen line | 5 | mil | |

### Profile Tolerances (Punch)

| Method | Tolerance | Unit |
|--------|-----------|------|
| Accurate mould | ±2 | mil |
| Ordinary mould | ±4 | mil |
| Knife mould | ±8 | mil |
| Hand-cut | ±15 | mil |

### Surface Finish Thickness

| Finish | Specification | Unit |
|--------|---------------|------|
| ENIG Nickel | 100-200 | μ" |
| ENIG Gold | 1-5 | μ" |
| Immersion Silver | 6-12 | μ" |
| OSP | 8-20 | μ" |

### Testing

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Test voltage | 50-300 | V | Fixture per spec |

## Source Reference

> "来自 APTPCB 已审核静态页面, 发布于 aptpcb.com"
> - Source: apt_flex_pcb_capability_page
> - URL: file:///code/hileap/frontendAPT/public/static/capabilities/en/flex-pcb.json
> - Authority: Tier-2 (internal_published_page)

## Usage Notes

These parameters represent confirmed flexible PCB manufacturing capabilities. Values are suitable for:
- Flex PCB design rule definition
- Bend radius calculations
- Dynamic flex feasibility assessment

## Design Recommendations

- Avoid placing vias, pads in dynamic bend regions
- Choose copper/insulation thickness per bend radius
- Keep copper balanced across flex area width
- Confirm stiffener compatibility early

## Limitations

- Special constructions require engineering review
- Dynamic flex life depends on material and routing choices
