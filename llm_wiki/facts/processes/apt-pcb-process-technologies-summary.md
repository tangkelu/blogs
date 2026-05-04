# Fact Card: APT PCB Process Technologies Summary

## Fact Metadata

- **fact_id**: apt_pcb_process_technologies_summary
- **fact_type**: process_capabilities
- **source_id**: apt_pcb_fabrication_core_processes
- **authority_tier**: Tier-2
- **domain**: pcb_manufacturing
- **application**: process_engineering
- **date_extracted**: 2026-05-02
- **verification_status**: verified

## Core Fabrication Process

### Process Flow
| Step | Technology | Key Capability |
|------|------------|----------------|
| **DFM Review** | Automated analysis | <24h feedback, ODB++/IPC-2581 native |
| **Inner Layer** | LDI imaging | Sub-3mil (75µm) precision, 3/3 mil L/S |
| **AOI** | Automated optical | Sub-mil defect capture |
| **Lamination** | Hydraulic press | Resin flow calculated, void-free |
| **Drilling** | CNC + Laser | 0.15mm mechanical, 0.075mm laser microvia |
| **Desmear** | Plasma + Chemical | PTFE compatible |
| **Plating** | Pulse-reverse | 15:1 aspect ratio, uniform copper |
| **Outer Layer** | LDI + Etch | Etch compensation for impedance |
| **Soldermask** | LPI (Liquid Photoimageable) | Registration accuracy |
| **Surface Finish** | 7 options | XRF-verified thickness |
| **Routing** | CNC precision | Complex shapes, tight tolerances |
| **E-Test** | Flying probe | Kelvin 4-wire, 100% coverage |
| **FQC** | Visual inspection | IPC-A-610 criteria |

### Critical Capabilities
| Parameter | Specification |
|-----------|---------------|
| **Line/Space** | 3/3 mil (75/75 µm) |
| **Drill Size** | 0.15mm mechanical, 0.075mm laser |
| **Aspect Ratio** | 15:1 plating capability |
| **Layer Count** | 4-64 layers standard |
| **Impedance Tolerance** | ±5Ω or ±7% |
| **Registration** | ±50µm backdrill accuracy |

## Drilling & Interconnect

### Drilling Technologies
| Type | Capability | Application |
|------|------------|-------------|
| **CNC Mechanical** | 0.15mm min drill, ±25µm | Standard through-holes |
| **UV Laser** | 0.075mm microvia | HDI, any-layer |
| **Backdrilling** | ±50µm depth control | Stub mitigation for high-speed |
| **VIPPO** | Via-in-pad plated over | BGA escape routing |
| **Plasma Desmear** | PTFE/Rogers compatible | High-frequency materials |

### Microvia Stacking
- Staggered microvias (preferred for reliability)
- Stacked microvias (higher density, requires ELIC)
- ELIC (Every Layer Interconnect) capability

## Surface Finishes

### Finish Selection Matrix
| Finish | Thickness | Best For | Shelf Life |
|--------|-----------|----------|------------|
| **ENIG** | Ni 3-5µm, Au 0.05-0.15µm | Fine pitch, wire bonding | 12 months |
| **ENEPIG** | Ni/Pd/Au | Universal finish, Al wire bond | 12 months |
| **Immersion Silver** | 0.15-0.4µm | RF, high-frequency | 6 months |
| **Immersion Tin** | 0.8-1.2µm | Press-fit connectors | 6 months |
| **OSP** | 0.2-0.5µm | Cost-sensitive, simple SMT | 6 months |
| **Hard Gold** | Ni 3-6µm, Au 0.8-2.5µm | Edge connectors | 24+ months |
| **LF-HASL** | SnCu alloy | Large components, cost | 12 months |

### XRF Verification
- Thickness measurement on every lot
- IPC J-STD-003 solderability compliance
- Dedicated chemistry lines prevent cross-contamination

## Impedance & Stack-up

### Impedance Control
| Structure | Typical Tolerance | Applications |
|-----------|-----------------|--------------|
| **Single-ended** | ±5Ω (target 50Ω) | RF, antennas |
| **Differential** | ±7% (target 90/100Ω) | USB, PCIe, Ethernet |
| **Coplanar** | ±7% | Mixed signal, RF/digital |

### Stack-up Design
- Polar Si9000 field solver
- 4-64 layer capability
- Hybrid material combinations (FR4 + Rogers)
- Resin flow calculation for void-free lamination
- Sequential lamination for HDI

## Quality Assurance

### Testing Protocol
| Test | Coverage | Standard |
|------|----------|----------|
| **Flying Probe** | 100% electrical | IPC-9252 |
| **TDR** | 100% impedance panels | ±5Ω verification |
| **AOI** | 100% inner/outer layers | IPC-A-610 |
| **X-Ray** | Sampling for BGA/QFN | IPC-A-610 |
| **Microsection** | Sampling per lot | IPC-6012 Class 3 |
| **Cleanliness** | Ionic contamination | IPC-TM-650 |

### Certifications
- ISO 9001:2015 (Quality Management)
- IATF 16949 (Automotive)
- ISO 13485 (Medical)
- AS9100 (Aerospace, via partners if needed)
- IPC-6012 Class 2/3 capability

## Advanced Technologies

### HDI Capability
| Feature | Specification |
|---------|---------------|
| Microvia diameter | 0.075mm (3mil) |
| Line/Space | 3/3 mil |
| Configurations | 1+N+1, 2+N+2, Any Layer |
| Laser type | UV laser ablation |

### Flex/Rigid-Flex
| Feature | Specification |
|---------|---------------|
| Flex layers | 1-8+ |
| Materials | Polyimide, LCP |
| Bend cycles | Static or 20,000+ dynamic |
| Stiffeners | FR4, aluminum, PI |

### Heavy Copper
| Feature | Specification |
|---------|---------------|
| Copper weight | Up to 20oz (700µm) |
| Techniques | External plating, embedded |
| Applications | Power electronics, motor drives |

### High-Frequency
| Feature | Specification |
|---------|---------------|
| Materials | Rogers, Taconic, Arlon, PTFE |
| DK range | 2.2-10.2 |
| DF (loss tangent) | 0.0009-0.0035 |
| Processing | Plasma desmear required |

## Design Guidelines

### Critical DFM Rules
1. **Aspect Ratio**: Keep plated holes <15:1
2. **Copper Balance**: Symmetrical stack-up preferred
3. **Annular Ring**: Maintain >0.15mm for vias
4. **Thermal Relief**: Use for plane connections
5. **Silkscreen**: Keep away from pads (≥0.15mm)
6. **Impedance**: Provide target values and tolerances

### Material Selection Guide
| Application | Recommended Material |
|-------------|---------------------|
| Standard digital | Standard FR-4 (Tg 130-140°C) |
| High temperature | High Tg FR-4 (Tg 170-180°C) |
| Low loss digital | Low-Dk FR-4, Megtron 6 |
| RF/Microwave | Rogers RO4350B, Taconic TLY-5 |
| High power | Metal core, heavy copper |
| Flex | Polyimide (Kapton) |

---

## Source Reference

> "来自 APTPCB 已审核静态页面, 发布于 aptpcb.com"
> - Sources: Core fabrication, drilling, finishes, impedance/stack-up, prototype, advanced technologies
> - URLs: file:///code/hileap/frontendAPT/public/static/pcb/en/*.json
> - Authority: Tier-2 (internal_published_page)

## Usage Notes

Complete PCB manufacturing capability from standard 4-layer boards to advanced 64-layer HDI with high-frequency materials. All processes backed by comprehensive quality assurance.
