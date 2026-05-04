---
fact_id: "standards-smart-meter-standards-and-metrology-identity-boundary"
title: "IEC 62052/62053, MID, ANSI C12, and AMI sources support smart-meter standards and metrology identity, not compliance or field-life proof"
topic: "Smart-meter standards and metrology identity boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-01"
source_ids:
  - "iec-62052-11-2020-product-page"
  - "iec-62052-31-2015-product-page"
  - "iec-62053-21-2020-product-page"
  - "iec-62053-22-2020-product-page"
  - "iec-62053-23-2020-product-page"
  - "eurlex-2014-32-eu-measuring-instruments-directive-page"
  - "ansi-blog-c12-1-2026-code-for-electricity-metering"
  - "ansi-blog-c12-20-2015-accuracy-classes-page"
  - "nist-nistir-7823-ami-release-announcement"
tags: ["smart-meter", "iec-62052-11", "iec-62052-31", "iec-62053-21", "iec-62053-22", "iec-62053-23", "mid", "mi-003", "ansi-c12-20", "ami", "metrology"]
---

# Canonical Summary

> Current IEC, EUR-Lex, ANSI, and NIST public pages support one narrow smart-meter standards and metrology identity lane only. `IEC 62052-11:2020` may be used as the named general meter-requirements and type-testing document family, while `IEC 62052-31:2015` is the named product-safety document family publicly referenced by the IEC meter pages. `IEC 62053-21:2020`, `IEC 62053-22:2020`, and `IEC 62053-23:2020` may be used as named particular-requirements document families for active-energy and reactive-energy meter classes, with type-test-only posture. `MID` may be used as the EU `Directive 2014/32/EU` legal-metrology framework that includes `MI-003` active electrical energy meters. `ANSI C12.20` may be used only as a historical/public U.S. accuracy-class document noun, because current ANSI public pages say its content was merged into `ANSI C12.1`. `AMI` may be used as an institutional system-context term from NIST. None of these sources prove that a PCB, meter, supplier, or factory is compliant, certified, utility-approved, long-life qualified, or revenue-grade accurate.

## Stable Facts

- IEC publicly identifies `IEC 62052-11:2020` as `Electricity metering equipment - General requirements, tests and test conditions - Part 11: Metering equipment`.
- The IEC `IEC 62052-11:2020` product page states that the document specifies requirements, tests, and test conditions for type testing of AC and DC electricity meters and explicitly says that tampering is not covered.
- The same IEC page publicly states that meter safety requirements were removed and are covered in `IEC 62052-31:2015`.
- IEC publicly identifies `IEC 62052-31:2015` as the `Part 31` product-safety requirements and tests document for electricity metering equipment.
- IEC publicly identifies `IEC 62053-21:2020` as the particular-requirements document for static meters for AC active energy, classes `0,5`, `1`, and `2`, and states that it applies to type tests only.
- IEC publicly identifies `IEC 62053-22:2020` as the particular-requirements document for transformer-operated static meters for AC active energy, classes `0,1S`, `0,2S`, and `0,5S`, and states that it applies to type tests only.
- IEC publicly identifies `IEC 62053-23:2020` as the particular-requirements document for static meters for reactive energy, classes `2` and `3`, and states that it applies to type tests only.
- The EUR-Lex page for `Directive 2014/32/EU` publicly states that the directive applies to instrument-specific annexes including `active electrical energy meters (MI-003)`, and that the MI-003 annex applies to active electrical energy meters intended for residential, commercial, and light industrial use.
- ANSI's 2026 public article states that the 2022 revision merged the content of `ANSI C12.20` into `ANSI C12.1`, making `ANSI C12.1` the singular document for the code for electricity metering and withdrawing `ANSI C12.20`.
- ANSI's public article for historical `ANSI C12.20-2015` identifies that document as the electricity-meter standard for `0.1`, `0.2`, and `0.5` accuracy classes and marks it as revised by current `ANSI C12.1`.
- NIST publicly uses `Advanced Metering Infrastructures (AMIs)` and `Smart Meters` as real system-context nouns in the `NISTIR 7823` release announcement.

## Conditions And Methods

- Use this card for `/code/blogs/tmps/2026.4.29/en/smart-meter-pcb.md` only when the rewrite needs exact document-family or system-context nouns such as `IEC 62052-11`, `IEC 62052-31`, `IEC 62053-21`, `IEC 62053-22`, `IEC 62053-23`, `MID`, `MI-003`, historical `ANSI C12.20`, or `AMI`.
- Safe `IEC` posture:
  treat `IEC 62052-11` as the general metering-equipment and type-testing document family, `IEC 62052-31` as the product-safety document family, and `IEC 62053-21/22/23` as the particular-requirements accuracy-class document family.
- Safe `MID` posture:
  treat `Directive 2014/32/EU` as the EU legal-metrology directive family and `MI-003` as the active-electrical-energy-meter annex identity.
- Safe `ANSI C12.20` posture:
  treat it as a historical/public U.S. accuracy-class document noun that now routes through current `ANSI C12.1` public framing rather than as a current standalone compliance anchor.
- Safe `AMI` posture:
  treat `AMI` as institutional system-context language for smart-meter infrastructure, not as proof of interoperability or protocol support.
- Pair this card with `wiki/processes/power-energy-pcb-pcba-review-boundaries.md` when the rewrite also discusses board partitioning, thermal route choice, test access, or production workflow.
- Recover a separate source lane before keeping exact communication-protocol nouns such as `DLMS/COSEM`, `IEC 62056`, `PRIME`, `G3-PLC`, `Wi-SUN`, `NB-IoT`, or `LTE-M`.

## Limits And Non-Claims

- This card does not authorize `complies with IEC 62052/62053`, `MID-certified`, `ANSI C12.20 compliant`, `utility-approved`, or equivalent conformity claims.
- It does not authorize exact creepage, clearance, hi-pot, surge, impulse, EMC, environmental, or anti-tamper thresholds.
- It does not authorize exact `Class 0.5S`, revenue-metering, no-recalibration, harmonic, or long-term metrology-performance claims for a specific design.
- It does not authorize `20-year field life`, `15-20 year service`, anti-tamper effectiveness, or field-reliability proof.
- It does not authorize communication-stack behavior or interoperability claims for `DLMS`, `PLC`, `PRIME`, `G3-PLC`, `Wi-SUN`, `Zigbee`, `NB-IoT`, `LTE-M`, or head-end integration.
- It does not authorize HILPCB documentation-package support, certification-support, pilot-volume, traceability, or regional-readiness claims.

## Open Questions

- Recover a separate communication-protocol identity lane only if future rewrites must retain exact `DLMS/COSEM`, `IEC 62056`, `PRIME`, `G3-PLC`, `NB-IoT`, `Wi-SUN`, `Zigbee`, or related utility-network nouns.
- Add narrower ANSI or NEMA public metadata only if future drafts require `ANSI C12.10`, `ANSI C12.30`, detachable-meter physical aspects, or service-switch test language.

## Source Links

- https://webstore.iec.ch/en/publication/28212
- https://webstore.iec.ch/en/publication/23312
- https://webstore.iec.ch/en/publication/28660
- https://webstore.iec.ch/en/publication/29987
- https://webstore.iec.ch/en/publication/29239
- https://eur-lex.europa.eu/eli/dir/2014/32/oj
- https://blog.ansi.org/ansi/ansi-c12-1-2024-code-electricity-metering/
- https://blog.ansi.org/ansi-c12-20-2015-electric-meters-accuracy-classes/
- https://csrc.nist.gov/news/2015/nist-announces-the-release-of-nistir-7823
