---
fact_id: "materials-arlon-ad-series-antenna"
title: "Arlon AD250/300/1000 Antenna-Grade PTFE Laminate"
topic: "RF microwave materials"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendapt-arlon-pcb-json"
tags: ["arlon", "ad250", "ad300", "ad1000", "antenna", "ptfe", "high-dk", "gps", "miniaturization"]
---

# Canonical Summary

> Arlon AD series (AD250/AD300/AD1000) are antenna-grade PTFE composites offering a wide range of dielectric constants. AD1000 (Dk 10.2) enables extreme miniaturization of patch antennas and filters.

## Stable Facts

### Electrical Properties
| Grade | Dk | Df @ 10GHz |
|-------|-----|-----------|
| AD250 | 2.50 | 0.0014 |
| AD300 | ~3.00 | 0.0014 |
| AD1000 | 10.2 | 0.0014 |

### Key Characteristics
- Antenna-grade PTFE / woven glass / ceramic
- Wide Dk range: 2.50 - 10.2
- Consistent Df 0.0014 across grades
- Requires plasma desmear
- AD1000 for extreme miniaturization

### Applications
- GPS/GNSS patch antennas
- Dielectric resonator antennas (DRA)
- Miniaturized filters
- Broadband base station antennas

## Conditions And Methods

- AD1000 Dk 10.2 allows 3x size reduction vs. standard FR-4
- Low Df (0.0014) maintains good efficiency at reduced size
- Plasma desmear mandatory

## Limits And Non-Claims

- Narrower bandwidth at higher Dk
- AD1000 requires precise impedance control
- Not for high-power applications (use TC350 instead)

## Source Links

- Internal: `frontendapt-arlon-pcb-json`
- Public: https://aptpcb.com/en/materials/arlon-pcb
