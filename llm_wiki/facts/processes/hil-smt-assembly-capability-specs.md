---
fact_id: "processes-hil-smt-assembly-capability-specs"
title: "HIL SMT Assembly Manufacturing Capabilities"
topic: "SMT assembly manufacturing capabilities"
category: "processes"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendhil-smt-assembly-product-en"
tags: ["hil", "smt", "assembly", "pcba", "fine-pitch", "bga", "spi", "aoi", "mes-traceability"]
---

# Canonical Summary

> HIL SMT Assembly: ±8-25μm placement, 008004 components, 3D SPI/AOI, FPY ≥98%, DPPM <500, MES traceability.

## Stable Facts

### Placement Accuracy
- **Standard**: ±25 μm @ 3σ
- **Advanced**: ±8 μm @ 3σ

### Component Sizes
- **Standard**: 0201 (0.6 × 0.3 mm)
- **Advanced**: 01005 (0.4 × 0.2 mm)
- **Ultra-fine**: 008004 (0.25 × 0.125 mm)

### Fine-Pitch Capability
- **BGA/CSP**: Down to 0.2 mm pitch

### Solder Paste Control
- **Stencil thickness**: 100–150 μm
- **Volume control**: ±10%
- **Transfer efficiency**: ~95–100%

### Inspection Coverage
| Stage | Method | Coverage |
|-------|--------|----------|
| Print | 3D SPI | Solder paste |
| Placement | Pre/post vision | Component verification |
| Reflow | AOI | >95% defect detection |
| Hidden joints | Sample X-ray | BGA/QFN per IPC-7095 |

### Reflow Capabilities
- **Nitrogen reflow**: Available for improved wetting
- **Profile zones**: Ramp, soak, TAL, peak
- **Temperature control**: ±5°C ΔT
- **Digital logging**: Per lot traceability

### Quality Metrics
- **FPY**: ≥98% (First Pass Yield)
- **DPPM**: <500 (Defects Per Million)

### Traceability
- **MES**: Manufacturing Execution System
- **Paste lot**: Full traceability
- **SPI-AOI correlation**: Continuous monitoring

### Assembly Types
- SMT only
- Through-hole only
- Mixed technology
- Double-sided SMT
- PoP (Package on Package)
- SiP (System in Package)

### Additional Services
- Selective solder for mixed technology
- Wave solder
- Underfill for harsh environments
- Conformal coating
- Ionic contamination control: ≤1.56 μg/cm²

### Standards
- IPC-A-610 (Acceptability)
- J-STD-001 (Soldering)

## Conditions And Methods

- Reflow profile optimization with thermocouple mapping
- Closed-loop temperature calibration
- AOI feedback for process control

## Limits And Non-Claims

- Fine-pitch requires specialized stencil design
- 008004 placement requires advanced platforms
- BGA voiding target <25% per IPC-7095

## Source Links

- Internal: `frontendhil-smt-assembly-product-en`
- Public: https://www.hilpcb.com/products/smt-assembly
