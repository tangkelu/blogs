---
task_id: "p4-142-frontendhil-advanced-products-index"
status: "completed"
owner: "cascade-agent"
lane: "frontendHIL Advanced Products Individual Indexing"
input_paths:
  - /code/hileap/frontendHIL/public/static/products/en/hdi-pcb.json
  - /code/hileap/frontendHIL/public/static/products/en/rigid-flex-pcb.json
  - /code/hileap/frontendHIL/public/static/products/en/high-frequency-pcb.json
  - /code/hileap/frontendHIL/public/static/products/en/rogers-pcb.json
  - /code/hileap/frontendHIL/public/static/products/en/ceramic-pcb.json
  - /code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json
output_paths:
  - /code/blogs/llm_wiki/sources/registry/internal/frontendhil-hdi-pcb-product-en.md
  - /code/blogs/llm_wiki/sources/registry/internal/frontendhil-rigid-flex-pcb-product-en.md
  - /code/blogs/llm_wiki/sources/registry/internal/frontendhil-high-frequency-pcb-product-en.md
  - /code/blogs/llm_wiki/sources/registry/internal/frontendhil-rogers-pcb-product-en.md
  - /code/blogs/llm_wiki/sources/registry/internal/frontendhil-ceramic-pcb-product-en.md
  - /code/blogs/llm_wiki/sources/registry/internal/frontendhil-turnkey-assembly-product-en.md
  - /code/blogs/llm_wiki/facts/internal/frontendhil-advanced-products-technical-boundary.md
  - /code/blogs/llm_wiki/logs/p4-142-frontendhil-advanced-products-index.md
write_scope:
  - /code/blogs/llm_wiki/sources/registry/internal/frontendhil-hdi-pcb-product-en.md
  - /code/blogs/llm_wiki/sources/registry/internal/frontendhil-rigid-flex-pcb-product-en.md
  - /code/blogs/llm_wiki/sources/registry/internal/frontendhil-high-frequency-pcb-product-en.md
  - /code/blogs/llm_wiki/sources/registry/internal/frontendhil-rogers-pcb-product-en.md
  - /code/blogs/llm_wiki/sources/registry/internal/frontendhil-ceramic-pcb-product-en.md
  - /code/blogs/llm_wiki/sources/registry/internal/frontendhil-turnkey-assembly-product-en.md
  - /code/blogs/llm_wiki/facts/internal/frontendhil-advanced-products-technical-boundary.md
blocked_claims:
  - real-time technology availability without verification
  - current certification status without validation
  - specific customer performance guarantees
  - unlimited layer count or via density capabilities
completed_at: "2026-05-03"
---

# P4-142 frontendHIL Advanced Products Index

## Scope

Individual indexing of 6 high-value HILPCB advanced product JSON files, extracting detailed technical specifications and creating aggregate capability boundary fact card.

## Changes Made

### Individual Source Records Created (6 files)

**`frontendhil-hdi-pcb-product-en.md`** (NEW)
- 50-75 μm laser microvias, aspect ratio ≤1:1
- Any-layer stackups (1+N+1 to any-layer)
- VIPPO (Via-in-Pad Plated Over) <10% dimple
- Low-loss Df 0.005-0.012 for 10-56 Gbps
- IST/HAST/1000+ thermal cycle qualification
- IATF 16949 / ISO 13485 / IPC Class 3

**`frontendhil-rigid-flex-pcb-product-en.md`** (NEW)
- IPC-6013 Class 3 workmanship
- Registration ±25-50 μm, impedance ±5%
- Dynamic/static bend options (R ≥ 10×t)
- Laser microvias 75-100 μm, depth ±5 μm
- Strain <0.3%, thermal shock −40↔+125°C
- AS9100 & ISO 13485 capable

