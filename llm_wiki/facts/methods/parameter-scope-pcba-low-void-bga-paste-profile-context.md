---
fact_id: "methods-parameter-scope-pcba-low-void-bga-paste-profile-context"
title: "Low-void BGA parameter cards may use only named paste or page-scoped profile terms, not generic reflow defaults"
topic: "PCBA parameter scope for low-void BGA paste and profile context"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "indium-8-9hf-solder-paste-pds"
  - "indium-reflow-profile-to-paste-spec"
  - "kester-standard-reflow-profile"
  - "frontendapt-pcba-spi-inspection-page-en"
  - "frontendapt-pcba-bga-qfn-fine-pitch-page-en"
  - "frontendapt-pcba-x-ray-inspection-page-en"
tags: ["parameter-scope", "pcba", "low-void", "bga", "reflow", "solder-paste", "spi", "x-ray"]
---

# Canonical Summary

> For `low-void BGA` writing, real parameters are admissible only when they stay attached to one named solder-paste source or one named local page context. Indium and Kester support profile-stage vocabulary and paste-specific profile review. They do not authorize a generic HIL low-void reflow recipe.

## Source-Backed Parameters

- `Indium8.9HF` is a valid named product anchor for product-specific solder-paste profile discussion because the registry record explicitly classifies it as a product data sheet and allows product-specific profile-window use only in that exact context.
- Indium's reflow-profile note supports the parameter families that may be discussed during profile review: ramp, soak, time above liquidus, peak, and cooling.
- Kester's standard profile supports the staged vocabulary `preheat`, `soak`, `reflow`, and `cooling` as source-backed process-region terms tied to Kester's own alloy/profile context.
- The internal SPI page supports paste-deposit parameter language such as `volume`, `height`, `area`, `offset`, `bridging risk`, and `missing paste` before placement.
- The internal fine-pitch and X-ray pages support hidden-joint context for BGA / QFN assemblies where print and profile tuning are discussed because post-reflow visibility is limited.

## Scope And Applicability Limits

- Use this card for `low-void-bga-reflow-data-center-optical-module`, `low-void-bga-reflow-high-speed-si`, `low-void-bga-reflow-industrial-robotics-control`, and `low-void-bga-reflow-medical-imaging-wearable`.
- Admissible real values must stay attached to the exact named paste or exact named source context. Example-safe posture: `Indium8.9HF datasheet values`, not `recommended lead-free BGA profile`.
- Safe parameter vocabulary for broad reuse without numbers: `preheat`, `soak`, `reflow`, `cooling`, `time above liquidus`, `peak`, `paste volume`, `paste height`, `alignment`, `offset`, `bridging`, `missing paste`.
- If a future draft needs exact numbers for peak, TAL, ramp, soak, or cooling, refresh directly from the cited product or profile document and keep the named paste or alloy context in the same sentence.

## Explicit Blocked Uses

- Do not convert Indium or Kester profile material into generic reflow recipes for HIL, APT, or unnamed customer assemblies.
- Do not derive void thresholds, void pass/fail criteria, or `low-void` outcome guarantees from these sources.
- Do not convert paste-specific values into coating thickness defaults, cure defaults, or any unrelated process window.
- Do not use these sources to make HIL capability claims, yield claims, cost claims, lead-time claims, or reliability guarantees.
- Do not reuse any fine-pitch or X-ray context as proof that a given BGA program achieves low voiding.

## Blog Usage

- empty-image slugs: `low-void-bga-reflow-data-center-optical-module`, `low-void-bga-reflow-high-speed-si`, `low-void-bga-reflow-industrial-robotics-control`, `low-void-bga-reflow-medical-imaging-wearable`
- families supported:
  - `low-void-bga`
  - `hidden-joint-inspection`
  - `dense-package-process-review`

## Open Questions

- The current environment did not provide local PDF text extraction for the Indium and Kester PDFs, so this card intentionally stops at parameter-family scope unless a later pass refreshes exact values from the product documents again.
- Add a narrower named-paste fact card later if one supported slug requires exact paste-window numbers in addition to stage vocabulary.

## Source Links

- https://www.indium.com/wp-content/uploads/2025/01/Indium8.9HF-High-Reliability-Solder-Paste-PDS-99702-R7.pdf
- https://www.indium.com/blog/matching-a-reflow-profile-to-a-solder-paste-spec/
- https://www.kester.com/Portals/0/Documents/Knowledge%20Base/Standard_Profile.pdf
- /code/hileap/frontendAPT/public/static/pcba/en/spi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/bga-qfn-fine-pitch.json
- /code/hileap/frontendAPT/public/static/pcba/en/x-ray-inspection.json
