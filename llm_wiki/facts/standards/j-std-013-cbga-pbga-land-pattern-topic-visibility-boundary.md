---
fact_id: "standards-j-std-013-cbga-pbga-land-pattern-topic-visibility-boundary"
title: "Public J-STD-013 TOC shows CBGA/PBGA land-pattern topic visibility, not reusable geometry criteria"
topic: "J-STD-013 CBGA/PBGA land-pattern topic visibility boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-12"
source_ids:
  - "j-std-013-toc"
  - "ipc-document-revision-table"
tags: ["ipc", "j-std-013", "cbga", "pbga", "land-pattern", "topic-visibility", "toc", "boundary"]
---

# Canonical Summary

> The public `J-STD-013` table of contents is strong enough to show that `CBGA` and `PBGA` land-pattern work exists as an explicit IPC standards topic, with publicly visible headings and figure-title labels such as `Land Pattern Comparisons`, `Solder Mask Defined Land Patterns for CBGA and PBGA`, and `Land Defined Land Patterns for CBGA and PBGA`, plus one visible `Variations - 1.50 Pitch` figure-list entry in package-details context. This improves standards-side topic visibility for the `1.50 mm` package lane. It does not expose geometry values, comparison criteria, or reusable land-pattern rules.

## Stable Facts

- Public IPC TOC access exists for `J-STD-013`.
- The public TOC visibly exposes `land pattern` as a standards topic for `CBGA` and `PBGA`.
- The public TOC visibly exposes topic-family headings including:
  - `Land Pattern Comparisons`
  - `Solder Mask Defined Land Patterns for CBGA and PBGA`
  - `Land Defined Land Patterns for CBGA and PBGA`
- The public TOC also visibly exposes figure-title labels including:
  - `Figure 4-3 Land Pattern Comparisons`
  - `Figure 5-2 Solder Mask Defined Land Patterns for CBGA and PBGA`
  - `Figure 5-3 Land Defined Land Patterns for CBGA and PBGA`
- The public TOC visibly includes one `Variations - 1.50 Pitch` entry in the BGA package-details figure list.
- The IPC revision table publicly marks `J-STD-013` as superseded by `IPC-7095`.
- The public TOC therefore gives the repo one stronger standards-side topic-discovery anchor than plain `BGA standard exists` wording alone.

## Conditions And Methods

- Use this card when a prompt needs to explain that public IPC material visibly treats `CBGA/PBGA land pattern` as a named standards topic.
- Pair this card with:
  - [bga-1p50mm-pitch-standards-existence-boundary.md](/code/blogs/llm_wiki/facts/methods/bga-1p50mm-pitch-standards-existence-boundary.md)
  - [ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md](/code/blogs/llm_wiki/facts/methods/ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md)
  - [jcet-pbga-family-pitch-availability-boundary.md](/code/blogs/llm_wiki/facts/methods/jcet-pbga-family-pitch-availability-boundary.md)
- Keep the safe reusable rule at:
  - public TOC = topic visibility
  - public TOC may expose figure-title visibility and named `1.50 Pitch` context
  - public TOC != geometry criteria
  - public TOC != exact replacement row

## Limits And Non-Claims

- This card does not provide `1.50 mm` land-pattern geometry.
- It does not provide `PBGA` or `CBGA` pad-diameter values.
- It does not provide solder-mask-opening values or package comparison results.
- It does not convert the visible `Variations - 1.50 Pitch` TOC entry into one public `1.50 mm` figure payload or geometry rule.
- It does not reopen the `1.50 mm` residual by itself.
- It does not exceed the current `IPC-hosted public geometry boundary` already landed in `P4-507`.

## Relationship To Local PCB资料 Intake

- This card adds one more public standards-side topic-visibility anchor above pure standards identity and family naming.
- It helps explain that `PBGA land pattern` is a real public standards topic and that the public TOC even reveals figure-title and `1.50 Pitch` topic visibility, while clause-level geometry remains non-public.
- It still does not convert the current `1.50 mm` residual into a public exact-geometry closure.

## Source Links

- https://www.ipc.org/TOC/J-STD-013.pdf
- https://www.ipc.org/ipc-document-revision-table
