---
fact_id: "processes-hil-high-speed-capability-specs"
title: "HIL High-Speed Digital PCB Manufacturing Capabilities"
topic: "High-speed PCB manufacturing capabilities"
category: "processes"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendhil-high-speed-pcb-product-en"
tags: ["hil", "high-speed", "pam4", "nrz", "pcie", "112g", "back-drilling", "signal-integrity"]
---

# Canonical Summary

> HIL high-speed digital capabilities: 25–112 Gbps PAM4/NRZ, PCIe Gen5/6, back-drilling to 5 mil stubs, SI/PI co-design.

## Stable Facts

### Data Rates
- **PAM4/NRZ**: 25–112 Gbps
- **Interfaces**: PCIe Gen5/Gen6

### Materials
- **Df range**: 0.001–0.004 @ 10 GHz
- **Standard**: Isola I-Speed, RO4350B
- **Advanced**: Megtron 6/7, Tachyon 100G, PTFE

### Impedance Control
- **Differential**: 85/90/100Ω ±5%
- **Validation**: TDR
- **Pair length tolerance**: ≤5–10 mil

### Back-Drilling
- **56G+**: Residual stubs <10 mil
- **112G**: ~5 mil target
- **Cross-section**: Verified per build

### Manufacturing Precision
- **LDI trace width**: ±10%
- **Registration**: ±25–50 μm
- **Layer count**: 2–48 layers
- **Copper**: 0.5–5 oz

### SI/PI Features
- **Skew mitigation**: ±7° routing or spread-glass
- **PDN**: Target impedance modeling
- **Hybrid stacks**: Ultra-low-loss + FR-4 (30–50% cost reduction)

### Channel Performance
- **Megtron 6**: 28 Gbps NRZ over 12–15 inches
- **Tachyon 100G**: 56–112 Gbps PAM4 over 20–25 inches
- **Low-profile copper**: Ra ≤1.5 μm (3–8% loss reduction)

## Conditions And Methods

- Statistical process control for lot-to-lot consistency
- Multi-depth back-drilling with verification
- Hybrid stackups optimized for cost/performance

## Limits And Non-Claims

- 112G channels require careful material selection and stackup design
- Channel reach depends on total loss budget
- Does not guarantee specific BER performance

## Source Links

- Internal: `frontendhil-high-speed-pcb-product-en`
- Public: https://www.hilpcb.com/products/high-speed-pcb
