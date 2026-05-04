---
fact_id: "high_speed_pcb_interface_requirements_and_design_boundaries"
title: "High-Speed PCB Interface Requirements and Design Boundaries"
topic: "High-Speed Interfaces SERDES PCIe Ethernet"
category: "interfaces"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
source_ids: ["apt_high_speed_pcb_interfaces_page"]
tags: ["high-speed", "interfaces", "PCIe", "Ethernet", "PAM4", "SERDES", "signal-integrity"]
---

# Canonical Summary

> High-speed PCB design requirements for 10-112 Gbps interfaces, covering material selection, geometry constraints, and validation methods.

## Supported Interface Standards

### PCIe Family
| Generation | Data Rate | Key Requirements |
|------------|-----------|------------------|
| **Gen 4** | 16 GT/s | Low-loss FR-4 or better |
| **Gen 5** | 32 GT/s | Df < 0.005, VLP copper |
| **Gen 6** | 64 GT/s | Df < 0.002, HVLP copper, via optimization |

### Ethernet Family
| Standard | Data Rate | PCB Requirements |
|----------|-----------|-------------------|
| **10GBASE-KR** | 10 Gbps | Standard low-loss materials |
| **25GBASE-KR/CR** | 25 Gbps | Megtron 4/6 class materials |
| **40GBASE-CR4/KR4** | 40 Gbps | Controlled impedance, via stub control |
| **100GBASE-CR4/KR4** | 100 Gbps | Low-loss stackup, PAM4 signaling |
| **400GBASE** | 400 Gbps | Ultra-low loss, advanced equalization |

### PAM4 Signaling
| Rate | Loss Budget | Material Requirement |
|------|-------------|---------------------|
| **56G PAM4** | ~28 dB @ 14 GHz | Megtron 6, I-Tera MT40 |
| **112G PAM4** | ~20 dB @ 28 GHz | Megtron 7/U, Tachyon 100G |

## Material Selection by Speed

### 10-16 Gbps
- **Materials**: Standard FR-4 (370HR), IT-180A
- **Df**: < 0.020
- **Copper**: Standard or VLP

### 25-28 Gbps  
- **Materials**: Megtron 4, FR408HR, I-Speed
- **Df**: < 0.006
- **Copper**: VLP (Ra 3-4 µm)

### 56 Gbps
- **Materials**: Megtron 6, I-Tera MT40, Tachyon 100G
- **Df**: < 0.004
- **Copper**: HVLP (Ra 1.5-2 µm)

### 112 Gbps
- **Materials**: Megtron 7/U, Tachyon 100G, EM-890K
- **Df**: < 0.002
- **Copper**: HVLP or better (Ra < 1.5 µm)

## Geometry Requirements

### Trace/Space
| Speed | Min Line/Space | Imaging Method |
|-------|---------------|----------------|
| ≤ 25 Gbps | 3/3 mil | Standard LDI |
| 56 Gbps | 3/3 mil | LDI |
| 112 Gbps | 2/2 mil | Advanced LDI |

### Via Requirements
| Type | Drill | Pad | Application |
|------|-------|-----|-------------|
| Through-hole | 0.20 mm | 0.45 mm | General routing |
| Microvia | 0.075 mm | 0.175 mm | Build-up layers |
| VIPPO | 0.10 mm | 0.25 mm | BGA escape |

### Backdrill Requirements
- Residual stub < 0.25 mm (10 mil)
- Depth tolerance ± 0.05 mm
- Required for > 5 Gbps signals

## Signal Integrity Constraints

### Impedance Control
| Interface | Target | Tolerance |
|-----------|--------|-----------|
| Single-ended | 50 Ω | ± 5% |
| Differential | 100 Ω | ± 5% |

### Length Matching
| Speed | Intra-pair Skew | Inter-pair Skew |
|-------|-----------------|-----------------|
| ≤ 10 Gbps | < 10 ps | < 100 ps |
| 25 Gbps | < 5 ps | < 50 ps |
| 56 Gbps | < 2 ps | < 20 ps |
| 112 Gbps | < 1 ps | < 10 ps |

### Return Path
- Continuous reference plane required
- Stitching vias within 1.5 mm of layer transitions
- Avoid splits under high-speed traces

## Validation Methods

### Electrical Validation
| Test | Purpose | Frequency |
|------|---------|-----------|
| TDR | Impedance verification | All builds |
| VNA | S-parameter validation | > 25 Gbps |
| Eye diagram | Signal quality | > 56 Gbps |
| Insertion loss | Channel budget | > 25 Gbps |

### COM (Channel Operating Margin)
- Required for 56G/112G PAM4
- COM > 3 dB for robust operation
- Includes crosstalk, noise, jitter

## Design Checklist

### Stackup Planning
- [ ] Symmetric construction
- [ ] Power/ground pairs < 3 mil separation
- [ ] Material compatibility (CTE match)
- [ ] Resin content documented

### Routing
- [ ] Differential pair coupling maintained
- [ ] Phase matching within skew budget
- [ ] Via count minimized
- [ ] Backdrill specified for > 5 Gbps

### Power Integrity
- [ ] Target impedance documented vs frequency
- [ ] Decoupling strategy for fast loads
- [ ] Plane continuity verified

### Documentation
- [ ] Stackup with materials and thicknesses
- [ ] Impedance table per layer
- [ ] Length matching requirements
- [ ] Test point locations

## Source References

- Source: `apt_high_speed_pcb_interfaces_page`
- URL: https://aptpcb.com/en/pcb/high-speed-pcb
- Material datasheets: Megtron 6/7, Tachyon 100G, I-Tera MT40
- Standards: PCIe CEM, IEEE 802.3, OIF CEI

## Usage Notes

This fact card supports:
- Interface capability assessment
- Material selection guidance
- Stackup planning
- Validation planning
- Risk identification for high-speed designs

---

*Authority: Tier-2 (internal published page) | Date: 2026-05-02*
