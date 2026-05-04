---
topic_id: "materials-abf-and-bt-substrate-material-classes"
title: "ABF And BT Substrate Material Classes"
category: "materials"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "materials-abf-and-bt-substrate-source-coverage"
  - "materials-package-substrate-boundary-kyocera-ajinomoto"
source_ids:
  - "frontendhil-ic-substrate-pcb-product-page-en"
  - "frontendapt-pcb-advanced-pcb-manufacturing-page-en"
  - "ajinomoto-abf-innovation-story"
  - "ajinomoto-fine-techno-abf-page"
  - "mgc-bt-materials-page"
tags: ["materials", "abf", "bt", "ic-substrate", "package-substrate", "build-up"]
---

# Definition

> ABF and BT should be routed as package-substrate material classes for IC-substrate and build-up discussions, not as shorthand for a complete manufacturable stackup. This page exists to keep class naming, substrate context, and supplier-source boundaries stable until grade-level datasheets and explicit platform evidence are attached.

## Why This Topic Matters

- Package-substrate and IC-substrate discussions increasingly appear next to advanced PCB and build-up topics, so the repository needs a clean routing surface for `ABF` and `BT`.
- Local facts already establish official source coverage for both classes, which is enough for boundary-level wiki use.
- The main governance problem is preventing material-class labels from being misread as proof of substrate platform readiness, manufacturability, or approved design windows.

## Stable Facts

- HIL/APT local business JSON already includes IC-substrate and advanced PCB manufacturing contexts where package-substrate material classes become relevant.
- Ajinomoto and Ajinomoto Fine-Techno provide official ABF background and insulating-film / product-family context for semiconductor substrate discussions.
- Mitsubishi Gas Chemical provides an official BT material-class anchor for printed-circuit laminated-material context.
- The current local fact layer supports class-level routing for package-substrate, IC-substrate, and build-up discussions without promoting grade-level constants.

## Routing Use

- Use `ABF` when the discussion is about build-up insulating-film class context in semiconductor or package-substrate structures.
- Use `BT` when the discussion is about laminated substrate-material class context in package-substrate or substrate-core framing.
- Use this page to separate package-substrate language from ordinary rigid-HDI or generic multilayer PCB language.
- Escalate to exact material cards or future datasheets before publishing class-specific constants, process windows, or stackup prescriptions.

## Engineering Boundaries

- Treat `ABF` and `BT` as class labels first, not as finished material selections for a customer substrate design.
- Keep Dk, Df, CTE, Tg, modulus, laser-drilling behavior, desmear behavior, reliability, and process-window claims behind current grade-level datasheets.
- Do not convert class-level source coverage into a statement that every ABF or BT package-substrate structure is manufacturable by HIL/APT or any other named platform owner.
- Keep package-substrate material discussion separate from OSAT, package-house, substrate-vendor, and customer approval gates.
- Keep this page at routing level; exact stackup architecture, via strategy, yield control, and qualification logic belong to narrower evidence lanes.

## Common Misreadings

- `ABF` and `BT` are not interchangeable shorthand for every advanced package substrate.
- An officially anchored material class does not mean a specific package-substrate stackup, build-up count, or substrate platform is approved.
- Internal IC-substrate capability framing does not replace supplier datasheets, package-design rules, or customer substrate standards.
- A class-level page does not justify freezing numeric laminate constants or design windows into external content.
- A package-substrate context page is not evidence of owner-platform qualification.

## Explicit Non-Claims

- This page does not make package-substrate performance claims.
- It does not prove owner-platform qualification for ABF or BT substrate builds.
- It does not support yield, reliability, cost, lead-time, or pass-rate claims.
- It does not decide between ABF and BT for a real customer program.

## Must Refresh Before Publishing

- Any material-constant table for ABF or BT
- Any design-window statement for line/space, via density, build-up count, thermal limits, or reliability behavior
- Any owner-platform qualification or customer-approval claim
- Any yield, cost, throughput, or reliability comparison
- Any comparison that claims one class is universally superior

## Related Fact Cards

- `materials-abf-and-bt-substrate-source-coverage`
- `materials-package-substrate-boundary-kyocera-ajinomoto`

## Primary Sources

- /code/hileap/frontendHIL/public/static/products/en/ic-substrate-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/advanced-pcb-manufacturing.json
- https://www.ajinomoto.com/innovation/our_innovation/buildupfilm
- https://www.aft-website.com/en/products/insulating_film-abf/
- https://www.mgc.co.jp/eng/products/sc/btprint/
