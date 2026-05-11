# `pcb_ziliao` PDF Evidence

This directory preserves page-level and asset-level evidence from `/code/blogs/tmps/PCB资料`.

Use this layer for:

- deletion-safe provenance after `tmps/` cleanup
- figure and photo lookup
- promotion support for `facts/local_pdf/`
- blocked-evidence tracking for claims that must not enter blog body

Do not use this layer by itself as blog-body authority.

Minimum record fields:

- `evidence_id`
- `batch_id`
- `original_pdf_title`
- `source_origin_path`
- `page`
- `evidence_type`
- `claim_summary`
- `authority_class`
- `allowed_use`
- `blocked_use`
- `promotion_status`
- `deletion_safe`

Current first-slice posture:

- `pcba/` stores image-based provenance for taxonomy and orientation examples that remain evidence-only
- `package/` stores structural diagrams, some of which now support curated `local_pdf_fact` cards
