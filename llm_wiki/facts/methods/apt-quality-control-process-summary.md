# Fact Card: APT Quality Control Process Summary

## Fact Metadata

- **fact_id**: apt_quality_control_process_summary
- **fact_type**: quality_capabilities
- **source_id**: apt_quality_control_processes
- **authority_tier**: Tier-2
- **domain**: quality_management
- **application**: pcba_quality_assurance
- **date_extracted**: 2026-05-02
- **verification_status**: verified

## Quality Control Layers

### Layer 1: Incoming Quality Control (IQC)

| Check Point | Verification |
|-------------|--------------|
| **Component Authenticity** | Source verification, counterfeit detection |
| **Packaging Integrity** | ESD, moisture barrier, physical condition |
| **Label Verification** | Part number, date code, lot code |
| **Quantity Confirmation** | Count verification |
| **Visual Inspection** | Damage, marking, lead condition |
| **Sample Testing** | Electrical/dimensional as needed |
| **Documentation** | C of C, test reports, certificates |

### Layer 2: First Article Inspection (FAI)

| Inspection Item | Details |
|-----------------|---------|
| **BOM Verification** | Correct components, values, ratings |
| **Placement Accuracy** | Position, orientation, alignment |
| **Solder Joint Quality** | Per IPC-A-610 criteria |
| **Dimensional Checks** | Board dimensions, component heights |
| **Electrical Verification** | Continuity, shorts, basic function |
| **Documentation Review** | Drawing compliance, marking |
| **Process Validation** | Profile, parameter verification |

### Layer 3: In-Process Quality Control

| Stage | Control Method |
|-------|----------------|
| **Solder Paste** | SPI - volume, height, alignment |
| **Placement** | AOI - component presence, position |
| **Reflow** | Profile monitoring, AOI post-reflow |
| **THT** | Visual inspection, selective solder profile |
| **Testing** | ICT, FCT, flying probe |

### Layer 4: Final Quality Inspection (FQI)

| Inspection Type | Criteria |
|-----------------|----------|
| **Visual** | IPC-A-610 Class 2/3 |
| **Dimensional** | Drawing tolerances |
| **Functional** | Sampling per plan |
| **Packaging** | Labeling, protection, documentation |
| **Cosmetic** | Customer-specific requirements |

## Quality Management System

### Certifications & Standards
| Standard | Scope |
|----------|-------|
| **ISO 9001:2015** | Quality management system |
| **IPC-A-610** | Acceptability of PCBAs (Class 2/3) |
| **IPC-7711/7721** | Rework, modification, repair |
| **IPC-J-STD-001** | Soldering requirements |
| **RoHS/REACH** | Environmental compliance |

### Quality Processes
| Process | Function |
|---------|----------|
| **Document Control** | Revision management, access control |
| **Traceability** | Lot tracking, component pedigree |
| **Corrective Action** | 8D problem solving, CAPA |
| **Continuous Improvement** | Kaizen, yield improvement |
| **Supplier Management** | AVL, supplier scorecards |
| **Customer Feedback** | Complaint handling, satisfaction |

### Metrics & KPIs
| Metric | Definition | Target |
|--------|------------|--------|
| **First-Pass Yield (FPY)** | Units passing all tests first time | >95% |
| **Defects Per Million (DPM)** | Defect rate in ppm | <100 |
| **Supplier PPM** | Incoming defect rate | <50 |
| **On-Time Delivery (OTD)** | Shipments on schedule | >98% |
| **Customer Complaints** | Issues per million units | <10 |
| **Internal Audit Score** | QMS compliance | >95% |

## Inspection Methods Matrix

| Method | Stage | Defects Detected | Speed | Cost |
|--------|-------|------------------|-------|------|
| **SPI** | Pre-placement | Print defects | Fast | Low |
| **AOI** | Post-placement, post-reflow | Placement, solder | Fast | Medium |
| **X-Ray** | Post-reflow | Hidden joints | Medium | High |
| **ICT** | Final | Electrical, values | Fast* | High* |
| **FCT** | Final | Functional | Slow | High |
| **Flying Probe** | Final | Electrical (no fixture) | Slow | Low |

*With existing fixture

## Quality Documentation

### Internal Records
| Record Type | Retention | Purpose |
|-------------|-----------|---------|
| **Inspection Reports** | 3+ years | Quality evidence |
| **Test Data** | Product life + 3 years | Traceability |
| **Process Parameters** | 1+ years | SPC, troubleshooting |
| **Non-Conformance** | 5+ years | CAPA analysis |
| **Calibration** | Per procedure | Equipment accuracy |

### Customer Deliverables
| Document | Content |
|----------|---------|
| **FAI Report** | Initial production verification |
| **Test Report** | ICT/FCT results |
| **C of C** | Certificate of Conformance |
| **Traceability Report** | Component lots, serial numbers |
| **Process Traveler** | Production history |

## Defect Classification (IPC-A-610)

| Class | Application | Acceptability |
|-------|-------------|---------------|
| **Class 1** | General electronics | Basic function |
| **Class 2** | Dedicated service | Performance + life |
| **Class 3** | High performance | Continuous reliability |

APTPCB is capable of all three classes, with Class 2 as standard and Class 3 available on request.

## Risk Management

| Risk Area | Mitigation Strategy |
|-----------|---------------------|
| **Component Quality** | IQC, AVL, supplier audits |
| **Process Variation** | SPC, DOE, control plans |
| **ESD Damage** | Protected areas, grounding, monitoring |
| **Moisture Sensitivity** | MSD handling, baking protocols |
| **Test Escapes** | Layered inspection, sampling plans |

---

## Source Reference

> "来自 APTPCB 已审核静态页面, 发布于 aptpcb.com"
> - Source: apt_quality_control_processes
> - URLs: file:///code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json, file:///code/hileap/frontendAPT/public/static/pcba/en/incoming-quality-control.json, file:///code/hileap/frontendAPT/public/static/pcba/en/final-quality-inspection.json, file:///code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
> - Authority: Tier-2 (internal_published_page)

## Usage Notes

Multi-layer quality control system ensuring product conformance from incoming materials through final shipment. Critical for:
- Reliability assurance
- Customer satisfaction
- Regulatory compliance
- Continuous improvement