**`frontendhil-high-frequency-pcb-product-en.md`** (NEW)
- Frequency: 500 MHz – 86 GHz mmWave
- Ultra-low-loss: Df 0.0009-0.004
- VNA S-parameter testing to 40-67 GHz
- Hybrid stackups (PTFE/ceramic + FR-4): 40-60% cost reduction
- Back-drill stubs <10 mil
- IPC-6012 Class 3 / MIL-PRF-31032

**`frontendhil-rogers-pcb-product-en.md`** (NEW)
- RO4350B, RO4835, RO3000, RT/duroid series
- Df 0.0009-0.004 @ 10 GHz, Dk ±2%
- Hybrid Rogers + FR-4: 30-50% cost savings
- Plasma activation >40 dynes/cm
- VNA to 40 GHz, TDR impedance ±5%
- IPC-6018 workflows

**`frontendhil-ceramic-pcb-product-en.md`** (NEW)
- Alumina (Al2O3) & AlN substrates
- Thermal conductivity: 170-190 W/m·K
- CTE match to silicon: ~4.5 ppm/°C
- DBC bond >1.4 N/mm, DPC 50/50 μm fine-line
- LTCC multilayer integration
- Temperature: −55°C to +250°C

**`frontendhil-turnkey-assembly-product-en.md`** (NEW)
- SMT, THT, mixed-technology
- Placement ±8-25 μm, 3D SPI ±10%
- AOI >95% detection, X-ray ≤25% voids
- ICT/FCT/Boundary-scan coverage
- FPY >98-99%, DPPM <500
- MES traceability, EOL alerts 6-12 months
- IATF 16949, ISO 9001:2015

### Aggregate Fact Card Created

**`frontendhil-advanced-products-technical-boundary.md`** (NEW)
- Comprehensive specifications for all 6 product categories
- Cross-cutting capabilities matrix (impedance, registration, thermal)
- Technology comparison tables
- Certification and qualification inventory

## Knowledge Value Added

1. **HDI Technology**: Detailed microvia and VIPPO specifications for high-density applications
2. **Rigid-Flex Capability**: IPC-6013 Class 3 with bend radius and strain engineering
3. **RF/mmWave Expertise**: Low-loss materials, VNA validation, frequency ranges
4. **Premium Materials**: Rogers portfolio with hybrid cost optimization
5. **Ceramic Solutions**: Thermal management and extreme environment capabilities
6. **Assembly Integration**: Comprehensive SMT/THT/test coverage with traceability

## Technical Specifications Summary

| Product | Key Spec | Range/Value |
|---------|----------|-------------|
| HDI | Microvia diameter | 50-75 μm |
| Rigid-Flex | Bend radius | R ≥ 10×t |
| High-Freq | Frequency | 500 MHz – 86 GHz |
| Rogers | Loss tangent | 0.0009-0.004 |
| Ceramic | Thermal conductivity | 170-190 W/m·K |
| Assembly | Placement accuracy | ±8-25 μm |

## Residual Gaps

| Gap | Reason | Status |
|-----|--------|--------|
| Real-time availability | Technology routing depends on capacity | `blocked` |
| Certification currency | IATF, AS9100, ISO status needs verification | `needs_review` |
| Maximum capabilities | Layer counts and via densities design-dependent | `blocked` |
| Customer-specific performance | Requires individual design review | `blocked` |

## HIL en Indexing Status

| Category | Indexed | Remaining |
|----------|---------|-----------|
| Advanced products (individual) | **6** | 0 |
| Basic products (grouped) | 5 | 0 |
| Service landings | 3 | 0 |
| **Total HIL en** | **33** | **~0** |

**frontendHIL English JSON indexing is now COMPLETE!**

## Relation to P4-141

Together with P4-141 (frontendAPT completion), this task completes the full English business JSON indexing for both brands:
- **frontendAPT**: 105 files (capabilities, industries, materials, pcb, pcba, resources, policies, about, quote, tools, home)
- **frontendHIL**: 33 files (all products + service landings)
- **Total en indexed**: 138 files

