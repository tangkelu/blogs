---
evidence_id: "pcbziliao-package-bga-array-layout-context"
batch_id: "pcb_ziliao"
original_pdf_title: "【PCB必备】42种-常见PCB封装设计指导规范"
source_origin_path: "/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf"
page: 28
evidence_type: "structural_diagram"
claim_summary: "BGA array layout illustration that is safe as family-aware array context only and remains too adjacent to blocked pitch-to-pad numerics for first-slice promotion."
authority_class: "blocked_evidence"
allowed_use:
  - "family-aware BGA array context"
  - "supporting provenance for future authority recovery"
blocked_use:
  - "pitch-to-pad tables"
  - "exact pitch or pad-diameter claims"
  - "default land-pattern rules"
promotion_status: "evidence_only"
deletion_safe: true
local_asset_path: "/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-42种-常见PCB封装设计指导规范/images/35a09507227a52b9.jpeg"
page_excerpt_ref: "asset:35a09507227a52b9"
related_fact_ids:
  - "methods-package-family-and-footprint-governance-vocabulary-boundary"
notes_on_branding: "No visible branding."
notes_on_translation: "Use English canonical package-family wording only."
---

# Claim Summary

This preserved local diagram is safe as BGA array-layout context only.

## Allowed Use

- Reference that a BGA family uses an array-footprint context.
- Preserve provenance for future authority recovery or later local_pdf promotion if a cleaner boundary is needed.

## Blocked Use

- Do not infer pitch or pad-diameter values.
- Do not imply a universal BGA land-pattern rule.

## Promotion Judgment

- current result:
  - `evidence_only`
- reason:
  - the same page remains too adjacent to blocked pitch-to-pad numerics
