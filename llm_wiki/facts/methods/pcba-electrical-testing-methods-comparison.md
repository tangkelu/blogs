# Fact Card: PCBA Electrical Testing Methods Comparison

## Fact Metadata

- **fact_id**: pcba_electrical_testing_methods_comparison
- **fact_type**: method_comparison
- **source_ids**: [apt_ict_testing_page, apt_flying_probe_testing_page, apt_xray_inspection_page]
- **authority_tier**: Tier-2
- **domain**: pcba_testing
- **application**: electrical_verification
- **date_extracted**: 2026-05-02
- **verification_status**: verified

## Testing Methods Overview

### In-Circuit Test (ICT) - Bed of Nails

**Core Characteristics**:
- Fixture-based testing with custom bed-of-nails
- High coverage: ≥80% nets typical
- Test speed: Seconds per board
- Best for: High-volume production, stable designs

**Capabilities**:
- Electrical verification of individual components
- Interconnection checking (traces, vias, solder joints)
- Component value verification (R, C, L)
- Polarity checking for polarized components
- Short/open circuit detection
- Boundary-scan integration for BGA access

**Defects Detected**:
| Defect Type | Detection |
|-------------|-----------|
| Short circuits | ✓ (solder bridges) |
| Open circuits | ✓ (lifted pads, open traces) |
| Missing components | ✓ |
| Incorrect component values | ✓ |
| Wrong component orientation | ✓ (polarized) |
| Damaged components | ✓ (electrically) |
| Solder joint quality | ✓ (electrical integrity) |

**Requirements**:
- Custom fixture design and fabrication
- Test point access on both sides
- Test program development from CAD/BOM
- Lead time: 24-48 hours for NPI

**Cost Structure**:
- Fixture investment required
- Low per-board cost once fixture made
- Economical for high volumes

---

### Flying Probe Test (FPT)

**Core Characteristics**:
- Fixture-free, software-driven testing
- Robotic probes access test points directly
- Test speed: Slower than ICT but no fixture overhead
- Best for: Prototypes, low-medium volume, frequent design changes

**Capabilities**:
- Continuity verification
- Short-circuit detection
- Component value measurement (R/C/L)
- Diode/transistor polarity and functionality
- Power net and isolation testing
- Both bare PCB and PCBA testing

**Design Guidelines**:
| Parameter | Recommendation |
|-----------|---------------|
| Test point diameter | 0.5-1.0 mm typical |
| Test point shape | Circular standard |
| Surface finish | ENIG or HASL (smooth, conductive) |
| Solder mask clearance | Adequate clearance around test points |
| Accessibility | Avoid component obstruction |
| Dual-side coverage | Utilize both sides for comprehensive access |
| Clamping areas | Designate non-critical regions |
| Edge clearance | Maintain space for clamping |

**Advantages vs ICT**:
| Factor | FPT | ICT |
|--------|-----|-----|
| Fixture cost | Zero | Custom fixture required |
| Setup time | Fast (software) | Longer (fixture fab) |
| Design change accommodation | Immediate | Fixture modification needed |
| Fine-pitch access | Excellent | Limited by fixture |
| Board modifications | None required | May need test pads |
| Per-board test time | Longer | Faster |
| Volume suitability | Low-medium | High |

**Bare PCB vs PCBA FPT**:
| Aspect | Bare PCB | PCBA |
|--------|----------|------|
| Focus | Traces, vias, pads integrity | + Component verification |
| Timing | Post-fab, pre-assembly | Post-assembly |
| Test types | Continuity, shorts, impedance, isolation | + Component presence/value/orientation |
| Accessibility | Full, unobstructed | Limited by components |
| Speed | Faster | Slower |
| Faults detected | Manufacturing defects | + Assembly + Component issues |

---

### X-Ray Inspection

**Core Characteristics**:
- Non-destructive internal visualization
- Penetrates multiple PCB layers
- Detects hidden/subsurface defects
- Best for: BGA, HDI, multilayer, hidden joints

