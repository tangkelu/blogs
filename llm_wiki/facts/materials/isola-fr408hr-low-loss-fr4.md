---
fact_id: "materials-isola-fr408hr-low-loss-fr4"
title: "Isola FR408HR Low-Loss FR-4 Laminate"
topic: "High-speed digital materials"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendapt-isola-pcb-json"
tags: ["isola", "fr408hr", "low-loss-fr4", "pcie", "nvme", "25g", "server", "data-center"]
---

# Canonical Summary

> Isola FR408HR is the default low-loss FR-4 choice for PCIe Gen4/Gen5 and 25G optical transceivers. 30% improvement in Z-axis expansion and 25% more electrical bandwidth than standard FR-4.

## Stable Facts

### Electrical Properties (@ 10 GHz)
- **Dk**: 3.68
- **Df**: 0.0092
- **Test Method**: IPC-TM-650 2.5.5.5

### Thermal Properties
- **Tg**: 190°C (DSC)
- **Td**: 360°C (TGA 5%)
- **CTE Z**: 35 ppm/°C (below Tg)
- **Moisture Absorption**: 0.10%

### Key Characteristics
- Lead-free compatible mid-loss laminate
- Tg 190°C (higher than standard FR-4)
- Spread-glass weave available for skew control
- Compatible with AOI and UV-blocking solder mask
- 30% improvement in Z-axis expansion vs. standard FR-4
- 25% more electrical bandwidth than standard FR-4

### Applications
- PCIe Gen4/Gen5 host bus adapters
- NVMe switch boards
- 25G optical transceivers
- High-layer-count HDI
- Data center infrastructure

## Conditions And Methods

- Stocked at APTPCB
- Common thicknesses available
- Spread-glass for fiber-weave skew control
- Compatible with standard FR-4 processing

## Comparison

| Property | 370HR | FR408HR | I-Speed |
|----------|-------|---------|---------|
| Dk | 4.04 | 3.68 | 3.64 |
| Df | 0.021 | 0.0092 | 0.0060 |
| Use Case | Standard | PCIe Gen4/5 | 25G SerDes |

## Limits And Non-Claims

- Df 0.0092 insufficient for 56G PAM4 (use I-Tera MT40)
- Higher cost than standard 370HR
- Does not guarantee specific channel compliance

## Source Links

- Internal: `frontendapt-isola-pcb-json`
- Public: https://aptpcb.com/en/materials/isola-pcb
