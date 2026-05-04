---
source_id: "frontendhil-turnkey-assembly-product-en"
title: "HILPCB Turnkey Assembly Product - SMT, THT, Box Build with MES Traceability"
organization: "HILPCB"
source_type: "internal_json"
url: "/code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json"
jurisdiction: "internal"
published_at: ""
checked_at: "2026-05-03"
trust_tier: "t2"
stability: "semi_stable"
must_refresh: true
topic_tags: ["internal", "hilpcb", "turnkey-assembly", "smt", "tht", "box-build", "mes", "traceability", "bom-lifecycle", "iatf-16949"]
status: "active"
notes: "Turnkey PCB assembly service from BOM sourcing through box build with 3D SPI/AOI/X-ray, ICT/FCT, and MES traceability."
---

# Source Summary

## What It Covers

- `/code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json`

### Product Overview

**Title**: PCB Assembly Service | Turnkey PCB Assembly from BOM Sourcing to Box Build

**Key Capabilities**:
- SMT, through-hole, mixed-technology
- Prototype to 1M+ units volume
- Placement accuracy: ±8–25 μm
- 3D SPI/AOI/X-ray inspection
- ICT/FCT/Boundary-scan testing
- MES traceability with serialization
- BOM lifecycle control with 6-12 month EOL alerts
- FPY typically >98-99%

### Trust Bar Features

- Prototype → 1M+ Units
- BOM Lifecycle & EOL Alerts (6–12 months)
- 3D SPI/AOI, Sample X-ray
- ICT/FCT/Boundary-Scan Coverage
- MES Traceability, FPY typically >98%

### Technical Specifications

| Parameter | Value |
|-----------|-------|
| Placement accuracy | ±8–25 μm |
| SPI paste volume tolerance | ±10% |
| 3D SPI/AOI defect detection | >95% |
| X-ray void criteria | ≤25% (BGA/QFN) |
| Conformal coating | 25–75 μm |
| FPY (First Pass Yield) | >98-99% (mature) |
| DPPM (mature) | <500 |

### Process Flow

1. **BOM Scrub**: Lifecycle review, parametric equivalence, alternates (3-5 sources)
2. **Sourcing**: Authorized distribution, XRF/decapsulation/AS6081 for brokers
3. **SMT**: Print → SPI → Place → Reflow → AOI
4. **THT**: Wave/selective solder with nitrogen
5. **Inspection**: 3D SPI, AOI, sample X-ray
6. **Testing**: ICT (manufacturing), Flying probe (low-volume), Boundary scan (digital), FCT (system)
7. **Box Build**: Firmware loading, cable harness, conformal coating
8. **Traceability**: MES traveler with lot/date code tracking

### Key Systems

- QMS revision control for ECOs
- AVL-controlled sourcing
- ERP + MES integration
- IATF 16949 and ISO 9001:2015

## Why It Matters

- Single-accountability workflow eliminates multi-vendor delays (15-25%)
- Full traceability from component to finished product
- Comprehensive test coverage at multiple stages
- Scales from prototype through 1M+ units

## Extraction Notes

- Safe for process descriptions and inspection stages
- Safe for placement accuracy and test coverage claims
- Safe for FPY/DPPM as stated typical performance
- Do not treat >98% FPY as guaranteed for all programs
- Do not cite specific pricing or lead times without refresh

## Refresh Notes

- Refresh before external use: current FPY/DPPM performance
- Verify current MES/ERP capabilities and serialization
- Confirm IATF 16949 and ISO 9001:2015 certification status
- Validate EOL alert lead times and sourcing practices