**Inspection Types**:
| Type | Capability | Application |
|------|-----------|-------------|
| 2D X-ray | Flat top-down view | Quick checks, solder bridging |
| 2.5D X-ray | Multiple angled images | Hidden joints, BGAs |
| 3D CT | Full 3D model, virtual cross-section | Critical analysis, complex defects |

**Defect Detection**:
| Defect Category | Specific Defects |
|-----------------|------------------|
| Solder joints | Voids, incomplete wetting, cracks |
| Open circuits | Lifted pads, micro-cracks, via breaks |
| Short circuits | Internal bridging, solder whiskers, debris |
| Component issues | Misalignment, tombstoning, insufficient solder |
| Internal layers | Trace breaks, delamination, voids, via barrel separation |

**Value Areas**:
- HDI boards (microvias, stacked vias)
- Multilayer PCBs with complex internal routing
- BGA and bottom-terminated packages
- Miniaturized electronics (wearables, IoT)

**Process**:
1. Sample preparation and positioning
2. Parameter optimization (voltage, current, exposure)
3. Systematic scanning
4. Image processing and enhancement
5. Analysis by trained operators (AI-augmented)
6. Detailed reporting with annotated images

---

## Test Method Selection Guide

### By Production Volume
| Volume | Recommended Primary Method | Complementary |
|--------|---------------------------|---------------|
| Prototype | FPT | X-ray (for BGA) |
| Low volume (<100) | FPT | X-ray (for hidden joints) |
| Medium volume (100-1000) | FPT or ICT | AOI + X-ray |
| High volume (>1000) | ICT | AOI + X-ray + sample FPT |

### By Board Characteristics
| Board Type | Recommended Methods |
|------------|---------------------|
| Simple, low density | AOI + FPT |
| High density, fine pitch | AOI + FPT + X-ray |
| BGA/QFN packages | X-ray mandatory + ICT/FPT |
| HDI with microvias | X-ray mandatory + ICT/FPT |
| Multilayer (>8 layers) | X-ray recommended + ICT/FPT |
| Rigid-flex | FPT + X-ray (flex areas) |

### By Defect Concern
| Primary Concern | Test Method Priority |
|-----------------|---------------------|
| Component values | ICT or FPT |
| Solder joint integrity | X-ray + AOI |
| BGA solder quality | X-ray (mandatory) |
| Trace/via integrity | FPT (bare PCB) or ICT |
| Assembly correctness | AOI + FPT/ICT |
| Hidden defects | X-ray |

---

## Integrated Quality Strategy

APTPCB recommended inspection chain:

```
SPI (Solder Paste) → AOI (Placement) → Reflow → AOI (Post-reflow) → 
X-Ray (Hidden joints) → ICT/FPT (Electrical) → FCT (Functional)
```

### Method Complementarity

| Combination | Value |
|-------------|-------|
| AOI + ICT/FPT | Physical + electrical verification |
| ICT + X-ray | Electrical + hidden joint integrity |
| FPT (bare) + FPT (PCBA) | Foundational + assembly verification |
| All three methods | Comprehensive coverage |

### Quality Integration Features

- NPI turnaround: 24-48 hours for all methods
- Process control: SPI feedback loop integration
- Defect tracking: PPM monitoring
- Traceability: Barcode + lot tracking
- Standards: IPC-A-610 Class 2/3

---

## Source References

> "来自 APTPCB 已审核静态页面, 发布于 aptpcb.com"
> - Sources: apt_ict_testing_page, apt_flying_probe_testing_page, apt_xray_inspection_page
> - URLs: file:///code/hileap/frontendAPT/public/static/pcba/en/*.json
> - Authority: Tier-2 (internal_published_page)

## Usage Notes

This comparison enables:
- Test method selection for specific applications
- Cost-optimization for different volumes
- Quality strategy development
- Design for testability (DFT) planning

## Key Decision Factors

1. **Volume**: FPT for low/medium, ICT for high
2. **Complexity**: X-ray for HDI/BGA
3. **Budget**: FPT has lower upfront cost
4. **Speed**: ICT faster per board (after fixture)
5. **Flexibility**: FPT accommodates design changes instantly
6. **Coverage**: Combine methods for comprehensive verification
