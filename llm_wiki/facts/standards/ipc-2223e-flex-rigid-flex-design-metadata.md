---
fact_id: "standards-ipc-2223e-flex-rigid-flex-design-metadata"
title: "IPC-2223E supports flex and rigid-flex design-standard vocabulary, not bend-life or supplier capability claims"
topic: "IPC-2223E flex and rigid-flex design metadata"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "ipc-2223e-flex-rigid-flex-design-standard-page"  # refreshed 2026-05-03
  - "ipc-6013e-toc"  # refreshed 2026-05-03
  - "ipc-document-revision-table"
tags: ["ipc-2223", "ipc-6013", "flex", "rigid-flex", "fpc", "design-standard", "metadata", "2025-10-20"]
---

# Canonical Summary

> `IPC-2223E` is a public IPC anchor for flexible and rigid-flexible printed-board design-standard vocabulary, while `IPC-6013E` remains the related flexible printed-board performance-specification anchor in this corpus. These public metadata sources support careful references to flex / rigid-flex design and performance-specification context, but they do not provide reusable bend-radius tables, bend-cycle limits, stackup rules, or supplier capability proof.

## Stable Facts

- IPC publicly identifies `IPC-2223E` as a sectional design standard for flexible and rigid-flexible printed boards.
- IPC publicly identifies `IPC-6013E` as a flexible printed-board qualification and performance-specification anchor.
- The IPC revision table is the refresh checkpoint for current IPC revision labels before publication.
- These sources are relevant to `2025.10.20` flex, FPC, bendable, dynamic-flex, rollable, foldable, and rigid-flex-adjacent blog topics.

## Conditions And Methods

- Use this card when a flex or rigid-flex blog needs standards-context language such as `design-standard context`, `performance-specification context`, or `IPC flex-board reference layer`.
- Keep design guidance generic unless a licensed standard, vendor design guide, or dated capability record supplies the exact rule.
- Pair this card with exact material cards such as `materials-dupont-kapton-hn`, `materials-ube-upilex-s`, or other vendor-controlled laminate sources before writing material-dependent design guidance.

## Limits And Non-Claims

- This card does not provide bend-radius values, bend-cycle counts, copper-type rules, adhesive / adhesiveless stackup rules, coverlay thickness, conductor geometry, via rules, or dynamic-flex lifetime thresholds.
- It does not prove that a specific flex, FPC, rollable, foldable, or rigid-flex build is compliant with IPC-2223E or IPC-6013E.
- It does not prove HILPCB, Highleap, or APTPCB capability, certification, production scale, yield, lead time, MOQ, stock, delivery, or quality performance.

## Open Questions

- Add official flex-laminate vendor design guides if future drafts require bend-radius, copper-type, adhesive-system, or coverlay-specific guidance.
- Add dated internal capability records if supplier-specific flex / FPC process windows or production claims are required.

## Source Links

- https://shop.electronics.org/ipc-2223/ipc-2223-standard-only/Revision-e/english
- https://www.ipc.org/TOC/IPC-6013E-EN_TOC.pdf
- https://www.ipc.org/ipc-document-revision-table
