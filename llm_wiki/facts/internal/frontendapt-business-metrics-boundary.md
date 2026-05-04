---
fact_id: "internal-frontendapt-business-metrics-boundary"
title: "APTPCB company profile includes 2002 founding, 20,000㎡ PCB + 4,500㎡ PCBA facilities, 100,000㎡/mo capacity, ISO 9001/13485/IATF 16949 certifications, with 24h DFM and 72h turnkey service commitments"
topic: "APTPCB company profile, facilities, and service commitments"
category: "internal"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "frontendapt-about-index-en"
  - "frontendapt-quote-index-en"
tags: ["aptpcb", "company-profile", "factory", "capacity", "certifications", "iso-9001", "iso-13485", "iatf-16949", "service-commitments", "dfm", "turnaround"]
---

# Canonical Summary

> APTPCB (Guangdong APTPCB Electronic Technology Co., Ltd.) operates as a national high-tech enterprise founded in 2002, with 20,000㎡ PCB fabrication facility and 4,500㎡ PCBA assembly facility. Key metrics include 100,000㎡/month PCB capacity, 80 engineers, 5 SMT lines, and certifications covering ISO 9001:2015, ISO 13485, IATF 16949, UL, CCC. Service commitments include 24-hour DFM feedback and 72-hour fastest turnkey delivery.

## Stable Facts

### Company Foundation

- **Legal Name**: Guangdong APTPCB Electronic Technology Co., Ltd.
- **Founded**: 2002
- **Location**: Guangzhou Industrial Park
- **Classification**: National high-tech enterprise

### Facility Scale

| Facility | Area | Capacity/Scale | Key Equipment |
|----------|------|----------------|---------------|
| PCB Factory (Shenzhen) | 20,000㎡ | 100,000㎡/mo | LDI, Auto Plating, Laser Drilling, AOI, E-test |
| PCBA Factory | 4,500㎡ | 5 SMT lines + 3 DIP lines | SPI, High-Speed SMT (01005), Reflow, Wave, X-ray |
| Workforce | 800-1,000 workers + 80 engineers | - | DFM, NPI, production ramp support |

### Certification Inventory

- **ISO 9001:2015** - Quality management system
- **ISO 13485** - Medical devices quality management
- **IATF 16949** - Automotive quality management
- **UL** - Product safety certification
- **CCC** - China Compulsory Certification
- **CE** - European conformity
- **RoHS** - Restriction of hazardous substances

### History Milestones

| Year | Milestone |
|------|-----------|
| 2002 | Company founded, PCBA factory establishment, ISO9001/CCC/UL |
| 2005 | Branch company established, full PCB/PCBA/sourcing service |
| 2008 | First global electronics industry exhibition participation |
| 2011 | ERP deployment, IATF16949 certification, military qualification |
| 2014 | Equipment upgrade (Japan/Germany/Swiss imports) |
| 2019 | ISO 13485:2016 certification |
| 2023 | Factory relocation and 4,500㎡ expansion |

### Service Commitments

| Commitment | Value | Context |
|------------|-------|---------|
| DFM Feedback | 24h | Quote response with manufacturability review |
| Return Rate | <0.1% | Historical across 2,000+ orders |
| Fastest Turnkey | 72h | Expedited delivery option |

### Technology Capabilities

**PCB Fabrication:**
- Rigid, FPC (Flexible), Rigid-Flex
- HDI (High Density Interconnect)
- High Frequency, Metal-core, Aluminum
- Standards: IPC-600G Class II / IPC-6012B (Class III optional)
- Testing: 100% AOI, 100% electrical testing, reliability lab

**PCBA Assembly:**
- SMT: Panasonic DPM-D3/TT2/NPM-W2 (01005 capability)
- THT/DIP: Wave soldering with controlled parameters
- Inspection: SPI, AOI, X-ray (BGA support)
- Testing: FCT (Functional Circuit Test), FAI (First Article Inspection)

**Design & NPI:**
- Hardware design and schematic (SCH) support
- PCB layout with manufacturability checkpoints
- 3D assembly support for fit checks
- Cross-team NPI kickoff and readiness planning

### Quality Control Stages

1. **DFM Checking** - PCB, BOM, schematic validation, manufacturability risk flags
2. **NPI Conference** - Sales, engineering, production, purchasing, quality alignment
3. **Component Sourcing** - Brand/part number adherence, original/first-level agents
4. **IQC (Incoming Inspection)** - PCB verification, component fit test, spot-check values
5. **PCB Fabrication** - High-quality materials, 100% AOI, 100% E-test, semi-inspection, reliability tests
6. **SMT + Inspection** - SPI, 16-zone reflow (4-hour curve records), AOI, X-ray for BGA
7. **Final Quality** - FCT, COC/COA documentation, logistics coordination

### Systems & Traceability

- **ERP** - Order, material, process control
- **MES** - Manufacturing execution with barcode tracking
- **Inventory Controls** - Barcode-based traceability
- **Cloudflare R2** - Secure file handling and backups

## Conditions And Methods

- Use this fact card for company profile framing, facility scale context, and certification inventory
- Reference history milestones for establishing experience depth (20+ years)
- Use service commitments (24h, 72h) as stated service levels, not guaranteed SLAs
- Pair with dated internal records before making current capacity or performance claims

## Limits And Non-Claims

- This card does not prove current real-time capacity utilization or availability
- It does not establish current headcount accuracy (figures are point-in-time from JSON)
- It does not prove ISO certifications are currently valid or audited
- It does not guarantee 24h/72h service levels under all conditions or workloads
- It does not cover pricing, MOQ, or specific customer terms
- Historical return rate (<0.1%) does not predict future performance

## Open Questions

- Verify currency: Are facility sizes, capacity figures, and headcount current?
- Certification validity: Confirm ISO 9001:2015, ISO 13485, IATF 16949 are currently valid
- Equipment currentness: Verify SMT lines and specific equipment models are current
- Service level confirmation: Confirm 24h DFM and 72h turnkey are currently offered

## Source Links

- /code/hileap/frontendAPT/public/static/about/en/index.json
- /code/hileap/frontendAPT/public/static/quote/en/index.json
