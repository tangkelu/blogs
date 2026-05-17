---
title: "ICT fixture introduction and method selection"
status: "active"
last_updated: "2026-05-10"
fact_ids:
  - "pcba-ict-boundary-and-flying-probe-method-identity"
  - "pcba-ict-fixture-introduction-gate"
  - "methods-pcba-flying-probe-vs-ict-selection-posture"
  - "methods-pcba-ict-fixture-strain-and-mlcc-latent-damage-boundary"
source_ids:
  - "keysight-in-circuit-test-systems-page"
  - "seica-flying-probe-page"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "murata-mlcc-test-probe-board-flex-precaution-faq"
  - "murata-small-mlcc-board-bending-caution-pdf"
  - "tdk-mlcc-flex-crack-cause-and-consequence-faq"
---

# ICT Fixture Introduction And Method Selection

## Safe Summary

ICT fixture introduction is a readiness decision that sits at the intersection of DFM, DFT, assembly support, and test-method selection. Treat it as part of the release path, not as a standalone tooling purchase.

On dense boards, fixture introduction is also a mechanical-strain decision. Official Murata and TDK guidance now supports guarded wording that probe load and board flex can crack very small MLCCs or open solder joints, so access planning should be reviewed together with backside support and strain relief rather than as electrical reachability alone.

## Use When

- A draft needs to explain why fixture introduction begins before the fixture is built.
- A draft needs to distinguish ICT from flying probe without overclaiming economics or coverage.
- A draft needs one real physical failure pattern for dense ICT access instead of only review-posture language.

## Do Not Use For

- Coverage percentages
- Fixture payback
- Universal cycle-time claims
- Locator-hole count or diameter guidance
- Universal probe-force, support-pin, or test-point-keepout numbers
- Supplier capability or acceptance claims
