---
fact_id: "local-pdf-footprint-review-dimensions-visual-boundary"
title: "Curated local PCB资料 footprint diagrams may support non-numeric review-dimension explanation only"
authority_class: "local_pdf_curated"
allowed_for: "blog_body"
not_allowed_for:
  - "official standard wording"
  - "manufacturer-recommended land-pattern defaults"
  - "supplier capability proof"
  - "numeric threshold bands"
evidence_ids:
  - "pcbziliao-package-leaded-footprint-review-dimensions-diagram"
  - "pcbziliao-package-chip-footprint-review-dimensions-diagram"
scope_type: "non_numeric_structural_visual_context"
confidence: "medium"
topic: "footprint review dimensions visual boundary"
must_refresh: false
reviewed_at: "2026-05-08"
related_official_fact_ids:
  - "methods-padstack-origin-pin1-and-footprint-review-governance-boundary"
tags: ["local-pdf", "package", "footprint", "toe", "heel", "side-clearance", "pad-length", "pad-width", "inner-spacing", "structural-visual"]
limits_and_non_claims:
  - "review-dimension explanation only"
  - "not a chip-size or leaded-package threshold rule"
  - "not a standards or package-owner recommendation"
---

# Canonical Summary

These accepted local PDF diagrams may support a narrow blog-body explanation of footprint-review dimensions only. In the leaded-package example, `toe`, `heel`, and `side clearance` are usable as non-numeric review dimensions. In the chip-footprint example, `pad length`, `pad width`, and `inner spacing` are usable as non-numeric review dimensions. This card does not authorize threshold bands, package-size rules, or owner-recommended land-pattern values.

## Curated Local-PDF Fact

- One preserved local figure shows lead-to-pad review dimensions for `toe`, `heel`, and `side clearance`.
- One preserved local figure shows chip-footprint review dimensions for `pad length`, `pad width`, and `inner spacing`.
- Both figures are reusable only for structural explanation of what the dimensions refer to.

## Safe Blog Usage

- Explain that leaded-package review and chip-footprint review use different geometric dimensions.
- Use the preserved local diagrams as scoped visual aids for those dimension names.
- Cite them as repo-accepted local handbook figures, not as official land-pattern recommendations.

## Limits And Non-Claims

- Do not restate `optimal`, `general`, `risk`, or `danger` tables.
- Do not convert the figures into mil, mm, or package-size-specific rules.
- Do not present the figures as official IPC, package-owner, or supplier DFM guidance.

## Evidence Links

- [leaded-footprint-review-dimensions-diagram.md](/code/blogs/llm_wiki/pdf_evidence/pcb_ziliao/package/leaded-footprint-review-dimensions-diagram.md)
- [chip-footprint-review-dimensions-diagram.md](/code/blogs/llm_wiki/pdf_evidence/pcb_ziliao/package/chip-footprint-review-dimensions-diagram.md)

## Related Official Facts

- [padstack-origin-pin1-and-footprint-review-governance-boundary.md](/code/blogs/llm_wiki/facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md)
