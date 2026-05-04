# Fact Card: APT PCB Manufacturing Capability Parameters - Rigid PCB

## Fact Metadata

- **fact_id**: apt_pcb_capability_parameters_rigid
- **fact_type**: capability_parameters
- **source_id**: apt_rigid_pcb_capability_page
- **authority_tier**: Tier-2
- **domain**: pcb_manufacturing
- **application**: rigid_pcb
- **date_extracted**: 2026-05-02
- **verification_status**: verified

## Capability Parameters

### Layer Count and Board Geometry

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Max layer count | 64 | layers | Rigid PCB |
| Min board size | 10 × 10 | mm | |
| Max board size | 610 × 1100 | mm | |
| Thickness range | 0.20 - 8.0 | mm | |
| Thickness tolerance (<1.0mm) | ±0.10 | mm | |
| Thickness tolerance (≥1.0mm) | ±10 | % | |

### Trace and Space

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Min inner trace/space | 2/2 | mil | |
| Min outer trace/space | 2/2 | mil | |
| Max inner copper | 20 | oz | |
| Max outer copper | 20 | oz | |

### Drilling and Vias

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Min mechanical drill | 0.15 | mm | |
| Min laser drill | 0.075 | mm | Microvias |
| Mechanical aspect ratio | 20:1 | | Max |
| Laser aspect ratio | 1:1 | | Microvias |
| PTH tolerance | ±0.075 | mm | |
| NPTH tolerance | ±0.05 | mm | |
| Press-fit tolerance | ±0.05 | mm | |
| Countersink tolerance | ±0.15 | mm | |

### Registration and Alignment

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Layer-to-layer registration | ±50 | μm | Typical |
| Solder mask registration | ±75 | μm | Typical |

### Impedance Control

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Single-ended (≤50Ω) | ±5 | Ω | |
| Single-ended (>50Ω) | ±7 | % | |
| Differential (≤50Ω) | ±5 | Ω | |
| Differential (>50Ω) | ±7 | % | |

### HDI Capability

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| SBU layers | 1-3 | | Sequential build-up |
| BGA pitch support | 0.3 | mm | With HDI via-in-pad |

### Quality and Reliability

| Parameter | Value | Unit | Condition |
|-----------|-------|------|-----------|
| Board warpage | ≤0.75 | % | Per IPC |
| Hi-pot test range | 50-3000 | V | Available on request |

## Source Reference

> "来自 APTPCB 已审核静态页面, 发布于 aptpcb.com"
> - Source: apt_rigid_pcb_capability_page
> - URL: file:///code/hileap/frontendAPT/public/static/capabilities/en/rigid-pcb.json
> - Authority: Tier-2 (internal_published_page)

## Usage Notes

These parameters represent confirmed manufacturing capabilities from APTPCB's published capability data. Values are suitable for:
- Design rule checking
- Stack-up feasibility assessment
- Manufacturing capability verification
- Customer communication

## Limitations

- Values beyond these limits require engineering consultation
- Special materials and processes may have different constraints
- Tighter tolerances available on request after DFM review
