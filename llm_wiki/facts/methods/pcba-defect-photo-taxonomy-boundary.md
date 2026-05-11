---
fact_id: "methods-pcba-defect-photo-taxonomy-boundary"
title: "PCBA defect-photo taxonomy can safely name visual defect families and contamination classes without promoting handbook thresholds or compliance judgments"
topic: "PCBA defect photo taxonomy boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-07"
source_ids:
  - "nasa-workmanship-page"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-quality-system-page-en"
tags: ["pcba", "inspection", "aoi", "workmanship", "taxonomy", "defects", "contamination", "visual-inspection"]
---

# Canonical Summary

> The current admitted source layer supports a conservative PCBA defect-photo taxonomy: agents may name recurring visual families such as solder wetting discontinuity, contact contamination, flux residue, particulate residue, adhesive contamination, placement misalignment, tombstone, and coplanarity-related anomalies. This layer supports inspection vocabulary and image classification only. It does not authorize pass/fail thresholds, percentages, or compliance judgments from secondary handbook plates.

## Stable Facts

- The existing inspection-governance layer already supports `AOI` as the visible geometry and workmanship-observation gate within a layered PCBA inspection flow.
- The NASA workmanship source supports top-level wording that interconnect quality depends on inspection techniques and defect-criteria discipline, without giving clause-level acceptance thresholds here.
- The local `B2` lane inventory provides stable candidate vocabulary for recurring visual families that can be preserved as taxonomy without promoting the handbook’s accept/reject framing.
- The safest promotion target is the identity of the visual class itself, not the handbook’s numeric or categorical judgment tied to that class.

## Safe Visual Taxonomy

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

## How To Use This Card

- Use this card when a draft needs English-only names for recurring PCBA defect-photo classes.
- Use it to describe what a local image appears to show at a taxonomy level.
- Pair it with the process-governance inspection cards when explaining where visible defect review belongs in the assembly flow.
- Keep local handbook images as supporting inventory only, with page and asset traceability retained outside this fact card.

## Engineering Boundaries

- A photo can support defect-family naming without proving acceptance or rejection.
- `Flux residue visibility`, `particulate contamination`, and `white residue` are taxonomy labels, not cleanliness thresholds.
- `Through-hole solder wetting continuity` is safe as a visual-class label, not as a minimum wetting percentage rule.
- `Gold finger solder contamination` is safe as a contact-area contamination class, not as a clause-level conformance statement.
- `Chip component misalignment`, `side-mounted chip placement`, `upside-down chip placement`, `tombstone defect`, and `coplanarity defect` are safe image-taxonomy labels, not proof of universal defect severity.

## Common Misreadings

- A handbook defect plate is not the same as an admitted acceptance standard.
- A named visual class is not permission to publish hidden thresholds that were shown in the secondary PDF.
- Local images should not be cited as proof that a board is compliant, noncompliant, reliable, or releasable.

## Must Stay Blocked

- solder-wetting percentages
- side-wetting coverage percentages
- solder-fill percentages
- heel, toe, fillet, or joint-height numeric limits
- `best / acceptable / unacceptable` workmanship labels from the secondary PDF
- any IPC-equivalent or NASA-equivalent acceptance conclusion inferred from the handbook

## Provenance Inventory

The following lane inventory established the promoted taxonomy candidates but does not act as source authority:

- `p4-215b2-2026-5-6-pcba-lane-b2-solder-defect-and-workmanship-pages.md`

Representative local asset families preserved in that inventory include:

- through-hole wetting example plates from pages `84-87`
- contact contamination plates from page `88`
- flux and residue images from pages `91-95`
- placement and early SMT anomaly plates from pages `130-151`

## Source Links

- /code/blogs/llm_wiki/sources/registry/methods/nasa-workmanship-page.md
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
