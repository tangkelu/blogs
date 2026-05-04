---
fact_id: "processes-apt-hdi-capability-specs"
title: "APT HDI PCB Manufacturing Capabilities"
topic: "HDI PCB manufacturing capabilities"
category: "processes"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids:
  - "frontendapt-hdi-pcb-capability-en"
tags: ["apt", "hdi", "microvia", "any-layer", "vippo", "fine-line"]
---

# Canonical Summary

> APT HDI capabilities: 32–64 layers, 1+N+1 to any-layer, 75–100 μm microvias, 3/3 mil trace/space, VIPPO.

## Stable Facts

### Layer Configurations
- **Types**: 1+N+1, 2+N+2, any-layer
- **Max layers**: 32–64

### Microvias
- **Diameter**: 0.075–0.10 mm (75–100 μm)
- **Types**: Blind, buried, stacked, VIPPO

### Trace/Space
- **Min**: 3/3 mil (0.076 mm)

### Impedance Control
- **Tolerance**: ±5%

### Lead Times
- **DFM review**: <24 hours
- **Prototype**: 24–48 hours

### Applications
- Smartphones
- Wearables
- Medical devices
- Automotive
- Aerospace
- High-speed networking

## Conditions And Methods

- Sequential build-up (SBU) technology
- Fine-line routing
- Controlled impedance for high-speed applications

## Limits And Non-Claims

- Specific layer count limits depend on design complexity
- Fine-line capability requires appropriate material selection
- Lead times subject to material availability

## Source Links

- Internal: `frontendapt-hdi-pcb-capability-en`
- Public: https://aptpcb.com/en/capabilities/hdi-pcb
