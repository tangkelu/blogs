---
fact_id: "standards-edge-contact-gold-finger-standards-metadata-boundary"
title: "Gold fingers and edge contacts can cite IPC metadata, but public TOCs do not provide thickness or durability rules"
topic: "Edge contact gold finger standards metadata boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-28"
source_ids:
  - "ipc-document-revision-table"
  - "ipc-6012f-toc"
  - "ipc-a-600k-toc"
  - "ipc-4552b-toc"
  - "ipc-4556-toc"
  - "ipc-status-of-standardization"
tags: ["gold-finger", "edge-contact", "edge-connector", "hard-gold", "enig", "enepig", "ipc"]
---

# Canonical Summary

> Gold-finger and edge-contact articles may route to IPC rigid-board performance, acceptability, and finish-standard metadata. Public TOCs and revision tables do not authorize hard-gold thickness, nickel underplate, bevel angle, insertion-cycle life, contact resistance, or acceptance-threshold claims.

## Stable Facts

- `IPC-6012F` is the public TOC anchor for rigid printed-board qualification and performance metadata.
- `IPC-A-600K` is the public TOC anchor for printed-board acceptability structure and bare-board inspection vocabulary.
- `IPC-4552B` is the public TOC anchor for ENIG finish metadata.
- `IPC-4556` is the public TOC anchor for ENEPIG finish metadata.
- The IPC document revision table and status page are suitable for public revision / status discovery, not clause extraction.
- Existing finish-zoning data already supports guarded examples such as ENIG on SMD pads plus hard gold on edge fingers, but that internal routing is not a public thickness or durability rule.

## Conditions And Methods

- Use this fact for gold-finger, edge-contact, edge-connector, contact finish, edge tab, and selective-finish articles.
- Keep connector-zone finish choice, edge beveling, plating thickness, contact wear, electrical resistance, and inspection acceptance as separate evidence needs.
- Cite licensed IPC standard text, customer specifications, or dated process records before writing exact requirements.

## Limits And Non-Claims

- This card does not provide hard-gold thickness, nickel thickness, edge bevel angle, insertion cycles, contact resistance, insertion loss, solder-finish junction criteria, or class-specific acceptance values.
- It does not prove supplier capability for hard gold, selective finish, beveling, masking, continuity testing, or inspection.
- It does not prove telecom, GPU, memory, automotive, aerospace, or high-reliability connector qualification.

## Open Questions

- Recover licensed standard text, customer drawing requirements, or dated internal capability records if exact gold-finger requirements are needed.
- Add finish-chemistry vendor sources for hard-gold and connector finish selection if public product-level discussion is required.

## Source Links

- https://www.ipc.org/ipc-document-revision-table
- https://www.ipc.org/TOC/IPC-6012F-TOC.pdf
- https://www.electronics.org/TOC/IPC-A-600K-toc.pdf
- https://www.ipc.org/TOC/IPC-4552B-toc.pdf
- https://www.ipc.org/TOC/IPC-4556.pdf
- https://www.ipc.org/Status
