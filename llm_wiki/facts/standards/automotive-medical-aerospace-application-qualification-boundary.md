---
fact_id: "standards-automotive-medical-aerospace-application-qualification-boundary"
title: "Automotive, medical, and aerospace application standards are system / device / program boundaries, not PCB readiness proof"
topic: "Regulated application qualification boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-28"
source_ids:
  - "iso-26262-road-vehicles-functional-safety-package"
  - "iatf-16949-overview-page"
  - "aec-documents-page"
  - "fda-mri-benefits-and-risks-page"
  - "fda-qmsr-page"
  - "faa-ac-20-152a-page"
  - "as9102c-first-article-inspection-page"
tags: ["automotive", "iso-26262", "iatf-16949", "aec-q", "medical", "mri", "fda", "aerospace", "faa", "qualification-boundary"]
---

# Canonical Summary

> Automotive, medical, and aerospace drafts can use official standards and regulator sources for application-layer boundaries, but those sources do not prove PCB readiness. `ISO 26262` is road-vehicle E/E functional-safety context, `IATF 16949` is automotive QMS context, `AEC-Q` documents are component-qualification context, FDA MRI pages are device-labeling and risk context, FDA QMSR is medical-device manufacturer QMS context, and FAA AC 20-152A is airborne-electronic-hardware design-assurance context.

## Stable Facts

- ISO's official `ISO 26262` package page supports functional-safety vocabulary for road-vehicle electrical / electronic systems.
- IATF's official overview supports automotive quality-management-system vocabulary.
- AEC's official document hub supports AEC-Q document-family discovery at electronic-component qualification scope.
- FDA MRI guidance supports `MR Safe`, `MR Conditional`, and `MR Unsafe` labeling context and MRI hazard framing at device level.
- FDA QMSR pages support medical-device quality-system regulatory framing, not PCB-shop certification proof.
- FAA AC 20-152A supports airborne electronic hardware / circuit-board assembly design-assurance context, not airworthiness approval for a PCB supplier.
- SAE AS9102 supports aerospace first-article-inspection identity and documentation workflow context, not automatic process-capability proof.

## Conditions And Methods

- Use this card when drafts discuss ADAS, ECU, automotive Ethernet, MRI equipment, pacemakers, implantables, flight-control boards, avionics, drones, aerospace, or defense-sensitive applications.
- Keep system lifecycle, organization QMS, component qualification, product labeling, and airborne design-assurance evidence separate.
- Require program-specific evidence before saying a PCB, PCBA, supplier, material, or lot is qualified, approved, certified, MR Conditional, ASIL-ready, PPAP-approved, or flight certified.

## Limits And Non-Claims

- This card does not support `ISO 26262 compliant PCB manufacturing`, `AEC-Q PCB`, `MRI-compatible PCB`, `pacemaker-ready PCB`, `flight-certified PCB`, or `defense-ready supplier` claims.
- It does not prove supplier certification status, OASIS listing, FDA registration, IATF certificate status, ASIL allocation, PPAP completion, EMC compliance, biocompatibility, airworthiness approval, or export-control compliance.
- It does not provide exact process windows, inspection limits, reliability metrics, lead times, yields, quality rates, or commercial readiness.

## Source Links

- https://www.iso.org/publication/PUB200262.html
- https://www.iatfglobaloversight.org/iatf-16949/
- https://www.aecouncil.com/AECDocuments.html
- https://www.fda.gov/radiation-emitting-products/mri-magnetic-resonance-imaging/benefits-and-risks
- https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-system-qs-regulationmedical-device-current-good-manufacturing-practices-cgmp
- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1041323
- https://saemobilus.sae.org/standards/as9102c-aerospace-series-first-article-inspection-requirements
