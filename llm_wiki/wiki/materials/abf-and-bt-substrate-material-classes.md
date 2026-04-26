---
topic_id: "materials-abf-and-bt-substrate-material-classes"
title: "ABF And BT Substrate Material Classes"
category: "materials"
status: "draft"
last_reviewed_at: "2026-04-24"
fact_ids:
  - "materials-abf-and-bt-substrate-source-coverage"
source_ids:
  - "frontendhil-ic-substrate-pcb-product-page-en"
  - "frontendapt-pcb-advanced-pcb-manufacturing-page-en"
  - "ajinomoto-abf-innovation-story"
  - "ajinomoto-fine-techno-abf-page"
  - "mgc-bt-materials-page"
tags: ["materials", "abf", "bt", "ic-substrate", "package-substrate", "build-up"]
---

# Definition

> ABF and BT should be handled as substrate-material classes for IC-substrate and package-build-up discussions, not as shorthand for a complete stackup decision. The wiki's job is to preserve class-level source boundaries until grade-level datasheets are explicitly attached.

## Why This Topic Matters

- HIL/APT already expose IC-substrate and advanced manufacturing contexts where ABF and BT become legitimate discussion topics.
- Official source coverage now exists for both `ABF` and `BT` as material classes, which is enough for class-level topic pages.
- The main governance problem is preventing class names from being misused as proof of process capability, package qualification, or frozen electrical values.

## Stable Facts

- HIL/APT non-blog pages include IC-substrate and advanced PCB manufacturing contexts.
- Ajinomoto and Ajinomoto Fine-Techno provide official ABF background and product-family context.
- Mitsubishi Gas Chemical provides an official BT-material class page for printed circuit board laminated materials.
- These sources support class-level framing for package-substrate, IC-substrate, and build-up material discussions.

## Engineering Boundaries

- Use `ABF` to anchor build-up insulating-film context in semiconductor substrate discussions.
- Use `BT` to anchor laminated substrate-material context, not as a complete package-material table.
- Keep Dk, Df, CTE, Tg, modulus, reliability, laser-drilling, desmear, and process-window claims behind current grade-level datasheets.
- Do not convert class-level source coverage into a statement that every ABF or BT structure is manufacturable by HIL/APT.
- Separate material-class discussion from OSAT, package-house, or customer qualification requirements.

## Common Misreadings

- `ABF` and `BT` are not interchangeable labels for any advanced substrate.
- A material class being officially anchored does not mean a specific package substrate stackup is approved.
- Internal IC-substrate capability framing does not replace supplier datasheets or package-design rules.
- A class-level BT page does not justify freezing numeric laminate constants into blog tables.

## Must Refresh Before Publishing

- Any material-constant table for ABF or BT
- Any design-window statement for via density, build-up count, reliability, or thermal limits
- Any claim about package qualification or customer approval
- Any comparison that claims one class is universally superior

## Related Fact Cards

- `materials-abf-and-bt-substrate-source-coverage`

## Primary Sources

- /code/hileap/frontendHIL/public/static/products/en/ic-substrate-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/advanced-pcb-manufacturing.json
- https://www.ajinomoto.com/innovation/our_innovation/buildupfilm
- https://www.aft-website.com/en/products/insulating_film-abf/
- https://www.mgc.co.jp/eng/products/sc/btprint/
