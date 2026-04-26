---
fact_id: "methods-pcba-layered-inspection-stack"
title: "Internal PCBA pages support a layered inspection stack from SPI to AOI, X-ray, ICT, and FCT"
topic: "PCBA layered inspection stack"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcba-spi-inspection-page-en"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "frontendapt-pcba-x-ray-inspection-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-quality-system-page-en"
tags: ["internal", "pcba", "spi", "aoi", "x-ray", "ict", "fct", "quality"]
---

# Canonical Summary

> The internal PCBA pages describe quality control as a layered stack: SPI controls solder paste before placement, AOI checks visible placement and solder features, X-ray covers hidden joints, ICT verifies electrical connectivity and component-level faults, and FCT validates powered board behavior.

## Stable Facts

- The APT SPI page places solder paste inspection after paste printing and before component placement.
- The same SPI page frames paste volume, height, alignment, bridging risk, insufficient paste, missing paste, and trend monitoring as SPI concerns.
- The APT AOI page frames AOI as an inspection method for bare PCB and SMT assembly defects, including visible geometry, placement, solder, and polarity issues.
- The APT X-ray page frames X-ray as the inspection layer for hidden joints and internal defects, especially BGA, QFN, CSP, voids, bridges, and concealed solder features.
- The hyphenated APT X-ray page variant adds CT analysis and hidden-joint defect wording without changing the basic boundary that X-ray addresses concealed solder and internal-defect questions.
- The APT ICT page frames ICT as fixture-based electrical verification for components and interconnections on assembled boards.
- The APT FCT page frames functional test as powered board-level behavior validation under intended operating conditions.
- The APT PCBA quality-system page places DFM/DFT, IQC, SPI/AOI/AXI, ICT/FCT, burn-in, final visual inspection, cleaning, and traceability into one multi-layer PCBA quality flow.

## Conditions And Methods

- Use this card to explain PCBA test coverage as layered risk reduction, not as one generic "inspection" step.
- Treat each method as complementary unless a project-specific test plan says otherwise.
- Refresh any exact coverage, turnaround, defect-rate, IPC class, or process-window number before publication.

## Limits And Non-Claims

- This card does not claim every program receives SPI, AOI, X-ray, ICT, FCT, burn-in, and cleaning.
- It does not claim one inspection method replaces the others.
- It does not state external standards requirements or acceptance criteria.

## Open Questions

- Add official source support for IPC-A-610, J-STD-001, IPC-9252, and IPC-7095 metadata in a later standards batch.
- Add a topic wiki page for `pcba-validation-ladder`.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/spi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/x-ray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
