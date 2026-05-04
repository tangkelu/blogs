# Fact Card: APT AOI & SPI Inspection Capabilities

## Fact Metadata

- **fact_id**: apt_aoi_spi_inspection_capabilities
- **fact_type**: inspection_capabilities
- **source_id**: apt_pcba_inspection_methods_aoi_spi
- **authority_tier**: Tier-2
- **domain**: pcba_inspection
- **application**: optical_quality_control
- **date_extracted**: 2026-05-02
- **verification_status**: verified

## AOI (Automated Optical Inspection)

### Technology
| Parameter | Capability |
|-----------|------------|
| **Inspection Types** | 2D & 3D AOI |
| **Defect Escape Rate** | <100 ppm |
| **Coverage** | 100% inline |
| **Integration** | SPI + X-Ray + ICT |
| **NPI Turnaround** | 24-48 hours |

### Defect Detection Capabilities

| Defect Category | Specific Defects |
|-----------------|------------------|
| **Component Issues** | Missing component, wrong component, incorrect orientation |
| **Placement Defects** | Misalignment, tombstoning, coplanarity issues, polarity errors |
| **Solder Defects** | Insufficient solder, excess solder, bridging/shorts, open joints |
| **Physical Defects** | Lifted leads, component damage, solder balls |

### Inspection Timing
- Post-print (optional, after solder paste)
- Pre-reflow (component placement verification)
- Post-reflow (solder joint quality)

---

## SPI (Solder Paste Inspection)

### Technology
| Parameter | Capability |
|-----------|------------|
| **Inspection Types** | 2D/3D SPI |
| **Measurements** | Volume, height, alignment, area |
| **Coverage** | Full coverage before component placement |
| **NPI Turnaround** | 24-48 hours |

### Defect Prevention

| Defect Type | Prevention Mechanism |
|-------------|----------------------|
| **Insufficient Paste** | Volume measurement catches potential opens |
| **Excess Paste** | Height/thickness detection prevents shorts |
| **Misalignment** | Offset measurement ensures pad alignment |
| **Stencil Issues** | Aperture blocking, wear detection |
| **Print Bridging** | Bridge detection between pads |

### Process Control Integration
- **SPI Feedback Loop**: Real-time data to stencil printer
- Process control integration
- Defect tracking with PPM monitoring
- Traceability: Barcode + lot
- IPC-A-610 Class 2/3

### Quality Metrics
| Metric | Target |
|--------|--------|
| First-pass yield improvement | Significant reduction in reflow defects |
| Defect prevention | Catches print defects before component placement |
| Process capability | Cpk monitoring for print quality |

---

## AOI vs SPI Comparison

| Aspect | AOI | SPI |
|--------|-----|-----|
| **Stage** | After component placement | Before component placement |
| **Focus** | Component + Solder | Solder paste only |
| **Defects Caught** | Placement, soldering | Print quality |
| **Technology** | 2D/3D optical | 3D laser/triangulation |
| **Value** | Catches assembly defects | Prevents defects from occurring |

---

## Integration in Inspection Chain

```
SPI (Solder Paste) → Component Placement → AOI (Placement) → 
Reflow → AOI (Solder) → X-Ray (Hidden Joints) → ICT/FCT (Electrical/Functional)
```

---

## Source Reference

> "来自 APTPCB 已审核静态页面, 发布于 aptpcb.com"
> - Source: apt_pcba_inspection_methods_aoi_spi
> - URLs: file:///code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json, file:///code/hileap/frontendAPT/public/static/pcba/en/spi-inspection.json
> - Authority: Tier-2 (internal_published_page)

## Usage Notes

AOI and SPI form the visual quality control foundation for PCBA manufacturing:
- SPI prevents defects by catching print issues before placement
- AOI catches placement and soldering defects after assembly
- Combined, they significantly reduce escapes and improve first-pass yield

## Design for Inspection (DFI) Recommendations

1. **Test Point Design**: Adequate spacing for probe access
2. **Component Orientation**: Consistent placement for automated inspection
3. **FIDUCIAL Placement**: For accurate AOI alignment
4. **Clearance**: Adequate space between components for inspection access
