# Fact Card: APT PCB Manufacturing Capability Parameters - Metal Core PCB

## Fact Metadata

- **fact_id**: apt_pcb_capability_parameters_metal_core
- **fact_type**: capability_parameters
- **source_id**: apt_metal_pcb_capability_page
- **authority_tier**: Tier-2
- **domain**: pcb_manufacturing
- **application**: metal_core_pcb
- **date_extracted**: 2026-05-02
- **verification_status**: verified

## Capability Parameters

### Layer Count and Materials

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Layer count | 1-4 | layers | Metal core |
| Metal base materials | Aluminum, Copper, Iron | | |
| Material suppliers | Ximai (China), Bergquist (USA) | | Others on request |

### Board Geometry

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Final thickness | 0.5-4.6 | mm | 0.02"-0.18" |
| Approximate Tg | 130-170 | °C | Depends on laminate |
| Min board size | 0.2 × 0.2 | inch | |
| Max board size | 43.3 × 19 | inch | Large capability |

### Trace and Space by Copper Weight

| Copper | Min Trace | Min Space | Unit |
|--------|-----------|-----------|------|
| 0.5 oz | 4 | 4 | mil |
| 1 oz | 5 | 5 | mil |
| 2 oz | 5 | 7 | mil |
| 3 oz | 7 | 8 | mil |
| 4 oz | 10 | 10 | mil |

### Hole Ring by Copper Weight

| Copper | Min Hole Ring | Unit |
|--------|-----------------|------|
| 0.5 oz | 4 | mil |
| 1 oz | 5 | mil |
| 2 oz | 7 | mil |
| 3 oz | 10 | mil |
| 4 oz | 16 | mil |

### Drilling

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Min hole (0.5-2.0mm boards) | 30 | mil | |
| Min hole (2.0-4.6mm boards) | 45 | mil | |
| PTH tolerance | ±4 | mil | |
| NPTH tolerance | ±3 | mil | |

### Plating Thickness

| Finish | Nickel | Gold/Tin/Silver | Unit |
|--------|--------|-----------------|------|
| HASL PTH Cu | - | 20-35 | μm |
| HASL PTH Sn | - | 5-20 | μm |
| ENIG | 100-200 | 2-4 (Au) | μ" |
| Hard Gold | 100-200 | 4-8 (Au) | μ" |
| Golden Finger | 100-200 | 5-15 (Au) | μ" |
| Immersion Silver | - | 6-12 | μ" |
| OSP | - | 8-20 | μ" (film) |

### Solder Mask

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Thickness | 0.2-1.6 | mil | |
| Dam (green) | 4 | mil | |
| Dam (other colors) | 5 | mil | |
| Hole plug diameter | 10-25 | mil | |

### Silkscreen

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Colors | White, black | | |
| Min line width | 5 | mil | |
| Min character height | 24 | mil | |

### Testing and Routing

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Test voltage (fixture) | 50-300 | V | |
| Test voltage (flying) | 30-250 | V | |
| CNC routing tolerance | ±5 | mil | |
| V-cut tolerance | ±5 | mil | |
| Min slot | 40 | mil | |
| V-cut angles | 15°, 20°, 30°, 45°, 60° | | |

### Quality

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Bow and twist | ≤1 | % | |
| Lead time | 7-15 | days | Working days |

## Solder Mask Colors (Glossy)

Green, black, red, yellow, white, purple, blue

## Solder Mask Colors (Matt)

Matt green, matt black

## Accepted Standards

- IPC Class 2
- IPC Class 3
- ISO 9000

## Surface Finishes

- Leaded HASL
- Lead-free HASL
- ENIG
- OSP
- Immersion silver
- Hard gold

## Source Reference

> "来自 APTPCB 已审核静态页面, 发布于 aptpcb.com"
> - Source: apt_metal_pcb_capability_page
> - URL: file:///code/hileap/frontendAPT/public/static/capabilities/en/metal-pcb.json
> - Authority: Tier-2 (internal_published_page)

## Usage Notes

These parameters represent confirmed metal core PCB manufacturing capabilities. Values are suitable for:
- LED lighting PCB design
- Power electronics thermal management
- Automotive module design

## Applications

- LED lighting
- Power electronics
- Automotive applications

## Limitations

- Thicker boards require larger minimum holes
- Heavy copper affects trace/space capabilities
- Metal base thermal expansion must be considered in design
