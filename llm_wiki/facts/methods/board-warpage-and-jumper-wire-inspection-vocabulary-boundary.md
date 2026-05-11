---
fact_id: "methods-board-warpage-and-jumper-wire-inspection-vocabulary-boundary"
title: "Board warpage and jumper-wire inspection vocabulary can be used as structural context without promoting handbook limits, gauge rules, or routing prescriptions"
topic: "Board warpage and jumper-wire inspection vocabulary boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-07"
source_ids:
  - "nasa-workmanship-page"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-quality-system-page-en"
tags: ["pcba", "inspection", "warpage", "jumper-wire", "workmanship", "taxonomy", "visual-inspection", "structural-context"]
---

# Canonical Summary

> The current admitted source layer supports conservative vocabulary for visible board-warp and jumper-wire inspection context: burn-mark versus discoloration, board warpage visual example, jumper-wire routing example, and path-clearance context. This layer is structural only. It does not authorize handbook bow/twist percentages, jumper-wire gauge rules, routing prescriptions, or accept/reject decisions.

## Stable Facts

- The existing inspection-governance layer supports visible workmanship review as part of broader assembly quality control.
- The NASA workmanship source supports general wording that inspection and defect-recognition discipline matter for interconnect quality.
- The `B3` lane inventory preserves visual examples that are useful for structural vocabulary around board shape distortion and jumper rework routing without upgrading the handbook’s thresholds into facts.

## Safe Structural Vocabulary

- `burn-mark versus solder-mask discoloration`
- `board warpage visual example`
- `jumper-wire routing example`
- `jumper-wire path clearance context`

## Safe Usage Boundary

- Use this card when a draft needs neutral vocabulary for visible board distortion or jumper-wire routing context.
- Use it to describe what a local image shows without claiming released criteria.
- Use it to keep structural image description separate from acceptance, reliability, or standards claims.

## Engineering Boundaries

- `Board warpage visual example` is safe as a structural description, not as a universal flatness limit.
- `Burn-mark versus solder-mask discoloration` is safe as a visual distinction, not as a severity threshold.
- `Jumper-wire routing example` is safe as a routing-context label, not as permission to reuse handbook path, insulation, or conductor rules.
- `Jumper-wire path clearance context` is safe as a descriptive phrase when it avoids dimensional or pass/fail wording.

## Common Misreadings

- A warped-board photo does not establish a numeric bow/twist limit.
- A jumper-wire image does not prove approved repair method, conductor class, or workmanship compliance.
- The presence of routing guidance in a secondary handbook does not make that guidance an admitted production rule.

## Must Stay Blocked

- warpage thresholds such as `1.5%` and `0.75%`
- jumper-wire dimensional rules such as `12.7 mm`
- jumper-wire wire-gauge prescriptions such as `22#-30#`
- material, insulation, or routing prescriptions reconstructed from handbook text
- any accept/reject conclusion inferred from handbook burn, warp, or jumper plates

## Provenance Inventory

The following lane inventory established the promoted structural vocabulary but does not act as source authority:

- `p4-215b3-2026-5-6-pcba-lane-b3-cleanliness-warpage-jumper-orientation-pages.md`

Representative local asset families preserved in that inventory include:

- board surface discoloration and burn examples from page `119`
- board warpage visual examples from page `119`
- jumper-wire routing example from page `121`

## Source Links

- /code/blogs/llm_wiki/sources/registry/methods/nasa-workmanship-page.md
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
