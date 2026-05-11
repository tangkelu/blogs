---
evidence_id: "pcbziliao-package-pin1-origin-installation-mark-text-boundary"
batch_id: "pcb_ziliao"
original_pdf_title: "【PCB必备】42种-常见PCB封装设计指导规范"
source_origin_path: "/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf"
page: 29-30
evidence_type: "text_excerpt"
claim_summary: "Handbook text describing pin-1 mark, polarity mark, installation mark, and package-origin placement examples that is safe only as local documentation-governance context."
authority_class: "local_pdf_supporting_evidence"
allowed_use:
  - "local documentation-governance context for pin-1 mark, polarity mark, and installation mark presence"
  - "local explanation that the handbook distinguishes regular-shape, through-hole, and connector origin placement examples"
  - "support for a tightly scoped local_pdf_fact"
blocked_use:
  - "universal footprint-origin rule"
  - "standards-grade pin-1 or installation-mark convention"
  - "numeric silkscreen, clearance, or keepout rules from the same pages"
promotion_status: "promoted_to_local_pdf_fact"
deletion_safe: true
page_excerpt_ref: "page-29-30-text"
related_fact_ids:
  - "methods-padstack-origin-pin1-and-footprint-review-governance-boundary"
notes_on_branding: "Page text is handbook-derived and surrounded by branded shell in the source PDF."
notes_on_translation: "Use English canonical governance wording only; do not preserve the handbook phrasing as universal rule text."
---

# Claim Summary

This preserved local text excerpt can support a narrow local explanation of package-documentation markers and origin-handling examples only.

## Allowed Use

- Explain that package documentation may need explicit `pin-1`, polarity, and installation markers.
- Explain that the handbook distinguishes different local origin-placement examples for regular-shape parts, through-hole parts, and connectors.
- Support a scoped `local_pdf_fact` that remains local-PDF-bound and non-universal.

## Blocked Use

- Do not restate the handbook examples as official IPC, CAD-owner, or package-owner rules.
- Do not promote page `29-30` silkscreen, spacing, keepout, or hole-table numerics through this record.
- Do not turn connector-origin examples into a universal library-default rule.

## Promotion Judgment

- current result:
  - `promoted_to_local_pdf_fact`
- promoted fact:
  - `local-pdf-pin1-origin-installation-mark-visual-boundary`
