---
fact_id: "standards-aviation-altimeter-standards-metadata-boundary"
title: "DO-160G, DO-254, and DO-155 support aviation standards metadata only, not PCB qualification proof"
topic: "aviation altimeter standards metadata boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-01"
source_ids:
  - "faa-ac-21-16g-do160-acceptability-page"
  - "faa-ac-20-152a-page"
  - "rtca-do-160g-product-page"
  - "rtca-do-254-product-page"
  - "rtca-do-155-product-page"
tags: ["do-160g", "do-254", "do-155", "faa", "rtca", "altimeter", "qualification-boundary", "avionics"]
---

# Canonical Summary

> Current FAA and RTCA public pages support one narrow aviation standards-metadata lane only. `DO-160G` may be used as the named RTCA environmental-conditions and test-procedures document family for airborne equipment, with FAA `AC 21-16G` stating that versions `D` through `G` contain acceptable environmental qualifications for certain airworthiness requirements and strongly encouraging `DO-160G` for new articles. `DO-254` may be used as the named RTCA airborne electronic hardware design-assurance document, with public RTCA metadata and FAA `AC 20-152A` supporting circuit-board-assembly context only. `DO-155` may be used only as the named RTCA minimum-performance-standard document for airborne low-range radar altimeters. These sources do not prove that a PCB, PCBA, supplier, or program is qualified, compliant, or approved.

## Stable Facts

- FAA `AC 21-16G` publicly identifies RTCA `DO-160` versions `D`, `E`, `F`, and `G` as containing acceptable environmental qualifications for showing compliance with certain airworthiness requirements and strongly encourages `DO-160G` for new articles.
- RTCA publicly identifies `DO-160G` as `Environmental Conditions and Test Procedures for Airborne Equipment`.
- RTCA publicly identifies `DO-254` as `Design Assurance Guidance for Airborne Electronic Hardware`.
- RTCA public metadata for `DO-254` explicitly includes hardware scope language that covers `circuit board assemblies`.
- Existing FAA `AC 20-152A` public guidance already supports airborne electronic hardware and circuit-board-assembly design-assurance context, not installation or supplier approval.
- RTCA publicly identifies `DO-155` as `Minimum Performance Standards-Airborne Low Range Radar Altimeters`, which narrows it to low-range radar-altimeter equipment rather than `altimeters` in general.

## Conditions And Methods

- Use this card when `altimeter` drafts mention `DO-160`, `DO-254`, or `DO-155`.
- Safe posture: treat these documents as standards-family, regulator-recognition, and scope-boundary vocabulary only.
- Keep `DO-160G`, `DO-254`, and `DO-155` separate:
  - `DO-160G` for airborne-equipment environmental-qualification document-family context
  - `DO-254` for airborne electronic hardware design-assurance context
  - `DO-155` for low-range radar-altimeter minimum-performance-standard context
- Pair this card with the existing barometric-sensor, radio-altimeter, first-article, and regulated-application boundary cards when the draft also discusses subsystem architecture or review workflow.

## Limits And Non-Claims

- This card does not authorize `with DO-160 qualification`, `must comply with DO-160G Section 21`, `DO-254 requires our PCB fabricator controls`, or similar direct qualification claims.
- It does not authorize exact section coverage, exact temperature, altitude, vibration, EMI, DAL, or verification numerics.
- It does not authorize `TSO`, airworthiness, installation approval, supplier approval, or program-acceptance claims.
- It does not authorize using `DO-155` as if it governs barometric or laser altimeters.
- It does not authorize HILPCB customer, deployment, certification, or program-history claims.

## Source Links

- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1019280
- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1041323
- https://my.rtca.org/productdetails?id=a1B36000001IcnSEAS
- https://my.rtca.org/productdetails?id=a1B36000001IcjTEAS
- https://my.rtca.org/productdetails?id=a1B36000001IcnqEAC
