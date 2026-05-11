---
topic_id: "testing-pcba-visual-inspection-taxonomy"
title: "PCBA Visual Inspection Taxonomy"
category: "testing"
status: "draft"
last_reviewed_at: "2026-05-07"
fact_ids:
  - "methods-pcba-inspection-process-governance-boundary"
  - "processes-inspection-governance-navigation-map"
  - "methods-parameter-scope-test-inspection-optical-method-dimensions"
  - "methods-pcba-defect-photo-taxonomy-boundary"
  - "methods-component-orientation-and-polarity-inspection-vocabulary-boundary"
  - "methods-board-warpage-and-jumper-wire-inspection-vocabulary-boundary"
source_ids:
  - "nasa-workmanship-page"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-quality-system-page-en"
tags: ["pcba", "inspection", "aoi", "taxonomy", "visual-inspection", "orientation", "polarity", "warpage", "jumper-wire", "contamination"]
---

# Definition

> PCBA visual inspection taxonomy is the bounded vocabulary layer for describing what visible assembly images and inspection views are about. It groups defect families, contamination classes, orientation and polarity terms, and structural context terms without turning secondary handbook image plates into acceptance criteria.

## Why This Topic Matters

- The PCBA learning program already recovered strong local image-taxonomy candidates from the `B2` and `B3` handbook lanes, but those lanes were secondary-PDF inventory, not admitted authority.
- The current internal inspection-governance layer already supports `AOI`, visible geometry review, and defect-recognition posture, which is enough to promote conservative naming vocabulary now.
- This page gives future writing a single place to route visual-inspection language while keeping thresholds, dimensions, and `acceptable / unacceptable` conclusions blocked.

## Stable Facts

- Visible assembly review belongs to the broader PCBA inspection stack and is distinct from `ICT`, `FCT`, and hidden-joint `X-ray` review.
- The current admitted layer supports taxonomy-level naming for common visible defect and contamination families.
- The current admitted layer also supports orientation and polarity vocabulary as image-description language.
- Board-warp and jumper-wire images can be described as structural context without promoting handbook percentages or repair prescriptions.

## Taxonomy Groups

### Defect and contamination classes

- `through-hole solder wetting continuity`
- `gold finger solder contamination`
- `flux residue visibility`
- `particulate contamination`
- `white residue`
- `adhesive contamination before soldering`
- `chip component misalignment`
- `side-mounted chip placement`
- `upside-down chip placement`
- `tombstone defect`
- `coplanarity defect`

### Orientation and polarity classes

- `horizontal component orientation`
- `component polarity visibility`
- `readable marking direction`
- `vertical component polarity orientation`
- `radial capacitor lead orientation`
- `reversed polarity example`

### Structural context classes

- `burn-mark versus solder-mask discoloration`
- `board warpage visual example`
- `jumper-wire routing example`
- `jumper-wire path clearance context`

## How To Use This Page

- Use this page when a draft needs English-only names for visible PCBA inspection images or defect families.
- Route process-sequencing questions to [inspection-governance-navigation-map](/code/blogs/llm_wiki/wiki/processes/inspection-governance-navigation-map.md).
- Route method-dimension wording to [parameter-scope-test-inspection-optical-method-dimensions.md](/code/blogs/llm_wiki/facts/methods/parameter-scope-test-inspection-optical-method-dimensions.md).
- Route detailed boundaries to:
  - [pcba-defect-photo-taxonomy-boundary.md](/code/blogs/llm_wiki/facts/methods/pcba-defect-photo-taxonomy-boundary.md)
  - [component-orientation-and-polarity-inspection-vocabulary-boundary.md](/code/blogs/llm_wiki/facts/methods/component-orientation-and-polarity-inspection-vocabulary-boundary.md)
  - [board-warpage-and-jumper-wire-inspection-vocabulary-boundary.md](/code/blogs/llm_wiki/facts/methods/board-warpage-and-jumper-wire-inspection-vocabulary-boundary.md)

## Engineering Boundaries

- This page is for taxonomy and inspection-language only.
- It does not authorize threshold, percentage, dimension, or release-criteria claims.
- It does not convert local handbook image plates into standards evidence.
- It does not allow `best / acceptable / unacceptable` wording from the secondary PDF to be treated as public workmanship truth.
- It does not let an image prove compliance, reliability, or shipment readiness.

## Must Stay Blocked

- solder-wetting percentages
- side-wetting coverage percentages
- solder-joint geometry limits
- standoff dimensions such as `1.5 mm`
- warpage thresholds such as `1.5%` and `0.75%`
- jumper-wire dimensional, gauge, and material prescriptions
- any IPC-equivalent, MIL-equivalent, or NASA-equivalent acceptance conclusion inferred from the handbook

## Provenance And Residual Gaps

- The promoted taxonomy was inventoried in:
  - `p4-215b2-2026-5-6-pcba-lane-b2-solder-defect-and-workmanship-pages.md`
  - `p4-215b3-2026-5-6-pcba-lane-b3-cleanliness-warpage-jumper-orientation-pages.md`
- Those lane logs preserve page-bounded asset traceability, but they remain provenance inventory rather than authority.
- Stronger public workmanship or standards references are still needed before any class-specific acceptance language can be promoted.

## Primary Sources

- /code/blogs/llm_wiki/sources/registry/methods/nasa-workmanship-page.md
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
