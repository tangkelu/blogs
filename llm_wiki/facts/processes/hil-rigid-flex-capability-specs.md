---
fact_id: "processes-hil-rigid-flex-capability-specs"
title: "HIL Rigid-Flex PCB Manufacturing Capabilities"
topic: "Rigid-Flex PCB manufacturing capabilities"
category: "processes"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendhil-rigid-flex-pcb-product-en"
tags: ["hil", "rigid-flex", "bookbinder", "stiffener", "dynamic-flex", "as9100", "multilayer-flex"]
---

# Canonical Summary

> HIL Rigid-Flex capabilities: 3-24+ layers, 50-75 μm trace/space, bookbinder construction, dynamic flex testing, AS9100.

## Stable Facts

### Layer Configurations
- **Standard**: 3–12 layers
- **Advanced**: Up to 24+ layers
- **Minimum**: 1 flex + 2 rigid
- **Builds**: Asymmetric configurations supported

### Flex Section
- **Layers**: 1–6 flex layers
- **Thickness**: 0.05–0.50 mm
- **Copper**: 0.5–2 oz

### Rigid Section
- **Thickness**: 0.20–3.20 mm
- **Copper**: Up to 6 oz (rigid sections)

### Trace/Space
- **Standard**: 75/75 μm (3/3 mil)
- **Advanced**: 50/50 μm (2/2 mil)

### Vias
- **Mechanical**: 0.15 mm (6 mil)
- **Laser microvia**: 0.075 mm (3 mil)

### Stiffeners
- **Standard**: Polyimide, FR-4
- **Advanced**: Stainless steel, aluminum

### Bend Radius
- **Dynamic**: 10× flex thickness
- **Static**: 6× flex thickness (1–2 layers)

### Impedance Control
- **Standard**: ±10%
- **Advanced**: ±5% with TDR

### Design Guidelines
- Copper perpendicular to bend lines
- Avoid vias/pads in dynamic flex areas
- Offset traces between layers for strain distribution
- Staggered or bookbinder layer lengths for multilayer
- Anti-pad/relief features near transitions

### Testing
- **Standard**: E-test, AOI, dimensional
- **Advanced**: Dynamic flex testing, TDR, thermal cycling/shock

### Certifications
- **Standard**: ISO 9001, UL, RoHS/REACH
- **Advanced**: AS9100, ISO 13485, IATF 16949

### Process Flow
1. Flex core imaging
2. Coverlay/bondply prep
3. Inner-layer AOI
4. Staged lamination with rigid cores
5. Laser microvia and controlled-depth routing
6. Finish and final inspection

### Lead Times
- **Standard**: 7–15 days
- **Quick-turn**: ≈5 days

## Conditions And Methods

- Registration verified at each lamination stage
- X-ray confirms via targets
- Plasma desmear cleans PI holes

## Limits And Non-Claims

- Complex designs require detailed DFM review
- Dynamic flex life depends on design and testing
- Does not guarantee specific reliability without qualification

## Source Links

- Internal: `frontendhil-rigid-flex-pcb-product-en`
- Public: https://www.hilpcb.com/products/rigid-flex-pcb
