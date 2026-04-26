---
fact_id: "methods-pcba-fai-fqi-and-traceability-gates"
title: "Internal PCBA pages treat FAI, final inspection, and traceability as distinct quality gates"
topic: "PCBA FAI, FQI, and traceability gates"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcba-incoming-quality-control-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "frontendapt-pcba-final-quality-inspection-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-components-bom-page-en"
  - "frontendapt-pcba-quality-system-page-en"
tags: ["internal", "pcba", "fai", "final-inspection", "traceability", "iqc", "quality"]
---

# Canonical Summary

> The internal PCBA pages separate incoming quality control, first-article inspection, final inspection, BOM context, and broader testing into distinct gates that support traceable release decisions.

## Stable Facts

- The incoming-quality page frames incoming materials checks as a gate before assembly.
- The first-article page frames the first build as a setup and launch confirmation step.
- The final-quality-inspection page frames end-of-line inspection as a release gate before shipment.
- The testing-quality page frames inspection and test as part of a layered quality system rather than one isolated step.
- The components-BOM page ties the build input list back to sourcing and traceability context.
- The quality-system page places traceability, IQC, inspection, and final acceptance inside one broader quality flow.

## Conditions And Methods

- Use this card when describing how release confidence accumulates across multiple checkpoints.
- Keep the quality language internal and program-specific unless a live quality plan supports broader claims.
- Refresh any sampling, defect-rate, or acceptance-window number before publication.

## Limits And Non-Claims

- This card does not claim every program uses the same acceptance criteria.
- It does not claim incoming QC, FAI, and final inspection alone guarantee zero defects.
- It does not replace customer-specific quality agreements or acceptance testing.

## Open Questions

- Add a later topic page for `pcba-release-gates-and-traceability`.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/incoming-quality-control.json
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/final-quality-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/testing-quality.json
- /code/hileap/frontendAPT/public/static/pcba/en/components-bom.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json

