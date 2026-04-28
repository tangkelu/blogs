---
fact_id: "methods-hidden-joint-xray-inspection-boundary"
title: "Hidden-joint X-ray language should stay as coverage boundary and defect-visibility context, not universal acceptance proof"
topic: "Hidden-joint X-ray inspection boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcba-xray-inspection-page-en"
  - "frontendapt-pcba-x-ray-inspection-page-en"
  - "frontendapt-pcba-bga-qfn-fine-pitch-page-en"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "nasa-pcb-inspection-and-quality-control-2022-page"
  - "ipc-a-610h-toc"
  - "ipc-j-std-001j-toc"
tags: ["hidden-joint", "x-ray", "axi", "ct", "bga", "qfn", "inspection", "boundary"]
---

# Canonical Summary

> Current internal X-ray pages and public metadata support guarded wording that `X-ray` or `AXI` is the inspection layer for hidden solder joints and internal solder-related defect visibility in BGA, QFN, CSP, and similar dense-package contexts. They do not support universal defect acceptability thresholds, mandatory inspection coverage rules, or claims that X-ray alone closes all assembly risk.

## Stable Facts

- The internal X-ray pages explicitly frame X-ray and CT analysis around hidden solder joints and internal defect visibility.
- The same internal pages place BGA, QFN, CSP, voiding, bridges, cold joints, and concealed solder features inside X-ray's coverage domain.
- The internal fine-pitch page supports the idea that dense packages create hidden-joint inspection concerns that ordinary visual access cannot fully resolve.
- Internal AOI and quality-system pages support a layered inspection model where AOI, X-ray, and electrical tests cover different defect classes.
- NASA's public inspection-and-quality-control record supports non-destructive-analysis and failure-analysis workflow vocabulary without supplying workmanship thresholds.
- IPC public TOC metadata supports naming `IPC-A-610` and `J-STD-001` as standards anchors, but not clause-level hidden-joint acceptance claims.

## Conditions And Methods

- Use this card when the supported slugs need to explain why hidden-joint assemblies often add X-ray or AXI language to the inspection plan.
- Prefer wording such as `used to inspect concealed joints`, `supports hidden-joint defect visibility`, and `belongs to a layered quality flow`.
- Keep X-ray or CT capability separate from AOI, SPI, ICT, FCT, and visual-inspection claims.
- Refresh any acceptance rule, defect threshold, sample plan, or coverage percentage before publication.

## Limits And Non-Claims

- This card does not provide universal void acceptance thresholds, bridge acceptance thresholds, or hidden-joint grading rules.
- It does not claim every BGA or QFN program requires 100 percent X-ray coverage or CT analysis.
- It does not claim X-ray replaces workmanship review, electrical test, functional test, or process validation.
- It does not reproduce IPC clause text or authorize class-specific accept/reject statements.

## Open Questions

- Add licensed IPC or customer-spec evidence later if one of the supported slugs needs class-specific hidden-joint acceptance language.
- Add a dedicated `AXI versus CT versus 2D X-ray` boundary card only if future drafts start blending those methods.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/x-ray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/bga-qfn-fine-pitch.json
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- https://ntrs.nasa.gov/citations/20220012424
- https://www.ipc.org/TOC/IPC-A-610H-toc.pdf
- https://www.ipc.org/TOC/IPC-J-STD-001J_TOC.pdf
