# Fact Card: APT Assembly Process Overview

## Fact Metadata

- **fact_id**: apt_assembly_process_overview
- **fact_type**: process_capabilities
- **source_id**: apt_smt_assembly_processes
- **authority_tier**: Tier-2
- **domain**: pcba_assembly
- **application**: electronics_manufacturing
- **date_extracted**: 2026-05-02
- **verification_status**: verified

## Assembly Technologies

### SMT (Surface Mount Technology)

| Parameter | Capability |
|-----------|------------|
| **Production Lines** | 7 SMT lines |
| **Component Size Range** | 01005 to large QFPs/BGAs |
| **Minimum BGA Pitch** | 0.3mm |
| **Micro-Components** | 01005 placement capable |
| **Inspection** | X-Ray for BGA/QFN |
| **Process Control** | Reflow profiling per board |

### THT (Through-Hole Technology)

| Process | Capability |
|---------|------------|
| **Wave Soldering** | High-volume THT assembly |
| **Selective Soldering** | Precision for mixed boards |
| **Hand Soldering** | Complex/rare components |
| **Component Types** | Axial, radial, high-power |

### Assembly Process Flow

```
PCB Incoming Inspection → Stencil Printing (SPI) → 
SMT Placement (AOI) → Reflow (AOI) → 
THT Insertion → Wave/Selective Solder → 
Inspection (AOI/X-Ray) → Testing (ICT/FCT) → 
Final QC → Packaging
```

## Production Models

| Model | Description | Typical Volume |
|-------|-------------|----------------|
| **Prototype** | 1-5 day builds, no MOQ | 1-10 units |
| **Small Batch** | Quick-turn, flexible | 10-100 units |
| **NPI** | DFX-first, pilot ready | 100-1000 units |
| **Mass Production** | Scaled, cost-optimized | 1000+ units |
| **Turnkey** | Full service, components to box | Any volume |

## Quality Integration

### Inspection Chain
```
SPI → AOI (Pre-reflow) → Reflow → AOI (Post-reflow) → 
X-Ray (BGA/QFN) → ICT/FCT → FQI
```

### Quality Systems
| System | Function |
|--------|----------|
| **Process Control** | SPI feedback loop, SPC |
| **Defect Tracking** | PPM monitoring, trend analysis |
| **Traceability** | Barcode + lot tracking |
| **Standards** | IPC-A-610 Class 2/3 |

## Specialized Capabilities

### Flex/Rigid-Flex Assembly
| Feature | Consideration |
|---------|---------------|
| Fixturing | Specialized for flexible substrates |
| Handling | Low-stress procedures |
| Temperature | Material limitations considered |
| Stiffeners | FR4, aluminum, polyimide |

### BGA/QFN Fine Pitch
| Feature | Capability |
|---------|------------|
| Minimum Pitch | 0.3mm |
| Inspection | X-Ray mandatory |
| Rework | Reballing services |
| Profile | Thermal optimization |

### Selective Soldering
| Feature | Benefit |
|---------|---------|
| Nitrogen Inerting | Improved joint quality |
| Mini-wave | Precision control |
| Dedicated Nozzle | Complex patterns |

### Conformal Coating
| Coating Type | Properties |
|--------------|------------|
| **Acrylic** | Easy repair, moisture resistant |
| **Urethane** | Chemical/abrasion resistant |
| **Silicone** | High temp, flexible |
| **Epoxy** | Maximum protection |

## Value-Added Services

| Service | Description |
|---------|-------------|
| **IC Programming** | Flash, MCU, FPGA loading |
| **Cable Assembly** | Custom interconnects |
| **Box Build** | System integration |
| **Test Development** | ICT/FCT fixture and program |
| **DFM Review** | Manufacturability optimization |

## Material Management

| Capability | Description |
|------------|-------------|
| **Component Sourcing** | Global supplier network |
| **AVL Management** | Approved vendor governance |
| **BOM Optimization** | Cost and lead time |
| **Kitting** | Component preparation |
| **Traceability** | Full component tracking |

## Metrics & Performance

| Metric | Target |
|--------|--------|
| **First-Pass Yield** | >95% typical |
| **Defect Rate** | <100 ppm |
| **On-Time Delivery** | >98% |
| **Customer Satisfaction** | Continuous improvement |

---

## Source Reference

> "来自 APTPCB 已审核静态页面, 发布于 aptpcb.com"
> - Source: apt_smt_assembly_processes
> - URLs: file:///code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json, file:///code/hileap/frontendAPT/public/static/pcba/en/turnkey-assembly.json, file:///code/hileap/frontendAPT/public/static/pcba/en/mass-production.json
> - Authority: Tier-2 (internal_published_page)

## Usage Notes

Comprehensive PCBA assembly capabilities from prototype to mass production, with full vertical integration from components to finished assemblies.
