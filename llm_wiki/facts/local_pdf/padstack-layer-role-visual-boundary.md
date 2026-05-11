---
fact_id: "local-pdf-padstack-layer-role-visual-boundary"
title: "A curated local PCB资料 padstack diagram may support non-numeric padstack layer-role explanation only"
authority_class: "local_pdf_curated"
allowed_for: "blog_body"
not_allowed_for:
  - "official standard wording"
  - "manufacturer-recommended land-pattern defaults"
  - "supplier capability proof"
  - "numeric geometry guidance"
evidence_ids:
  - "pcbziliao-package-padstack-layer-role-diagram"
scope_type: "non_numeric_structural_visual_context"
confidence: "medium"
topic: "padstack layer-role visual boundary"
must_refresh: false
reviewed_at: "2026-05-08"
related_official_fact_ids:
  - "methods-padstack-origin-pin1-and-footprint-review-governance-boundary"
tags: ["local-pdf", "package", "padstack", "thermal-relief", "anti-pad", "solder-mask", "structural-visual"]
limits_and_non_claims:
  - "diagram-level explanation only"
  - "not a numeric padstack rule"
  - "not a standards or package-owner recommendation"
---

# Canonical Summary

This accepted local PDF diagram may support a narrow blog-body explanation of padstack layer-role vocabulary: plated drill, pad, thermal relief, anti pad, and solder-mask layers can be described structurally through the preserved local figure. The card is diagram-scoped only. It does not authorize formulas, default dimensions, or manufacturer-recommended land-pattern values.

## Curated Local-PDF Fact

- The preserved local figure shows a cross-section and top-view relationship among plated drill, pad, thermal relief, anti pad, and solder-mask layers.
- The diagram is reusable only to explain what those review objects are and how they relate structurally.
- English canonical wording remains the retrieval layer even though the preserved local image still contains Chinese labels.

## Safe Blog Usage

- Explain that padstack review concerns multiple layer roles rather than one generic copper shape.
- Use the diagram as a scoped visual aid when describing thermal relief or anti-pad terminology.
- Cite it as a repo-accepted local handbook figure, not as an official package-owner or standards source.

## Limits And Non-Claims

- Do not infer pad, drill, or annular defaults.
- Do not restate compensation equations.
- Do not present the diagram as an official IPC, CAD-owner, or manufacturer recommendation.

## Evidence Links

- [padstack-layer-role-diagram.md](/code/blogs/llm_wiki/pdf_evidence/pcb_ziliao/package/padstack-layer-role-diagram.md)

## Related Official Facts

- [padstack-origin-pin1-and-footprint-review-governance-boundary.md](/code/blogs/llm_wiki/facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md)
