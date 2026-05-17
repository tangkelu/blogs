---
fact_id: "methods-pcba-ict-fixture-strain-and-mlcc-latent-damage-boundary"
title: "Official vendor guidance supports a guarded ICT fixture-strain warning: probe load and board flex can crack small MLCCs or open solder joints, creating latent post-test failure risk"
topic: "PCBA ICT fixture strain and MLCC latent damage boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-14"
source_ids:
  - "murata-mlcc-test-probe-board-flex-precaution-faq"
  - "murata-small-mlcc-board-bending-caution-pdf"
  - "tdk-mlcc-flex-crack-cause-and-consequence-faq"
  - "keysight-in-circuit-test-systems-page"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
tags: ["pcba", "ict", "fixture", "probe-force", "board-flex", "mlcc", "0201", "latent-damage", "dft", "dfm"]
---

# Canonical Summary

> Current official vendor guidance is strong enough to support one guarded dense-PCBA testability warning: ICT probe load is not only an electrical-access issue. Test-probe force can flex the PCB, very small MLCCs become more crack-sensitive as package size shrinks, and flex-cracked MLCCs can later show up as open or short defects. This supports physical-failure wording around fixture strain and access planning, but not universal force, spacing, or keepout numbers.

## Stable Facts

- Murata states that the thrusting force of a test probe can flex the PCB and result in cracked chips or open solder joints.
- Murata recommends backside support pins close to the probe point to prevent warping or flexing during inspection.
- Murata's small-MLCC caution states that crack risk rises as package size shrinks into very small classes such as `0402` and `0201`, especially when the surrounding geometry is not reconsidered with the smaller part.
- TDK states that severe board bending or flexure during manufacturing or assembly can cause MLCC flex cracks.
- TDK states that a flex-cracked MLCC can later present as an open or short defect depending on crack progression and resistance degradation.
- The existing ICT fixture-introduction fact already supports the broader framing that assembly safety belongs inside the front-end ICT readiness decision.
- The existing APT X-ray source already supports guarded vocabulary around micro-cracks and hidden defects that may escape simple surface review.

## Conditions And Methods

- Use this card when a draft about ICT, bed-of-nails access, test points, dense PCBA DFT, or fixture readiness needs one real physical failure chain instead of only review-posture language.
- The safe public pattern is: `dense access pressure -> probe load or poor support -> local board flex -> small-MLCC crack or open solder joint -> latent field short/open risk`.
- Pair this card with `pcba-ict-fixture-introduction-gate` when the article must explain why test-point planning is also a mechanical-support and release-risk decision.
- Pair this card with hidden-joint or X-ray cards when the same article also discusses BGA-edge density or latent solder-joint risk, but keep BGA statements qualitative unless separate owner-backed sources are added.

## Limits And Non-Claims

- This card does not authorize exact probe-force limits, support-pin spacing, support-pin count, test-point keepout values, or fixture design rules.
- It does not authorize universal claims that every dense board near an MLCC will fail under ICT.
- It does not authorize exact BGA-edge clearance or solder-joint life predictions.
- It does not replace project-specific fixture review, board-support design, or package-owner mechanical guidance.

## Open Questions

- A later source-recovery lane can add stronger owner-backed BGA or hidden-joint strain sources if future prompts need more than qualitative BGA-edge caution.

## Source Links

- https://www.murata.com/support/faqs/capacitor/ceramiccapacitor/mnt/0016
- https://www.murata.com/-/media/webrenewal/products/capacitor/ceramiccapacitor/faq/mnt/small-mlcc-caution-ver3.ashx?la=en
- https://product.tdk.com/en/contact/faq/capacitors-0086.html
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/x-ray-inspection.json
