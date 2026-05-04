---
fact_id: "processes-hil-ic-substrate-capability-specs"
title: "HIL IC Substrate PCB Manufacturing Capabilities"
topic: "IC Substrate PCB manufacturing capabilities"
category: "processes"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendhil-ic-substrate-pcb-product-en"
tags: ["hil", "ic-substrate", "sap", "abf", "bt-resin", "flip-chip", "advanced-packaging", "15um-line"]
---

# Canonical Summary

> HIL IC Substrate capabilities: SAP 15-20μm line/space, ABF/BT, 25-50μm microvias, flip-chip ready, ≤0.5% warpage, 4-50 layers.

## Stable Facts

### Technology
- **Semi-Additive Process (SAP)**: 15–20 μm line/space
- **Density gain**: 2–4× vs subtractive HDI
- **mSAP**: Alternative for specific designs
- **Cleanroom**: Class 1000 for fine-line processing

### Materials
| Material | Dielectric | CTE | Application |
|----------|------------|-----|-------------|
| ABF | 30–60 μm layers | - | Build-up dielectric |
| BT Resin | - | 12–14 ppm/°C | CTE bridge |
| Composite target | - | 9–14 ppm/°C | Silicon matching |

### CTE Matching
- **Silicon**: ~2.6 ppm/°C
- **BT Resin**: 12–14 ppm/°C
- **FR-4**: ~16–18 ppm/°C
- **Goal**: Bridge gap to reduce stress

### Microvias
- **Diameter**: 25–50 μm
- **Depth control**: ±5 μm
- **Stacked**: Supported for high density

### Fine-Line Capability
| Process | Line/Space | Undercut |
|---------|-----------|----------|
| SAP | 15–20 μm | Minimal |
| Subtractive HDI | 50–75 μm | Higher |

### Layer Count
- **Standard**: 4–16 layers
- **Advanced**: Up to 50 layers

### Board Thickness
- **Standard**: 0.20–0.80 mm
- **Advanced**: Down to 0.10 mm

### Plating Control
- **Seed-layer uniformity**: ±10%
- **Pulse-reverse**: Edge growth management
- **Differential etch**: Width control ±10%

### Warpage Control
- **Target**: ≤0.5% of diagonal
- **Critical for**: Flip-chip assembly yield
- **ABF thickness control**: Stabilizes impedance and PDN inductance

### Impedance
- **Tolerance**: ±5%

### Inspection
| Method | Resolution/Capability | Purpose |
|--------|----------------------|---------|
| AOI | ≤5 μm | Fine-line defect detection |
| X-ray | Registration targets | Alignment verification |
| IST | 200–500 cycles | Interconnect stress test |

### Applications
- Advanced semiconductor packaging
- Flip-chip (C4 bump) assemblies
- SiP (System in Package)
- Wire-bond ready substrates
- High-density fan-out

### Standards
- JEDEC-aligned reliability
- IPC-4101/4103 (materials)
- Signal integrity correlation

## Conditions And Methods

- SAP for maximum density
- Controlled warpage for flip-chip placement
- PDN loop inductance optimization

## Limits And Non-Claims

- SAP significantly more expensive than standard PCB
- Fine-line requires specialized cleanroom facilities
- IST cycles vary by design complexity

## Source Links

- Internal: `frontendhil-ic-substrate-pcb-product-en`
- Public: https://www.hilpcb.com/products/ic-substrate-pcb
