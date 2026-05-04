---
fact_id: "materials-taconic-bonding-materials"
title: "Taconic fastRise 27 and TacLam Bonding Materials"
topic: "RF microwave materials"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendapt-taconic-pcb-json"
tags: ["taconic", "fastrise", "taclam", "bondply", "prepreg", "hybrid", "multilayer"]
---

# Canonical Summary

> Taconic offers two bonding solutions: fastRise 27 (low-loss thermoset prepreg for hybrid PTFE/FR-4 builds) and TacLam (pure PTFE film for all-PTFE multilayers).

## Stable Facts

### fastRise 27 / 27HF
| Property | Value |
|----------|-------|
| Dk | 2.72 ± 0.04 |
| Df @ 10GHz | 0.0014 |
| Thermal Conductivity | 0.28 W/m·K |
| Chemistry | Low-loss thermoset bonding prepreg |

**Purpose**: Bonding prepreg for hybrid multilayers combining PTFE signal cores with FR-4 structural cores.

**Applications**:
- Hybrid Taconic TLY/FR-4 multilayers
- Hybrid Rogers RO4350B/FR-4 bonding
- High-speed digital with integrated RF sections

### TacLam
| Property | Value |
|----------|-------|
| Dk | 2.10 - 2.35 |
| Df @ 10GHz | 0.0008 |
| Chemistry | Pure PTFE bonding film (unfilled) |

**Purpose**: Ultra-low-loss PTFE bonding film for all-PTFE multilayer constructions.

**Applications**:
- All-PTFE multilayer stripline networks
- Satellite transponders
- Defense radar antenna panels requiring uniform PTFE dielectric

## Conditions And Methods

- **fastRise**: Compatible with both Taconic and Rogers RF cores, standard lamination
- **TacLam**: Requires careful press-profile management (temperature/pressure controlled)
- Stocked at APTPCB: fastRise 27

## Limits And Non-Claims

- fastRise Df (0.0014) higher than core PTFE materials
- TacLam processing more demanding than fastRise
- Bondline quality affects overall RF performance

## Source Links

- Internal: `frontendapt-taconic-pcb-json`
- Public: https://aptpcb.com/en/materials/taconic-pcb
