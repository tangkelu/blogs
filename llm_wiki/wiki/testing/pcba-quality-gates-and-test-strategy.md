---
topic_id: "testing-pcba-quality-gates-and-test-strategy"
title: "PCBA Quality Gates And Test Strategy"
category: "testing"
status: "draft"
last_reviewed_at: "2026-04-24"
fact_ids:
  - "methods-pcba-layered-inspection-stack"
  - "methods-pcba-ict-vs-fct-boundary"
  - "methods-pcba-fai-fqi-and-traceability-gates"
  - "methods-pcba-flying-probe-test-positioning"
  - "methods-pcba-bom-sourcing-and-traceability-posture"
  - "methods-spi-aoi-ict-boundaries"
source_ids:
  - "frontendapt-pcba-spi-inspection-page-en"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "frontendapt-pcba-bga-reballing-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-incoming-quality-control-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "frontendapt-pcba-final-quality-inspection-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-components-bom-page-en"
  - "frontendapt-pcba-component-sourcing-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-npi-assembly-page-en"
  - "frontendapt-pcba-small-batch-page-en"
  - "frontendhil-turnkey-assembly-product-page-en"
  - "frontendhil-box-build-assembly-product-page-en"
  - "koh-young-spi-technology"
  - "koh-young-aoi-technology"
  - "keysight-ict-systems"
tags: ["pcba", "testing", "quality-gates", "spi", "aoi", "x-ray", "ict", "fct", "flying-probe", "fai", "fqi", "traceability"]
---

# Definition

> PCBA quality gates and test strategy are a layered release model: sourcing and incoming review establish build trust, SPI/AOI/X-ray catch different inspection classes, ICT and flying probe cover electrical defect detection, FCT confirms powered behavior, and FAI/FQI plus traceability govern when a build can be released.

## Why This Topic Matters

- PCBA quality language gets distorted when `SPI`, `AOI`, `X-ray`, `ICT`, `FCT`, `flying probe`, `FAI`, and `FQI` are treated as one generic "test" bucket.
- The internal corpus already separates inspection, electrical verification, functional behavior, release gating, and supply-chain traceability, but those signals live in different pages.
- This topic page gives future blog writing a single internal frame for describing which gate answers which question, and where the limits of each method sit.

## Stable Facts

- The layered inspection stack card supports a sequence of `SPI` before placement, `AOI` for visible assembly defects, `X-ray` for hidden joints, `ICT` for fixture-based electrical verification, and `FCT` for powered behavior validation.
- The BGA reballing source adds a hidden-joint recovery and post-rework inspection use case, which reinforces why `X-ray` and inspection evidence remain important after dense-package rework.
- The ICT/FCT boundary card keeps `ICT` and `FCT` separate: `ICT` is node-level electrical access through a fixture, while `FCT` is end-use behavior under operating conditions.
- The FAI/FQI and traceability card treats incoming quality, first-article inspection, final inspection, BOM context, and traceability as distinct release gates rather than a single checkpoint.
- The flying-probe card positions flying probe as fixture-free electrical verification for low-volume or changing builds, complementary to fixture-based `ICT`.
- The BOM sourcing and traceability card ties component sourcing, lifecycle review, authenticity, and traceability into the turnkey assembly flow that sits upstream of final release.
- The SPI/AOI/ICT boundaries card makes the stage split explicit: `SPI` measures paste before reflow, `AOI` checks optical geometry and solder features, and `ICT` checks electrical faults on the assembled board.
- Taken together, the source set supports a quality strategy in which inspection, electrical coverage, functional validation, and release governance are related but not interchangeable.

## Engineering Boundaries

- Do not use `SPI`, `AOI`, `X-ray`, `ICT`, `FCT`, `flying probe`, `FAI`, or `FQI` as synonyms.
- `SPI` answers whether solder paste deposition is in control before placement; it does not replace assembly inspection or board electrical testing.
- `AOI` answers whether visible geometry, placement, polarity, and solder features are acceptable; it does not prove hidden joints or powered function.
- `X-ray` answers hidden-joint and concealed-defect questions; it does not replace optical inspection or functional testing.
- `ICT` answers electrical connectivity, opens, shorts, and component fault coverage on an assembled board; it does not prove the board behaves correctly in its end application.
- `FCT` answers whether the assembled board works in its intended powered context; it does not substitute for defect localization or fixture-level node access.
- `flying probe` answers fixture-free electrical coverage questions for prototypes, low-volume runs, or changing designs; it does not imply the same access model as `ICT`.
- `FAI` and `FQI` answer release-readiness and final acceptance questions; they do not replace the underlying inspection and test evidence.
- BOM sourcing and traceability answer component-risk and provenance questions; they do not by themselves certify board-level electrical or functional performance.

## Common Misreadings

- A board can pass `AOI` and still fail `ICT` or `FCT`.
- A board can pass `ICT` and still fail `FCT` because electrical continuity is not the same as intended behavior.
- `X-ray` can expose hidden solder defects, but it does not make `AOI` unnecessary.
- `flying probe` is not simply a cheaper `ICT`; it is a different access and economics model that fits different build conditions.
- `FAI` is not final shipment release by itself, and `FQI` is not a substitute for upstream inspection data.
- Traceability does not guarantee quality on its own; it is a control and evidence layer, not a defect-detection method.

## Must Refresh Before Publishing

- Coverage percentages or claimed fault-coverage ranges for any inspection or test method
- Report depth, including whether results are summary-only, trace-level, or include defect localization and images
- Fixture scope, including bed-of-nails access, boundary-scan support, custom tooling, and whether flying probe is the fallback
- Lead times for fixtures, test-program development, board access review, and first-article turnaround
- Customer-facing guarantees about pass/fail confidence, yield, reliability, or acceptance criteria

## Related Fact Cards

- `methods-pcba-layered-inspection-stack`
- `methods-pcba-ict-vs-fct-boundary`
- `methods-pcba-fai-fqi-and-traceability-gates`
- `methods-pcba-flying-probe-test-positioning`
- `methods-pcba-bom-sourcing-and-traceability-posture`
- `methods-spi-aoi-ict-boundaries`

## Primary Sources

- /code/hileap/frontendAPT/public/static/pcba/en/spi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/bga-reballing.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/incoming-quality-control.json
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/final-quality-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/testing-quality.json
- /code/hileap/frontendAPT/public/static/pcba/en/components-bom.json
- /code/hileap/frontendAPT/public/static/pcba/en/component-sourcing.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/npi-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/small-batch.json
- /code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/box-build-assembly.json
- https://kohyoung.com/en/solder-paste-inspection-technology/
- https://kohyoung.com/en/automated-optical-inspection-technology/
- https://www.keysight.com/us/en/products/in-circuit-test-for-manufacturing/in-circuit-test-systems.html
