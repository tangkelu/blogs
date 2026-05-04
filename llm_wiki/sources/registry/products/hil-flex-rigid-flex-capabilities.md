# Source Record: HIL Flexible & Rigid-Flex PCB Capabilities

## Source Metadata

- **source_id**: hil_flex_rigid_flex_capabilities
- **source_type**: internal_published_page
- **authority_tier**: Tier-2
- **organization**: HILPCB
- **title**: Flexible PCB (FPC) & Rigid-Flex Manufacturing | Polyimide & LCP | Dynamic Bending & RF
- **url**: file:///code/hileap/frontendHIL/public/static/products/en/flex-pcb.json, file:///code/hileap/frontendHIL/public/static/products/en/rigid-flex-pcb.json
- **canonical_url**: https://hilpcb.com/products/flex-pcb, https://hilpcb.com/products/rigid-flex-pcb
- **date_published**: 2026-05-01
- **date_accessed**: 2026-05-02
- **must_refresh**: false

## Content Summary

High-reliability flexible and rigid-flex PCBs for dynamic and space-constrained applications.

### Flexible PCB Capabilities
| Feature | Specification |
|---------|-------------|
| **Materials** | Polyimide (PI), Liquid Crystal Polymer (LCP) |
| **Copper Options** | Rolled Annealed (RA), Electrodeposited (ED) |
| **Fine Line** | 50/50µm (2/2 mil) capability |
| **Impedance Control** | ±10% (±5% available) |
| **Dynamic Bend** | >1 million cycles |
| **Layer Count** | 1–8 layers |
| **Thickness** | 0.05–0.40mm |

### Rigid-Flex Capabilities
| Feature | Specification |
|---------|-------------|
| **Layer Count** | 4–16+ layers typical |
| **Flex Layers** | 1–6+ flexible sections |
| **Stiffeners** | PI, FR-4, steel, aluminum |
| **Bend Cycles** | Static or dynamic (20,000+) |

### Design Guidelines
- Bend radius R ≥ 10× thickness for dynamic designs
- Staggered traces in flex regions
- Teardrops and filleted coverlay apertures
- Neutral axis at conductor plane
- Avoid vias in flex regions

### Specifications
| Parameter | Standard | Advanced |
|-----------|----------|----------|
| **Base Materials** | Polyimide, ED copper | LCP, RA copper |
| **Thickness** | 0.05–0.20mm | Up to 0.40mm |
| **Bend Cycles** | Static | >1M dynamic |
| **Certification** | IPC-6013 Class 2/3 | - |
| **Testing** | 100% AOI & E-test | - |

## Cross-Validation with APT Data

| Parameter | HIL Value | APT Value | Match |
|-----------|-----------|-----------|-------|
| Materials | PI, LCP | PI, LCP | ✅ |
| Fine Line | 50/50µm | 3/3 mil (75µm) | HIL finer |
| Dynamic Bend | >1M cycles | 20,000+ | HIL higher spec |
| Max Layers | 8 (flex) | 8+ (flex) | ✅ |
| Impedance | ±10%/±5% | ±5% | ✅ |

## Extraction Notes

Tier-2 internal source from HILPCB. Flex capabilities comparable to APTPCB. HIL emphasizes finer line/space (50µm vs 75µm) and higher bend cycle ratings.
