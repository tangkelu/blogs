---
fact_id: "methods-pcba-inspection-process-governance-boundary"
title: "PCBA inspection process governance should separate SPI, AOI, X-ray, ICT, and FCT into distinct gates with clear sequencing and defect-class ownership"
topic: "PCBA inspection process governance boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "frontendapt-pcba-spi-inspection-page-en"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-quality-system-page-en"
tags: ["pcba", "inspection", "governance", "spi", "aoi", "x-ray", "ict", "fct", "process-control", "defect-detection", "layered-quality"]
---

# Canonical Summary

> PCBA inspection governance is strongest when SPI, AOI, X-ray, ICT, and FCT are treated as separate gates with distinct defect-class ownership, clear sequencing, and traceable evidence accumulation. SPI owns solder-paste print quality before placement; AOI owns component placement and visible solder joint geometry; X-ray owns hidden joints and internal defects; ICT owns electrical fault coverage; FCT owns powered functional behavior validation.

## Stable Facts

### Inspection Gate Sequence

| Gate | Stage | Defect Class Ownership | Method |
|------|-------|----------------------|--------|
| **SPI** | After printing, before placement | Solder paste volume, height, area, offset, bridging, missing paste, trend monitoring | 2D/3D optical measurement |
| **Pre-reflow AOI** | After placement, before reflow | Component presence, orientation, polarity, type, position | 2D/3D optical |
| **Post-reflow AOI** | After reflow | Solder joint geometry, wetting, fillet, bridging, tombstone, component shift | 2D/3D optical |
| **X-ray/AXI** | After reflow (hidden joints) | BGA/QFN/CSP voids, bridges, cold joints, head-in-pillow, internal layer defects | 2D/2.5D/3D CT |
| **ICT** | After assembly | Opens, shorts, component value/tolerance, missing/wrong components, boundary-scan faults | Bed-of-nails electrical |
| **FCT** | Final validation | Powered behavior, communication interfaces, firmware, signal integrity under load | Functional test fixture |

### Quality System Integration

- APTPCB quality system frames PCBA validation as a multi-layered flow: DFM/DFT → IQC → SPI → AOI → Reflow/Wave → X-ray → ICT → FCT → Burn-in → Final Inspection → Cleaning
- Each gate contributes to a cumulative evidence stack rather than a single pass/fail event
- Traceability is maintained through barcode + lot tracking across all gates
- Defect tracking uses PPM monitoring with process feedback loops

### Defect Class Boundaries

**SPI Defects** (Paste-level, pre-component):
- Insufficient/excess paste volume
- Misalignment/offset
- Bridging between pads
- Missing paste deposits
- Area/height deviations

**AOI Defects** (Component and joint geometry):
- Missing, wrong, or reversed components
- Polarity errors
- Tombstoning, billboarding
- Insufficient solder, bridging, solder balls
- Component shift/rotation

**X-ray Defects** (Hidden/internal):
- BGA/CSP voids, insufficient solder
- Hidden bridges under components
- Head-in-pillow defects
- Cold joints in hidden areas
- Internal layer defects (for bare PCB X-ray)

**ICT Defects** (Electrical):
- Open circuits, short circuits
- Wrong component values
- Missing components
- Diode/transistor orientation
- Boundary-scan chain integrity

**FCT Defects** (Functional):
- Power-on failures
- Communication protocol errors
- Firmware load failures
- Signal integrity issues under load
- Interface timing violations

## Conditions And Methods

- Use this card when framing PCBA quality as a gated process rather than a single inspection event
- Pair with IPC-A-610 metadata for workmanship class context (Class 2/3)
- Treat each gate as optional/customizable per project requirements, not universal mandatory
- Maintain clear defect-class ownership boundaries to avoid gate overlap confusion

## Limits And Non-Claims

- This card does not specify acceptance thresholds, coverage percentages, or sampling plans
- It does not claim that every project receives every gate (customizable per project)
- It does not provide turnaround times or throughput rates as universal commitments
- It does not prove supplier qualification or certification status
- It does not replace IPC, JEDEC, or customer-specific workmanship standards

## Open Questions

- Clarify which gates are standard vs optional for different project types (NPI vs mass production)
- Document burn-in stress-test parameters when available
- Add flying probe testing boundary for low-volume/early-stage projects

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/spi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json

