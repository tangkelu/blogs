# Source Record: HIL FR-4 PCB Product Capabilities

## Source Metadata

- **source_id**: hil_fr4_pcb_capabilities
- **source_type**: internal_published_page
- **authority_tier**: Tier-2
- **organization**: HILPCB
- **title**: FR-4 PCB Manufacturing | High-Tg, Low-Loss, HDI | 12-Hour Express
- **url**: file:///code/hileap/frontendHIL/public/static/products/en/fr4-pcb.json
- **canonical_url**: https://hilpcb.com/products/fr4-pcb
- **date_published**: 2026-05-01
- **date_accessed**: 2026-05-02
- **must_refresh**: false

## Content Summary

FR-4 multilayer PCB manufacturing from standard to high-performance grades.

### Key Capabilities
| Feature | Specification |
|---------|-------------|
| **Express Manufacturing** | 12-hour express builds |
| **Quality** | IPC Class 3 compliance |
| **Certifications** | IATF 16949 & ISO 13485 |
| **Impedance Control** | ±5% tolerance |
| **HDI Microvia** | ≤0.075mm (75µm) |
| **Tg Range** | 130–180°C+ |

### Material Grades
| Grade | Tg | Applications |
|-------|-----|--------------|
| **Standard FR-4** | 130–140°C | Consumer, general embedded |
| **Mid-Tg** | 150–160°C | Denser multilayers |
| **High-Tg** | 170–180°C | Automotive, industrial, multiple reflow |
| **Low-Loss** | Df 0.009–0.012 | 10–25 Gbps signaling |

### Manufacturing Specifications
| Parameter | Standard | Advanced |
|-----------|----------|----------|
| **Layer Count** | 1–8 layers | Up to 32 layers |
| **Board Thickness** | 0.8–2.4mm | 0.4–6.0mm |
| **LDI Registration** | ±12.5µm | - |
| **Mechanical Drill** | 0.20mm | - |
| **Laser Microvia** | 0.075mm | - |
| **Plating Variation** | ±10% | - |

## Cross-Validation with APT Data

| Parameter | HIL Value | APT Value | Match |
|-----------|-----------|-----------|-------|
| Tg Range | 130–180°C | 130–180°C | ✅ |
| Microvia | ≤0.075mm | 0.075mm | ✅ |
| Impedance Tol | ±5% | ±5% | ✅ |
| Max Layers | 32 | 64 | APT higher |
| LDI Reg | ±12.5µm | Sub-3mil (75µm) | Comparable |

## Extraction Notes

Tier-2 internal source from HILPCB. FR-4 capabilities align with APTPCB data with consistent quality standards. Minor capability differences noted (max layers).
