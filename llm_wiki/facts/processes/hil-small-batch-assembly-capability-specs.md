---
fact_id: "processes-hil-small-batch-assembly-capability-specs"
title: "HIL Small Batch PCB Assembly Capabilities"
topic: "Small batch PCBA capabilities for prototypes and NPI"
category: "processes"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-03"
source_ids:
  - "frontendhil-small-batch-assembly-product-en"
tags: ["hil", "small-batch", "prototype", "npi", "quick-turn", "3-10-day", "bga-0.25mm", "mes-traceability"]
---

# Canonical Summary

> HIL Small Batch: 10-5,000 units, 3-10 day quick-turn, BGA 0.25mm pitch, FPY>98%, stencil 95-100% transfer, production-grade NPI.

## Stable Facts

### Batch Volume
- **Standard**: 10–1,000 pcs
- **Maximum**: Up to 5,000 pcs
- **Focus**: Prototypes and NPI (New Product Introduction)

### Lead Time
- **Quick-turn**: 3–10 days
- **Value**: Production-grade process in prototype volumes

### Component Capability
| Component | Size/Pitch |
|-----------|------------|
| Standard | 0201 (0.6 × 0.3 mm) |
| Advanced | 01005, fine-pitch BGA 0.25 mm |

### Quality Metrics
- **FPY**: >98%
- **DPPM**: <500
- **Same gates**: As mass production

### Solder Paste Control
- **Stencil optimization**: Transfer efficiency ~95–100%
- **Volume control**: ±10%
- **3D SPI**: Pre-placement verification

### Reflow
- **Profiling**: Closed-loop with logged parameters
- **Parameters**: Ramp, TAL (Time Above Liquidus), peak per alloy

### Inspection
| Stage | Method | Coverage |
|-------|--------|----------|
| Post-placement | AOI | Prevents cascading defects |
| Post-reflow | AOI | Joint quality verification |
| Hidden joints | Sample X-ray | Void ≤25% per IPC-7095 |

### Assembly Types
- SMT only
- Through-hole (selective/wave)
- Mixed technology
- PoP (Package on Package)
- Fine-pitch BGA

### ESD Protection
- **Standard**: ANSI/ESD S20.20
- **Monitoring**: Continuous

### Testing Options
- ICT (In-Circuit Test)
- FCT (Functional Circuit Test)
- Boundary-scan (digital devices)

### Data Value
- **Predictive models**: Build data feeds volume scaling
- **Smooth handoff**: To large-volume and box build
- **Quality continuity**: Same criteria from pilot to production

### Standards
- J-STD-001 (soldering)
- IPC-7095 (BGA)

### Risk Mitigation
- **Stencil variation**: Process characterization prevents
- **Paste slump**: X-bar/R control charts monitor
- **Thermal imbalance**: Reflow profile optimization addresses

## Conditions And Methods

- DFM/DFT reviews before commitment
- Component sourcing: kitted, partial, or full turnkey
- Rapid iteration without sacrificing coverage

## Limits And Non-Claims

- Small batch cost per unit higher than volume
- Some tests (ICT) may require fixture investment
- Design changes require revision control

## Source Links

- Internal: `frontendhil-small-batch-assembly-product-en`
- Public: https://www.hilpcb.com/products/small-batch-assembly
