---
fact_id: "methods-spi-aoi-ict-boundaries"
title: "SPI, AOI, and ICT cover different defect classes and should not be treated as interchangeable"
topic: "SPI AOI ICT"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids: ["koh-young-spi-technology", "koh-young-aoi-technology", "keysight-ict-systems"]
tags: ["spi", "aoi", "ict", "inspection", "pcba-testing"]
---

# Canonical Summary

> SPI, AOI, and ICT belong to different stages of the PCBA quality stack: SPI is about solder-paste deposit measurement before reflow, AOI is about optical inspection of assembled geometry and solder features, and ICT is about electrical fault coverage on the assembled board.

## Stable Facts

- Koh Young frames solder paste printing as a three-dimensional process where paste volume measurement is critical for process control.
- The same SPI source emphasizes that visibility and shadow issues matter when measuring irregular deposits.
- Koh Young frames modern AOI as an inspection method for components, solder joints, patterns, and foreign material on assembled PCBs.
- The AOI source also highlights that geometry shadowing and package complexity can limit simpler optical approaches.
- Keysight positions ICT as a production-line electrical method with high fault coverage for manufacturing defects such as opens, shorts, soldering faults, and component issues.
- Keysight explicitly places ICT in medium- to high-volume PCBA manufacturing with mixed analog and digital content.

## Conditions And Methods

- Treat SPI as upstream print-process measurement.
- Treat AOI as optical / geometric post-placement or post-reflow inspection depending on flow.
- Treat ICT as an electrical verification method that complements, rather than replaces, optical inspection.

## Limits And Non-Claims

- This card does not claim one method can replace the full inspection stack.
- The specific defect coverage of any line depends on fixture access, board design, component mix, and program quality.

## Open Questions

- Add flying probe, X-ray, and FCT cards next so the full test stack is represented

## Source Links

- https://kohyoung.com/en/solder-paste-inspection-technology/
- https://kohyoung.com/en/automated-optical-inspection-technology/
- https://www.keysight.com/us/en/products/in-circuit-test-for-manufacturing/in-circuit-test-systems.html
