---
fact_id: "standards-ipc-finish-standards-metadata"
title: "IPC finish-standard metadata for ENIG, immersion silver, immersion tin, and ENEPIG must be treated as dynamic revision data"
topic: "IPC finish standards metadata"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids:
  - "ipc-document-revision-table"
  - "ipc-4552b-toc"
  - "ipc-4553a-chinese-toc"
  - "ipc-4554-am1-toc"
  - "ipc-4556-toc"
  - "ipc-status-of-standardization"
tags: ["ipc", "surface-finish", "enig", "immersion-silver", "immersion-tin", "enepig", "revision-control"]
---

# Canonical Summary

> IPC finish-standard references should be handled as revision-controlled metadata unless the actual licensed standard text is available. The public IPC revision table is suitable for naming and revision-status checks; it is not sufficient for clause-level finish requirements.

## Stable Facts

- The public IPC revision table lists `IPC-4552 Specification for Electroless Nickel/Immersion Gold (ENIG) Plating for Printed Circuit Boards` as `Rev B 5/21` at the time of this review.
- The public IPC revision table lists `IPC-4553 Specification for Immersion Silver Plating for Printed Circuit Boards` as `No Longer Maintained`, with `Rev A 5/09` and original publication `6/05` shown in its history at the time of this review.
- The public IPC revision table lists `IPC-4554 Specification for Immersion Tin Plating for Printed Circuit Boards` as `No Longer Maintained`, with `Amend 1 9/11` and original publication `2/07` shown in its history at the time of this review.
- The public IPC revision table lists `IPC-4556 Specification for Electroless Nickel/Electroless Palladium/Immersion Gold (ENEPIG) Plating for Printed Circuit Boards` as `Rev A 7/25` at the time of this review.
- Public IPC table-of-contents PDFs can anchor document identity and section structure, but they do not replace the licensed standards.

## Conditions And Methods

- Use this fact card for revision metadata, source discovery, and pre-publish refresh checks.
- Use the IPC revision table as the primary public source for current status labels.
- Use TOC PDFs only as document-identity anchors unless the licensed standard text is available.
- Treat all revision labels and status labels as dynamic because IPC can revise, withdraw, replace, or update documents.

## Limits And Non-Claims

- This card does not state finish thickness, acceptance criteria, sampling rules, chemistry controls, defect criteria, or process limits.
- It does not reproduce IPC standard text.
- It does not prove whether your team has licensed access to the full standards.
- It does not mean `No Longer Maintained` documents are unusable in all customer contexts; it only records the public IPC status label visible at review time.

## Open Questions

- Confirm which IPC finish standards are licensed internally before extracting clause-level requirements.
- Re-check whether IPC publishes a newer public TOC for `IPC-4556 Rev A`.
- Decide whether `IPC-4555 OSP` should be added to the finish-standard metadata set.

## Source Links

- https://www.ipc.org/ipc-document-revision-table
- https://www.ipc.org/TOC/IPC-4552B-toc.pdf
- https://www.ipc.org/TOC/IPC-4553A-Chinese.pdf
- https://www.ipc.org/TOC/IPC-4554Am1.pdf
- https://www.ipc.org/TOC/IPC-4556.pdf
- https://www.ipc.org/Status
