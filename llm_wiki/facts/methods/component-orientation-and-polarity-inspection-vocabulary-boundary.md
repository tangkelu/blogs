---
fact_id: "methods-component-orientation-and-polarity-inspection-vocabulary-boundary"
title: "Component orientation and polarity inspection vocabulary can be promoted as visual-language only, without handbook standoff or acceptability claims"
topic: "Component orientation and polarity inspection vocabulary boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-07"
source_ids:
  - "nasa-workmanship-page"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-quality-system-page-en"
tags: ["pcba", "inspection", "aoi", "orientation", "polarity", "workmanship", "taxonomy", "visual-inspection"]
---

# Canonical Summary

> The current admitted source layer supports English-only inspection vocabulary for component orientation and polarity review: horizontal orientation, vertical orientation, polarity visibility, readable marking direction, radial capacitor lead orientation, and reversed-polarity examples. This card supports visual-language and inspection-taxonomy use only. It does not authorize handbook acceptability judgments, standoff dimensions, or universal polarity rules for every component class.

## Stable Facts

- The process-governance layer already supports `AOI` and visual inspection as the stage where presence, orientation, polarity, and visible placement conditions are reviewed.
- The NASA workmanship source supports the broad connection between workmanship quality, inspection discipline, and defect-recognition posture.
- The `B3` lane inventory preserves page-bounded local examples showing orientation and polarity classes that are useful for vocabulary normalization even though the handbook judgment labels remain blocked.

## Safe Orientation And Polarity Vocabulary

- `horizontal component orientation`
- `component polarity visibility`
- `readable marking direction`
- `vertical component polarity orientation`
- `radial capacitor lead orientation`
- `reversed polarity example`

## Safe Usage Boundary

- Use this card to name what an inspector or image appears to be checking.
- Use it to distinguish orientation vocabulary from solder-geometry vocabulary.
- Use it to explain that polarity review is part of visible assembly inspection rather than electrical proof.
- Use it with local image provenance when later image-linked pages are built.

## Engineering Boundaries

- Orientation identity is safe; orientation acceptability thresholds from the handbook are not.
- `Readable marking direction` is safe as a visibility concept, not as a universal requirement for every assembly style.
- `Radial capacitor lead orientation` is safe as a named visual class, not as permission to reuse handbook lead-length or standoff dimensions.
- `Reversed polarity example` is safe as a taxonomy label, not as a universal field-failure claim.

## Common Misreadings

- Polarity visibility does not prove powered functionality.
- A local photo showing correct or reversed orientation does not by itself establish a released inspection criterion.
- Handbook `best / acceptable / unacceptable` image labels are not equivalent to admitted public workmanship clauses.

## Must Stay Blocked

- the `1.5 mm` axial standoff example
- any implied universal standoff minimum
- any handbook orientation `best / acceptable / unacceptable` conclusion
- any clause-level IPC, NASA, or MIL workmanship acceptance content not already admitted through stronger sources

## Provenance Inventory

The following lane inventory established the promoted orientation and polarity vocabulary but does not act as source authority:

- `p4-215b3-2026-5-6-pcba-lane-b3-cleanliness-warpage-jumper-orientation-pages.md`

Representative local asset families preserved in that inventory include:

- horizontal placement and polarity-visibility plates from page `44`
- vertical polarity-orientation figures from page `45`
- radial capacitor and axial-part orientation figures from page `46`

## Source Links

- /code/blogs/llm_wiki/sources/registry/methods/nasa-workmanship-page.md
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
