---
fact_id: "standards-22-layer-hi-rel-acceptance-workflow-boundary"
title: "22-layer hi-rel acceptance workflow should be framed as layered program context, not as a free acceptance-table shortcut"
topic: "22-layer hi-rel acceptance workflow boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-26"
source_ids:
  - "ipc-a-600k-toc"
  - "ipc-6011a-toc"
  - "ipc-6012f-toc"
  - "ipc-6012em-medical-addendum-release"
  - "ipc-6012em-medical-addendum-page"
  - "ipc-6012fa-automotive-addendum-page"
  - "ipc-6012fa-toc"
  - "ipc-6012fs-space-military-addendum-page"
  - "ipc-6012fs-toc"
  - "ipc-6012-addendum-taxonomy-page"
  - "as9102c-first-article-inspection-page"
  - "as9145-page"
  - "fda-21cfr-820181-device-master-record-page"
  - "fda-21cfr-820184-device-history-record-page"
tags: ["22-layer", "high-reliability", "acceptance-workflow", "ipc-6012", "ipc-a-600", "fai", "dmr", "dhr", "boundary"]
---

# Canonical Summary

> Public IPC, SAE, and FDA/eCFR records are strong enough to support a guarded `22-layer` acceptance-workflow hierarchy in `llm_wiki`: base printed-board framework, procurement-triggered addendum family, inspection/acceptability vocabulary, documented first-article workflow, and controlled build-history vocabulary. They are not strong enough to provide reusable acceptance thresholds, approval decisions, or release authority.

## Stable Facts

- A conservative `22-layer` rewrite may describe acceptance workflow as a layered governance problem rather than a single `Class 3` shortcut.
- Public `IPC-6011A` metadata supports a generic `IPC-601X` framework layer where procurement documentation defines class and exceptions.
- Public `IPC-6012F` and addendum metadata support a base-vs-addendum hierarchy for rigid boards across medical, automotive, and space/military branches.
- Public `IPC-A-600K` metadata supports a separate bare-board inspection/acceptability vocabulary layer distinct from assembly workmanship and distinct from supplier-status claims.
- Public `AS9102C` and `AS9145` metadata support documented first-build and product/process-validation workflow language as governance context, not as proof of accepted results.
- Public `DMR` and `DHR` records support controlled-build-document and manufacturing-history vocabulary when a regulated or mission-sensitive program needs it.
- Procurement-triggered addenda and build-history records may be mentioned as workflow context, but they do not collapse into one freely reusable acceptance rule set.

## Conditions And Methods

- Use this card when a `22-layer` draft needs to explain how acceptance-related language sits across framework, addendum, inspection, first-article, and build-history layers.
- Pair this card with `facts/standards/22-layer-high-reliability-rewrite-guardrail.md`, `facts/standards/fai-and-aerospace-quality-workflow-metadata.md`, and `facts/standards/fda-medical-device-documentation-and-traceability-metadata.md`.
- Prefer wording such as `may be governed by`, `can involve`, `may require documented`, and `should be confirmed by procurement documentation` over wording such as `must pass`, `meets Class 3`, or `is accepted under`.
- Keep `IPC-A-600K`, `IPC-6011A`, and addendum references attached to hierarchy and role separation, not to free technical criteria.

## Limits And Non-Claims

- This card does not provide `Class 2 / 3 / 3A` thresholds, sample sizes, acceptance tables, or technical criteria.
- It does not prove that any `22-layer` board is accepted, releasable, compliant, or approved under any addendum branch.
- It does not prove that `FAI`, `DMR`, or `DHR` records exist for any supplier, lot, or board family.
- It does not turn public hierarchy metadata into release authority or disposition authority.

## Open Questions

- Add a narrower follow-on card only if future work needs a separate boundary between bare-board acceptability and finished-device release workflow.
- Reassess `22-layer` readiness only after stronger public threshold handling or supplier-evidence layers exist.

## Source Links

- https://www.electronics.org/TOC/IPC-A-600K-EN_TOC.pdf
- https://www.electronics.org/TOC/IPC-6011A_TOC.pdf
- https://www.ipc.org/TOC/IPC-6012F-TOC.pdf
- https://www.electronics.org/news-release/ipc-releases-ipc-6012em-medical-applications-addendum-ipc-6012e-qualification-and
- https://shop.electronics.org/ipc-6012/ipc-6012-addendum/Revision-e/english-0
- https://shop.electronics.org/ipc-6012/ipc-6012-addendum/Revision-f/english-0
- https://www.electronics.org/TOC/IPC-6012FA-TOC.pdf
- https://shop.electronics.org/taxonomy/term/792
- https://www.electronics.org/TOC/IPC-6012FS_TOC.pdf
- https://saemobilus.sae.org/standards/as9102c-aerospace-series-first-article-inspection-requirements
- https://saemobilus.sae.org/standards/as9145-aerospace-series-requirements-advanced-product-quality-planning-production-part-approval-process
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.181
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.184
