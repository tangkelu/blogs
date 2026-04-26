---
fact_id: "methods-hybrid-rf-stackup-capability"
title: "Internal support for hybrid RF stackups is already a repeated site-level capability claim"
topic: "Hybrid RF stackup capability"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendhil-rogers-product-page-en"
  - "frontendhil-high-frequency-product-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
tags: ["internal", "hybrid-stackup", "rf", "fr4", "ptfe", "methods"]
---

# Canonical Summary

> Across both HIL and APT non-blog product pages, hybrid RF stackups are already presented as a core internal capability: premium RF laminate on signal-critical layers, FR-4 or other structural materials elsewhere, with cost, manufacturability, and validation explicitly discussed.

## Stable Facts

- The HIL Rogers product JSON explicitly presents `hybrid Rogers + FR-4 stackups` as a supported build style.
- The same HIL source frames selective use of Rogers on RF energy paths with FR-4 internal planes as a cost/performance strategy.
- The HIL high-frequency product JSON also positions `hybrid stackups` as a standard cost-optimization method for RF and mmWave work.
- The APT high-frequency page states hybrid PTFE, hydrocarbon, and low-loss FR-4 stackups are part of the public service framing.
- The APT microwave page includes `Hybrid FR-4` in the hero chips and gives example stackups such as `Hybrid RO3003 + FR-4 stripline`.
- Across these internal pages, hybrid builds are connected to both RF performance control and practical manufacturing tradeoffs.

## Conditions And Methods

- This card captures repeated internal service framing, not official laminate-manufacturer guidance.
- Use it to support internal wiki pages about stackup strategy, quoting intake, and solution framing.
- If a blog needs a numeric cost-saving or performance claim, re-check against stronger sources first.

## Limits And Non-Claims

- This card does not prove every hybrid stackup is manufacturable without case-by-case review.
- It also does not prove any specific percentage cost reduction for every build.

## Open Questions

- Add a dedicated internal stackup-intake checklist card next

## Source Links

- /code/hileap/frontendHIL/public/static/products/en/rogers-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/microwave-pcb.json
